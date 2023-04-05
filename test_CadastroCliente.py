# -*- coding: utf-8 -*-

from Cliente import Cliente
from CadastroCliente import CadastroCliente

def test_que_cliente_seja_cadastrado_com_sucesso():
        cliente = Cliente("João", 20, "test@gmail.com")
        cadastro = CadastroCliente()
        resposta = cadastro.cadastrar_cliente(cliente)
        assert "Cliente cadastrado com sucesso!" == resposta

# Teste cliente não pose ser menor de idade
def test_que_cliente_nao_seja_cadastrado_com_menor_de_idade():
        cliente = Cliente("João", 17, "test@gmail.com")
        cadastro = CadastroCliente()
        resposta = cadastro.cadastrar_cliente(cliente)
        assert "Cliente não pode ser menor de idade" == resposta

# Teste email deve ser válido
def test_que_cliente_nao_seja_cadastrado_com_email_invalido():
        cliente = Cliente("João", 20, "testgmail.com")
        cadastro = CadastroCliente()
        resposta = cadastro.cadastrar_cliente(cliente)
        assert "Email inválido" == resposta

# Cliente não pode ter nome com menos de três caracteres
def test_que_cliente_nao_seja_cadastrado_com_nome_com_menos_de_tres_caracteres():
        cliente = Cliente("Jo", 20, "test@gmail.com")
        cadastro = CadastroCliente()
        resposta = cadastro.cadastrar_cliente(cliente)
        assert "Nome deve ter mais de 3 caracteres" == resposta