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

## mathjax

**加入 \fbox,\ceec 用來實作選填題**

[MathJax/config/](https://github.com/mathjax/MathJax/tree/master/config) 有mathiax內建的configuration清單。

[config-files](http://docs.mathjax.org/en/latest/config-files.html) 有內建configuration的說明

檢查[TeX-AMS-MML_HTMLorMML.js](https://github.com/mathjax/MathJax/blob/master/config/TeX-AMS-MML_HTMLorMML.js)的內容，
可以看到他有包括Amsmath.js的擴充。