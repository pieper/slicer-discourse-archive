# Substract a 3d model from another model

**Topic ID**: 14216
**Date**: 2020-10-23
**URL**: https://discourse.slicer.org/t/substract-a-3d-model-from-another-model/14216

---

## Post #1 by @Christos_Tzerefos (2020-10-23 19:30 UTC)

<p>I have two 3d skull models of the same patient. I want to align them perfectly and create a model that would be their difference (skull defect).<br>
Is this possible?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04ef022bbac35c742ef6eea867e5c8a4bf88d8fb.jpeg" data-download-href="/uploads/short-url/HDYXneBJWkwflJaOIeU1MJOeKv.jpeg?dl=1" title="Inked12_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04ef022bbac35c742ef6eea867e5c8a4bf88d8fb_2_690x335.jpeg" alt="Inked12_LI" data-base62-sha1="HDYXneBJWkwflJaOIeU1MJOeKv" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04ef022bbac35c742ef6eea867e5c8a4bf88d8fb_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04ef022bbac35c742ef6eea867e5c8a4bf88d8fb_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/04ef022bbac35c742ef6eea867e5c8a4bf88d8fb_2_1380x670.jpeg 2x" data-dominant-color="B4B6D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Inked12_LI</span><span class="informations">1902×924 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bb5b04ab9fb55447a371009c0f14ba4d9518f41.jpeg" data-download-href="/uploads/short-url/3X89MEzYmbHQ1B1OZvmj215fykF.jpeg?dl=1" title="Inked123_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bb5b04ab9fb55447a371009c0f14ba4d9518f41_2_690x334.jpeg" alt="Inked123_LI" data-base62-sha1="3X89MEzYmbHQ1B1OZvmj215fykF" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bb5b04ab9fb55447a371009c0f14ba4d9518f41_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bb5b04ab9fb55447a371009c0f14ba4d9518f41_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bb5b04ab9fb55447a371009c0f14ba4d9518f41_2_1380x668.jpeg 2x" data-dominant-color="B2B3CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Inked123_LI</span><span class="informations">1904×922 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2020-10-23 19:35 UTC)

<p>Please do not post screen capture with PHI on them.</p>
<p>As for your question, you can use the logical operation in the segment editor.</p>

---

## Post #3 by @Christos_Tzerefos (2020-10-23 19:49 UTC)

<p>I edited the images. Thank you for noting it. As for the subtraction, the models are created from different ct scans and they are not aligned. I have reached this point. Is there any way to align them?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e7b5a6f926ce55f2b96ccf5459a34885a135087.png" data-download-href="/uploads/short-url/4lEBEkckiHEyoT9CHrI2BmxnIVN.png?dl=1" title="new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e7b5a6f926ce55f2b96ccf5459a34885a135087_2_690x333.png" alt="new" data-base62-sha1="4lEBEkckiHEyoT9CHrI2BmxnIVN" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e7b5a6f926ce55f2b96ccf5459a34885a135087_2_690x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e7b5a6f926ce55f2b96ccf5459a34885a135087_2_1035x499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e7b5a6f926ce55f2b96ccf5459a34885a135087_2_1380x666.png 2x" data-dominant-color="BBBDDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new</span><span class="informations">1905×920 99.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Christos_Tzerefos (2020-10-23 20:58 UTC)

<p>I tried to align them manually with transform. Is there an easier way?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f50dc780ee30d398b1454e89064c4cf2c1fa11b2.png" data-download-href="/uploads/short-url/yXQv8PDB6WZhYYZMXmhXuzdUN10.png?dl=1" title="new2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f50dc780ee30d398b1454e89064c4cf2c1fa11b2_2_690x339.png" alt="new2" data-base62-sha1="yXQv8PDB6WZhYYZMXmhXuzdUN10" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f50dc780ee30d398b1454e89064c4cf2c1fa11b2_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f50dc780ee30d398b1454e89064c4cf2c1fa11b2_2_1035x508.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f50dc780ee30d398b1454e89064c4cf2c1fa11b2_2_1380x678.png 2x" data-dominant-color="BFBED8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new2</span><span class="informations">1902×935 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2020-10-23 21:04 UTC)

