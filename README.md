# userbot
Юзербот, что меняет написание и отправку вашего сообщения (Beta)

# Установка (Termux/Linux)

Pip install pyrogram 

git clone https://github.com/serafit/userbot

cd userbot

apt install nano 

nano config.ini 

(Потом, в параметрах "api_id" и "api_hash" вводите id и hash своего telegram. Дабы получить их вы можете через сайт https://my.telegram.org/auth регистрируйтесь, выбирайте параметр "API development tools" и создовайте обсолютно рандомное "приложение" с обсолютно рандомными характеристиками. Заходим в него и получаем "

App api_id: 121313131
App api_hash: "xxxxxxxxxxx" 


Далее, вставлете значения подпунктов "App api_id" и "App api_hash" в congig.ini. Сохраняете это дела сочитанием "ctrl + s" и выходите из "nano" командой "ctrl + x")

python tl.py 

потом, можете сварачивать термукс (или строку) и пользоваться телегрумом, но с небольшими "фишечками"

# Функции

1. ".type" - высвечивает строку с этой командой (к примеру, написав ".type Ваше сообщение" и отправив это получателю, оно будет постепенно отсвечивать его как "Ваше сообщен▒". И так с каждой буквой и знаком припенания). 
2. ".hack" - вводите сообщение получателю в телеграме без каких либо других слов и наслаждайтесь ахуем вашего собесебника))
3. Фильтрация даты. Оно не имеет особых "команд", а все делает пассивно. Просто фотографии и видео в телегруме чуть быстрее загружаются...
