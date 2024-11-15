const password = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");

togglePassword.addEventListener("mousedown", function () {
    password.type = "text";
    togglePassword.src = "/frontend/assets/imgs/eye_icon.svg";
});

togglePassword.addEventListener("mouseup", function () {
    password.type = "password";
    togglePassword.src = "/frontend/assets/imgs/eye-off_icon.svg";
});

togglePassword.addEventListener("mouseleave", function () {
    password.type = "password";
    togglePassword.src = "/frontend/assets/imgs/eye-off_icon.svg";
});

const repeat_password = document.getElementById("repeat_password");
const togglePassword_2 = document.getElementById("togglePassword_2");

togglePassword_2.addEventListener("mousedown", function () {
    repeat_password.type = "text";
    togglePassword_2.src = "/frontend/assets/imgs/eye_icon.svg";
});

togglePassword_2.addEventListener("mouseup", function () {
    repeat_password.type = "password";
    togglePassword_2.src = "/frontend/assets/imgs/eye-off_icon.svg";
});

togglePassword_2.addEventListener("mouseleave", function () {
    repeat_password.type = "password";
    togglePassword_2.src = "/frontend/assets/imgs/eye-off_icon.svg";
});