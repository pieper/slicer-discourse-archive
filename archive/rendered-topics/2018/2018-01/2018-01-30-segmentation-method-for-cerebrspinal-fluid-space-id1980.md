# Segmentation method for cerebrspinal fluid space

**Topic ID**: 1980
**Date**: 2018-01-30
**URL**: https://discourse.slicer.org/t/segmentation-method-for-cerebrspinal-fluid-space/1980

---

## Post #1 by @Omkar_Kaskar (2018-01-30 22:30 UTC)

<p>Hi,<br>
I am a new 3D slicer user. I am looking to build a 3D model of the cerebrospinal fluid space from CT images of the human brain. I was wondering if someone could elaborate on how I should go about it. I tried using thresholding in the editor module as they have a predefined scale for CSF space, but that didn’t quite work out.<br>
Any help would be great!</p>

---

## Post #2 by @lassoan (2018-01-30 23:19 UTC)

<aside class="quote no-group" data-username="Omkar_Kaskar" data-post="1" data-topic="1980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/7ba0ec/48.png" class="avatar"> Omkar_Kaskar:</div>
<blockquote>
<p>I tried using thresholding in the editor module as they have a predefined scale for CSF space, but that didn’t quite work out</p>
</blockquote>
</aside>
<p>What was the problem?</p>
<p>In general, if there is intensity difference between regions that you would like to separate, “Grow from seeds” effect works very  well. You would paint a few strokes (“seeds”) with the Paint effect inside CSF using one segment, and outside using another segment. Then, “Grow from seeds” effect should be able to create a complete CSF segmentation. If the results are not perfect then you can interactively edit the seeds. Check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">these tutorials</a> to learn how to use Grow from seeds and other effects.</p>

---
