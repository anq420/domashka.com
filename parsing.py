from lxml import html
import requests


origin_link = 'https://gippo-market.by'
ROOT_URL = requests.get('https://gippo-market.by/catalog')
catalog_links = []
link = '//a[@class="catalog-start__item"]/@href'
categories = html.fromstring(ROOT_URL.text).xpath(link)[11:12]


#здесь мы достаём ссылки на ВСЕ подкатегории
while categories:
    category = categories.pop()
    response = requests.get(f'{origin_link}{category}')
    # print(f'{origin_link}{category}', response)
    req = '//div[@class="link-arrow link-arrow--green"]/a[@class="link-arrow__link"]/@href'
    under_categories = html.fromstring(response.text).xpath(req)

    if under_categories:
        categories.extend(under_categories)
    else:
        catalog_links.append(str(f'{origin_link}{category}'))

# print(catalog_links)

#здесь мы достаём ссылки на ВСЕ продукты во всех подкатегориях
all_products_links =[]
for link in catalog_links:
    req_products = catalog_links.pop()
    # print(req_products)
    response = requests.get(link)
    # print(link, response)
    req_product = '//a[contains(@class, "product-card__img-wrap")]/@href'
    get_product = html.fromstring(response.text).xpath(req_product)
    all_products_links.extend(get_product)

# print(all_products_links)

#здесь мы выстакиваем название продукта и его характеристики
all_products = []
for link in all_products_links:
    full_link = f'{origin_link}{link}'
    response = requests.get(full_link)
    #здесь получаем название продукта
    req_name_product = '//div[@class="page-header"]/h1/text()'
    get_name = html.fromstring(response.text).xpath(req_name_product)[0]
    req_product = '//div[@class="product-page__table"]/div[@class="descr-table descr-table--dotted"]/div[@class="descr-table__item"]'
    get_product = html.fromstring(response.text).xpath(req_product)
    #здесь мы проходимся по каждой характеристике отдельно, тк их всего 5 (углеводы, жиры и тд)
    for product in get_product:
        name = product.xpath('./div[@class="descr-table__name"]/text()')[0].strip()
        prop = product.xpath('./div[@class="descr-table__prop"]/text()')[0].strip()
        all_products.append({get_name: {name: prop}})

print(all_products)



































#это вам не нужно))
# main_link = 'https://gippo-market.by/catalog/molochnye-produkty-yaytso-isg22/syr-isg262/myagkiy-syr-isg135/syr-myagkiy-slivochnyy-m-s-zh-55-ves-150-gr-s-napoln-quot-gretskiy-orekh-chesnok-chia-quot-tm-bela-b-4810099037032/'
# response = requests.get(main_link)
# req = '//div[@class="product-page__table"]/div[@class="descr-table descr-table--dotted"]/div[@class="descr-table__item"]'
# products = html.fromstring(response.text).xpath(req)
# req_name_product = '//div[@class="page-header"]/h1/text()'
# get_name = html.fromstring(response.text).xpath(req_name_product)[0]
# print(get_name)
#
# some_list = []
# for product in products:
#     name = product.xpath('./div[@class="descr-table__name"]/text()')[0].strip()
#     prop = product.xpath('./div[@class="descr-table__prop"]/text()')[0].strip()
#     some_list.append(
#         {
#             name: prop
#         }
#     )
#
#
# print(some_list)