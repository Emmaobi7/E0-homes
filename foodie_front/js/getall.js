const host3 = 'https://e0-homes-api.onrender.com';
//const host3 = 'http://localhost:5000';

async function marketData () {
    try {
        const response = await axios.get(`${host3}/api/v1/products`)
        const data = response.data;
        let markup =  ''
        data.map((item) => {
            markup += `
            <div class="col-lg-2 market-border">
                    <button class="add-to-cart" onclick="add_to_cart(${item.id})">Add to cart</button>
                    <a href="detail.html?id=${item.id}">
                  <img class="market-img" src="${item.image}" alt="furniture">
                   </a>
                    <a href="detail.html?id=${item.id}"><button class="add-to-cart"})>$${item.price}</button></a>
                </div>
            `;
            
        })

       

        document.querySelector('.dynamic-data-all').innerHTML = markup;
        return ids;
    } catch(err) {
        console.log(err)
        return
    }
}

marketData()