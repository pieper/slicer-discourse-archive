---
topic_id: 3361
title: "Local Adaptive Thresolding"
date: 2018-07-03
url: https://discourse.slicer.org/t/3361
---

# Local - adaptive Thresolding

**Topic ID**: 3361
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/local-adaptive-thresolding/3361

---

## Post #1 by @mading (2018-07-03 13:18 UTC)

<p>Dear all,<br>
I’m using 3D slicer for wooden objects.<br>
I need to extract accurate surfaces, and I did not get good results with global thresolding approaches (I mean the same grey value for all the object).<br>
Spruce wood is very non-homogeneous, showing great variations between late and early wood.<br>
Dedicated packages such as VGStudio perform easily this task, but with a limited control on the algorithm.</p>
<p>Is there any tools in 3Dslicer that allows you to perform an adaptive thresold? This would help me very much.</p>
<p>Many thanks</p>

---

## Post #2 by @pieper (2018-07-03 14:10 UTC)

<p>If you provide a small sample dataset and illustration of the segmentation you wish to achieve we may be able to give better suggestions.</p>

---

## Post #3 by @mading (2018-07-03 20:47 UTC)

<p>Thanks Steve.<br>
What do you mean by small? A crop of around 50-100 Mb is OK? As an example I think is enough.<br>
Dataset from industrial tomography are on the order of 10 Gb.</p>

---

## Post #4 by @pieper (2018-07-03 22:16 UTC)

<p>Sure, whatever the smallest reasonable size that illustrates the issue would be fine.  You can’t attach it directly here, but if you post a link to dropbox/onedrive/googledrive etc here we should be able to give some suggestions.  It would also help to see some screenshots of what other applications threshold the data (plus maybe a brief overview of what you are trying to achieve by doing the segmentation).</p>

---

## Post #5 by @mading (2018-07-04 22:13 UTC)

<p>Thanks Peter,<br>
first of all I uploaded an mhd+raw files: <a href="https://www.mediafire.com/?dmv88mjng8m8w" class="inline-onebox" rel="noopener nofollow ugc">My Files</a></p>
<p>I would like to extract precise surfaces for reverse. This is not possible with global thresold: wood density varies a lot. You usually have at least a couple of materials peaks in the histogram.<br>
I’m looking for something that consider the local gradient rather than a single ISO50 gray value for all the volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e39a3e4e82b4f46f408f944146cc50cc407d3aa3.jpeg" data-download-href="/uploads/short-url/wtsQKaGJIoQ1CJ7DDd4AZWsn4PN.jpg?dl=1" title="10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e39a3e4e82b4f46f408f944146cc50cc407d3aa3_2_690x350.jpg" alt="10" data-base62-sha1="wtsQKaGJIoQ1CJ7DDd4AZWsn4PN" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e39a3e4e82b4f46f408f944146cc50cc407d3aa3_2_690x350.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e39a3e4e82b4f46f408f944146cc50cc407d3aa3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e39a3e4e82b4f46f408f944146cc50cc407d3aa3.jpeg 2x" data-dominant-color="F9FAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10</span><span class="informations">751×381 38.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>VGStudio Max uses its own proprietary algorithm:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c70ef76e2c89c1c52c4edba80bbcbdec46cfadd0.jpeg" data-download-href="/uploads/short-url/soX56aIBYAWXoBTOg6nNAcIR3ry.jpeg?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70ef76e2c89c1c52c4edba80bbcbdec46cfadd0_2_690x408.jpeg" alt="12" data-base62-sha1="soX56aIBYAWXoBTOg6nNAcIR3ry" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70ef76e2c89c1c52c4edba80bbcbdec46cfadd0_2_690x408.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70ef76e2c89c1c52c4edba80bbcbdec46cfadd0_2_1035x612.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c70ef76e2c89c1c52c4edba80bbcbdec46cfadd0_2_1380x816.jpeg 2x" data-dominant-color="D1D1D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">2111×1250 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It takes into account what happens locally, rather than using a global value for thresold:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f29c63bb51c2ffd76692cd55f124c65bf468f305.jpeg" data-download-href="/uploads/short-url/yCeBSzLykTN7vlvUxHmMwY0N5Fb.jpg?dl=1" title="11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f29c63bb51c2ffd76692cd55f124c65bf468f305_2_690x459.jpg" alt="11" data-base62-sha1="yCeBSzLykTN7vlvUxHmMwY0N5Fb" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f29c63bb51c2ffd76692cd55f124c65bf468f305_2_690x459.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f29c63bb51c2ffd76692cd55f124c65bf468f305_2_1035x688.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f29c63bb51c2ffd76692cd55f124c65bf468f305_2_1380x918.jpg 2x" data-dominant-color="A9A9A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11</span><span class="informations">1629×1086 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-07-05 02:44 UTC)

