urunler = [
    {"isim": "Mekanik Klavye", "fiyat": 1200, "puan": 4.8},
    {"isim": "Kablosuz Mouse", "fiyat": 450, "puan": 4.2},
    {"isim": "Geniş Ekran Monitör", "fiyat": 4500, "puan": 4.5},
    {"isim": "Laptop Soğutucu", "fiyat": 300, "puan": 3.9}
]

print("------------------Fiyata göre sıralama------------------")

# sorted liste içinde sözlük olduğu için neye göre sıralayacağını bilmiyor o yüzden bir key lazım
# lambda geçici fonksiyon demek lambdanın yanına da yazdığımız değişken ismi
# geçici olarak liste içindeki elemanlara verilen isim iki noktadan sonra neye göre sıralanacağı yazılır
# burda içindeki sözlük olduğu için bu sözlükte "fiyat" etiketinin karşılığına göre sırala demiş oluyoruz
# sonra bunu başka bi listeye o sırayla yazıyor for ile de içinde dolaşıp ekrana yazdırabiliyoruz
fiyat_sıra = sorted(urunler, key = lambda urun: urun["fiyat"])

for urun in fiyat_sıra:
    print(f"Ürün adı: {urun['isim']}  Fiyat: {urun['fiyat']}")