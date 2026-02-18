# Interactive lobe segmentation with one lobe missing

**Topic ID**: 17296
**Date**: 2021-04-24
**URL**: https://discourse.slicer.org/t/interactive-lobe-segmentation-with-one-lobe-missing/17296

---

## Post #1 by @Tibor_Krajc (2021-04-24 11:16 UTC)

<p>Hi, I am comparing lung lobe volumes before and after anatomical resection to evaluate the influence of new spatial configuration of the remaining lobes on their volume. This is planned for multiple patients and optimally should require as little manual input as possible.</p>
<p>When trying to perform interactive lobe segmentation after right upper lobe lobectomy, the horizontal fissure cannot be defined, and yet fiducials are required for the segmentation to start.</p>
<p>Placing these fiducials on the upper surface of the middle lobe or inside the middle lobe leads to a misbehaving app: no lobe or airway segmentations are created and colored, and their representations in Segmentations module are not present, even though no error message appears after “completing” the segmentation. Therefore conversion to segment node or creation of closed surface are not possible, hence no segment statistics are available.</p>
<p>In addition to this, the red slice shows the last visible ct image only, which stays fixed despite scrolling, which affects only the fiducials.</p>
<p>Is there any reproducible way to tackle this problem in a semi-automated way?</p>

---

## Post #2 by @lassoan (2021-04-25 13:32 UTC)

<p>What extension/module do you use for live segmentation?</p>
<p>How many cases have missing lobes? (if there are not tooany data sets then it may be less overall effort to use a more manual workflow using general Segment Editor tools than creating or modifying automated tools)</p>

---

## Post #3 by @Tibor_Krajc (2021-04-25 14:16 UTC)

<p>Hi Andras,<br>
I am using Chest Imaging Platform’s Interactive Lobe Segmentation module to define the fissures and segment individual lobes as shown in one of your tutorials.</p>
<p>Alas, all (~200) cases are missing at least one lobe - the purpose of the analysis is to find out how reliable is our current prediction of actual lung volume loss based on arbitrarily assigned fractions (No. of remaining segments divided by No. of all preoperatively present segments) and whether it can be improved by using CT-volumetry.</p>
<p>I did try using Grow Seeds with 3 different segments for airway, lung and other tissue, but that turned out to be tricky due to high similarity of emphysematous lung and residual air in the pleural cavity - there were just too many “leaks” that needed manual repairing and the result was unsatisfactory. In the end I resorted to setting a threshold mask in Segment Editor and manual painting slice by slice which wass quite time-consuming.</p>
<p>Also, I suspect I will never be able to achieve comparable results by performing the preoperative segmentation algorithmically (Interactive Lobe Segmentation) and the postoperative one manually.</p>
<p>I was wondering if there is a way to mimic what Interactive Lobe Segmentation module does by performing its partial tasks “manually” by using a sequence of modules included in the Toolkit of Chest Imaging Platform.</p>
<p>Thank you for your kind help.</p>

---

## Post #4 by @rbumm (2021-04-25 19:20 UTC)

<p>Have you tried the LungCTSegmenter followed by the LungCTAnalyzer ?<br>
Both are now part of the Chest imaging suite, relatively easy to operate, and should give you reliable lung (not lobe) volumes, even with infiltrations, collapse, and emphysema.</p>
<p>Regards<br>
Rudolf</p>

---

## Post #5 by @lassoan (2021-04-26 14:01 UTC)

<p>You can get left/right lung segmentation in about 1 minute using LungCTSegmenter as recommended by <a class="mention" href="/u/rbumm">@rbumm</a>.</p>
<p>After that you can set masking settings to restrict painting inside segments, paint a segment with a very large brush on a couple of slices and create full segmentation by activating “Fill between slices” effect or “Grow from seeds” effect. The former does not rely on image contrast at all, so it works regardless how well the lobe boundaries are visible (as long as you can see them), but it may require painting on more slices. I would recommend to segment 4-5 images with both methods and see which one takes less time in the end.</p>
<p>See a tutorial on how to use Fill between slices effect for lobe segmentation here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cplH8cvAB8s" data-video-title="Organ segmentation 3.1 : Lungs, lobes, volumetry" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cplH8cvAB8s" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cplH8cvAB8s/maxresdefault.jpg" title="Organ segmentation 3.1 : Lungs, lobes, volumetry" width="" height="">
  </a>
</div>

<p>You could also draw fissure surfaces manually by defining the fissure surface boundary by a closed curve (using Valve View module in SlicerHeart extension can help with quickly defining this curve) and then generate a surface from it (using Baffle Planner module in SlicerHeart extension). Then you can import the baffle surface to a segmentation and use that to partition the segmentation (using Islands effect). However, most likely this workflow would take more time than a simple Fill between slices based segmentation.</p>
<p>I would expect that segmenting one lung should not take more than 5-10 minutes, which means you can segment 200 images in 2-4 full days. If segmentation takes 3 minutes using the Interactive Lobe Segmentation module then it means you can segment 200 images in 1-2 days. Most likely it would take much longer for you to find a developer who could dig into the Interactive lobe segmentation module (and make it possible to use on your special images) than those few extra days that the more manual segmentation workflow takes.</p>
<p><a class="mention" href="/u/raul">@raul</a> Is there a chance that someone from your team could look into testing Interactive lobe segmentation module with resected lungs?</p>

---

## Post #6 by @Tibor_Krajc (2021-05-02 16:08 UTC)

