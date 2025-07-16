const renderDiv = document.getElementById("renderDiv")
const bookingsResP = document.getElementById("bookingsResP")

const bookings = JSON.parse(localStorage.getItem("Bookings")) || [];

if(bookings.length === 0) {
    bookingsResP.innerHTML = "No Bookings!"
    bookingsResP.style.color = "red"
}else{
    bookingsResP.innerHTML = `You Currently Have ${bookings.length} Bookings:`
    bookingsResP.style.color = "green"

    renderDiv.innerHTML = ""

    bookings.forEach(curVal => {
        renderDiv.innerHTML += `
        <div class="bookedDiv">
            <p class="bookedInfo">Name: ${curVal.name}</p>
            <p class="bookedInfo">Location: ${curVal.location}</p>
            <p class="bookedInfo">People: ${curVal.people}</p>
            <p class="bookedInfo">Start Date: ${curVal.startDate}</p>
            <p class="bookedInfo">End Date: ${curVal.endDate}</p>
        </div>
        `
    });
}