<p>You can use the Fiducial Registration in SlicerIGT extension and use landmark sets across these to models to align them better than just using manual transforms.</p>
<p>I think there is a segment registration module that is built on Elastix that may help you. BUt I have no experience with that.</p>

---

## Post #6 by @lassoan (2020-10-24 14:47 UTC)

<p>Manual landmark-based registration that <a class="mention" href="/u/muratmaga">@muratmaga</a> recommended is a good approach that is guaranteed to work well for every case, and it as accurate as your point placement is.</p>
<p>If that does not work well for you for some reason then Slicer has many other registration methods. To narrow down the problem a bit we would need to know more about your constraints and requirements. How much time do you have for registration - few seconds, 1-2 minutes, 1-2 hours, or no specific time limit? How many image pairs you need to register - a few, dozens, or hundreds? How much error is tolerable - 0.1mm, about 1mm, or up to few mm?</p>

---

## Post #7 by @Christos_Tzerefos (2020-10-24 18:04 UTC)

<p>Let me explain to you want I want to do. I have a pair of CT images for every patient (around 100 patients, a number which may be doubled). I have one CT scan before the operation and one after the procedure. The CT scans are not aligned. The surgical operation is called decompressive craniectomy and consists of removing a large piece o f bone out of the skull. What I want to do is to calculate the area of this bone defect. This area is irregular and has a curvature.<br>
I think that there are three ways. The first one is to create a flat model without taking into account the curvature.<br>
The second one is to create a model by comparing it with the other healthy side of the skull, like building a mirror image. (in this case, only one ct scan will be needed. I have not tried this yet)<br>
The third is to compare the two CT scans and create the model with subtraction.  This method would be the most scientific of all.<br>
As you figured out, the problems are the alignment that affects significantly accuracy and the long time needed to create the final model.<br>
Also, I would like to know or calculate the extend of error because of the software itself. Finally, I need a balance between time and accuracy, but I would prefer a greater accuracy method.</p>
<p>Is there any way for better alignment? Is it better to align the raw data from CT scans and then create the model? Maybe a script with python making tests with alignment scenarios and finding out the best could be a solution? (I have experience with <a href="http://vb.net" rel="noopener nofollow ugc">vb.net</a>; I am a “noob” in terms of python, and I don’t know how easily this could be achieved)</p>
<p><strong>The model before the operation</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f0f07e3e4f98e33d4da27957d16a6f48a7bdc55.png" data-download-href="/uploads/short-url/mH67vQisC2tZLwZLGB0GqCjI5I9.png?dl=1" title="pre-op1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0f07e3e4f98e33d4da27957d16a6f48a7bdc55_2_517x252.png" alt="pre-op1" data-base62-sha1="mH67vQisC2tZLwZLGB0GqCjI5I9" width="517" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0f07e3e4f98e33d4da27957d16a6f48a7bdc55_2_517x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0f07e3e4f98e33d4da27957d16a6f48a7bdc55_2_775x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f0f07e3e4f98e33d4da27957d16a6f48a7bdc55_2_1034x504.png 2x" data-dominant-color="BCBFDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pre-op1</span><span class="informations">1626×792 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>The model after the operation</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed9bd3148c892a788f8f1f62fccc1cd10716502.png" data-download-href="/uploads/short-url/mFfWwXvI6Ww0WEbv1JID3H75MJQ.png?dl=1" title="Post-op" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed9bd3148c892a788f8f1f62fccc1cd10716502_2_517x216.png" alt="Post-op" data-base62-sha1="mFfWwXvI6Ww0WEbv1JID3H75MJQ" width="517" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed9bd3148c892a788f8f1f62fccc1cd10716502_2_517x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed9bd3148c892a788f8f1f62fccc1cd10716502_2_775x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed9bd3148c892a788f8f1f62fccc1cd10716502_2_1034x432.png 2x" data-dominant-color="BABBD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Post-op</span><span class="informations">1907×797 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>The alignment</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a45669bbf57f617d31473d41e64f50d01b595563.png" data-download-href="/uploads/short-url/nrNrxwk3zppUag5WKdX9Yk4RmPp.png?dl=1" title="alignement with fiducials" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45669bbf57f617d31473d41e64f50d01b595563_2_517x215.png" alt="alignement with fiducials" data-base62-sha1="nrNrxwk3zppUag5WKdX9Yk4RmPp" width="517" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45669bbf57f617d31473d41e64f50d01b595563_2_517x215.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45669bbf57f617d31473d41e64f50d01b595563_2_775x322.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45669bbf57f617d31473d41e64f50d01b595563_2_1034x430.png 2x" data-dominant-color="B5B8D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alignement with fiducials</span><span class="informations">1894×789 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>After subtraction</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/0615432d72bd2dc509b52de02550024d25550277.png" data-download-href="/uploads/short-url/ROpZUgXWmFLK7SddsHicd374W3.png?dl=1" title="after subtraction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0615432d72bd2dc509b52de02550024d25550277_2_517x257.png" alt="after subtraction" data-base62-sha1="ROpZUgXWmFLK7SddsHicd374W3" width="517" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0615432d72bd2dc509b52de02550024d25550277_2_517x257.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0615432d72bd2dc509b52de02550024d25550277_2_775x385.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/0615432d72bd2dc509b52de02550024d25550277_2_1034x514.png 2x" data-dominant-color="BCC0D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after subtraction</span><span class="informations">1580×786 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>The final bone piece</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32b2d035eddd1e620fdf2706b007e3a44f97dae8.png" data-download-href="/uploads/short-url/7euYIqAb8nSDVeG3Mx8xsFgqjNK.png?dl=1" title="The bone piece I want to calculate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b2d035eddd1e620fdf2706b007e3a44f97dae8_2_517x263.png" alt="The bone piece I want to calculate" data-base62-sha1="7euYIqAb8nSDVeG3Mx8xsFgqjNK" width="517" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b2d035eddd1e620fdf2706b007e3a44f97dae8_2_517x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b2d035eddd1e620fdf2706b007e3a44f97dae8_2_775x394.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b2d035eddd1e620fdf2706b007e3a44f97dae8_2_1034x526.png 2x" data-dominant-color="BEC2DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">The bone piece I want to calculate</span><span class="informations">1543×787 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-10-24 19:35 UTC)

