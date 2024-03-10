import uvicorn

if __name__ == "__main__":
    uvicorn.run("settings:app", host="0.0.0.0", port=8111,
                reload=True, workers=1, log_level="info")
