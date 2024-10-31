import json
#import pystardict

class VocabDictionary():
    def __init__(self, name, lang, cover_image):
        self.name = name
        self.lang = lang
        self.cover_image = cover_image
        self._loaded = False
        
    def load(self):
        self._loaded = True

    def unload(self):
        self._loaded = False

    def is_loaded(self):
        return self._loaded

    def query(self, term):
        return ''

#class StardictDictionary(VocabDictionary):
#	def __init__(self, name, lang, cover_image, filepath):
#		super().__init__(name, lang, cover_image)
#		self.stardict = pystardict.Dictionary(filepath)
#
#	def query(self, term):
#	    return self.stardict.get(term).strip() 

class JsonDictionary(VocabDictionary):
    def __init__(self, cover_image, file_prefix_path):
        super().__init__('Default Name', 'en', cover_image)
        self.file_prefix_path = file_prefix_path
        self.info = {}
        self.indexes = {}
        self.definitions = {}
        
        self.load_info()

    def load_info(self):
        file_jifo = f"{self.file_prefix_path}.jifo"
        try:
            with open(file_jifo, 'r', encoding='utf-8') as f:
                self.info = json.load(f)
            self.name = self.info['name']
            self.lang = self.info['lang']
        except:
            print("Load jidx file Error!")
        
    def load_indexes(self):
        file_jidx = f"{self.file_prefix_path}.jidx"
        try:
            with open(file_jidx, 'r', encoding='utf-8') as f:
                self.indexes = json.load(f)
        except:
            print("Load jidx file Error!")
            return False
        return True
    
    def load_definitions(self):
        file_jdict = f"{self.file_prefix_path}.jdict"
        try:
            with open(file_jdict, 'r', encoding='utf-8') as f:
                self.definitions = json.load(f)
        except:
            print("Load jdict file Error!")
            return False
        return True

    def load(self):
        self.load_indexes()
        self.load_definitions()
        self._loaded = True

    def unload(self):
        self.indexes = None
        self.definitions = None
        self.indexes = {}
        self.definitions = {}
        self._loaded = False

    def query(self, term):
        if term in self.indexes:
            word_ids = self.indexes[term]
            defis = []
            for wid in word_ids:
                defis.append(self.definitions[wid])
            return "\n\n".join(defis)
        return ''

    def query_as_list(self, term):
        if term in self.indexes:
            word_ids = self.indexes[term]
            defis = []
            for wid in word_ids:
                defis.append(self.definitions[wid])
            return defis
        return []
	
