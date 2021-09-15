from asyncio.runners import run
import random
import uuid
import asyncio
import os
from time import time
from typing import Any
from time import perf_counter

from azure.storage.blob import BlobServiceClient

async def main(loopCount:int, sleepDuration:int) -> Any:
                
    startTimer = perf_counter()

    returnValue = []

    parallel_tasks = []

    for loopIndex in range(loopCount):
        tempIndex = loopIndex+1
        print(f"{tempIndex}/{loopCount}")
        parallel_tasks.append(create_random_string(sleepDuration))
    
    #service = BlobServiceClient()

    startTimer = perf_counter()                    
    
    #loop = asyncio.get_event_loop()
    asyncio.run(parallel_tasks)
    #loop.run_until_complete(parallel_tasks)
    #loop.close()

    stopTimer = perf_counter()

    print(f"Random generator completed in {stopTimer-startTimer:.3f}")

    return returnValue



async def create_random_string(duration:int ) -> str:
        
    randomString = str(uuid.uuid4()).replace('-', '')
    
    await asyncio.sleep(duration)

    print(randomString)
    
    return randomString
    