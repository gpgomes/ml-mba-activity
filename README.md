# ml-mba-activity
Material de apoio para o módulo de Cloud Computing do MBA de ML

## Atividade

- Desenvolver na sua conta AWS um pipeline de Extração, Transformação e Carregamento de Dados
- Depois de configurar os serviços, a ingestão do arquivo deverá ser feita manualmente para o serviço de Storage, a partir desse ponto todos os eventos deverão ser iniciados automaticamente
- No banco de dados final deverão conter os dados originais do arquivo e as agregações realizadas

## Passo-a-passo
- Criar instância no RDS
  - Instalar DBeaver ou similar
  - Configurar segurança da instância para receber conexões públicas.
- Criar dois buckets no S3
- Desenvolver lambda com trigger de S3 para leitura do arquivo csv e envio de mensagem para o SQS
- Desenvolver lambda com trigger de SQS para salvar dados no RDS


## Links
- DBeaver (DB Client): https://dbeaver.io/download/ 
- Kaggle: https://www.kaggle.com/ 
- Dataset Titanic: https://www.kaggle.com/datasets/brendan45774/test-file