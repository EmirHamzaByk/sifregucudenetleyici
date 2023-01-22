# Bu kod, kullanıcının girdiği şifrenin güvenliğini kontrol etmek için kullanılır.Bu kod, kullanıcının girdiği şifrenin güvenliğini kontrol etmek için kullanılır.

Kod, kullanıcının girdiği şifrenin uzunluğunu, içerisinde küçük harf, büyük harf, rakam ve özel karakterlerin varlığını kontrol eder. Eğer şifre kurallarının tümünü sağlarsa **"Güçlü"** olarak değerlendirilir, aksi takdirde **"Zayıf"** veya **"Orta"** olarak değerlendirilir.

Kod, **"re"** kütüphanesini kullanır. Bu kütüphane, kod içinde arama işlemlerini yapmak için kullanılır. Örneğin, **"re.search("[a-z]", password)"** kodu, şifrenin içinde küçük harflerin olup olmadığını kontrol eder.

**While** döngüsü kullanılmış, bu sayede kullanıcı şifresini tekrar tekrar girerek güvenliğini kontrol edebilir. Eğer kullanıcı 'kapat' yazarsa döngü son bulur.

Son olarak, kod, kullanıcının şifresinin güvenlik seviyesini ekrana yazdırır. Örneğin,Şifreniz , Güçlü" şeklinde.
