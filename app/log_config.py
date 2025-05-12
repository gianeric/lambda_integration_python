import logging
import sys
import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars, merge_contextvars

def configure_logging():
    # USAR SOMENTE NA AWS
    # logging.basicConfig(level=logging.INFO)
    
    ###########################
    ### REMOVER, USAR SOMENTE NO LOCALSTACK
    # Remove qualquer handler antigo (opcional, mas útil em testes ou reexecuções)
    root_logger = logging.getLogger()
    if root_logger.handlers:
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
            
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(message)s"))  # Apenas o que o structlog emitir
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)
    ###########################

    structlog.configure(
        processors=[
            merge_contextvars, # Habilita suporte a contextvars (como correlation_id)
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )

def set_correlation_id(correlation_id):
    clear_contextvars()  # Evita "sujeira" entre execuções
    bind_contextvars(correlation_id=correlation_id)
