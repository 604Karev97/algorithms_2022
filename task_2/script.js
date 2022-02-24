let divSecond = document.querySelector(".products"),
    products = {
        product1: ['banana.jpeg', 'Бананы', 50],
        product2: ['apple.jpg', 'Яблоки', 65],
        product3: ['pineapple.jpg', 'Ананасы', 100],
        product4: ['grape.jpg', 'Виноград', 95],
        product5: ['cherry.jpg', 'Вишня', 150],
        product6: ['strawberry.jpg', 'Клубника', 300],
        product7: ['orange.jpg', 'Апельсины', 40],

    };
btn = document.getElementById("btn");
cont = document.querySelector(".basket")
btn.addEventListener('click', () => {
    cont.classList.toggle("visibility");
})

for (let key in products) {
    let el = document.createElement('div'),
        img = document.createElement('img'),
        h3 = document.createElement('h3'),
        span = document.createElement('span'),
        button = document.createElement('button');

    el.className = 'product';
    img.src = 'images/' + products[key][0];
    h3.innerHTML = products[key][1];
    span.innerHTML = products[key][2];
    button.innerHTML = '+';
    el.innerHTML = img.outerHTML + h3.outerHTML + span.outerHTML;

    button.onclick = function(e) {
        let price = e.target.parentNode.querySelector('span').cloneNode(true),
            img = e.target.parentNode.querySelector('img').cloneNode(true),
            title = e.target.parentNode.querySelector('h3').cloneNode(true),
            el2 = document.querySelector('.basket'),
            div = document.createElement('div');
        div.className = 'basket_product';
        div.innerHTML += img.outerHTML + title.outerHTML + price.outerHTML;
        div.onclick = function() {
            div.remove();
            total();
        };
        el2.prepend(div);
        total();
    };
    el.append(button);
    divSecond.append(el);
}

function total() {
    let el = document.querySelector('.subtotal h2'),
        price = document.querySelectorAll('.basket .basket_product span'),
        total = 0;
    for (let i = 0; i <= price.length - 1; i++) {
        total += +price[i].innerHTML;
    }
    el.innerHTML = 'Итог: ' + total.toFixed(2);
}