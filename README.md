# Crypto hand project
![img](https://i.ibb.co/p098ZGq/photo-2023-06-23-13-09-41.jpg)

## ```What the purpose of this bot?```
> The main purpose is to make possible to saw really cryptocurrency exchange rate and help to find new promising crypto currencies without downloading separate app and going to the site



## ```Main tasks:```
- [ ] Create all bot structure
- [ ] create buttons and functional in bot
- [ ] Save user selected buttons in sql `(user_id: [bitcoin, dogecoin])`
## `How to test the bot?`
1. Create bot in [@BotFather](https://t.me/BotFather)
2. replace line of code from this:

```python
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
 ```
 to this:
```python
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)
 ```
3. Run ```bot.py``` file
## ```All links:```
- ### [Current design (you can offer your own design)🎨](https://www.figma.com/file/ukSP82PqNmDyt3CAz2cQXs/crypto-project?type=design&node-id=0%3A1&mode=design&t=xXpiAYWumHv17oaO-1)
- ### [Link to bot🤖](https://t.me/Crypto_hand_bot)

