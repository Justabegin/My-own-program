# 抓取 Medium 的網頁原始碼
import urllib.request as req
url = 'https://medium.com/_/api/home-feed'
# 建立一個 request 物件 ， 附加 Request Headers 的資訊
request = req.Request (url, headers={
        "User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        'authority' :"medium.com"
})
# 不要直接打網址 用 request 物件打開網址
with req.urlopen(request) as response :
    data = response.read().decode('utf-8')
# 解析原始碼， 取得每篇文章的標題
import json
# 把文章中不是字典格式的原始碼去掉
data = data.replace("])}while(1);</x>","")
data = json.loads(data)
# 取得 JSON 資料中的文章標題
posts = data['payload']['references']['Post']
for key in posts:
    post = posts[key]['title']
    print(post)
# 等於  post = posts[key]
#       print(post['title'])