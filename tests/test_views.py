from django.urls import reverse


def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    url = reverse('address-parse')
    response = client.get(url, {'address': address_string})
    assert response.status_code == 200
    data = response.json()
    assert 'address_components' in data
    assert 'address_type' in data
    assert 'AddressNumber' in data['address_components']
    assert 'StreetName' in data['address_components']
    assert 'PlaceName' in data['address_components']


def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    url = reverse('address-parse')
    response = client.get(url, {'address': address_string})
    assert response.status_code == 400
    data = response.json()
    assert 'detail' in data
    assert (
        'RepeatedLabelError' in data['detail'] or
        'Unable to tag this string' in data['detail']
    )
