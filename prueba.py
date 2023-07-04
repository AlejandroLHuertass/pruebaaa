import requests

def main():
    try:
        total_planets = 100  # Cantidad total de planetas que deseas obtener
        url = f"https://swapi.dev/api/people/"
        planets = []

        while len(planets) < total_planets:
            response = requests.get(url)
                   
            if response.status_code == 200:
                data = response.json()
                results = data.get('results', [])
                print(results)
                planets.extend(results)
                url = data.get('next')  # Obtener la URL para la siguiente página de resultados
            else:
                print(f"Error en la solicitud: {response.text}")
                break

        for planet in planets:
            print(planet)
            
    except Exception as ex:
        print(f"Error en la solicitud: {ex}")

if __name__ == "__main__":
    main()
