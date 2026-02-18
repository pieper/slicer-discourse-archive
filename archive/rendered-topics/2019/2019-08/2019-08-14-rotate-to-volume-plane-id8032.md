# Rotate to volume plane

**Topic ID**: 8032
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/rotate-to-volume-plane/8032

---

## Post #1 by @Leon (2019-08-14 19:08 UTC)

<p>Maybe someone has already asked this question before, but I could not find it in one of the topics on this forum.</p>
<p>I’ve noticed that sometimes when I load a serie of dicom’s that they are not always properly displayed in the viewports. What I mean is that they are rotated more or less, so I have to use the ‘Rotate to volume plane’ function to correct this. I try to make it a routine do check this first before doing anything else, but is there a specific reason why this happens and if yes, is it possible to automatically correct this at import?</p>

---

## Post #2 by @pieper (2019-08-14 19:32 UTC)

<p>Yes, slicer maintains patient space views rather than image space and, well, we consider this a feature not a bug, but I guess that depends on your specific use.</p>
<p>It would be possible to write a small script that observes changes in the scene and invokes the rotate method.</p>

---

## Post #3 by @Leon (2019-08-15 08:51 UTC)

<p>But the actual CT or MRI scanning is done in straight angles towards the apparatus itself, so why not display them like that in the viewports.</p>
<p>The first time I came across this is was when I painted over a view with threshold painting (for instance a stroke from left to right) and then one part (let’s say the right part) was painted in on the adjacent slice. First I thought that my segmentation was fucked up, so I started a new one, but then I discovered it was due to the fact that my slice wasn’t lying flat in my viewport.</p>
<p>Very confusing at first, but now I’m triggered to do a check first (although I sometimes forget <img src="https://emoji.discourse-cdn.com/twitter/face_with_hand_over_mouth.png?v=9" title=":face_with_hand_over_mouth:" class="emoji" alt=":face_with_hand_over_mouth:">).</p>

---

## Post #4 by @pieper (2019-08-15 11:52 UTC)

<aside class="quote no-group" data-username="Leon" data-post="3" data-topic="8032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>But the actual CT or MRI scanning is done in straight angles towards the apparatus itself</p>
</blockquote>
</aside>
<p>Well, often yes, but it’s also quite common to have multiparametric acquisitions at different angles in MR, and ultrasounds are very arbitrary.  But yes, displaying the slices in patient space is just a convention.</p>

---
