import base64
import json
import urllib.parse
from decimal import Decimal

import boto3


s3 = boto3.client(
    "s3",
    endpoint_url="http://host.docker.internal:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://host.docker.internal:4566",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

table = dynamodb.Table("NotasFiscais")


def resposta(status_code, conteudo):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(conteudo, default=str)
    }


def processar_evento_s3(event):
    quantidade = 0

    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        response = s3.get_object(
            Bucket=bucket,
            Key=key
        )

        conteudo = response["Body"].read().decode("utf-8")

        notas_fiscais = json.loads(
            conteudo,
            parse_float=Decimal
        )

        for nota in notas_fiscais:
            table.put_item(Item=nota)
            quantidade += 1

    return resposta(
        200,
        {
            "message": "Arquivo processado com sucesso",
            "quantidade": quantidade
        }
    )


def processar_post(event):
    body = event.get("body")

    if event.get("isBase64Encoded"):
        body = base64.b64decode(body).decode("utf-8")

    if not body:
        return resposta(
            400,
            {"error": "O corpo da requisição está vazio."}
        )

    nota = json.loads(
        body,
        parse_float=Decimal
    )

    campos_obrigatorios = {
        "id",
        "cliente",
        "valor",
        "data_emissao"
    }

    campos_ausentes = campos_obrigatorios - nota.keys()

    if campos_ausentes:
        return resposta(
            400,
            {
                "error": "Campos obrigatórios ausentes.",
                "campos": list(campos_ausentes)
            }
        )

    table.put_item(Item=nota)

    return resposta(
        201,
        {
            "message": "Nota fiscal cadastrada com sucesso",
            "id": nota["id"]
        }
    )


def processar_get():
    resultado = table.scan()

    return resposta(
        200,
        {
            "quantidade": resultado.get("Count", 0),
            "notas": resultado.get("Items", [])
        }
    )


def lambda_handler(event, context):
    try:
        # Evento disparado pelo S3
        if "Records" in event:
            primeiro_record = event["Records"][0]

            if "s3" in primeiro_record:
                return processar_evento_s3(event)

        # Evento vindo do API Gateway
        metodo = (
            event.get("httpMethod")
            or event.get("requestContext", {})
                    .get("http", {})
                    .get("method")
        )

        if metodo == "POST":
            return processar_post(event)

        if metodo == "GET":
            return processar_get()

        return resposta(
            400,
            {
                "error": "Tipo de evento ou método não reconhecido.",
                "evento_recebido": event
            }
        )

    except Exception as error:
        return resposta(
            500,
            {
                "error": str(error),
                "evento_recebido": event
            }
        )