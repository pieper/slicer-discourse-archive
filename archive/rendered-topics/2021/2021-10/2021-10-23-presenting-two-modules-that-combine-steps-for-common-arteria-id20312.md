# Presenting two modules that combine steps for *common* arterial segmentation

**Topic ID**: 20312
**Date**: 2021-10-23
**URL**: https://discourse.slicer.org/t/presenting-two-modules-that-combine-steps-for-common-arterial-segmentation/20312

---

## Post #1 by @chir.set (2021-10-23 14:11 UTC)

<p>Here are two small modules that <em>combine</em> the different usual steps to segment <em>small</em> portions of arteries on CT angioscans, with an ultimate goal of extracting centerlines. They do not target ‘head to toe’ segmentations.</p>
<p>They are definitely useful to me as time saving tools, and I present them here under the assumption that they might be useful to others. However, if this post is perceived as dead noise, please apologize in advance.</p>
<p>Both of them remote control the ‘Segment editor’ modules and the ‘Extract centerline’ modules. Internally, API calls are made as much as possible, else, UI gestures are simulated. The latter part may be seen as a ‘macro style’ approach.</p>
<p><a href="https://github.com/chir-set/MetaCenterlineExtraction/tree/main/FiducialCenterlineExtraction/" rel="noopener nofollow ugc">Fiducial centerline extraction</a></p>
<p>This module uses fiducial points as input, placed inside the arterial lumen. An ROI must be used to limit segmentation to a targeted small region. Each fiducial point will be an endpoint in the ‘Extract centerline’ module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56129a887369b76f6be043c04694337c36eeb0b.png" data-download-href="/uploads/short-url/pSyAIW8dhSD01ciDATyFbPdRJ5p.png?dl=1" title="carotid_0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56129a887369b76f6be043c04694337c36eeb0b_2_188x500.png" alt="carotid_0" data-base62-sha1="pSyAIW8dhSD01ciDATyFbPdRJ5p" width="188" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56129a887369b76f6be043c04694337c36eeb0b_2_188x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b56129a887369b76f6be043c04694337c36eeb0b_2_282x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56129a887369b76f6be043c04694337c36eeb0b.png 2x" data-dominant-color="1D211A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">carotid_0</span><span class="informations">288×762 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is suitable for common regions dealt with in vascular surgery (aorto-iliac bifurcation, carotid bifurcation, visceral arteries with the aorta…), with ‘goodly sized’ arteries. The resulting segmentation is usually of good quality and centerline extraction succeeds readily. This module is not that much time consuming.</p>
<p><a href="https://github.com/chir-set/MetaCenterlineExtraction/tree/main/CurveCenterlineExtraction/" rel="noopener nofollow ugc">Curve centerline extraction</a></p>
<p>This one uses a markups open curve as input, to produce a single tube as output. Each control point <em>must</em> be placed in the lumen, else the resulting segmentation will be a malformed time consuming lump.</p>
<p>It targets otherwise difficult to segment vessels, with poor contrast or very small or surrounded by veins with excessive contrast. In practice, I’ve seen it so far quite efficient for diseased small vessels like distal visceral arteries, or subclavians that are surrounded by many bones. Segmenting left anterior descending and right coronary arteries have produced good results too. Even with the greater saphenous vein, when there is sufficient contrast in it in CT angioscans studying arteries.</p>
<p>Control point placement is determining. A few points can be placed in a ‘Volume rendering’ 3D view, or in slice views, followed by curve resampling. Next, each point must be checked to lie in the lumen. This is yet time consuming.</p>
<p>The first and last points will be endpoints to ‘Extract centerline’ module, and are not used for segmentation. It is therefore helpful that the second control point be reasonably close to the first point, and that the before last one be close to the last point.</p>
<p>The resulting segmentation mush be checked in slice views, so that is not excessive, overlapping on calcifications, or insufficient.</p>
<p>Centerline extraction may often fail however. In such cases, smoothing with ‘Fill holes’ at minimal kernel size helps to create centerlines (smoothing is faster using the 3D brush). After smoothing, work should be continued directly in ‘Extract centerline’ module obviously. It is recommended  to save work done before extracting centerlines, because this may crash Slicer on poor quality segments.</p>
<p>Whether with the segmentation step or with extracting centerlines, post-procesing is often needed here.</p>
<p>This module might perhaps be more suitable for research work. Its targeted approach by point placement is probably its main interest.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83f84016890df24007446cb0f08905bebdc59ea7.jpeg" data-download-href="/uploads/short-url/iPsqcexbgQoKv5g8quGS7Gp4jPh.jpeg?dl=1" title="anterior_communicating_0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83f84016890df24007446cb0f08905bebdc59ea7.jpeg" alt="anterior_communicating_0" data-base62-sha1="iPsqcexbgQoKv5g8quGS7Gp4jPh" width="690" height="479" data-dominant-color="A17261"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">anterior_communicating_0</span><span class="informations">1097×762 65.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02a1ed50ee355a0a9ee30d49f6cf1ad5813f8d5.png" data-download-href="/uploads/short-url/mQSDy4hdSV31U6hJXs86lGhuuKp.png?dl=1" title="right_subclavian" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02a1ed50ee355a0a9ee30d49f6cf1ad5813f8d5_2_690x494.png" alt="right_subclavian" data-base62-sha1="mQSDy4hdSV31U6hJXs86lGhuuKp" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02a1ed50ee355a0a9ee30d49f6cf1ad5813f8d5_2_690x494.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02a1ed50ee355a0a9ee30d49f6cf1ad5813f8d5_2_1035x741.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02a1ed50ee355a0a9ee30d49f6cf1ad5813f8d5.png 2x" data-dominant-color="2A2D29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">right_subclavian</span><span class="informations">1063×762 87.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the hope that they might be useful to others.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-10-23 22:47 UTC)

