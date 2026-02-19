---
topic_id: 32503
title: "Alpaca Segmentation"
date: 2023-10-31
url: https://discourse.slicer.org/t/32503
---

# ALPACA & segmentation

**Topic ID**: 32503
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/alpaca-segmentation/32503

---

## Post #1 by @Michal_Graitzer (2023-10-31 12:31 UTC)

<p>Operating system: windows<br>
Slicer version:5.2.1</p>
<p>Does the use of “Alpaca” require prior segmentation?</p>

---

## Post #2 by @muratmaga (2023-10-31 14:58 UTC)

<p>ALPACA does not require segmentation, but it expects you will provide models that have comparable anatomy. If you don’t, performance will suffer.</p>
<p>So if your existing models are of the same anatomical region/content, no segmentation/cleanup is necessary.</p>

---

## Post #3 by @Michal_Graitzer (2023-11-08 10:26 UTC)

<p>Thank you for your answer.</p>
<p>I have a DICOM file, and I cropped the volume for my purposes, but I am not able to save it as a 3d file suitable for ALPACA, such as ply* file that is recommended.<br>
What can I do?</p>
<p>Thank you for your help<br>
Michal</p>
<p>‫בתאריך יום ג׳, 31 באוק׳ 2023 ב-16:58 מאת ‪Murat Maga via 3D Slicer Community‬‏ &lt;‪<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>‬‏&gt;:‬</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb13cfd92e1bf7553a206a418204cc218ac813da.png" alt="image001.png" data-base62-sha1="zP8i63JcFF7B2tUar6lVNbztAvw" width="146" height="63"></p>

---

## Post #4 by @muratmaga (2023-11-08 15:23 UTC)

<p>Process of making 3D models out of volumetric data is called swgmentation. You can read about it more here <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<p>The tool to use is segment editor, after you can export your segmentation to ply nd use it with alpaca.</p>

---
