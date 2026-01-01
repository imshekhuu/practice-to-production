function validateRegister() {
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirm = document.getElementById("confirm_password").value;
    let errorMsg = document.getElementById("error-msg");

    if (!username || !email || !password || !confirm) {
        errorMsg.textContent = "All fields are required";
        return false;
    }

    if (password.length < 4) {
        errorMsg.textContent = "Password must be at least 4 characters";
        return false;
    }

    if (password !== confirm) {
        errorMsg.textContent = "Passwords do not match";
        return false;
    }

    return true;
}
