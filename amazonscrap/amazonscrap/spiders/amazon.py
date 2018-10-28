import scrapy
class products(scrapy.Spider):

	name = 'amazon'
	allowed_domains = ["amazon.in"]
	
	deals = []
	sales = []
	no_sale= []
	dotd = []
	
	product_name= input('Enter product name you want to scrap:')


	start_urls=["https://www.amazon.in/s/ref=sr_pg_1?bq=%28not+browse%3A%2714991705031%7C14991710031%7C14991712031%7C14991716031%7C14991714031%7C14991718031%27%29&rh=i%3Aaps%2Ck%3AWatch&page=1&keywords="+product_name,
	"https://www.amazon.in/s/ref=sr_pg_2?bq=%28not+browse%3A%2714991705031%7C14991710031%7C14991712031%7C14991716031%7C14991714031%7C14991718031%27%29&rh=i%3Aaps%2Ck%3AWatch&page=2&keywords="+product_name,
	"https://www.amazon.in/s/ref=sr_pg_3?bq=%28not+browse%3A%2714991705031%7C14991710031%7C14991712031%7C14991716031%7C14991714031%7C14991718031%27%29&rh=i%3Aaps%2Ck%3AWatch&page=3&keywords="+product_name,
	"https://www.amazon.in/s/ref=sr_pg_4?bq=%28not+browse%3A%2714991705031%7C14991710031%7C14991712031%7C14991716031%7C14991714031%7C14991718031%27%29&rh=i%3Aaps%2Ck%3AWatch&page=4&keywords="+product_name,
	"https://www.amazon.in/s/ref=sr_pg_5?bq=%28not+browse%3A%2714991705031%7C14991710031%7C14991712031%7C14991716031%7C14991714031%7C14991718031%27%29&rh=i%3Aaps%2Ck%3AWatch&page=5&keywords="+product_name]
	def  parse(self, response):
		for product in response.css('li.s-result-item'):
			urls = product.css('a.a-link-normal::attr(href)').extract_first()
			if urls != None:
				next_url = urls
				
				yield scrapy.Request(next_url,self.namesd)

				
				
	def namesd(self,response):
		deal = response.css('#priceblock_dealprice_lbl::text').extract_first()
		sale = response.css('#priceblock_saleprice_lbl::text').extract_first()
		if response.css('a.a-button-text > span::text').extract_first() != 'Kindle Edition':

			if deal=="Deal Price:":
				deals = {
				'product_name': response.css('span.a-size-large::text').extract_first().strip(),
				'price': response.css('#priceblock_dealprice').extract_first().split()[6].strip('</span>'),
				'mrp': response.css('td.a-span12').extract_first().split()[9].strip('</span>'),
				'product_link' : response.request.url,
				'type': 'Deal'
				}
				yield deals
			elif deal =="Deal of the Day:":
				dotd = {
				'product_name': response.css('span.a-size-large::text').extract_first().strip(),
				'price': response.css('#priceblock_dealprice::text').extract_first().strip(),
				'mrp': response.css('td.a-span12').extract_first().split()[9].strip('</span>'),
				'product_link' : response.request.url,
				'type': 'deal of the day'
				}
				yield dotd
			elif sale =="Sale:":
				sales = {
				'product_name': response.css('span.a-size-large::text').extract_first().strip(),
				'price': response.css('#priceblock_saleprice::text').extract_first().strip(),
				'mrp': response.css('td.a-span12').extract_first().split()[9].strip('</span>'),
				'product_link' : response.request.url,
				'type': 'Sale'
				}
				yield sales
		
			else:
				no_sale = {
				'product_name': response.css('span.a-size-large::text').extract_first().strip(),
				'price': response.css('#priceblock_ourprice').extract_first().split()[6].strip('</span>'),
				'mrp': response.css('td.a-span12').extract_first().split()[9].strip('</span>'),
				'product_link' : response.request.url,
				'type' : 'Normal listing'
				}

				yield no_sale