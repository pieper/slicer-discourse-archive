---
topic_id: 15691
title: "Cbct Noise Removal"
date: 2021-01-27
url: https://discourse.slicer.org/t/15691
---

# CBCT noise removal

**Topic ID**: 15691
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/cbct-noise-removal/15691

---

## Post #1 by @martig (2021-01-27 11:14 UTC)

<p>Hi,</p>
<p>I would like to remove noise from CBCT images before I import them to a surgery planning software that can only do simple thresholding and only accepts DICOM files as input.</p>
<p>I have read the various threads on these forums and googled the topic, but I have not really found a working solution. I have tried using the gradient anisotropic diffusion filter and unsharp mask, but the effect was barely noticeable.</p>
<p>Does anyone have a process they use that they would like to share?</p>

---

## Post #2 by @lassoan (2021-01-28 02:15 UTC)

<p>This is a very large topic. To narrow down it a little you would need to provide more information.</p>
<p>What kind of noise or artifacts you would like to address? Streak artifacts (due to dental filling, etc), partial volume effects (thin bones not discernible from soft tissues), low contrast to noise ratio (due to scattering, low dose, detector noise, etc)?</p>
<p>What is the surgical procedure(s) that you are interested in? What would you need to segment (teeth, bones,…)? What are the clinical requirements and constraints (accuracy, computation time, clinical expert’s time,…)?</p>
<p>Can you attach a few example images?</p>

---

## Post #3 by @martig (2021-02-01 08:31 UTC)

<p>Hi,</p>
<p>Thank you for asking clarification. I now see that my question was too general.<br>
In short I would like to make the CBCT scans look more like CT scans.<br>
So the issue is mostly about clearly differentiating bone and soft tissue, meaning low contrast to noise ratio.<br>
The streaks are not such a big issue.</p>
<p>The procedures include orthognatic and reconstructive surgeries. My main interest is to have good models of the bones for creating surgical guides. Also, sometimes it’s very difficult to tell if there’s really a hole in the bone or it just seems this way because of the low contrast to noise ratio.<br>
I would like to both save time and increase accuracy.</p>
<p>Here’s an example, the maxilla has some large holes that don’t really exist:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db9423646a73882393586f0d8aee56f8ed116464.jpeg" data-download-href="/uploads/short-url/vktWWKsXhF27Ntb4BUKSBX9eQ2o.jpeg?dl=1" title="pilt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db9423646a73882393586f0d8aee56f8ed116464_2_588x500.jpeg" alt="pilt" data-base62-sha1="vktWWKsXhF27Ntb4BUKSBX9eQ2o" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db9423646a73882393586f0d8aee56f8ed116464_2_588x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db9423646a73882393586f0d8aee56f8ed116464.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db9423646a73882393586f0d8aee56f8ed116464.jpeg 2x" data-dominant-color="5A5340"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pilt</span><span class="informations">738×627 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-02-01 15:41 UTC)

