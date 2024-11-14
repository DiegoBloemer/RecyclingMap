const password = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");

togglePassoword.addEventListener("mousedown", function () {
    password.type = "text";
    togglePassoword.src = "/frontend/assets/imgs/eye_icon.svg";
});

togglePassoword.addEventListener("mouseup", function () {
    password.type = "password";
    togglePassoword.src = "/frontend/assets/imgs/eye-off_icon.svg";
});

togglePassoword.addEventListener("mouseleave", function () {
    password.type = "password";
    togglePassoword.src = "/frontend/assets/imgs/eye-off_icon.svg";
});