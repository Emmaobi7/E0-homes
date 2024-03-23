const host2 = 'https://e0-homes-api.onrender.com';
let cartCount = 0;

async function add_to_cart (productId) {
    try{
        const options = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const data = {
            product_id: productId,
            user_id: localStorage.getItem('userId')
        };
        const response = await axios.post(`${host2}/api/v1/add_to_cart`, data, options)
        const product = response.data;
        cartCount = cartCount + 1
        document.querySelector('#cart-info').innerHTML = cartCount
        updateCart(product.message);
    } catch(err) {
        console.log(err)
    }
}



async function updateCart(id) {
    const response = await axios.get(`${host2}/api/v1/products/${id}`);
    const data = response.data;
    
    const existingItems = document.querySelector('.cart-data').innerHTML;
    
    const newItemMarkup = `
    
        <div class="cart-item">
            <div>${data.title}</div>
            <div>$${data.price}</div>
        </div>
    `;

    const updatedMarkup = existingItems + newItemMarkup;
    
    document.querySelector('.cart-data').innerHTML = updatedMarkup;
}

async function loadCartData() {
    try {
  
      const response = await axios.get(`${host2}/api/v1/get-cart/${localStorage.getItem('userId')}`)
      const data = response.data;
      const lastElements = data.map(array => array[array.length - 1]);
      lastElements.map( async (id) => {
        cartCount = cartCount +1;
        document.querySelector('#cart-info').innerHTML = cartCount;
        const response_data = await axios.get(`${host2}/api/v1/products/${id}`);
        const cartData = response_data.data;
  
        const existingItems = document.querySelector('.cart-data').innerHTML;
      
        const newItemMarkup = `
            <div class="cart-item">
            <span class="remove-cart"" data-product-id="${id}">&times;</span>
                <div c>${cartData.title}</div>
                <div>$${cartData.price}</div>
            </div>
        `;
    
        const updatedMarkup = existingItems + newItemMarkup;
        
        document.querySelector('.cart-data').innerHTML = updatedMarkup;

        const removeButtons = document.querySelectorAll('.remove-cart');
            removeButtons.forEach(button => {
                button.addEventListener('click', async function() {
                    const productId = button.getAttribute('data-product-id');
                    cartCount = cartCount - 1;
                    document.querySelector('#cart-info').innerHTML = cartCount;
                    button.closest('.cart-item').style.display = 'none';
                    const res = await axios.get(`${host2}/api/v1/delete_cart/${productId}`);
                    return res.status;
                });
      });
    });
     
    } catch(err) {
      console.log(err)
    }
  
  }
  
loadCartData()


async function toCheckout(productId) {
    await add_to_cart(productId);
    window.location.href = "./checkout.html";
}


async function getOne(productId) {
    console.log(productId)
    try {
        const response = await axios.get(`${host2}/api/v1/products/${productId}`);
        const data = response.data;
        let markup = `
            <div class="row">
                <div class="col-lg-4 margin">
                    <img src="${data.image}" alt="furniture image" class="desc-img">
                </div>
                <div class="col-lg-8 btn-list">
                <div class="btnflex">
                    <button type="submit" class="cta buy" onclick="toCheckout(${[productId]})">BUY NOW</button>
                    <button type="submit" class="cta cart" onclick="add_to_cart(${[productId]})">ADD TO CART</button>
                </div>
                    <h4 class="spec-title">${data.name}</h4>
                    <ul class="desc-list">
                        <li>Single couch.</li>
                        <li>Beautiful brown.</li>
                        <li>Wooden.</li>
                        <li>Home and Office.</li>
                    </ul>
                </div>
            </div>
            <hr>
            <div class="row">
                <div class="col-lg-6">
                    <div id=""><h5 class="desc-ttext">DESCRIPTION</h5></div>
                    <p class="desc">${data.description}</p>
                </div>
            </div>
        `;
        document.querySelector('.dynamic-single-data').innerHTML = markup;
    } catch(err) {
        console.error(err);
    }
}


document.addEventListener("DOMContentLoaded", function() {
    // Function to get URL parameters
    const getUrlParameter = name => {
        name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
        const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
        const results = regex.exec(location.search);
        return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
    };

    // Get the product ID from the URL query parameter
    const productId = getUrlParameter('id');

    // Call the getOne function with the retrieved product ID
    getOne(productId);
});
