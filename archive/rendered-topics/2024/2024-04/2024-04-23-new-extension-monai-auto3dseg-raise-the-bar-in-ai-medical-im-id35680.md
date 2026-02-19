---
topic_id: 35680
title: "New Extension Monai Auto3Dseg Raise The Bar In Ai Medical Im"
date: 2024-04-23
url: https://discourse.slicer.org/t/35680
---

# New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation

**Topic ID**: 35680
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation/35680

---

## Post #1 by @diazandr3s (2024-04-23 14:21 UTC)

<h1><a name="p-110049-new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation-1" class="anchor" href="#p-110049-new-extension-monai-auto3dseg-raise-the-bar-in-ai-medical-image-segmentation-1" aria-label="Heading link"></a>New extension: MONAI Auto3DSeg - raise the bar in AI medical image segmentation</h1>
<p>MONAI Auto3DSeg extension is a collaboration between MONAI and 3D Slicer developer teams (led by Andres Diaz Pinto - NVIDIA and Andras Lasso - PerkLab) to improve on the state-of-the-art in fully automatic 3D medical image segmentation and make the results widely accessible.</p>
<p>The extension comes with dozens of pre-trained segmentation models for specific clinical use cases, which are designed to be fast and run anywhere within minutes - on any average computer, without GPU, even on laptops. The models can segment images of various modalities (CT, MRI), anatomies (mediastinal, vertebra, brain, prostate, lungs, etc.) and pathologies (tumor, hemorrhage, edema, etc.), using one or more input images. All models come with a description and sample data set for easy testing. See <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults" rel="noopener nofollow ugc">complete list of models - with screenshots, computation times, list of segments</a>.</p>
<p><strong>To get started</strong>: <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/tree/main?tab=readme-ov-file#setup" rel="noopener nofollow ugc">install the latest Slicer Preview Release (revision 32818 or later) and the MONAIAuto3DSeg extension</a> and follow this <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg?tab=readme-ov-file#setup" rel="noopener nofollow ugc">step-by-step tutorial</a>. 3-minute video demo/tutorial showing the module in action:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="N8Dy2Bu8fjo" data-video-title="Automatic multi modality AI medical image segmentation in 3D Slicer using MONAIAuto3DSeg extension" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=N8Dy2Bu8fjo" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/N8Dy2Bu8fjo/maxresdefault.jpg" title="Automatic multi modality AI medical image segmentation in 3D Slicer using MONAIAuto3DSeg extension" width="690" height="388">
  </a>
</div>

<p>MONAI Auto3DSeg allows <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/tree/main?tab=readme-ov-file#developers" rel="noopener nofollow ugc">adding your own custom models</a> to the plugin. Users can leverage this feature to create segmentation models that are optimized for their own data, to their specific clinical requirements.</p>
<p>The extension works offline, without internet connection (after the setup is completed and selected model is downloaded) and does not send any data to the cloud or any other computer.</p>
<p>The MONAI Auto3DSeg software is open-source and freely accessible (Apache License 2.0). The developers do not claim that the tools are appropriate for any specific clinical purpose and the user is responsible for obtaining any necessary ethics or regulatory approvals.</p>

---

## Post #2 by @dzenanz (2024-04-23 14:46 UTC)

<p>Does it work on Windows? Auto3DSeg <a href="https://github.com/Project-MONAI/MONAI/issues/6821#issuecomment-1789933361" rel="noopener nofollow ugc">didn’t work on Windows</a> half a year ago.</p>

---

## Post #3 by @lassoan (2024-04-23 14:48 UTC)

<p>Yes, it works well on Windows (also on Linux and macOS). Everything is automatically installed and set up by a single click when the user starts the segmentation.</p>

---

## Post #4 by @dzenanz (2024-04-23 15:58 UTC)

<p>I now see that this extension only runs the inference, and not training.</p>

---

## Post #5 by @lassoan (2024-04-23 16:09 UTC)

<p>Yes, the extension provides lots of ready-to use pre-trained models for users. They cover a wide range of body parts, anatomical structures and lesions, using multiple imaging modalities.</p>
<p>If a developer wants to create new models, there are links to examples and tutorials in the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg?tab=readme-ov-file#training-models">documentation</a>. For interactive training, <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1630">integration with MONAILabel</a> is being considered. But so far models have been trained from already labeled data, so it was all done by just running a Python script non-interactively.</p>

