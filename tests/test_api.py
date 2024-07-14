def test_rag_endpoint(test_app):
    response = test_app.get("/rag/query?query=test&k=5")
    
    assert response.status_code == 200
    assert "response" in response.json()  # Check the key name in the response schema
    assert isinstance(response.json()["response"], str)  # Adjust based on your ResponseSchema
