import bs4, requests 

def carologiladas_productPlusprice(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    
    soupPrice = bs4.BeautifulSoup(res.text, 'html.parser')
    price = soupPrice.select('html body.js-head-offset.head-offset.template-product.theme-rounded div.js-main-content.main-content div#single-product.js-has-new-shipping.js-product-detail.js-product-container.js-shipping-calculator-container.position-relative div.container-fluid div.row.section-product-detail div.js-product-detail-form-col.col-12.col-md-4.product-detail-form-col div.js-sticky-product.product-detail-container div.price-container.mb-4 span.d-inline-block.mr-3 h3#price_display.js-price-display.regular-price.font-weight-bold.mb-0')
    
    soupName = bs4.BeautifulSoup(res.text, 'html.parser')
    name = soupName.select('html body.js-head-offset.head-offset.template-product.theme-rounded div.js-main-content.main-content div#single-product.js-has-new-shipping.js-product-detail.js-product-container.js-shipping-calculator-container.position-relative div.container-fluid div.row.section-product-detail div.js-product-detail-form-col.col-12.col-md-4.product-detail-form-col div.js-sticky-product.product-detail-container section.page-header div h1.h2.js-product-name.h2-md')
    
    if price and name:
        return 'Nombre: ' + name[0].text.strip() + ' Precio: ' + price[0].text.strip()
    else:
        return "Price not found on the page."

productUrl = 'https://www.carologiladas.com/productos/cutu-negros-acero-par/'
print(carologiladas_productPlusprice(productUrl))