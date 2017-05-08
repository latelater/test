import urllib.request
import re
from bs4 import BeautifulSoup

# x = 0
class deepyouxian(object):
	"""docstring for deepyouxian"""
	def __init__(self, visiturl, deep, visited):
		self.visiturl = visiturl
		self.visiturl = []
		self.visited = visited
		self.visited = []
		self.deep = deep
		self.deep = 2
	def chushihuaurl(self, url):
		the_page = self.getHtml(url)
		self.visiturl = self.link(the_page)
		# self.urlsaved(self.visiturl)
		self.visited.append(url)
		lenth = 1
		deepp = 1
		# print(self.visiturl)
		while deepp < self.deep:
			deepp += 1
			deep1 = len(self.visiturl)
			while deep1 > lenth :
				lenth += 1
				# try:
				burl = self.visiturl.pop(0)
					# print(burl)
				if burl not in self.visited:
					print(burl)
					try:
						the_page = self.getHtml(burl)
					except Exception as e:
						# print("链接链接链接链接链接链接链接链接")
						print(e)
						continue

					try:
						self.getImg(the_page)
					except Exception as e:
						# print("图片图片")
						print(e)
						continue

					visit11 = self.link(the_page)
						# print(visit11)
					self.visiturl.append(visit11)
					self.visited.append(burl)
				# except Exception as e:
				# 	print(e)
				# 	continue
		self.urlsaved(self.visited)

	def getHtml(self,url):
		print("***********************")
		# req=urllib.request.Request(url)
		# response=urllib.request.urlopen(url)
		headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/535.11'}
		request = urllib.request.Request(url, headers=headers)
		response = urllib.request.urlopen(request)
		contentType = response.headers['Content-Type']
		print("------" + response.headers['Content-Type'] + "---------")
		code = "UTF-8"
		pos = contentType.find('=')
		if -1 != pos:
			code = contentType[pos + 1:len(contentType)]
		the_page1=response.read()
		the_page=the_page1.decode(code, 'ignore')
		# if(url == "http://yjs.njupt.edu.cn/epstar/web/outer/dsfc_ny_.jsp?dsgh=19890007"):
		# 	print(the_page)
		return the_page

	def link(self, the_page):
		link_list =re.findall(r"(?<=ref=\").+?(?=\")|(?<=href=\').+?(?=\')" ,the_page)
		return link_list

	def urlsaved(self,visiturl):
		with open('urllink.txt','w') as urlw:
			for url in self.visited:
				urlw.writelines(url + '\n')
				
	def getImg(self, html):
		reg = r'src="(.+?\.jpg)'
		imgre = re.compile(reg)
		imglist = imgre.findall(html)
		# print(imglist)
		# x = [0]
		y = "http://yjs.njupt.edu.cn"
		z = "&sPath=/opt/yjs/dszp"
		for imgurl in imglist:
			img_list = y+imgurl+z
			print(img_list)
			img_name = img_list[65:77]
			urllib.request.urlretrieve(img_list, 'D:/code/javascript/js/teacherpachong/tutu/%s' %img_name)

b = deepyouxian('1', 2, '1')
# url = "http://cs.njupt.edu.cn/s/42/t/289/p/2/c/1942/list.htm"
url = "http://cs.njupt.edu.cn/1943/list.htm"
b.chushihuaurl(url)

# D:/code/javascript/js/teacherpachong/tutu/
# http://yjs.njupt.edu.cn/epstar/web/outer/dsfc_ny_.jsp?dsgh=19890007
# http://yjs.njupt.edu.cn/epstar/web/outer/showimage_ny.jsp?&id=19890007.jpg&sPath=/opt/yjs/dszp

# http://yjs.njupt.edu.cn/epstar/web/outer/showimage_ny.jsp?&id=20120021.jpg&sPath=/opt/yjs/dszp
# src="/epstar/web/outer/showimage_ny.jsp?&id=19890007.jpg&sPath=/opt/yjs/dszp"