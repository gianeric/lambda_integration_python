import json
import uuid
from log_config import configure_logging, set_correlation_id
from servico import processar
import structlog

configure_logging()
log = structlog.get_logger()

def handler(event, context):
    correlation_id = str(uuid.uuid4())
    set_correlation_id(correlation_id)

    try:
        log.info("Iniciando a lambda", payload=event)
        
        resultado = processar("Dante")
        log.info("Processamento concluído", payload={"resultado": resultado})
        return {
            "statusCode": 200,
            "body": "Lambda executada com sucesso!"
        }
    except Exception as e:
        # Caso algum erro aconteça, retorna uma mensagem amigável
        return {
            'statusCode': 400,
            'body': f'Ocorreu um erro ao processar o evento: {str(e)}'
        }
