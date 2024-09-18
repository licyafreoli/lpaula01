salario_mensal = float(input("Digite quanto você ganha por mês: "))
horas_semana = float(input("Digite o número de horas trabalhadas por semana: "))

total_horas_mes = horas_semana * 4
salario_por_hora = salario_mensal / total_horas_mes
print(f"O seu salário por hora é: R$ {salario_por_hora:.2f}")

