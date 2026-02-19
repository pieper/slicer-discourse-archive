---
topic_id: 8039
title: "Elastix Masking Registration"
date: 2019-08-15
url: https://discourse.slicer.org/t/8039
---

# Elastix masking registration

**Topic ID**: 8039
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/elastix-masking-registration/8039

---

## Post #1 by @labixin (2019-08-15 01:56 UTC)

<p>Hi all,</p>
<p>I am using Elastix to register two breast CTs. I have cropped volume to proper size and built masks to each volume. But the registration still failed indicating that “Description: itk::ERROR: AdvancedMattesMutualInformationMetric(00000000037346C0): Too many samples map outside moving image buffer: 473 / 2048”. And I am not sure about the error log messages (shown below). Could you give some advice? Your help is highly appreciated!</p>
<p>Crayon</p>
<details>
<summary>
Log</summary>
<p>bool __cdecl qSlicerSubjectHierarchyFolderPlugin::resolveHierarchies(void) : Unable to find subject hierarchy item for hierarchy node  AnnotationHierarchy_1<br>
bool __cdecl qSlicerSubjectHierarchyFolderPlugin::resolveHierarchies(void) : Unable to find subject hierarchy item for hierarchy node  AnnotationHierarchy Copy<br>
bool __cdecl qSlicerSubjectHierarchyFolderPlugin::resolveHierarchies(void) : Unable to find subject hierarchy item for hierarchy node  AnnotationHierarchy_1<br>
bool __cdecl qSlicerSubjectHierarchyFolderPlugin::resolveHierarchies(void) : Unable to find subject hierarchy item for hierarchy node  AnnotationHierarchy Copy<br>
Traceback (most recent call last):<br>
File “C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-28431/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py”, line 335, in onApplyButton<br>
forceDisplacementFieldOutputTransform = self.forceDisplacementFieldOutputChecbox.checked)<br>
File “C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-28431/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py”, line 779, in registerVolumes<br>
self.logProcessOutput(ep)<br>
File “C:/Users/Administrator/AppData/Roaming/NA-MIC/Extensions-28431/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules/Elastix.py”, line 719, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 1.</p>
</details>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/499c3167ef31f473bd4c464cb313f4cb29499b45.png" alt="01" data-base62-sha1="avbuPyYgEcKff4Wd3JerbfomXK5" width="490" height="155"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed13486f84db5a022b0467c48364411b3b9f39da.png" alt="02" data-base62-sha1="xPgtoazpYT9pA1aENUbxusurfgS" width="488" height="320"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e92cef1caec97099c04be6a5abda4698754c23b.png" data-download-href="/uploads/short-url/fMb3y3qiNiUeGQuLRRuBeBQjc8j.png?dl=1" title="03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e92cef1caec97099c04be6a5abda4698754c23b_2_690x469.png" alt="03" data-base62-sha1="fMb3y3qiNiUeGQuLRRuBeBQjc8j" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e92cef1caec97099c04be6a5abda4698754c23b_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e92cef1caec97099c04be6a5abda4698754c23b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e92cef1caec97099c04be6a5abda4698754c23b.png 2x" data-dominant-color="282929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03</span><span class="informations">875×596 84.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-08-15 02:21 UTC)

<p>This is probably the most common cause of early registration failures and discussed exhaustively in ITK and Elastix forums.</p>
<p>To give a short summary: The error occurs when random point sampling fails. It may happen if input images do not overlap enough; or if masked region is much smaller than the image. I assume your images are already pre-aligned, so most likely you have problems because of the small mask. There may be strategies to make the sampler more tolerant to small masked regions (force it to try more samples), but the most efficient solution is to crop your image so that it is not much larger than the masked area.</p>

---

## Post #3 by @labixin (2019-11-22 03:03 UTC)

<p>Hi all,</p>
<p>I am a bit confused about the ErodeMask in Elastix parameters setting. What’s the difference between “false” (serves as region of interest) and “true” (indicates which pixels are valid)? Shown below.</p>
<details>
<summary>
description</summary>
<p>// If you use a mask, this option is important.<br>
// If the mask serves as region of interest, set it to false.<br>
// If the mask indicates which pixels are valid, then set it to true.<br>
// If you do not use a mask, the option doesn’t matter.<br>
(ErodeMask “false”)</p>
</details>
<p>I need to register two images which have noncorresponding region. So I want to try the mask function. And I have made labelmap volume (outside noncorresponding region be 1 and inside be 0) both in moving and fixed images. I want to use them as mask but don’t know which setting is proper.</p>
<p>Does anyone know about the difference? Hope for some suggestions. Thanks a lot!</p>
<p>Crayon</p>

