---
topic_id: 32115
title: "Software Crashes On Macbook Pro With M2 Chip"
date: 2023-10-09
url: https://discourse.slicer.org/t/32115
---

# Software crashes on MacBook Pro with m2 chip

**Topic ID**: 32115
**Date**: 2023-10-09
**URL**: https://discourse.slicer.org/t/software-crashes-on-macbook-pro-with-m2-chip/32115

---

## Post #1 by @Madhu_Ar (2023-10-09 11:54 UTC)

<p>Hello,<br>
I have the 3D slicer software on a MacBook Pro with m2 chip. I meets all system requirements. However, while using the software if I take a break the software just stops responding and I loose data because I cannot save anything.<br>
Can someone please help me with this issue.</p>

---

## Post #2 by @lassoan (2023-10-09 11:58 UTC)

<p>Please try the latest Slicer Preview Release and let us know if your still experience problems. Puttonyos more details about the size of your data, memory size of your computer, and what is the operation that fails (during segmentation? while using which effect? while deleting data from the scene?..)</p>

---

## Post #3 by @Madhu_Ar (2023-10-09 15:46 UTC)

<p>Hello I tried even the latest 5.5 version and that crashes too. My ram is 16 gb,  memory in my computer is 500 gb , size of file is 252mb.<br>
It happens during segmentation and sometimes after I used grow from seeds.<br>
So if I minimize it for sometime when I am working on something else and come back , it will be frozen and I cannot do anything else but to force quit it.</p>

---

## Post #4 by @lassoan (2023-10-10 11:03 UTC)

<p>Thank you, this is already helpful, but we would need more specific information about what do you do exactly during segmentation so that we can reproduce the issue.</p>
<p>How much free disk space do you have?</p>
<p>Can you copy here the content of the crash reporting window?</p>

---

## Post #5 by @Madhu_Ar (2023-10-10 12:04 UTC)

<p>I have almost 500gb of disk free space.<br>
It does not give me crash report. It just freezes.<br>
So after segmentation or sometimes even during I usually just place the seeds. It most often happens when I minimize the screen to work on some other program.</p>

---

## Post #6 by @lassoan (2023-10-10 20:36 UTC)

<aside class="quote no-group" data-username="Madhu_Ar" data-post="5" data-topic="32115">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/madhu_ar/48/67789_2.png" class="avatar"> Madhu_Ar:</div>
<blockquote>
<p>It most often happens when I minimize the screen to work on some other program.</p>
</blockquote>
</aside>
<p>This is most likely due to some issues with Qt (the GUI toolkit that Slicer uses) and the operating system. Upgrading your operating system might fix it (if you are not using the latest already). If that does not help then it might be fixed when <a href="https://github.com/Slicer/Slicer/issues/6388">Qt in Slicer is updated to Qt6</a> and/or <a href="https://github.com/Slicer/Slicer/issues/5944">Slicer is built natively to ARM architecture</a> - expected within about 6-12 months. Until then you may consider using an Intel macOS system or save more frequently.</p>

---
