from woocommerce import API
from woocomerce_keys import Woocomerce

woo = Woocomerce()

wcapi = API(
    url="https://www.jamaicatea.cl",
    consumer_key=woo.get_key(),
    consumer_secret=woo.get_secret(),
    #wp_api=True,
    version="wc/v3"
)

#print(wcapi.get("products").json())

data = {
    'regular_price': '1290',
    'sale_price': '990'
}

print(wcapi.put("products/2844/variations/2845", data).json())