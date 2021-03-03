import requests
import select

res = requests.get("https://www.kommersant.ru/doc/4712725?utm_source=yxnews&utm_medium=desktop")

f = open("data.html", "w", encoding="utf-8")
f.write(res.text)

print(res.text)