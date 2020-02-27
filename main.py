from opencc import OpenCC
import clipboard
from wox import Wox, WoxAPI

class Main(Wox):

    def copy(self, text):
	
        clipboard.copy(text)
		
    def query(self, param):
	
        results = []
		
        if not param:
            results.append({
                "Title": '簡繁轉換',
                "SubTitle": 'Conversions',
                "IcoPath": "Images/icon.png"
            })
            return results

        if len(param.split(':')) == 2:
            code = param.split(':')[1]
            if code.endswith("s2t"):			
                code = "s2t"
            elif code.endswith("s2tw"):			
                code = "s2tw"
            elif code.endswith("s2twp"):
                code = "s2twp"
            elif code.endswith("hk2s"):
                code = "hk2s"
            elif code.endswith("s2hk"):
                code = "s2hk"
            elif code.endswith("t2hk"):
                code = "t2hk"			
            elif code.endswith("t2s"):
                code = "t2s"
            elif code.endswith("t2tw"):
                code = "t2tw"
            elif code.endswith("tw2s"):
                code = "tw2s"
            elif code.endswith("tw2sp"):
                code = "tw2sp"
            else:
                code = "s2twp"
        else:
            code = "s2twp"
            
        cc = OpenCC(code)
        converted = cc.convert(param.split(':')[0])
		
        results.append({
            "Title": converted,
            "SubTitle": code,
            "IcoPath": "Images/"+code+".png",
            'JsonRPCAction': {
                'method': 'copy',
                'parameters': [converted]
            }
            })

        return results



if __name__ == "__main__":
    Main()
