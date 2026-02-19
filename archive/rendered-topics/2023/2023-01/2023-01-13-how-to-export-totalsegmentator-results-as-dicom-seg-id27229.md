---
topic_id: 27229
title: "How To Export Totalsegmentator Results As Dicom Seg"
date: 2023-01-13
url: https://discourse.slicer.org/t/27229
---

# How to export TotalSegmentator results as DICOM SEG?

**Topic ID**: 27229
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/how-to-export-totalsegmentator-results-as-dicom-seg/27229

---

## Post #1 by @fedorov (2023-01-13 14:56 UTC)

<p>I would like to export results of TotalSegmentator into DICOM Segmentation format. I am using latest Slicer stable 5.2.1 on Mac.</p>
<p>I loaded input CT series from DICOM Browser. I have QuantitativeReporting extension installed. However, segmentation results are not automatically placed properly in the patient hierarchy on segmentation completion, see below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b15093f06afe28ae57292bb4c96b55404271d6a.jpeg" data-download-href="/uploads/short-url/jQnr9VHcwlTdxUp3dyNy8rIyqQq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b15093f06afe28ae57292bb4c96b55404271d6a_2_690x423.jpeg" alt="image" data-base62-sha1="jQnr9VHcwlTdxUp3dyNy8rIyqQq" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b15093f06afe28ae57292bb4c96b55404271d6a_2_690x423.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b15093f06afe28ae57292bb4c96b55404271d6a_2_1035x634.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b15093f06afe28ae57292bb4c96b55404271d6a_2_1380x846.jpeg 2x" data-dominant-color="D7D7DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1528×938 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I then manually drop segmentation under the patient node, but I am still getting the same error when I select the segmentation node and try to “Export to DICOM…”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/767b35046a61155cb8ec6ee804903724dcd35e84.gif" alt="2023-01-13_09-54-22" data-base62-sha1="gU8jjqdlCDIj4nLf1ijs2HK5fuI" width="690" height="410" class="animated"></p>
<p>If I click “OK” in the shown popup, a dummy patient item is created in the hierarchy, which is definitely not what I want to do.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ab95b376f9d9c19eaaabc82d53c960a35bdd9aa.jpeg" data-download-href="/uploads/short-url/m4KEzYRerZlmbmP2seauUHBHjZ0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ab95b376f9d9c19eaaabc82d53c960a35bdd9aa_2_690x454.jpeg" alt="image" data-base62-sha1="m4KEzYRerZlmbmP2seauUHBHjZ0" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ab95b376f9d9c19eaaabc82d53c960a35bdd9aa_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ab95b376f9d9c19eaaabc82d53c960a35bdd9aa_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9ab95b376f9d9c19eaaabc82d53c960a35bdd9aa_2_1380x908.jpeg 2x" data-dominant-color="E8E8EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1500×988 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>cc: <a class="mention" href="/u/justin_kirby">@Justin_Kirby</a></p>

---

## Post #2 by @pieper (2023-01-13 23:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> have you ever tried this?  The terminology should be good so maybe it’s just a matter of setting up the subject hierarchy to connect the segmentation results to the study.  Maybe you have suggestions <a class="mention" href="/u/cpinter">@cpinter</a>  ?</p>

---

## Post #3 by @lassoan (2023-01-14 04:14 UTC)

<p>Yes, it all works!</p>
<p>Probably the reference volume was not set in the segmentation. I’ve tried to explain this in the message in the DICOM export dialog (see red text):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0116885085ecb472d66e6a564b6f058bbc53c95d.png" data-download-href="/uploads/short-url/9CKGQRbhB1qEdoS5fm9rwXoGmN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0116885085ecb472d66e6a564b6f058bbc53c95d_2_690x480.png" alt="image" data-base62-sha1="9CKGQRbhB1qEdoS5fm9rwXoGmN" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0116885085ecb472d66e6a564b6f058bbc53c95d_2_690x480.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/0116885085ecb472d66e6a564b6f058bbc53c95d_2_1035x720.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/0116885085ecb472d66e6a564b6f058bbc53c95d.png 2x" data-dominant-color="37373A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1095×763 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The solution is to specify segmentation geometry using the DICOM image as source:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e00927c537fcfd689614d4683225ae47efc8e1.png" data-download-href="/uploads/short-url/2phDiQG25hQTr0LMUk5qwq3ZcI1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10e00927c537fcfd689614d4683225ae47efc8e1_2_689x409.png" alt="image" data-base62-sha1="2phDiQG25hQTr0LMUk5qwq3ZcI1" width="689" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10e00927c537fcfd689614d4683225ae47efc8e1_2_689x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10e00927c537fcfd689614d4683225ae47efc8e1_2_1033x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10e00927c537fcfd689614d4683225ae47efc8e1.png 2x" data-dominant-color="47484F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1299×770 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ve now <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/9996633bb5c64a5a3e50b0281b22d5c0ef4b9f3e">updated TotalSegmentator to do this step automatically</a>.</p>
<p>DICOM export takes 40 seconds and loading takes 50 seconds. This is tolerable but for comparison, when we save/load as nrrd then both take about 1 second.</p>

