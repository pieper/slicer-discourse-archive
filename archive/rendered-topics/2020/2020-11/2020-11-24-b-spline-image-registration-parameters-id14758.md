---
topic_id: 14758
title: "B Spline Image Registration Parameters"
date: 2020-11-24
url: https://discourse.slicer.org/t/14758
---

# B-spline image registration parameters

**Topic ID**: 14758
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/b-spline-image-registration-parameters/14758

---

## Post #1 by @marianaslicer (2020-11-24 16:36 UTC)

<p>Hi everyone,</p>
<p>I’m using the latest nightly version and I want to register two images from a virtual phantom:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dcf655daf998df3416840c0f214bc0b85538765.png" alt="image" data-base62-sha1="4fIbO379lpEPXUwc2g30OL8gXfT" width="185" height="137"></p>
<p>Since I will need the B-spline image registration algorithm to further register patient data, I need to apply this algorithm for this data as well. However, the default parameters do not align the images. I tried to change the parameters in a trial error process without success. Could you give some guidance on the suitable parameters to register these images?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2020-11-24 18:54 UTC)

<p>Intensity-based image registration methods requires the image to have some texture.</p>
<p>If you want to register binary images like this then you can use distance-map-based methods, such as Segment Registration (you need to create segments from those blobs by thresholding).</p>
<p>If you can generate more realistic images (with proper texture and intensity variations) then I would recommend to use SlicerElastix extension, as it usually does not require any parameter tuning.</p>

---

## Post #3 by @lassoan (2020-11-25 20:30 UTC)

<p>A post was split to a new topic: <a href="/t/export-multiple-series-into-same-study/14774">Export multiple series into same study</a></p>

---
