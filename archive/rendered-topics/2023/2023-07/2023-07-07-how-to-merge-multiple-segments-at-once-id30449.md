# How to merge multiple segments at once

**Topic ID**: 30449
**Date**: 2023-07-07
**URL**: https://discourse.slicer.org/t/how-to-merge-multiple-segments-at-once/30449

---

## Post #1 by @Kitchen-Sinkk (2023-07-07 11:26 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0829fbfa2b13968d6d7d9b252b378739baae023c.jpeg" alt="slicer1" data-base62-sha1="1adLMuZeEAKkgiG0IJ9MPt8QGPW" width="537" height="387"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11215015765472f55927e53e7c81c3bf14b69b57.jpeg" data-download-href="/uploads/short-url/2rxulg2VXN7WetgqZvRaHd12uvZ.jpeg?dl=1" title="SLICERS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11215015765472f55927e53e7c81c3bf14b69b57_2_346x500.jpeg" alt="SLICERS" data-base62-sha1="2rxulg2VXN7WetgqZvRaHd12uvZ" width="346" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11215015765472f55927e53e7c81c3bf14b69b57_2_346x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11215015765472f55927e53e7c81c3bf14b69b57_2_519x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11215015765472f55927e53e7c81c3bf14b69b57.jpeg 2x" data-dominant-color="EAEDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SLICERS</span><span class="informations">529×764 87.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
as the images showed, I have mutiple segements. I can add them one by one through the “logic operators” functions. However, I like to merge or “add” them together at once. Are there any method to achieve this goal?</p>

---

## Post #2 by @lassoan (2023-07-08 04:09 UTC)

<p>I find that the easiest to merge many segments is:</p>
<ul>
<li>show all the segments that you want to add (hide those segments you don’t want to add)</li>
<li>select “Logical operators” effect</li>
<li>select “Operation” → “Fill”</li>
<li>uncheck “Bypass masking”</li>
<li>select “Masking” / “Editable area” → “Inside all visible segments”</li>
<li>click “Apply”</li>
</ul>

---

## Post #3 by @Kitchen-Sinkk (2023-07-12 01:28 UTC)

<p>It’s work! thank you very much!</p>

---

## Post #4 by @rbumm (2023-07-12 08:36 UTC)

<p>As this is such an important feature it would be nice to have a special entry or preset in the “Operation” dropdown like “Merge visible segments” which automates that recipe</p>

---

## Post #5 by @lassoan (2023-07-12 14:09 UTC)

<p>Would it be enough if the “Logical operators” effect allowed selection of multiple input segments?</p>

---

## Post #6 by @rbumm (2023-07-12 14:31 UTC)

<p>Probably yes, maybe also “Fill/Merge”?</p>

---

## Post #7 by @Deep_Learning (2023-10-02 15:47 UTC)

<p>Could you please clarify.<br>
I want to merge 4 segments.</p>
<p>Make the four segments visible.</p>
<ul>
<li>select “Logical operators” effect</li>
<li>select “Operation” → “Fill”</li>
<li>uncheck “Bypass masking”</li>
<li>select “Masking” / “Editable area” → “Inside all visible segments”</li>
</ul>
<p>%%%$$$   Now which segment should be selected before applying?</p>
<p>A new empty segment? Any one of the four segments…</p>
<p>No matter what I do, I end up with the whole volume segmented (A big box)</p>
<p><a href="https://discourse.slicer.org/u/lassoan"><br>
lassoan</a><a href="https://discourse.slicer.org/u/lassoan">Andras Lasso</a></p>
<p><a href="https://discourse.slicer.org/t/how-to-merge-multiple-segments-at-once/30449/2">Jul 8</a></p>
<p>I find that the easiest to merge many segments is:</p>
<ul>
<li>show all the segments that you want to add (hide those segments you don’t want to add)</li>
<li>select “Logical operators” effect</li>
<li>select “Operation” → “Fill”</li>
<li>uncheck “Bypass masking”</li>
<li>select “Masking” / “Editable area” → “Inside all visible segments”</li>
<li>click “Apply”</li>
</ul>

---

## Post #8 by @rbumm (2023-10-03 15:23 UTC)

<p>You should create a new segment → “combined”. Here is a short video showing the process:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87621985237ec8a8a2d30e9d65e0b200a4529169.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87621985237ec8a8a2d30e9d65e0b200a4529169.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87621985237ec8a8a2d30e9d65e0b200a4529169.mp4</a>
    </video>
  </div><p></p>
<p>Good luck.</p>

---

## Post #9 by @Deep_Learning (2023-10-04 12:02 UTC)

<p>[quote=“Deep_Learning, post:7, topic:30449”]</p>
<p>Thank you, I was missing the “allow overlap”.</p>
<p>Slicer 5.1:</p>
<ul>
<li>show all the segments that you want to add (hide those segments you don’t want to add)</li>
<li>select “Logical operators” effect</li>
<li>select “Operation” → “Fill”</li>
<li>create a new Segment and select it</li>
<li>uncheck “Bypass masking”</li>
<li>select “Masking” / “Editable area” → “Inside all visible segments”</li>
<li>select “Modify other Segments”→ “Allow Overlap"</li>
<li>click “Apply”</li>
</ul>

---

## Post #10 by @CS1 (2025-11-14 11:47 UTC)

<p>Sorry lassoan, got a silly question, what happen with the overlapped volume/area between the two merged segments? would they be calculated twice Thanks!</p>

---

## Post #11 by @cpinter (2025-11-14 11:48 UTC)

<p>No, the merged segment will have no knowledge about where the different regions came from. Any statistic about the merged segment will be strictly about the contained voxel data in the segment.</p>

---

## Post #12 by @CS1 (2025-11-18 12:04 UTC)

<p>Thank you! this is very helpful!</p>

---
