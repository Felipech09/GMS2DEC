import csv
from datetime import datetime

def dms_para_decimal(graus, minutos, segundos, hemisferio):
    valor_decimal = graus + (minutos / 60) + (segundos / 3600)
    if hemisferio in ['S', 'W']:
        valor_decimal *= -1
    return valor_decimal


def ler_coordenada(tipo):
    print(f"\n--- {tipo.upper()} ---")
    graus = int(input("Graus: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    hemisferio = input("Hemisfério (N/S ou E/W): ").strip().upper()
    return graus, minutos, segundos, hemisferio

def main():
    print("=== GEO2DEC: Conversor de Coordenadas ===")

    # Arquivo com nome único
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"coordenadas_{data_hora}.csv"

    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        while True:
            # LATITUDE
            g_lat, m_lat, s_lat, h_lat = ler_coordenada("Latitude")
            lat_dec = dms_para_decimal(g_lat, m_lat, s_lat, h_lat)

            # LONGITUDE
            g_lon, m_lon, s_lon, h_lon = ler_coordenada("Longitude")
            lon_dec = dms_para_decimal(g_lon, m_lon, s_lon, h_lon)

            # BLOCO LATITUDE
            escritor.writerow(
                ["Lat Graus", "Lat Minutos", "Lat Segundos", "Lat Hemisfério", "Latitude Decimal"]
            )
            escritor.writerow([g_lat, m_lat, s_lat, h_lat, lat_dec])

            # BLOCO LONGITUDE
            escritor.writerow(
                ["Lon Graus", "Lon Minutos", "Lon Segundos", "Lon Hemisfério", "Longitude Decimal"]
            )
            escritor.writerow([g_lon, m_lon, s_lon, h_lon, lon_dec])

            escritor.writerow([])  # Linha propositalmente em branco para melhorar visualização

            continuar = input("Adicionar outra coordenada neste arquivo? (S/N): ").strip().upper()
            if continuar != 'S':
                break

    print(f"\nArquivo '{nome_arquivo}' gerado com sucesso!")


if __name__ == "__main__":
    main()
