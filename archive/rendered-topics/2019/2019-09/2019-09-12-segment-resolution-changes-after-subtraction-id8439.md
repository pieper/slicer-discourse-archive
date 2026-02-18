# Segment resolution changes after subtraction

**Topic ID**: 8439
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/segment-resolution-changes-after-subtraction/8439

---

## Post #1 by @Netta_Z (2019-09-12 18:58 UTC)

<p>Thank you for the response.</p>
<p>I smoothed the model using the Median method and it did shorten the update time when using eraser tool to adjust segmentation, however I noticed the smoothing isn’t retained by the model when the following is performed:</p>
<ol>
<li>Import segmentation from obj file</li>
<li>Copy into existing model segmentation (which is smoothed)</li>
<li>Using logical operator, subtract the imported segmentation from existing model</li>
<li>The smoothed model becomes grainier when subtract operator completes its job</li>
<li>Each time the subtract operator is used, the model becomes grainier progressively<br>
However if the subtract operator takes a segment created from the editor tools(eg. paint) as the modifier, the model stays smooth. Any input on why this is happening? I have attached some screenshots of the segmentation before and after using subtract operator.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14a625741685530042d841f0ebc6b9b2533a3c12.png" alt="1" data-base62-sha1="2WFw0lPpK8aL1KN3BmwnsKGVNbc" width="338" height="132"></li>
</ol>

---

## Post #2 by @lassoan (2019-09-12 21:20 UTC)

<p>Can you save the scene as a .mrb file and share it via dropbox/onedrive/gdrive?</p>

---

## Post #3 by @Netta_Z (2019-09-13 14:37 UTC)

<p>I’ve attached the scene with the model here: <a href="https://drive.google.com/file/d/1Nlkp4hUTY_DZmVLv-lyatALaDx9D4yhQ/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1Nlkp4hUTY_DZmVLv-lyatALaDx9D4yhQ/view?usp=sharing</a>. There’s a green rod shaped tool that I use as the modifier segment, loaded from .obj. To use the logical operator you need to transform the modifier to intersect the bone model, then copy the modifier into the model segmentation.</p>
<p>After exploring the issue a little further, I noticed that saving the scene, restarting slicer, and loading the scene seemed to help. With those procedures done the subtract operator didn’t mess up the smoothing the first time you use it. In the same session without saving, if you transform and copy the imported modifier into the model segment a second time and use the subtract operator, the smoothness decreases. These are my observations on the nightly version.</p>
<p>Thanks so much for helping!</p>

---

## Post #4 by @Michael_Hardisty (2019-09-13 15:51 UTC)

<p>I wanted to clarify how to recreate the behaviour step by step.</p>
<ol>
<li>Load the scene CopySegmentBinaryOperator.mrb</li>
<li>Copy the Toggable Sphere Segment to the Spine Segmentation<br>
a. Go to the segmentations module<br>
b. Select the Spine Segmentation as the active segmentation<br>
c. Go to copy/move segments<br>
i.     Current segmentation select Segmentation Sphere<br>
ii.     Select Toggable Sphere<br>
iii.     Add the Toggable Sphere segment to the Spine Segmentation node by pressing &lt;+</li>
<li>Subtract the Toggable Sphere Segment from the Model Segment<br>
a.      Go to the Segment Editor module<br>
i.     Select Model as the active segment<br>
ii.     Select the Logical Operators effect<br>
iii.     Select Substract operation<br>
iv.     Select Toggable Sphere from Substract Segment<br>
v.     Hit Apply</li>
</ol>
<p>The problem is that the whole 3d surface visualized changes, rather than just where the segments intersect.  The segment becomes much less smooth.</p>

---

## Post #5 by @lassoan (2019-09-16 01:46 UTC)

<p>Thanks for the detailed report, I could reproduce and fix the issue (fix available in rev28498).</p>
<p>The problem was that the modifier segment had different geometry (origin, spacing) as the modified segment. The effect resampled the modified segment with the geometry of the modifier segment and you saw the effect of this resampling.</p>
<p>I’ve fixed the issue now in the latest Preview Release, but if you use different version then as a workaround you can avoid the error by using the same labelmap geometry in the modifier segment. For example, you can achieve this by importing the modifier segment directly from a model node.</p>

---

## Post #6 by @Michael_Hardisty (2019-09-19 17:13 UTC)

<p>Thanks Andras for fixing the issue!  I can confirm that the behaviour as described has been fixed…onto the next error but that’s for another thread.</p>

---
