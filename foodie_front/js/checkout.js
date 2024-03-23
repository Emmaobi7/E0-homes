const host4 = 'https://e0-homes-api.onrender.com';

async function test() {
    try {
        let price = 0;
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