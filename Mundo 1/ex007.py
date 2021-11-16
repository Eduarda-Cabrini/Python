medida = float(input('Uma distância em métros: '))
cm = medida * 100 
mm = medida * 1000
print('A média de {}m a {:.0f}cm e {:.0f}m '.format(medida, cm, mm))
