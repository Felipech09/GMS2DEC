# GMS2DEC – Conversor de Coordenadas Geográficas

## 📌 O que é
O **GMS2DEC** é um programa em Python que converte coordenadas geográficas no formato  
**GMS (Graus, Minutos e Segundos)** para **graus decimais**.

Ele trabalha com **latitude e longitude**, formando uma coordenada completa e válida para mapas.

---

## 🎯 Para que serve
- Converter coordenadas usadas em mapas, GPS e geografia
- Facilitar cálculos e visualizações em ferramentas como Google Maps
- Gera um arquivo em csv para facilitar a importação para outros sistemas

---

## ⚙️ Como o programa funciona
1. O usuário informa:
   - Latitude (graus, minutos, segundos e hemisfério)
   - Longitude (graus, minutos, segundos e hemisfério)
2. O programa converte cada valor de GMS para decimal
3. Os dados são exibidos no terminal
4. As coordenadas são salvas em um arquivo CSV
5. O usuário pode adicionar várias coordenadas no mesmo arquivo
6. Ao encerrar, o arquivo CSV é salvo automaticamente

- Cada execução do programa gera **um novo arquivo CSV**, evitando sobrescrita.
- O nome do arquivo inclui data e hora, por exemplo
