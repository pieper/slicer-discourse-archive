# VMTK Centerline Computation error

**Topic ID**: 12789
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/vmtk-centerline-computation-error/12789

---

## Post #1 by @janneke_slicer (2020-07-30 08:40 UTC)

<p>Hello,</p>
<p>I want to use VMTK Centerline Computation. However, I get the following error after using the Preview button (it isn’t even possible to use the Start button):<br>
‘local variable ‘vtkvmtkComputationalGeometry’ referenced before assignment’.<br>
I used Slicer 4.10.2 on Windows. I also tried to use the VMTK extension in Slicer 4.11.0, but it says it’s not available for that version.</p>
<p>I’m following the tutorials and can’t find what’s wrong. Can someone please help me?<br>
Thank you.</p>

---

## Post #2 by @lassoan (2020-07-30 13:16 UTC)

<p>Use latest Slicer Preview Release. There is a few-hour gap every morning the new nightly Slicer build is already available but not all the extensions yet. By now SlicerVMTK extension is already built (see <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK">dashboard</a>).</p>

---

## Post #3 by @janneke_slicer (2020-07-30 13:51 UTC)

<p>Thank you, it works!<br>
I downloaded the latest Release again and now I can install the VMTK extension.</p>

---

## Post #4 by @LeeaLee12345 (2021-12-12 11:34 UTC)

<p>Hello, I also have this problem. I have replaced multiple 3D slicer versions and failed. How can I solve it<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1982162acb7b88043511dda5546661639a02dfd1.jpeg" data-download-href="/uploads/short-url/3DEE3cVzqim7xB0TRZH8Yk8JFPX.jpeg?dl=1" title="problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1982162acb7b88043511dda5546661639a02dfd1_2_690x391.jpeg" alt="problem" data-base62-sha1="3DEE3cVzqim7xB0TRZH8Yk8JFPX" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1982162acb7b88043511dda5546661639a02dfd1_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1982162acb7b88043511dda5546661639a02dfd1_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1982162acb7b88043511dda5546661639a02dfd1_2_1380x782.jpeg 2x" data-dominant-color="C1C2D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem</span><span class="informations">1920×1090 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2021-12-14 17:42 UTC)

<p>You need to use a more recent Slicer version. Since the latest Slicer Stable Release is rather old, I would recommend using the latest Slicer Preview Release.</p>

---

## Post #6 by @LeeaLee12345 (2021-12-21 07:18 UTC)

<p>Thank you very much! This works！</p>

---

## Post #8 by @lassoan (2023-02-27 16:52 UTC)

<p>A post was split to a new topic: <a href="/t/unit-of-radius-an-length-in-vmtk-centerline-computation/28072">Unit of radius an length in VMTK centerline computation</a></p>

---
