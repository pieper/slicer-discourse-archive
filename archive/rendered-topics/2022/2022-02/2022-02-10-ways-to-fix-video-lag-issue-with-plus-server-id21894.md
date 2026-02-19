---
topic_id: 21894
title: "Ways To Fix Video Lag Issue With Plus Server"
date: 2022-02-10
url: https://discourse.slicer.org/t/21894
---

# Ways to Fix Video Lag Issue with Plus Server

**Topic ID**: 21894
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/ways-to-fix-video-lag-issue-with-plus-server/21894

---

## Post #1 by @Srijeet_Chatterjee (2022-02-10 14:07 UTC)

<p>Hi everyone,</p>
<p>I am trying to record videos (.mkv format) using the PlusServerRemoteControl.exe from two different epiphan framegrabbers. I find that there is a lag in the recorded videos when I am playing it. Can anyone please suggest me ways to improve the video quality and overcome the lag.</p>
<p>Thank you,<br>
Best regards,<br>
Srijeet</p>

---

## Post #2 by @lassoan (2022-02-10 20:08 UTC)

<p>Check that your configuration is optimized for performance:</p>
<ul>
<li>
<code>Enabled item skip during playback</code> is checked in Sequences module’s Advanced section</li>
<li>
<code>Save changes</code> is enabled for video streams (that allows making a shallow-copy of the images from the sequence into the scene, which is faster than deep-copy)</li>
<li>Window/level is set to <code>Manual W/L</code> for all volume proxy nodes in Volumes module → Display section (auto-window/level takes a little bit of time, manual mode disables the computation)</li>
<li>Remove any unnecessary rendering that may slow down the rendering (such as volume rendering, markups, or complex models)</li>
</ul>
<p>If these don’t help then you can reduce the amount of data to process (reduce the frame size, frame rate, color depth) or upgrade your hardware. If these are not feasible then do profiling (e.g., using VerySleepy) and report what are the performance bottlenecks when you replay the videos.</p>

---

## Post #3 by @Srijeet_Chatterjee (2022-02-11 08:58 UTC)

<p>Thank you so much, the optimization helped!</p>
<p>Best regards,<br>
Srijeet</p>

---

## Post #4 by @lassoan (2022-02-11 12:54 UTC)

<p>Thanks for the update. Do you know which recommendations were the most impactful for your use case?</p>

---

## Post #5 by @Srijeet_Chatterjee (2022-02-14 20:53 UTC)

<p>Upgrading the Hardware (6 cores to 12 cores) was most impactful in my case while recording. Also I enabled the item skip during playback and Window/level is set to <code>Manual W/L</code> while replay.</p>

---

## Post #6 by @Srijeet_Chatterjee (2022-05-16 09:42 UTC)

<p>I am getting back to the this old post, because I face another problem with recording the videos. I need to perform some image processing algorithms which utilises a lot of CPU as well. But at the same time I need to record.</p>
<p>Is there a possibilty to somehow use the GPU while recording? to avoid lags and obtain better video quality with the recording of the plus server.</p>

---

## Post #7 by @lassoan (2022-05-16 23:44 UTC)

<p>Recording requires lots of RAM (to record into memory) and/or fast disk. GPU could make compression faster, but it would be still an overhead to pass the images to the GPU and get back the compressed data from the GPU, so it would overall slow things down compared to direct uncompressed writing to main memory or disk.</p>
<p>If you find that one computer cannot reliable handle all the tasks then you can offload either the recording. For example:</p>
<ul>
<li>Use a “data acquisition computer” that records data locally to disk and broadcasts the recorded data via OpenIGTLink. The “visualization and processing computer” would receive the data via OpenIGTLink and process and display the data (and would not need to worry about recording).</li>
<li>Use a “main computer” for acquiring, recording, and visualization; and use a “processing” computer that receives data from the main computer, processes it, and sends it back to the main computer.</li>
</ul>
<p>If you find that your computer has idle cores then you can distribute the workload over several processes on the same computer (e.g., do the processing in several separate processes, using for example the <a href="https://github.com/pieper/SlicerParallelProcessing">ParallelProcessing extension</a>.</p>

---

## Post #8 by @Srijeet_Chatterjee (2022-05-17 07:12 UTC)

<p>Thanks a lot for your suggestions. I would try them out!</p>

---
