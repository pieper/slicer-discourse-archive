---
topic_id: 12045
title: "Post Processing Of Brain Vessel Models"
date: 2020-06-15
url: https://discourse.slicer.org/t/12045
---

# Post-processing of brain vessel models

**Topic ID**: 12045
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/post-processing-of-brain-vessel-models/12045

---

## Post #1 by @Andreas (2020-06-15 21:24 UTC)

<p>I still have questions about post-processing of brain vessel models:</p>
<p>1.) Is it more advantageous to use first the smoothing function for post-processing the vessel models in order to improve the vessel lumen and thus the flow rate?</p>
<p>Or it is better to add the vessel wall (hollow) first and then to process the vessel with the smoothing function</p>
<p>2.) Which smoothing function is recommended for very small (brain) vessels?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d4923a40f0508e15d904cba7138f7727a3cbeb0.jpeg" alt="Smoothing" data-base62-sha1="1TwUfbygnnsTY4f3WuNoP8IHgu4" width="553" height="332"></p>
<p>3.)Can you recommend other post-processing tools?</p>
<p>4.)In my patient-specific vessel model, only the “trunk” and the main branches are important for the later training model.<br>
Is there an elegant way to remove the small branches? I mostly use the ‘’ scissors ‘’ function which is very time consuming and cumbersome. In addition, it is hardly reproducible.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6709bd83ae989b25ac240cc29f4dd3ce9b732583.jpeg" data-download-href="/uploads/short-url/eHw2YfF9msJNQz0HafEhAuu6pMf.jpeg?dl=1" title="before and after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6709bd83ae989b25ac240cc29f4dd3ce9b732583_2_690x270.jpeg" alt="before and after" data-base62-sha1="eHw2YfF9msJNQz0HafEhAuu6pMf" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6709bd83ae989b25ac240cc29f4dd3ce9b732583_2_690x270.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6709bd83ae989b25ac240cc29f4dd3ce9b732583_2_1035x405.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6709bd83ae989b25ac240cc29f4dd3ce9b732583.jpeg 2x" data-dominant-color="9F96C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before and after</span><span class="informations">1152×452 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>With best regards</p>

---

## Post #2 by @lassoan (2020-06-16 04:17 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Is it more advantageous to use first the smoothing function for post-processing the vessel models in order to improve the vessel lumen and thus the flow rate?</p>
</blockquote>
</aside>
<p>If the segmented vessel contains small holes or extrusions then smoothing can help.</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Or it is better to add the vessel wall (hollow) first and then to process the vessel with the smoothing function</p>
</blockquote>
</aside>
<p>It depends. What is the purpose of your project? 3D printing, computational fluid dynamics analysis, intervention planning, creation of educational models, …?</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Which smoothing function is recommended for very small (brain) vessels?</p>
</blockquote>
</aside>
<p>It depends what kind of errors your segmentation has. For removing small holes and removing small extrusions in a single segment, I would recommend median filtering.</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Can you recommend other post-processing tools?</p>
</blockquote>
</aside>
<p>Yes. For this, it is necessary to see examples images and segmentations and know what you are trying to achieve.</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Is there an elegant way to remove the small branches?</p>
</blockquote>
</aside>
<p>Probably the simplest is to make small cuts with Scissors effect then use Islands effect’s Keep largest island method to remove the cut-off branches.</p>
<p>It could be also possible to enhance Slicer-VMTK extension’s centerline extraction module to allow specifying branch end points. This could save 1-2 minutes per segmentation, but the effort to implement this would probably only pay off if you processed hundreds of cases. Nevertheless, it is a Python scripted module, so you can give it a try to make this improvement.</p>

---

## Post #3 by @Andreas (2020-06-28 17:42 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Or it is better to add the vessel wall (hollow) first and then to process the vessel with the smoothing function</p>
</blockquote>
</aside>
<p>It depends. What is the purpose of your project? 3D printing, computational fluid dynamics analysis, intervention planning, creation of educational models, …?</p>
<p>My project is defined as follows:</p>
<p>Stents are often used to treat vascular diseases in the brain or heart. These are to be examined for their mechanical and fluid dynamic behavior before their clinical application. <strong>Vessel models</strong> made of visible <strong>polymers</strong> are used, which are produced <strong>on the</strong> <strong>basis of patient-specific anatomy in 3D printing</strong> . The aim of the work is the conception, realization and investigation of a process for the production of synthetic vessel models with physiological true mechanical properties. In a final investigation, the manufactured <strong>vessel models are tested for their mechanical and fluid dynamic properties</strong> . (no computer-aided analysis)</p>

---

## Post #4 by @lassoan (2020-07-01 00:37 UTC)

