function setupPasswordToggle(passwordFieldId, toggleButtonId) {
    const passwordField = document.getElementById(passwordFieldId);
    const toggleButton = document.getElementById(toggleButtonId);

    if (passwordField && toggleButton) {
        // Get the image URLs from data attributes
        const eyeIcon = toggleButton.dataset.eyeIcon;
        const eyeOffIcon = toggleButton.dataset.eyeOffIcon;

        toggleButton.addEventListener("mousedown", function () {
            passwordField.type = "text";
            toggleButton.src = eyeIcon;
        });

        toggleButton.addEventListener("mouseup", function () {
            passwordField.type = "password";
            toggleButton.src = eyeOffIcon;
        });

        toggleButton.addEventListener("mouseleave", function () {
            passwordField.type = "password";
            toggleButton.src = eyeOffIcon;
        });
    }
}

// For the first password field
setupPasswordToggle("password", "togglePassword");

// For the repeat password field, if present
setupPasswordToggle("repeat_password", "togglePassword_2");