---

## Post #4 by @lassoan (2019-11-22 04:09 UTC)

<p>From the description, my understanding is that you need to set ErodeMask to false if zero mask regions should be ignored.</p>
<p>It is recommended to crop input images before registration so that they approximately covert the same region. If you don’t do it then computation time and chance that registration does not converge to the correct solution may increase significantly.</p>
<p>Masking is mainly for setting non-rectangular shaped region of interest (mask out a tool in an intra-operative image, mask out a removed tumor in a post-operative image, etc).</p>

---

## Post #5 by @labixin (2019-12-11 06:17 UTC)

<p>Thanks for your reply. Sorry but I am still stuck in setting the mask related to my problem.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f682ac4fb16fb19d0370903738ec749bcdd426b.png" data-download-href="/uploads/short-url/4tPYFlwGpayHeauJ43Xdv59tziX.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f682ac4fb16fb19d0370903738ec749bcdd426b_2_690x231.png" alt="1" data-base62-sha1="4tPYFlwGpayHeauJ43Xdv59tziX" width="690" height="231" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f682ac4fb16fb19d0370903738ec749bcdd426b_2_690x231.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f682ac4fb16fb19d0370903738ec749bcdd426b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f682ac4fb16fb19d0370903738ec749bcdd426b.png 2x" data-dominant-color="4E4F51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">795×267 93.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Left is the fixed image and I only want to focus on the breast ROI which needs to subtract (tumor+1) region for tumor resection. I need to know how the rest of the breast tissue move and determine the location of contour of tumor+2(or further) in moving image through registration. Right is the moving image. Doctors have already contoured the removed tumor region and breast ROI (although not exactly the same range as in fixed image).</p>
<p>I want to set the <em><strong>breast-(tumor+1)</strong></em> as fixed mask (=1) and parameter file “ErodeFixedMask false”. But I am not sure about the moving mask and the ErodeMovingMask setting.</p>
<p>I have tried setting <em><strong>breast-tumorbed</strong></em> (tumorbed means removed tumor region) and <em><strong>whole-tumorbed</strong></em> (which just maskout the noncorresponding tumorbed region in whole moving image) to mask (=1). And (1)when I set <em><strong>breast-tumorbed</strong></em> to mask=1, both ErodeMovingMask setting (true or false) run in error. [Description: itk::ERROR: AdvancedMattesMutualInformationMetric(00000000037437E0): Too many samples map outside moving image buffer: 0 / 34491] (2)when I set <em><strong>whole-tumorbed</strong></em> to mask=1, both setting can run without error. But “ErodeFixedMask false” setting seems not to consider my moving mask (the log file indicates that “Setting the moving masks took: 0 ms”).</p>
<p>Now I can run with fixed mask=<em><strong>breast-(tumor+1)</strong></em> (=1) and “ErodeFixedMask false”; moving mask=<em><strong>whole-tumorbed</strong></em> (=1) and “ErodeMovingMask true”. And I just don’t know the difference, especially the “true” setting. How does it consider the mask region?</p>
<p>I have looked through the elastix manual 5.4 Masks but still have no idea. The details are shown below.</p>
<details>
<summary>
Description</summary>
<p>Sometimes you are specifically interested in aligning only a part of the image. A possibility to focus on this<br>
part is to crop the image. Cropping, however, restricts the region of interest (ROI) to be a square (2D) or<br>
cube (3D) only. If you need an irregular shaped ROI, you can use masks. A mask is a binary image, filled<br>
with 0’s and 1’s. If you use a mask, you only perform registration on the part of the image that is within<br>
the masks, i.e. where the mask has 1’s.<br>
You can/should use a mask<br>
• when your image contains an artificial edge that has no real meaning. The registration might be<br>
tempted to align these artificial edges, thereby neglecting the meaningful edges. The conic beam edge<br>
in ultrasound images is an example of such an artificial edge.<br>
• when the image contains structures in the neighbourhood of your ROI that may influence the registration<br>
within your ROI. This is for example the case when matching lung data. Usually, you are<br>
interested in the lungs, and not if the rib cage is well aligned. However, the ribs are structures that<br>
for example in CT can have a strong influence on the similarity metric, especially if you use the MSD<br>
metric. In that case, the rib cage may be well aligned at the cost of vessels structures near the border<br>
of the lung with the rib cage. In this case it will help you if you use a dilated lung segmentation as a<br>
mask.<br>
Masks can be used both for the fixed and the moving image. A fixed image mask is sufficient to focus<br>
the registration on a ROI, since samples are drawn from the fixed image. You only want to use a mask for<br>
the moving image when your moving image contains nonsense grey values near the ROI.<br>
In case you are using a mask to prevent bad karma from an artificial edge, you also need to set the<br>
parameter:<br>
(ErodeMask “true”)<br>
If not, then when performing multi-resolution, information from the artificial edge will flow into you ROI<br>
due to the smoothing step. In case the edge around your ROI is meaningful, e.g. in the lung example, you<br>
should set it to false, because this edge will help to guide the registration.<br>
A common exception that elastix throws when drawing samples is: “Could not find enough image<br>
samples within reasonable time. Probably the mask is too small.” The probable cause for this is that your<br>
fixed image mask is too small. See the FAQ for more information.</p>
</details>
<p>Do you have any suggestions about my case? Your help is highly appreciated.</p>
<p>Crayon</p>

