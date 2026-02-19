---
topic_id: 24681
title: "Unexpected Results From Training New Model In Monai Label"
date: 2022-08-08
url: https://discourse.slicer.org/t/24681
---

# Unexpected results from training new model in Monai Label

**Topic ID**: 24681
**Date**: 2022-08-08
**URL**: https://discourse.slicer.org/t/unexpected-results-from-training-new-model-in-monai-label/24681

---

## Post #1 by @mahranahm (2022-08-08 16:27 UTC)

<p>Hi 3D slicer community,</p>
<p>We are working to train a new model to segment the heart. We have 6 pre-labelled scans which I am using for the initial training. I kept all the parameters on default except increasing the max_epoch to 1000. I am using a cloud GPU for the server (A100 (40 GB), 30 VCPUs, 200 GiB RAM, 512 GiB SSD) and SSH with port forwarding to my local 3Dslicer 5.0.3 r30893. I added the correct labels to the segmentation.py and turned the pre.trained model to “false”. My first model didn’t include a background label but however in my second run I included it but with no better results.</p>
<p>Here is what autosegmentation of a validation set looks like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a03c191c7cf6d21de312db5be99c133b27576ddc.jpeg" data-download-href="/uploads/short-url/mRv9BccjcgH1M7z2qbpe1C5oPBa.jpeg?dl=1" title="Screen Shot 2022-08-05 at 5.14.16 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03c191c7cf6d21de312db5be99c133b27576ddc_2_690x425.jpeg" alt="Screen Shot 2022-08-05 at 5.14.16 PM" data-base62-sha1="mRv9BccjcgH1M7z2qbpe1C5oPBa" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03c191c7cf6d21de312db5be99c133b27576ddc_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03c191c7cf6d21de312db5be99c133b27576ddc_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a03c191c7cf6d21de312db5be99c133b27576ddc_2_1380x850.jpeg 2x" data-dominant-color="5E5D69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-05 at 5.14.16 PM</span><span class="informations">1920×1183 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is a the labelled segmentations found in the (labels/final) folder.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a6207188ebfb880329294f0aa622cbde2c25c21.jpeg" data-download-href="/uploads/short-url/m1Jyl46aAInigpOmatRu8GnpRg5.jpeg?dl=1" title="Screen Shot 2022-08-08 at 12.00.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6207188ebfb880329294f0aa622cbde2c25c21_2_690x460.jpeg" alt="Screen Shot 2022-08-08 at 12.00.31 PM" data-base62-sha1="m1Jyl46aAInigpOmatRu8GnpRg5" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6207188ebfb880329294f0aa622cbde2c25c21_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6207188ebfb880329294f0aa622cbde2c25c21_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a6207188ebfb880329294f0aa622cbde2c25c21.jpeg 2x" data-dominant-color="6C6C7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-08 at 12.00.31 PM</span><span class="informations">1375×917 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does anyone know how to improve this?</p>

---

## Post #2 by @rbumm (2022-08-08 17:31 UTC)

<aside class="quote no-group" data-username="mahranahm" data-post="1" data-topic="24681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3ec8ea/48.png" class="avatar"> mahranahm:</div>
<blockquote>
<p>Here is a the labelled segmentations found in the (labels/final) folder.</p>
</blockquote>
</aside>
<p>Is that one of the labels you have used for training?</p>

---

## Post #3 by @mahranahm (2022-08-08 17:34 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> yes thats correct, with a total of 6 labelled volumes</p>

---

## Post #4 by @rbumm (2022-08-08 17:48 UTC)

<p>Did you include sternum, ribs, lungs, and airways on purpose? Maybe leave out those for the next test if acceptable</p>
<aside class="quote no-group" data-username="mahranahm" data-post="1" data-topic="24681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3ec8ea/48.png" class="avatar"> mahranahm:</div>
<blockquote>
<p>My first model didn’t include a background label</p>
</blockquote>
</aside>
<p>The “segmentation” model does not need a background label.</p>

---

## Post #5 by @mahranahm (2022-08-08 19:51 UTC)

<p>Ideally I would like to have these things segmented as well, but left them out for a test to see the results but not much changed. See results below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123c8af3e0ff8e627985f08e075e2bd4fe854cc8.jpeg" data-download-href="/uploads/short-url/2Bkj1hfxvxipZR9W67HOQQx0eVO.jpeg?dl=1" title="Screen Shot 2022-08-08 at 3.37.57 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c8af3e0ff8e627985f08e075e2bd4fe854cc8_2_690x463.jpeg" alt="Screen Shot 2022-08-08 at 3.37.57 PM" data-base62-sha1="2Bkj1hfxvxipZR9W67HOQQx0eVO" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c8af3e0ff8e627985f08e075e2bd4fe854cc8_2_690x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c8af3e0ff8e627985f08e075e2bd4fe854cc8_2_1035x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123c8af3e0ff8e627985f08e075e2bd4fe854cc8.jpeg 2x" data-dominant-color="62616F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-08 at 3.37.57 PM</span><span class="informations">1345×904 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @rbumm (2022-08-08 20:07 UTC)

<p>Ok are you able to do the auto-segmentation on the trained volumes with better results?</p>
<p>Are all label numbers identical for your targets?</p>
<aside class="quote no-group" data-username="mahranahm" data-post="5" data-topic="24681">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/3ec8ea/48.png" class="avatar"> mahranahm:</div>
<blockquote>
<p>, but left them out for a test to see the results but not much changed. See results below:</p>
</blockquote>
</aside>
<p>This last test volume seems to be a NIFTI format - did you train on NIFT images as well ?</p>

---

## Post #7 by @mahranahm (2022-08-08 20:51 UTC)

<p>So I ran the auto segmentation on a few volumes including the trained volumes and I seem to be getting the exact same result for all of them, The exact same segmentation like the one above.</p>
<p>Both the training and validation datasets are in NIFTI format</p>

---

## Post #8 by @rbumm (2022-08-09 04:54 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> could you have a look at this? Thank you.</p>

---

## Post #9 by @diazandr3s (2022-08-09 14:28 UTC)

<p>Many thanks for pinging me here, <a class="mention" href="/u/rbumm">@rbumm</a> - I haven’t seen this post.</p>
<p><a class="mention" href="/u/mahranahm">@mahranahm</a> welcome to the Slicer forum and thanks for posting this issue.</p>
<p>Could you please let us know which monai label version are you using?</p>
<p>If it is easy for you, I’d suggest you work directly with the GitHub repo. The reason for this is because it includes a more robust segmentation model called <em><a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/localization_spine.py" rel="noopener nofollow ugc">localization_spine</a></em> - probably not the best name but I’m still working on this to make it generic <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>The only two changes you have to make to this model before training are to update the label names here: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/configs/localization_spine.py#L33-L58" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/localization_spine.py at main · Project-MONAI/MONAILabel · GitHub</a>  - please don’t include background. you don’t need to segment it either.</p>
<p>And comment this line out: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/lib/infers/localization_spine.py#L83" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/localization_spine.py at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Another question/comment is about the label numbering - have you checked that each segment in the database has the same number? i.e. the right lung should be represented by the same number in all volumes.</p>
<p>Hope this helps,</p>

---