<p>Thank you for your swift advice, Rudolf, I have seen your video tutorials before and it works beautifully and very fast when there is no residual intrapleural air and no chest tubes.</p>
<p>Alas, in the particular case that I’m stuck with now, I always ended up getting hairy (with lots of weird leaks) models of the non-operated side, and the operated lung fused with intrapleural air as well as air outside of patient (due to continuous contact via chest tubes). The latter could be solved by using island effects but I was unable to get such nice segmentations as preoperatively. The slices are 1 mm thick and the quality of the dicom images is very good, there is no soft tissue emphysema…perhaps it’s just this particular series.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb4d9a452c1a9c322a361544f7c6624be41e01f7.jpeg" data-download-href="/uploads/short-url/xzAt2wiKMhnvRtIHbBzf3uxli3d.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb4d9a452c1a9c322a361544f7c6624be41e01f7_2_667x500.jpeg" alt="image" data-base62-sha1="xzAt2wiKMhnvRtIHbBzf3uxli3d" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb4d9a452c1a9c322a361544f7c6624be41e01f7_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb4d9a452c1a9c322a361544f7c6624be41e01f7_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb4d9a452c1a9c322a361544f7c6624be41e01f7.jpeg 2x" data-dominant-color="49484B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1196×896 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Tibor_Krajc (2021-05-02 16:27 UTC)

<p>Thank you, Andras, amazing how quickly you always respond. Thanks for the link to the excellent tutorial on filling between slices, I did watch it before but did not pay attention closely enough to notice all the steps.<br>
Following the tutorial I was able to get a smooth model of both lungs, however, the residual space filled with air became a part of the right lung.<br>
I have tried using a different threshold mask in order to later on subtract the thus created air segmentation from the “lung” model, but stumbled upon the problematic distinction between air and emphysematous lung, again.</p>
<p>I have yet to try the baffle planner some more, so far I have not succeeded to create a closed “pseudospherical” surface with convex and concave areas when trying to mark the surface of the lobe surrounded by air - probably because the baffle planner is designed to create a cutout of curved surface, and not a closed one.<br>
I have also looked into using Markups To Model from IGT but failed to understand how to define a group of fiducials that could be used to create a surface model. With Surface Cut from the Extras it was possible to segment the desired lobe partly surrounded by air but with higher number of fiducials the defining polygonal line became quite alive and sometimes unpredictable.</p>
<p>Reproducibility and equivalence of the methods used for preoperative (all lobes present) and postoperative (one or more lobes missing) volumetry are important in order to provide some degree of independence on operator input, we don’t really worry that much about time spent segmenting. However, even if all was done manually, there is risk of operator dependent bias. That’s why I am trying to find as uniform a way as possible.</p>
<p>I have noticed in the “Segment Lung Lobes” (CIP → Toolkit → Segmentation → Segment Lung Lobes) that additional information can be provided via “Region and type points file” to form a full set of points along the lobe boundaries. Would these apply to the surface of the lung bordering on intrapleural air and not the neighboring lobe? And if so, how can I feed it to the sub-module?</p>
<p>Thank you for your support!</p>

---

## Post #8 by @rbumm (2021-05-02 16:46 UTC)

<p>The Lung CT Segmenter has an additional lung intensity range slider (usually hidden in “Advanced”).<br>
After placing your fiducials, but before pressing “Apply”, you may want to move the right (upper range) slider a little  left in that particular case.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d070b218bff97c27276f2af9ca8a3076939457.png" alt="image" data-base62-sha1="wN1V9y7ggSMNOfT4oqh6iRJXVrh" width="541" height="483"></p>
<p>Try -250 and press “Update”. If your are satisfied with the preview, press “Apply”.</p>
<p>If there is still a problem with that case you could anonymize the CT data (save it as nrrd file)  and send me a download link. I´ll be happy to test it out …</p>

---

## Post #9 by @Tibor_Krajc (2021-05-02 17:45 UTC)

<p>Sorry Rudolf, even after fine-tuning my result is not so nice.<br>
Would you mind trying it out?<br>
the file should be in this folder&gt;<br>
<a href="https://1drv.ms/u/s!AqzfnkdqZokWhvw6w38MRFlUjVLe_Q?e=L9t5Xj" class="onebox" target="_blank" rel="noopener nofollow ugc">https://1drv.ms/u/s!AqzfnkdqZokWhvw6w38MRFlUjVLe_Q?e=L9t5Xj</a><br>
Thanks a lot!</p>

---

## Post #10 by @rbumm (2021-05-02 18:32 UTC)

<p>That is a difficult but interesting case for segmentation.</p>
<p>The problems seem to be</p>
<p>(a) partial inflation / remaining pneumothorax after right upper lobectomy<br>
(b) subcutaneous soft tissue emphysema<br>
(c) noisy data set</p>
<p>I set the lung intensity sliders to -1500 and -370, but there was still a segmentation leak from the right lung to → subcutaneous to → air surrounding patient.</p>
<p>So I had to place some “Other” fiducials (outside of patient and subcutaneous) until I got:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06bf977e232ac6a3b6368a3b18649a378e3e20f6.jpeg" data-download-href="/uploads/short-url/XHlAQ5r4n7wm9wkc2a1YFuJY4S.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06bf977e232ac6a3b6368a3b18649a378e3e20f6_2_690x317.jpeg" alt="image" data-base62-sha1="XHlAQ5r4n7wm9wkc2a1YFuJY4S" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06bf977e232ac6a3b6368a3b18649a378e3e20f6_2_690x317.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06bf977e232ac6a3b6368a3b18649a378e3e20f6_2_1035x475.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06bf977e232ac6a3b6368a3b18649a378e3e20f6_2_1380x634.jpeg 2x" data-dominant-color="99999C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×874 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
