from helper import get_embedding,dbconnection

# Function to perform similarity search in the database
def similarity_search_famous_places(user_query):
    try:
        query_embedding = get_embedding(user_query)
        if query_embedding is not None:            
            conn = dbconnection()
            if conn is not None:
                cursor = conn.cursor()
                cursor.execute("""SELECT place, description FROM famousPlacesTamilNadu ORDER BY vectors <=> %s::vector LIMIT 1;""", (query_embedding,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()
                if result:
                    return {
                        "place":result[0],
                        "description":result[1],
                        "status":True,
                        "message":"Famous places in Tamil Nadu"
                    }
                else:
                    return {
                        "status": False,
                        "message":"No similar place found."
                    }                    
            else : 
                return {
                    "status": False,
                    "message":"Database connection failed"
                }
        else :
            return {
                "status": False,
                "message":"Failed to get embedding for the query."
            }
    except Exception as e:
        print("Error in similarity search:", str(e))
        return {
                "status": False,
                "message":str(e)
            }