<p>Slicer’s Segment editor has several effects that determines segment boundary based on local gradient change (grow from seeds, watershed, fast marching).</p>
<p>For example, using Watershed effect (available in Segment editor after yo install SegmentEditorExtraEffects extension):</p>
<ul>
<li>create a segment with threshold range minimum-14000 (surely background region)</li>
<li>create a segment with threshold range 25000-maximum (surely object region)</li>
<li>select Watershed effect</li>
<li>set object scale to 0.5mm (to control size of small blobs that are allowed at the object boundary)</li>
<li>click Initialize, then Apply</li>
</ul>
<p>Seed segments for Watershed effect, created using global thresholding:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a396bfbc45a45b602b2a9312ef787013a015645c.png" data-download-href="/uploads/short-url/nlaNXHGw01mtrfoV5KmhhcwwFLm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a396bfbc45a45b602b2a9312ef787013a015645c.png" alt="image" data-base62-sha1="nlaNXHGw01mtrfoV5KmhhcwwFLm" width="505" height="500" data-dominant-color="8A8988"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">726×718 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Segmentation result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c43f18d40fc8e987af08ddfe71246a3cf2410916.jpeg" data-download-href="/uploads/short-url/s04LFyPuOoDFZJCQP3qJnhKjC8C.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43f18d40fc8e987af08ddfe71246a3cf2410916_2_690x351.jpg" alt="image" data-base62-sha1="s04LFyPuOoDFZJCQP3qJnhKjC8C" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43f18d40fc8e987af08ddfe71246a3cf2410916_2_690x351.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43f18d40fc8e987af08ddfe71246a3cf2410916_2_1035x526.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c43f18d40fc8e987af08ddfe71246a3cf2410916_2_1380x702.jpg 2x" data-dominant-color="8B8EA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1644×838 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e5d4062ad2d3290f128c27c1208585a2bcac9b.gif" data-download-href="/uploads/short-url/9oXrio76dzxFEecsRu3DB7J6nIn.gif?dl=1" title="SlicerCapture2"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e5d4062ad2d3290f128c27c1208585a2bcac9b_2_503x500.gif" alt="SlicerCapture2" data-base62-sha1="9oXrio76dzxFEecsRu3DB7J6nIn" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e5d4062ad2d3290f128c27c1208585a2bcac9b_2_503x500.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e5d4062ad2d3290f128c27c1208585a2bcac9b_2_754x750.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e5d4062ad2d3290f128c27c1208585a2bcac9b.gif 2x" data-dominant-color="9295C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerCapture2</span><span class="informations">820×814 1 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve found that simple global thresholding (e.g., with Otsu threshold preset in recent nightly builds) gives good results, but you may need to manually remove small internal islands or blobs at the boundary:</p>
<ul>
<li>use Logical operators effect to invert the segment</li>
<li>optionally use Smoothing effect’s Opening method to remove small extrusions (without changing the geometry at other places)</li>
<li>use Islands effect, remove small islands to remove internal blobs</li>
<li>use Logical operators effect to invert the segment back to its original form</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b263b6017d62907b67cfd6f472da60f16e2289f.png" data-download-href="/uploads/short-url/d0lmp2K3w0FKSoag6cNEracDtpl.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b263b6017d62907b67cfd6f472da60f16e2289f_2_690x359.png" alt="image" data-base62-sha1="d0lmp2K3w0FKSoag6cNEracDtpl" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b263b6017d62907b67cfd6f472da60f16e2289f_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b263b6017d62907b67cfd6f472da60f16e2289f_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b263b6017d62907b67cfd6f472da60f16e2289f_2_1380x718.png 2x" data-dominant-color="8C849C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1635×851 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Once you find a good segmentation workflow, you can write a script that performs all steps by a single click.</p>

---

## Post #7 by @mading (2018-07-07 07:21 UTC)

<p>Great!<br>
Sorry for late reply.<br>
Next week I will gave a try to this approach, it seems promising.<br>
For sure I’ll ask more practical questions, hope this thread is the right place for continuing the discussion.</p>
<p>Andras would you like to make the stl available  for comparing it to the results of other approaches?</p>
<p>Thanks again for prompt and high-quality reply.<br>
It’s a pleasure to be here.</p>

---

## Post #8 by @lassoan (2018-07-07 14:53 UTC)

<aside class="quote no-group" data-username="mading" data-post="7" data-topic="3361">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c89c15/48.png" class="avatar"> mading:</div>
<blockquote>
<p>Andras would you like to make the stl available for comparing it to the results of other approaches?</p>
</blockquote>
</aside>
<p>See scene files and an example export here: <a href="https://1drv.ms/f/s!Arm_AFxB9yqHtKxmKF5t18bQ3SfFOw">https://1drv.ms/f/s!Arm_AFxB9yqHtKxmKF5t18bQ3SfFOw</a><br>
You can adjust the boundary location by tuning threshold values. I’ve computed the STL file using 14000 and 25000 as described above. There are several other parameters you can adjust, such as Watershed object size, and smoothing factor used for generation of closed surface representation.</p>

---
