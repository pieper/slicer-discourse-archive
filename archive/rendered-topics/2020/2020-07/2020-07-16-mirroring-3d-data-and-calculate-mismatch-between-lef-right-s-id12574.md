---
topic_id: 12574
title: "Mirroring 3D Data And Calculate Mismatch Between Lef Right S"
date: 2020-07-16
url: https://discourse.slicer.org/t/12574
---

# Mirroring 3D-data and calculate mismatch between lef&right side

**Topic ID**: 12574
**Date**: 2020-07-16
**URL**: https://discourse.slicer.org/t/mirroring-3d-data-and-calculate-mismatch-between-lef-right-side/12574

---

## Post #1 by @Bernardo (2020-07-16 12:53 UTC)

<p>Hello<br>
I found out that it is possible to mirror 3D data of a CT scan, so that i.e. the right side matches the left side in uninjuried extremities. Is it also possible to calculate the mismatch between both sides (in percentage terms) in a selected area of the scan? For example, a patient with distal radius fracture on the right side, CT scan of both sides available (left side not injured): dislocation/malunion of the right side is xx %?<br>
Thanks for your help!</p>

---

## Post #2 by @lassoan (2020-07-16 13:43 UTC)

<p>You can use Surface toolbox module to mirror a model, then align using SlicerIGT extension’s Fiducial registration wizard module. You can compute mismatch (surface distance) using “ModelToModelDistance” extension.</p>
<p>If you have the corresponding CT image, then you can view differences in the images, too, by mirroring the volume using Transforms module (applying a transform to the volume where you change one of the 1.0 values in the diagonal to -1.0) and then apply the same transform as you applied to the segmented model.</p>

---

## Post #3 by @J_Deng (2020-09-06 02:18 UTC)

<p>Any possibility of showing a screen shot about mirroring images [or reversing a sequence]? I tried changing the numbers from 1 to -1, but the 3D view moved around instead of being mirrored. My particularly needs for this is because the original slices were converted in a reversed order, resulting in the left side of the body parts being displayed on the right, and vice versa. Many thanks.</p>

---

## Post #4 by @lassoan (2020-09-06 05:12 UTC)

<p>You might find Surface Toolbox module simpler to use. Create a new node for output, select Mirror, check the mirror axis, then click Apply.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d1997790d17f228d5001c9b142c33220037243b.jpeg" data-download-href="/uploads/short-url/dhBeyaKFmIIc7dzDS9I8FxJDY2n.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d1997790d17f228d5001c9b142c33220037243b_2_690x410.jpeg" alt="image" data-base62-sha1="dhBeyaKFmIIc7dzDS9I8FxJDY2n" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d1997790d17f228d5001c9b142c33220037243b_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d1997790d17f228d5001c9b142c33220037243b_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d1997790d17f228d5001c9b142c33220037243b_2_1380x820.jpeg 2x" data-dominant-color="6A6C73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2303×1371 434 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @J_Deng (2020-09-06 17:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cf5d11172973d2c0adfbda6eff324c634fe73f9.png" data-download-href="/uploads/short-url/k6ZvlJG86wOXmZHYIhb4eCG6v1f.png?dl=1" title="3d-slicer-mirror" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf5d11172973d2c0adfbda6eff324c634fe73f9_2_503x500.png" alt="3d-slicer-mirror" data-base62-sha1="k6ZvlJG86wOXmZHYIhb4eCG6v1f" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf5d11172973d2c0adfbda6eff324c634fe73f9_2_503x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cf5d11172973d2c0adfbda6eff324c634fe73f9_2_754x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cf5d11172973d2c0adfbda6eff324c634fe73f9.png 2x" data-dominant-color="B0ADB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d-slicer-mirror</span><span class="informations">962×956 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Many thanks, Andras, for prompt reply as usual.</p>
<p>Tried using the latest preview 4.11.0-2020-08-29 r29335 / 0311336 , after hitting Apply and it showed Done, it did not appear to have mirrored [or changed] anything on the screen [x, y, z all tried]. Also, in “Input model”, I could not type a name, but after “Create a new model as …” in the Output model, I could go back to choose Model_1.</p>
<p>Tried using formal release 4.10 … but because my segmentation was created on 4.11, I could not open it as it was displayed on 4.11 .</p>

---

## Post #6 by @lassoan (2020-09-06 17:19 UTC)

<p>Surface Toolbox module operates on model nodes. You need to export the segmentation node to model node by right-clicking on it in Data module.</p>

---

## Post #7 by @J_Deng (2020-09-06 18:14 UTC)

<p>Got you and succeeded. Thanks a lot.<br>
As you are so knowledgeable [and a bit off-the thread], could you redirect me to the latest progress in importing GE 4D ultrasound data either from its adult cardiac studies [E9 and E95] or from its fetal cardiac studies [E10]? Info about either direct import or indirect import via TomTec or EchoPac would greatly appreciated!</p>

---

## Post #8 by @lassoan (2020-09-06 18:27 UTC)

<p>4D ultrasound import from GE systems now works well, using <a href="https://github.com/SlicerHeart/SlicerHeart#open-image3d-api">Image3dAPI implemented in SlicerHeart extension</a>.</p>

---