---

## Post #4 by @lassoan (2023-01-14 16:20 UTC)

<p>2 posts were split to a new topic: <a href="/t/improve-totalsegmentator-pre-segmentation-speed/27238">Improve TotalSegmentator pre-segmentation speed</a></p>

---

## Post #5 by @fedorov (2023-01-16 19:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="27229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably the reference volume was not set in the segmentation. I’ve tried to explain this in the message in the DICOM export dialog (see red text):</p>
</blockquote>
</aside>
<p>Andras, before the fix, it was not possible to get to that export dialog unless a dummy patient was created. The initial popup I showed in the initial message had only the option to cancel, or to create a dummy patient.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="27229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve now <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/9996633bb5c64a5a3e50b0281b22d5c0ef4b9f3e">updated TotalSegmentator to do this step automatically </a></p>
</blockquote>
</aside>
<p>Thank you, it is working now!</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="27229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>DICOM export takes 40 seconds and loading takes 50 seconds.</p>
</blockquote>
</aside>
<p>I am working on one improvement to dcmqi that I know will help reduce this time. For the record, there was not even an attempt to optimize DICOM SEG import/export, since for smaller number of segments this is not a practical issue. I don’t know how much I can improve this, but I will look into it.</p>

---

## Post #6 by @lassoan (2023-01-16 21:44 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="27229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am working on one improvement to dcmqi that I know will help reduce this time. For the record, there was not even an attempt to optimize DICOM SEG import/export, since for smaller number of segments this is not a practical issue. I don’t know how much I can improve this, but I will look into it.</p>
</blockquote>
</aside>
<p>Reading/writing hundreds of files have significant overhead, so probably dcmqi should have support for storing multiple segments in one 3D volume, and allow multiple 3D volumes for storing overlapping segments (so the segmentation file is 3D if all segments are non-overlapping; 4D if there are overlaps). We have implemented functions in Slicer for splitting/merging overlapping/non-overlapping segments that you might find useful for this.</p>
<p>We have found that even with using a single 3D file for storing all the segments, splitting them to separate volumes and process one by one is much slower. For example, when in Slicer we stored each segment as a separate volume, it took about 30 seconds to load the Brain Atlas. When we switched to storing all segments in the usual single 3D shared labelmap representation then loading time went down to a fraction of a second. I know that supporting this would require improving the DICOM standard, but I think it would worth it, not only because of the speed improvement but also because of simplicity and reduced memory need.</p>

---

## Post #7 by @fedorov (2023-01-25 16:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="27229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We have implemented functions in Slicer for splitting/merging overlapping/non-overlapping segments that you might find useful for this.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you help with pointers to those relevant functions in Slicer?</p>

---

## Post #8 by @fedorov (2023-01-25 16:59 UTC)

<p>I started working on adding that functionality in <a href="https://github.com/QIICR/dcmqi/pull/464" class="inline-onebox">Add support for saving segments in a single file by fedorov · Pull Request #464 · QIICR/dcmqi · GitHub</a></p>

---

## Post #9 by @lassoan (2023-01-25 20:31 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="27229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>can you help with pointers to those relevant functions in Slicer?</p>
</blockquote>
</aside>
<p>This file is a good starting point: <a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkSegmentationModifier.cxx">https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkSegmentationModifier.cxx</a></p>

---
