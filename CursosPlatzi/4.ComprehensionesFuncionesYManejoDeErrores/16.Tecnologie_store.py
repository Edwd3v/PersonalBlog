def message_creator(text):
   
   options = {'computadora':'Con mi computadora puedo programar usando Python', 'celular':'En mi celular puedo aprender usando la app de Platzi', 'cable':'¡Hay un cable en mi bota!'}

   if text in options.keys():
      return options[text]
   else:
      return 'Articulo no encontrado'

text = 'comida'
response = message_creator(text)
print(response)