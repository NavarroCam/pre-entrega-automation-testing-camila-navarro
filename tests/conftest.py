# Fixtures compartidas de Pytest

import logging

import pytest

from utils.helpers import crear_driver, realizar_login

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    # Navegador limpio para cada test (así los tests son independientes)
    logger.info("Abriendo navegador")
    navegador = crear_driver()
    yield navegador
    import time; time.sleep(3) 
    logger.info("Cerrando navegador")
    navegador.quit()


@pytest.fixture
def driver_logueado(driver):
    # Navegador con el login ya realizado
    logger.info("Iniciando sesión como standard_user")
    realizar_login(driver)
    return driver