<p>For flow testing, the highest priority is to have accurate vessel lumen geometry. A good workflow can be:</p>
<ul>
<li>Import vascular CT or CBCT</li>
<li>Crop and resample the image. Choose spacing value that is at least 4-6x smaller than the minimum vessel diameter that you want to segment and at least a few times smaller than the thinnest wall thickness you want to print.</li>
<li>Segment the vessel lumen using Segment Editor module</li>
<li>Cut off branches and smooth the segment as needed. It is very easy and quick to remove branches if you just snip them where they originate and then delete them using Islands effect / Keep largest island.</li>
<li>Use hollow effect in “Use current segment as inside surface” mode.</li>
</ul>
<p>In theory, shell thickness would be determined from patient’s vessel wall thickness. However, in practice, most likely wall thickness will be entirely dictated by your 3D printer’s minimum wall thickness and properties of the printing material: you will have to use the thinnest wall that you can print that is still mechanically strong enough so it does not tear or leaks too easily. Start experimenting with different printers, materials, and wall thicknesses early on, to make sure you don’t spend time with trying to determine parameters (wall thickness, printing material properties) that are not feasible anyway.</p>
<p>VMTK extension’s Extract centerline can be used to create centerline tree where only a few selected branches are kept, but about 20-30 lines of code would need to be added to the module that would generate a model from that trimmed centerline that can be used as a mask to remove unselected branches. Probably we will add this feature to the module at some point but if you need it earlier then you should be able to add it, too.</p>

---

## Post #5 by @Deepa (2020-07-01 03:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Extract centerline can be used to create centerline tree where only a few selected branches are kept, but about 20-30 lines of code would need to be added to the module that would generate a model from that trimmed centerline that can be used as a mask to remove unselected branches</p>
</blockquote>
</aside>
<p>That will be a really nice feature</p>

---

## Post #6 by @Andreas (2020-07-12 20:09 UTC)

<p>I have another question about the Threshold Range:</p>
<p>Do you leave the minimum at the standard value of 99.00 or do you have to click on “Set” and take the determined value to get the optimal threshold range? (see figure Threshold Range)</p>
<p>In your opinion, is “Otsu” the best method for calculating threshold values when using CT images with contrast medium (brain vessels)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f98ae2c346a44a7eeb6e11f4051b93a28723f96e.jpeg" data-download-href="/uploads/short-url/zByrZRY7Smupf8rIrTFW5K25pn0.jpeg?dl=1" title="Threshold Range" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f98ae2c346a44a7eeb6e11f4051b93a28723f96e_2_690x119.jpeg" alt="Threshold Range" data-base62-sha1="zByrZRY7Smupf8rIrTFW5K25pn0" width="690" height="119" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f98ae2c346a44a7eeb6e11f4051b93a28723f96e_2_690x119.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f98ae2c346a44a7eeb6e11f4051b93a28723f96e_2_1035x178.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f98ae2c346a44a7eeb6e11f4051b93a28723f96e.jpeg 2x" data-dominant-color="F0F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Threshold Range</span><span class="informations">1134×196 46.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My next question is about smoothing:<br>
For the smoothing tools, I mostly only use the median function (see illustration smoothing), because I find that this function changes the least in the actual geometry. Is there a certain guideline value for the kernel size or for the pixels with which an optimal result can be achieved? (e.g. everything in the pixel area: 3x3x3 pixels).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/998929d269df7e446fa5fefa5e93759a2ee30bbd.jpeg" alt="smoothing" data-base62-sha1="lUeVinIySzMc0MDMlLvkoC8YRBj" width="524" height="105"></p>

---

## Post #7 by @lassoan (2020-07-13 18:58 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="6" data-topic="12045">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>In your opinion, is “Otsu” the best method for calculating threshold values when using CT images with contrast medium (brain vessels)?</p>
</blockquote>
</aside>
<p>There are several classes of voxels in contrasted CT images (air, various soft tissues, bones, contrast agent), so I don’t think Otsu’s method would be ideal (or even picked up the threshold between contrast agent and background if you use the whole image as input).</p>
<p>Since contrast filling may be uneven and smaller vessels may have lower density due to a number of reasons, and contrasted vessels may have similar density as bones, a simple global thresholding method usually does not produce very good results.</p>
<p>Instead, I would recommend local threshold effect, which can compute a local histogram to help you with optimal threshold selection and then uses intensity difference based region growing for extracting vessels. See tutorial here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="caEuwJ7pCWs" data-video-title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=caEuwJ7pCWs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/caEuwJ7pCWs/maxresdefault.jpg" title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" width="" height="">
  </a>
</div>


---
