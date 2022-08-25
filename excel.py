import streamlit as st
import os
import pandas as pd
from io import BytesIO
from google.cloud import storage

#my_gcp_credentials.jsonはサービズアカウントから発行
storage_client = storage.Client.from_service_account_json('service-495585574816@gs-project-accounts.iam.gserviceaccount.com')

#バケットを作成する
#created_bucket_name = 'smart12'
#bucket = storage_client.create_bucket(created_bucket_name)

#ローカルファイルをバケットへ転送する
#bucket = 'smart12'
#file_name = 'data.csv' #送るものの名前
#destination_blob_name = 'data/data_csv' #送り先での名前

#bucket = storage_client.get_bucket(bucket_name)
#blob = bucket.blob(destination_blob_name)
#blob.upload_from_filename(file_name)

#バケット内のファイルを削除する。
#bucket_name = 'smart12'
#file_name = 'sended_txt.txt'

#bucket = storage_client.get_bucket(buket_name)
#blob = buket.blob(file_name)
#blob.delete()

#バケット内にあるファイルを読み込む
#bucket_name = 'smart12'
#file_name = 'sended_txt.txt' #読み込むたいバケット内のファイル名

#bucket = storage_client.get_bucket(bucket_name)
#blob = storage.Blob(file_name,bucket)

#content = bolb.download_as_string()
#with open('sended_txt.txt',mode='wb') as f:
#    f.write(content)

#バケット上のCSVファイルをpandasで読み込む
#bucket_name = 'smart12'
#file_name = 'sended_txt.txt' #読み込むたいバケット内のファイル名

#bucket = storage_client.get_bucket(bucket_name)
#blob = storage.Blob(file_name,bucket)
#content = blob.download_as_string()
#df_csv = pd.read_csv(BytesIO(content))

#バケットに書き込む
def get(self):
  bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

  self.response.headers['Content-Type'] = 'text/plain'
  self.response.write('Demo GCS Application running from Version: '
                      + os.environ['CURRENT_VERSION_ID'] + '\n')
  self.response.write('Using bucket name: ' + bucket_name + '\n\n')




#body
if 'page' not in st.session_state:
    st.session_state.page=0

select_radio = ['新規','追記']
radio = st.radio('which',select_radio)

#page=0
if radio == '新規':
    ban = 1
    st.write(f'登録番号:{ban}')
    tokui = st.text_input('得意先')
    shiken = st.text_input('試験名')
    touroku = st.button('登録')
    file_path = 'C:Users¥ono¥Desktop¥123.txt'
    
    if touroku:
        with open(file_path,'w') as f:
            f.write(tokui)
            f.close()

if radio == '追記':
    st.write('前回の続き')