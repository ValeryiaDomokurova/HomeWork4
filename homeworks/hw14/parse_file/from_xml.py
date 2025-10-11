import xml.etree.ElementTree as ET


def calculate_total_cost(filename):
    try:
        tree = ET.parse(filename)
        total = sum(
            float(item.find('price').text) * int(item.find('quantity').text)
            for item in tree.getroot().findall('item')
        )
        return total
    except FileNotFoundError:
        return 0


print(f"Total cost: {calculate_total_cost('products.xml')} rub.")
