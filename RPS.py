# La función de ejemplo a continuación realiza un seguimiento del historial del oponente y reproduce lo que el oponente jugó hace dos jugadas.
ke = {}

def jugador(previo, historial_op=[]):
  global ke

  n = 5

  if previo in ["R","P","S"]:
    historial_op.append(previo)

  adiv = "R" # default, until statistic kicks in

  if len(historial_op)>n:
    inp = "".join(historial_op[-n:])

    if "".join(historial_op[-(n+1):]) in ke.keys():
      ke["".join(historial_op[-(n+1):])]+=1
    else:
      ke["".join(historial_op[-(n+1):])]=1

    posible =[inp+"R", inp+"P", inp+"S"]

    for i in posible:
      if not i in ke.keys():
        ke[i] = 0

    predict = max(posible, key=lambda key: ke[key])

    if predict[-1] == "P":
      adiv = "S"
    if predict[-1] == "R":
      adiv = "P"
    if predict[-1] == "S":
      adiv = "R"


  return adiv