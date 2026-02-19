---
topic_id: 32470
title: "Totalsegmentator V2"
date: 2023-10-30
url: https://discourse.slicer.org/t/32470
---

# TotalSegmentator v2

**Topic ID**: 32470
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/totalsegmentator-v2/32470

---

## Post #1 by @rbumm (2023-10-30 10:36 UTC)

<p>We are excited to announce that the 3D Slicer TotalSegmentator extension is now compatible with TotalSegmentator v2!</p>
<p>TotalSegmentator stands out as a powerful tool, proficient in segmenting up to 117 classes in CT images. It is robust, fast, comprehensive, and can even be run without a GPU. Given its training on a vast variety of CT images - spanning different scanners, institutions, and protocols - it works consistently well across a broad spectrum of images.</p>
<p>These new structures are available in the freely available “total” (full-body CT segmentation) model: skull, sternum, costal cartilages, lumbosacral joint (S1), spinal cord, thyroid gland, prostate, brachiocephalic vein (left, right, trunk), common carotid artery (left/right), left atrial appendage, subclavian artery (left/right), pulmonary vein, superior vena cava, kidney cyst.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970fcfc79165f686cb1df8e39dac950f4e89e045.jpeg" data-download-href="/uploads/short-url/lylYphfmAaImdtFQDZBOPUmVqLz.jpeg?dl=1" title="image_00002" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970fcfc79165f686cb1df8e39dac950f4e89e045_2_589x500.jpeg" alt="image_00002" data-base62-sha1="lylYphfmAaImdtFQDZBOPUmVqLz" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970fcfc79165f686cb1df8e39dac950f4e89e045_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970fcfc79165f686cb1df8e39dac950f4e89e045_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970fcfc79165f686cb1df8e39dac950f4e89e045_2_1178x1000.jpeg 2x" data-dominant-color="47413C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00002</span><span class="informations">1920×1628 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Additional freely usable models (including some less robust, experimental ones): body surface, vertebral bodies, lung vessels, cerebral bleed, hip implants, coronary arteries, pleural and pericardial effusion.</p>
<p>New models with restricted license (free for academic use with some limitations; or paid commercial license) are also available, such as appendicular bones (patella, tibia, fibula, tarsal, metatarsal, feet phalanges; ulna, radius, carpal, metacarpal, hand phalanges) and tissue types (subcutaneous fat, skeletal muscle, torso fat).</p>
<p>Detailed description of all updates in TotalSegmentator v2 is available <a href="https://github.com/wasserth/TotalSegmentator/blob/master/resources/improvements_in_v2.md" rel="noopener nofollow ugc">here</a>.</p>
<p>To try these enhancements, install latest Slicer Preview Release (version 5.5.0 - rev32251, or later) and the TotalSegmentator extension.</p>
<p>Thank you for <a class="mention" href="/u/wasserth">@wasserth</a> for keeping developing <a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator</a>, <a class="mention" href="/u/lassoan">@lassoan</a> for maintaining the Slicer extension, and <a class="mention" href="/u/fedorov">@fedorov</a> and <span class="mention">@dclunie</span> for helping with updating standard terminology for all the new structures.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41ae347d14a65695d947687aedd15768248d4350.mp4">
  </div><p></p>

---

## Post #2 by @pieper (2023-10-30 11:23 UTC)

<p>Nice!  This updated version looks great <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p><em>Original text of this post:</em></p>
<blockquote>
<p>People should be aware that while the previous version of TotalSegmentator was freely available, the new version is free only for non-commercial and non-clinical use.</p>
</blockquote>
<p><em>Updated based on follow up information:</em></p>
<p>People should be aware that while much of TotalSegmentator freely available, the new version has some features that are free only for non-commercial and non-clinical use.  This is unlike Slicer itself and unlike many other Slicer extensions that are essentially unrestricted.  The TotalSegmentator license for these restricted features is here:<br>
<a href="https://backend.totalsegmentator.com/license-academic/" class="onebox" target="_blank" rel="noopener">https://backend.totalsegmentator.com/license-academic/</a></p>
<p>People interested in commercial or clinical applications should contact <a class="mention" href="/u/wasserth">@wasserth</a> for information.</p>

---

## Post #3 by @wasserth (2023-10-30 12:00 UTC)

<p>Thanks for upgrading the TotalSegmentator Extension to v2! Great work!</p>
<p>A bit more information about the license of TotalSegmentator v2:<br>
Everything which was freely available in v1 is also freely available in v2 and even a lot more classes. Just as v1 it can be used freely for any usage (e.g. commercially). Only a few of the newly added classes have a more restricted license. Specifically we are talking about the the subtasks heartchambers_highres, appendicular_bones, tissue_types, face (see <a href="https://github.com/wasserth/TotalSegmentator#subtasks" rel="noopener nofollow ugc">readme</a>). For these subtasks the restrictions which Steve mentioned apply. You can use them freely for non-commercial usage. If you want to use them commercially you need to purchase a license.</p>

