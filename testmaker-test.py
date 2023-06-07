import os
import openai
from PIL import Image
import pyocr

assistant_roll = input("科目名を入れてください")
system_request = "あなたは{}の大学教授です"
system_result = system_request.format(assistant_roll)
print(system_result)

text = "77616, 267540の最大公約数を,ユークリッドの互除法によって求めなさい。"
user_request = "{}に類似した問題とその答えを作成してください"
user_result = user_request.format(text)
print(user_result)