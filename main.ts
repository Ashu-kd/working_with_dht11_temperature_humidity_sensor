input.onButtonPressed(Button.A, function () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    true,
    true
    )
    if (dht11_dht22.readDataSuccessful()) {
        Humidity = dht11_dht22.readData(dataType.humidity)
    }
})
input.onButtonPressed(Button.B, function () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    true,
    true
    )
    if (dht11_dht22.readDataSuccessful()) {
        Temperature = dht11_dht22.readData(dataType.temperature)
    }
})
let Temperature = 0
let Humidity = 0
dht11_dht22.selectTempType(tempType.celsius)
