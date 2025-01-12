import requests

URL = 'http://localhost:8000'

def test_current_time():
    print("\ntest POST /api/v1/time...")
    payload = {'time_zone': 'Asia/Tomsk'}
    response = requests.post(f"{URL}/api/v1/time", json=payload)
    print(f"Answer: {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert 'current_time' in data
    print("test POST /api/v1/time success\n")

def test_current_date():
    print("test POST /api/v1/date...")
    payload = {'time_zone': 'Europe/Moscow'}
    response = requests.post(f"{URL}/api/v1/date", json=payload)
    print(f"Answer: {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert 'current_date' in data
    print("test POST /api/v1/date success\n")

def test_date_diff():
    #Тест с временной зоной
    print("test POST /api/v1/datediff with timezone...")
    payload = {
        'start': {
            'time_zone': 'Europe/Moscow',
            'date': '01.01.2025 12:00:00'
        },
        'end': {
            'time_zone': 'Asia/Barnaul',
            'date': '01.02.2025 12:00:00'
        }
    }
    response = requests.post(f"{URL}/api/v1/datediff", json=payload)
    print(f"Answer: {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert 'difference' in data
    print("test POST /api/v1/datediff success\n")

    #Тест без временной зоны
    print("test POST /api/v1/datediff without timezone...")
    payload = {
        'start': {
            'date': '01.01.2025 12:00:00'
        },
        'end': {
            'date': '01.02.2025 12:00:00'
        }
    }
    response = requests.post(f"{URL}/api/v1/datediff", json=payload)
    print(f"Answer: {response.text}")
    assert response.status_code == 200
    data = response.json()
    assert 'difference' in data
    print("test POST /api/v1/datediff success\n")

def run_tests():
    test_current_time()
    test_current_date()
    test_date_diff()

if __name__ == '__main__':
    run_tests()
