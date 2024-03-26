# Deve receber 3 parametros (operation, num1, num2)

# Validar os parametros e todos devem ser validos
# do contrario retornaremos uma excessao com a mensagem do erro

# Deve retornar o resultado da operacao quando os param forem validos

def calculator(operation, num1, num2):
    
    validate(operation, num1, num2)

    if operation == 'add':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2 
    elif operation == 'mult':
        return num1 * num2
    elif operation == 'div':
        try:
            return num1 / num2
        except ZeroDivisionError:
            raise ZeroDivisionError("Você não pode dividir um número por 0")

def validate(operation, num1, num2):
    if operation is None:
        raise Exception('Operação não pode ser nulo')
    
    if num1 is None or num2 is None:
        raise Exception(
            'Informe dois números válidos para realizar a operação')

    if operation not in ['add', 'sub', 'mult', 'div']:
        raise Exception('Informe uma operação válida (add, sub, mult, div)')