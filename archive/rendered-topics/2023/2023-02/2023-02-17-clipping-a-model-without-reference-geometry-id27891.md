# Clipping a model without reference geometry

**Topic ID**: 27891
**Date**: 2023-02-17
**URL**: https://discourse.slicer.org/t/clipping-a-model-without-reference-geometry/27891

---

## Post #1 by @DeepaKrishnaswamy (2023-02-17 23:54 UTC)

<p>Hi,</p>
<p>I have a set of STL files that I would like to clip. I’m in the process of trying to use the clipping planes within Models, and also the Dynamic Modeler under Surface Models. However, I do not have the underlying MR data or information about the reference geometry. Is it still possible to use these methods without the underlying data? If not, are there other methods that would be appropriate?</p>
<p>Thank you,</p>
<p>Deepa</p>

---

## Post #2 by @DeepaKrishnaswamy (2023-02-18 00:46 UTC)

<p>I think I figured out how to clip the model by converting to a segmentation node and then to a binary label map, and then using the clipping planes for the model. But when I go to save the clipped model, only the original one is saved. How do I save out the edited one?</p>
<p>Thanks!</p>

---

## Post #3 by @tsehrhardt (2023-02-18 12:47 UTC)

<p>You can install the EasyClip module and clip a 3D model without a reference volume. Even without the volume, you can use the sliders in the 3 views to set the coordinates or move the cutting plane.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8126c196391a285c87f1a67182cdaaf9001c1ac3.jpeg" data-download-href="/uploads/short-url/iqwCXNF6k4x87bYrDc5nHZIePgD.jpeg?dl=1" title="2023-02-18_7-44-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8126c196391a285c87f1a67182cdaaf9001c1ac3_2_690x377.jpeg" alt="2023-02-18_7-44-16" data-base62-sha1="iqwCXNF6k4x87bYrDc5nHZIePgD" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8126c196391a285c87f1a67182cdaaf9001c1ac3_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8126c196391a285c87f1a67182cdaaf9001c1ac3_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8126c196391a285c87f1a67182cdaaf9001c1ac3_2_1380x754.jpeg 2x" data-dominant-color="8D8D97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_7-44-16</span><span class="informations">1920×1050 87.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @tsehrhardt (2023-02-18 12:49 UTC)

<p>You can also use Dynamic Modeler without a reference volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8424d6b097764ec65a12b1f05be947a9dab1fc9b.jpeg" data-download-href="/uploads/short-url/iQZX3quohfPhSo5S98iHfphtfth.jpeg?dl=1" title="2023-02-18_7-48-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8424d6b097764ec65a12b1f05be947a9dab1fc9b_2_690x377.jpeg" alt="2023-02-18_7-48-00" data-base62-sha1="iQZX3quohfPhSo5S98iHfphtfth" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8424d6b097764ec65a12b1f05be947a9dab1fc9b_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8424d6b097764ec65a12b1f05be947a9dab1fc9b_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8424d6b097764ec65a12b1f05be947a9dab1fc9b_2_1380x754.jpeg 2x" data-dominant-color="82838D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_7-48-00</span><span class="informations">1920×1050 80.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7be8bb7e4ab5515448db79770f3d08a925cf82b1.jpeg" data-download-href="/uploads/short-url/hG9m3oTEGsRATsTQH3TDLXgg5SF.jpeg?dl=1" title="2023-02-18_7-48-30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be8bb7e4ab5515448db79770f3d08a925cf82b1_2_690x377.jpeg" alt="2023-02-18_7-48-30" data-base62-sha1="hG9m3oTEGsRATsTQH3TDLXgg5SF" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be8bb7e4ab5515448db79770f3d08a925cf82b1_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be8bb7e4ab5515448db79770f3d08a925cf82b1_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7be8bb7e4ab5515448db79770f3d08a925cf82b1_2_1380x754.jpeg 2x" data-dominant-color="818290"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_7-48-30</span><span class="informations">1920×1050 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @slicer365 (2023-02-20 00:11 UTC)

<p>I think this way can only be used for special plane.</p>
<p>Is there a way to cut the model along any curve created by mouse?</p>
<p>Way like the scissors in segmentEditor，of course, I dont want to import the model to a segmentation. It will change the primary shape.</p>

---

## Post #6 by @tsehrhardt (2023-02-20 14:54 UTC)

<p>Yes there is a curve option–the little scissors button right next to the plane cut button in Dynamic Modeler. You can define an open or closed curve in Markups, then go back to Dynamic Modeler and select the “Curve Cut” button, then call up the curve you created in Markups.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/756f92aaf5bf9c30183dbe1fef12324c30b2ca58.jpeg" data-download-href="/uploads/short-url/gKSUi3CzLKhkwRBbwKyYPV16mPC.jpeg?dl=1" title="2023-02-20_9-46-18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756f92aaf5bf9c30183dbe1fef12324c30b2ca58_2_690x377.jpeg" alt="2023-02-20_9-46-18" data-base62-sha1="gKSUi3CzLKhkwRBbwKyYPV16mPC" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756f92aaf5bf9c30183dbe1fef12324c30b2ca58_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756f92aaf5bf9c30183dbe1fef12324c30b2ca58_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/756f92aaf5bf9c30183dbe1fef12324c30b2ca58_2_1380x754.jpeg 2x" data-dominant-color="A0A3B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-20_9-46-18</span><span class="informations">1920×1050 95.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/967543dccfe829eb7020654180e5d1df97f996ac.jpeg" data-download-href="/uploads/short-url/lt0RjiGa4tKew8MEusryfWFFaUI.jpeg?dl=1" title="2023-02-20_9-47-07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967543dccfe829eb7020654180e5d1df97f996ac_2_690x377.jpeg" alt="2023-02-20_9-47-07" data-base62-sha1="lt0RjiGa4tKew8MEusryfWFFaUI" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967543dccfe829eb7020654180e5d1df97f996ac_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967543dccfe829eb7020654180e5d1df97f996ac_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967543dccfe829eb7020654180e5d1df97f996ac_2_1380x754.jpeg 2x" data-dominant-color="A3A4B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-20_9-47-07</span><span class="informations">1920×1050 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Provide names if you want for the parts that will be generated. Click Apply then go to Models and see your parts. I just made a random curve so you can see what it does.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ef84e8776cd49d26323ffd5e72ced355354838b.jpeg" data-download-href="/uploads/short-url/4pYjLMo4tCurVxkwAL2vR6uEif1.jpeg?dl=1" title="2023-02-20_9-47-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ef84e8776cd49d26323ffd5e72ced355354838b_2_690x377.jpeg" alt="2023-02-20_9-47-39" data-base62-sha1="4pYjLMo4tCurVxkwAL2vR6uEif1" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ef84e8776cd49d26323ffd5e72ced355354838b_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ef84e8776cd49d26323ffd5e72ced355354838b_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1ef84e8776cd49d26323ffd5e72ced355354838b_2_1380x754.jpeg 2x" data-dominant-color="A2A3B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-20_9-47-39</span><span class="informations">1920×1050 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @slicer365 (2023-02-20 23:33 UTC)

<p>It is a good idea, thank you!</p>

---
