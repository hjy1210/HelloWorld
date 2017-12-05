# Mpeg-Dash

[Mpeg-Dash](https://bitmovin.com/dynamic-adaptive-streaming-http-mpeg-dash/) 
介紹了 Dynamic Adaptive Streaming over HTTP，讓接收端設備可以動態的根據連線的速度選取恰當的影音檔片段，網路頻寬不足時選取較低解析度的影音檔，網路頻寬充裕時選取較高解析度的影音檔。

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
複製並貼到 output_AV.mpd 裡面的節點`<Representation id="1"....></Representation>`之後，並將新加入的 id="1" 改成 id="2"。
3. 將 input.mp4_360V.mpd 裡面的節點`<Representation id="1"....></Representation>` 
複製並貼到 output_AV.mpd 裡面的節點`<Representation id="2"....></Representation>`之後，並將 id="1" 改成 id="3"。
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

## 影音檔串接

我們可以用 MovieMaker 或 VideoStudioX 等軟體將數個影音檔串接編輯。也可以用FFmpeg來串接。

下面是一個用FFmpeg來串接的例子。AdeleHD.mp4是一個1280x720,fps=25的影音檔，Mia.mp4是一個360x640,fps=24的影音檔。我們要將它們連接起來。

第一步要做的是修改成1280x720的影片。指令
```
d:\ffmpeg\bin\ffmpeg -y -i mia.mp4 -c:a aac -ac 2 -ab 128k -c:v libx264 -vf "scale=trunc(oh*a/2)*2:720,pad=1280:720:(1280-trunc(oh*a/2)*2)/2:0:black" -sar 1:1  mia_scaled.mp4
```
將360x640的影片先放大成404x720的影片，其中oh=720,a=9/16,trunc(oh*a/2)*2=404。再將左右兩側平均補上黑色，最後設定sample aspect ratio(sar=1:1)。產生1280x720,sar=1:1的影片mia_scaled.mp4。

指令
```
d:\ffmpeg\bin\ffmpeg -y -i adeleHD.mp4 -i mia_scaled.mp4 -i adeleHD.mp4 -filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][2:a:0]concat=n=3:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" concatedthree.mp4
```
將 adeleHD.mp4, mia_scaled.mp4, adeleHD.mp4 三個檔案串接起來，其中的[0:v:0]代表檔案0(adeleHD.mp4)的Video stream 0,[0:a:0]代表檔案0(adeleHD.mp4)的Audeo stream 0,其中的[1:v:0]代表檔案1(mia_scaled.mp4)的Video stream 0,[1:a:0]代表檔案1(mia_scaled.mp4)的Audeo stream 0,[2:v:0]代表檔案2(adeleHD.mp4)的Video stream 0,[2:a:0]代表檔案2(adeleHD.mp4)的Audeo stream 0，得到檔案concatedthree.mp4。各個參數的意義請看[說明文件](https://trac.ffmpeg.org/wiki/Concatenate)


## 參考資料
* [Mpeg-Dash](https://bitmovin.com/dynamic-adaptive-streaming-http-mpeg-dash/)
* [HOW TO ENCODE MULTI-BITRATE VIDEOS IN MPEG-DASH FOR MSE BASED MEDIA PLAYERS 1/2](https://blog.streamroot.io/encode-multi-bitrate-videos-mpeg-dash-mse-based-media-players/)
* [HOW TO ENCODE MULTI-BITRATE VIDEOS IN MPEG-DASH FOR MSE BASED MEDIA PLAYERS 2/2](https://blog.streamroot.io/encode-multi-bitrate-videos-mpeg-dash-mse-based-media-players-22/)
* [FFmpeg documentation](https://ffmpeg.org/documentation.html)
* [MPEG-DASH Content Generation with MP4Box and x264](https://bitmovin.com/mp4box-dash-content-generation-x264/)
* [DASH Tutorial – #1 Getting started with DASH](http://halcyon.ch/dash-tutorial-1-getting-started-with-dash/)
* [DASH Tutorial – #2 Display DASH Stream](http://halcyon.ch/dash-tutorial-2-display-dash-stream/)

注意：ffmpeg 在轉換影音檔時，也用了x264。