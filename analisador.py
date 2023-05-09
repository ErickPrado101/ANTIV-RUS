import os
import subprocess
import requests
import json
import subprocess
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/check-virus', methods=['POST'])
def check_virus():
    file = request.files['file']
    file_path = os.path.join(app.root_path, 'uploads', file.filename)
    file.save(file_path)
    result = subprocess.run(['clamscan', '--no-summary', file_path], capture_output=True, text=True)
    if 'FOUND' in result.stdout:
        os.remove(file_path)
        message = 'O arquivo contém um vírus!'
    else:
        message = 'O arquivo está limpo.'
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
    


file_path = 'caminho/do/arquivo'
# Configure o URL e a chave de API para a chamada da API do Microsoft Defender Antivirus;ConfigurAR as informações do arquivo;  # ALTERAR o cabeçalho ;EnviAR a solicitação;
while True :
 print("Gostaria de uma verificação rápida ou completa?")
 verif = int(input("Digite "1" para verificação rápida ou "2" para verificação completa: ")) 
 if verif == 1
    def check_file_for_virus(file_path):    
    url = "https://api.livemeeting.ms/api/file/scan"
    api_key0 = "<SUA_CHAVE_DE_API_AQUI>"   
    files = {'file': open(file_path, 'rb')}   
    headers = {'Ocp-Apim-Subscription-Key': api_key0}
    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.content)    
    if result["detected"] == True:
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")

        while True: 
         print("Deseja apagar esse arquivo?")
         apg = int(input("Digite "1" para deletar o ou "2" manter o arquivo "))
         if apg ==1
            caminho_do_arquivo = "/caminho/para/o/arquivo/arquivo.txt"
            if os.path.exists(caminho_do_arquivo):
            os.remove(caminho_do_arquivo)
            print("Arquivo apagado com sucesso!")
            break
         elif apg ==2
          print("Arquivo mantido")
          break
         
         else:
          print("O arquivo não existe ou não é possível acessá-lo.")
          break
                  


                  
                  

    else:
     print("O arquivo está limpo.")
     print("Abrindo arquivo")
     check_file_for_virus("C:caminho/para/o/arquivo/suspeito.exe")
     subprocess.run(caminho_arquivo, shell=True)


 elif verif ==2
 def check_file_for_virus(file_path):    
    url = "https://api.livemeeting.ms/api/file/scan"
    api_key1 = "<SUA_CHAVE_DE_API_AQUI>"   
    files = {'file': open(file_path, 'rb')}   
    headers = {'Ocp-Apim-Subscription-Key': api_key1}
    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.content)    
    if result["detected"] == True:
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")

        while True: 
         print("Deseja apagar esse arquivo?")
         apg = int(input("Digite "1" para deletar o ou "2" manter o arquivo "))
         if apg ==1
            caminho_do_arquivo = "/caminho/para/o/arquivo/arquivo.txt"
            if os.path.exists(caminho_do_arquivo):
            os.remove(caminho_do_arquivo)
            print("Arquivo apagado com sucesso!")
            break
         elif apg ==2
          print("Arquivo mantido")
          break
         
         else:
          print("O arquivo não existe ou não é possível acessá-lo.")
          break
                  


                  
                  

    else:
     def check_file_for_virus(file_path):    
    url = "https://api.livemeeting.ms/api/file/scan"
    api_key2 = "<SUA_CHAVE_DE_API_AQUI>"   
    files = {'file': open(file_path, 'rb')}   
    headers = {'Ocp-Apim-Subscription-Key': api_key2}
    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.content)    
    if result["detected"] == True:
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")

        while True: 
         print("Deseja apagar esse arquivo?")
         apg = int(input("Digite "1" para deletar o ou "2" manter o arquivo "))
         if apg ==1
            caminho_do_arquivo = "/caminho/para/o/arquivo/arquivo.txt"
            if os.path.exists(caminho_do_arquivo):
            os.remove(caminho_do_arquivo)
            print("Arquivo apagado com sucesso!")
            break
         elif apg ==2
          print("Arquivo mantido")
          break
         
         else:
          print("O arquivo não existe ou não é possível acessá-lo.")
          break
                  


                  
                  

    else:
     def check_file_for_virus(file_path):    
    url = "https://api.livemeeting.ms/api/file/scan"
    api_key3 = "<SUA_CHAVE_DE_API_AQUI>"   
    files = {'file': open(file_path, 'rb')}   
    headers = {'Ocp-Apim-Subscription-Key': api_key3}
    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.content)    
    if result["detected"] == True:
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")

        while True: 
         print("Deseja apagar esse arquivo?")
         apg = int(input("Digite "1" para deletar o ou "2" manter o arquivo "))
         if apg ==1
            caminho_do_arquivo = "/caminho/para/o/arquivo/arquivo.txt"
            if os.path.exists(caminho_do_arquivo):
            os.remove(caminho_do_arquivo)
            print("Arquivo apagado com sucesso!")
            break
         elif apg ==2
          print("Arquivo mantido")
          break
         
         else:
          print("O arquivo não existe ou não é possível acessá-lo.")
          break
                  


                  
                  

    else:
     def check_file_for_virus(file_path):    
    url = "https://api.livemeeting.ms/api/file/scan"
    api_key4 = "<SUA_CHAVE_DE_API_AQUI>"   
    files = {'file': open(file_path, 'rb')}   
    headers = {'Ocp-Apim-Subscription-Key': api_key4}
    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.content)    
    if result["detected"] == True:
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("CUIDADO!!!")
        print("O arquivo foi detectado como um vírus!")

        while True: 
         print("Deseja apagar esse arquivo?")
         apg = int(input("Digite "1" para deletar o ou "2" manter o arquivo "))
         if apg ==1
            caminho_do_arquivo = "/caminho/para/o/arquivo/arquivo.txt"
            if os.path.exists(caminho_do_arquivo):
            os.remove(caminho_do_arquivo)
            print("Arquivo apagado com sucesso!")
            break
         elif apg ==2
          print("Arquivo mantido")
          break
         
         else:
          print("O arquivo não existe ou não é possível acessá-lo.")
          break
                  


                  
                  

    else:
     print("O arquivo está limpo.")
     print("Abrindo arquivo")
     check_file_for_virus("C:caminho/para/o/arquivo/suspeito.exe")
     subprocess.run(caminho_arquivo, shell=True)
        
  
