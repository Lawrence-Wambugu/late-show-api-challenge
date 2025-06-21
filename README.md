# 🌙 Late Show API — Phase 4 Code Challenge

A Flask RESTful API for managing a late-night show’s guests, episodes, and appearances.

---

## 🚀 Tech Stack

- Python 3.8
- Flask + Flask-SQLAlchemy + Flask-Migrate
- Flask-JWT-Extended (token-based auth)
- PostgreSQL
- Postman for testing
- GitHub for version control

---

## 📁 Project Structure

late-show-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ ├── controllers/
├── migrations/
├── challenge-4-lateshow.postman_collection.json
├── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<Lawrence-Wambugu>/late-show-api-challenge.git
cd late-show-api-challenge
2. Create Virtual Environment
bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
3. Setup PostgreSQL Database
bash
Copy
Edit
sudo -u postgres psql
Inside psql:

sql
Copy
Edit
CREATE DATABASE late_show_db;
ALTER USER postgres WITH PASSWORD 'mypassword123';
\q
Update server/config.py:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mypassword123@localhost:5432/late_show_db"
4. Migrate + Seed DB
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial"
flask db upgrade
python server/seed.py
5. Run the App
bash
Copy
Edit
flask run
App will run at: http://localhost:5000

🔐 Auth Flow
Register: POST /register

Login: POST /login → returns JWT

Use JWT for protected routes:

makefile
Copy
Edit
Authorization: Bearer <token>
📡 API Endpoints
Method	Route	Auth?	Description
POST	/register	❌	Create user
POST	/login	❌	Login user + return JWT
GET	/guests	❌	List all guests
GET	/episodes	❌	List all episodes
GET	/episodes/<id>	❌	Episode + appearances
DELETE	/episodes/<id>	✅	Delete episode
POST	/appearances	✅	Create appearance

📬 Postman Collection
Open Postman

Import challenge-4-lateshow.postman_collection.json

Use the requests:

Register

Login (copy token)

Send token in Authorization header for protected routes

✅ Submission Checklist
 MVC folder structure

 PostgreSQL used

 Models with relationships and validation

 Token auth implemented

 Working seed file

 All routes tested

 README completed

 Code pushed to GitHub

📎 GitHub Repo
https://github.com/<Lawrence-Wambugu>/late-show-api-challenge

Made with ❤️ by Lawrence Wambugu
