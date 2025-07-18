# MBA ITI UFSCar - Atividade
Material de apoio para o módulo de Cloud Computing do MBA de ML

## Atividade

- Desenvolver na sua conta AWS um pipeline de Extração, Transformação e Carregamento de Dados
- Depois de configurar os serviços, a ingestão do arquivo deverá ser feita manualmente para o serviço de Storage, a partir desse ponto todos os eventos deverão ser iniciados automaticamente
- No banco de dados final deverá conter os dados originais do arquivo
- Arquivo original encontra-se no repositório do Github: titanic_data.json
- Arquivo com script sql para gerar tabela para salvar os dados: titanic_database.sql

## Passo-a-passo
- Criar dois buckets no S3
  - mba-raw
  - mba-structured
- Criar fila SQS
  - sqs-titanic
- Criar política de acesso no IAM com permissões para Cloud Watch, S3 e SQS
  - mba-ufscar 
- Criar RDS
- Configurar DBeaver ou similar
- Desenvolver lambda com trigger de S3 para leitura do arquivo original e criação do arquivo csv
  - titanic-pipeline-raw-to-structured
- Desenvolver lambda com trigger de S3 para leitura do arquivo csv e envio de mensagem para o SQS
  - titanic-pipeline-structured-to-sqs
- Desenvolver lambda com trigger de SQS para salvar dados no RDS
  - titanic-pipeline-sqs-to-rds

## Links para Lambda Layers (Python 3.9)
- PyMySQL : https://drive.google.com/file/d/1bBJANtI_Tj0_CGcwGeZWT0giipHKSEXB/view?usp=sharing

## Links de Referência
- DBeaver (DB Client): https://dbeaver.io/download/ 
- Kaggle: https://www.kaggle.com/ 
- Dataset Titanic: https://www.kaggle.com/datasets/brendan45774/test-file
- Lambda Layer: https://towardsdatascience.com/how-to-install-python-packages-for-aws-lambda-layer-74e193c76a91

