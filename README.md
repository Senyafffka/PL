# **Сервер времени**
Проект представляет из себя веб приложение, написанное на python, реализация которого представлена в файле `app.py`.

## Установка из Docker Hub
Для этого необходимо быть авторизированным пользователем Docker Hub и иметь установленный на компьютер docker.
> В командной строке введите `docker run -d -p 8000:8000 senyaffka/app:v1.0`
> 
> Команда попытается найти образ локально, а затем обратится к репозиторию Docker Hub, скачает образ и запустит контейнер на порту 8000. 

## Чистая установка
Для этого необходимо иметь установленный Python. 
> Скачайте `app.py` и запустите его с помощью любого интерпретатора Python, предварительно установив зависимости следующими командами:
> + `pip install pytz`
> + `pip install requests`
> + `pip install tzlocal`
>   
> Команды необходимо выполнять в консоли среды, в которой запускаете приложение.
  
## Использование
Приложение будет доступно по адресу `http://localhost:8000`, просто введите это в поисковой строке браузера и увидете время в своей временной зоне.

Для получения времени в определенной временной зоне используйте следующий формат Get-запросов:

+ `http://localhost:8000/Europe/Moscow`
+ `http://localhost:8000/Asia/Tomsk`

Также доступны следующие Post-запросы (по умолчанию используется временная зона сервера):

+ `/api/v1/time` - отдает в формате json текущее время в зоне определенной параметром time_zone
+ `/api/v1/date` - отдает в формате json текущую дату в зоне определенной параметром time_zone
+ `/api/v1/datediff` - отдает в формате json разницу во времени между датами определенными параметрами start и end

> [!NOTE]
> Для тестирования Post-запросов запустите скрипт `test.py`

