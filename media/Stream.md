# DASH
## What is DASH(MPEG-DASH)
Following paragraphs are digested from [wikipedia:Dynamic Adaptive Streaming over HTTP](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP):

Dynamic Adaptive Streaming over HTTP (DASH), also known as MPEG-DASH, is an adaptive bitrate streaming technique that enables high quality streaming of media content over the Internet delivered from conventional HTTP web servers. Similar to Apple's HTTP Live Streaming (HLS) solution, MPEG-DASH works by breaking the content into a sequence of small HTTP-based file segments, each segment containing a short interval of playback time of content that is potentially many hours in duration, such as a movie or the live broadcast of a sports event. The content is made available at a variety of different bit rates, i.e., alternative segments encoded at different bit rates covering aligned short intervals of play back time are made available. While the content is being played back by an MPEG-DASH client, the client automatically selects from the alternatives the next segment to download and play back based on current network conditions. The client selects the segment with the highest bit rate possible that can be downloaded in time for play back without causing stalls or re-buffering events in the playback. Thus, an MPEG-DASH client can seamlessly adapt to changing network conditions, and provide high quality play back with fewer stalls or re-buffering events.

MPEG-DASH is the first adaptive bit-rate HTTP-based streaming solution that is an international standard. MPEG-DASH should not be confused with a transport protocol — the transport protocol that MPEG-DASH uses is TCP.

MPEG-DASH uses existing HTTP web server infrastructure that is used for delivery of essentially all World Wide Web content. It allows devices like Internet-connected televisions, TV set-top boxes, desktop computers, smartphones, tablets, etc. to consume multimedia content (video, TV, radio, etc.) delivered via the Internet, coping with variable Internet receiving conditions. Standardizing an adaptive streaming solution is meant to provide confidence to the market that the solution can be adopted for universal deployment, compared to similar but more proprietary solutions like Smooth Streaming by Microsoft, or HDS by Adobe.

Unlike, HLS, HDS and Smooth Streaming, DASH is codec-agnostic, which means it can use content encoded with any coding format like H.265, H.264, VP9 etc.

