function validateForm() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let errorMsg = document.getElementById("error-msg");

    if (username === "" || password === "") {
        errorMsg.textContent = "All fields are required";
        return false;
    }

    if (password.length < 4) {
        errorMsg.textContent = "Password must be at least 4 characters";
        return false;
    }

    return true;
}
