# Import the Python SDK
import google.generativeai as genai
import streamlit as st
import os

#API_KEYの設定
#環境変数にAPI_KEYを設定した
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

#モデルを初期化する
model = genai.GenerativeModel('gemini-pro')

# アプリのタイトル
st.title("勝手に選書アプリ")

# ユーザーからの情報を収集
age = st.sidebar.number_input("年齢", min_value=0, max_value=120, step=1, value=43)
gender = st.sidebar.selectbox("性別", ["男性", "女性", "その他"], index=0)
genre1 = st.sidebar.selectbox("好きな本のジャンル❶", ["推理","絵本","歴史", "文化","戦争","経済","子供","勉強","健康","人生","宗教","ファンタジー", "SF", "ミステリー", "ノンフィクション", "ロマンス", "自己啓発", "ホラー", "ビジネス書", "IT","統計学","AI","その他"], index=0)
genre2 = st.sidebar.selectbox("好きな本のジャンル❷", ["推理","絵本","歴史", "文化","戦争","経済","子供","勉強","健康","人生","宗教","ファンタジー", "SF", "ミステリー", "ノンフィクション", "ロマンス", "自己啓発", "ホラー", "ビジネス書", "IT","統計学","AI","その他"], index=0)
genre3 = st.sidebar.selectbox("好きな本のジャンル❸", ["推理","絵本","歴史", "文化","戦争","経済","子供","勉強","健康","人生","宗教","ファンタジー", "SF", "ミステリー", "ノンフィクション", "ロマンス", "自己啓発", "ホラー", "ビジネス書", "IT","統計学","AI","その他"], index=0)
hobby1 = st.sidebar.text_input("趣味や好きなことは？",value="複数記載するときは「、」で区切ってください")
hobby2 = st.sidebar.text_input("嫌いなことは？", value="複数記載するときは「、」で区切ってください")
mood1 = st.sidebar.selectbox("今の気持ちは？❶", ["喜び","悲しみ","愛情","不安","怒り","驚き","嫌気","信頼"])
mood2 = st.sidebar.selectbox("今の気持ちは？❷", ["喜び","悲しみ","愛情","不安","怒り","驚き","嫌気","信頼"])
purpose = st.sidebar.text_input("本を読む目的は？", "元気になりたい")
favorite_author = st.sidebar.text_input("好きな作家", "養老孟司")
personality = st.sidebar.text_input("性格", "飽きっぽい、好奇心旺盛")
prompt = "読書大好き"
#推薦ボタン
if st.button("おすすめの本を教えて"):
    # プロンプトの生成
    prompt = f"""
    以下の情報を基に、おすすめの本を3冊教えてください。それぞれの本について、タイトル、著者、簡単な内容（200文字）、おすすめした理由（200文字）を表示してください。
    年齢: {age}
    性別: {gender}
    好きな本のジャンル❶: {genre1}
    好きな本のジャンル❷: {genre2}
    好きな本のジャンル❸: {genre3}
    趣味や好きなこと❶: {hobby1}
    嫌いなこと❷: {hobby2}
    今の気持ち❶: {mood1}
    今の気持ち❷: {mood2}
    本を読む目的: {purpose}
    好きな作家: {favorite_author}
    性格: {personality}
    """



response = model.generate_content(prompt)
st.write(response.text)
    
    
