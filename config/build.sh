#!/bin/bash

# 確保腳本在遇到錯誤時終止
set -e

# 可選：激活虛擬環境
# source /path/to/your/virtualenv/bin/activate

# 安裝依賴
pip install -r requirements.txt

# 運行數據庫遷移
python manage.py migrate --noinput

# 收集靜態文件
python manage.py collectstatic --noinput

# 可選：運行測試
# python manage.py test

# 可選：製作 Docker 容器
# docker build -t yourapplication .

# 其他必要的構建步驟...