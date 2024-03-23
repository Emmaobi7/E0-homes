const host1 = 'https://e0-homes-api.onrender.com';

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
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

if (localStorage.getItem('userId')) {
  document.querySelector('.logout').innerHTML = `
  <button class="nav-link out" onclick="logout()" href="checkout.html">Logout</button>
  `
} else {
  document.querySelector('.logout').innerHTML = `
  <button class="nav-link out" onclick="toAuth()" href="checkout.html">Sign up</button>
  `
}

