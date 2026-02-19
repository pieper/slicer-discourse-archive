---
topic_id: 28214
title: "Perpendicular View Functionalities"
date: 2023-03-07
url: https://discourse.slicer.org/t/28214
---

# Perpendicular view functionalities

**Topic ID**: 28214
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/perpendicular-view-functionalities/28214

---

## Post #1 by @bserrano (2023-03-07 13:01 UTC)

<p>Hi all,</p>
<p>I am trying to segment coronary vessels. For this job I use the Endoscopy module, which builds perpendicular planes along a centerline. And I’m struggling with the following issues:</p>
<ol>
<li>
<p>I cannot modify the number of frames, even if the centerline a different number of points. Is it possible to get more frames?</p>
</li>
<li>
<p>If I use the paint tool in the perpendicular plane it acts differently if I click or if I drag with the same threshold. Why is that?</p>
</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98dd924990b81d2073ba924bd876aeea382dacfb.png" alt="imagen" data-base62-sha1="lOjhZdlgu0crLKWqNqvFpdGBKrx" width="162" height="164"></p>
<p>Drag:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7273d840a715cfef3fce3e6d49a56faa06b8adf5.png" alt="imagen" data-base62-sha1="gkuCVoxPC4YDGVrcU9YxHQo87Vb" width="136" height="145"><br>
Result:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ace1116e94a7a2047a1b21e532551b99193ef8e2.png" alt="imagen" data-base62-sha1="oFmkwGxHxfZ0gGQM1MwrK1cZOXo" width="122" height="111"></p>
<ol start="3">
<li>Tool feel between slices works fine if the slices are in axial but works poorly if they are painted in perpendicular view. How can I fix that?</li>
</ol>

---

## Post #2 by @chir.set (2023-03-07 17:26 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>segment coronary vessels</p>
</blockquote>
</aside>
<p>You may try ‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/GuidedArterySegmentation.md" rel="noopener nofollow ugc">Guided artery segmentation</a>’ in SlicerVMTK extension, that you can install using the ‘Extensions manager’.</p>
<p>The result always depends on the quality of the contrasted CT scan, how diseased the target vessel to segment is and how much you want to segment. In general, less is better.</p>

---

## Post #3 by @chir.set (2023-03-07 17:38 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>perpendicular planes along a centerline</p>
</blockquote>
</aside>
<p>You may also do that without segmenting.</p>
<p>'<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CrossSectionAnalysis.md" rel="noopener nofollow ugc">Cross-section analysis’</a> module is handy for that. It’s also in SlicerVMTK extension.</p>
<p>You should then use an ‘Open curve’ along the blood vessel. You may place the control points either at the best estimate of the center of the artery downstream, or on its surface (without spirals) such that the curve remains parallel to the artery’s axis.</p>

---

## Post #4 by @bserrano (2023-03-08 15:12 UTC)

<p>Hi, many thanks for the recommendation.</p>
<p>We discovered <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/QuickArterySegmentation.md" rel="noopener nofollow ugc">Quick artery segmentation</a> module, which seems to be very useful too. Is there more documentation about how to set the parameters and how they work?</p>

---

## Post #5 by @chir.set (2023-03-08 15:54 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="4" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Is there more documentation about how to set the parameters and how they work</p>
</blockquote>
</aside>
<p>No, the main page you pointed to is the only one.</p>
<p>The trick is to adapt the ‘Flood filling parameters’. Contrast in the arterial lumen is usually between 200 - 450 HU, and the default parameters are good enough.</p>
<p>If the intensity range is much higher, use a higher ‘Intensity tolerance’, and inversely. A mouse click is simulated at each control point. The intensity range given to the connectivity filter is the HU value at that point +/- the ‘Intensity tolerance’, i.e., “Find voxels that are connected with this intensity range”. This is the ‘Flood filling’ effect of the ‘Segment editor’ that is being remotely controlled.</p>
<p>The ‘Neighbourhood size’ parameter controls leakage. The higher it is, the less leakage occurs, with more processing time.</p>
<p>With good quality CT scans, it can save time. Please note that it targets short portions of arteries to study, like carotid/femoral bifurcations, first few centimeters of visceral arteries… Aorta to popliteal study cannot give good results, you should then do each step independently.</p>
<p>Lastly, very tight, pre-occlusive stenosis as we say, remains a challenge for segmentation, the more so as major calcifications complicate matters.</p>

---

## Post #6 by @bserrano (2023-03-09 16:38 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>The intensity range given to the connectivity filter</p>
</blockquote>
</aside>
<p>We’ve been testing the algorithm with some patients and it works pretty well. We wonder if there is a “border detection algorithm” or is just pointIntensity +/- intensity tolerance. How does quick artery segmentation work then?</p>
<p>What do you mean by “connectivity filter”?</p>
<p>Many thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @chir.set (2023-03-09 17:44 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="6" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>What do you mean by “connectivity filter”?</p>
</blockquote>
</aside>
<p>You may check this class : <a href="https://vtk.org/doc/nightly/html/classvtkImageThresholdConnectivity.html" rel="noopener nofollow ugc">vtkImageThresholdConnectivity</a>.</p>
<aside class="quote no-group" data-username="bserrano" data-post="6" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>is just pointIntensity +/- intensity tolerance</p>
</blockquote>
</aside>
<p>The details are <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/a7785ddc0c9e362eeeb3079bedb5ea18507b2d1e/SegmentEditorFloodFilling/SegmentEditorFloodFillingLib/SegmentEditorEffect.py#L191" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #8 by @lassoan (2023-03-10 22:11 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>You may check this class : <a href="https://vtk.org/doc/nightly/html/classvtkImageThresholdConnectivity.html">vtkImageThresholdConnectivity </a>.</p>
</blockquote>
</aside>
<p>This is available in Flood filling effect in Segment Editor (provided by SegmentEditorExtraEffects extension).</p>

---

## Post #9 by @chir.set (2023-03-10 22:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="28214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is available in Flood filling effect</p>
</blockquote>
</aside>
<p>Yes, ‘Flood filling’ is what I referenced above indeed, and from where I discovered this class.</p>

---
