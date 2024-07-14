from rag_app.schemas.rag_schema import QuerySchema

def test_texts_endpoint(test_app):
    query_data = QuerySchema(query="test texts", k=1)
    response = test_app.get("/rag/query", params=query_data.model_dump())
    
    assert response.status_code == 200
    assert "response" in response.json()  # Check the key name in the response schema
    assert isinstance(response.json()["response"], str)  # Adjust based on your ResponseSchema
