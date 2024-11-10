const regForm = document.getElementById("regForm")
const regBtn = document.getElementById("regBtn")
const emailError = document.getElementById("email-error")
const passwordError = document.getElementById("password-error")

const db = []

regBtn.addEventListener("click", function(){
    const email = regForm.elements.email.value
    const password = regForm.elements.password.value
    const admin = regForm.elements.admin.value

    if(email.length < 8){
        emailError.style.color = "red"
        emailError.textContent = "email too short"

    }else if(password.length < 5){
        passwordError.style.color = "red"
        passwordError.textContent = "password too short"

    }else{
        emailError.textContent = ""
        passwordError.textContent = ""

        db.push(email)
        db.push(password)
        db.push(admin)

        console.log(db)
    
        regForm.elements.email.value = ""
        regForm.elements.password.value = ""
        regForm.elements.admin.value = ""


        document.body.innerHTML = `
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav>
        <p id="nav-p">Ivan</p>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">Reviews</a></li>
            <li><a href="../Register/index.html">Registration</a></li>
            <li><a href="#">Login</a></li>
        </ul>
        <button class="nav-btn">Join Waitlist</button>
    </nav>

    <main id="login-main">
        <div id="main-div">
            <p id="slogan">"Invest in tomorrow<br>because the future is built today."</p>    

            <form id="logForm">
                <h2 class="form-h2">Log In:</h2>
                <div class="input-div">
                    <label for="email-input">Enter your email:</label>
                    <input type="email" name="logEmail" id="email-input" placeholder="example@gmail.com">
                    <span id="email-error"></span>
                </div>

                <div class="input-div">
                    <label for="password-input">Enter your password:</label>
                    <input type="password" name="logPassword" id="password-input" placeholder="Password!123">
                    <span id="password-error"></span>
                </div>

                <button id="logBtn" type="button" class="nav-btn">Login</button>
            </form>
        </div>
    </main>





    <script src="script.js"></script>
</body>
</html>`

    const loginBtn = document.getElementById("logBtn")
    const logForm = document.getElementById("logForm")

    loginBtn.addEventListener("click",function(){
        loginEmail = logForm.elements.logEmail.value
        loginPassword = logForm.elements.logPassword.value

        if(loginEmail == db[0] && loginPassword == db[1]) {
            document.body.innerHTML = `
            <!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="home.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav>
        <p id="nav-p">Ivan</p>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">Reviews</a></li>
            <li><a href="../Register/index.html">Registration</a></li>
            <li><a href="#">Login</a></li>
        </ul>
        <button class="nav-btn">Join Waitlist</button>
    </nav>

    <div id="home-bg">
        <p id="hello-p"></p>
    </div>
</body>
</html>
            `
        }

        
        
    })
}
})
