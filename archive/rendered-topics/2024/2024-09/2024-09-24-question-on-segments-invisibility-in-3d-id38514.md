# Question on segments invisibility in 3D

**Topic ID**: 38514
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/question-on-segments-invisibility-in-3d/38514

---

## Post #1 by @alientex (2024-09-24 11:54 UTC)

<p>Hello,</p>
<p>Suppose we have two segments, A and B, with their visibility turned on and “Show 3D” enabled. If I turn off the visibility of segment A, does Slicer unload any part of segment A from memory when it becomes invisible in the 3D view?</p>
<p>Moreover, does Slicer only load the parts of segments that have their visibility turned on for 3D?</p>

---

## Post #2 by @alientex (2024-09-24 12:19 UTC)

<p>BTW, this is an Occlusion culling technique that I am mentioning for rendering performance.</p>

---

## Post #3 by @lassoan (2024-09-24 12:26 UTC)

<p>What is the operation that you would like to make faster? Camera rotation, toggling visibility of individual segments, create closed surface representation, …?</p>

---

## Post #5 by @alientex (2024-09-25 09:26 UTC)

<p>The toggling visibility of individual segments, where enabling Show 3D should only create a closed surface representation of those segments that have visibility turned on in 3D.</p>
<p>I noticed the slicer creates a closed surface representation for all segments, regardless of their visibility, when enabling Show 3D.</p>
<p>This is what I was referring to regarding unloading surfaces of segments from 3D that do not have visibility.</p>

---

## Post #6 by @cpinter (2024-09-25 11:02 UTC)

<p>This sounds reasonable in order to save computation time on each update. However, it is currently not supported to have a different set of representations per segment, and it would be an unproportinonally large work to implement it well. Also the GUI would become super complex (see Representations section of the Segmentations module). I don’t personally think that this will happen in the near future unless you design and implement the change.</p>

---

## Post #7 by @lassoan (2024-09-25 12:44 UTC)

<p>An additional reason for always having the same representations for all segments is that 3D display is an important use of closed surface representations, but it is not the only use.</p>
<p>If you want to improve performance at the cost of increased complexity then you can move those segments into a different segmentation that you don’t want to compute closed surface representation for.</p>
<p>If you want to increase speed of creating closed surface representation, you can enable usage of surface nets algorithm.</p>

---

## Post #8 by @Roberto_Neto (2024-09-25 14:46 UTC)

<p>Hello everybody<br>
I segmented multiple structures and would like to export them to separate views. clicking and removing and adding as needed, in an app on the iPad<br>
Thank you in advance</p>

---

## Post #9 by @lassoan (2024-09-25 20:06 UTC)

<p>You can export the segmentation to glTF or OBJ format using <a href="https://github.com/PerkLab/SlicerOpenAnatomy">SlicerOpenAnatomy extension</a> and then view it in any web browser (on your computer, tablet, phone, etc.) in 3D. See detailed description of the steps <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/README.md">here</a>.</p>

---

## Post #10 by @Roberto_Neto (2024-09-25 21:05 UTC)

<p>Thank you very much for your kindness!!!</p>

---

## Post #11 by @alientex (2024-09-26 12:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="38514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to improve performance at the cost of increased complexity then you can move those segments into a different segmentation that you don’t want to compute closed surface representation for.</p>
</blockquote>
</aside>
<p>Thank you for the suggestion. I will definitely try it.</p>
<br>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="38514">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to increase speed of creating closed surface representation, you can enable usage of surface nets algorithm.</p>
</blockquote>
</aside>
<p>Yes, I have tried surface nets, and I noticed a sudden increase in performance.</p>

---
