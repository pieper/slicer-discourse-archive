# How to exclude area through thresholding?

**Topic ID**: 36703
**Date**: 2024-06-11
**URL**: https://discourse.slicer.org/t/how-to-exclude-area-through-thresholding/36703

---

## Post #1 by @kev1n (2024-06-11 16:19 UTC)

<p>Hi there,</p>
<p>I’m trying to segment out a CT w/ contrast of the L hip. I’m trying to use a threshold to segment just the bone but the contrast has the same intensity as the bone and I’m unable to effectively separate out the two. I was able to set the threshold to just include the contrast and I was wondering if there was a way to exclude this and paint over the bone or a way to inverse it? I’m still new to slicer and could use any tips or tricks! Thank you!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db9cfb01fae56886c7ef999f6a8419d87aa59635.png" alt="Screenshot 2024-06-11 103519" data-base62-sha1="vkMTv8koOnr0wEnrjfOtpkqtbNP" width="359" height="298"></p>

---

## Post #2 by @lassoan (2024-06-11 16:23 UTC)

<p>You can use tools in the Segment Editor to separate bones from contrasted vessels. Easiest is to use <code>Islands</code> effect, choose <code>Keep selected island</code> mode, and click on the component you want to keep. You can also remove islands using the same effect, or use <code>Scissors</code> effect, etc.</p>
<p>However, normally you don’t need to do any of these manually anymore. AI segmentation tools, such as <code>MONAI Auto3DSeg</code> and <code>TotalSegmentator</code> extensions in Slicer can segment all major bones and vessels fully automatically in a few minutes.</p>

---

## Post #3 by @kev1n (2024-06-11 17:36 UTC)

<p>Thank you for that. I have been trying out MONAI Auto3D and for some reason after I run it and hit apply- it doesn’t seem to be working. Does that software only work for the sample data it comes with?</p>

---

## Post #4 by @lassoan (2024-06-11 18:38 UTC)

<p>MONAI Auto3DSeg and TotalSegmentator are very robust and work well with any CT images.</p>

---
