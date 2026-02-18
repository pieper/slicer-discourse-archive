# How to label segmented organs?

**Topic ID**: 5289
**Date**: 2019-01-06
**URL**: https://discourse.slicer.org/t/how-to-label-segmented-organs/5289

---

## Post #1 by @Mojtaba (2019-01-06 20:21 UTC)

<p>hi<br>
I want to calculate a dose absorption for some organs from PET and CT images. for this goal, I need to label segimented organs. which module can help me?<br>
thank you.</p>

---

## Post #2 by @lassoan (2019-01-06 21:15 UTC)

<p>You can segment (a.k.a. label, contour) images using Segment Editor module.</p>

---

## Post #3 by @Mojtaba (2019-01-07 09:13 UTC)

<p>hi again<br>
I require to produce a dat file for assessing dose by GATE.  an example of dat file:<br>
2<br>
1 1 kidney<br>
2 2 spleen<br>
I require to assess dose in these organs. in addition of dat file, GATE needs images.<br>
I don’t know how to produce this interfile.<br>
can you any guidance to me?<br>
Thank you.</p>

---

## Post #4 by @Alex_Vergara (2019-01-07 12:47 UTC)

<p>Gate can use MetaImages (mhd) images as long as they are uncompressed. you can save youir images in that way</p>

---
