const host4 = 'https://e0-homes-api.onrender.com';
//const host4 = 'http://localhost:5000';
let price = 0;
async function test() {
    try {
      
        let cartN = 0;
      const response = await axios.get(`${host4}/api/v1/get-cart/${localStorage.getItem('userId')}`)
      const data = response.data;
      const lastElements = data.map(array => array[array.length - 1]);
      lastElements.map( async (id) => {
        cartN = cartN + 1;
        const response_data = await axios.get(`${host4}/api/v1/products/${id}`);
        const cartData = response_data.data;
  
        const existingItems = document.querySelector('.all-cart').innerHTML;
      
        const newItemMarkup = `
        <p>${cartData.title}<span class="price">$${cartData.price}</span></p>
        `;
        price = price + cartData.price;
        document.querySelector('.real').innerHTML = `$${price}`;
    
        const updatedMarkup = existingItems + newItemMarkup;
        
        document.querySelector('.all-cart').innerHTML = updatedMarkup;
      });
     
    } catch(err) {
      console.log(err)
    }
  }

test();


let checkoutForm = document.getElementById('checkout-form')

let newWindow;
let handleCheckout = async function onCheckout(e) {
  e.preventDefault();
  const loginData = new FormData(e.target)
  const data = {
    email: loginData.get('email'),
    amount: price
  }
  const submitButton = e.target.querySelector('#checkout-btn');
  submitButton.disabled = true;
  submitButton.value = 'Processing...'
  try {
    const options = {headers: { 'Content-Type': 'application/json'  }};
    const response = await axios.post(`${host4}/api/v1/payment`, data, options)
    const authorizationUrl = response.data.data.data.authorization_url;
    reference = response.data.data.data.reference;
    console.log(`i am ${reference}`)
    console.log(authorizationUrl)

    newWindow = window.open(authorizationUrl, '_blank');
    if (reference) {
      await verify(reference)
    }



  } catch(err) {
    console.log(err)
  }
}

checkoutForm.addEventListener('submit', handleCheckout)

async function verify(reference) {
  const options = { headers: { 'Content-Type': 'application/json' } };
  const data = { reference: reference };
  try {
    let response;
    let maxCall = 0;
    do {
      response = await axios.post(`${host4}/api/v1/verify_payment`, data, options);
      console.log(response.data.data.data.gateway_response);
      if (response.data.data.data.gateway_response !== 'Successful') {
        await new Promise(resolve => setTimeout(resolve, 5000));
        maxCall += 1;
      }
      if (maxCall >= 100) {
        newWindow.close();
        logout();
        return 
       }
    } while (response.data.data.data.gateway_response !== 'Successful');
    let user_Id = localStorage.getItem('userId');
    const id = await getCartId(user_Id)
    const delRes = await axios.get(`${host4}/api/v1/delete-all_cart/${id}`)
    console.log(delRes)

  } catch (err) {
    console.log(err);
  }
}


async function getCartId(user_Id) {
  try {
    const response = await axios.get(`${host4}/api/v1/get_cart_id/${user_Id}`);
    return response.data;
  } catch(err) {
    console.log(err)
  }
}
