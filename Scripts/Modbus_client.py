"""El módulo actua como un cliente MODBUS TCP para conectarse con el PLC
El programa usa la librería pyModbusTCP para adquisisción de datos
Cuenta con seis funciones para escritua/lectura de bits y registros"""

from pyModbusTCP.client import ModbusClient



def read_inputs(ip,address,Length=1):
    """Lectura de registros INPUTS
    Nececita de tres parámetros:
        - ip: La dirección IP del servidor
        - address: La dirección del registro en base 0 (ejemplo si la dirección Modbus es 30001 address es 1)
        - Length: El numero de datos a leer (default: 1)"""
    client = ModbusClient(ip,502,1,auto_open=True)
    input_read = client.read_input_registers(address,Length)
    if input_read:
        print(input_read)
        client.close()
        return input_read
    else:
        print("Error en la lectura")
        client.close()
        return None
    
def read_contacts(ip,address,Length):
    """Lectura de bits CONTACT
    Nececita de tres parámetros:
        - ip: La dirección IP del servidor
        - address: La dirección del registro en base 0 (ejemplo si la dirección Modbus es 10001 address es 1)
        - Length: El numero de datos a leer (default: 1)"""
    client = ModbusClient(ip,502,1,auto_open=True)
    discret_values = client.read_discrete_inputs(address,Length)
    if discret_values:
        print(discret_values)
        client.close()
        return discret_values
    else:
        print("Error en la lectura")
        client.close()
        return None 

def write_simple_coil(ip,address,value):
    """Escritura de simple COIL
    Nececita de tres parámetros:
        - ip: La dirección IP del servidor
        - address: La dirección del registro en base 0 (ejemplo si la dirección Modbus es 00001 address es 1)
        - value: El estado del bit que va a escribir al servidor (1/0)"""
    client = ModbusClient(ip,502,1,auto_open=True)
    state = client.write_single_coil(address,value)
    if state:
        print("Coil enviado correctamente")
        client.close()
        return state
    else:
        print("Error en la escritura")
        client.close()
        return state
    
def write_multiple_coils(ip,address,values):
    """Escritura de multiples COIL
    Nececita de tres parámetros:
        - ip: La dirección IP del servidor
        - address: La primera dirección del registro en base 0 (ejemplo si la dirección Modbus es 00001 address es 1)
        - values: Los estados de los bits que va a escribir al servidor en forma de lista [1/0,1/0,1/0,....]
        la función realiza una escritura secuencial, es decir si la dirección es 1 y envía tres valores, se realiza escrita en la dirección 00001,00002,00003"""
    client = ModbusClient(ip,502,1,auto_open=True)
    state = client.write_multiple_coils(address,values)
    if state:
        print("Coils enviados correctamente")
        client.close()
        return state
    else:
        print("Error en la escritura")
        client.close()
        return state

def write_simple_holding(ip,address,value):
    """Escritura de simple HOLDING
    Nececita de tres parámetros:
        - ip: La dirección IP del servidor
        - address: La dirección del registro en base 0 (ejemplo si la dirección Modbus es 40001 address es 1)
        - value: El estado del registro que va a escribir al servidor"""
    client = ModbusClient(ip,502,1,auto_open=True)
    state = client.write_single_register(address,value)
    if state:
        print("Coils enviados correctamente")
        client.close()
        return state
    else:
        print("Error en la escritura")
        client.close()
        return state

def write_multiple_holding(ip,address,values):
    """Escritura de multiples HOLDING
    Nececita de tres parámetros:
        - ip: La dirección IP del servidor
        - address: La primera dirección del registro en base 0 (ejemplo si la dirección Modbus es 40001 address es 1)
        - values: Los estados de los registros que va a escribir al servidor en forma de lista [val0,val1,val2,....,valn]
        la función realiza una escritura secuencial, es decir si la dirección es 1 y envía tres valores, se realiza escrita en la dirección 40001,40002,40003"""
    client = ModbusClient(ip,502,1,auto_open=True)
    state = client.write_multiple_registers(address,values)
    if state:
        print("Coils enviados correctamente")
        client.close()
        return state
    else:
        print("Error en la escritura")
        client.close()
        return state