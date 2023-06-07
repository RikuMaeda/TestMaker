import os
import openai
from PIL import Image
import pyocr

text = "77616, 267540の最大公約数を,ユークリッドの互除法によって求めなさい。"

# APIキーの設定
openai.api_key = "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"

assistant_roll = input("科目名を入れてください：")

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