<p>CBCT uses a cone beam (as opposed to pencil beams on CT), which means that there is significant amount of scattered radiation getting into each detector pixel from surrounding regions. Therefore, CBCT will be always inherently worse in distinguishing soft tissues than CT. It is not just noise, but you actually have less information in a CBCT than in a CT, which cannot be undone by reducing noise. Although you cannot generate CT-quality images, it should be possible to create specialized image segmentation workflows, which can create the bone surface you need for surgical planning.</p>
<p>So far, what you have tried seem to be volume rendering, which is essentially global thresholding. It is the simplest possible segmentation method, which works well if you have perfect images, but you often need to use more sophisticated segmentation tools - available in Segment Editor module. For example, tools that rely on local intensity changes (for example, Grow from seeds effect) can pick up much subtle, local intensity variations. Or you can use semi-automatic segmentation tools that allow experts to manually delineate structures on a few slices and create a full 3D segmentation from that (for example, Fill between slices effect). If you often need to segment particular bone segments manually then you can develop an image pre-processing method specifically for that purpose (for example, we discussed on this forum several times how to extract thin orbital walls) and/or fill holes in segmentation (for example, using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">Wrap solidify</a> effect).</p>
<p>Overall, probably with a few days or weeks of experimenting with different segmentation tools, you should be able to come up with a workflow that gives you a good quality bone surface with 5-10 minutes of manual work, without any custom software development. You can probably reduce the manual effort to zero or near-zero with some custom Python scripting, that implements a combination of image pre-processing, automated segmentation, and segmentation post-processing.</p>

---

## Post #5 by @martig (2021-02-02 09:20 UTC)

<p>Thank you for a comprehensive answer.<br>
I have tried wrap solidify and it’s a very useful tool.<br>
I really haven’t had much success with filters, but I’ll keep experimenting.</p>
<p>The CMF surgery planning software only accepts data in the DICOM format.<br>
Can I export the segmentations back to the DICOM format from Slicer?<br>
The software performs global thresholding to extract the bones and soft tissue.</p>

---

## Post #6 by @lassoan (2021-02-02 13:47 UTC)

<aside class="quote no-group" data-username="martig" data-post="5" data-topic="15691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/martig/48/4516_2.png" class="avatar"> martig:</div>
<blockquote>
<p>The CMF surgery planning software only accepts data in the DICOM format.<br>
Can I export the segmentations back to the DICOM format from Slicer?<br>
The software performs global thresholding to extract the bones and soft tissue.</p>
</blockquote>
</aside>
<p>You can then use the segmentation for blank out a CT volume (e.g., set everything that is outside the segment to a very different voxel value from everything else) and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-files">export that CT to DICOM</a>.</p>

---

## Post #7 by @martig (2021-02-08 10:24 UTC)

<p>This is the result of global thresholding:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5f39563fc8175735f533c0ca0acef221d03115a.jpeg" data-download-href="/uploads/short-url/nG4ENiWMjLqSvEvuYjAvUTS47uq.jpeg?dl=1" title="pilt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f39563fc8175735f533c0ca0acef221d03115a_2_215x250.jpeg" alt="pilt" data-base62-sha1="nG4ENiWMjLqSvEvuYjAvUTS47uq" width="215" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f39563fc8175735f533c0ca0acef221d03115a_2_215x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f39563fc8175735f533c0ca0acef221d03115a_2_322x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5f39563fc8175735f533c0ca0acef221d03115a_2_430x500.jpeg 2x" data-dominant-color="A79B8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pilt</span><span class="informations">873×1013 335 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the result after applying the gradient anisotropic diffusion filter:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b85260af5c6a227ecaafd93c7430498aee8df22.jpeg" data-download-href="/uploads/short-url/flamfDPVtLTEFNERdEluFALz6H8.jpeg?dl=1" title="pilt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b85260af5c6a227ecaafd93c7430498aee8df22_2_203x250.jpeg" alt="pilt" data-base62-sha1="flamfDPVtLTEFNERdEluFALz6H8" width="203" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b85260af5c6a227ecaafd93c7430498aee8df22_2_203x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b85260af5c6a227ecaafd93c7430498aee8df22_2_304x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b85260af5c6a227ecaafd93c7430498aee8df22_2_406x500.jpeg 2x" data-dominant-color="728883"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pilt</span><span class="informations">828×1016 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It looks much cleaner. I used the following settings for the filter:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4f33108f8417385784bbcf029107b550682848b.png" alt="pilt" data-base62-sha1="s6iCq4yP0yzCzckz6ADSogrVNEL" width="244" height="97"></p>
<p>Do you have any ideas on how I could do the blanking while preserving both the bone and the skin?</p>

---

## Post #8 by @lassoan (2021-02-08 21:06 UTC)

<aside class="quote no-group" data-username="martig" data-post="7" data-topic="15691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/martig/48/4516_2.png" class="avatar"> martig:</div>
<blockquote>
<p>Do you have any ideas on how I could do the blanking while preserving both the bone and the skin?</p>
</blockquote>
</aside>
<p>You can segment the skin surface and after blanking out everything outside the bone segment with value=0 (corresponding to HU of soft tissues), you blank out everything outside the skin segment with value=-1000 (corresponding to air).</p>

---
