# Combine several segmentation VOIs on z axis

**Topic ID**: 31875
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/combine-several-segmentation-vois-on-z-axis/31875

---

## Post #1 by @Windy (2023-09-25 02:39 UTC)

<p>I have a CT volume of 1500 x 1500 x 3000. To be able to segment them without crashing my laptop while seeing enough details, I follow the following pipeline.</p>
<ol>
<li>I have divided them into 3 VOIs along the z-axis, each VOI having 1500 x 1500 x 1000</li>
<li>Downsampled them to 1/2 resolution.</li>
<li>Segmented the features.</li>
</ol>
<p>Now, I need to combine these three VOIs one after the other and create a single stl for geometric morphometrics. Is there a way to do this within Slicer without using Python? If not, what would be the best way to do it in Python?</p>

---

## Post #2 by @muratmaga (2023-09-25 03:37 UTC)

<p>If you used Slicer to crop the VOIs, the segments should still preserve the correct spatial relationship.<br>
If that’s the case just export the segmentations as 3D models from each VOI, and then use the <code>merge models</code> module to make them into a single model.</p>
<p>if they spatial relationships are lost (e.g., you exported the VOIs from ImageJ individually), you might still be able to fix it by figuring out the offset manually, entering that value into the Image origin field of the volumes module, but it is likely going to be tedious.</p>

---

## Post #3 by @Windy (2023-09-26 01:08 UTC)

<p>Thank you for your answer. However, I have some further questions.</p>
<p>I had image slices. So I ended up manually putting them in separate folders as VOIs as my VOI selection is relatively straightforward. So this means I should go ahead with 2nd approach where I mention the offsets. Since it is the same resolution, if I have 1000 slices each, do I have to give only the z-axis offset <code>1001</code> or should it be <code>1001 x my_spacing_in_mm</code>? Also, how can I give an offset when combining models? The “Merge model” module only seems to have 2 input models and one output model.</p>

---

## Post #4 by @muratmaga (2023-09-26 01:15 UTC)

<aside class="quote no-group" data-username="Windy" data-post="3" data-topic="31875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/91b2a8/48.png" class="avatar"> Windy:</div>
<blockquote>
<p>So I ended up manually putting them in separate folders as VOIs as my VOI selection is relatively straightforward.</p>
</blockquote>
</aside>
<p>Please don’t do this in future. You are creating whole lot of unnecessary complications for your self. use the <code>ImageStacks</code>, import the full stack at the preview setting with correct original image spacing entered and use different ROIs to import different regions as separate volumes in full resolution. That way you don’t have to guess what the offsets should be.</p>
<p>the z-axis offset might 1000 or 1000 x spacing, it would dependent on what image spacing value you entered for these partial volumes (1x1x1mm or 0.014 as your earlier post).</p>

---

## Post #5 by @muratmaga (2023-09-26 01:17 UTC)

<aside class="quote no-group" data-username="Windy" data-post="3" data-topic="31875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/91b2a8/48.png" class="avatar"> Windy:</div>
<blockquote>
<p>The “Merge model” module only seems to have 2 input models and one output model.</p>
</blockquote>
</aside>
<p>For this you can use the merge models sequentially (i.e., merge model_1 and model_2 and then use the output of this to merge with model_3.</p>

---

## Post #8 by @Windy (2023-09-26 23:02 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="31875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>For this you can use the merge models sequentially (i.e., merge model_1 and model_2 and then use the output of this to merge with model_3.</p>
</blockquote>
</aside>
<p>I think I miscommunicated. I figured out this part. My question is, how do we give the offsets for a manually separated ROI since the “merge module” does not support entering the offsets as a parameter?</p>

---

## Post #9 by @Windy (2023-09-26 23:04 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="31875">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Please don’t do this in future. You are creating whole lot of unnecessary complications for your self. use the <code>ImageStacks</code>, import the full stack at the preview setting with correct original image spacing entered and use different ROIs to import different regions as separate volumes in full resolution. That way you don’t have to guess what the offsets should be.</p>
<p>the z-axis offset might 1000 or 1000 x spacing, it would dependent on what image spacing value you entered for these partial volumes (1x1x1mm or 0.014 as your earlier post).</p>
</blockquote>
</aside>
<p>Thank you, Murat. I have tried the approach you mentioned and done a test sample. However, after segmenting, I apply some smoothing to get a proper model. I think because of that, I am getting small gaps between the models when I combine them. Could you please advise me on how to handle this, either inside the slicer or in a mesh software like MeshLab (if you have prior experience with this kind of case)?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e99caae7e473e59aca9593808cde683b1b31d22.jpeg" data-download-href="/uploads/short-url/bdkJSlVEfPm6KRFNahjePPOqmpc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e99caae7e473e59aca9593808cde683b1b31d22_2_690x198.jpeg" alt="image" data-base62-sha1="bdkJSlVEfPm6KRFNahjePPOqmpc" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e99caae7e473e59aca9593808cde683b1b31d22_2_690x198.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e99caae7e473e59aca9593808cde683b1b31d22_2_1035x297.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e99caae7e473e59aca9593808cde683b1b31d22.jpeg 2x" data-dominant-color="A7A7B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×314 43.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @muratmaga (2023-09-26 23:12 UTC)

<p>You can apply the smoothing after you merge the model using the <code>surface toolbox</code>. If that doesnt fix, your offset is probably wrong.</p>

---
