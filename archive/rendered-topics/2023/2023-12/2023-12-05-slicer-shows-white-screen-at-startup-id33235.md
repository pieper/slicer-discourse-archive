# Slicer shows white screen at startup

**Topic ID**: 33235
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/slicer-shows-white-screen-at-startup/33235

---

## Post #1 by @Yangtting (2023-12-05 13:14 UTC)

<aside class="quote no-group quote-modified" data-username="Eduardo_Hernandez" data-post="6" data-topic="17792" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eduardo_hernandez/48/17229_2.png" class="avatar"><a href="https://discourse.slicer.org/t/slicer-does-not-open/17792/6">slicer does not open</a></div>
<blockquote>
<p>I’ve jus installed 3DSlicer 5.0.3 on my computer and it just stays on white screen and does not open anything, not even the threat of starting.<br>
What do you think is happening?<br>
Thanks in advance!</p>
</blockquote>
</aside>
<p>Dear Sir, I met the same problem, after I installed 3D Slicer 5.6.0 on my computer, it stays on white screen. Here are the specs of my computer:<br>
Operating system : windows 10<br>
Processor : 13th Gen Intel(R) Core™ i9-13900K   3.00 GHz<br>
RAM : 64.00 GB<br>
GPU : NVIDIA RTX A6000</p>
<p>What do you think is happening?<br>
Thanks in advance!</p>

---

## Post #2 by @Yangtting (2023-12-05 14:46 UTC)

<p>Oh，I forgot I have two NVIDIA A6000，someone suggested that maybe the two  graphics cards is the reason, I really needs  your  help! Thanks  very much!</p>

---

## Post #3 by @lassoan (2023-12-05 16:03 UTC)

<p>Most likely it is a driver issue. Have you installed the latest drivers? Can you try with disabling one and the other graphics card?</p>

---

## Post #4 by @muratmaga (2023-12-05 16:58 UTC)

<aside class="quote no-group" data-username="Yangtting" data-post="1" data-topic="33235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yangtting/48/67841_2.png" class="avatar"> Yangtting:</div>
<blockquote>
<p>Processor : 13th Gen Intel(R) Core™ i9-13900K 3.00 GHz</p>
</blockquote>
</aside>
<p>We use A6000 daily, they work great with Slicer. Make sure windows settings for Slicer is set to use the A6000, as opposed to the internal GPU on i9. See this <a href="https://discourse.slicer.org/t/windows-10-is-now-handling-the-gpu-selection/13064" class="inline-onebox">WIndows 10 is now handling the gpu selection</a></p>

---

## Post #5 by @Yangtting (2023-12-08 04:53 UTC)

<p>Thanks for your help! I tried to change windows settings to make sure that A6000 was used for Slicer. However, it still occurs the problem even though I also had updated the newest drivers. I’m wondering if it’s because I’ve previously set up the “monailabel” python environment. I’m looking forward to your reply! Thanks again!</p>

---

## Post #6 by @jcfr (2023-12-08 06:55 UTC)

<blockquote>
<p>I’m wondering if it’s because I’ve previously set up the “monailabel” python environment</p>
</blockquote>
<p>Since each Slicer installation comes with its own Python environment, you could re-download the latest version of Slicer, install it in a different folder and try again.</p>
<p>You can read more at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html</a></p>

---

## Post #7 by @Yangtting (2023-12-08 13:06 UTC)

<p>Thanks for your help! I had solved it!</p>

---

## Post #8 by @muratmaga (2023-12-08 15:31 UTC)

<p>What was the solution? So that others can benefit from it.</p>

---

## Post #9 by @Yangtting (2023-12-09 01:45 UTC)

<p>I am using a desktop computer, but I did not connect the monitor before. After connecting the monitor, it returned to normal. It may be that the graphics output cannot be configured because the monitor is not connected.</p>

---

## Post #10 by @cpinter (2023-12-09 21:21 UTC)

<p>Thanks for letting us know. FYI, if you don’t want to have a monitor always connected you can buy an HDMI dummy plug (also called display emulator or headless adapter) that fixes this issue but does not occupy space or consume electricity.</p>

---

## Post #11 by @Yangtting (2023-12-11 02:07 UTC)

<p>Thanks for your suggestion! Have a nice day!</p>

---
