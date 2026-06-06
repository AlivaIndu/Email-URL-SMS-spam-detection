from flask import Flask,render_template,request, jsonify
from urllib.parse import urlparse
from flask_cors import CORS
import pickle
import random
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from urllib.parse import urlparse

nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

app = Flask(__name__)
CORS(app)

model = pickle.load(open('phishing.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

sms_model = pickle.load(open('sms_model.pkl','rb'))
sms_vectorizer = pickle.load(open('sms_vectorizer.pkl', 'rb'))

def process(text):
    nopunc = [
        char for char in text
        if char not in string.punctuation
    ]

    nopunc = ''.join(nopunc)

    clean = [
        word for word in nopunc.split()
        if word.lower() not in stop_words
    ]

    return clean

email_model = pickle.load(open('email_model.pkl','rb'))
email_vectorizer = pickle.load(open('email_vectorizer.pkl', 'rb'))

trusted_domains = [
    # Search / Tech
    "google.com",
    "microsoft.com",
    "apple.com",
    "openai.com",
    "adobe.com",
    "intel.com",
    "ibm.com",
    "oracle.com",
    "nvidia.com",

    # Social Media
    "facebook.com",
    "instagram.com",
    "linkedin.com",
    "twitter.com",
    "x.com",
    "snapchat.com",
    "reddit.com",
    "discord.com",
    "whatsapp.com",
    "telegram.org",

    # Video / Streaming
    "youtube.com",
    "netflix.com",
    "spotify.com",
    "primevideo.com",

    # Shopping / E-commerce
    "amazon.com",
    "flipkart.com",
    "myntra.com",
    "ebay.com",

    # Payment / Finance
    "paypal.com",
    "visa.com",
    "mastercard.com",
    "stripe.com",
    "paytm.com",
    "phonepe.com",

    # Developer Platforms
    "github.com",
    "gitlab.com",
    "stackoverflow.com",

    # Email / Productivity
    "gmail.com",
    "outlook.com",
    "zoom.us",
    "notion.so",
    "dropbox.com",

    # Education
    "coursera.org",
    "udemy.com",
    "edx.org",
    "wikipedia.org",

    # Government / Security
    "ac.in",
    "edu.in",
    "org.in",
    "gov.in",
    "nic.in"
]
def transform_text(text):
    text = str(text).lower()

    tokens = nltk.word_tokenize(text)

    filtered = []

    for token in tokens:
        if (
            token.isalnum()
            or "http" in token
            or "." in token
        ):

            if (
                token not in stop_words
                and token not in string.punctuation
            ):
                filtered.append(ps.stem(token))

    return " ".join(filtered)

def is_valid_url(url):

    try:
        parsed = urlparse(url)

        # only allow real protocols
        if parsed.scheme not in ["http", "https"]:
            return False

        # must contain domain
        if not parsed.netloc:
            return False

        # domain should contain dot
        if "." not in parsed.netloc:
            return False

        return True

    except:
        return False

@app.route("/",methods=['GET'])
def home():
    return render_template("Index.html")

@app.route("/predict-url", methods=['POST'])
def predict_url():

    data = request.json
    url = data['url'].strip()
    print("INPUT URL:", url)

    if not is_valid_url(url):
        print("INVALID URL")
        return jsonify({
            "valid": False,
            "message": "Invalid URL format"
        })
    print("VALID URL")

    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.lower()

    if domain_name.startswith("www."):
        domain_name = domain_name[4:]

    for domain in trusted_domains:
        if domain == domain_name or domain_name.endswith("." + domain):
            random_score = round(random.uniform(87, 94), 2)
            return jsonify({
                "valid": True,
                "phishing": False,
                "score": random_score,
                "recommendedActions": [
                    "Trusted domain detected",
                    "Website appears safe"
                ]
            })

    # Convert URL into vector
    vector = vectorizer.transform([url])

    # Predict
    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    # Confidence score
    confidence = round(max(probability) * 100, 2)

    # Response
    if prediction == "bad":

        return jsonify({
            "valid": True,
            "phishing": True,
            "score": confidence,
            "recommendedActions": [
                "Avoid opening the link",
                "Do not enter credentials",
                "Report suspicious website"
            ]
        })

    else:

        return jsonify({
            "valid": True,
            "phishing": False,
            "score": confidence,
            "recommendedActions": [
                "Website appears safe",
                "No phishing indicators found"
            ]
        })
    
@app.route("/predict-sms", methods=['POST'])
def predict_text():

    data = request.json
    text_input = data.get('message', '')

    transformed = transform_text(text_input)

    vector = sms_vectorizer.transform([transformed])

    prediction = sms_model.predict(vector)[0]

    probability = sms_model.predict_proba(vector)[0]
    confidence = round(max(probability) * 100, 2)

    print("RAW:", text_input)
    print("TRANSFORMED:", transformed)
    print("PREDICTION:", prediction)

    if prediction == 1:
        return jsonify({
            "phishing": True,
            "score": confidence,
            "recommendedActions": [
                "Avoid clicking suspicious links",
                "Do not share passwords or OTPs",
                "Verify sender authenticity"
            ]
        })

    else:
        return jsonify({
            "phishing": False,
            "score": confidence,
            "recommendedActions": [
                "Message appears legitimate",
                "No phishing indicators detected"
            ]
        })
    
@app.route("/predict-email", methods=['POST'])
def predict_email():
    data = request.json
    text_input = data.get('message', '')

    vector = email_vectorizer.transform([text_input])
    prediction = email_model.predict(vector)[0]
    probability = email_model.predict_proba(vector)[0]
    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        return jsonify({
            "phishing": True,
            "score": confidence,
            "recommendedActions": [
                "Avoid clicking suspicious links",
                "Do not share passwords or OTPs",
                "Verify sender authenticity"
            ]
        })

    else:
        return jsonify({
            "phishing": False,
            "score": confidence,
            "recommendedActions": [
                "Email appears legitimate",
                "No phishing indicators detected"
            ]
        })
    
    
if __name__=="__main__":
    app.run(debug=True)
