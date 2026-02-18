# vtkMRMLSequenceBrowserNode Playback Speed

**Topic ID**: 32167
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/vtkmrmlsequencebrowsernode-playback-speed/32167

---

## Post #1 by @nicholas489 (2023-10-11 18:16 UTC)

<p>Machine 1:<br>
Operating System: macOS 14.0<br>
Processor: Apple M2 CPU @ 3.00 GHz, 3000 MHz, 8 Core(s) 8 Logical Processor(s)<br>
Installed Physical Memory: 16 GB</p>
<p>Machine 2:<br>
Operating System: Windows 10 x64-based PC<br>
Processor: Intel® Core™ i5-6300U CPU @ 2.40GHz, 2400 Mhz, 2 Core(s), 4 Logical Processor(s)<br>
Installed Physical Memory (RAM): 8.00 GB</p>
<p>Slicer version: 5.4.0 stable release<br>
Expected behaviour: After loading .mha images into vtkMRMLSequenceBrowserNode to then display this sequence image-by-image on 3d slicer at a default rate of 1 image per second, and editing the method <code>SetPlaybackRateFps</code> to display say for example 3 images per second<br>
Actual behaviour: Machine 1 does the expected behaviour fine without any issues, but Machine 2 will start skipping to later images in the sequence (while playing the sequence went from Image <span class="hashtag-raw">#19</span> to Image <span class="hashtag-raw">#32</span> in 1 second with <code>SetPlaybackRateFps</code> of 3)</p>
<p>Kindly let me know if this issue is occuring due to hardware limitations or any other reason as to why this could be occuring</p>

---

## Post #2 by @lassoan (2023-10-12 03:20 UTC)

<p>Machine2 cannot replay the sequence at the requested rate. This computer is about 8 years old (has a 6-th generation Intel CPU - while the current generation is 13), so  it is normal that it is much slower.</p>
<p>To play at the maximum rate without skipping: you can disable “Enable item skip during playback” option in Sequences module / Browser / Advanced.</p>

---

## Post #3 by @nicholas489 (2023-10-13 19:34 UTC)

<p>Thank you for your reply, it seems to be working now!</p>

---
