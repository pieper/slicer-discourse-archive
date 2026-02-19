---
topic_id: 17681
title: "Buffer Queue Overflow Dropping Error In Ffmpeg On Windows"
date: 2021-05-18
url: https://discourse.slicer.org/t/17681
---

# "buffer queue overflow, dropping" error in ffmpeg on windows

**Topic ID**: 17681
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/buffer-queue-overflow-dropping-error-in-ffmpeg-on-windows/17681

---

## Post #1 by @muratmaga (2021-05-18 19:16 UTC)

<p>As per <a href="https://discourse.slicer.org/t/slicermorph-animator-yellow-highlight-on-gif-images/17653/18">this discussion</a> we have updated the Animator to match the encodings used in Screen Capture module. However, this resulted in a repeatable error in ffmpeg encoding (see video below). Same happens in Screen Capture when the number of images are set to maximum.</p>
<p>Curiously this only happens on windows, mac’s doesn’t seem to be affected.</p>
<pre><code>ffmpeg standard output:
ffmpeg error output: ffmpeg version 3.2.4 Copyright (c) 2000-2017 the FFmpeg developers
built with gcc 6.3.0 (GCC)
configuration: --enable-gpl --enable-version3 --enable-d3d11va --enable-dxva2 --enable-libmfx --enable-nvenc --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libfreetype --enable-libgme --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-libzimg --enable-lzma --enable-zlib
libavutil 55. 34.101 / 55. 34.101
libavcodec 57. 64.101 / 57. 64.101
libavformat 57. 56.101 / 57. 56.101
libavdevice 57. 1.100 / 57. 1.100
libavfilter 6. 65.100 / 6. 65.100
libswscale 4. 2.100 / 4. 2.100
libswresample 2. 3.100 / 2. 3.100
libpostproc 54. 1.100 / 54. 1.100
Input #0, image2, from 'C:/Users/amaga/AppData/Local/Temp/Slicer-zwrdHG\Slicer-%04d.png':
Duration: 00:00:12.00, start: 0.000000, bitrate: N/A
Stream #0:0: Video: png, rgb24(pc), 640x480, 25 fps, 25 tbr, 25 tbn, 25 tbc
Output #0, gif, to 'C:/Users/amaga/Desktop/after.gif':
Metadata:
encoder : Lavf57.56.101
Stream #0:0: Video: gif, pal8, 640x480, q=2-31, 200 kb/s, 60 fps, 100 tbn, 60 tbc (default)
Metadata:
encoder : Lavc57.64.101 gif
Stream mapping:
Stream #0:0 (png) -&gt; palettegen
Stream #0:0 (png) -&gt; paletteuse:default
paletteuse -&gt; Stream #0:0 (gif)
[Parsed_paletteuse_1 @ 0000000000e1e020] [framesync @ 00000000029300a8] Buffer queue overflow, dropping.
Last message repeated 71 times
frame= 0 fps=0.0 q=0.0 size= 0kB time=00:00:00.00 bitrate=N/A speed= 0x
[Parsed_paletteuse_1 @ 0000000000e1e020] [framesync @ 00000000029300a8] Buffer queue overflow, dropping.
Last message repeated 162 times
[Parsed_palettegen_0 @ 0000000000e1dee0] 255(+1) colors generated out of 88442 colors; ratio=0.002883
frame= 4 fps=4.0 q=-0.0 size= 137kB time=00:00:00.06 bitrate=18711.6kbits/s speed=0.0596x
frame= 42 fps= 28 q=-0.0 size= 2095kB time=00:00:00.69 bitrate=24870.0kbits/s speed=0.456x
frame= 65 fps= 35 q=-0.0 Lsize= 3504kB time=00:00:04.99 bitrate=5752.4kbits/s speed=2.71x
video:3503kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.036830%
Export to video...
Start ffmpeg:
C:\Users\amaga\AppData\Roaming\NA-MIC\ffmpeg\ffmpeg-3.2.4-win64-static\bin\ffmpeg.exe -nostdin -y -r 60 -start_number 0 -i C:/Users/amaga/AppData/Local/Temp/Slicer-zwrdHG\Slicer-%04d.png -filter_complex palettegen,[v]paletteuse C:/Users/amaga/Desktop/after.gif
</code></pre>
<p><code>Video export succeeded to file: C:/Users/amaga/Desktop/after.gif</code></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d1a9d64f39871e317fdc6c0559eed1aaefdc8ae.gif" alt="after" data-base62-sha1="dhDqsp56CAmiDn2LRkTE9ssO8j4" width="320" height="240" class="animated"></p>

