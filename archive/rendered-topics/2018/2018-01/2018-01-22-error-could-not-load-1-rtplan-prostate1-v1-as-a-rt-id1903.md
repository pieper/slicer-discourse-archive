---
topic_id: 1903
title: "Error Could Not Load 1 Rtplan Prostate1 V1 As A Rt"
date: 2018-01-22
url: https://discourse.slicer.org/t/1903
---

# Error : Could not load: 1: RTPLAN: Prostate1_v1 as a RT

**Topic ID**: 1903
**Date**: 2018-01-22
**URL**: https://discourse.slicer.org/t/error-could-not-load-1-rtplan-prostate1-v1-as-a-rt/1903

---

## Post #1 by @moosaviaskari (2018-01-22 17:46 UTC)

<p>Hello,</p>
<p>I have two questions.<br>
I am using Slicer 4.6.2, and the SlicerRT toolkit is installed as well. However, when I import a DICOM file and load it, I receive an error that says Could not load RTPLAN as a RT. <strong>How are we able to load RTPLAN in Slicer?</strong></p>
<p>Also, by using information in RTPLAN, such as the coordinates of catheters used in a brachytherapy prostate, I want to calculate the Hausdorff distance between the “dwell positions” on certain catheters and the rectum. I know that by suing SlicerRT–&gt;Segment Comparison, we are able to calculate Hausdorff distance metrics between different segments. However, is it possible to calculate Hausdorff distance between selected points (dwell positions) and a segment (rectum) ?</p>
<p>Thank you in advance</p>

---

## Post #2 by @gcsharp (2018-01-22 18:08 UTC)

<p>Hi Reza,</p>
<p>RTPLAN import was not available at all in 4.6.2, and does not support brachy plans even in the current version.  For your application, you probably can workaround this limitation using dcmdump and grep</p>
<p>Regarding your second question, what it sounds like you are wanting is not the Hausdorff distance between segments, but rather distance from a point to a segment.  This can be accomplished by creating a distance map to the segment, and then probing its value at the location of interest.</p>
<p>Greg</p>

---

## Post #3 by @lassoan (2018-01-22 18:27 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="2" data-topic="1903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>For your application, you probably can workaround this limitation using dcmdump and grep</p>
</blockquote>
</aside>
<p>If you have some experience in Python, then you could also implement a simple importer that parses data using pydicom (already bundled with Slicer) and create markup fiducial or model nodes from the dwell positions. Let us know if you were interested in working on this and we’ll help getting you started.</p>

---

## Post #4 by @moosaviaskari (2018-01-22 19:58 UTC)

<p>Hi Greg,</p>
<p>Thank you for your response. I appreciate your consideration.<br>
Could you please explain how the dcmdump and grep is done?</p>
<p>Also, regarding the second part, the distance between a point and a segment would be practical. How can we create a distance map in slicer?</p>

---

## Post #5 by @moosaviaskari (2018-01-22 19:59 UTC)

<p>Hello Andras,</p>
<p>Your help is greatly appreciated.<br>
Yes, I am interested in working on that. Could you please help me in that regard.</p>

---

## Post #6 by @gcsharp (2018-01-22 20:52 UTC)

<p>Hi Reza,</p>
<p>Sure.  You would need a unix shell of some sort, and dcmtk installed.  Then you do something like this:</p>
<p>dcmdump file.dcm | grep ControlPoint3DPosition | uniq | sed -e ‘s/[^<span class="chcklst-box fa fa-square-o fa-fw"></span><em>[//’ | sed -e 's/].</em>//’</p>
<p>Andras already answered the second question here.  <img src="https://emoji.discourse-cdn.com/twitter/smiling_face.png?v=12" title=":smiling_face:" class="emoji" alt=":smiling_face:" loading="lazy" width="20" height="20"></p>
<aside class="quote quote-modified" data-post="2" data-topic="1126">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/adjusting-and-saving-binary-labelmaps/1126/2">Adjusting and saving binary labelmaps</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    When you export to Segmentation to Labelmap in Segmentations module’s Export-import section, in the Advanced section you can set a Reference volume. Segments will be padded/resampled to have the same geometry as the Reference volume. 
Note that with numpy, SimpleITK, VTK, etc. libraries readily available in Slicer in Python, it’s hard to find anything that is worth sent to be computed in Matlab. 
For example, you have several distance map computation algorithms in SimpleITK that you can call dir…
  </blockquote>
</aside>

<p>Peace,<br>
Greg</p>

---

## Post #7 by @cpinter (2018-01-23 14:39 UTC)

<p>Hi Reza,</p>
<ol>
<li>
<p>Although Greg’s suggestion to dump the tags and use them directly sounds simpler, it is a one-time solution for a problem you may need very often, so it’s better to add the import feature.<br>
If you’re willing to spend some time with adding brachy plan support to SlicerRT, that would be really great! Many from the community would be happy to have this feature. And I’d be happy to help with the implementation, with giving you pointers about where to start and what to use, etc.</p>
</li>
<li>
<p>Distance maps can be calculated in the Simple Filters module by selecting the SignedMaurerDistanceMapImageFilter filter.</p>
</li>
</ol>

---
