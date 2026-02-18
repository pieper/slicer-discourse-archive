# Data Import Error 

**Topic ID**: 7264
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/data-import-error/7264

---

## Post #1 by @victoria (2019-06-20 17:40 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.6.2<br>
Expected behavior: volume data loading correctly - after data import, highlighted areas will show on the MRI imported using the DCM function<br>
Actual behavior: volume data is not showing when loaded. the volumes were created using version 4.6.2 on a mac laptop, and will not load when put into the same 4.6.2 version but for pc computers.</p>

---

## Post #2 by @lassoan (2019-06-20 17:44 UTC)

<p>Please try again, saving your scene as an mrb file to make sure that all the files are included.<br>
If there is still an issue, then try saving and loading with latest stable version (Slicer-4.10.2).</p>

---

## Post #3 by @victoria (2019-06-21 19:19 UTC)

<p>I started to convert the files to the mrb format and it seems to have fixed it, however, some of them are not saving properly. Some are saving as the “slicer supported file” and others are showing as textsheet documents. I used the same steps for all of them. Is there any way to resolve this issue so all of them will open with slicer?</p>

---

## Post #4 by @lassoan (2019-06-22 03:57 UTC)

<aside class="quote no-group" data-username="victoria" data-post="3" data-topic="7264">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ea5d25/48.png" class="avatar"> victoria:</div>
<blockquote>
<p>Some are saving as the “slicer supported file” and others are showing as textsheet documents.</p>
</blockquote>
</aside>
<p>What is the file extension of the files? .mrb for all of them?<br>
Does all the file open correctly in Slicer (menu: File / Add data)?</p>

---

## Post #5 by @victoria (2019-06-24 12:44 UTC)

<p>all of the files are .mrb, some load correctly in slicer (the ones that are called “Slicer Supported File” and some are not opening properly called “Textsheet Document.”</p>

---

## Post #6 by @lassoan (2019-07-01 00:27 UTC)

<p>It seems that for some reason Textsheet (or some other software) thinks that it can open Slicer scene files as Textsheet documents. Uninstalling Textsheet (or some other software) may solve the problem. If you don’t want to do that or it does not help then you can still always open Slicer scene files using Slicer’s File menu / Add data.</p>

---
