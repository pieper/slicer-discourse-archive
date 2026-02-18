# Editable intensity range

**Topic ID**: 17845
**Date**: 2021-05-28
**URL**: https://discourse.slicer.org/t/editable-intensity-range/17845

---

## Post #1 by @H.Khasawneh (2021-05-28 19:09 UTC)

<p>I am trying to use the Editable intensity range option for editing  pre-existing segmentation masks to crop around our region of interest however it is not working  properly. We have attempted multiple ranges without success. The only thing that is currently working is going slice by slice to edit the mask which is time and energy consuming.<br>
Of note, we are using the newest version of slicer but have tried the previous one as well.</p>
<p>I’d appreciate any inputs or suggestions to solve this.</p>

---

## Post #2 by @lassoan (2021-05-28 21:11 UTC)

<p>Editable intensity range specifies what parts of the image you can edit. If you want to remove part of a mask that is in a specific intensity range then you can use Logical operators effect’s “Clear” method (with “Bypass masking” option disabled).</p>

---

## Post #3 by @Alex_Black (2021-06-05 13:02 UTC)

<p>Hey, <a class="mention" href="/u/lassoan">@lassoan</a> <a href="https://www.essayontime.com/services/essay.html" rel="noopener nofollow ugc">.</a> Can I use it for several ranges at once?</p>

---

## Post #4 by @lassoan (2021-06-05 13:29 UTC)

<p>Yes, you can mask with arbitrary combination of intensity ranges. For this, you first create a segment for each intensity range and fill out with thresholding, then combine them into one segment using Logical operators effect. You will select this for masking.</p>

---

## Post #5 by @Alex_Black (2021-06-10 11:00 UTC)

<p>Thanks! <a href="https://www.bestessaytips.com/review_essay.php" rel="noopener nofollow ugc"><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji only-emoji" alt=":grinning:"></a></p>

---
