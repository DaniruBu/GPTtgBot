# GPTtgBot
#### Python Library:
`~ % pip install openai`
`~ % pip install aiogram`

#### How to store tokens

`~ % pip install python-dotenv`
```python
...
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) # find .env

bot = Bot(os.getenv('TOKEN')) # read TOKEN from .env
dp = Dispatcher(bot)
...
```
Creat `.env`, write your tokens and save:
```
TOKEN = "<your token>"
```
Put `.env` in `.gitignore`:
```
~ % echo .env >> .gitignore
```

