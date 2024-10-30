import bs4
from dicts import StardictDictionary, JsonDictionary

class DaijirinDictionary(JsonDictionary):
    def __init__(self, cover_image, file_prefix_path):
        super().__init__(cover_image, file_prefix_path)

    def query(self, term):
        definitions = super().query_as_list(term)
        if len(definitions) > 0:
            result = []
            for defi in definitions:
                result.append(defi)
            return "\n\n".join(result)
        return ''

class DaijisenDictionary(JsonDictionary):
    def __init__(self, cover_image, file_prefix_path):
        super().__init__(cover_image, file_prefix_path)

    def query(self, term):
        definitions = super().query_as_list(term)
        if len(definitions) > 0:
            result = []
            for defi in definitions:
                result.append(defi)
            return "\n\n".join(result)
        return ''

class OldDaijirinDictionary(StardictDictionary):
    def __init__(self, cover_image, filepath):
        super().__init__('三省堂·スーパー大辞林', 'ja', cover_image, filepath)

    def query(self, term):
        definition = self.stardict.get(term).strip()
        if definition != '':
            definition = self.parse_definition(definition)
        return definition

    def parse_definition(self, text):
        result_texts = []
        objSoup = bs4.BeautifulSoup(text, 'lxml')
        tag_hg = objSoup.find('span', 'hg')
        hg = tag_hg.text
        result_texts.append(f"<p>{hg}</p>")
        tag_sg_list = objSoup.find_all('span', 'sg')

        for tag_sg in tag_sg_list:
            tag_posg = tag_sg.find('span', 'posg')
            if tag_posg:
                pos = tag_posg.text
                result_texts.append(f"<p>{pos}</p>")
                
            tag_tcord = tag_sg.find_all('span', 't_core')
            for tcord in tag_tcord:
                result_texts.append(f"<p>{tcord.text}</p>")
            result_texts.append("<br/>")

            tag_tsubsence = tag_sg.find_all('span', 't_large')
            for tsubsence in tag_tsubsence:
                result_texts.append(f"<p>{tsubsence.text}</p>")
            if len(tag_tsubsence) > 0:
                result_texts.append("<br/>")

            tag_infg_list = tag_sg.find_all('span', 'infg')
            for tag_infg in tag_infg_list:
                tag_lbl = tag_infg.find('span', 'lbl')
                tag_inf = tag_infg.find('span', 'inf')
                result_texts.append(f"[{tag_lbl.text}] {tag_inf.text}")

            tag_deri_list = objSoup.find_all('span', 't_derivatives')

            for tag_deri in tag_deri_list:
                result_texts.append(f"<p>{tag_deri.text}</p>")
        return "\n".join(result_texts)

class OldDaijisenDictionary(StardictDictionary):
    def __init__(self, cover_image, filepath):
        super().__init__('小学館·大辞泉', 'ja', cover_image, filepath)

    def query(self, term):
        definition = self.stardict.get(term).strip()
        if definition != '':
            definition = self.parse_definition(definition)
        return definition

    def parse_definition(self, text):
        result_texts = []
        objSoup = bs4.BeautifulSoup(text, 'lxml')
        tag_head = objSoup.find('span', '見出G')
        result_texts.append(f"<p>{tag_head.text}</p>")
        tag_meaning_list = objSoup.find_all('meaning')
        for meaning in tag_meaning_list:
            result_texts.append(f"<p>{meaning.text}</p>")
        return "\n".join(result_texts)