<p>Based on what you describe the following will provide high enough accuracy and does not require any custom development, and can be completed in a few minutes per case (by practicing or Python-scripting the repetitive steps):</p>
<ul>
<li>Segment the skull on the pre-op and post-op image and export them to model nodes</li>
<li>Register the pre-op and post-op CT using Fiducial registration wizard module. Up to a few mm error is acceptable (since displacement of the cut by even as much as 5-10 millimeters, would probably cause just a few percent surface area measurement error). Probably 4-6 landmarks are enough, but they need to be distributed over the head (not just on the face, but on the posterior side, too). It is worth spending some time with experimenting with which landmarks work best. Choose the pre-op image as fixed and the post-op image as moving (so that you don’t need to manually apply the transform to other nodes).</li>
<li>Draw a closed contour of the craniotomy on the post-op image</li>
<li>Resample the closed contour to 30-40 points, constraining control points to post-op skull surface model (Markups module / Resample). This helps preserving the contour shape when we constrain the contour to the surface in the next step.</li>
<li>Constrain the closed contour to the pre-op skull surface model (Markups / Curve settings / Curve type -&gt; Shortest distance on surface, Model node -&gt; pre-op skull surface model).</li>
<li>Cut out a curved surface patch from the pre-op skull surface model using Dynamic modeler module (add Curve cut tool, choose Model -&gt; pre-op skull surface model, Curve -&gt; closed curve, inside model -&gt; new model), click Apply</li>
<li>Get surface area of cut-out surface patch from Models module Information section</li>
</ul>
<p>Once you confirmed on 5-10 patients that this workflow is good, you can automate it using Python scripting. Only the segmentation and landmark placements will need manual clicking, all the other steps can be done by a very simple, fully automatic processing script.</p>

