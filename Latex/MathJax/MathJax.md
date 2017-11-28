# MathJax
用 MathJax 我們可以讓網頁顯示數學公式。

加上 mhchem.js 的擴充，可以方便顯示化學方程式。
若使用較新的 mhchem3.js，除了化學方程式外還可以方便顯示物理單位。

## 在瀏覽器端顯示數學物理化學公式
下面是一個html的示例。
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script type="text/x-mathjax-config">
    // Reference http://docs.mathjax.org/en/latest/tex.html
    MathJax.Hub.Config({ 
      TeX: { 
        extensions: ["mhchem.js"],
        mhchem:{legacy:false} 
      } 
    })
  </script>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML'></script>

  <title>Document</title>
</head>
<body>
  Solution of \(ax^2+bx+c=0\) is
  \[x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\]
  \[\ce{H2SO4} \pu{1.0e-20}\]
  \[x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\]
  
  \[\ce{C6H5-CHO}\]
  \[\ce{$A$ ->[\ce{+H2O}] $B$}\]
  \[\ce{SO4^2- + Ba^2+ -> BaSO4 v}\]
  \[\ce{A\bond{-}B\bond{=}C\bond{#}D}\]
  \[\pu{1.0e-20}\]

  <p><a href="http://docs.mathjax.org/en/latest/tex.html">Here</a> is a userful reference.</p>
</body>
</html>
```
有兩個要點
* 在網頁的`head`裡面，用兩個tag，`<script type="text/x-mathjax-config">`與`<script src='...'>`來做準備工作。
* 本文區的數學，inline math 請用 Latex 語法打在成對的 `\(` 與 `\)` 裡面，display math 請用 Latex 語法打在成對的 `\[` 與 `\]` 裡面。

注意事項：
`<script type="text/x-mathjax-config">` 裡面的 `mhchem:{legacy:false}` 代表使用 mhchem3.js。若將 false 改成 true 則是使用古典的 mhchem.js。

## 在伺服器端產生數學物理化學公式
在nodejs環境中，用mathjax-node套件，我們可以在伺服器端動態產生數學物理化學公式再送到瀏覽器端。

根據瀏覽器端是否支援 svg, mml 決定產生何種格式的輸出。

下面是一個產生mml輸出的示例：
```
    var mjAPI = require("mathjax-node");
    mjAPI.config({
      MathJax: {
        extensions: 'mhchem.js',
        "TeX": { 
          mhchem: { legacy: false}
        }
      }
    });
    
    var yourMath = '\\ce{H2SO4} \\pu{1.0e-20}';
    
    mjAPI.typeset({
      math: yourMath,
      format: "TeX", // "inline-TeX", "MathML"
      mml:true, //  svg:true,
    }, function (data) {
      console.log(data.mml)
    });
```

