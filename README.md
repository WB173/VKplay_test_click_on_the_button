Версии: 
Google Chrome 124.0.6367.208
selenium-server 4.20.0
java 22.0.1
Python 3.12.3
Python библиотека selenium: 4.20.0

Запуск сервера selenium с использованием системного Chrome, поэтому используется аргумент--selenium-manager:
java -jar selenium-server-4.20.0.jar  standalone --port 4444  --selenium-manager true
