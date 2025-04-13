const cartDiv = document.getElementById("shoppingCartDiv");
const buyBtn = document.getElementsByClassName("buyNowBtn");
const sumP = document.getElementById("priceSumP");
const itemRemoveBtn = document.getElementsByClassName("itemRemoveBtn")

for (let i = 0; i < itemRemoveBtn.length; i++){
    itemRemoveBtn[i].addEventListener("click", (e) => {
        e.target.parentElement.remove()
    })
}

let priceSum = 0;
let cartItems = JSON.parse(localStorage.getItem("Cart")) || [];

cartItems.forEach(item => {
    addToCart(item.name, item.price);
    priceSum += parseFloat(item.price.slice(8,));
});

sumP.innerHTML = priceSum.toFixed(2);

for (let i = 0; i < buyBtn.length; i++) {
    buyBtn[i].addEventListener("click", (e) => {
        const productDiv = e.target.parentElement;
        const productName = productDiv.querySelector(".productName").innerText;
        const productPrice = productDiv.querySelector(".productPrice").innerText;

        const priceValue = parseFloat(productPrice.slice(8,));
        console.log(priceValue)
        priceSum += priceValue;
        sumP.innerHTML = priceSum.toFixed(2);

        const product = { name: productName, price: productPrice };
        cartItems.push(product);
        localStorage.setItem("Cart", JSON.stringify(cartItems));

        addToCart(productName, productPrice);
    });
}

function addToCart(name, price) {
    const productDiv = document.createElement("div");
    productDiv.className = "cartProductDiv";

    const nameP = document.createElement("p");
    nameP.textContent = name;

    const priceP = document.createElement("p");
    priceP.textContent = price;

    const removeBtn = document.createElement("button");
    removeBtn.textContent = "Remove";
    removeBtn.className = "removeBtn";

    removeBtn.addEventListener("click", () => {
        const priceValue = parseFloat(productPrice.slice(8,))
        priceSum -= priceValue;
        sumP.innerHTML = priceSum.toFixed(2);

        cartItems = cartItems.filter(item => !(item.name === name && item.price === price));
        localStorage.setItem("Cart", JSON.stringify(cartItems));

        productDiv.remove();
    });

    productDiv.appendChild(nameP);
    productDiv.appendChild(priceP);
    productDiv.appendChild(removeBtn);

    cartDiv.appendChild(productDiv);
}
