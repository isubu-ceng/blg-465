# Test Yönetimi Dokümantasyonu

Bu repository'de GitHub Issues kullanarak test case yönetimi yapıyoruz.

## Test Case Oluşturma

1. Repository'de **Issues** sekmesine gidin
2. **New Issue** butonuna tıklayın
3. **Test Case** template'ini seçin
4. Formu doldurun:
   - Test ID (örn: TC-001)
   - Test açıklaması
   - Ön koşullar
   - Test adımları
   - Beklenen sonuç
   - Öncelik seviyesi
   - Durum

## Test Sonucu Kaydetme

1. Test case'i çalıştırdıktan sonra **Test Result** template'i ile yeni bir issue oluşturun
2. Test Case ID'yi belirtin
3. Test sonucunu işaretleyin (Passed/Failed/Blocked)
4. Detayları doldurun
5. Screenshot veya kanıt ekleyin

## Test Label'ları

- 🧪 `test-case` - Test case issue'ları için
- ✅ `test-passed` - Başarılı testler
- ❌ `test-failed` - Başarısız testler
- ⏸️ `test-blocked` - Engellenmiş testler
- 📊 `test-result` - Test sonuç kayıtları

## Test Durumları

- **Not Tested**: Henüz test edilmedi
- **Passed**: Test başarılı
- **Failed**: Test başarısız
- **Blocked**: Test engellenmiş (başka bir soruna bağlı)

## Örnek Test Case Formatı

```
Test ID: TC-001
Description: Kullanıcı giriş fonksiyonu testi

Preconditions:
- Kullanıcı kayıtlı olmalı
- Uygulama çalışır durumda olmalı

Steps:
1. Giriş sayfasına git
2. Geçerli kullanıcı adı gir
3. Geçerli şifre gir
4. "Giriş Yap" butonuna tıkla

Expected Result:
- Kullanıcı başarıyla giriş yapar
- Ana sayfaya yönlendirilir
- Hoşgeldin mesajı görüntülenir
```

## Test Raporlama

Test sonuçlarını görmek için:
1. Issues sekmesinde `test-result` label'ı ile filtreleyin
2. Son test sonuçlarını gözden geçirin
3. Başarısız testler için `test-failed` label'ı ile filtreleyin

## İletişim

Test ile ilgili sorularınız için issue açabilirsiniz.