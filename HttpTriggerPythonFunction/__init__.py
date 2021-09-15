import logging

import azure.functions as func

from HttpTriggerPythonFunction import RandomGenerator as rg

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()

            loopcount = req_body['loopCount']
            sleepduration = req_body['sleepDuration']
            
            name = await rg.main(loopCount=int(loopcount), sleepDuration=int(sleepduration));

        except ValueError:
            pass
        except Exception as e:
            print(e)
        else:
            name = req_body.get('name')


    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
