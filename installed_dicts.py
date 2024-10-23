from en_dicts import DrEyeDictionary
from ja_dicts import DaijirinDictionary, DaijisenDictionary

INSTALLED_DICTS = {
    "en": [
        DrEyeDictionary('dictionaries/dict_dreye.jpg', 'dictionaries/DrEye')
    ],
    "ja": [ 
        DaijirinDictionary('dictionaries/dict_daijirin.jpg', 'dictionaries/SuperDaijirin'),
        DaijisenDictionary('dictionaries/dict_daijisen.jpg', 'dictionaries/daijisen')
    ]
}
