# Fixtures compartidas de Pytest

import logging

import pytest

from utils.helpers import crear_driver, realizar_login, tomar_captura

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    # Navegador limpio para cada test (así los tests son independientes)
    logger.info("Abriendo navegador")
    navegador = crear_driver()
    yield navegador
    logger.info("Cerrando navegador")
    navegador.quit()


@pytest.fixture
def driver_logueado(driver):
    # Navegador con el login ya realizado
    logger.info("Iniciando sesión como standard_user")
    realizar_login(driver)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Si un test falla, saca una captura de pantalla y la adjunta al reporte HTML
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:
        navegador = item.funcargs.get("driver") or item.funcargs.get("driver_logueado")
        if navegador:
            ruta = tomar_captura(navegador, item.name)
            logger.error(f"Test fallido. Captura guardada en: {ruta}")

            # Adjuntar la imagen al reporte de pytest-html
            plugin_html = item.config.pluginmanager.getplugin("html")
            if plugin_html:
                extras = getattr(reporte, "extras", [])
                extras.append(plugin_html.extras.image(ruta))
                reporte.extras = extras