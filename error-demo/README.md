## 練習error

練習例外狀況將 Error 物件傳遞給錯誤處理函數。下面例子，正常的話(req.params.message==="1")將檔案傳出，不正常的話交給後台的錯誤處理函數。
```
  if (req.params.message==="1"){
    res.sendFile(path.join(__dirname, '../public/images/Mia20161013.jpg'));
  } else {
    var error=new Error("not found!!!")
    console.log(error.stack)
    error.status=404
    next(error)
  }

```

## debug

1. 設定中斷點
2. Debug > start debug > node.js 開始除錯