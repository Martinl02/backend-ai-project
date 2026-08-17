import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(len(data))

    elif response.status_code == 404:
        print("Endpoint no encontrado (404)")

    else:
        print(f"Error inesperado: {response.status_code}")

except Exception as e:
    print(f"Error de conexión: {e}")