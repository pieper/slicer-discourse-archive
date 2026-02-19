---
topic_id: 11715
title: "Error No Image Data In Input Volume 0"
date: 2020-05-26
url: https://discourse.slicer.org/t/11715
---

# Error: No image data in input volume #0

**Topic ID**: 11715
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/error-no-image-data-in-input-volume-0/11715

---

## Post #1 by @TomNB (2020-05-26 16:07 UTC)

<p>Hello,</p>
<p>I have CT images of the plastic water phantom loaded for orthovoltage dose calculation. The same images were used by my  colleagues last year. Surprisingly, I get this error <strong>Error: No image data in input volume <span class="hashtag">#0</span></strong> when I try to calculate the dose similar to  what my colleagues did.</p>
<p>Anyone aware of what might be the reason for this error.</p>
<p>Thank you,</p>
<p>Tom</p>

---

## Post #2 by @cpinter (2020-05-26 16:21 UTC)

<p>Based on the error message the selected reference image is invalid. Make sure you select it and that it is the right one.</p>

---
