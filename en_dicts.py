import bs4
from dicts import StardictDictionary

class DrEyeDictionary(StardictDictionary):
    def __init__(self, cover_image, filepath):
        super().__init__('譯典通英漢雙向辭典', 'en', cover_image, filepath)

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

            tag_deri_list = objSoup.find_all('span', 't_derivatives')

            for tag_deri in tag_deri_list:
                result_texts.append(f"<p>{tag_deri.text}</p>")
        return "\n".join(result_texts)