## What is dash.js
dsah.js is a reference client implementation for the playback of MPEG-DASH via JavaScript and compliant browsers. Learn more about DASH IF Reference Client on its [wiki](https://github.com/Dash-Industry-Forum/dash.js/wiki).

### Installation of dash.js
1. Install node.js if not installed.
2. Install globally grunt by `npm install -g grunt-cli`
3. Clone dsah.js by `git clone https://github.com/Dash-Industry-Forum/dash.js.git`
4. In root directory of dash.js, `npm install`

After installation, samples directory contains many samples.

If you do not want install, you can play with [DASH Reference Client 2.5.0](http://mediapm.edgesuite.net/dash/public/nightly/samples/dash-if-reference-player/index.html) online.

### Simple MPEG-DASH player
```
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8' />
    <script src="http://cdn.dashjs.org/latest/dash.all.min.js"></script>
    <style>
        video {
            width: 640px;
            height: 360px;
        }
    </style>
</head>
<body>
    <div>
        <video data-dashjs-player autoplay src="http://dash.edgesuite.net/envivio/EnvivioDash3/manifest.mpd" controls></video>
    </div>
    <div>
        <video data-dashjs-player src="http://dash.edgesuite.net/envivio/EnvivioDash3/manifest.mpd" controls></video>
    </div>
</body>
</html>
```

## How to produce materials for dash.js

成功的步驟請看[Mpeg-Dash.md](Mpeg-Dash.md)，
下面則是嘗試的過程。

Dash player need mpd(Media Presentation Description)file and corresponding segments.

How to provide these? There are two alternatives.
### use [bitmovin](https://bitmovin.com/) online service to provide for us.
Note: If the mp4 file is downloaded from youtube video(e.g. https://youtu.be/fk4BbF7B29w) by [youtubeinmp4](http://youtubeinmp4.com/) without high definition, it do not work.

### use MP4Box.exe and x264.exe to produce by oneself.

Following are useful resources for producing by oneself:

* [MPEG-DASH Content Generation with MP4Box and x264](https://bitmovin.com/mp4box-dash-content-generation-x264/)
* [DASH Tutorial – #1 Getting started with DASH](http://halcyon.ch/dash-tutorial-1-getting-started-with-dash/)
* [DASH Tutorial – #2 Display DASH Stream](http://halcyon.ch/dash-tutorial-2-display-dash-stream/)


#### Tools
* **MP4Box** : In [GPAC](https://gpac.wp.imt.fr/) website, [gpac-0.6.2-DEV-rev1510-gabef25d-master-x64.exe](https://gpac.wp.imt.fr/downloads/gpac-nightly-builds/) is an installation file. 
After installing, command line tool MP4Box.exe is located in "c:\program files\GPAC".
* **x264** : In [videolan](http://www.videolan.org) website,  [x264-r2762-90a61ec.exe](http://www.videolan.org/developers/x264.html) is a command line tool. After download rename it as x264.exe.

#### Simple tour

Following steps demostrate how to:

create video/audio streams of a simple Mp4 file Mia.mp4 and concate those mpd files as a single mpd file.

arrange those files to stream audio/video as a single entry.


1. "c:\Program Files\GPAC\mp4box.exe" -dash 4000 -frag 4000 -rap -profile baseline -segment-name video/Mia_V_ -out Mia_V.mpd Mia.mp4#video
2. "c:\Program Files\GPAC\mp4box.exe" -dash 4000 -frag 4000 -rap -profile baseline -segment-name audio/Mia_A_ -out Mia_A.mpd Mia.mp4#audio
3. combine Mia_V.mpd, Mia_A.mpd as Mia_AV.mpd
    * `copy Mia_V.mpd Mia_AV.mpd`
    * copy the AdaptationSet element in Mia_A.mpd, insert it beneath the original AdaptationSet element in Mia_AV.mpd
4. Put Mia_AV.mpd and subdirectories video and audio in some where in your website.
5. Set the src attributes in above simple MPEG-DASH player.
6. browse to the simple player in your website.

Note: If web server is IIS, we need setup up mime types for mpd, mp4, m4s in IIS manager.

Note: For mp4 files downloaded from youtube video(e.g. https://youtu.be/fk4BbF7B29w) by [youtubeinmp4](http://youtubeinmp4.com/) with/without high definition, the video stream created by above method terminiated strangely at about 2 minutes 30 seconds.

#### use x264 to produce video streams for different bitrates and sizes:
1. use command `x264 --output intermediate_2400k.264 --fps 24 --preset slow --bitrate 2400 --vbv-maxrate 4800 --vbv-bufsize 9600 --min-keyint 96 --keyint 96 --no-scenecut --pass 1 --video-filter "resize:width=1280,height=720" Mia.mp4` to produce intermediate_2400k.264.

2. use command `"c:\Program Files\GPAC\mp4box.exe" -add intermediate_2400k.264 -fps 24 Mia_2400k.mp4` to produce Mia_2400k.mp4.

3. use command `"c:\Program Files\GPAC\mp4box.exe" -dash 4000 -frag 4000 -rap -profile baseline -segment-name video_2400k/Mia_V_ -out Mia_V_2400k.mpd Mia_2400k.mp4#video` to produce Mia_V_2400k.mpd and corresponding segments.

Note: For mp4 files downloaded from youtube video(e.g. https://youtu.be/fk4BbF7B29w) by [youtubeinmp4](http://youtubeinmp4.com/) with/without high definition, the video stream created by above method hove some lag compared with audio stream.


#### What is x264 
* `x264 --help` : list basic options
* `x264 --longhelp` : list more options
* `x264 --fullhelp` : list all options

Study [x264 Options Explained](http://www.digital-digest.com/articles/x264_options_page1.html).

x264 is a free H.264 encoder

What is H.264, quoted from [H.264 Playback Guide](http://www.digital-digest.com/articles/mp4_h264_playback_page1.html) : 

H.264 is a video compression standard that is set to replace MPEG-2. H.264 (also known as MPEG-4 AVC, or MPEG-4 Part 10) can offer the same quality video as MPEG-2 at only a third or half the bit-rate. What this means that by using more advanced video encoding techniques, H.264 clips are only a third or half the size of MPEG-2 clips of the same quality. Even DivX/XviD is no match for H.264 - H.264 can often be 30% smaller than DivX/XviD and still offer the same quality video.

Frames Basics
* Intra(I) frames(least compressible)
* Predictive(P) frames(motion compensation)
* Bidirectional(B) frames(most compressible)

So basically, a compressed video will be a combination of I, P and B frames, some referencing others. The successful combination of these frames and the referencing determines how well the video is compressed.

Study [X264 Settings](http://www.chaneru.com/Roku/HLS/X264_Settings.htm)

keyint(Default: 250)

Sets the maximum interval between IDR-frames (aka keyframes) in x264's output. You can specify "infinite" to never insert non-scenecut IDR-frames.
IDR-frames are 'delimiters' in the stream - no frame can reference data from the other side of the IDR-frame. As well as this, IDR-frames are also I-frames, so they don't reference data from any other frame. This means they can be used as seek points in a video.
Note that I-frames are generally significantly larger than P/B-frames (often 10x or more in low motion scenes), so they can play havoc with ratecontrol when combined with aggressively low VBV settings (eg, sub-second buffer sizes). In these cases, investigate --intra-refresh.
The default setting is fine for most videos. When encoding for Blu-ray, broadcast, live streaming or certain 

min-keyint(Default: auto (MIN(--keyint / 10,--fps))

Sets the minimum length between IDR-frames.
See --keyint for an explanation of IDR-frames. Very small keyint ranges can cause "incorrect" IDR-frame placement (for example, a strobing scene). This option limits the minimum length in frames after each IDR-frame before another can be placed.
The maximum allowed value for min-keyint is --keyint/2+1

no-scenecut(Default: Not Set)

Completely disables adaptive I-frame decision.
See also: --scenecut

scenecut(Default: 40)

Sets the threshold for I/IDR frame placement (read: scene change detection).
x264 calculates a metric for every frame to estimate how different it is from the previous frame. If the value is lower than scenecut, a 'scenecut' is detected. An I-frame is placed if it has been less than --min-keyint frames since the last IDR-frame, otherwise an IDR-frame is placed. Higher values of scenecut increase the number of scenecuts detected. For more information on how the scenecut comparison works, see this doom9 thread.
Setting scenecut to 0 is equivalent to setting --no-scenecut.

#### options of MP4Box
`MP4Box -h all` list all options

[MP4Box Documentation](https://gpac.wp.imt.fr/mp4box/mp4box-documentation/)

## What is ffmpeg?
A complete, cross-platform solution to record, convert and stream audio and video.

We can download ffmpeg binary from [here](http://ffmpeg.zeranoe.com/builds/).

[ffmpeg document](https://ffmpeg.org/documentation.html) is very huge but very useful.

Some mp4 files, which are downloaded from youtube or produced by Microsoft Movie Maker, are not directly compatible with MP4Box. In such case, we can use ffmpeg to normalize it.
Following is the steps:(Assume mp4 file is test.mp4)

1. execute `ffmpeg -i test.mp4 testFF.mp4`, produce testFF.mp4
2. execute `mp4box.exe -dash 4000 -frag 4000 -rap -profile baseline -segment-name video/test_V_ -out test_V.mpd testFF.mp4#video`, produce test_V.mpd and corresponding video segments.
3. execute `mp4box.exe -dash 4000 -frag 4000 -rap -profile baseline -segment-name audio/test_A_ -out test_A.mpd testFF.mp4#audio`, produce test_A.mpd and corresponding audio segments.
4. merge the AdaptionSet element of test_A.mpd into test_V.mpd as sibling of AdaptionSet element of test_V.mpd.
5. use test_V.mpd as source of MPEG-DASH player.

Note 1: above steps(2,3,4) can be combined as `mp4box.exe -dash 4000 -frag 4000 -rap -profile baseline -out test_V.mpd testFF.mp4#video testFF.mp4#audio`

Note 2: `ffmpeg -y -i test.mp4 -an -s  640x360 test360.mp4 2>test360.txt` will log message in test360.txt. Inspect this file, we can see ffmpeg using x264 internally.

Note 3: Above method DO work for [Bitmovin Player](https://bitmovin.com/tutorials/get-started-bitmovin-html5-adaptive-player/). As for dash.js, the video palyer stop at about 70%--80%.

Note 4: ffmpeg with option -f dash can produce mpd, video segments, audio segments in single command. Those mpd and segemnts can be used in Bitmovin Player but not dash.js player.

Note 5: Following is a successful demo, can be played in dash.js player：
```
# OK 3:26 Input Mia.mp4 to Microsoft Movie Maker to produce MMMMia.mp4
ffmpeg -y -i ..\MMMMia.mp4 -s 640x360 test.mp4
ffmpeg -y -i ..\MMMMia.mp4 -s 480x270 -an test2.mp4
mp4box -dash 1000 -rap -profile full -out full/test.mpd test.mp4#video test.mp4#audio test2.mp4

# OK 3:45
ffmpeg -y -i ..\AdeleSD.mp4 -s 640x360 test.mp4
ffmpeg -y -i ..\AdeleSD.mp4 -s 480x270 -an test2.mp4
mp4box -dash 1000 -rap -profile full -out full/test.mpd test.mp4#video test.mp4#audio test2.mp4

# OK 3:45
ffmpeg -y -i ..\AdeleHD.mp4 -s 640x360 test.mp4
ffmpeg -y -i ..\AdeleHD.mp4 -s 480x270 -an test2.mp4
mp4box -dash 1000 -rap -profile full -out full/test.mpd test.mp4#video test.mp4#audio test2.mp4

# OK 17:53
ffmpeg -y -i ..\Full720.mp4 -s 640x360 test.mp4
ffmpeg -y -i ..\Full720.mp4 -s 480x270 -an test2.mp4
mp4box -dash 1000 -rap -profile full -out full/test.mpd test.mp4#video test.mp4#audio test2.mp4

# OK 17:53
ffmpeg -y -i ..\Full.mp4 -s 640x360 test.mp4
ffmpeg -y -i ..\Full.mp4 -s 480x270 -an test2.mp4
mp4box -dash 1000 -rap -profile full -out full/test.mpd test.mp4#video test.mp4#audio test2.mp4

```

## What is Bento4
Quoted from [bento4](https://www.bento4.com/):

Bento4 is a C++ class library and tools designed to read and write ISO-MP4 files. This format is defined in international specifications ISO/IEC 14496-12, 14496-14 and 14496-15. The format is a derivative of the Apple Quicktime file format, so Bento4 can be used to read and write most Quicktime files as well.

Features:
* MPEG DASH with fragmented MP4 files, as defined in the international specification ISO/IEC 23009-1
* MPEG Common Encryption (CENC) as specified in the international specification ISO/IEC 23001-7
* The PIFF (Protected Interoperable File Format) encrypted, fragmented MP4 format specified by Microsoft and used for encrypted HTTP Smooth Streaming is also supported.
* Reading and writing 3GPP and iTunes-compatible metadata.
* ISMA Encrytion and Decryption as defined in the ISMA E&A specification
* OMA 2.0 and 2.1 DCF/PDCF Encryption and Decryption as defined in the OMA specifications.
* ISO-MP4 files profiled as part of the  3GPP family of standards.
* The UltraViolet (DECE) CFF (Common File Format).
* MPEG CMAF (Common Media Application Format)
* Parsing and multiplexing of H.264 (AVC) video and AAC audio elementary streams
* Support for multiple DRM systems that are compatible with MP4-formatted content (usually leveraging CENC Common Encryption), such as Marlin, PlayReady, Widevine and FairPlay.
* Support for a wide range of codecs, including H.264 (AVC), H.265 (HEVC), AAC, AC3 and eAC3 (Dolby Digital), DTS, ALAC, and many more.
* Generation of HLS (HTTP Live Streaming), including HLS with fMP4 (Fragmented MP4) segments for a dual DASH/HLS output.

[bento4 documentation](https://www.bento4.com/documentation/).

## Use ffmpeg+bento4 to encode MPEG-DASH
Assume source mp4 is test.mp4, following are the procedures:
1. execute `ffmpeg -i test.mp4 test_FF.mp4`, produce test_FF.mp4.
2. execute `mp4fragment test_FF.mp4 test_FF_fragmented.mp4`, produce test_FF_fragmented.mp4.
3. execute `mp4dash test_FF_fragmented.mp4`, produce the mpd file and corresponding audio/video segments in subdirectory output.

Note 1: mp4dash is a batch file, which need python(>=2.6), python 3 is not supported.

Note 2: **above procedures DO work for mp4 files created by Microsoft Movie Maker. Can be played correctly in dash.js palyer and shaka player**.

## shaka player
[shaka player](https://github.com/google/shaka-player) is another free dash player which is created by google. It's documentation is very good.



## TODO
 * Inspect samples in Dash.js.
 * Study [dash.js Documentation](http://cdn.dashjs.org/latest/jsdoc/module-MediaPlayer.html) of dash.js
 
