document.getElementById("scanBtn").addEventListener("click", async () => {
    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });
    const url = tab.url;
    document.getElementById("result").innerHTML = "Scanning...";
    try {
        const response = await fetch("http://127.0.0.1:5000/predict-url", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        });
        const data = await response.json();
        if(data.phishing){
            document.getElementById("result").innerHTML =
                `⚠️ Phishing Website <br> Risk Score: ${data.score}%`;
        }
        else{
            document.getElementById("result").innerHTML =
                `✅ Legitimate Website <br> Confident: ${data.score}%`;
        }
    } catch(error){
        document.getElementById("result").innerHTML =
            "Server Error";

        console.log(error);
    }
});