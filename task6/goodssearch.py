import requests
from bs4 import BeautifulSoup
import bs4

#使用request下载网页
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#使用beautifulsoup解析网页并提取所需内容
def fillGoodsList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for goods in soup.find_all('section',attrs={'class':"items-box"}):
        if isinstance(goods,bs4.element.Tag):
            name = goods('h3',attrs={'class':'items-box-name font-2'})
            prise = goods('div',attrs={'class':"items-box-price font-5"})
            ulist.append([prise[0].string, name[0].string])

#打印所需内容
def printGoodsList(ulist,num):
    print("{:^10}\t{:^50}".format("价格","名字"))
    for i in range(num):
        u = ulist[i]
        print("{:^12}\t{:^50}".format(u[0],u[1]))

#爬取HOYOYO网页里mercari上的商品价格和名称
# （因为本人经常会关注该页面商品的上新，所以想使用爬虫直接爬取自己最关注的商品信息，方便查看有没有想买的好价商品）
def main():
    uinfo = []
    search = "僕のヒーローアカデミア+東京"         #定义需要搜索的商品名称关键字
    for page in range(3):                        #定义需要爬取的页数
        try:
            url = 'https://cn.hoyoyo.com/mercari~search.html?page='+str(page)+'&keyword=' + search
            html = getHTMLText(url)
            fillGoodsList(uinfo,html)
        except:
            continue
    printGoodsList(uinfo, 10)       #数字代表需要打印多少条商品信息
main()
