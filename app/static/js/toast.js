//static/js/toast.js

let toastTimeout;

function showToast(message, type="default") {
    const toast = document.getElementById("toast");
    if (!toast) return;

    clearTimeout(toastTimeout);
    toast.textContent = message;

    if (type === "success") {
        toast.style.background = "green";
    } else if (type === "danger") {
        toast.style.background = "red";
    } else {
        toast.style.background = "blue";
    }

    toast.style.opacity = "1";

    toastTimeout = setTimeout(() => {
        toast.style.opacity = "0";
    }, 2000);
}