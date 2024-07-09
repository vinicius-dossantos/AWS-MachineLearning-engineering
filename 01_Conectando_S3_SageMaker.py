## importando bibliotecas
import pandas as pd
import numpy as np
import boto3
from io import BytesIO

# Configurar suas credenciais da AWS
aws_access_key_id = 'xxxxxxxxxxxxxxx'
aws_secret_access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
region_name = 'us-east-1'

# Variaveis para buscar o arquivo
bucket_name = 'nome-do-seu-bucket-onde-esta-o-arquivo'
file_name = 'arquivo_que_precisa_importar.csv'

# Criar uma conexão com o S3
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=region_name)

# Ler o arquivo CSV do S3 usando o pandas
object = s3.get_object(Bucket=bucket_name, Key=file_name)
csv_bytes = object['Body'].read()
df_salaries = pd.read_csv(BytesIO(csv_bytes))

# Imprimir o conteúdo do seu dataframe
df_salaries.head()

#teste