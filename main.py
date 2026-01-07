import csv
def dms_para_decimal(graus, minutos, segundos, hemisferio):
    
  valor_decimal = graus + (minutos / 60) + (segundos / 3600) 

  if hemisferio.upper() in ['S', 'W']: 
    valor_decimal *= -1 
    
  return valor_decimal
  
def main():
    print("=== GEO2DEC: Conversor de Coordenadas ===")
    coordenadas = []

    while True:
        grau = int(input("Digite os graus: "))
        minutos = int(input("Digite os minutos: ")
        segundos = int(input("Digite os segundos: ")
        hemisferio = input("Digite o hemisferio (N/S ou E/W").strip().upper()

        resultado = dms_para_decimal(grau, minutos, segundos, hemisferio)
        print (f"Coordenada em decimal: {resultado}")

        coordenadas.append([graus, minutos, segundos, hemisferio, resultado])

        continuar = input("Deseja converter outra coordenada? (S/N)").strip().uppe
          if continuar != 'S':
            break

with open("coordenadas_convertidas.csv", mode="w", newline="", encoding="utf-8") as arquivo: 
    escritor = csv.writer(arquivo) 
    escritor.writerow(["Graus", "Minutos", "Segundos", "Hemisfério", "Decimal"]) 
    escritor.writerows(coordenadas) 
  
  print("Arquivo 'coordenadas_convertidas.csv' salvo com sucesso!") 

if __name__ == "__main__": 
  main()