---

## Post #4 by @lassoan (2023-10-30 15:31 UTC)

<p>2 posts were split to a new topic: <a href="/t/can-totalsegmentator-segment-maxillofacial-ct-as-well/32484">Can TotalSegmentator segment maxillofacial CT as well?</a></p>

---

## Post #5 by @pieper (2023-10-30 12:32 UTC)

<p>Thank you for the clarification Jakob.  Sorry my previous post was overly broad.  I think it’s important for people to be aware of these issues so they can comply with the license terms.  I notice the license also says that that segmentations from restricted models are not to be used to train new models, so that’s something that some developers will need to take into consideration.</p>
<p>I understand that the SlicerTotalSegmentator user interface flags the models that require a license, so I hope that will help people use the tool in accordance with the licenses.</p>

---

## Post #7 by @Brandon_Holt (2023-10-30 13:56 UTC)

<p>Thanks for the update Dr. Bumm! I didn’t realize this was your Extension! This is amazing.</p>

---

## Post #9 by @rbumm (2023-10-30 14:15 UTC)

<p>Thanks Brandon, the extension was written by Andras Lasso <a class="mention" href="/u/lassoan">@lassoan</a> as the principal author and maintained by us as a team.</p>

---

## Post #10 by @mau_igna_06 (2023-10-30 16:12 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="32470">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I notice the license also says that that segmentations from restricted models are not to be used to train new models</p>
</blockquote>
</aside>
<p>Hi</p>
<p>How does someone detect this? I foresee AI models will be like gold in the sense that when you have a gold bar you never know from where it was sourced after melting it</p>
<p>Does someone share this thought?</p>

---

## Post #11 by @pieper (2023-10-30 16:26 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="10" data-topic="32470">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>you never know from where it was sourced</p>
</blockquote>
</aside>
<p>Yes, people should be very careful about what data they rely on when training their models in order to respect the licensing terms.</p>
<p>This particular term applies specifically to the restricted models for the subtasks that Jakob mentioned.  I understand now that you won’t have access to these models unless you specifically request them from the TotalSegmentator site, so it should be clear when this clause is in effect.  But people should be aware so they can make appropriate plans if they want to use those restricted models.</p>
<blockquote>
<p>3.2 LICENSEE shall not use the results of the use of the SOFTWARE or any IMPROVEMENTS to train an own similar algorithm. For the avoidance of doubt, “results of the use of the SOFTWARE or any IMPROVEMENTS” means any data, information, or insights generated by the SOFTWARE or any IMPROVEMENTS, including but not limited to predictions and segmentations.</p>
</blockquote>
<p>Linked from this site: <a href="https://backend.totalsegmentator.com/license-academic/" class="inline-onebox">Streamlit</a></p>
<p>But I also understand now that this term does not apply to the free models available in v1 and v2 of TotalSegmentator.</p>

---

## Post #12 by @mau_igna_06 (2023-10-30 17:59 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="10" data-topic="32470">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Does someone share this thought?</p>
</blockquote>
</aside>
<p>NOTE: just to empathize this thought I had is not intended for any AI project/researcher in particular, here is the same post from 2 months ago in my LinkedIn <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.linkedin.com/posts/engineerdominguez_gold-knowledge-activity-7102815056056233984-hPnj/">
  <header class="source">
      <img src="https://static.licdn.com/aero-v1/sc/h/al2o9zrvru7aqj8e1x2rzsrca" class="site-icon" width="" height="">

      <a href="https://www.linkedin.com/posts/engineerdominguez_gold-knowledge-activity-7102815056056233984-hPnj/" target="_blank" rel="noopener nofollow ugc">linkedin.com</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://static.licdn.com/aero-v1/sc/h/c45fy346jw096z9pbphyyhdz7" class="thumbnail">

<h3><a href="https://www.linkedin.com/posts/engineerdominguez_gold-knowledge-activity-7102815056056233984-hPnj/" target="_blank" rel="noopener nofollow ugc">Mauro Dominguez on LinkedIn: #gold #knowledge</a></h3>

  <p>As far as I understand #gold is fungible, after melting it from a labelled bar, it has almost the same value though you may need to check chemically to confirm…</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @lassoan (2023-10-30 18:30 UTC)

<p>It may be difficult to trace the origin of a trained AI model using technical means. However, there are legal ways to make it very difficult for someone for taking advantage of inappropriately obtained goods (gold, source code, data, etc). Therefore, licensing restrictions can provide meaningful protection.</p>

---

## Post #14 by @lassoan (2023-10-30 18:55 UTC)

<p>A post was split to a new topic: <a href="/t/problem-running-totalsegmentator-in-slicer-5-4/32491">Problem running TotalSegmentator in Slicer-5.4</a></p>

