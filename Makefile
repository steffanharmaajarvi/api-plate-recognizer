start:
	mv .env.sample .env
	pip install -r requirements.txt
	uvicorn main:app --reload