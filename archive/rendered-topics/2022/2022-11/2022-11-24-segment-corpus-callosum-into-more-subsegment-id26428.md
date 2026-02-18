# Segment corpus callosum into more subsegment

**Topic ID**: 26428
**Date**: 2022-11-24
**URL**: https://discourse.slicer.org/t/segment-corpus-callosum-into-more-subsegment/26428

---

## Post #1 by @bnc0720 (2022-11-24 20:09 UTC)

<p>Hello Everyone,</p>
<p>I want to segment the corpus callosum into 5 subsegment to compare them with each other.<br>
Is there any solution, trick for that in Slicer3D?<br>
I attached a picture to help to illustrate our goal.</p>
<p>I did the main segmentation with grow from seeds.</p>
<p>Thank You the answers!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e5151132ff6311ac94cbe2b07cc536c8b78432.png" alt="image" data-base62-sha1="nf29IB6FyzPnm4AundTg64HB1HY" width="600" height="336"></p>

---

## Post #2 by @lassoan (2022-11-25 16:29 UTC)

<p>You could automate this splitting many different ways. One possibility would be to draw the AP line using a markups line (you can do it manually or you could get the oriented bounding box using Segment Statistics module), then compute cutting planes (the white lines you show in your image). You can use those planes in “Dynamic modeler” module’s “Plane cut” tool, on the model of the Corpus callosum (that you exported from the segmentation).</p>

---
