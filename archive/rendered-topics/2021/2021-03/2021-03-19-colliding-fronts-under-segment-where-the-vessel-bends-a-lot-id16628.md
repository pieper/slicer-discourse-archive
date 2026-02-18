# Colliding fronts under-segment where the vessel bends a lot

**Topic ID**: 16628
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/colliding-fronts-under-segment-where-the-vessel-bends-a-lot/16628

---

## Post #1 by @Dave_Fang (2021-03-19 05:02 UTC)

<p>hi， guys,<br>
I use colliding fronts to initialize the segementaion on 3D DSA of intracranial blood vessels.<br>
But I found there was serious under-seg where the vessel bends a lot, <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d99e8828675a24188d24771a6db77ebb27bf6dcf.jpeg" data-download-href="/uploads/short-url/v39gmZjorOWszc4ROt9MOZyI84n.jpeg?dl=1" title="under_seg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d99e8828675a24188d24771a6db77ebb27bf6dcf_2_452x499.jpeg" alt="under_seg" data-base62-sha1="v39gmZjorOWszc4ROt9MOZyI84n" width="452" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d99e8828675a24188d24771a6db77ebb27bf6dcf_2_452x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d99e8828675a24188d24771a6db77ebb27bf6dcf_2_678x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d99e8828675a24188d24771a6db77ebb27bf6dcf_2_904x998.jpeg 2x" data-dominant-color="6F6F7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">under_seg</span><span class="informations">1059×1171 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Anyone else know the solution to the problem? Thanks so much for your advice.</p>

---

## Post #2 by @lassoan (2021-03-19 05:31 UTC)

<p>If you have such perfect image quality then you can segment the vessel very easily using thresholding (or if you want to be very fancy then using Grows from seeds effect or Fast marching effect) in 3D Slicer’s Segment Editor.</p>

---

## Post #3 by @Dave_Fang (2021-03-20 14:43 UTC)

<p>hi, Lassoan<br>
Thank you for your reply.<br>
Yeah, DSA is much better than MRA or CTA in image quality. But I want to use the robust method to make seg results very robust and make results consistency,  while threshold or grows rely heavily on the threshold setting.<br>
Of course , I have tried fast marching on same data, it dose much better but it include all branches. I also want to use colliding fronts on MRA and CTA.<br>
I just want to know if it is resonable for the collding fronts has such under-seg result on the bending part of vessel even on so much better image quality. And  how to resolve?</p>
<p>Look forward to your reply, thank you!</p>

---

## Post #4 by @lassoan (2021-03-26 17:36 UTC)

<p>For me, colliding fronts algorithm performed very poorly (I could not get any useful result from it). However, I’m not sure that I used it optimally, or my images fulfilled all the prerequisites of the algorithm. I just switched to use a combination of tools in Segment Editor in 3D Slicer that provides good segmentation for all the cases.</p>

---

## Post #5 by @ckolluru (2024-02-01 21:30 UTC)

<p>I realize this is an old post, but what does your input (speed function) to the colliding fronts algorithm look like? I found similar issues when the speed varies significantly in the region of interest. Setting the speed to a constant value (1) seemed to work to a reasonable extent. You could also try rescaling your speed function to be within 0 and 1 and give it a try.</p>
<p>On a related note, when I run this colliding fronts filter, I see that the segmentation leaks slightly into branches that we are not interested in. Are there good ways to delineate lumen in vessels at the location of bifurcations? Or stop the colliding fronts output from leaking into branches? <a class="mention" href="/u/lantiga">@lantiga</a></p>

---

## Post #6 by @lassoan (2024-04-01 15:52 UTC)

<p>Classic segmentation methods in medical imaging have mostly become irrelevant. I would recommend to use a deep learning based fully automatic segmentation method instead. You may find a pre-trained model on the internet or you can train your own using MONAILabel, nnUNet, etc.</p>

---
