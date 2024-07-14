def test_add_text_data(test_app):
    """test the create new text endpoint
    """
    text_data = {"text": "example"}
    response = test_app.post("/texts", json=text_data)
    assert response.status_code == 201

def test_get_text(test_app):
    """test the get a text search endpoint
    """
    response = test_app.get("/texts?text=5&k=1")
    assert response.status_code == 200

def test_rag_endpoint(test_app):
    """test the rag endpoint
    """
    response = test_app.get("/rag/query?query=test&k=5")
    
    assert response.status_code == 200
    assert "response" in response.json() 
    assert isinstance(response.json()["response"], str)
