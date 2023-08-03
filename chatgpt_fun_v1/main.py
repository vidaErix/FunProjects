from fastapi import FastAPI, HTTPException
import openai

OPEN_API_KEY = "sbasdadswdwsd"

app = FastAPI()

openai.api_key = OPEN_API_KEY

@app.post("/generate-text/")
async def generate_text(prompt: str):
    try:
        # Call the OpenAI GPT-3.5 API to generate text
        response = openai.Completion.create(
            engine="text-davinci-002",  #engine
            prompt=prompt,
            max_tokens=150,  # Maximum length of generated text
            stop=["\n"]  # Stop generating text after a new line
        )
        return {"text": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to check if the API is up and running
@app.get("/ping/")
async def ping():
    return {"status": "pong"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
