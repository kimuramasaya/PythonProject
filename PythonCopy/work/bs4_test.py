# -*- coding:utf-8 -*-

#HTMLの<a>タグ<href>タグの抽出
import bs4

html = """
        <html>
            <head>
                <body>
                    <a href="http://www.yahoo.co.jp">Yahoo!!</a>
                    <a href="https://www.google.co.jp">Google</a>
                    <p>こんにちは</p>
                </body>
            </head>
        </html>
        """

resources = []

# BeautifulSoupオブジェクトを作成
soup = bs4.BeautifulSoup(html)

# htmlのすべてのaタグの中のhref属性の内容を取得
for a_tag in soup.find_all("a"):
    href_str = a_tag.get("href")
    resources.append(href_str)

# hrefの内容を表示
for resource in resources:
    print(resource)

