# Kindle VocabMate
將 Kindle 生詞本導出轉換成可匯入 Anki 牌組之工具。以 Python 語言開發之跨平台圖形介面工具，目前支援 Windows、macOS 與 Unix-like 平台。

最新版本請在[這裡](https://github.com/mainlander/KindleVocabMate/releases/tag/v1.0)下載。

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

### 1. 安裝字典

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

### 2. 導入 Kindle 生詞本

於主畫面上方的「Kindle vocab.db 檔案路徑」輸入框，用於輸入 Kindle 生詞本資料庫檔案之路徑。Kindle 生詞本之資料庫位於 Kindle 設備的 `system/vocabulary/vocab.db`，此資料夾為隱藏資料夾，預設不可見。

可點選輸入框右方的「開啟...」按鈕，手動選擇 Kindle 生詞本資料庫 vocab.db 檔案的位置。若於 Kindle 設備以 USB 傳輸線連接電腦的情況下，可按下右方的「自動偵測」按鈕，KindleVocabMate 會自動偵測 Kindle 設備及 vocab.db 檔案之路徑，無需手動選取。自動偵測功能，目前僅於 Windows 與 macOS 平台有效。

手動選擇或自動偵測 Kindle 生詞本資料庫 vocab.db 檔案路徑後，按下右方之「載入DB」按鈕，即可載入 Kindle 生詞本內容。初次載入時會自動從 Amazon 網站下載書籍封面，會需要比較長的時間。

![load_db](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-load-db.png)

### 3. 選擇書籍與時間點

Kindle 生詞本資料庫載入完成後，主畫面左方的書籍列表即會顯示於 Kindle 設備中曾查閱過的書籍清單，若為 Amazon 上所購買之書籍會顯示其於 Amazon 的書籍封面。

於書籍列表清單中可選擇欲匯出之書籍，若要匯出所有的書籍中的生詞，可選擇第一項「全部書籍」。

![select_book](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-select-book.png)

擇定書籍之後，下方之「在此時間點之後：」之輸入框為設定匯入單詞之時間點 Timestamp，於設定的時間點**之後**曾進行查詢的生詞才會匯入。該 Timestamp 時間點為 Unix Epoch Time 格式，可點選輸入框右方的「日期...」按鈕，以點選之方式便捷選擇時間。若保持預設值 1 的話，無論時間為何，會匯入所有的生詞。

![select_time](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-select-timestamp.png)

選擇書籍並設定時間點之後，便可按下下方的「載入生詞」按鈕，將選擇之書籍於設定之時間點之後所查詢的生詞載入 KindleVocabMate。

### 4. 增加解釋

載入生詞完成後，於主畫面右上方會顯示載入之生詞表格，每一列即為所選之書籍中曾查閱之生詞，及該詞於書中的用例，最右欄之「解釋」欄位初始值為空值。

![load_vocab](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-load-vocab.png)

於生詞表格下方之「字典語言」下拉式選單中可依據語言分類切換所安裝之字典，而後請點選想使用的字典，再按下右方的「增加解釋」按鈕，KindleVocabMate 即會將生詞表格中的每一個生詞，查詢所選擇之字典，將字典中之解釋填入生詞表格中之「解釋」欄位。

![add_definition](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-add-definition.png)

若該生詞於字典中找不到解釋，則生詞表格中之「解釋」欄位仍會保持空值。此時可點選另一本字典，再次按下「增加解釋」按鈕，KindleVocabMate 會再次將仍未有解釋的生詞，查詢選擇的字典，將字典之解釋填入欄位之中。

### 5. 匯出 TSV 檔案

生詞增加解釋完成後，可於生格表格中檢視結果。確認內容無誤後，按下最下方之「匯出成 TSV 檔案」按鈕，即可將完成之結果，匯出成 Anki 可使用之 TSV 格式檔案，可於 Anki 匯入牌組時使用。點選「匯出成 TSV 檔案」按鈕後，會打開作業系統預設之儲存檔案對話框，可選擇欲存檔之路徑。檔名預設為「**{書籍名稱}-{現在日期}-{Timestamp}.tsv**」，其中之 Timestamp 為本次匯出之所有生詞中最晚之時間點，可用於下一次導入生詞時設定時間點之參考。

![export_tsv](https://raw.githubusercontent.com/mainlander/KindleVocabMate/refs/heads/main/screenshot/screen-export-tsv.png)
