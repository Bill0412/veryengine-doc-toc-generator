from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# max page id to crawl
maxPages = 500

CHROMEDRIVER_PATH = 'driver/chromedriver'

chromedriver_path = CHROMEDRIVER_PATH
options = Options()
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--verbose')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')

driver = webdriver.Chrome(chromedriver_path, options=options)

file = "contents.html"

body = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>VeRyEngine Docs - Table of Contents</h1>
<ul>
{}
</ul>
</body>
</html>
"""
ul = ""


for i in range(maxPages):
    link = "http://doc.veryengine.cn/readme/web/#/9?page_id={}".format(i)
    driver.get(link)
    driver.refresh()
    driver.implicitly_wait(3)

    try:
        title = driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/section/section/main/div[1]/h2'
        ).text

        row = '<li><{}>. <a href="{}" target="_blank">{}</a></li>'.format(i, link, title)
        ul += row
    except Exception:
        title = "null"

    print("<{}>. {}".format(i, title))


with open("contents.html", 'w') as out:
    out.write(body.format(ul))

driver.close()
driver.quit()
