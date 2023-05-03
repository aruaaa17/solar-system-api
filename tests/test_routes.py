def test_get_all_planets_with_empty_list(client):
    response=client.get('/planets')
    response_body=response.get_json()
    
    assert response_body == []
    assert response.status_code==200
    
def test_get_all_planets_with_populated_db(client,two_planets):
    response=client.get('/planets')
    response_body=response.get_json()
    
    assert response.status_code==200
    assert response_body==[
        {   
            "id":1,
            "name": "Mars", 
            "description":"It's a rocky planet."

        },
        {
            "id": 2,
            "name":"Jupiter", 
            "description":"It's a gas planet."
        }
        
    ]
    
def test_get_one_planet_empty_db_returns_404(client):
    response= client.get("/planets/1")
    assert response.status_code == 404

def test_returns_400_with_invalid_planet_id(client):
    response = client.get("/planets/Jupiter")
    assert response.status_code == 400
    
def test_post_one_animal_creates_planet_in_db(client):
    response = client.post("/planets", json={
        "name": "Mars",
        "description": "It's a rocky planet."
        }
    )

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body["id"] == 1
    assert response_body["name"] == "Mars"
    assert "msg" in response_body


def test_update_one_animal_updates_planet_in_db(client, two_planets):
    response = client.put("/planets/2", json={
        "name": "Jupiter",
        "description": "It's a gas planet."
    })

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == 2
    assert response_body["name"] == "Jupiter"
    assert response_body["description"] =="It's a gas planet."



def test_delete_one_animal_updates_planet_in_db(client, two_planets):
    response = client.delete("/planets/2", json={})

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body is None