aiGPT is an artificial intelligence language model based on the GPT-3.5 architecture, trained with a massive amount of data and designed to generate human-like text.
Features
* Generates human-like text
* Can be fine-tuned for specific tasks
* Supports multiple languages
* Can be used for a wide range of applications, including chatbots, content generation, and more
Requirements
* Python 3.7 or higher
* PyTorch 1.9 or higher
* Transformers 4.11 or higher
Installation
1. Clone the repository:
git clone https://github.com/myusername/aigpt.git
Install the requirements:
pip install -r requirements.txt

Start the server:
python server.py
Usage
To generate text using AI GPT, you can send a POST request to the server with the following parameters:
* text: The prompt text to generate text from.
* model: The name of the pre-trained model to use (e.g., gpt2, gpt2-medium, gpt2-large, gpt2-xl).
* num_samples: The number of samples to generate.
* length: The length of each sample, in tokens.
* temperature: The sampling temperature to use (default is 1.0).
import requests

data = {
    'text': 'The quick brown fox',
    'model': 'gpt2',
    'num_samples': 1,
    'length': 50,
    'temperature': 0.5
}

response = requests.post('http://localhost:8080/generate', data=data)
print(response.json()['generated_text'])

Contributing
Contributions are welcome! If you would like to contribute to AI GPT, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:

git checkout -b feature/my-new-feature
Make your changes and commit them:
git commit -am 'Add some feature'
Push your changes to your fork:
git push origin feature/my-new-feature
1. Create a pull request on the original repository.
License
AI GPT is licensed under the MIT License. See LICENSE for details.
Configuration Files
The following configuration files are required for running AI GPT:
logging.ini
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=consoleFormatter,fileFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=fileHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=consoleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=fileFormatter
args=('/var/log/aigpt.log', 'a', 1000000, 5)

[formatter_consoleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S

[formatter_fileFormatter]
format=%(asctime)s
