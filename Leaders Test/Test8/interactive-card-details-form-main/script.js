const cardNumber = document.getElementById("cardNumber")
const cardName = document.getElementById("cardHolderName")
const cardDate = document.getElementById("cardDate")
const cardCvc = document.getElementById("cvcP")
const form = document.getElementById("myForm")


form.addEventListener("submit", (e) => {
    e.preventDefault();

    const cardNumP = form.cardNumInput.value
    const cardNameP = form.cardNameInput.value
    const cardMonthP = form.cardMonthInput.value
    const cardYearP = form.cardYearInput.value
    const cardCvcP = form.cardCvcInput.value

    cardNumber.innerHTML = cardNumP
    cardName.innerHTML = cardNameP
    cardDate.innerHTML = `${cardMonthP}/${cardYearP}`
    cardCvc.innerHTML = cardCvcP

    form.reset()
})