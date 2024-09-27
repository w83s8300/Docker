# 使用官方的 Node.js 鏡像作為基礎鏡像來進行 Vue.js 應用的構建
FROM node:16-alpine AS build

# 設定應用的工作目錄
WORKDIR /app

# 複製 package.json 和 package-lock.json 到工作目錄
COPY package*.json ./

# 安裝依賴
RUN npm install

# 複製專案所有檔案
COPY . .

# 構建 Vue.js 應用
RUN npm run build

# 使用官方的 Nginx 鏡像來運行靜態文件
FROM nginx:stable-alpine

# 複製自訂的 Nginx 配置檔到容器中
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 複製構建後的檔案到 Nginx 的靜態文件目錄
COPY --from=build /app/dist /usr/share/nginx/html

# 暴露 Nginx 預設的 80 端口
EXPOSE 80

# 啟動 Nginx
CMD ["nginx", "-g", "daemon off;"]
