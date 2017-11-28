d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v 1500k -maxrate 1500k -bufsize 1000k -vf "scale=1280:720,fps=24" %1_720.mp4
d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v  800k -maxrate  800k -bufsize  500k -vf "scale=960:540,fps=24" %1_540.mp4
d:\ffmpeg\bin\ffmpeg -y -i %1 -c:a aac -ac 2 -ab 128k -c:v libx264 -x264opts keyint=24:min-keyint=24:no-scenecut -b:v  400k -maxrate  400k -bufsize  400k -vf "scale=640:360,fps=24" %1_360.mp4
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile baseline -segment-name %1_360V_ -out baseline/%1_360V.mpd %1_360.mp4#video
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile baseline -segment-name %1_540V_ -out baseline/%1_540V.mpd %1_540.mp4#video
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile baseline -segment-name %1_720V_ -out baseline/%1_720V.mpd %1_720.mp4#video
"c:\Program Files\GPAC\mp4box.exe" -dash 2000 -frag 2000 -rap -profile baseline -segment-name %1_720A_ -out baseline/%1_720A.mpd %1_720.mp4#audio