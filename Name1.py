from urllib.request import urlopen
from xml.etree.cElementTree import parse

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
file = urlopen(url)
xml_doc = parse(file)

# ввод кода валют
extra_currencies_input = input()
extra_currencies = []

# проверка на наличие запятых и сплит
if ',' in extra_currencies_input:
    extra_currencies = extra_currencies_input.split(',')
else:
    extra_currencies.append(extra_currencies_input)


currencies = ['USD', 'EUR'] + extra_currencies


root = xml_doc.getroot()

for item in root.findall('Valute'):
    output = ''
    char_code = item.find('CharCode').text
    value = item.find('Value').text
    name = item.find('Name').text
    nominal = item.find('Nominal').text
    nominal_int = int(nominal)

    if char_code in currencies:
        if nominal_int > 1:
            output += ' ' + nominal
        output += ' ' + name + ' - '
        output += value
        print(output)


