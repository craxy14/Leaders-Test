const form = document.getElementById("myForm");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const user = {
        username: form.username.value,
        email: form.email.value,
        password: form.password.value,
    };

    localStorage.setItem("Users", JSON.stringify(user))
    window.location.href = "./login.html"
});
