# Rotation of image using python cuts off part of image

**Topic ID**: 24310
**Date**: 2022-07-14
**URL**: https://discourse.slicer.org/t/rotation-of-image-using-python-cuts-off-part-of-image/24310

---

## Post #1 by @KateDelb (2022-07-14 12:08 UTC)

<p>I have written a little script that rotates an image based on a transform (.tfm) that I’ve obtained from the Slicer GUI:</p>
<pre><code class="lang-auto">def resample(image, transform):
    # Output image Origin, Spacing, Size, Direction are taken from the reference
    # image in this call to Resample
    reference_image = image
    interpolator = sitk.sitkCosineWindowedSinc
    default_value = 100.0
    return sitk.Resample(image, reference_image, transform,
                         interpolator, default_value)

fet_180 = resample(fet, rotation_180)
</code></pre>
<p>Works perfectly, except for the fact that the images get cut off after the rotation. Example (zoomed out for clarity:<br>
Before rotation:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/725b8df0694bfc425acb14498415b44df2794e1e.png" alt="image" data-base62-sha1="gjEAl6lWM3egTHIdhUbqZSYFUSO" width="304" height="336"></p>
<p>After Rotation:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/150d3c8816f0bee331dda7a9b4ea5dc096bfe0f7.png" alt="image" data-base62-sha1="30enVbVOc8xsMohhbUzo8QewHkj" width="278" height="301"></p>
<p>This doesn’t happen when rotating in the Slicer GUI itself, what can I do to fix this?</p>

---