---

## Post #6 by @labixin (2019-12-11 08:12 UTC)

<p>I have looked through the <a href="https://github.com/SuperElastix/elastix/wiki/FAQ" rel="nofollow noopener">Elastix FAQ</a> about the common cause of registration failures (for example “Too many samples map outside moving image buffer”). I think the error mentioned above is mainly caused by not overlapping enough.</p>
<p>But I wonder if I can run three kinds of registration in one time (set rigid &amp; affine &amp; b-spline registration within one parameter file). Am I supposed to run rigid/affine registration and also crop in advance? The reason that I don’t want to register pre-aligned moving image to fixed image is that I need to double check the contour which is used for mask in pre-aligned moving image (there may be some inconsistence after transformation and resampling). So what I try now is to set proper mask both in fixed and moving image and run the parameter file in one time.</p>
<p>Is there anything unreasonable? How can I improve my registration? Hope for some advice. Thank you very much.</p>
<p>Crayon</p>

---

## Post #7 by @lassoan (2019-12-11 13:41 UTC)

<aside class="quote no-group" data-username="labixin" data-post="6" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I wonder if I can run three kinds of registration in one time (set rigid &amp; affine &amp; b-spline registration within one parameter file)</p>
</blockquote>
</aside>
<p>Yes, you can define multiple stages in your <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Resources/RegistrationParameters/ElastixParameterSetDatabase.xml">ParameterSetDatabase.xml</a>, each defined by a separate parameter file.</p>
<aside class="quote no-group" data-username="labixin" data-post="6" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Am I supposed to run rigid/affine registration and also crop in advance?</p>
</blockquote>
</aside>
<p>I would try cropping and manual rigid alignment. You may find it is easier to do manual alignment by identifying pairs of matching anatomical landmarks and computing transform using Fiducial Registration Wizard in SlicerIGT extension. You may also try warping transform of Fiducial Registration Wizard module to register the deformed breast, just to get an approximate idea about the complexity of the displacement field.</p>
<aside class="quote no-group" data-username="labixin" data-post="6" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Is there anything unreasonable? How can I improve my registration?</p>
</blockquote>
</aside>
<p>Breast registration is known to be a hard problem because there can be a lot of displacement and deformation. You may get ideas for the registration from parameter sets and publications listed at <a href="http://elastix.bigr.nl/wiki/index.php/Parameter_file_database">http://elastix.bigr.nl/wiki/index.php/Parameter_file_database</a>.</p>

---

## Post #8 by @labixin (2019-12-31 02:21 UTC)

<p>Thank you for your reply. I have tried Fiducial registration wizard but I wonder how to computes TRE (as RMS of the distance between fixed points and transformed moving points) using the transform computed by Elastix? Not just rigid/similarity/warping transform as the module provided? I couldn’t find the settings.<br>
I have defined 17 pairs of corresponding points both in fixed and moving image. The pictures are shown below. Hope for some advice.<br>
Besides, could you please post some links of Elastix forum? Thanks a lot!</p>
<p>Crayon</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a68ddc36231f0fcd0dfa3d21bf5a96d71762cee.png" alt="post" data-base62-sha1="63aJb5hwJurxV0FXRc34Ygc8oFw" width="496" height="465"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1db7d2ee7a81a2cb51dec13365572f04d417478b.png" alt="post2" data-base62-sha1="4eTGDisKET54Y0Nbx0JoatBxJvJ" width="497" height="139"></p>

