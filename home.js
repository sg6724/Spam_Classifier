// Optional: Add interactivity or client-side validation if needed
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const emailMessage = document.getElementById("email_message");

    form.addEventListener("submit", (e) => {
        if (!emailMessage.value.trim()) {
            e.preventDefault();
            alert("Please enter a valid email message.");
        }
    });
});