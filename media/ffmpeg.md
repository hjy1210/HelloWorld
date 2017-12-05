## What is ffmpeg
一個跨平台的軟體，可以用來進行影音檔的錄影、轉換與串流。

它的說明文件在[這裡](https://ffmpeg.org/documentation.html)

## How to play a media

下面指令播放example2.mp3檔案，起自9秒，播放5秒，接著自動結束 process。
```
ffplay -ss 0:9 -t 5 -nodisp -autoexit example2.mp3
```

## How to get length of a media
下面指令可以得知 example2.mp3 檔案的長度為17.04秒。
```
ffprobe example2.mp3
```

## How to get silence intervals of a media
參考[這裡](https://ffmpeg.org/ffmpeg-filters.html#silencedetect)，下面指令可以得到長度超過0.5秒，低於50分貝的靜音資料。
```
ffmpeg -i example2.mp3 -af silencedetect=n=-50dB:d=0.5 -f null -
```

## How to extract frames from a media
下面指令從 Mia201705061105.mp4 擷取起自0分55秒長度0分10秒的畫面, 存到 output_xxxxx.jpg.
```
fmpeg.exe -ss 0:55 -t 0:10 -i Mia201705061105.mp4 -an -f image2 "output_%05d.jpg"
```
 
## How to get codecs supported by ffmpeg
指令
```
ffmpeg -codes
```
可以用來得知 ffmpeg 支援影音檔那些編碼方式。


