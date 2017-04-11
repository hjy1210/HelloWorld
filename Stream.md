# Dash.js
A reference client implementation for the playback of MPEG DASH via JavaScript.

## Reference
* [DASH Tutorial – #1 Getting started with DASH](http://halcyon.ch/dash-tutorial-1-getting-started-with-dash/)
* [DASH Tutorial – #2 Display DASH Stream](http://halcyon.ch/dash-tutorial-2-display-dash-stream/)

## Tools
* In [GPAC](https://gpac.wp.imt.fr/) website, [gpac-0.6.2-DEV-rev1510-gabef25d-master-x64.exe](https://gpac.wp.imt.fr/downloads/gpac-nightly-builds/) is an installation file. 
After installing, command line tool MP4Box.exe is located in "c:\program files\GPAC".
* In [videolan](http://www.videolan.org) website,  [x264-r2762-90a61ec.exe](http://www.videolan.org/developers/x264.html) is a command line tool. After download rename it as x264.exe.

## Simple tour
Simple tour start from a simple MP4 file squirrel_video.mp4, through transform, segments, manifest, implement video element,
stream it by SimpleHttpServer.

Following are the steps:

1. download [squirrel_video.mp4](http://halcyon.ch/halcyon_dash/tutorial_part_1/squirrel_video.mp4)

2. use command `x264 --output intermediate_2400k.264 --fps 24 --preset slow --bitrate 2400 --vbv-maxrate 4800 --vbv-bufsize 9600 --min-keyint 48 --keyint 48 --scenecut 0 --no-scenecut --pass 1 --video-filter "resize:width=1280,height=720" squirrel_video.mp4` to produce intermediate_2400k.264.

3. use command `MP4Box -add intermediate_2400k.264 -fps 24 output_squirrel.mp4` to produce output_squirrel.mp4.

4. use command `MP4Box -dash 4000 -frag 4000 -rap -segment-name segment_ output_squirrel.mp4` to produce output_squirrel_dash.mpd and segment_*.m4s

5. use command `python -m SimpleHTTPServer 8080` to start server

6. Insert following snippet into dash.js/samples/getting-started-basic-embed/auto-load-single-video.html.
```
<video class="dashjs-player" autoplay preload="none" controls="true">
 <source src="http://localhost:8080/output_squirrel_dash.mpd" type="application/dash+xml"/>
</video>
 ```

 ## TODO
 * Inspect samples in Dash.js.
 * Study parameters of x264 and MP4Box.
 * Study [Documentation](http://cdn.dashjs.org/latest/jsdoc/module-MediaPlayer.html) of dash.js

