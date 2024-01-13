# 國軍休假回報機器人
這個聊天機器人用於國軍休假時，幫助班頭快速整理班兵休假狀態，方便快速回報

## 設置教學
請參考: [Line Bot 教學](https://github.com/yaoandy107/line-bot-tutorial?tab=readme-ov-file)
分別到 Heroku 跟 Line Bot 註冊，即可創造一個聊天機器人。

## 更新機器人
```
# Login Heroku
heroku login

# Update App
git add .
git commit -m "commit"
git push -f heroku master
```

## 使用方式
1. 首先利用 **設定** 指令來註冊班上的成員
   例如在聊天室輸入:
   >設定  
   >001 AAA  
   >002 BBB  
   
   即可註冊 AAA、BBB 兩位成員  
   註冊成功後，機器人會回傳
   >已更新成員!
3. 
