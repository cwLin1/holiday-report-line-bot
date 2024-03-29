# 國軍休假回報機器人
這個聊天機器人用於國軍休假時，幫助班頭快速整理班兵休假狀態，方便快速回報

<img src="https://github.com/cwLin1/holiday-report-line-bot/assets/61427980/dc8c0b65-84eb-4d13-ba66-69d983079802" width="320">\
<img src="https://github.com/cwLin1/holiday-report-line-bot/assets/61427980/1ec3eb8b-9866-457d-8ed5-7eedfa87bf82" width="320">  

## 設置教學
請參考: [Line Bot 教學](https://github.com/yaoandy107/line-bot-tutorial?tab=readme-ov-file)
分別到 Heroku 跟 Line Bot 註冊並綁定，即可創造一個聊天機器人

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
1. 註冊成員:  
   首先利用 **設定** 指令來註冊班上的成員  
   例如在聊天室輸入:
   > 設定  
   > 001 AAA  
   > 002 BBB
   
   即可註冊 AAA、BBB 兩位成員  
   註冊成功後，機器人會回傳:
   > 已更新成員!

2. 回報休假狀態:  
   利用以下格式即可完成回報  
   > "學號" "姓名" "狀態"
   
   成功回報時，機器人會回傳:  
   > 已更新回報狀態!
   此時狀態跟對話時間會被記錄

3. 輸出回報結果:  
   在聊天室中輸入 **回報** 即可，若未更新狀態，則會預設為 **未回報**  
   例如在 1234 時回報了
   > 001 AAA 在家睡覺
   
   此時輸入回報，機器人會回傳:  
   > 001 AAA 1234 在家睡覺  
   > 002 BBB 未回報

4. 重置回報結果:  
   在回報完成後，可在聊天室中輸入 **重置** ，將所有人狀態回復到預設狀態  
   成功後機器人會回傳
   > 已重置回報!
   
