---
topic_id: 5139
title: "Best Viewer To See Your Exported Models"
date: 2018-12-19
url: https://discourse.slicer.org/t/5139
---

# Best viewer to see your exported models

**Topic ID**: 5139
**Date**: 2018-12-19
**URL**: https://discourse.slicer.org/t/best-viewer-to-see-your-exported-models/5139

---

## Post #1 by @sarvpriya1985 (2018-12-19 03:20 UTC)

<p>Operating system: WINDOWS 10<br>
Slicer version:4.10<br>
Expected behavior:<br>
Actual behavior:<br>
Hi everyone,<br>
I have been struggling with a decent viewer to look the exported models. I tried sketchfab to display OBJ format. But after exporting through slicer (converting decimal point to 0.8), i was unable to load directly into sketchfab. I had to run it via meshmixer and then export it again.<br>
But even after that, there was no color in the model in sketchfab and 3d rotation was not very smooth. Can’t say why it happened with my model as other uploaded models in the website work fine.</p>
<p>Can any one pls help me with this. Would appreciate help.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @sarvpriya1985 (2018-12-19 03:04 UTC)

<p>Hi,</p>
<p>Thanks a lot. I was able to reduce size. But when I exported the file in OBJ format, and tried to upload it into web server (sketchfab) to show model, it loses its color. Is there to fix that.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #3 by @lassoan (2018-12-19 03:43 UTC)

<p>Use “Export to files” feature (available in Segment Editor module / Segmentations… button dropdown menu), choose export to OBJ format, upload both obj and mtl file to sketchfab (in a zip file).</p>
<p>I’ve just tested this and it works nicely:</p>
<p>          <iframe src="https://sketchfab.com/models/53683f94633245748194506bf2d042f4/embed?" width="695" height="521" scrolling="no" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation">
          </iframe>
</p>

---

## Post #4 by @sarvpriya1985 (2018-12-19 11:45 UTC)

<p>Thanks Andras. I was able to upload it by doing it as a zip file. However, still when you start rotating it, it lags behind the command. I tested the already uploaded files on the website and they worked fine. Even when I played the file that you have uploaded there is a lag on my command. It is not as  smooth as it is the slicer menu.</p>
<p><a href="https://skfb.ly/6EINE" rel="nofollow noopener">https://skfb.ly/6EINE</a></p>
<p>Thanks,<br>
Sarv</p>

---

## Post #5 by @lassoan (2018-12-19 14:44 UTC)

<p>Your model has 543700 triangles, while the model above has 381500 triangles, so it is normal that it is a bit faster to render.</p>
<p>543700 triangles does not seem necessary for this model, so use the method that <a class="mention" href="/u/cpinter">@cpinter</a> described to remove dispensable triangles (you can try decimation factors between 0.8 - 0.99):</p>
<blockquote>
<p>Change segmentation conversion parameter to enable decimation: Go to Segmentations module, long-click the Create button for Closed surface, select Advanced create or Update (depending on whether you had surfaces already or not). In the popup window choose the only path, and set a non-zero Decimation factor. 0.8 means that 80% of the triangles will be removed. Then export segmentation to STL</p>
</blockquote>

---
