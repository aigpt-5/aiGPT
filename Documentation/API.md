The aiGPT API allows you to generate human-like text using aiGPT language model.
Usage
To generate text using AI GPT, you can send a POST request to the server with the following parameters:
* text: The prompt text to generate text from.
* model: The name of the pre-trained model to use (e.g., gpt2, gpt2-medium, gpt2-large, gpt2-xl).
* num_samples: The number of samples to generate.
* length: The length of each sample, in tokens.
* temperature: The sampling temperature to use (default is 1.0).
Request
POST /generate HTTP/1.1
Host: localhost:8080
Content-Type: application/json

{
    "text": "The quick brown fox",
    "model": "gpt2",
    "num_samples": 1,
    "length": 50,
    "temperature": 0.5
}
Response
HTTP/1.1 200 OK
Content-Type: application/json

{
    "generated_text": "The quick brown fox jumps over the lazy dog."
}
Error Codes
The API may return one of the following HTTP error codes:
* 400 Bad Request: The request was invalid or missing required parameters.
* 500 Internal Server Error: An error occurred on the server while processing the request.
License
This API is licensed under the MIT License. See LICENSE for details.
Feel free to modify this structure based on your needs.