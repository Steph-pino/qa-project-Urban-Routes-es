import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Helpers:

    def retrieve_phone_code(driver) -> str:
        """FRANCIELE FERREIRA, esta separación no la explican, y al poner este metodo en otro archivo y en otra clase.
        me marca error. También me di cuenta que no revisó nada de mi proyecto porque lo tenia en otra branch,
         así que aqui le dejo este mensaje que espero lea y me ayude con la solucion
         pues lo que marca amarillo: str, get_log y execute_cdp_cmd no tengo ni idea cómo resolverlo"""

        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code