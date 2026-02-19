---
topic_id: 28803
title: "Totalsegmentator Missing Humerus Distal Part"
date: 2023-04-07
url: https://discourse.slicer.org/t/28803
---

# TotalSegmentator - Missing humerus distal part

**Topic ID**: 28803
**Date**: 2023-04-07
**URL**: https://discourse.slicer.org/t/totalsegmentator-missing-humerus-distal-part/28803

---

## Post #1 by @Augusto (2023-04-07 20:27 UTC)

<p>Hello,</p>
<p>I am using TotalSegmentator for 3DSlicer version 1.5.5 (which is the most recent one right?) for the segmentation of the clavicle, humerus and scapula bones, using CPU and full resolution mode, in Slicer 5.2.1. The extension works fine, but the distal part of the humerus is not segmented (part that connects with the radius and ulna), thus not allowing to save a STL with a full segmented humerus. The scapula and clavicle seem to be segmented correctly, in all their structure. I have uploaded an image with the 3D visualization of the bones resulting from the TotalSegmentator.</p>
<p>My question is if this is a current problem of the extension, or should it also make the segmentation of the distal part of the humerus? I looked up the <a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">github webpage of the TotalSegmentator module</a> and i wonder if it is not related to the subtasks available, since there is one called “bone_extremeties”, which seems to account for this type of segmentations of the extremeties, but is not present in the 3dSlicer options. If so, should i get some kind of license (like it is said in the github site) to have this option in 3DSlicer, or these type of subtasks are not yet implemented for the 3DSlicer extension? Maybe <a class="mention" href="/u/wasserth">@wasserth</a> can help on this matter.</p>
<p>I also saw a <a href="https://discourse.slicer.org/t/how-to-segment-the-tibia-using-totalsegmentator/">topic</a> which may be related to this problem.</p>
<p>I also tested TotalSegmentator in Slicer sample data, and the same happens.</p>
<p>Thanks,</p>
<p>Augusto</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d869143c13cf221edc29c314adf3ec3d84195a63.png" data-download-href="/uploads/short-url/uSsgos0XGM44tNavtyOA10cYnon.png?dl=1" title="ex" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d869143c13cf221edc29c314adf3ec3d84195a63_2_322x500.png" alt="ex" data-base62-sha1="uSsgos0XGM44tNavtyOA10cYnon" width="322" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d869143c13cf221edc29c314adf3ec3d84195a63_2_322x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d869143c13cf221edc29c314adf3ec3d84195a63.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d869143c13cf221edc29c314adf3ec3d84195a63.png 2x" data-dominant-color="A09DB4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ex</span><span class="informations">327×507 57.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2023-04-08 09:14 UTC)

<p>Your observation seems to be accurate. On the TotalSegmentator GitHub, the humerus is listed under the structures that will require a license. They seem to be under development with special AI training, and according to our information, free licenses will be available for academic projects. It is worth mentioning that the TotalSegmentator AI could be <a href="https://github.com/wasserth/TotalSegmentator/blob/4f4196ac6e7d7b3b33bbb7ed6afe7cdd81aa9438/README.md#retrain-model-on-your-own">retrained on your own models</a> or that you could use incomplete segmentations (here humerus), improve them and train AI using the <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer#monai-label-plugin-for-3d-slicer">MONAILabel extension</a>.</p>
<p>We don’t yet have access to the complete license system’s specifications, and it’s unclear whether integrating this system into the TotalSegmentator 3D Slicer extension will even be possible or justified.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49464b25d9fb064bf1990326d11fc9429e9f101f.png" data-download-href="/uploads/short-url/asdsqKm0ZTpO1g581llNCRdbiJp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49464b25d9fb064bf1990326d11fc9429e9f101f.png" alt="image" data-base62-sha1="asdsqKm0ZTpO1g581llNCRdbiJp" width="690" height="228" data-dominant-color="F2F2E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1040×344 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @wasserth (2023-04-08 11:41 UTC)

<p>We are currently in the process of finishing these additional models. The “bones_extremities” models will  have a lot better humerus segmentation. It will be freely available for academic purposes. I can give you preliminary access. Integration into 3D Slicer extension should be possible when we are done with the final model.</p>

---

## Post #4 by @Augusto (2023-04-08 12:50 UTC)

<p>Understood. Thank you for the explanation!</p>

---

## Post #5 by @Augusto (2023-04-08 12:57 UTC)

<p>Thank you for your answer. Really glad you are working on this! I will wait for further updates in the TotalSegmentator github page, and then contact <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/lassoan">@lassoan</a> to understand if integrating the new subtasks into the 3DSlicer interface is feasible or not.</p>

---
