INSS (Instituto Naciona do Seguro Social)

O desconto do INSS é calculado de acordo com a faixa salarial do funcinário:
    * Salário ate R$ 1.100,00: 7,5%
    * Salário de R$ 1.100,01 até R$ 2203,48: 9%
    * Salário de R$ 2.203,49 até R$ 3.305,22: 12%
    * Salário de R$ 3.305,23 até R$ 6.433,57: 14%
    * O valor máximo de desconto do INSS é de R$ 854,36.
    
IRRF (Imposto de Renda Retido na Fonte)
O desconto do IRRF é calculado de acordo com a faixa salarial do funcionário e com a quantidade de dependentes:
    * Isento: Salário até R$ 2.259,20
    * 7,5%: Salário de RS 2.259,21 até R$ 2.826.65
    * 15%: Salário de 2.286,66 até R$ 3.751,05
    * 22,5%: Salário de R$ 3.751,05 até R$ 4.664,68
    * 27,5%: Salário acima de R$ 4.664,68
    * Dedução por dependente: R$ 189,59 por dependente.    
"""

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base