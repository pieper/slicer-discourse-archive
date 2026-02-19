---
topic_id: 26426
title: "Extract Centerline Start In Py"
date: 2022-11-24
url: https://discourse.slicer.org/t/26426
---

# Extract CenterLine - Start in py

**Topic ID**: 26426
**Date**: 2022-11-24
**URL**: https://discourse.slicer.org/t/extract-centerline-start-in-py/26426

---

## Post #1 by @lucas_sd (2022-11-24 16:32 UTC)

<p>Hi,</p>
<p>I have two points and a segmentation and I would like to obtain the center line. I did that using the extension VMTK and now I would like to do this in my phyton script, just like an other part of my process.</p>
<p>Can I use slicer.modules.extractcenterline.logic() for that? How? Can anybody share un example to guide me? I saw the extratcenterline.py but Im really lost.</p>
<p>Thanks, Lucas.</p>

---

## Post #2 by @chir.set (2022-11-24 18:38 UTC)

<p>If your script runs inside Slicer, you can get the logic class this way :</p>
<pre><code class="lang-auto">import ExtractCenterline
extractCenterlineLogic = ExtractCenterline.ExtractCenterlineLogic()
</code></pre>
<p>It contains everything you need to work with your inputs.</p>

---

## Post #3 by @lucas_sd (2022-11-28 17:42 UTC)

<p>Hi Chir, once again thanks for your help. I used the same logic to use the module CurvedPlanar and it worked very well.<br>
Thanks!</p>

---
