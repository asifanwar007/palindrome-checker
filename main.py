from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/check-palindrome/", response_class=HTMLResponse)
async def check_palindrome(request: Request):
    form_data = await request.form()
    word = form_data["word"]
    is_palindrome = check_palindrome(word)
    return templates.TemplateResponse("result.html", {"request": request, "word": word, "is_palindrome": is_palindrome})

def check_palindrome(word):
    word_length = len(word)
    for i in range(word_length):
        first_char = word[i]
        last_char = word[word_length-1-i]
        if first_char == last_char:
            continue
        else:
            # exit fucntion
            return False
    return True

if __name__ == "__main__":
    import uvicorn
    try:
       uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except Exception as e:
        print(e)

