---
topic_id: 28295
title: "Should I Resample On Z Axis If Forcing 2D Feature Extraction"
date: 2023-03-10
url: https://discourse.slicer.org/t/28295
---

# Should I resample on z-axis if forcing 2D feature extraction?

**Topic ID**: 28295
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/should-i-resample-on-z-axis-if-forcing-2d-feature-extraction/28295

---

## Post #1 by @fabio.b (2023-03-10 20:19 UTC)

<p>Dear all,<br>
I have a question about a problem I am facing.<br>
I am currently working on MRI images with a slice thickness which is either 2 mm (in some patients) or 3 mm (in some other patients). And I would like to extract 2D features.<br>
My question is:</p>
<ul>
<li>Should I resample the images on the z-axis in order to get a common thickness? (e.g. specifying “resampledPixelSpacing: [1, 1, 2.5]”).</li>
<li>Or should I not resample the z-axis? (e.g. specifying “resampledPixelSpacing: [1, 1, 0]”), therefore accepting the fact that the z dimension can differ from patient to patient?</li>
</ul>
<p>Thank you in advance!<br>
Fabio</p>

---

## Post #2 by @fabio.b (2023-03-15 09:50 UTC)

<p>Hi everyone!<br>
Is there any idea or suggestion?<br>
Thank you very very much!!<br>
Kind regards,<br>
Fabio</p>

---
