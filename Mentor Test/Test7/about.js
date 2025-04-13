const clock = document.getElementById("clock")
const date = document.getElementById("date")

function updateClock() {
    let now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    let days = now.getDate();
    let month = now.getMonth();
    let year = now.getFullYear();

    hours = hours < 10 ? '0' + hours : hours;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    clock.innerHTML = hours + ':' + minutes + ':' + seconds;
    date.innerHTML = days + "/" + month + "/" + year
}

setInterval(updateClock, 1000);

updateClock();