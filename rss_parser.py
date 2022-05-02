import feedparser
file = feedparser.parse(r'feed.xml')

# El objeto file.feed contiene todas las etiquetas relativas al canal
print(" ")
print("*********************")
print(file.feed.description)
print("*********************")
print(" ")
# file.entries es un array con todas las entradas
for i in range(0,len(file.entries)):
  print("Noticia "+ str(i)+":") 
  print("--------------") 
  print(file.entries[i].title)
  print(file.entries[i].description)
  print(" ")
