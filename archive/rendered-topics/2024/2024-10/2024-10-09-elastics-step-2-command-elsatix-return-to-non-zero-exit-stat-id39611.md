---
topic_id: 39611
title: "Elastics Step 2 Command Elsatix Return To Non Zero Exit Stat"
date: 2024-10-09
url: https://discourse.slicer.org/t/39611
---

# Elastics Step 2.command "elsatix return to non-zero exit status 1 error"

**Topic ID**: 39611
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/elastics-step-2-command-elsatix-return-to-non-zero-exit-status-1-error/39611

---

## Post #1 by @Osman_Basri_Erbek (2024-10-09 12:52 UTC)

<p>Please Help Me urgently,<br>
“I am trying to create a 3D image, and I will use the ABLTemporalBoneSegmentation module for this. I am following the steps in the application guide, but in Step 2, I am getting the error ‘command ‘elastix’ returned non-zero exit status 1.’ I have read what has been written in previous forums, and it seems that this error occurs because the two images are not aligned with each other. How can I align the two images? Thank you in advance.”</p>

---

## Post #2 by @lassoan (2024-10-10 04:20 UTC)

<p>Do you get any error if you try to register a <code>MRBrainTumor1</code> and <code>MRBrainTumor2</code> sample data sets to each other using <code>Elastix</code> module?</p>
<p>If it works then it is not a problem with Elastix but with the bone segmentation extension. Check out this topic:</p>
<aside class="quote" data-post="2" data-topic="39609">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/abl-temporal-bone-segmentation-module-error/39609/2">ABL Temporal Bone Segmentation Module ERROR</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This means the fixed and moving images are too far from each other. Most likely the issue is that you do not register your image to the atlas correctly. A few people has struggled with this, too - see <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/9">here</a>. You may work with these people to figure out how to do this registration. You may try to contact the developers of this extension, but there have not been any updates in the repository for several years, so you may need to do some digging to find someone.
  </blockquote>
</aside>


---

## Post #3 by @Osman_Basri_Erbek (2024-10-17 07:38 UTC)

<p>I am trying to use the data MRBrainTumor1 and MRBrainTumor2, but I’m not sure what to select in some places. Could you help me? for ex:<br>
-input wolume? MRBrainTumor1 or MRBrainTumor2 ?<br>
-moving volume? MRBrainTumor1 or MRBrainTumor2 ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82b3cc7a37e177fbae3e46f148b81134e1f66003.jpeg" data-download-href="/uploads/short-url/iEfhRLQjAfqgfsazr9tUgg2ZoTp.jpeg?dl=1" title="Adsız" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b3cc7a37e177fbae3e46f148b81134e1f66003_2_690x387.jpeg" alt="Adsız" data-base62-sha1="iEfhRLQjAfqgfsazr9tUgg2ZoTp" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b3cc7a37e177fbae3e46f148b81134e1f66003_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b3cc7a37e177fbae3e46f148b81134e1f66003_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82b3cc7a37e177fbae3e46f148b81134e1f66003_2_1380x774.jpeg 2x" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Adsız</span><span class="informations">1920×1077 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
