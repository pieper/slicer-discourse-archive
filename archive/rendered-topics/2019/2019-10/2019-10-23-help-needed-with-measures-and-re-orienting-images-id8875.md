# Help needed with measures and re-orienting images

**Topic ID**: 8875
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/help-needed-with-measures-and-re-orienting-images/8875

---

## Post #1 by @Meli55a (2019-10-23 12:55 UTC)

<p>Hello, i am trying to use slicer to take measurements on CT scans of specific bones for research purposes, but im having a hard time figuring out a couple things, hoping you guys can help me.</p>
<p>I need to measure the bone from one edge of the cortex to the other along perpendicular lines. I would like to place these lines on a single slice (2D image) that is taken at a specific &amp; reproducible plane based on bone landmarks.</p>
<p>I saw the post on using a pre-written python code to get the plane on the “red” view but i am having a hard time figuring out how to get the measurements. Im not even sure if i should be using slicer for this. Ive been trying to figure this out for the last month and as i am from a medical background and have very little knowledge of coding, it has been a struggle. Any advice is greatly appreciated !<br>
Thank you!</p>

---

## Post #2 by @lassoan (2019-10-23 13:16 UTC)

<p>Can you provide an annotated picture of what you are trying to achieve?</p>

---

## Post #3 by @Meli55a (2019-10-23 18:10 UTC)

<p>Unfortunately, what we are measuring is confidential. My adviser isnt allowing me to post a drawing, but i can be more descriptive. Imagine a long horizontal bone like the cartoon bone you see with cartoon dogs. I select my slice plane by choosing the widest point of the fat part at one end, and the 3rd point being the little dimple between the 2 round tips at the other end. Once i have the slice that intersects those 3 points, i need to make multiple pairs of  lines that intersect at a 90 degree angle and measure the length of the lines that overlap with bone in the 2D picture</p>

---

## Post #4 by @lassoan (2019-10-23 18:19 UTC)

<p>Defining the slice plane should be easy, using this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials" rel="nofollow noopener">example in the script repository</a>.</p>
<p>Since it is not clear how you define those line pairs, I cannot give any specific advice on how to deal with those. You can place landmark points or line endpoints and you can add observers to them and update other markups based on these positions as shown in examples in the script repository.</p>

---
