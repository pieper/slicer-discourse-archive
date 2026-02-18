# Deformation automatically inverted after centering volume

**Topic ID**: 21597
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/deformation-automatically-inverted-after-centering-volume/21597

---

## Post #1 by @alan6690 (2022-01-24 13:18 UTC)

<p>I have deformably register two CT volumes using the SlicerElastix extension and save the deformation transformation. The output volume is well matched with the fixed volume after the deformation as the deformation also change the origin of the moving volume to be the same as the fixed volume.</p>
<p>However, when I later try to deform another volume using the saved transformation, the output volume is shifted away from its original position. If I center the volume after the transformation, the deformed volume would be inverted back as if the transformation has not been done. As a result, I can’t visually inspect the alignment between the deformed image and the fixed image as they can not be in the same field of view. I don’t really understand the reason behind. Should I manually change the origin of the moving volume as the same with the firxed volume? Or there is a way to center the deformed volume back to my field of view? It would be great if anyone can give me some advices. Thank you.</p>

---

## Post #2 by @muratmaga (2022-01-25 04:20 UTC)

<p>Unless your second moving volume is in the same space as your original moving volume that you used in the registration, there is no reason to assume that applying the resultant transformation will give you a reasonable result. That’s because registration provides a mapping between those two sets of spaces.</p>
<p>You can try to rigidly register your second moving volume to your first moving volume, and then  if you apply for transformation you should a better alignment.</p>
<p>I would not mess with randomly centering the volumes, that usually creates more headaches than it solves.</p>

---

## Post #3 by @alan6690 (2022-01-25 14:03 UTC)

<p>Thank you for your reply. I do think the first and second moving volume are in the same space if I have not misinterpreted what you mean. Let me provide more details of my situation.</p>
<p>I have a pair of CTs (Let them be A: moving volume, B: fixed volume). I saved the deformable transformation from A to B. Then for testing the transformation, I simply import a copy of A (let’s call it A2) into Slicer and carry out the transformation under Transform module using the saved transfomation. So the first and second volumes should be identical. The only difference I realize is that when I register A to B, the SlicerElastix Module also automatically change the origin of A to be the same as B. But when I do the second transformation on A2, this does not happen. So the volume  (A2) after the transformation is moved away from the original space and I cannot find a way to move it back without inverting the deformable registration I have done.</p>
<p>(I wish to use the saved transformation on another volume that is converted from A using a machine learning model. That’s why I need to test the reproducibiility of the saved transformation.)</p>

---

## Post #4 by @lassoan (2022-01-25 14:45 UTC)

<aside class="quote no-group" data-username="alan6690" data-post="3" data-topic="21597">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/bc79bd/48.png" class="avatar"> alan6690:</div>
<blockquote>
<p>But when I do the second transformation on A2, this does not happen.</p>
</blockquote>
</aside>
<p>Maybe what you don’t expect is that there is a difference between dynamically <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">apply</a> a transform and permanently <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden</a> a transform. You can do both in Slicer and the results are slightly different.</p>
<p>When you request an output volume from Elastix provides a volume that is resampled to the fixed volume’s geometry (the moving to fixed transform is hardened on the moving volume). If you choose to use a centering transform to a volume then that transform is just applied to the node (the volume node is not changed).</p>

---

## Post #5 by @alan6690 (2022-01-26 11:40 UTC)

<p>Thank for your reply.</p>
<p>I am actually looking for a way to display the transformed volume and the fixed volume in the same space. However, the transformed volume is always shifted far away from the original position after the transform. I cannot find a way to move it back without it turning back to the pre-transform state, even I have harden the wrap transform. Is there any method to put both volumes in the same space other than centering both volumes?</p>

---

## Post #6 by @lassoan (2022-01-27 02:41 UTC)

<p>First to need to harden whatever transform is already applied to the volume, and then apply the additional transform. If you don’t do this then the new transform replaces the precious transform.</p>
<p>Alternatively, you can apply the additional transform to the volume’s current transform (and not to the volume itself).</p>
<p>If these don’t help then probably we don’t understand what you want to achieve. It could help if you provide an overview diagram of your workflow and maybe also a few screenshots.</p>

---

## Post #7 by @muratmaga (2022-01-27 04:24 UTC)

<aside class="quote no-group" data-username="alan6690" data-post="5" data-topic="21597">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/bc79bd/48.png" class="avatar"> alan6690:</div>
<blockquote>
<p>I am actually looking for a way to display the transformed volume and the fixed volume in the same space. However, the transformed volume is always shifted far away from the original position after the transform.</p>
</blockquote>
</aside>
<p>Perhaps first try with some of the sample data Slicer provides. Screenshots below are from the sample data called DentalSurgery. It is clear that, as provided these two scans do not occupy the same physical space, even though they come from the same individual.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de1c382aca8910b28acca9fd96719b8fac97708a.jpeg" data-download-href="/uploads/short-url/vGSsprqSAwpvymwnKMjzQdkLIWC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de1c382aca8910b28acca9fd96719b8fac97708a_2_500x500.jpeg" alt="image" data-base62-sha1="vGSsprqSAwpvymwnKMjzQdkLIWC" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de1c382aca8910b28acca9fd96719b8fac97708a_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de1c382aca8910b28acca9fd96719b8fac97708a_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de1c382aca8910b28acca9fd96719b8fac97708a_2_1000x1000.jpeg 2x" data-dominant-color="3D3C3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1153×1153 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this case, a rigid registration of post-surgery (moving) to pre-surgery (fixed) is sufficient (I used the General Registration, but it shouldn’t matter which registration framework you use in the slicer). I chose to save the output of this registration as a linear transformation as opposed creating a new transformed output volume.  The only inconsistencies are due to surgical manipulation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35be551c8513f0c910cf431a10f7bdd4c17808f4.jpeg" data-download-href="/uploads/short-url/7Fr5Fce397CMeFn7GJLwc3MSN9i.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35be551c8513f0c910cf431a10f7bdd4c17808f4_2_572x499.jpeg" alt="image" data-base62-sha1="7Fr5Fce397CMeFn7GJLwc3MSN9i" width="572" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35be551c8513f0c910cf431a10f7bdd4c17808f4_2_572x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/35be551c8513f0c910cf431a10f7bdd4c17808f4_2_858x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35be551c8513f0c910cf431a10f7bdd4c17808f4.jpeg 2x" data-dominant-color="373634"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1117×976 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, if I had a third set of image that is exactly in the same space as the post-surgery scans, I can apply this transform to make it align it with my fixed image (pre-surgery).</p>
<p>You may want to try this first to understand how to work with transforms and registration, and then apply it to your data.</p>

---

## Post #8 by @alan6690 (2022-02-01 11:08 UTC)

<p>Thank you for all the help.</p>

---
