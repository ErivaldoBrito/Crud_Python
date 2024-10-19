"""
INSS (Instituto Nacional do Seguro Social)
O desconto do INSS é calculado de acordo com a faixa salarial do funcionário:

Salário até R$ 1.100,00: 7,5%
Salário de R$ 1.100,01 até R$ 2.203,48: 9%
Salário de R$ 2.203,49 até R$ 3.305,22: 12%
Salário de R$ 3.305,23 até R$ 6.433,57: 14%
O valor máximo de desconto do INSS é de R$ 854,36.

áximo de desconto do INSS é de R$ 854,36.
IRRF (Imposto de Renda Retido na Fonte)
O desconto do IRRF é calculado de acordo com a faixa salarial do funcionário e com a quantidade de dependentes:

Isento: Salário até R$ 2.259,20
7,5%: Salário de R$ 2.259,21 até R$ 2.826,65
15%: Salário de R$ 2.826,66 até R$ 3.751,05
22,5%: Salário de R$ 3.751,06 até R$ 4.664,68
27,5%: Salário acima de R$ 4.664,68
Dedução por dependente: R$ 189,59 por dependente.
Vale Transporte
Desconto de 6% do salário base do funcionário, caso opte pelo benefício.

Vale Refeição
Desconto de 20% do valor do benefício fornecido pela empresa.

Plano de Saúde
Desconto fixo de R$ 150,00 por dependente.

Instruções
Solicite a matrícula e senha do funcionário para ter acesso aos seus dados.
Solicite o salário base do funcionário.
Pergunte se o funcionário deseja receber vale transporte (s/n).
Pergunte o valor do vale refeição fornecido pela empresa.
Calcule os descontos e acréscimos na folha de pagamento do funcionário.
Mostre o salário líquido do funcionário após os descontos e acréscimos.
Observações
Considere que o funcionário possui apenas um dependente.
Considere que o salário base é o salário antes de quaisquer descontos ou acréscimos.
Considere que o salário base, o vale refeição e o plano de saúde são informados em reais (R$).
Exemplos de Cálculo
Exemplo 1: Salário Baixo (R$ 1.412,00) com 0 Dependentes e Vale Transporte
Salário Base: R$ 1.412,00
Dependentes: 0
Vale Transporte: Sim
Vale Refeição: R$ 300,00
Salário Líquido: R$ 1.161,38

Exemplo 2: Salário Alto (R$ 10.000,00) com 2 Dependentes e Sem Vale Transporte
Salário Base: R$ 10.000,00
Dependentes: 2
Vale Transporte: Não
Vale Refeição: R$ 500,00
Salário Líquido: R$ 6.400,92
"""

# Calculo do imposto sobre o salário de um funcionário.

def calcular_inss(salario):
    if salario <= 1100.00:
        desconto = salario * 0.075
    elif salario <= 2203.48:
        desconto = salario * 0.09
    elif salario <= 3305.22:
        desconto = salario * 0.12
    elif salario <= 6433.57:
        desconto = salario * 0.14
    else:
        desconto = 854.36
    return desconto

def calcular_irrf(salario, dependentes):
    deducao_dependente = 189.59 * dependentes
    base_calculo = salario - deducao_dependente
    
    if base_calculo <= 2259.20:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225
    else:
        return base_calculo * 0.275

def calcular_descontos(salario, vale_transporte, vale_refeicao, dependentes):
    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario, dependentes)
    transporte = salario * 0.06 if vale_transporte else 0
    refeicao = vale_refeicao * 0.20
    
    total_descontos = inss + irrf + transporte + refeicao
    return total_descontos

def main():
    print("=== Cálculo da Folha de Pagamento ===")
    matricula = input("Digite a matrícula do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    salario = float(input("Digite o salário base do funcionário: R$ "))
    vale_transporte = input("Deseja receber vale transporte? (s/n): ").strip().lower() == 's'
    vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa: R$ "))
    dependentes = 1  # Considerando apenas um dependente conforme especificado

    descontos = calcular_descontos(salario, vale_transporte, vale_refeicao, dependentes)
    salario_liquido = salario - descontos

    print(f"\nSalário Base: R$ {salario:.2f}")
    print(f"Total de Descontos: R$ {descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()
