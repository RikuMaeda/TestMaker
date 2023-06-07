import os
import openai
from PIL import Image
import pyocr

#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'C:\\Users\\maeda\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#文字を抽出したい画像のパスを選ぶ
img = Image.open('C:\\python_portfolio\\TestMaker\\png\\pychology.png')

#画像の文字を抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

print(text)

# APIキーの設定
openai.api_key = "API_KEY"

assistant_roll = input("科目名を入れてください")
system_request = "あなたは{}の大学教授です"
system_result = system_request.format(assistant_roll)

user_request = "{}に類似した問題とその答えを作成してください"
user_result = user_request.format(text)


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_result},
        {"role": "user", "content": user_result},
    ],
)
print(response.choices[0]["message"]["content"].strip())