"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

"""

Nesta aula o professor falou que o quanto menos complicado for o seu código melhor e também falou que a complexibilidade vai sempre vir de que te contratar. 

"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
    
if vel_carro_pass_radar_1:
    print('Velocidade carro passou do rada 1')

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print('Carro multado em radar 1')








