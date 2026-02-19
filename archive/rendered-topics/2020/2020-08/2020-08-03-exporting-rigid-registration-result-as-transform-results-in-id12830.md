---
topic_id: 12830
title: "Exporting Rigid Registration Result As Transform Results In"
date: 2020-08-03
url: https://discourse.slicer.org/t/12830
---

# Exporting Rigid Registration result as Transform results in strange errors

**Topic ID**: 12830
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/exporting-rigid-registration-result-as-transform-results-in-strange-errors/12830

---

## Post #1 by @PfeifferMIcha (2020-08-03 14:36 UTC)

<p>Hi,</p>
<p>I rigidly registered two images using the Landmark-Based registration. I chose “Affine Registration” as the Registration Type and “Rigid” as Registration Mode. The resulting registration looks good, so I tried to export the transform for usage in other programs by choosing “save”.<br>
However, the resulting files (I tested both .txt and .mat) have a slightly different transformation matrix than what I get when I look at the transform in slicer (Right click on the transformation-&gt;Edit properties).</p>
<p>Slicer’s GUI shows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56d96c6ec0ec006974989492ab938ef6517676ad.png" alt="image" data-base62-sha1="coiTciZ5Dokdhw8Bx1JEfSzrynX" width="342" height="162"></p>
<p>In the text file, I have:</p>
<blockquote>
<p><span class="hashtag-raw">#Insight</span> Transform File V1.0<br>
<a class="hashtag-cooked" href="/tag/transform" data-type="tag" data-slug="transform" data-id="498"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>transform</span></a> 0<br>
Transform: AffineTransform_double_3_3<br>
Parameters: 0.9989776251379424 0.04090843080016693 -0.01924070589205142 -0.04089969593416781 0.9991628979972874 0.0008474303244814285 0.01925926650340259 -0.00005962491247667927 0.9998145213481452 -4.374452815811267 -95.00156325189849 424.48027296194584<br>
FixedParameters: 0 0 0</p>
</blockquote>
<p>I expect the first 9 parameters to be the rotation and the last three to be the translation. Some values are not the same (see for example the x-value of the translation which changes from -7 mm to -4 mm)</p>
<p>When applying the exported transform in blender or paraview (to the segmented meshes which I get from the original images) I thus get a small offset in position and rotation.</p>
<p>Tested with Slicer Version 4.8.0 r26489. Is this a bug, or am I interpreting the transform wrong in the other programs?</p>

---

## Post #2 by @lassoan (2020-08-03 14:41 UTC)

<p>What you describe is the correct behavior. The difference that you see compared to the transform in Slicer GUI is due to ITK storing resampling transform (“from parent” direction) between data sets are defined in LPS coordinate system. See explanation and conversions between different coordinate systems and directions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_files">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_files</a></p>

---

## Post #3 by @PfeifferMIcha (2020-08-11 15:25 UTC)

<p>Thank you, that was the issue! I was able to get the correct transformation into another program by loading the saved transform and using the python script under the link you posted to convert it.</p>
<p>Thanks a lot for the quick reply as well!</p>

---
