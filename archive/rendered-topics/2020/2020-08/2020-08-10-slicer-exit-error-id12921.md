# Slicer exit error

**Topic ID**: 12921
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/slicer-exit-error/12921

---

## Post #1 by @Tesla2687 (2020-08-10 05:47 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>When I exit the Slicer, something wrong happened. please check the screenshot below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ad7bc8e1f278e2719cada672bc48ae87dfa1a03.jpeg" data-download-href="/uploads/short-url/jOg6t3W5SJ39mwmoaVdVg2mKeLV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ad7bc8e1f278e2719cada672bc48ae87dfa1a03_2_666x500.jpeg" alt="image" data-base62-sha1="jOg6t3W5SJ39mwmoaVdVg2mKeLV" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ad7bc8e1f278e2719cada672bc48ae87dfa1a03_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ad7bc8e1f278e2719cada672bc48ae87dfa1a03_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ad7bc8e1f278e2719cada672bc48ae87dfa1a03_2_1332x1000.jpeg 2x" data-dominant-color="E3E3E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1352×1015 395 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-08-10 12:23 UTC)

<p>Hi, thanks for the report.  Please add what steps led to this (what extensions were installed, what operations you performed).  Generally memory leaks like this aren’t harmful but we’d like to clean them up.</p>

---

## Post #3 by @lassoan (2020-08-10 13:32 UTC)

<p>The first listed object that you haven’t released from memory is a <code>vtkCollection</code>, which usually indicates that you have forgot to call <code>UnRegister</code> for a collection returned by a factory method, such as <code>slicer.mrmlScene.GetNodesByClass</code>.</p>
<p>See these pages for more information:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement">Developer FAQ- memory management</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Track_memory_leaks">Tracking memory leaks</a></li>
</ul>
<p><code>Deleting unknown object</code> error might indicate that something wrong with how the VTK object is constructed. Make sure you follow example of other MRML nodes exactly (e.g., you use <code>vtkStandardNewMacro</code> to implement <code>New()</code> method).</p>

---

## Post #4 by @Tesla2687 (2020-08-14 07:37 UTC)

<p>Hello Steve,</p>
<p>The problem has been solved after delete one extenson.</p>
<p>Thank you very much.</p>

---

## Post #5 by @Tesla2687 (2020-08-14 07:37 UTC)

<p>Hello Andras,</p>
<p>The problem has been solved after delete one extenson.</p>
<p>Thank you very much.</p>

---
