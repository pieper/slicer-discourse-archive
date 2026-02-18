# Rotating an image to align with the 2D projection of the 3d model

**Topic ID**: 22219
**Date**: 2022-02-28
**URL**: https://discourse.slicer.org/t/rotating-an-image-to-align-with-the-2d-projection-of-the-3d-model/22219

---

## Post #1 by @Hitesh_Ganjoo (2022-02-28 17:16 UTC)

<p>Hi All,</p>
<p>I want to rotate a slice view such that the projection of a model in the 2d views is always in the specific orientation(e.g. vertical US probe in the attached image). The 3d model is controlled by several transformations and I simply want to generate the 2d slices based on the normal to the model(lets say z axis) and such that the slice view always appears to have the 2d projection vertical.</p>
<p>I wish to do this in a C++ based module preferably and not in python.  How can I achieve this?</p>
<p>Thanks in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80a5a7385773e0c653b6f9bf955e69691a32b58c.png" data-download-href="/uploads/short-url/im41E89ewka0JQ4ZazQSS9Ke2vO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a5a7385773e0c653b6f9bf955e69691a32b58c_2_690x339.png" alt="image" data-base62-sha1="im41E89ewka0JQ4ZazQSS9Ke2vO" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a5a7385773e0c653b6f9bf955e69691a32b58c_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a5a7385773e0c653b6f9bf955e69691a32b58c_2_1035x508.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80a5a7385773e0c653b6f9bf955e69691a32b58c_2_1380x678.png 2x" data-dominant-color="4E4F4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×944 90.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2022-02-28 18:19 UTC)

<p>Apply a transform WorldToUsProbeModel to the model and the slice. If you want it to look vertical you just need to concatenate a transform to rotate your model (if your model frame default orientation is similar to world’s one)</p>

---

## Post #3 by @Hitesh_Ganjoo (2022-02-28 19:09 UTC)

<p>Thanks, but I dont want to apply a transform to the model and the probe since it will change the slice data itself. I am getting the slice data based on the specific position of the probe(a subset of the existing ultrasound data at that position). Is there a way I can simple rotate the slice view without applying the transform? Hope am able to explain the situation…</p>

---

## Post #4 by @mau_igna_06 (2022-02-28 19:55 UTC)

<p>If your problem is transforming the model because that will change the slicing, just clone the model, apply to it only the rotation transform, and to the slice view apply the transform I told you earlier. I think that should work. The only way you can move a plane (the sliceView) on the 3D View that I know of is by using a transform.</p>

---
