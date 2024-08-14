const checkbox = document.getElementById("moderator");
const form = document.getElementById("reg-form");
const loginBtn = document.getElementById("login-btn");

let db = {};

form.addEventListener("submit", function(e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const isModerator = checkbox.checked;

    db["email"] = email;
    db["password"] = password;
    db["moderator"] = isModerator;
    console.log(db);

    alert("Successfully Registered");
});

const myFunc = () => {
    const emailLogin = document.getElementById("emailLogin").value;
    const passwordLogin = document.getElementById("passwordLogin").value;

    if (emailLogin === db["email"] && passwordLogin === db["password"]) {
        window.location.href = "main.html";
    } else {
        alert("Invalid login credentials");
    }
};

loginBtn.addEventListener("click", myFunc);


export { db };