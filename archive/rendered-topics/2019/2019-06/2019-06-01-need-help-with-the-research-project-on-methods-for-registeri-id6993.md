---
topic_id: 6993
title: "Need Help With The Research Project On Methods For Registeri"
date: 2019-06-01
url: https://discourse.slicer.org/t/6993
---

# Need help with the research project on methods for registering some objects.

**Topic ID**: 6993
**Date**: 2019-06-01
**URL**: https://discourse.slicer.org/t/need-help-with-the-research-project-on-methods-for-registering-some-objects/6993

---

## Post #1 by @Maxi (2019-06-01 22:28 UTC)

<p>Hi, I am getting my masters, so need to complete my research project where I need to superimpose 2 objects based on certain areas (ROI) and look at the differences of other (not superimposed) parts of those 2 objects. Basically, need a method. Should be easy for those who know the program and I am willing to compensate. Any developers can help with that?</p>

---

## Post #2 by @jcfr (2019-06-03 14:13 UTC)

<p>Congratulation of wrapping up your research project, this is exciting!</p>
<blockquote>
<p>I need to superimpose 2 objects based on certain areas (ROI)</p>
</blockquote>
<p>May be you could use the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/FiducialRegistration">FiducialRegistration</a> module to align the two images.</p>
<blockquote>
<p>look at the differences of other (not superimposed) parts of those 2 objects.</p>
</blockquote>
<p>After computing the registration transform, you could display each images in a different viewer. This should allow allow you to “look” at both images.</p>
<p>You could also display the transformation. Look for “Transform display options” at <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Transforms">https://www.slicer.org/wiki/Documentation/4.10/Modules/Transforms</a></p>
<blockquote>
<p>I am willing to compensate</p>
</blockquote>
<p>While some of the <a href="https://www.slicer.org/wiki/CommercialUse#Commercial_Partners">Commercial Partners</a> could help with this, I think you should be able to get help and make progress leveraging this forum first.</p>

---

## Post #3 by @Maxi (2019-06-17 02:10 UTC)

<p>Hi, thank you for your reply, the reason I asked for help is because I am getting stuck on a very basic step. I loaded my .stl files and Slicer recognized them as “models”. Than, when I want to register, it asks me to select “volumes” to register and it seems like it does not recognize the data files I loaded.<br>
Please see attached picture<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b52d3f7f638e7aa5757c9a40fddedaeda25a5c0.jpeg" data-download-href="/uploads/short-url/fjqxWE4pwPipcab1eBZcrN3hzNe.jpeg?dl=1" title="49%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b52d3f7f638e7aa5757c9a40fddedaeda25a5c0_2_690x409.jpeg" alt="49%20PM" data-base62-sha1="fjqxWE4pwPipcab1eBZcrN3hzNe" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b52d3f7f638e7aa5757c9a40fddedaeda25a5c0_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b52d3f7f638e7aa5757c9a40fddedaeda25a5c0_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b52d3f7f638e7aa5757c9a40fddedaeda25a5c0_2_1380x818.jpeg 2x" data-dominant-color="CACBE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">49%20PM</span><span class="informations">2256×1340 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2019-06-17 13:46 UTC)

<p>You can use the ModelRegistration module in the SlicerIGT extension.</p>

---

## Post #5 by @Maxi (2019-06-17 16:43 UTC)

<p>Is it something I need to install? Or how do I access in in Slicer?</p>

---

## Post #6 by @lassoan (2019-06-17 16:51 UTC)

<p>Yes, you need to install SlicerIGT extension to get ModelRegistration module.</p>
<p>ModelRegistration module provides rigid registration. If you need deformable registration then you can convert model nodes to segmentation node (using Segmentations module, by creating a new segmentation and importing the models into it), then use Segment Registration module (provided by SegmentRegistration extension) to compute transformation between them.</p>

---
