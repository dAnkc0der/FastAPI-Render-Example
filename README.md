# FastAPI-Render-Example

### Description

I have created a simple CRUD API that allows students to store their details. The following are the requests with their payloads.

```
  POST REQUEST:
    {
      "name": string,
      "roll_no: string,
      "phone_number: integer,
      "is_active: boolean(default: true)
    }

  GET REQUEST:
  GET REQUEST BY ID: URL/{id}
  UPDATE REQUEST: URL/{id} - Make changes in the payload that are the same as in POST REQUEST
  DELETE REQUEST: URL/{id}
```
### LIVE LINK 

The link will take 20-30 seconds to open.

[Github](https://carvach-submission.onrender.com/docs#/)

### Local Install

1). Clone the directory - ```git clone "Copied URL" ```

2). Install all libraries from requirements.txt file - ```pip install -r requirements.txt```

3). Within the app folder, inside config.py file, comment out DATABASE_URL and uncomment everything else in the class Settings.

4). Again within the app folder, inside database.py, comment out DATABASE_URL and add this line

```
DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
```

5). Create an env file in the folder and add this data inside the file with the credentials for your postgres database.

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
```

6). When all the things are finished run the webapp using this command

```
uvicorn app.main:app --reload
```
