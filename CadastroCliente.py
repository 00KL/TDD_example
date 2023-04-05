# -*- coding: utf-8 -*-

class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []
    
    def cadastrar_cliente(self, cliente):
        if cliente.idade < 18:
            return "Cliente não pode ser menor de idade"
        elif "@" not in cliente.email:
            return "Email inválido"
        elif len(cliente.nome) < 3:
            return "Nome deve ter mais de 3 caracteres"
        else:
            self.clientes_cadastrados.append(cliente)
            return "Cliente cadastrado com sucesso!"