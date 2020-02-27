# OPENCC_wox
  A [Wox](https://github.com/Wox-launcher/Wox).Plugin that converts between Traditional Chinese and Simplified Chinese using [OpenCC](https://github.com/BYVoid/OpenCC).

## Getting Started

  OpenCC (Open Chinese Convert, 開放中文轉換) 是相當知名的中文簡繁轉換開源項目。
  [yichen0831](https://github.com/yichen0831/opencc-python) 將其改寫為純 Python程式碼，可相當輕鬆的整合到 Wox。


### Installing

將資料夾存放在 ..\AppData\Roaming\Wox\Plugins\ 下即可使用。

(需先安裝 `opencc-python`)
> `pip install opencc-python-reimplemented`

### Usage 

- 輸入關鍵詞 (`opencc`) 及簡體中文，直接轉換為臺灣正體(符合台灣常用詞彙)。
- 輸入關鍵詞 (`opencc`) 及目標文字，並在 `:` 後指定轉換格式。

#### Conversions
  * `hk2s`: Traditional Chinese (Hong Kong standard) to Simplified Chinese

  * `s2hk`: Simplified Chinese to Traditional Chinese (Hong Kong standard)

  * `s2t`: Simplified Chinese to Traditional Chinese

  * `s2tw`: Simplified Chinese to Traditional Chinese (Taiwan standard)

  * `s2twp`: Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)

  * `t2hk`: Traditional Chinese to Traditional Chinese (Hong Kong standard)

  * `t2s`: Traditional Chinese to Simplified Chinese

  * `t2tw`: Traditional Chinese to Traditional Chinese (Taiwan standard)

  * `tw2s`: Traditional Chinese (Taiwan standard) to Simplified Chinese

  * `tw2sp`: Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases) 

## Credits
[yichen0831](https://github.com/yichen0831/opencc-python) for [opencc-python](https://github.com/yichen0831/opencc-python).
