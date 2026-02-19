---
topic_id: 2909
title: "Elastix Fails To Update Resampled Image And Transform"
date: 2018-05-23
url: https://discourse.slicer.org/t/2909
---

# Elastix fails to update resampled image and transform

**Topic ID**: 2909
**Date**: 2018-05-23
**URL**: https://discourse.slicer.org/t/elastix-fails-to-update-resampled-image-and-transform/2909

---

## Post #1 by @dzenanz (2018-05-23 14:26 UTC)

<p>I am using a downloaded Slicer 4.9.0-2018-05-04 r27180. Using sample data MRBrainTumor1 and MRBrainTumor2, I try to register them using SlicerElastix extension. I tried a couple of presets (<code>3D MRI, monomodal (brain)</code> among them), but that doesn’t seem to matter. After registration is finished:</p>
<pre><code>Volume registration is started in working directory: C:/Temp/User/Slicer/Elastix/20180523_093922_751
Register volumes...
Generate output...
Registration is completed
</code></pre>
<p>Nothing looks changed. If I try to save the scene, the transform and resampled volume are not selected by default, meaning they are empty nodes.</p>
<p>If I go to the temp folder and load the intermediate images (e.g. <code>result.hdr</code>), they are correctly resampled. Can anyone confirm this?</p>

---

## Post #2 by @lassoan (2018-05-23 17:20 UTC)

<p>It works well for me with “generic (all)” preset? Have you tried with that?</p>

---

## Post #3 by @dzenanz (2018-05-23 19:08 UTC)

<p><code>generic (all)</code> and <code>generic (rigid)</code> do work now, but I could have sworn they didn’t work earlier today. <code>3D MRI, monomodal (brain)</code> does not work in repeated tests. This applies both to 4.9.0-2018-05-04 r27180 and today’s nightly.</p>

---

## Post #4 by @dzenanz (2018-05-23 20:18 UTC)

<p><a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> was able to reproduce this on his computer. I submitted an <a href="https://issues.slicer.org/view.php?id=4562" rel="nofollow noopener">issue</a>.</p>

---

## Post #5 by @lassoan (2018-05-24 04:46 UTC)

<p>Issue fixed (input file format in the parameter file was set incorrect), should work in tomorrow’s nightly build.</p>

---

## Post #6 by @Andinet_Enquobahrie (2018-05-24 15:15 UTC)

<p>I tested it. it looks good. Thanks for fixing it. -Andinet</p>

---
