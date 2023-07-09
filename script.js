function generateText() {
    var prompt = document.getElementById("prompt").value;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.generated_text;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
