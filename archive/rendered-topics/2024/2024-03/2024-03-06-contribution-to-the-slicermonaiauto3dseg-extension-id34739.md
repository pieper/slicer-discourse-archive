---
topic_id: 34739
title: "Contribution To The Slicermonaiauto3Dseg Extension"
date: 2024-03-06
url: https://discourse.slicer.org/t/34739
---

# Contribution to the SlicerMONAIAuto3DSeg extension

**Topic ID**: 34739
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/contribution-to-the-slicermonaiauto3dseg-extension/34739

---

## Post #1 by @rfenioux (2024-03-06 12:25 UTC)

<p>There has been an internal effort at Kitware Europe to simplify the use of segmentation models available as <a href="https://docs.monai.io/en/latest/bundle_intro.html" rel="noopener nofollow ugc">MONAI bundles</a> from 3D Slicer.</p>
<p>The goal of this post is to gather some feedback about the best way to share this work.</p>
<p>For this purpose, we are working on a module that allows users to load and run segmentation models from a bundle available locally, or download one from the <a href="https://monai.io/model-zoo.html" rel="noopener nofollow ugc">MONAI model zoo</a>. Our intention is to make this work available to the community, and we initially planned to create a new 3D Slicer extension for this.</p>
<p>However, we realized that our work present an overlap with what offers the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg" rel="noopener nofollow ugc">SlicerMONAIAuto3DSeg extension</a> (<a class="mention" href="/u/lassoan">@lassoan</a>), which is why are now pondering whether contributing our work to this project would make more sense. A new extension might be redundant, as both projects aim to provide an easy way to run inference for Monai segmentation models from within 3D Slicer.</p>
<p>Here are some of the features that we could bring, that are not available in SlicerMONAIAuto3DSeg as far as we are aware:</p>
<ul>
<li>support models distributed as Monai bundles (instead of Auto3DSeg)</li>
<li>load local bundles from disk</li>
<li>retrieve bundles from the Monai Model Zoo</li>
</ul>
<p>Note that, like SlicerMONAIAuto3DSeg, there are limitations to our work due to the assumptions we need to make about the model (MONAI bundle being very permissive and general, to allow for many different architectures, input/outputs, etc.).</p>
<p>We would love to hear your thoughts about this.</p>

---

## Post #2 by @lassoan (2024-03-06 13:22 UTC)

<p>The features you described could be very easily added to the MONAIAuto3DSeg extension (and we have been considering adding running from local folder anyway), so collaborating on this extension would make the most sense.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> what do you think? If thr scope of the extension will be broadened then we may need to rename the extension.</p>
<p><a class="mention" href="/u/rfenioux">@rfenioux</a> If you send a pull request with a runner script for MONAI bundle models and code snippet to download a model from the MONAI Model Zoo then I can take care of the rest.</p>
<p>Note that in this extension we have achieved two important goals:</p>
<ul>
<li>democratizing AI segmentation: we do not require a GPU, low-resolution version is provided for each model that runs on the CPU in few minutes</li>
<li>describe segmentation output using standard terminology codes (using some arbitary common English name is not suitable for clinical use)</li>
</ul>
<p>It would be nice if the newly added models could meet these standards, but it is not a dealbreaker if they don’t (we could add filtering option to hide models that only work on GPU or do not properly specify their segmentation output).</p>

---

## Post #3 by @diazandr3s (2024-03-06 14:37 UTC)

<p>Hi <a class="mention" href="/u/rfenioux">@rfenioux</a>,</p>
<p>This is great! Thanks for posting/asking this.</p>
<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a>, MONAI Bundles can be easily integrated/added to the MONAI Auto3DSeg extension - we might need to change the name once the extension can consume bundles.</p>
<p>MONAI Bundles allow you to do inference and training. So far MONAIAuto3DSeg has been designed for inference only (both in CPU and GPU). We assume the training is done with the Auto3DSeg in a separate cycle.</p>
<p>There are Bundles for different types of image modalities: endoscopy (video), pathology and radiology (CT and MR). Within radiology, there are bundles for detection, segmentation and landmark detection.</p>
<p>Here are the current ones for radiology applications:</p>
<p><em>brats_mri_segmentation</em><br>
<em>lung_nodule_ct_detection</em><br>
<em>multi_organ_segmentation</em><br>
<em>pancreas_ct_dints_segmentation</em><br>
<em>prostate_mri_anatomy</em><br>
<em>renalStructures_CECT_segmentation</em><br>
<em>renalStructures_UNEST_segmentation</em><br>
<em>spleen_ct_segmentation</em><br>
<em>spleen_deepedit_annotation</em><br>
<em>swin_unetr_btcv_segmentation</em><br>
<em>valve_landmarks</em><br>
<em>ventricular_short_axis_3label</em><br>
<em>wholeBody_ct_segmentation</em><br>
<em>wholeBrainSeg_Large_UNEST_segmentation</em></p>
<p>I’d suggest starting with the bundles for segmentation in radiology and the ones on a single modality/sequence. Once this is working, we can move to multimodality and then detection.</p>
<p>I’ll be more than happy to further discuss this over a video call.</p>
<p>Looking forward to your comments/thoughts</p>

---

## Post #4 by @rfenioux (2024-03-06 16:56 UTC)

<p>Thank you both for your valuable inputs, I’m glad to see our intuition confirmed.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="34739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be nice if the newly added models could meet these standards, but it is not a dealbreaker if they don’t (we could add filtering option to hide models that only work on GPU or do not properly specify their segmentation output).</p>
</blockquote>
</aside>
<p>Strictly enforcing these rules requires having control over the available models I think, which is not the case when running locally stored bundles. It’s also not necessarily appropriate for this use case, since people may want to run custom bundles (e.g. fine tuned on their specific tasks).<br>
However filtering would make sense for models retrieved from the model zoo (we’ll need to filter for supported bundles anyway).</p>
<aside class="quote no-group quote-modified" data-username="diazandr3s" data-post="3" data-topic="34739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>MONAI Bundles allow you to do inference and training. […]<br>
I’d suggest starting with the bundles for segmentation in radiology and the ones on a single modality/sequence.</p>
</blockquote>
</aside>
<p>I fully agree. Inference, and especially segmentation is the task that benefits most from being integrated in a 3D Slicer workflow (and conversely, it is probably what most 3D Slicer users are interested in).</p>

---

## Post #5 by @e.baldelomar (2025-04-04 20:56 UTC)

<p>Hello, has there been any update to integrate models/bundles into Slicer via  Auto3Dseg? I’m very much interested in specifically applying one of the renalStructures one…if it is already possible to use these models with 3DSlicer/Monai, would very much appreciate any guidance how to do this.</p>

---

## Post #6 by @rfenioux (2025-04-07 07:57 UTC)

<p>Hello Edwin,<br>
There is work underway, I will keep you updated as soon as it is made available.</p>

---
