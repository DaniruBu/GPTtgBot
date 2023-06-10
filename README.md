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

openai.api_key = (os.getenv('OPENAI_API_KEY'))
...
```
Creat `.env`, write your tokens and save:
```
TOKEN = "<telegram_token>"
OPENAI_API_KEY = "<openai_token>"
```
Put `.env` and `venv` in `.gitignore`:
```
~ % echo .env >> .gitignore
~ % echo venv >> .gitignore
```
#### Requirements
```
~ % touch requirements.txt
~ % pip freeze >> requirements.txt
```
