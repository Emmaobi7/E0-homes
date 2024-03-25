const host1 = 'https://e0-homes-api.onrender.com';
//const host1 = 'http://localhost:5000';

if (localStorage.getItem('userId')) {
  console.log('first')
  document.querySelector('.logout').innerHTML = `
  <button class="nav-link out" onclick="logout()" href="checkout.html">Logout</button>
  `
  document.getElementById('checkout-show').innerHTML = 'Checkout';
  
  document.getElementById('cart-show').innerHTML = `
  <a class="nav-link" href="javascript:void(0)" id="myBtn">Cart <i class="fa-solid fa-cart-shopping"><span id="cart-info"></span></i></a>
  `
} else {
  console.log('no user found')
  document.querySelector('.logout').innerHTML = `
  <button class="nav-link out" onclick="toAuth()" href="checkout.html">Sign up</button>
  `
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
if (localStorage.getItem('userId')) {
  btn.onclick = function() {
    modal.style.display = "block";
  }
}



// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}




async function getSix() {
  try {
    const response = await axios.get(`${host1}/api/v1/products/?page=1&per_page=6`)
    const data = response.data;
    let markup = ''
    data.map((item) => {
      markup += `
      <div class="col-lg-3 market-border">
              <button class="add-to-cart" onclick="add_to_cart(${item.id})">Add to cart</button>
              <a href="detail.html?id=${item.id}">
                  <img class="market-img" src="${item.image}" alt="furniture">
              </a>
              <a href="detail.html?id=${item.id}"><button class="add-to-cart">$${item.price}</button></a>
          </div>
      `;
    })

    document.querySelector('.dynamic-data').innerHTML = markup;
  } catch(err) {
    console.log(err)
  }
}


getSix();

function toAuth() {
  window.location.replace('./auth.html')
}



let date = new Date().getFullYear();
document.querySelector('.d').innerHTML = `copyright @${date}`

