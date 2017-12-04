# Mpeg-Dash

[Mpeg-Dash](https://bitmovin.com/dynamic-adaptive-streaming-http-mpeg-dash/) 
介紹了 Dynamic Adaptive Streaming over HTTP，讓接收端設備可以動態的根據連線的速度選取恰當的影音檔片段，網路平寬不足時選取較低解析度的影音檔，網路平寬充裕時選取較高解析度的影音檔。

## Dashify content
將完整的影音檔切割成長度相同的片段，每一片段製作出解析度不同而時間長度相同的檔案，並用mpd檔當作影音目錄。

用 ffmpeg 準備檔案，mp4box 進行切割。

下面的批次檔，可以製作出包括解析度1280x767,969x540,640x360的影片片段以及目錄。
```
d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1000k -vf "scale=1280:720,fps=24" %1_720.mp4
d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v  800k -maxrate  800k -bufsize  500k -vf "scale=960:540,fps=24" %1_540.mp4
d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v  400k -maxrate  400k -bufsize  400k -vf "scale=640:360,fps=24" %1_360.mp4
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile onDemand -segment-name %1_360V_ -out onDemand/%1_360V.mpd %1_360.mp4#video
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile onDemand -segment-name %1_540V_ -out onDemand/%1_540V.mpd %1_540.mp4#video
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile onDemand -segment-name %1_720V_ -out onDemand/%1_720V.mpd %1_720.mp4#video
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile onDemand -segment-name %1_720A_ -out onDemand/%1_720A.mpd %1_720.mp4#audio
```
使用方法如下：
```
dashify input.mp4
```
會在 onDemand 子目錄產生 input.mp4_720V.mpd,input.mp4_540V.mpd,input.mp4_360V.mpd,input.mp4_720A.mpd以及影音檔案。前三個mpd檔分別是1280x720,960x540,640x360的影片片段目錄，第四個是聲音片段的目錄。

手動將這四個mpd合併成完整的目錄output_AV.mpd，方法如下：
1. 將 input.mp4_720V.mpd 複製到 output_AV.mpd。
2. 將 input.mp4_540V.mpd 裡面的節點`<Representation id="1"....></Representation>` 
複製並貼到 output_AV.mpd 裡面的節點`<Representation id="1"....></Representation>`
之後，並將新加入的 id="1" 改成 id="2"。
3. 將 input.mp4_360V.mpd 裡面的節點`<Representation id="1"....></Representation>` 
複製並貼到 output_AV.mpd 裡面的節點`<Representation id="2"....></Representation>`
之後，並將 id="1" 改成 id="3"。
4. 將 input.mp4_720A.mpd 裡面的節點 `<AdaptationSet...>...</AdaptationSet>`
複製並貼到 output_AV.mpd 裡面的節點 `<AdaptationSet...>...</AdaptationSet>` 的後面。

完成後 output_AV.mpd 裡面有兩個 `<AdaptationSet>`，第一個`<AdaptationSet>`
裡面有3個`<Representation>`。第1個`<Representation>` 的 id="1"，其內容是從input.mp4_720V.mpd 抄過來的；第2個`<Representation>` 的 id="2"，其內容是從input.mp4_540V.mpd 抄過來的；第3個`<Representation>` 的 id="3"，其內容是從input.mp4_360V.mpd 抄過來的。第二個`<AdaptationSet>` 的內容是從
input.mp4_720A.mpd 抄過來的。

## Play content by dash player
示範如下面的 html 檔案：
```
<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8' />
  <script src="http://cdn.dashjs.org/latest/dash.all.min.js"></script>
  <style>
    video {
      width: 1280px;
      height: 720px;
    }
  </style>
</head>
<body>
  <div>
    <video data-dashjs-player src="http://localhost:3000/onDemand/output_AV.mpd" controls></video>
  </div>
</body>
</html>
```
## youtube-dl.exe
[youtube-dl.exe](https://youtube-dl.org/) 用來下載 youtube 的影片非常方便。

例如：
```
youtube-dl.exe https://www.youtube.com/watch?v=fk4BbF7B29w
```
會下載得 "Adele - Send My Love (To Your New Lover)-fk4BbF7B29w.mkv"

## ffmpeg
批次檔 standardize.bat
```
d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1000k -vf "scale=1280:720,fps=24" %1_720.mp4
```
可用來將影音檔標準化以利銜接。用法為
```
standardize input.mkv
```
會產生 input.mkv_720.mp4

```
ffmpeg -f concat
```
可以用來合併檔案。請參考[Concatenating media files](https://trac.ffmpeg.org/wiki/Concatenate)。

例如：mylist.txt的內容如下：
```
file adele1.webm_720.mp4
file Adele2.mkv_720.mp4
```
則指令
```
d:\ffmpeg\bin\ffmpeg -f concat -safe 0 -i mylist.txt -c copy two.mp4
```
會將兩個檔案 adele1.webm_720.mp4 與 Adele2.mkv_720.mp4 銜接成 two.mp4。

注意：要用上述方法銜接檔案，兩個檔案的video size/Aspect Ratio必須相同。
若兩個檔案的video size 不同，可用MovieMaker來串接。
```
ffmpeg -codes
```
可以用來得知 ffmpeg 支援影音檔那些編碼方式。

## 參考資料
* [Mpeg-Dash](https://bitmovin.com/dynamic-adaptive-streaming-http-mpeg-dash/)
* [HOW TO ENCODE MULTI-BITRATE VIDEOS IN MPEG-DASH FOR MSE BASED MEDIA PLAYERS 1/2](https://blog.streamroot.io/encode-multi-bitrate-videos-mpeg-dash-mse-based-media-players/)
* [HOW TO ENCODE MULTI-BITRATE VIDEOS IN MPEG-DASH FOR MSE BASED MEDIA PLAYERS 2/2](https://blog.streamroot.io/encode-multi-bitrate-videos-mpeg-dash-mse-based-media-players-22/)
* [FFmpeg documentation](https://ffmpeg.org/documentation.html)
* [MPEG-DASH Content Generation with MP4Box and x264](https://bitmovin.com/mp4box-dash-content-generation-x264/)
* [DASH Tutorial – #1 Getting started with DASH](http://halcyon.ch/dash-tutorial-1-getting-started-with-dash/)
* [DASH Tutorial – #2 Display DASH Stream](http://halcyon.ch/dash-tutorial-2-display-dash-stream/)

注意：ffmpeg 在轉換影音檔時，也用了x264。