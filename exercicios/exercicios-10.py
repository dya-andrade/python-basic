def convertToFahrenheit(celsius):
    '''
    :param celsius float:
    :return fahrenheit float:
    '''
    return ((9 * celsius) + 160) / 5

def printFahrenheit(celsius = 10):
    f = convertToFahrenheit(celsius)
    print(f'A temperatura em Celsius: {celsius}ºC em Fahrenheit: {f}ºF')


printFahrenheit(30)