---

## Post #9 by @Christos_Tzerefos (2020-10-25 20:40 UTC)

<p>Thank you for your answer. I used your method, and I created this model (1st image) . I think that it was quite accurate. However, to have greater accuracy, firstly, I have to practice align the models with the fiducials as good as I can (3rd image), and also, when I create the curve, be as presise I can.<br>
I also calcualted the area with the method I suggested at first.  (2nd image). It was more time consuming and underestimates the area.</p>
<p>In case I want to use this method in a scientific article how can I asses the issue of accuracy? How can I cite the software and the relevant modules and explain the method that the algorithm uses to calculate areas?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d60d230ff402888f23515886c26801ca95fa99.png" data-download-href="/uploads/short-url/mWOZSHCINfmJzrY7QysoRN4mjQ5.png?dl=1" title="new" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d60d230ff402888f23515886c26801ca95fa99_2_690x284.png" alt="new" data-base62-sha1="mWOZSHCINfmJzrY7QysoRN4mjQ5" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d60d230ff402888f23515886c26801ca95fa99_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d60d230ff402888f23515886c26801ca95fa99_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d60d230ff402888f23515886c26801ca95fa99_2_1380x568.png 2x" data-dominant-color="BCB5CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new</span><span class="informations">1899×784 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2770834f1843cee09b4d66fc3bf233ba0dc2b72.png" data-download-href="/uploads/short-url/rKjEz21NqO7zJQ6Vv58sFJd9twm.png?dl=1" title="new2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2770834f1843cee09b4d66fc3bf233ba0dc2b72_2_690x324.png" alt="new2" data-base62-sha1="rKjEz21NqO7zJQ6Vv58sFJd9twm" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2770834f1843cee09b4d66fc3bf233ba0dc2b72_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2770834f1843cee09b4d66fc3bf233ba0dc2b72_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2770834f1843cee09b4d66fc3bf233ba0dc2b72_2_1380x648.png 2x" data-dominant-color="ACAFCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">new2</span><span class="informations">1896×893 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2224e32f641e5f1f3eadf8f03f9416c74ff2c7b2.jpeg" data-download-href="/uploads/short-url/4S3gqyXMnqsEjugjZYb2SIUs9ge.jpeg?dl=1" title="two.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2224e32f641e5f1f3eadf8f03f9416c74ff2c7b2_2_640x500.jpeg" alt="two.PNG" data-base62-sha1="4S3gqyXMnqsEjugjZYb2SIUs9ge" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2224e32f641e5f1f3eadf8f03f9416c74ff2c7b2_2_640x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2224e32f641e5f1f3eadf8f03f9416c74ff2c7b2_2_960x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2224e32f641e5f1f3eadf8f03f9416c74ff2c7b2.jpeg 2x" data-dominant-color="9B87A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">two.PNG</span><span class="informations">964×752 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2020-10-25 22:26 UTC)

