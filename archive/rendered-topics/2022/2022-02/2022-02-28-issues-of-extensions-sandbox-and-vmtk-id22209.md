# Issues of Extensions-Sandbox and VMTK

**Topic ID**: 22209
**Date**: 2022-02-28
**URL**: https://discourse.slicer.org/t/issues-of-extensions-sandbox-and-vmtk/22209

---

## Post #1 by @xiaolin (2022-02-28 10:15 UTC)

<p>Hi, I am a doctoral student.<br>
I am working on the 4D reconstruction of animal cardiac CT now. I am having several issues when I installed the extensions.<br>
Windows 10 Professional version.</p>
<ol>
<li>VMTK extension is unavailable on Slicer 4.13.0. 2022-05-25</li>
<li>Sandbox extension is unavailable on Slicer 4.11.20210226<br>
Could please help me to figure them out? Or there are issues with these extensions which are under being improved?<br>
Furthermore, does anybody know how to crop the 4D volume from 4d cardiac CT? When I cropped the volume from a 4d cardiac CT, the results were like a screenshot from each frame of the 4D sequence, it was a 3D volume, not a dynamic 4d volume.<br>
Thanks a lot and best wishes.</li>
</ol>

---

## Post #2 by @chir.set (2022-02-28 10:53 UTC)

<aside class="quote no-group" data-username="xiaolin" data-post="1" data-topic="22209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/x/c4cdca/48.png" class="avatar"> xiaolin:</div>
<blockquote>
<p>VMTK extension is unavailable on Slicer 4.13.0. 2022-05-25</p>
</blockquote>
</aside>
<p>I suppose you mean 2022-02-25.</p>
<p>SlicerVMTK does not build currently with recently updated VTK used by Slicer. It can be fixed in different ways, pending <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/56" rel="noopener nofollow ugc">advice</a> on which way to follow. I hope it gets back online soon.</p>

---
