from Televisor import Televisor
from ControleRemoto import ControleRemoto

tv = Televisor('SONY', 'SONY-123')
controle = ControleRemoto(tv)

controle.sintonizaCanal('GLOBO')
controle.trocaDeCanal('GLOBO')
print(tv.canal_atual)