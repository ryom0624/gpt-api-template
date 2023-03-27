import env
import openai
from datetime import datetime

start_time = datetime.now()

# OpenAI APIの認証情報を環境変数から読み込む
openai.api_key = env.OPENAI_API_KEY
model_name = "gpt-3.5-turbo"
# model_name = "gpt-4" # API開放待ち

# システムの設定
system = """\
あなたは優秀なプログラマです。
"""

# チャットボットの質問を入力する。
question = """\
GPT3.5のAPIを使うサンプルを作って。
"""


""" コメント
system: AIアシスタントの設定などを記述（キャラとか）
assistant: AIアシスタントの発話（AIからの返答を含むこれまでの会話を全て送ることで、その文脈を踏まえて回答してもらえるようにするため）
user: ユーザーの発話
"""
response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": question},
        # {"role": "assistant", "content": "Answer"},
    ],
)

end_time = datetime.now()

print(response.choices[0]["message"]["content"].strip())
print(f"elapsed time: {end_time - start_time}")

# write to output-${yyyymmddthhmmss}.txt
# with open(f"./outputs/output-{model_name}-{datetime.now().strftime('%Y%m%dT%H%M%S')}-{question}.txt", "w") as f:
#     f.write(f"model: {model_name}\n")
#     f.write("time: " + str(end_time - start_time) + "\n")
#     f.write("question: " + question + "\n")
#     f.write("answer: " + response.choices[0]["message"]["content"].strip() + "\n")
