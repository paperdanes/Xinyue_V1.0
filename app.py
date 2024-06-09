import os

os.system("python download_model.py ajupyter/EmoLLM_aiwei")
os.system('streamlit run web_demo-aiwei.py --server.address=0.0.0.0 --server.port 7860')

