//static/js/login.js

async function loginUser(event) {
    event.preventDefault();

    try{
    const response = await fetch("/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    });

    const button = document.querySelector(".login-button");
    button.disabled = true;
    
    const data = await response.json();

    button.disabled = false;
    
    if (data.state === "success") {
        sessionStorage.setItem("toastMessage", data.message);
        sessionStorage.setItem("toastType", data.state);
        window.location.href = data.redirect;
    } else {
        showToast(data.message, data.state)
    }

} catch(error){
    showToast("Network error. Please Try again.", "danger");
}
}



