import urllib.parse
import requests
import datetime
Hora_Actual = datetime.datetime.now()
print ("Bienvenidos" , Hora_Actual) 
main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
    orig = input("Ciudad De Origen: ")
    if orig == "R" or orig == "r":
        break
    dest = input("Ciudad De Destino: ")
    if dest == "R" or dest == "r":
        break

    key = "jTJ45ZS0HTm7ZueY91pVM1XENUcZJsPo"
    url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest}) 
    json_data = requests.get (url) .json ()
    json_data = requests.get(url).json()
    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print ("API Status:” + str (json_status) + “= Una llamada de ruta exitosa.\ n")
        print("=============================================")
        print("Duraccion del viaje" + (orig) + " hasta " + (dest))
        print("Direccion de viaje: " + (json_data["route"]["formattedTime"]))
        print ("Millas:" + str (json_data ["route"] ["distance"]))
        print("Kilometros: " + str((json_data["route"]["distance"])*1.61))

    print("=============================================")

    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
