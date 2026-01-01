


в первый раз запуск
python3 -m venv env


и каждый раз активировать окружени
Set-ExecutionPolicy Unrestricted -Scope Process
env\Scripts\Activate



pip install fastapi uvicorn sqlalchemy alembic asyncpg psycopg2  pydantic aiosqlite

pip install -r requirements.txt




для запуска фастапи сервера

uvicorn main:app --reload