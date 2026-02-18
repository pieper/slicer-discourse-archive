# 3D Slicer crashed when clicking on the Segment Editor button

**Topic ID**: 5349
**Date**: 2019-01-13
**URL**: https://discourse.slicer.org/t/3d-slicer-crashed-when-clicking-on-the-segment-editor-button/5349

---

## Post #1 by @f10w (2019-01-13 07:25 UTC)

<p>Hello,</p>
<p>I am working on a segmentation task and I am given an example as a <code>RTSTRUCT.dcm</code> file. After loading it into 3D Slicer, I can visualize the corresponding 3D model and the segmentation (with different colors). However, when clicking on the Segment Editor button (I want to see the labels), the app closed. I guess this is a bug? Or maybe I did something wrong.</p>
<p>I am using 3D Slicer 4.10.0 on macOS 10.14.2.</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @lassoan (2019-01-13 14:37 UTC)

<p>Do you have this problem with the latest nightly version of Slicer?</p>
<p>If yes, then most likely you have run out of memory. How much physical memory do you have in your computer? How much free disk space?</p>
<p>Freeing up 50GB disk space may solve the problem.</p>

---

## Post #3 by @f10w (2019-01-27 12:57 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a> !<br>
Sorry for my late reply, as I missed the notification email.<br>
I have 8GB of RAM, and 30GB of disk space left. Is that a bug that Slicer requires 50GB of free space for that feature? It is quite a lot :o<br>
I am going to try the nightly version and get back. Thanks!</p>

---

## Post #4 by @f10w (2019-01-27 13:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Unfortunately the SlicerRT extension, which I need, does not support the nightly build yet <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #5 by @lassoan (2019-01-27 13:46 UTC)

<p>Depending on how many structures you have and the resolution of the volume, you may need a lot of memory space. 30GB disk space should be enough if the data set is not extremely large or fine-resolution.</p>
<p>Could you try with latest stable version (4.10.1)?<br>
Can you share an anonymized data set that reproduces the problem? (or if you can save the segmentation and you can reproduce the issue by reloading that saved segmentation then that will work, too)</p>

---

## Post #6 by @f10w (2019-01-27 15:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks.<br>
4.10.1 also crashed. I am going to try it on a Linux machine to see, and try saving/reloading as you suggested as well.<br>
Regarding the data I’m not sure that I can share them, maybe but I’ll have to ask.<br>
Thanks again!</p>

---

## Post #7 by @f10w (2019-02-26 12:12 UTC)

<p>I am really sorry for my delayed feedback. I have tried on two different Linux machines (Ubuntu and Linux Mint) and the problem still occurs. I also tried saving the segmentation and reloading it but the software still crashed when I click on the Segment Editor button. I’ll send you the data by private message later today when I get home, so that you can reproduce the issue. Thanks again!</p>

---
