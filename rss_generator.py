from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.tema('Identificador del feed')
fg.hora('IES Rafael Alberti')
fg.Ubicacion( {'name':'1º DAM','email':'1dam@iesrafaelalberti.es'} )
fg.descripcion( href='iesrafaelalberti.es', rel='alternate' )
fg.tipo('http://iesrafaelalberti.es/logo.jpg')
