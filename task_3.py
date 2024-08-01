import matplotlib.pyplot as plt

def read_sales_data(file_path):
    '''которая принимает путь к файлу и возвращает список продаж.
    product_name, quantity, price, date'''
    keys = ['product_name', 'quantity', 'price', 'date']
    list_file=[]
    with open(file_path, "r", encoding='utf-8') as file:
        for values in list(map(lambda line: line.replace(',','').split(), file.readlines())):
            list_file.append(dict(zip(keys, values)))
        return list_file


def total_sales_per_product(sales_data):
    '''принимает список продаж и возвращает словарь, где ключ - название продукта,
 а значение - общая сумма продаж этого продукта.'''
    result = {}
    for i in sales_data:
        for key, value in i.items():
            if key == 'product_name':
                result[value] = result.get(value, 0) + int(i['quantity']) * int(i['price'])
    return result


def sales_over_time(sales_data):
    '''принимает список продаж и возвращает словарь, где ключ - дата, а значение общая
сумма продаж за эту дату.'''
    result = {}
    for i in sales_data:
        for key, value in i.items():
            if key == 'date':
                result[value] = result.get(value, 0) + int(i['quantity']) * int(i['price'])
    return result



path_file = f'product.txt'

'''
Определить, какой продукт принес наибольшую выручку.
Определить, в какой день была наибольшая сумма продаж.
'''

sales_data = read_sales_data(path_file)
list_product = total_sales_per_product(sales_data)
list_data = sales_over_time(sales_data)

max_product = list([max(list_product.items(), key=lambda k_v: k_v[1])])
max_data = list([max(list_data.items(), key=lambda k_v: k_v[1])])


print(f'{max_product[0][0]} - это тот продукт, который принес наибольшую выручку, равную: {max_product[0][1]} едениц')
print(f'{max_data[0][0]} - в этот день была наибольшая сумма продаж, равная: {max_data[0][1]} едениц')

'''
Построить график общей суммы продаж по каждому продукту.
Построить график общей суммы продаж по дням.
'''

fig, axs = plt.subplots(1, 2)

index_l = [i[-5::] for i in list(list_data.keys())]
bw = 0.8
axs[0].bar(list_product.keys(), list_product.values(), bw, color='g')
plt.xlabel('Продукты')
plt.ylabel('Выручка')
plt.title('График общей суммы продаж по каждому продукту.')

index = [i for i in range(len(list_data))]
axs[1].bar(list_data.keys(), list_data.values(), bw, color='g')
plt.xlabel('Дата')
plt.xticks(index, index_l, rotation=90)
plt.ylabel('Выручка')
plt.title('График общей суммы продаж по дням.')

plt.show()