<p>Thank you for sharing these modules. It would be nice if you could record a video of a typical case (preferably on one of the Slicer sample data sets) just in case someone has difficulty following the written instructions.</p>
<p>You could also consider submitting these modules to the extensions index. You can do that by either moving them to Slicer VMTK extension (a bit less work) or submit your extension (a bit more visibility at the cost of some maintenance and support workload). Based on all your contributions and experience in Slicer extension development, you could now get direct write access to SlicerVMTK extension, so you would not have to wait for your changes to be reviewed each time.</p>

---

## Post #3 by @chir.set (2021-10-24 13:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>record a video</p>
</blockquote>
</aside>
<p>Here are links for 3 studies :</p>
<p>Centerline <a href="https://disk.yandex.com/i/HYdOroqLlpiPyA" rel="noopener nofollow ugc">extraction</a> with fiducials in Panoramix-Abdomen sample<br>
Curve <a href="https://disk.yandex.com/i/Y9YzUNOYHiN58A" rel="noopener nofollow ugc">extraction</a> of the right subclavian artery in CTA-cardio<br>
Curve <a href="https://disk.yandex.com/i/xmbf6mY4VIDdPw" rel="noopener nofollow ugc">extraction</a> of the left internal mammary artery in CTA-cardio</p>
<p>The third one is quite lengthy, but it shows a very challenging segmentation.</p>

---

## Post #4 by @chir.set (2021-10-24 13:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>moving them to Slicer VMTK extension</p>
</blockquote>
</aside>
<p>Thank your for considering these modules fit for inclusion in Slicer VMTK extension. That’s what I prefer indeed.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you could now get direct write access to SlicerVMTK extension</p>
</blockquote>
</aside>
<p>Thanks again for this proposal. I’ll do all necessary edits for pointing the documentation at the right place. How does the write access grant happen ? What should I wait for ? What should I do then ?</p>
<p>Regards.</p>

---

## Post #5 by @lassoan (2021-10-26 02:33 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="4" data-topic="20312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Thanks again for this proposal. I’ll do all necessary edits for pointing the documentation at the right place. How does the write access grant happen ? What should I wait for ? What should I do then ?</p>
</blockquote>
</aside>
<p>I’ve sent you an invitation to get write access (you should have received a notification but you can also click <a href="https://github.com/vmtk/SlicerExtension-VMTK/invitations">here</a> to accept it). After accepting the invitation you can commit changes directly into the SlicerExtension-VMTK repository. You can use that to add and make changes to your new modules; or make any other simple changes. If you are not sure about any change or there is something more complicated then you can create a pull request and go through the usual review process.</p>

---

## Post #6 by @chir.set (2021-10-26 07:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="20312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you are not sure about any change or there is something more complicated then you can create a pull request and go through the usual review process.</p>
</blockquote>
</aside>
<p>Thanks, I accepted the invitation and now have push access to this repo. Of course, I’ll go through PR for anything doubtful to me.</p>

---
