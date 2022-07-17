# 抓取 PTT 八卦的網頁原始碼
import urllib.request as req
def getData(url):
    # 建立一個 request 物件 ， 附加 Request Headers 的資訊
    request = req.Request (url, headers={
            "cookie" : "over18=1" ,
            "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
})
    # 不要直接打網址 用 request 物件打開網址
    with req.urlopen(request) as response :
        data = response.read().decode('utf-8')
    # 解析原始碼， 取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data,'html.parser') # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
    print(root.title.string)
    titles = root.find('div',class_='title') # 尋找 class="title" 的標簽 會找到其中一個
    titles = root.find_all('div',class_='title') # 尋找 class="title" 的標簽 會找到全部
    for title in titles:
        if title.a != None : # 如果標題包含 a 標簽（沒有被刪除）， 印出來
                print(title.a.string)
    # 抓取上一頁的鏈接
    nextlink = root.find('a',string='‹ 上頁') # 找到内文是 ‹ 上頁的 a 標簽
    print(nextlink['class'])
    nextlink = 'https://www.ptt.cc/' + nextlink['href']
    print(nextlink)
    return nextlink
# 抓取一個頁面的標題
pageurl = 'https://www.ptt.cc/bbs/Gossiping/index.html'
count = 0
while count < 5 :
    pageurl = getData(pageurl)
    count+=1