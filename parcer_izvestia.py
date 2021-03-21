import requests
run = True
id = 1101000
max_id=1101050
while run and id < max_id:
    print(id)
    res = requests.get(f"https://iz.ru/{id}")
    if res.status_code==200:
        f = open(f"{id}.html", "w", encoding="utf-8")
        f.write(res.text)
        f.close()
        if res.text.find("Доступ к запрашиваемой странице закрыт") != -1:
            run =False
 #   else:
 #       run=False
    id +=1