import scrapy

class TaskSpider(scrapy.Spider):
  name = 'task'
  start_urls = ['https://www.gov.uk/government/organisations/companies-house']

  
  def parse(self, response):
    
      for link in response.css('div.gem-c-image-card__text-wrapper a::attr(href)').getall():
        
        yield response.follow(link, callback=self.parse_task) 
      

        
  def parse_task(self, response):
    task_dict={
       'Name':response.css('div.govuk-grid-column-two-thirds h1::text').get(),
       'Profession':response.css('div.govuk-grid-column-two-thirds span::text').getall()[-2:],
       'Biography':response.css('div.govuk-grid-column-two-thirds p::text').getall()[5:9],
       'Picture':response.css('div.govuk-grid-row img::attr(src)').get()
       
    }
    yield task_dict