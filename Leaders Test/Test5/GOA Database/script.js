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
    
    if (emailLogin === db["email"] && passwordLogin === db["password"] && db["moderator"] == true) {
        document.body.innerHTML = `
        <!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://kit.fontawesome.com/0e8e964837.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="group0.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<nav>
<ul>
    <div class="socials-nav">
        <a href="https://discord.com/"><i class="fa-brands fa-discord"></i></a>
            <a href="https://www.facebook.com/nika11keshelava"><i class="fa-brands fa-facebook"></i></a>
            </div>
                <h3><a href="./index.html">GOA Database</a></h3>
            
            <div class="socials-nav">
                <a href="https://github.com/craxy14"><i class="fa-brands fa-github"></i></a>
                <a href="https://www.instagram.com/goal_oriented_academy__goa/"><i class="fa-brands fa-instagram"></i></a>
            </div>
            </ul>
        </nav>

    <table contenteditable="true" border="1">
        <tr>
            <th>Students Fullname</th>
            <th>Students Facebook</th>
            <th>Students Age</th>
            <th>Parents Fullname</th>
            <th>Parents Facebook</th>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Sandro Zabakhidze</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>39</td>
            <td>Davit Zabakhidze</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Nika Kvaracxelia</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>41</td>
            <td>Giorgi Kvaracxelia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Nikoloz Nutsubidze</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>23</td>
            <td>Luka Nutsubidze</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Aleqsandre Jimshiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>35</td>
            <td>Giorgi Jimshiashvili</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Sandro Zabakhidze</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>39</td>
            <td>Davit Zabakhidze</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Nika Kvaracxelia</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>41</td>
            <td>Giorgi Kvaracxelia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>


        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>


    </table>

    <p id="db-role-p">You are: ${db["moderator"] == true ? "Moderator" : "Viewer"}, You can edit the Values</p>


</body>
</html>
        
        `
    } else if(emailLogin === db["email"] && passwordLogin === db["password"] && db["moderator"] == false){
        document.body.innerHTML = `
        <!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://kit.fontawesome.com/0e8e964837.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="group0.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <nav>
        <ul>
            <div class="socials-nav">
                <a href="https://discord.com/"><i class="fa-brands fa-discord"></i></a>
                <a href="https://www.facebook.com/nika11keshelava"><i class="fa-brands fa-facebook"></i></a>
            </div>
            
            <h3><a href="./index.html">GOA Database</a></h3>
            
            <div class="socials-nav">
                <a href="https://github.com/craxy14"><i class="fa-brands fa-github"></i></a>
                <a href="https://www.instagram.com/goal_oriented_academy__goa/"><i class="fa-brands fa-instagram"></i></a>
            </div>
        </ul>
    </nav>

    <table border="1">
        <tr>
            <th>Students Fullname</th>
            <th>Students Facebook</th>
            <th>Students Age</th>
            <th>Parents Fullname</th>
            <th>Parents Facebook</th>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Sandro Zabakhidze</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>39</td>
            <td>Davit Zabakhidze</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Nika Kvaracxelia</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>41</td>
            <td>Giorgi Kvaracxelia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Nikoloz Nutsubidze</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>23</td>
            <td>Luka Nutsubidze</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Aleqsandre Jimshiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>35</td>
            <td>Giorgi Jimshiashvili</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Sandro Zabakhidze</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>39</td>
            <td>Davit Zabakhidze</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>

        <tr>
            <td>Nika Kvaracxelia</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>41</td>
            <td>Giorgi Kvaracxelia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>


        <tr>
            <td>Vano Motiashvili</td>
            <td><a href="https://www.facebook.com/vano.motiashvili">Facebook</a></td>
            <td>17</td>
            <td>Eka Tsulaia</td>
            <td><a href="https://www.facebook.com/avto.skola.auto.school">Facebook</a></td>
        </tr>
    </table>


</body>
</html>
        `
    }
};

loginBtn.addEventListener("click", myFunc);