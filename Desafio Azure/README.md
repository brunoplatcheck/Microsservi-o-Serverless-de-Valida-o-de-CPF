# Desafio Azure

## Overview
This project is an Azure Function that validates Brazilian CPF (Cadastro de Pessoas Físicas) numbers. It checks the validity of the CPF and returns a JSON response indicating whether the CPF is valid.

## Features
- Validates CPF numbers using a custom algorithm.
- Returns JSON responses for both valid and invalid inputs.
- Logs the validation process for better traceability.

## Requirements
- Python 3.x
- Azure Functions Core Tools
- Additional dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Desafio Azure
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the function locally, use the Azure Functions Core Tools:
```bash
func start
```

You can test the function by sending an HTTP request to the endpoint:
```
GET /api/ValidateCpfFunction?cpf=<your-cpf>
```

## License
This project is licensed under the MIT License.
