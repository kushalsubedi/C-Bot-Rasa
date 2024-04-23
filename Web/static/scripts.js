function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    appendMessage("user", userInput);
    document.getElementById("user-input").value = "";

    fetch('/api/parse', { // Send request to Flask server
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_message: userInput
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display Flask server response
        data.forEach(response => {
            appendMessage("bot", response.text);
        });
    })
    .catch(error => console.error('Error:', error));
}


function appendMessage(sender, message) {
    var chatContent = document.getElementById("chat-content");
    var messageElement = document.createElement("div");
    messageElement.className = sender;
    messageElement.innerHTML = message;
    chatContent.appendChild(messageElement);
    chatContent.scrollTop = chatContent.scrollHeight;
}
