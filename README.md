# Kindle VocabMate
將 Kindle 生詞本導出轉換成可匯入 Anki 牌組之工具。以 Python 語言開發之跨平台圖形介面工具，目前支援 Windows、macOS 與 Unix-like 平台。

## 開發環境需求
* Python 3
* PyQt6
* wmi (僅於Windows平台)

## 安裝方式
### Windows
1. 下載 KindleVocabMate 應用程式壓縮檔
2. 解開 zip 壓縮檔案
3. 進入 KindleVocabMate 目錄
4. 執行 KindeVocabMate.exe 檔案

### macOS
1. 下載 KindleVocabMate 應用程式之磁碟映像檔
2. 雙擊掛載 DMG 碰碟映像檔
3. 將 KindleVocabMate 拖曵至 Application 資料夾

### Unix-like (Linux、FreeBSD…)
1. 安裝 Python 3
2. 安裝 PyQt6
3. 下載 KindleVocabMate 專案原始碼
4. 進入 KindleVocabMate 目錄
5. 執行 python main.py

## 使用手冊
### 主畫面
![mainwindow](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-main.png)

### 使用步驟
#### 1. 安裝字典

初次啟動 KindleVocabMate 時，會出現未安裝字典的提示對話框：

![no_dict](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-no-dict-messagebox.png)

KindleVocabMate 需要額外安裝的字典，才能將 Kindle 生詞本裡的生詞增加解釋內容，作為 Anki 單字卡的背面項目。由於字典多為版權物，無法隨本專案一併散佈提供，請自行取得。

KindleVocabMate 使用的字典為專屬的 JSON 格式，如您需使用自己的字典，請參考本專案裡的 [auxiliary/JSON Dict Processing.ipynb](https://github.com/mainlander/KindleVocabMate/blob/main/auxiliary/JSON%20Dict%20Processing.ipynb) 檔案，將您的字典轉換成 KindleVocabMate 使用的格式。

一個完整的字典需包含如下四個檔案：
* 字典檔名.jifo
* 字典檔名.jidx
* 字典檔名.jdict
* 字典封面圖檔 (JPEG 或 PNG 格式)

欲新增字典，請點選主功能表的「設定」選單中的「管理字典...」項目：

![setting](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-menu-settings.png)

於「已安裝的字典」對話框中，點選「新增」按鈕：

![ins_dict](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-dict-dialog.png)

於「新增字典」對話框中，設定字典的 .jifo 檔案與封面圖檔的路徑，可點選輸入框右方的「開啟...」按鈕，打開作業系統的檔案選擇對話框，選擇相應的檔案。

![add_dict](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-add-dict-dialog.png)

完成後按下「確定」按鈕，若字典檔案正常載入，即回到「已安裝的字典」對話框，並可看到新增的字典已出現於選單之中。

![ins_dict_finish](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-add-dict-finish.png)

若欲新增其它字典，請重覆以上操作流程。
