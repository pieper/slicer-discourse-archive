# Steps to set up 3D slicer as viewer and annotation tool

**Topic ID**: 8767
**Date**: 2019-10-13
**URL**: https://discourse.slicer.org/t/steps-to-set-up-3d-slicer-as-viewer-and-annotation-tool/8767

---

## Post #1 by @Jigabytes (2019-10-13 20:47 UTC)

<p>Hi I have requirement where I need to annotate 3D CT scan dicom image slices I would need visualization tool to be able to do so. Is it natural use case for 3D slicer workflow set up? If so can u please provide links that would help me to do this set up quickly and start manually annotating images. I have done image segmentation but I need a visual tool to see the results Thanks, Jiten</p>

---

## Post #2 by @lassoan (2019-10-16 04:17 UTC)

<aside class="quote no-group" data-username="Jigabytes" data-post="1" data-topic="8767">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jigabytes/48/4467_2.png" class="avatar"> Jigabytes:</div>
<blockquote>
<p>I have requirement where I need to annotate 3D CT scan dicom image slices I would need visualization tool to be able to do so. Is it natural use case for 3D slicer workflow set up?</p>
</blockquote>
</aside>
<p>Yes, it is a common use case.</p>
<aside class="quote no-group" data-username="Jigabytes" data-post="1" data-topic="8767">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jigabytes/48/4467_2.png" class="avatar"> Jigabytes:</div>
<blockquote>
<p>please provide links that would help me to do this set up quickly and start manually annotating images</p>
</blockquote>
</aside>
<p>See segmentation tutorials: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a></p>
<p>You may also find <a href="https://github.com/JoostJM/SlicerCaseIterator">CaseIterator extension</a> useful for iterating through a large number of annotated images.</p>
<p>If you have any specific questions then let us know.</p>

---

## Post #4 by @Jigabytes (2019-10-17 02:14 UTC)

<p>Thanks much <a class="mention" href="/u/lassoan">@lassoan</a> I will kick of setup and working on it. Is there any web version of 3D slicer ? Thanks Jiten</p>

---

## Post #5 by @lassoan (2019-10-17 02:54 UTC)

<p>Yes, you can run Slicer as a Jupyter notebook server and there are also Docker images that allows you to run Slicer in your web browser. You can find more information on these by searching on google or on this forum.</p>

---
