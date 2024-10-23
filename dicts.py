import pystardict

class VocabDictionary():
    def __init__(self, name, lang, cover_image):
        self.name = name
        self.lang = lang
        self.cover_image = cover_image
        
    def query(self, term):
        return ''

class StardictDictionary(VocabDictionary):
	def __init__(self, name, lang, cover_image, filepath):
		super().__init__(name, lang, cover_image)
		self.stardict = pystardict.Dictionary(filepath)

	def query(self, term):
	    return self.stardict.get(term).strip() 