---

## Post #6 by @ShaneKirkbride (2024-04-23 16:49 UTC)

<p>Has any work been done related to cardiology/heart segmentation?</p>

---

## Post #7 by @lassoan (2024-04-23 16:54 UTC)

<p>Yes, there are a couple of heart segmentation models. See complete list of models <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults">here</a>. New models will be added based on user demand and availability of training data.</p>
<p>The SlicerHeart group is developing models for cardiac ultrasound segmentation using MONAI Auto3DSeg and it seems to work well, too, but I’m not sure if those models will be made openly available. If they will be then we’ll add them to this extension.</p>

---

## Post #8 by @fedorov (2024-04-23 20:06 UTC)

<p>Looks very cool, thank you for putting this together! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>What are the terms of the licenses for the models that are integrated?</p>
<p>From what I have seen before, sometimes the license imposes restrictions on the use of the segmentation results produced by the model. It would be helpful if the <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults">aforementioned list of models</a> included licensing information.</p>

---

## Post #9 by @fedorov (2024-04-23 20:20 UTC)

<p>To clarify, I do understand that the code places no restrictions on reuse, but I believe in some cases model may be covered by a different license, or model license terms may be dictated by the license covering the data that was used to train the model.</p>

---

## Post #10 by @lassoan (2024-04-23 21:01 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> can provide more details on the training data sources, but in short: we only trained on data sets that did not impose any restrictions on how the data is used. Previously, we used some data sets that were distributed with restrictive licenses, but in the end we decided to drop all those models, both to simplify our life (so that we don’t need to track what models are restricted and how and warn the users, etc.) and also not promote any data sets that come with strings attached.</p>
<p>We will add more information on all sources that were used to train each model to make this more clear.</p>

---

## Post #11 by @diazandr3s (2024-04-23 21:12 UTC)

<p>Thanks for asking this, <a class="mention" href="/u/fedorov">@fedorov</a>.</p>
<p>This is a very good point. We’ll add that information to all the available models.</p>
<p>To answer your question now, we’ve used BRATS (You are free to use and/or refer to the BraTS datasets in your own research …), Medical Segmentation Decathlon (Creative Commons license CC-BY-SA4.0), TotalSegmentatorV1 (Apache License 2.0) and TotalSegmentatorV2 (Apache License 2.0) datasets to train the available models.</p>
<p>The model for ICrH and brain CT segmentation was trained on a randomized controlled trial conducted by Ken: <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/pull/40#issuecomment-2050509368" class="inline-onebox" rel="noopener nofollow ugc">Add codes for intracranial hemorrhage model by lassoan · Pull Request #40 · lassoan/SlicerMONAIAuto3DSeg · GitHub</a></p>
<p>We’ll update all this in the repo.</p>

---

## Post #12 by @fedorov (2024-04-23 22:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/diazandr3s">@diazandr3s</a> thanks for the quick responses! Having this information along the models will be great.</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="11" data-topic="35680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Medical Segmentation Decathlon (Creative Commons license CC-BY-SA4.0)</p>
</blockquote>
</aside>
<p>I think CC-BY-SA may be equivalent to the viral GNU - “SA” means “Share Alike”: <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en" class="inline-onebox">CC BY-SA 4.0 Deed | Attribution-ShareAlike 4.0 International | Creative Commons</a>.</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="11" data-topic="35680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>TotalSegmentatorV1 (Apache License 2.0) and TotalSegmentatorV2 (Apache License 2.0)</p>
</blockquote>
</aside>
<p>From what I can tell, TotalSegmentator datasets are shared under <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">CC-BY</a>, which is less restrictive than CC-BY-SA - it only requires attribution: <a href="https://zenodo.org/records/10047292" class="inline-onebox">Dataset with segmentations of 117 important anatomical structures in 1228 CT images</a>.</p>

---

## Post #13 by @pieper (2024-04-23 22:22 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="35680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>equivalent to the viral GNU</p>
</blockquote>
</aside>
<p>Yes, <a href="https://creativecommons.org/share-your-work/licensing-considerations/compatible-licenses/#:~:text=GPLv3%3A%20The%20GNU%20General%20Public%20License%20version%203%20was%20declared%20a%20%E2%80%9CBY%2DSA%E2%80%93Compatible%20License%E2%80%9D%20for%20version%204.0%20on%208%20October%202015.">according to the CC site</a> GPLv3 is one of the only licenses you can use for material based on CC-BY-SA content.  Just how this applies to the trained models is <a href="https://hbr.org/2023/04/generative-ai-has-an-intellectual-property-problem">a tricky topic</a>.</p>

