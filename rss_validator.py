import feedvalidator
archivo = open("feed_ejemplo.xml", "rb") 
feedvalidator.validateStream(archivo)