# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import urllib2 as ulib

_url = ulib.build_opener()
_url.addheaders = [('User-agent', 'Mozilla/5.0')]
# print dir(ulib)
res = _url.open("http://www.amazon.in/gp/product/B07G9V9Z7B?pf_rd_p=f2b20090-067d-415f-953d-b8dcecc9109f&pf_rd_r=KBHG2C6547DWZAX7SJSP")
# print 'dir', res.read()
# print 'html', html

bs_content = BS(res)


tag = bs_content.find(id="priceblock_ourprice")
tag1 = bs_content.find(id="productTitle")
tag2 = bs_content.find(id="imgTagWrapperId")
# print 'tag', tag2.img
stock = {
	# "product_price": r"%s"%tag.string.strip(),
	"product_title": r"%s"%tag1.string.strip(),
	"product_img": tag2.img.get("src")
}

print 'stock', stock
# print 'title', bs_content.title.string