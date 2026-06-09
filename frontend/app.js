const API_URL = "http://127.0.0.1:8000/chat";

// Send message on Enter key
document.getElementById("userInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
});

function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    
    if (!message) return;

    // Show user message in chat
    appendMessage(message, "user");
    input.value = "";

    // Disable send button while waiting
    document.getElementById("sendBtn").disabled = true;

    // Show typing indicator
    const typingId = showTyping();

    // Call FastAPI backend
    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        // Remove typing indicator
        removeTyping(typingId);

        // Show bot response
        appendMessage(data.response, "bot");

        // Show which agent handled it
        showIntent(data.intent);

        // Re-enable send button
        document.getElementById("sendBtn").disabled = false;
    })
    .catch(err => {
        removeTyping(typingId);
        appendMessage("Sorry, I'm having trouble connecting. Please try again.", "bot");
        document.getElementById("sendBtn").disabled = false;
    });
}

function appendMessage(text, sender) {
    const messages = document.getElementById("chatMessages");
    
    const div = document.createElement("div");
    div.className = `message ${sender === "bot" ? "bot-message" : "user-message"}`;
    
    const bubble = document.createElement("div");
    bubble.className = "message-bubble";
    bubble.innerHTML = text.replace(/\n/g, "<br>");
    
    div.appendChild(bubble);
    messages.appendChild(div);
    
    // Auto scroll to bottom
    messages.scrollTop = messages.scrollHeight;
}

function showTyping() {
    const messages = document.getElementById("chatMessages");
    const id = "typing-" + Date.now();
    
    const div = document.createElement("div");
    div.className = "message bot-message typing";
    div.id = id;
    
    const bubble = document.createElement("div");
    bubble.className = "message-bubble";
    bubble.textContent = "AI is thinking...";
    
    div.appendChild(bubble);
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    
    return id;
}

function removeTyping(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}

function showIntent(intent) {
    const bar = document.getElementById("intentBar");
    const label = document.getElementById("intentLabel");
    
    bar.style.display = "block";
    label.textContent = intent;
    label.className = `intent-${intent}`;
}