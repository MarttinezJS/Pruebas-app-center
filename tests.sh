pytest app/test/test.py -s -v > result.txt
uvicorn app.main:app --host 0.0.0.0 --port 80