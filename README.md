# Market-Alisveris-Hesaplama

Bu proje python ile arayüz tasarlamayı ilk öğrendiğim zamanlarda oluşturduğum bir projedir.  
Amacı kullanıcının adı soyadı, ürün adedi ve ürün fiyat bilgisi alınıp messageBox ile ekrana yazdırmak.  
Bu projeyi oluşturmak için öncelikle python arayüz kütüphanesi olan tkinter’i indirmek gerekir.  

![image](https://user-images.githubusercontent.com/103186397/173690525-08daaa05-6b6f-43e7-ab47-210595abb920.png)  
*1. Satırda python da arayüz oluşturmak  için gereken tkinter kütüphanesi import edildi.  
*2. Satırda win adlı bir arayüz penceresi oluşturulur. 27. Satır sayesinde win adlı pencere biz kapatana kadar açık kalır.  
*4. Satırda oluşturaln fonksiyon çağrıldığı zaman işlev kazanacak.  
*9. Satırda oluşturulan label’de text kısmına ‘adını gir:’ ile müşteri adı sorulur, parantez içerisinde yazılan win sayesinde arayüze eklenir ve place ile labelin konumıu ayarlanır.  
*10. Satırda win adlı pencere arayüzünü kullanıcı bilgi giriş yeri eklenir.  
*11. Satırda bilgi giriş yerinin konumu ayarlanır.  
*13-14-15, 17-18-19, 21-22-23 satırlarında 9-10-11 satırlarındaki işlemler gerçekleşir.  
*25. Satırda win adlı pencereye hesapla isimli bir buton eklenir. .place(x=100, y=150) ile butonun konumu ayarlanır. Command=hesapla ile 4. Satırdaki fonksiyona erişilir.  
*hesapla butonuna basılırsa 5-6-7 kodları çalışır.  
*5. Satırda sonuç adlı değişkene ürün adedi ile ürün fiyatının çarpım sonucu atanır.  
*6 ve 7. Satırda messagebox ile ekrana gereken bilgi verilir.  

### KOD ÇALIŞTIKTAN  SONRA ORTAYA ÇIKAN GÖRÜNTÜ  
![image](https://user-images.githubusercontent.com/103186397/173690717-19bbdd6f-9561-426b-b70a-faf85e890b2f.png)
*Şeklinde bir arayüz oluşturulur ve doldurulur.  
![image](https://user-images.githubusercontent.com/103186397/173690763-d52d7106-ca3b-4edc-9004-a500764ff14a.png)
*Bu şekilde bir messagebox ile bilgi verilir.  
