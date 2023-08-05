
# Simple Chat Bot

Here is a simple implementation of a chat bot using intents and naive bias to figure out the most relevant response to a prompt





## Tech Stack

**Client:** vue, typescript, TailwindCSS

**Server:** Python- FastAPI

** Model ** Python - sklearn | numpy


## Run Locally

Clone the project

```bash
  git clone git@github.com:shadmeoli/bot.git
```

Go to the project directory

```bash
  cd bot
```


### Running server

Navigate to backend folder
```bash
cd backend
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server

> using uvicorn 
```bash
  python3 main.py
```

> using Gunicorn and uvicorn workers
```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

> If you don't have an API client you can test and view all the URLs by opening the provided server URL from the logs and open swagger using ```https://0.0.0.0:8000/docs``` or alternatively you can use redoc to view the documentation of the API by substituting docs with **redoc**

### Running client
To run the client you can open a new terminal sessiona in the same bot folder and navigate to the fronten folder

```bash
cd frontend
```

You have to install the dependencies for node
>yarn
```bash
yarn
```

No run the client server powerd by vite
```bash
yarn dev
```

if you are using any other package manger you can check on how to install dependencies and initiate the dev server.


## Support

For support, email shadcodes@duck.com

> Python : 3.8^ \
> vue: 3.0^ \
> Node: LTS 16^ 

## API Reference

#### Get all items
[API URL](https://shop-zetu-bot.onrender.com)


```bash
  POST {API_URL}/api/v1/chat
```

| Parameter | Type     |
| :-------- | :------- | 
| `message` | `string` |
