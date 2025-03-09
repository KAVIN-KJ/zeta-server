import json
from flask import Flask,request,jsonify 
import subprocess
import os
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_KEY")


import os
app = Flask(__name__)
CORS(app)

# COMPILE AND RUN
@app.route('/run',methods=['POST'])
def run():
    data = request.json
    code = data["code"]
    code_ip = data["input"]
    language = data["language"]
    filename = ""
    if language=="py":
        filename = "run.py"
    elif language=="java":
        filename = "run.java"
    elif language=="cpp":
        filename = "run.cpp"
        
    print("Request received\n",code,code_ip,filename)
    
    os.makedirs("./user-codes", exist_ok=True)
    
    file_path = f"./user-codes/{filename}"
    dir_path = "./user-codes"
    with open(file_path, "w") as file:
        file.write(code)    
    
    cmd = []
    
    if language=="py":
        cmd = ["python3",file_path]
        result = subprocess.run(cmd,
                                input=code_ip,
                                capture_output=True,
                                text=True,
                                timeout=5)
    
    elif language=="java":
        cmd = ["java",file_path]
        result = subprocess.run(cmd,
                                input=code_ip,
                                capture_output=True,
                                text=True,
                                timeout=5)
        
    elif language=="cpp":
        cmd = f"g++ {file_path} -o {dir_path}/a.out && {dir_path}/a.out"
        result = subprocess.run(cmd,
                                input=code_ip,
                                capture_output=True,
                                text=True,
                                shell=True,
                                timeout=5)
    output = result.stdout if result.returncode==0 else result.stderr
    
    return json.dumps({"output":output})


# CHATBOT
@app.route('/zetaBot',methods=["POST"])
def zetaBot():
    data = request.json
    prompt = data["prompt"]
    code = data["code"]
    print(prompt)
    client = Groq(api_key=API_KEY)
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant and your name is \"Zeta Bot\". who will help newbie Programmers to understand and solve errors in their programs. Always make sure to give links to any relevant web-articles only when relevant for the user to learn, Give High preference to Youtube video links also make sure to generate your responses in proper markdown so that I can render it to my frontend Make sure not to give too many newline characters in your response. also don't give the corrected code right away. try to teach the user and provide a code output only when asked explicitly"
        },
        {
            "role": "user",
            "content": code +"\n"+ prompt,
        }
    ],
    model="llama3-70b-8192",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
    )
    return json.dumps({"response":chat_completion.choices[0].message.content})
    



@app.route('/')
def root():
    return "The ROOT page !"

app.run(host="zeta-server.onrender.com/",port=10000)
