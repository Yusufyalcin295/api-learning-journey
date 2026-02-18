import requests

#1.Hedef Adres Belirleme (Endpoint)
url= "https://jsonplaceholder.typicode.com/posts/1"

print(f" İstek Gönderiliyor:{url}")

#2.Get isteği atma(Postmandaki "Send" butonu)
response =requests.get(url)

#3.Durum Kontrolü (status) (200 OK mı)

if response.status_code==200:
    print("Başarılı (200 OK)")
    print("-" * 30)

    #4.Gelen JSON verisini Ayrıştırma
    data=response.json()

    #veriyi  yazdırma
    print(f"ID: {data['id']}")
    print(f"Title: {data['title']}")
    print(f"Content: {data['body']}")
    print("-" * 30)

else:
    print(f"Hata Oluştu ! Kod: {response.status_code}")

try:
    response = requests.get(url, timeout=5) # 5 saniye içinde cevap gelmezse bırak
    response.raise_for_status() # 404 veya 500 gibi hatalarda otomatik uyarı verme
except requests.exceptions.RequestException as e:
    print(f"Bağlantı sırasında bir hata oluştu: {e}")