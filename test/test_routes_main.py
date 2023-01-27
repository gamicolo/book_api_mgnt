
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

def test_book_comments_management_with_book_not_stored(test_client):

    response = test_client.get('/api/v1/assessment/book_comments_management/2')
    assert response.status_code == 404
    assert b"The book doesn't exist on the database"

def test_book_comments_management_update(test_client):

    #Store a book on the DB first in order to test the book comments management views fo the API
    r = test_client.post('/api/v1/assessment/store_book_info/9',json={'book_info':{'book name':'this is the name of the book'},'book_comments':'first comment'})

    response = test_client.put('/api/v1/assessment/book_comments_management/9',json={'book_comments':'updating the first comment'})

    assert response.status_code == 200
    assert b"Success updating the comment in the book" in response.data
    
def test_book_comments_management_delete(test_client):

    #Store a book on the DB first in order to test the book comments management views fo the API
    r = test_client.post('/api/v1/assessment/store_book_info/9',json={'book_info':{'book name':'this is the name of the book'},'book_comments':'first comment'})

    response = test_client.delete('/api/v1/assessment/book_comments_management/9')

    assert response.status_code == 200
    assert b"Success deleting the comment of the book" in response.data

def test_book_comments_management_get(test_client):

    #Store a book on the DB first in order to test the book comments management views fo the API
    r = test_client.post('/api/v1/assessment/store_book_info/10',json={'book_info':{'book name':'this is the name of the book'},'book_comments':'first comment'})

    response = test_client.get('/api/v1/assessment/book_comments_management/10')

    assert response.status_code == 200
    assert b"first comment" in response.data
