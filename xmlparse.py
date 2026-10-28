import xml.etree.ElementTree as et

tree = et.parse('currency.xml')
root= tree.getroot()
currencies = []

for valute in root.findall('Valute'):
    value = float(valute.find('Value').text.replace(',', '.'))
    currencies.append(value)

average_value = sum(currencies) / len(currencies)

print(f'Среднее значение: {round(average_value, 2)}')