---

## Post #14 by @lassoan (2024-04-23 22:34 UTC)

<p>The main thing we wanted to make sure is that we are not tainted by non-commercial clauses (NC). Even if share-alike (SA) is interpreted the strictest possible way, it is still allowed to commercially use models that were trained on SA data if the resulting model is shared, which it is.</p>

---

## Post #15 by @pieper (2024-04-23 23:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="35680">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it is still allowed to commercially use models that were trained on SA data if the resulting model is shared, which it is.</p>
</blockquote>
</aside>
<p>Right - I agree the models offered here are compatible with the SA terms, but if someone trains a new model based on this data or on data generated by models trained on this data and wishes not to share it then they should review these terms with IP consultation.</p>

---

## Post #16 by @amitjc (2024-04-24 02:49 UTC)

<p>This is awesome. Thanks a ton.</p>
<p>Amitkumar J. Choudhari, DNB, FRCR<br>
Consultant Radiologist &amp; Associate Prof.,<br>
Tata Memorial Centre.</p>

---

## Post #17 by @lassoan (2024-04-25 14:51 UTC)

<p>12 posts were split to a new topic: <a href="/t/facial-muscle-segmentation-using-monai-auto3dseg/35734">Facial muscle segmentation using MONAI Auto3DSeg</a></p>

---

## Post #28 by @lassoan (2024-04-25 18:47 UTC)

<p>5 posts were split to a new topic: <a href="/t/error-when-running-monai-auto3dseg-cannot-import-name-metakeys-from-monai-utils/35738">Error when running MONAI Auto3DSeg (cannot import name ‘MetaKeys’ from ‘monai.utils’)</a></p>

---

## Post #29 by @lassoan (2024-04-29 13:46 UTC)

<p>3 posts were split to a new topic: <a href="/t/help-with-setting-up-monailabel/35796">Help with setting up MONAILabel</a></p>

---

## Post #30 by @lassoan (2024-05-11 12:27 UTC)

<p>5 posts were split to a new topic: <a href="/t/automatic-segmentation-tools-for-brain-avm/36082">Automatic segmentation tools for brain AVM?</a></p>

---

## Post #31 by @lassoan (2024-07-08 13:52 UTC)

<p>2 posts were split to a new topic: <a href="/t/is-monai-auto3dseg-whole-body-segmentation-model-based-on-segresnet/37255">Is MONAI Auto3DSeg Whole body segmentation model based on SegResNet?</a></p>

---

## Post #33 by @lassoan (2024-07-08 13:50 UTC)

<p>5 posts were split to a new topic: <a href="/t/are-there-automatic-segmentation-models-for-musculoskeletal-anatomy/37254">Are there automatic segmentation models for musculoskeletal anatomy?</a></p>

---

## Post #34 by @lassoan (2024-07-12 19:15 UTC)

<p>A post was split to a new topic: <a href="/t/ai-segmentation-models-for-head-neck-and-dental/37339">AI segmentation models for head&amp;neck and dental</a></p>

---

## Post #35 by @Carlos_Arrieta (2025-03-01 00:08 UTC)

<p>Hi amazing module !!! is it possible to export a model after its colorized and lights where applied as a 3D object ?</p>

---

## Post #36 by @lassoan (2025-03-01 03:05 UTC)

<p>Yes, just save the scene, everything is saved in standard/open file formats. What you may find challenging is not many software can render RGBA volumes and of course each software has its own lighting model and settings.</p>

---

## Post #37 by @Chris_Longros (2025-08-17 18:20 UTC)

<p>Does this extension use the Pancreas CT DiNTS for pancreas segmentation? (<a href="https://monai.io/model-zoo.html#/model/pancreas_ct_dints_segmentation" class="inline-onebox" rel="noopener nofollow ugc">MONAI Model Zoo - Pre-trained Models for Medical Imaging</a>)</p>

---

## Post #39 by @Dr.Hunz (2025-12-20 17:26 UTC)

<p>do we have for segmentate the tooth. Thankyou</p>

---
