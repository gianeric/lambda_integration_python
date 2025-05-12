import structlog

log = structlog.get_logger()

def processar(nome):
    log.info("Iniciando o processamento", nome=nome)

    # Simula uma lógica qualquer
    resultado = f"Olá, {nome}! Tudo certo por aqui."

    log.info("Processamento concluído", resultado=resultado)
    return resultado