---

## Post #9 by @lassoan (2019-12-31 03:38 UTC)

<aside class="quote no-group" data-username="labixin" data-post="8" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I wonder how to computes TRE (as RMS of the distance between fixed points and transformed moving points)</p>
</blockquote>
</aside>
<p>The error that Fiducial registration wizard displays is the residual error and is computed as the RMS of the distances between each fixed point and corresponding transformed moving point.</p>
<p>Landmark registration (by Fiducial registration wizard, etc.) is an alternative to intensity-based registration (by Elastix, etc.). You use one or the other, or sometimes you do an approximate rigid landmark registration to prealign images before intensity-based registration.</p>
<aside class="quote no-group" data-username="labixin" data-post="8" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>could you please post some links of Elastix forum?</p>
</blockquote>
</aside>
<p><a href="https://groups.google.com/forum/#!forum/elastix-imageregistration" class="onebox" target="_blank" rel="noopener">https://groups.google.com/forum/#!forum/elastix-imageregistration</a></p>

---

## Post #10 by @labixin (2020-01-02 10:26 UTC)

<p>Thanks for your explanation. I have tried Fiducial registration wizard (warping transform) to get an approximate prealignment of specific points before intensity-based registration (by Elastix) and indeed got a better result. But after intensity-based registration, the pre-aligned points (done by fiducial registration) have been pulled away again. Now I want to try a metric “CorrespondingPointsEuclideanDistanceMetric” which help minimize the distance of two point sets with known correspondence (the explanation is attached in the bottom).</p>
<p>I have searched the elastix forum and found the <a href="https://groups.google.com/forum/#!searchin/elastix-imageregistration/CorrespondingPointsEuclideanDistanceMetric/elastix-imageregistration/qtSDYtvK7_4/SkhRA4mHDgAJ" rel="noopener nofollow ugc">source code links</a>. Now I have annotated 50 pairs of corresponding points in Markup module. I wonder how to specify them as elastix input? Something like the mask input?</p>
<p>Could you give some suggestions? Thank a lot!</p>
<p>Crayon</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d37219303a36a17a72ba2b19b750a6ec76eb0f13.png" data-download-href="/uploads/short-url/uaxcsqdUjWO6lvmwduMMy2572fh.png?dl=1" title="P1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d37219303a36a17a72ba2b19b750a6ec76eb0f13.png" alt="P1" data-base62-sha1="uaxcsqdUjWO6lvmwduMMy2572fh" width="690" height="340" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">P1</span><span class="informations">915×451 8.99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2020-01-02 15:52 UTC)

<aside class="quote no-group" data-username="labixin" data-post="10" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I have tried Fiducial registration wizard (warping transform) to get an approximate prealignment of specific points before intensity-based registration</p>
</blockquote>
</aside>
<p>If you want to use landmark registration for initial alignment, then do not use warping transform, just rigid transform. Warping would provide the full registration (you don’t need to do any additional intensity-based image registration).</p>
<aside class="quote no-group" data-username="labixin" data-post="10" data-topic="8039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Now I have annotated 50 pairs of corresponding points in Markup module</p>
</blockquote>
</aside>
<p>If these landmarks are accurate and reliable enough then probably you can register the images based on these landmarks alone (no need for Elastix).</p>
<p>If you still want to use combined landmark+intensity-based registration in Elastix then you need to slightly modify SlicerElastix Python scripts to pass markup fiducial point coordinates to Elastix. Earlier <a class="mention" href="/u/stephan">@stephan</a> made a try to implement this - see this <a href="https://github.com/lassoan/SlicerElastix/pull/11/files">pull request</a>. You can try and test and update this pull request as needed and let us know how it works.</p>

---

## Post #12 by @tenzin_kunkyab (2024-10-25 14:45 UTC)

<p>Hi Andras,</p>
<p>The parameterSetDatabase.xml is quite useful! I wanted to ask do you have a parameter file like this for CT to CBCT registration for prostate cases? or do you recommend one of those files in the link?</p>
<p>The prostate deformation looks pretty good visually but a little larger organ such as bladder doesn’t look too similar to the target (CBCT) after registration with elastix.</p>
<p>Thanks!</p>

---

## Post #13 by @lassoan (2024-10-25 14:51 UTC)

<p>You can check latest parameter sets on ElastiX websites and ask on the <a href="https://github.com/SuperElastix/elastix/discussions">ElastiX forum</a>, but you can also just edit the parameter files and see if you can get improvements.</p>

---
