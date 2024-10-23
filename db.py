import sqlite3

class VocabDB():
    def __init__(self, filepath):
        self.conn = sqlite3.connect(filepath)
    
    def book_infos(self):
        cur = self.conn.cursor()
        res = cur.execute('SELECT id,lang,title,authors,asin FROM BOOK_INFO')
        items = res.fetchall()
        
        result = []
        for item in items:
            book = {'id':item[0], 'lang':item[1], 'title':item[2], 'authors':item[3], 'asin':item[4]}
            result.append(book)
        return result
    
    def words(self, book_id, timestamp=1):
        cur = self.conn.cursor()
        res = cur.execute(f'SELECT LOOKUPS.word_key,LOOKUPS.usage,WORDS.word,WORDS.stem,WORDS.lang,LOOKUPS.timestamp FROM LOOKUPS, WORDS WHERE LOOKUPS.word_key=WORDS.id AND LOOKUPS.book_key="{book_id}" AND LOOKUPS.timestamp>{timestamp}')
        all_words = res.fetchall()
        
        result = []
        for word_key in all_words:
            key = word_key[0]
            usage = word_key[1]
            word = word_key[2]
            stem = word_key[3].replace('・', '').replace('‐', '')
            lang = word_key[4]
            timestamp = word_key[5]
            item = {'word':word, 'key':key, 'usage':usage, 'stem':stem, 'lang':lang, 'definition':'', 'timestamp':timestamp}
            result.append(item)
        return result
