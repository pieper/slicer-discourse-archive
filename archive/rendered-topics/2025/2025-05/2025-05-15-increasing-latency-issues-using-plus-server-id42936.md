---
topic_id: 42936
title: "Increasing Latency Issues Using Plus Server"
date: 2025-05-15
url: https://discourse.slicer.org/t/42936
---

# Increasing latency issues using Plus Server

**Topic ID**: 42936
**Date**: 2025-05-15
**URL**: https://discourse.slicer.org/t/increasing-latency-issues-using-plus-server/42936

---

## Post #1 by @orionwiersma (2025-05-15 03:15 UTC)

<p>Hello, I’m having issues with an increase in latency in slicer. The outputted stream suffers from a constant increase in latency.<br>
I suspect the issue has to do with a delay in plus server. When I run the stream directly on VLC media, the output remains at a constant latency (around 620ms), however as soon as I run plus server, latency begins to increase steadily (over 30s delay after ~10min of having it running).  Restarting plus server resets the latency, but it increases again in the same manner over time.<br>
For context I’m running an Android emulator off of my PC, with FFmpeg and MediaMTX as the streaming ports. Is this an issue seen before?</p>
<p>Any help or insight would be appreciated.</p>

---

## Post #2 by @lassoan (2025-05-15 03:17 UTC)

<p>Can you copy here your PLUS configuration file?<br>
Can you provide instructions on how to reproduce the problem the simplest possible way?</p>

---

## Post #3 by @orionwiersma (2025-05-15 12:34 UTC)

<p>Hi,</p>
<p>Here is a onedrive link to the configuration file: <a href="https://dalu-my.sharepoint.com/:u:/g/personal/or942416_dal_ca/ESpUVZGBOE9Hnb-xVyVzMPoBC4X3bNsyOySIwiFcxY4VKA" rel="noopener nofollow ugc">PlusDeviceSet_Server_L12-4_35mm_No_WebCam_No_OptiTrack_ffmpeg.xml</a><br>
Note that I’ve commented out opti track and a webcam we were using to help with debugging.</p>
<p>Instructions (I’m operating on a Windows 11 Machine):</p>
<ol>
<li>
<p>Download/run an android emulator, I use <a href="https://www.genymotion.com/product-desktop/download/" rel="noopener nofollow ugc">Genymotion</a> (its free and is easiest to install)<br>
i. I’m running a custom tablet version 12.1. Increase Hardware specs if you’d like but default settings for the rest is fine.<br>
ii. For testing latency I play the stopwatch on the android to check for noticeable time changes.</p>
</li>
<li>
<p>Download/run MediaMTX<br>
i. In a new terminal cd to mediamtx folder and run mediamtx.exe</p>
</li>
</ol>
<ul>
<li>If this works correctly, you should see a line saying:</li>
</ul>
<p>“[RTSP] listener opened on :8554 (TCP), :8000 (UDP/RTP), :8001 (UDP/RTCP)” * Allow this application to continue running in the background.</p>
<ol start="3">
<li>Download/run FFmpeg.<br>
i. In a new termainl cd to /ffmpeg/bin and run:</li>
</ol>
<p>ffmpeg -f gdigrab -draw_mouse 0 -framerate 60 -i title=“Title of Window goes here” -c:v libx264 -preset ultrafast -crf 28 -tune zerolatency -f rtsp rtsp://localhost:8554/live.sdp</p>
<p>Note: Change the title of the window to the window of the android emulator.</p>
<ul>
<li>If this works correctly, you should see an increasing counter showing the number of frames that have been sent. Allow this application to continue running in the background.</li>
</ul>
<ol start="4">
<li>Run fCal (or Plus Server Launcher → Slicer if you’d like) and check to see an increase in latency. After a few minutes you should see an increase in difference between the stop watch on the android and the stop watch streamed through plus server.</li>
</ol>
<p>Here is a video of me running through the process with the increasing delay: <a href="https://dalu-my.sharepoint.com/:v:/g/personal/or942416_dal_ca/EbE8tfIZFZpLhHpO3JgSi_AB188hfCxxFlTiAS7Ah8m6Zg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&amp;e=1IfRoj" rel="noopener nofollow ugc">Plus_Server_Latency_video.mp4</a></p>
<p>Comparing with a VLC stream (where there is no change in latency), I believe this issue has to do with the way plus server is processing the stream. This could also have to do with the android emulator being used. Please let me know if I should clarify anything else.</p>

---

## Post #4 by @orionwiersma (2025-05-15 17:36 UTC)

<p>I was able to resolve the issue. I think it had to do with the bit rate that the stream was being rendered at as this caused slow connection issues to increase latency.</p>

---
