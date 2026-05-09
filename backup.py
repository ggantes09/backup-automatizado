import config
import shutil
import os
import datetime

def fazer_backup():
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_backup = f"backup_{data_atual}"
    print(nome_backup)
    os.makedirs(config.pasta_destino, exist_ok=True)
    caminho_backup = os.path.join(config.pasta_destino, nome_backup)
    shutil.make_archive(caminho_backup, "zip", config.pasta_origem)
    caminho_do_log = os.path.join(config.pasta_destino, "backup.log")
    with open(caminho_do_log, "a") as log:
            log.write(f"[{data_atual}] Backup realizado: {nome_backup}.zip\n")
    arquivos = os.listdir(config.pasta_destino)
    backups = [f for f in arquivos if f.endswith(".zip")]
    backups.sort()
    if len(backups) > config.manter_backups:
        mais_antigo = os.path.join(config.pasta_destino, backups[0])
        os.remove(mais_antigo)

fazer_backup()