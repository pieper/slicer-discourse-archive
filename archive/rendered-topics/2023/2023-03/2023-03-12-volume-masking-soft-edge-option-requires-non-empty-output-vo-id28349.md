# Volume masking "soft edge" option requires non-empty output volume

**Topic ID**: 28349
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/volume-masking-soft-edge-option-requires-non-empty-output-volume/28349

---

## Post #1 by @chir.set (2023-03-12 13:42 UTC)

<p>This backtrace is obtained with ‘Mask volume’ effect while setting ‘Soft edge’ :</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/user/programs/Slicer/lib/Slicer-5.3/qt-scripted-modules/SegmentEditorEffects/SegmentEditorMaskVolumeEffect.py", line 323, in onApply
    SegmentEditorMaskVolumeEffect.maskVolumeWithSegment(segmentationNode, segmentID, operationMode, fillValues, inputVolume, outputVolume,
  File "/home/user/programs/Slicer/lib/Slicer-5.3/qt-scripted-modules/SegmentEditorEffects/SegmentEditorMaskVolumeEffect.py", line 435, in maskVolumeWithSegment
    outputArray = slicer.util.arrayFromVolume(outputVolumeNode)
  File "/home/user/programs/Slicer/bin/Python/slicer/util.py", line 1662, in arrayFromVolume
    nshape = tuple(reversed(volumeNode.GetImageData().GetDimensions()))
AttributeError: 'NoneType' object has no attribute 'GetDimensions'
</code></pre>
<p>To reproduce :</p>
<p>Start Slicer<br>
Load CTA-cardio<br>
Go to ‘Segment editor’<br>
Create a segment<br>
Paint at random<br>
Switch to ‘Mask volume’ effect<br>
Set ‘Soft edge’ parameter at 0.50<br>
Select ‘Fill inside’<br>
Apply</p>
<p>The ‘Wait’ mouse cursor runs for ever, a ‘Temporary volume mask’ volume is present.</p>
<p>It ‘Mask volume’ is applied without setting ‘Soft edge’, it completes normally. Subsequently, if ‘Soft edge’ is set to &gt; 0.0, it completes as expected.</p>

---

## Post #2 by @lassoan (2023-03-12 17:26 UTC)

<p>I cannot reproduce this issue.</p>
<p>Does it work well if you first run the effect without soft edge and then rerun with soft edge on the same output volume?</p>

---

## Post #3 by @chir.set (2023-03-12 17:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="28349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does it work well if you first run the effect without soft edge and then rerun with soft edge on the same output volume?</p>
</blockquote>
</aside>
<p>Yes, that’s the point.</p>
<p>A first run without ‘Soft edge’, and a next run with ‘Soft edge’ is OK.</p>
<p>A first run with ‘Soft edge’ hangs with the above description.</p>
<p>I’ll try again later on with my next build. It’s not a big issue, was just reporting.</p>
<p>P.S. : running on Linux, self built Slicer. Did not test yet with factory Slicer.</p>

---

## Post #4 by @lassoan (2023-03-12 22:17 UTC)

<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/ac14df2b1010de94c1f45b8b0049f689b14afe9e">made the effect more robust</a>, from tomorrow it should work now with any output volume.</p>

---

## Post #5 by @chir.set (2023-03-13 08:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="28349">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/ac14df2b1010de94c1f45b8b0049f689b14afe9e" rel="noopener nofollow ugc">made the effect more robust</a></p>
</blockquote>
</aside>
<p>Yep, now it works, thanks.</p>

---
