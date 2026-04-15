from ultralytics import YOLO
import cv2
import os
import time as time_module
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("url")                                    # URL do Supabase
KEY = os.getenv("key")                                    # Chave do Supabase
supabase: Client = create_client(URL, KEY)

def salvar_no_supabase(conteudo):
    if conteudo is None:
        print("Erro: A variável 'saida' está vazia (None).")
        return

    try:
        dados = {"texto_saida": str(conteudo)}
        
        response = supabase.table("registros").insert(dados).execute()
        print("Saída salva com sucesso no Supabase!")
        return response
        
    except Exception as e:
        print(f"Erro ao enviar para o banco: {e}")

model = YOLO("yolov8n.pt")
 
cap = cv2.VideoCapture(1)

ultimo_envio = 0           # Controle do tempo de envio ao banco
intervalo_envio = 3        # Intervalo em segundos para salvar no Supabase (ajuste como quiser)
 
while True:
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    success, frame = cap.read()
 
    resultados = model(frame, classes=[0], verbose=False)[0]

    for box in resultados.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (128, 0, 128), 2)
        cv2.putText(frame, f"Pessoa, {time}", (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (128, 0, 128), 2)
    
    total = len(resultados.boxes)
    cv2.putText(frame, f"Pessoas: {total}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 0, 128), 2)

    if total > 0:      
        tempo_atual = time_module.time()
        
        # Sé salva no Supabase se já se passaram 'intervalo_envio' segundos (ex: 3 segundos)
        if (tempo_atual - ultimo_envio) > intervalo_envio:
            print(time, f"Salvando no banco... Pessoas detectadas: {total}")
            salvar_no_supabase((time,f"Pessoas detectadas: {total}"))
            ultimo_envio = tempo_atual
        else:
            # Imprime no terminal normalmente mas NÃO manda pro banco para não travar o vídeo
            print(time, f"Pessoas detectadas: {total}")
            
    cv2.imshow("Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
