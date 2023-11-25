def on_button_pressed_a():
    global Humidity
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, True, True)
    if dht11_dht22.read_data_successful():
        Humidity = dht11_dht22.read_data(dataType.HUMIDITY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Temperature
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, True, True)
    if dht11_dht22.read_data_successful():
        Temperature = dht11_dht22.read_data(dataType.TEMPERATURE)
input.on_button_pressed(Button.B, on_button_pressed_b)

Temperature = 0
Humidity = 0
dht11_dht22.select_temp_type(tempType.CELSIUS)