# Учебный проект в рамках лабораторной работы по docker-compose
## Реализовано 3 сервиса:

**Сервис-1**. MySQL База данных. Сервис запускается, ожидает входящих соединений на своем порту.

**Сервис-2**. Контейнер со скриптом для наполнения базы. Сервис запускается, подключается по порту к базе данных и заполняет базу набором данных. Набор данных представлен CSV-файлом `data.csv` в каталоге `data`. В каждой строке 2 поля: текст и число (данные могут быть любые). Сервис-2 стартует после старта сервиса-1 и завершается (убивается контейнер) после выполнения.

**Сервис-3**. Контейнер с демоном отдающим из базы эти данные по http-запросу. Демон умеет принимать http запрос, соединяется с контейнером базы через порт базы, делает запрос, получает ответ, отдает данные в http ответе. Для реализации REST API использован flask. Запросы ожидаются на порту 32755.