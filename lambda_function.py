import base64
from urllib.parse import parse_qs, unquote_plus

def lambda_handler(event, context):
    print("EVENTO COMPLETO:")
    print(event)
    
    # Decodificar base64
    raw_body = base64.b64decode(event["body"]).decode("utf-8")
    print("BODY DECODIFICADO:")
    print(raw_body)  

    # Parsear con parse_qs
    params = parse_qs(raw_body)
    
    # Extraer valores de los parámetros
    body = unquote_plus(params.get('Body', [''])[0])
    from_number = unquote_plus(params.get('From', [''])[0])

    print("MENSAJE RECIBIDO:")
    print(f"De: {from_number}")
    print(f"Mensaje: {body}")

    return {
        'statusCode': 200,
        'body': f"Mensaje recibido de {from_number}: {body}"
    }
