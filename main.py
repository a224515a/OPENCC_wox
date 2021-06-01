'''pip install opencc-python-reimplemented'''
# from opencc import OpenCC
'''now we have official OpenCC binding for Python:
    pip install opencc'''
import opencc
import clipboard
from wox import Wox, WoxAPI

class Main(Wox):
    def copy(self, text):
        clipboard.copy(text)

    def convert_opencc_core(text, code):
        cc = opencc.OpenCC(code)
        convertedtext = cc.convert(text)
        # clipboard.copy(convertedtext)
        return convertedtext

    def selectcode(self, code):
        WoxAPI.change_query(code)

    def query(self, param):

        results = []

        if not param:
            results.append({
                "Title": '輸入任意文字，即可完成簡繁轉換',
                "SubTitle": 'opencc',
                "IcoPath": "Images/icon.png"
            })
            results.append({
                "Title": '前綴 "-t2s" 繁體到簡體',
                "SubTitle": "Traditional Chinese to Simplified Chinese",
                "IcoPath": "Images/t2s.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -t2s "],
                        "dontHideAfterAction": True
                        }
            })
            results.append({
                "Title": '前綴 "-s2twp" 簡體到繁體（臺灣正體標準）並轉換為臺灣常用詞彙',
                "SubTitle": "Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)",
                "IcoPath": "Images/s2twp.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -s2twp "],
                        "dontHideAfterAction": True
                        }
            })
            results.append({
                "Title": '前綴 "-s2tw" 簡體到臺灣正體',
                "SubTitle": "Simplified Chinese to Traditional Chinese (Taiwan standard)",
                "IcoPath": "Images/s2tw.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -s2tw "],
                        "dontHideAfterAction": True
                        }
            })
            results.append({
                "Title": '前綴 "-s2t" 簡體到繁體',
                "SubTitle": "Simplified Chinese to Traditional Chinese",
                "IcoPath": "Images/s2t.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -s2t "],
                        "dontHideAfterAction": True
                        }
            })
            results.append({
                "Title": '前綴 "-tw2sp" 繁體（臺灣正體標準）到簡體並轉換為中國大陸常用詞彙',
                "SubTitle": "Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)",
                "IcoPath": "Images/tw2sp.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -tw2sp "],
                        "dontHideAfterAction": True
                        }
            })
            results.append({
                "Title": '前綴 "-t2tw" 繁體（OpenCC 標準）到臺灣正體',
                "SubTitle": "Traditional Chinese to Traditional Chinese (Taiwan standard)",
                "IcoPath": "Images/t2tw.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -t2tw "],
                        "dontHideAfterAction": True
                        }
            })
            results.append({
                "Title": '前綴 "-tw2s" 臺灣正體到簡體',
                "SubTitle": "Traditional Chinese (Taiwan standard) to Simplified Chinese",
                "IcoPath": "Images/tw2s.png",
                "JsonRPCAction": {
                        "method": "selectcode",
                        "parameters": ["cc -tw2s "],
                        "dontHideAfterAction": True
                        }
            })           
            return results
        
        if param.lower().startswith("-s2twp"):
            code = "s2twp"
        elif param.lower().startswith("-s2tw"):
            code = "s2tw"
        elif param.lower().startswith("-s2t"):
            code = "s2t"
        elif param.lower().startswith("-s2hk"):
            code = "s2hk"
        elif param.lower().startswith("-hk2s"):
            code = "hk2s"
        elif param.lower().startswith("-hk2t"):
            code = "hk2t"
        elif param.lower().startswith("-t2s"):
            code = "t2s"
        elif param.lower().startswith("-t2hk"):
            code = "t2hk"
        elif param.lower().startswith("-t2tw"):
            code = "t2tw"
        elif param.lower().startswith("-tw2sp"):
            code = "tw2sp"
        elif param.lower().startswith("-tw2s"):
            code = "tw2s"
        elif param.lower().startswith("-tw2t"):
            code = "tw2t"
        elif param.lower().startswith("-t2jp"):
            code = "t2jp"
        elif param.lower().startswith("-jp2t"):
            code = "jp2t"
        else:
            converted1 = Main.convert_opencc_core(param, "s2twp")
            converted2 = Main.convert_opencc_core(param, "t2s")
            results.append({
                    "Title": converted1,
                    "SubTitle": "s2twp",
                    "IcoPath": "Images/s2twp.png",
                    'JsonRPCAction': {
                            'method': 'copy',
                            'parameters': [converted1]
                            }
                    })
            results.append({
                    "Title": converted2,
                    "SubTitle": "t2s",
                    "IcoPath": "Images/t2s.png",
                    'JsonRPCAction': {
                            'method': 'copy',
                            'parameters': [converted2]
                            }
                    })
            return results
        
        param = param[len(code)+1:len(param)]
        converted = Main.convert_opencc_core(param, code)

        results.append({
            "Title": converted,
            "SubTitle": code,
            "IcoPath": "Images/" + code + ".png",
            'JsonRPCAction': {
                'method': 'copy',
                'parameters': [converted]
            }
        })

        return results


if __name__ == "__main__":
    Main()
