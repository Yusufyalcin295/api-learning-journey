import  requests

#1.Hedef Adres belirlem (Endpoint)
url="https://jsonplaceholder.typicode.com/posts"

#Bu adrese göndereceğimiz veri
new_data={
    "title": "Python ile API Öğreniyorum",
    "body": "Python ile POST isteği atma",
    "userId": 1
}

print(f"Veri Gönderiliyor: {url}")

#Post isteği atma (json= parametresini kullanıyoruz)
response=requests.post(url,json=new_data)

#Durum Kontrolü (Yeni kayıt için genelde 201 döner)

if response.status_code==201:
    print("Başarılı! Veri sunucuya iletildi. (201 Created)")

    # Son olarak sunucunun bize verdiği yanıtı(oluşturulan objeyi) görrelim
    result = response.json()
    print("\n--- Sunucudan Gelen Yanıt ---")
    print(f"Atanan ID: {result['userId']}")
    print(f"Başlık: {result['title']}")
    print("------------------------")

else:

   print(f"Hata! Kod: {response.status_code}")

