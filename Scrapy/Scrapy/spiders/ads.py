import scrapy
import yaml


def resources(name:str) -> dict[str:str]:
    """Read xpath.yml file that contains xpath's to scrape"""

    with open("../../xpath.yml", "r") as f:
        content:dict[str:str] = yaml.safe_load(f)
        return content[name]

class AdsSpider(scrapy.Spider):
    name = "ads"
    sedan = resources("cars_sedan")
    start_urls = ["https://www.encuentra24.com/el-salvador-es/autos-usados?q=f_style.3|imagesonly.on|number.50"]

    def parse(self, response):
        ad_link = response.xpath("//a[@class='ann-ad-tile__title']/@href").getall()

        for link in ad_link:
            yield response.follow(link, callback=self.data)


    def data(self, response):
        description = response.xpath(self.sedan["description"])
        price = response.xpath(self.sedan["price"])
        model = response.xpath(self.sedan["model"])
        year = response.xpath(self.sedan["year"])
        kilometers = response.xpath(self.sedan["kilometers"])

        yield {
            "desc": description,
            "model": model
        }
