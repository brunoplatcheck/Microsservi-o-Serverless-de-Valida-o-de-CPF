import logging
import re
import json
from azure.functions import HttpRequest, HttpResponse

def is_valid_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)  # Remove non-numeric characters
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digit(digits):
        return sum(int(d) * f for d, f in zip(digits, range(len(digits) + 1, 1, -1))) * 10 % 11 % 10

    d1 = calc_digit(cpf[:9])
    d2 = calc_digit(cpf[:9] + str(d1))
    return cpf[-2:] == f"{d1}{d2}"

def main(req: HttpRequest) -> HttpResponse:
    logging.info('Validating CPF...')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
            cpf = req_body.get('cpf')
        except ValueError:
            logging.error('Invalid JSON in request body.')
            return HttpResponse(
                json.dumps({"error": "Invalid JSON."}),
                status_code=400,
                mimetype="application/json"
            )

    if cpf:
        logging.info(f'CPF provided: {cpf}')
        is_valid = is_valid_cpf(cpf)
        return HttpResponse(
            json.dumps({"cpf": cpf, "valid": is_valid}),
            status_code=200,
            mimetype="application/json"
        )
    else:
        logging.warning('No CPF provided in the query string or request body.')
        return HttpResponse(
            json.dumps({"error": "Please provide a CPF in the query string or request body."}),
            status_code=400,
            mimetype="application/json"
        )