<p>If those are the estimates (~16,200mm2 and 15,700mm2), those differ about 3% in measurement, which doesn’t sound quite bad to me.</p>
<p>If you want to measure your accuracy, your best option is to do repeated measures. Meaning for every subject, you align your two meshes using landmarks, do your subtraction, and calculate the area of bone segment multiple times. From this, you can estimate the mean of the surface area for a subject and its standard error of mean. Most of this calculation can be done scripted, once you collected your sets of landmarks.</p>
<p>I am not sure if there is anything to cite for calculating surface area, since its simply a summation of areas of those tiny triangles. But you should cite the Slicer as a platform paper [1,2], as well as the suggested citation for SlicerIGT [3] and any other citations for the specific module(s) you are using.</p>
<p>[1] Fedorov, A., Beichel, R., Kalpathy-Cramer, J., Finet, J., Fillion-Robin, J.-C., Pujol, S., … Kikinis, R. (2012). 3D Slicer as an image computing platform for the Quantitative Imaging Network. <em>Magnetic Resonance Imaging</em> , <em>30</em> (9), 1323–1341. doi:<a href="https://doi.org/10.1016/j.mri.2012.05.001" rel="noopener nofollow ugc">10.1016/j.mri.2012.05.001</a></p>
<p>[2] Kikinis, R., Pieper, S. D., &amp; Vosburgh, K. G. (2014). 3D Slicer: A Platform for Subject-Specific Image Analysis, Visualization, and Clinical Support. In <em>Intraoperative Imaging and Image-Guided Therapy</em> (pp. 277–289). Springer, New York, NY. doi:<a href="https://doi.org/10.1007/978-1-4614-7657-3_19" rel="noopener nofollow ugc">10.1007/978-1-4614-7657-3_19</a></p>
<p>[3] Ungi, T., Lasso, A., &amp; Fichtinger, G. (2016). Open-source platforms for navigated image-guided interventions. <em>Medical Image Analysis</em> , <em>33</em> , 181–186. doi:<a href="https://doi.org/10.1016/j.media.2016.06.011" rel="noopener nofollow ugc">10.1016/j.media.2016.06.011</a></p>

---

## Post #11 by @tsehrhardt (2020-10-26 18:57 UTC)

<p>I feel like there should be a way to do this at the CT volume level, but I haven’t done it–to eliminate any errors in segmenting the models from 2 different CT scans.</p>
<p>Another option is Meshlab–it’s not a Boolean subtraction, but you can</p>
<ul>
<li>
<p>align the models with minimum 4 landmarks,</p>
</li>
<li>
<p>measure the distance between two meshes (like the Model to Model Distance module),</p>
</li>
<li>
<p>colorize the mapped model according to distance,</p>
</li>
<li>
<p>select the parts of the mesh according to distance and move them to another “layer”.</p>
</li>
</ul>
<p>I cut a hole in a skull and ran a mock-up. I don’t know if there is a way to use the Model to Model Distance values to “select” areas the way Meshlab does.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b1f4c595b1d1870adc7427d921164160d239d1.png" data-download-href="/uploads/short-url/cEDhLXH2akRJHsAGCXRJVaEJ54J.png?dl=1" title="2020-10-26_14-37-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b1f4c595b1d1870adc7427d921164160d239d1_2_690x458.png" alt="2020-10-26_14-37-49" data-base62-sha1="cEDhLXH2akRJHsAGCXRJVaEJ54J" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b1f4c595b1d1870adc7427d921164160d239d1_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b1f4c595b1d1870adc7427d921164160d239d1_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b1f4c595b1d1870adc7427d921164160d239d1.png 2x" data-dominant-color="927E45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-10-26_14-37-49</span><span class="informations">1149×763 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2020-10-26 19:06 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="11" data-topic="14216">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>I feel like there should be a way to do this at the CT volume level, but I haven’t done it–to eliminate any errors in segmenting the models from 2 different CT scans.</p>
</blockquote>
</aside>
<p>I agree that for things that you can directly see in the image, such as diameter or circumference of the craniotomy, bone thickness, etc. you are better off working directly with the volume. However, you need  segmentation if you want to get bone surface area.</p>
<p>There is no need for subtraction or Boolean operations, unless you need to measure bone volumes. The additional complexity with subtraction is that the two meshes are quite different (cropped differently, there are extra objects in one image that are not in the other, etc), so you would end up having to deal with many irrelevant differences.</p>
<p>The registration and segmentation-based workflow described above seems simple enough to me and should meet the clinical accuracy requirements.</p>

---
