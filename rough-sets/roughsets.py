from twd import TWD

# Tabela de decisão
dt = [["y","y","normal",   "n"],
      ["y","n","high",     "y"],
      ["y","y","normal",   "y"],
      ["n","y","normal",   "n"],
      ["n","n","high",     "n"],
      ["n","y","very high","y"]]

# Labels de informações
labels = ["headache","muscle pain", "temperature"]

#Criação do objeto roughset
rs = TWD(dt,labels)

# Conjunto universo (todos os objetos da tabela de decisão)
U = rs.getU()

# Casos positivos
casos_positivos = rs.getX("y")

indiscernibilidade = rs.getIND(labels) # Indiscernibilidade

rs.getLowerAX(casos_positivos, indiscernibilidade) #Aproximação inferior
rs.getUpperAX(casos_positivos, indiscernibilidade) #Aproximação superior

rs.precision(casos_positivos, indiscernibilidade) #Precisão da aproximação
rs.quality(casos_positivos, indiscernibilidade) #Qualidade da aproximação
rs.roughness(casos_positivos, indiscernibilidade) # Imprecisão do conjunto