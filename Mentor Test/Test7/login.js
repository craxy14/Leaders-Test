const form = document.getElementById("myForm")

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const user = {
        login_email: form.email.value,
        login_password: form.password.value
    }

    const storedUsers = JSON.parse(localStorage.getItem("Users"));

    if (storedUsers) {
        if (user.login_email == storedUsers.email && user.login_password == storedUsers.password) {
            console.log("hello");
            window.location.href = "./home.html"
        } else {
            alert("Invalid login credentials");
        }
    } else {
        console.log("No users found in localStorage.");
    }
});
