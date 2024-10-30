import sys, os
import os.path
from en_dicts import DrEyeDictionary
from ja_dicts import DaijirinDictionary, DaijisenDictionary

basedir = os.path.dirname(__file__)

INSTALLED_DICTS = {
    "en": [
        DrEyeDictionary(os.path.join('dictionaries', 'dict_dreye.jpg'), os.path.join('dictionaries', 'DrEye'))
    ],
    "ja": [ 
        DaijirinDictionary(os.path.join('dictionaries', 'dict_daijirin.jpg'), os.path.join('dictionaries', 'daijirin')),
        DaijisenDictionary(os.path.join('dictionaries', 'dict_daijisen.jpg'), os.path.join('dictionaries', 'daijisen'))
    ]
}
