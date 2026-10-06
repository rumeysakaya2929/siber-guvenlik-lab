## Soruların Cevapları
1. **Hangi özet anında kırıldı, hangisi yavaştı, neden?** 
   MD5 ve SHA-256 anında kırıldı, bcrypt yavaştı. Nedeni bcrypt'in maliyet faktörüyle kasıtlı olarak yavaş tasarlanmış olmasıdır.
2. **MD5 ile SHA-256 arasında kırma kolaylığı açısından fark var mıydı?** 
   Süre olarak ikisi de çok hızlı çözüldü. SHA-256 daha modern bir algoritmadır ancak çalışma mantığı gereği donanım gücüyle hızlı taranabilir.
3. **bcrypt neden hem kullanıcı için sorun değil hem saldırgan için kâbus?** 
   Normal kullanıcı girişinde milisaniyelik gecikme hissettirmez, ancak kaba kuvvet saldırılarında saniyedeki deneme sayısını dramatik ölçüde düşürür.
4. **'Tuz' (salt) ne işe yarar?** 
   Aynı parolaya sahip farklı kullanıcıların aynı hash değerini üretmesini engeller ve gökkuşağı tablosu saldırılarını etkisiz hale getirir.
