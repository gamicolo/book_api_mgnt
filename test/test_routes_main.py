
def test_store_book_info(test_client):

    response = test_client.post('/api/v1/assessment/store_book_info/111',json={'book_info':{'book name':'jhon doe'},'book_comments':'first comment'})

    assert response.status_code == 200

def test_get_existing_book_info_from_db(test_client):

    response = test_client.get('/api/v1/assessment/get_book_info/111')
    assert response.status_code == 200
    assert b"jhon doe" in response.data

def test_get_non_existing_book_info_from_external_api(test_client):

    response = test_client.get('/api/v1/assessment/get_book_info/123')
    assert response.status_code == 404
    assert b"Could not retrieve the info of the book with ISBN <123>" in response.data

def test_get_existing_book_info_from_external_api(test_client):

    response = test_client.get('/api/v1/assessment/get_book_info/9780140328721')
    assert response.status_code == 200
    assert b"Fantastic Mr. Fox" in response.data
