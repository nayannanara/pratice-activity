import pandas as pd
import csv

class PraticeActivity:

    def __init__(self) -> None:
        self.registration_data_one = []
        self.registration_data_two = []
        self.registration_data_three = []

        self.products_sold = []
        self.prices_table = []
        self.new_table = []

    def sorted_list(self,list) -> list:
        sorted_list = sorted(list, key=lambda k: k['registration']) 
        return sorted_list

    def inverte(self, frase) -> str:
        invertida = ' '.join(palavra[::-1] for palavra in frase.split())
        return invertida

    def question_one(self) -> None:
        records_quantity = 10
        cont = 0
        print("**** Let's make your registration ****")

        while cont <= records_quantity:
            registration = int(input("Enter your RA: "))
            name = str(input("Enter your name: "))
            address = str(input("Enter your address: "))

            print("*******************************")
            data = {
                'registration': registration,
                'name': name,
                'address': address
            }
            self.registration_data_one.append(data)
            cont = cont+1
        
        print("**** Now let's another make registration ****")

        cont = 0

        while cont <= records_quantity:
            registration = int(input("Enter your RA: "))
            number_of_dependents = int(input("Enter number of dependents: "))
            print("*******************************")
            data = {
                'registration': registration,
                'number_of_dependents': number_of_dependents,
            }
            self.registration_data_two.append(data)
            cont = cont+1

        print("***** List one ordened *****")    
        sorted = self.sorted_list(self.registration_data_one)
        print(sorted)
        print("***** List two ordened *****")    
        sorted = self.sorted_list(self.registration_data_two)
        print(sorted)

        cont = 0

        while cont <= records_quantity:
            registration = int(input("Enter your RA: "))
            name = str(input("Enter your name: "))
            number_of_dependents = int(input("Enter number of dependents: "))
            
            print("*******************************")

            data = {
                'registration': registration,
                'name': name,
                'number_of_dependents': number_of_dependents,
            }
            self.registration_data_three.append(data)
            cont = cont+1

        print("***** List three ordened *****")    
        sorted = self.sorted_list(self.registration_data_three)
        print(sorted)
    
    def question_two(self)-> None:
        order_quantity = 1
        cont = 0
        print("**** Let's create your order ****")
        
        while cont <= order_quantity:
            number_of_order = int(input("Enter the number of order: "))
            if number_of_order < 0:
                print('Number less than zero, ending execution')
                exit()
            number_of_product = int(input("Enter the number of product: "))
            quantity_sold = int(input("Enter quantity sold: "))
        

            print("*******************************")

            data = {
                'number_of_order': number_of_order,
                'number_of_product': number_of_product,
                'quantity_sold': quantity_sold,
            }
            self.products_sold.append(data)
            cont = cont+1

        print("**** Now let's read the price table ****")

        cont = 0

        while cont <= order_quantity:
            number_of_order = int(input("Enter the number of order: "))
            if number_of_order < 0:
                print('Number less than zero, ending execution')
                exit()
            unit_price = int(input("Enter unit price: "))
        

            print("*******************************")

            data = {
                'number_of_order': number_of_order,
                'unit_price': unit_price,
            }
            self.prices_table.append(data)
            cont = cont+1

        for prod in self.products_sold:
            for prod_price in self.prices_table:
                if prod['number_of_order'] == prod_price['number_of_order']:
                    data = {
                        'number_of_order': prod['number_of_order'],
                        'number_of_product': prod['number_of_product'],
                        'quantity_sold': prod['quantity_sold'],
                        'unit_price': prod_price['unit_price'],
                        'price_total': prod['quantity_sold'] * prod_price['unit_price'],
                    }

                    self.new_table.append(data)
                else:
                    print('Produto inexistente')
            

        sorted_list = sorted(self.new_table, key=lambda k: k['number_of_order']) 
        df = pd.DataFrame(sorted_list, columns = ['number_of_order','number_of_product','quantity_sold','unit_price', 'price_total'])
        print(df)

    def question_three(self)-> None:
        word = str(input("Enter your word or phrase: "))

        print(f"O tamanho dessa palavra é: {len(word)}")
        print(f"Palavra em caixa alta: {word.upper()}")
        print(f"Palavra invertida: {self.inverte(word.lower())}")

    def question_four(self)-> None:
        word = str(input("Enter your word: "))
        abr = word[0:3]
        print (f"{word} - {abr.upper()}")

    def question_five(self)-> None:
        print("*** MENU ***")
        print("1- Inserir")
        print("2- Listar")
        print("3- Sair")

        opt = int(input("Digite o numero de uma opcao: "))
        cont = 0
        palavras = []

        if opt == 1:
            qtd = int(input("Quantas palavras quer digitar? "))

            while cont < qtd:
                word = str(input("Digite uma palavra "))
                palavras.append(word)

                with open('file.csv', 'w', encoding='utf-8') as f:
                    w = csv.writer(f)

                    for p in palavras:
                        w.writerow([p])       

                    cont=cont+1

        elif opt == 2:
            with open('file.csv') as csv_file:

                csv_reader = csv.DictReader(csv_file, fieldnames=["palavra"])

                csv_reader.__next__()
                
                for row in csv_reader:
                    print(row["palavra"])
        else:
            exit()

    def question_six(self, texto)-> None:
        print(len(texto.split()))

    def question_seven(self, data)-> None:
        meses = {
            '01': 'janeiro',
            '02': 'fevereiro',
            '03': 'março',
            '04': 'abril',
            '05': 'maio',
            '06': 'junho',
            '07': 'julho',
            '08': 'agosto',
            '09': 'setembro',
            '10': 'outubro',
            '11': 'novembro',
            '12': 'dezembro'
        }
        data = data.split('/')
        for mes in meses.keys():
            if data[1] in mes:
                print(f"A data por extenso é: {data[0]} de {meses[data[1]]} de {data[2]}")

p = PraticeActivity()
p.question_five()
