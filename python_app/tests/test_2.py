# Checking that responce is not empty
def test_index(client_test):
    response = client_test.get('/')
    assert response.data
