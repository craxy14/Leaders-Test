const form = document.getElementById("myForm")
const resultP = document.getElementById("resultP")

const bookingsArr = []


form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = form.name.value
    const location = form.location.value
    const people = form.people.value
    const startDate = form.startDate.value
    const endDate = form.endDate.value

    if(formValidation(startDate, endDate)){
        bookingsArr.push({name, location, people, startDate, endDate})
        localStorage.setItem("Bookings", JSON.stringify(bookingsArr))
        form.reset();
    }
})



const formValidation = (startDate, endDate) => {
    const splitedStart = startDate.split("-")
    const splitedEnd = endDate.split("-")

    if(Number(splitedEnd[0]) - Number(splitedStart[0]) >= 0){
        resultP.innerHTML = "Sucesfully Booked!"
        resultP.style.color = "green"
        return true
    }else{
        resultP.innerHTML = "Wrong Date!"
        resultP.style.color = "red"
        return;
    }
}