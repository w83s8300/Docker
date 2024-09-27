# 使用官方的 Python 3.10 基礎映像
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 將 requirements.txt 複製到容器中
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 將整個應用程式目錄複製到容器
COPY ./app ./app

# 開放 8000 port（FastAPI 預設埠）
EXPOSE 8000

# 啟動 FastAPI 應用程式，使用 uvicorn 來執行
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