---

## Post #15 by @lassoan (2023-10-30 19:17 UTC)

<p>A post was split to a new topic: <a href="/t/failed-to-get-totalsegmentator-package-version-on-macos/32492">Failed to get TotalSegmentator package version on macOS</a></p>

---

## Post #16 by @akmal871026 (2023-10-31 00:42 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>TotalSegmentator v2 can run using version 5.4.0?</p>

---

## Post #17 by @lassoan (2023-10-31 05:02 UTC)

<p>TotalSegmentator v2 requires Slicer-5.5.0 - rev32251 or later, as Python packages bundled with Slicer-5.4.0 are too old, which would make installation of the required Python packages too complicated.</p>
<p>We may update Python packages in the Slicer-5.4.1 patch release in a couple of weeks. If that happens then we’ll switch to TotalSegmentator v2.</p>

---

## Post #18 by @evaherbst (2023-10-31 11:07 UTC)

<p>Thanks <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for implementing this, and <a class="mention" href="/u/wasserth">@wasserth</a> for the new version. Looking forward to testing it out!</p>

---

## Post #19 by @Mohamed_Alalli_BILAL (2023-11-01 06:58 UTC)

<p>Nice! This updated version looks great <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #20 by @belkacemi_djelloul (2023-11-01 11:31 UTC)

<p>it looks amazing !!!</p>

---

## Post #21 by @belkacemi_djelloul (2023-11-01 11:35 UTC)

<p>is it available or not yet?</p>

---

## Post #22 by @rbumm (2023-11-01 12:00 UTC)

<p>If you install 3d Slicer 5.5.0 (preview) and the TotalSegmentator extenson it is available already.</p>

---

## Post #23 by @Samuel_Guigo (2023-11-01 20:33 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfb5d77cde08c0829c0512067b64d9d103ad1912.jpeg" data-download-href="/uploads/short-url/vV24ljr3bC7c8uRKoGI69pcgHJw.jpeg?dl=1" title="Capture d’écran 2023-11-01 à 21.28.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb5d77cde08c0829c0512067b64d9d103ad1912_2_690x285.jpeg" alt="Capture d’écran 2023-11-01 à 21.28.23" data-base62-sha1="vV24ljr3bC7c8uRKoGI69pcgHJw" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb5d77cde08c0829c0512067b64d9d103ad1912_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb5d77cde08c0829c0512067b64d9d103ad1912_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb5d77cde08c0829c0512067b64d9d103ad1912_2_1380x570.jpeg 2x" data-dominant-color="625C67"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-11-01 à 21.28.23</span><span class="informations">3552×1472 784 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks so much ! But i have this type of results, not so smooth … somebody had the solution ? thanks</p>

---

## Post #24 by @rbumm (2023-11-01 20:44 UTC)

<p>You seem to work in CPU mode, where the volumes are downsampled for the segmentation. Invest in a CUDA-enabled GPU to get better results. You could also smooth your segmentations in the segment editor.</p>

---

## Post #25 by @Samuel_Guigo (2023-11-01 20:58 UTC)

<p>Yess i’m actually work with a macbook pro m2 pro.</p>

---

## Post #26 by @rbumm (2023-11-01 21:25 UTC)

<p>Apple hardware has no CUDA-enabled GPU unfortunately.</p>

---

## Post #27 by @lassoan (2023-11-02 00:37 UTC)

<p>Apple has some hardware acceleration that PyTorch may be able to utilize, so it is worth trying the full-quality mode (disable “fast” option) and see what segmentation quality you can get and with what computation time.</p>
<p>If you don’t want to invest into buying a computer that has a CUDA-capable GPU then you can rent a GPU-equipped virtual machine from Amazon/Microsoft/Google and install&amp;run Slicer there.</p>

---

## Post #28 by @fedorov (2023-11-02 02:53 UTC)

<p>If you are a researcher funded by the US government, it is rather easy to get access to a VM desktop with GPU via ACCESS allocation - quite a few of us in the IDC team have been using those VMs exactly for the purpose of testing/using Slicer functionality that requires GPU: <a href="https://learn.canceridc.dev/cookbook/access-allocations" class="inline-onebox">ACCESS allocations - IDC User Guide</a>.</p>

---

## Post #29 by @Chuan (2023-11-09 19:43 UTC)

<p>Thanks for your updating. It looks amazing on adult!  But do you think it will also work well for infants?<br>
Also do those training data cover infant whole body CT images, since I am interested in infant whole body segmentation!</p>

---

## Post #30 by @lassoan (2023-11-21 12:11 UTC)

<p>The model had been trained on a very wide variety of data. It can even pick up some anatomy on animal CTs (for example on swine images, ribs and spine was segmented well, liver was found but segmented inaccurately). I would expect that it would work fairly well on human infant CTs, but please try and let us know.</p>

---
