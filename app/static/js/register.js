//static/js/register.js

async function registerUser(event) {
    event.preventDefault();
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirm_password').value

    if(password !== confirm_password){
        showToast("Passwords do not match","error")
        return
    }else{
        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: document.getElementById("username").value,
                password: password,
            })
        });

        const data = await response.json();

        sessionStorage.setItem("toastMessage", data.message);
        sessionStorage.setItem("toastType", data.state);
        window.location.href = data.redirect;
    }
}