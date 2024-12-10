import faker

f = faker.Faker()

print(f.email())

Адреса
Название	Метод	Пример
Индекс	fake.postcode()	875746
Название улицы	fake.street_name()	ул. Прудовая
Адрес на улице	fake.street_address()	ул. Балтийская, д. 23
Суффикс улицы	fake.street_suffix()	ул.
Название страны	fake.country()	Suriname
Название города	fake.city()	Самара
Полный адрес	fake.address()	к. Приозерск, ул. Урицкого, д. 98, 713715
Имена
Название	Метод	Пример
ФИО	fake.name()	Тарасова Наина Вениаминовна
Мужское ФИО	fake.name_male()	Кудряшов Платон Елизарович
Женское ФИО	fake.name_female()	Архипова Марфа Вадимовна
Фамилия	fake.last_name()	Селиверстов
Мужская Фамилия	fake.last_name_male()	Ширяев
Женская Фамилия	fake.last_name_female()	Кудряшова
Имя	fake.first_name()	Венедикт
Мужское Имя	fake.first_name_male()	Пантелеймон
Женское Имя	fake.first_name_female()	Фаина
Женский Префикс	fake.prefix_female()	г-жа
Мужской Префикс	fake.prefix_male()	тов.
Дополнительные методы
Название	Метод	Пример
Профессия	fake.job()	Нейрохирург
Номер телефона	fake.phone_number()	+78415389555
Сайт	fake.hostname()	web-59.rao.net
Почта	fake.ascii_free_email()	ladimir24@mail.ru
Ссылка	fake.uri()	http://www.zhuravlev.biz/blog/main/main/
Компания	fake.company()	РАО «Суворова Мельников»
