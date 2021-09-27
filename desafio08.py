medida = float(input('Digite uma distância em mêtros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {} corresponde a {:.0f} cm e {:.0f} mm '.format(medida, cm, mm))
