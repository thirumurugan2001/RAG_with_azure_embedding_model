from fastapi import FastAPI
import uvicorn
from model import USERQUERY
from datamanipulation import similarity_search_famous_places
app = FastAPI()


@app.post("/rag/query")
async def ragUserQuery(Query: USERQUERY):
    try :
        print()
        response  = similarity_search_famous_places(Query.query)
        if response['status']:
            return {
                "data":[{
                    "place": response['place'],
                    "description": response['description'],
                }],
                    "message":"Successfully completed the RAG for your Query",
                    "status":True,
                    "statusCode":200,
                },200
        else : 
            return {
                "data":[{
                    "response": response['message']
                }],
                "message":"Failed to RAG your Query",
                "status":False,
                "statusCode":400,
            },400
    except Exception as e:
        print("Error in the createResume",str(e))
        return {
            "data":[{
                    "response": str(e)
                }],
            "message":"Failed to RAG your Query",
            "stratusCode": 400,
            "status":False
        },400

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
