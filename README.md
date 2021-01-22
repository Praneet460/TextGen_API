## TextGen API

TextGen API is a text generation api build using python as programming language and frameworks like django, djangorestframeork, tensorflow and huggingfaces.

### API Endpoints

- Get
    - ```http://localhost:8000/api/v1/textgen/?context=I want to eat cake```
    - Response 
    ```
    {
        "response": [
            {
                "id": 3,
                "date_created": "2021-01-22T23:34:55.895284Z",
                "model_type": "beam_ngram_penality",
                "gen_text": "I want to eat cake,\" he said.\"I don't know what I'm going to do with my life, but I'll do whatever it takes to make it happen.\"",
                "context": 5
            }
        ]
    }
    ```
