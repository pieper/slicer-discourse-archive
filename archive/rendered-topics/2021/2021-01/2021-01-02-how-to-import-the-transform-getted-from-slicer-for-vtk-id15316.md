---
topic_id: 15316
title: "How To Import The Transform Getted From Slicer For Vtk"
date: 2021-01-02
url: https://discourse.slicer.org/t/15316
---

# How to import the transform getted from slicer for vtk?

**Topic ID**: 15316
**Date**: 2021-01-02
**URL**: https://discourse.slicer.org/t/how-to-import-the-transform-getted-from-slicer-for-vtk/15316

---

## Post #1 by @timeanddoctor (2021-01-02 11:47 UTC)

<p>I registrated two model in slicer and get the transform but it is not the same with VTK.(The promblem may be “different coordinate system” )<br>
I searched the forum to deal with it by python code(get the slicer’s transformcould be import in vtk) but get nothing.<br>
And another problem: can I set the same coordinate system between VKT and slicer?<br>
Thanks.<br>
The different results:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d694e347a1436591cc7b8cc0a837239313ff59a.jpeg" data-download-href="/uploads/short-url/6tJ6kCoCTzFaAY9kPfRiEQAFXpE.jpeg?dl=1" title="屏幕截图 2021-01-02 174905" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d694e347a1436591cc7b8cc0a837239313ff59a_2_540x500.jpeg" alt="屏幕截图 2021-01-02 174905" data-base62-sha1="6tJ6kCoCTzFaAY9kPfRiEQAFXpE" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d694e347a1436591cc7b8cc0a837239313ff59a_2_540x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d694e347a1436591cc7b8cc0a837239313ff59a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d694e347a1436591cc7b8cc0a837239313ff59a.jpeg 2x" data-dominant-color="C2BEBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2021-01-02 174905</span><span class="informations">712×659 91.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-02 21:23 UTC)

<p>The Transforms module developer documentation should answer all your questions: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html#transform-files">https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html#transform-files</a></p>
<p>If anything is not clear then let us know.</p>

---