---

## Post #2 by @lassoan (2021-05-18 19:23 UTC)

<p>I have never seen this error. How many frames did you use? What is the size of one frame?</p>
<p>You can search for this error on the web and if nothing useful comes up then report it to ffmpeg developers.</p>

---

## Post #3 by @hherhold (2021-05-18 19:27 UTC)

<p>Dunno if this helps, but an answer on stack overflow suggests inserting a fifo for this error (not exactly same params as yours, but similar error):</p>
<aside class="onebox stackexchange">
  <header class="source">

      <a href="https://stackoverflow.com/questions/39574032/ffmpeg-error-buffer-queue-overflow-dropping-when-merging-two-videos-with-del" target="_blank" rel="noopener nofollow ugc">stackoverflow.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/3357569/stefan-urbansky" target="_blank" rel="noopener nofollow ugc">
    <img alt="Stefan Urbansky" src="https://i.stack.imgur.com/r9r41.jpg?s=128&amp;g=1" class="thumbnail onebox-avatar" width="60" height="60">
  </a>

<h4>
  <a href="https://stackoverflow.com/questions/39574032/ffmpeg-error-buffer-queue-overflow-dropping-when-merging-two-videos-with-del" target="_blank" rel="noopener nofollow ugc">ffmpeg-Error "Buffer queue overflow, dropping." when merging two videos with delay</a>
</h4>

<div class="tags">
  <strong>audio, video, ffmpeg</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/3357569/stefan-urbansky" target="_blank" rel="noopener nofollow ugc">
    Stefan Urbansky
  </a>
  on <a href="https://stackoverflow.com/questions/39574032/ffmpeg-error-buffer-queue-overflow-dropping-when-merging-two-videos-with-del" target="_blank" rel="noopener nofollow ugc">01:08PM - 19 Sep 16 UTC</a>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @muratmaga (2021-05-18 19:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I have never seen this error. How many frames did you use? What is the size of one frame?</p>
</blockquote>
</aside>
<p>640x480, 300 frames…</p>

---

## Post #5 by @lassoan (2021-05-18 20:33 UTC)

<p>I was able to reproduce the problem with the ffmpeg version that ScreenCapture module installs by default. I’ve downloaded the latest version from <a href="https://www.gyan.dev/ffmpeg/builds/">here</a> and that build did not have this problem. We could update the download link to get a more recent ffmpeg version.</p>
<p>However, the resulting gif was 55MB. If you put a few of such animations in a slide deck then you can get into trouble. The same animation saved as H.265 mp4 file is 950KB. I would recommend to go with mp4 if storing if gif file size is more than a few MB.</p>

---

## Post #6 by @muratmaga (2021-05-18 20:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="17681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could update the download link to get a more recent ffmpeg version.</p>
</blockquote>
</aside>
<p>That will be great, thank you.</p>

---

## Post #7 by @lassoan (2021-05-18 21:04 UTC)

<p>Please test if the essential build is sufficient or if we need the full build (<a href="https://www.gyan.dev/ffmpeg/builds/">https://www.gyan.dev/ffmpeg/builds/</a>). Also, please check if we can delete ffplay.exe and ffprobe.exe from the package to reduce download time.</p>

---

## Post #8 by @muratmaga (2021-05-18 21:21 UTC)

<p>I downloaded the essential build, removed the ffplay and ffprobe from bin folder, reconfigured the screen capture to use this ffmpeg, and it seemed to work fine (no stutter, no error, and no complains about ffplay or ffprobe).</p>
<p>This is with the latest stable.</p>

---

## Post #9 by @lassoan (2021-05-19 14:33 UTC)

<p>I’ve updated the download link: <a href="https://github.com/Slicer/Slicer/commit/7b60eed09c2cef6358e2f67935623e8a90b28cb1" class="inline-onebox">ENH: Update ffmpeg download link for Windows to allow creating large … · Slicer/Slicer@7b60eed · GitHub</a></p>
<p>Existing ffmpeg installations will not be modified. Users who wants to upgrade need to clear their (usersetting)/ffmpeg folder to force update. The folder location can be printed by copying this command into the Python console:</p>
<pre><code class="lang-python">import os
print(os.path.dirname(slicer.app.slicerUserSettingsFilePath)+'/ffmpeg')
</code></pre>

---
