const messages = [
    " Welcome",
    " I'm Mustafa Mohammed",
    " I'm Programmer",
    " I'm Python Developer",
    " Django Developer",
    " Flask Developer",
    " Node.js Developer",
];

let messageIndex = 0;
let letterIndex = 0;


function revealLetters() {
    const welcomeMessageElement = document.getElementById('welcome-message');

    // Get the current message based on the index
    const currentMessage = messages[messageIndex];

    // Reveal letters of the current message
    if (letterIndex <= currentMessage.length) {
        welcomeMessageElement.textContent = currentMessage.slice(0, letterIndex);
        letterIndex++;
        setTimeout(revealLetters, 100); // Adjust the speed here
    } else {
        // Move to the next message after the current one is fully displayed
        messageIndex++;
        letterIndex = 0;

        // Loop back to the first message if at the end
        if (messageIndex >= messages.length) {
            messageIndex = 0; // Reset to the first message
        }

        // Pause before the next message
        setTimeout(revealLetters, 600); // Adjust the pause duration here
    }
}

// Start revealing letters when the page loads
window.onload = revealLetters;