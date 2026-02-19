---
topic_id: 11830
title: "Wall Thickness Measurements Of Intracranial Arteries"
date: 2020-06-02
url: https://discourse.slicer.org/t/11830
---

# wall thickness measurements of intracranial arteries

**Topic ID**: 11830
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/wall-thickness-measurements-of-intracranial-arteries/11830

---

## Post #1 by @Andreas (2020-06-02 16:04 UTC)

<p>Hello everyone,</p>
<p>I would like to know whether it is possible to use CT images of brain vessels (contrast medium) to determine the respective patient-specific wall thickness of the vessels - see figure.<br>
I assume that the dark red border represents the vessel wall.</p>
<p>I have another question about the hollow function.</p>
<p>Which surface (inside, medial, outside) do I have to choose to get the patient-specific anatomy? In the 3D model shown, is that the total diameter of the vessel or just the inner diameter? (shown in red)</p>
<p>Many thanks for your help</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f66f72fd34d50fb2d0e8ea969759764d1ef05b7.jpeg" alt="wall thickness" data-base62-sha1="ib3eYdgzM9XxIUhzJ4Z3ffJc3R5" width="181" height="187"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd6120b1e81f2d4e72f8e36d275529bed57f15c8.jpeg" alt="hollow" data-base62-sha1="tiRYy5JxniIncoYqX7nlsG1VPa8" width="584" height="224"></p>

---

## Post #2 by @lassoan (2020-06-03 01:16 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>I would like to know whether it is possible to use CT images of brain vessels (contrast medium) to determine the respective patient-specific wall thickness of the vessels</p>
</blockquote>
</aside>
<p>I would expect this to be very challenging in live humans, due to lack of contrast between the vessel wall and surrounding soft tissues (the contrast agent does not enhance healthy vessel wall), and relatively low spatial resolution (in commonly used CT brain imaging protocols voxel size is several tenth of a millimeter, which is about the same size or larger than vessel wall thickness). Maybe you can see something around very large vessels, but even then you might not be able to reliably tell where the vessel wall begins and ends. For more reliable, accurate measurement you probably need to use MRI with a protocol that is specifically developed for wall thickness measurement.</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Which surface (inside, medial, outside) do I have to choose to get the patient-specific anatomy? In the 3D model shown, is that the total diameter of the vessel or just the inner diameter?</p>
</blockquote>
</aside>
<p>Contrast agent fills the vessel lumen, so you what you get is the inner diameter. Choose “use current segment as <em>inside surface</em>”.</p>

---

## Post #3 by @Andreas (2020-06-03 12:52 UTC)

<p>Thank you for answering my request.</p>
<p>I’m still not quite sure whether the dark red area really belongs to the inside diameter, because it looks to me as if it were already the wall of the vessel?</p>
<p>Unfortunately, I can only use CT data in my work and no MRI data. Should I then go to the scientific database (Reference values). What would you recommend?</p>
<p>thanks in advance</p>

---

## Post #4 by @lassoan (2020-06-03 21:54 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="3" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>I’m still not quite sure whether the dark red area really belongs to the inside diameter, because it looks to me as if it were already the wall of the vessel?</p>
</blockquote>
</aside>
<p>The attached image is very low quality (it looks like a photo of a screen), so I cannot tell what is on it, but we know for sure that the contrast agent only fills the vessel lumen, as it replaces the blood and does not perfuse healthy vessel walls.</p>
<aside class="quote no-group" data-username="Andreas" data-post="3" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>I can only use CT data in my work and no MRI data. Should I then go to the scientific database (Reference values). What would you recommend?</p>
</blockquote>
</aside>
<p>Unless you have very high resolution and low noise CT images then it is unlikely that you can measure vessel wall thickness. Depending on what you want to do, you may use some general values you find in the literature instead of patient-specific values. You may have other constraints, too, for example if you want to 3D-print a model then most likely the wall thickness will be dictated by the minimum wall thickness that your printer supports.</p>

---

## Post #5 by @Andreas (2020-06-15 20:14 UTC)

<p>Hello Mr. Lasso,</p>
<p>Thanks again for your help.</p>
<p>I still have questions about the limitation of the wall thickness and the dimension of the brain vessel:</p>
<p>1.) In the literature I found a study to measure wall thickness using MRI. For example, the basilar artery has a wall thickness between 0.38 mm and 0.73 mm. However, with 3D Slicer I cannot choose a wall thickness smaller than 0.75 mm (inside surface), because all dimensions below are rejected as too thin. (see attachment ‘‘too thin’’)</p>
<p>What does this limit depend on? Can the program determine the actual wall thickness based on the respective vessel volume?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f65d7b00d40127eb86077471b37bd71337b63b4.jpeg" data-download-href="/uploads/short-url/fTtc8MMA8gNTEVaVGkHc2zABGwk.jpeg?dl=1" title="too thin" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f65d7b00d40127eb86077471b37bd71337b63b4_2_690x414.jpeg" alt="too thin" data-base62-sha1="fTtc8MMA8gNTEVaVGkHc2zABGwk" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f65d7b00d40127eb86077471b37bd71337b63b4_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f65d7b00d40127eb86077471b37bd71337b63b4_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f65d7b00d40127eb86077471b37bd71337b63b4_2_1380x828.jpeg 2x" data-dominant-color="909097"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">too thin</span><span class="informations">1680×1010 489 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>2.) Since I would later like to print patient-specific brain vessel models based on CT images using the SLA method, I need to know whether the dimensions of the printed model correspond 1: 1 to the CT image or whether there are any deviations.<br>
This applies in particular to the volume of individual vessel sections.</p>
<p>Is there a suitable module for measuring the volume?<br>
The ‘’ Ruler ‘’ function is too imprecise for this, and you cannot get to all places, e.g. the aneurysm. (see attachment ‘‘Ruler’’)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ca50c9146b7a7ce715ca7a251f550c043d22cdf.jpeg" data-download-href="/uploads/short-url/k4csDAl18exipHNmHHT5wJglhTh.jpeg?dl=1" title="Ruler" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ca50c9146b7a7ce715ca7a251f550c043d22cdf_2_690x415.jpeg" alt="Ruler" data-base62-sha1="k4csDAl18exipHNmHHT5wJglhTh" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ca50c9146b7a7ce715ca7a251f550c043d22cdf_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ca50c9146b7a7ce715ca7a251f550c043d22cdf_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ca50c9146b7a7ce715ca7a251f550c043d22cdf_2_1380x830.jpeg 2x" data-dominant-color="908F95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ruler</span><span class="informations">1678×1010 520 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>3.) This question is a bit complicated to formulate and I hope you will understand my problem.</p>
<p>For this I have inserted screenshots from the systems mentioned above.<br>
Goal: Measure the lumen.<br>
Question: Do I first have to wrap the vessel wall around the volume in the thickness I have chosen and then remove the contrast medium shown so that a cavity is created? (see attachment Volume or Hollow)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7adea3e48aec9fcfbde8360776a908fd779baef2.jpeg" data-download-href="/uploads/short-url/hwXfRqX138LVynIsZ4gKLGIiiky.jpeg?dl=1" title="Volume or Hollow" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7adea3e48aec9fcfbde8360776a908fd779baef2_2_690x270.jpeg" alt="Volume or Hollow" data-base62-sha1="hwXfRqX138LVynIsZ4gKLGIiiky" width="690" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7adea3e48aec9fcfbde8360776a908fd779baef2_2_690x270.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7adea3e48aec9fcfbde8360776a908fd779baef2_2_1035x405.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7adea3e48aec9fcfbde8360776a908fd779baef2.jpeg 2x" data-dominant-color="484948"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Volume or Hollow</span><span class="informations">1141×448 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Sincerely yours</p>

---

## Post #6 by @lassoan (2020-06-16 05:03 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="5" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>However, with 3D Slicer I cannot choose a wall thickness smaller than 0.75 mm (inside surface)</p>
</blockquote>
</aside>
<p>The smallest unit in a segmentation is a single voxel. If you want to represent thinner structures than that then you need to oversample the segmentation as described <a href="https://discourse.slicer.org/t/update-oversampling-factor/11717/4">here</a>.</p>
<aside class="quote no-group" data-username="Andreas" data-post="5" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>I need to know whether the dimensions of the printed model correspond 1: 1 to the CT image or whether there are any deviations.</p>
</blockquote>
</aside>
<p>3D-printed model size will very accurately match the true size of the anatomy. Precision is limited by layer thickness and minimum wall thickness of your printer; and resolution (voxel size) of your segmentation.</p>
<aside class="quote no-group" data-username="Andreas" data-post="5" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Is there a suitable module for measuring the volume?</p>
</blockquote>
</aside>
<p>You can measure volume of segments using Segment statistics module.</p>
<aside class="quote no-group" data-username="Andreas" data-post="5" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>For this I have inserted screenshots from the systems mentioned above.<br>
Goal: Measure the lumen.<br>
Question: Do I first have to wrap the vessel wall around the volume in the thickness I have chosen and then remove the contrast medium shown so that a cavity is created? (see attachment Volume or Hollow)</p>
</blockquote>
</aside>
<p>First of all, the image above is so low quality (bright areas are oversaturated, noise is overamplified) that your error is expected to be high. If it is not just an incorrect window/level (see how to adjust it <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level">here</a>) then you may consider trying to obtain better quality images.</p>
<p>If you want to measure vessel diameter at only a few places then find those places, zoom in, and measure distances using Markups line or Annotation ruler tools. There is no need to segment the images, just look at the images and determine where the boundaries of the vessels are, based on your expert judgement. If you want to measure vessel lumen radius across the entire vessel tree then you can use SlicerVMTK extension’s Centerline extraction module (it requires segmentation of the vessel tree as input).</p>

---

## Post #7 by @Andreas (2020-06-28 17:48 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="5" data-topic="11830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Is there a suitable module for measuring the volume?</p>
</blockquote>
</aside>
<p>You can measure volume of segments using Segment statistics module.</p>
<p>In the attached screenshot ‘Module segment statistics’ 3 volumes are shown as well as values ​​for minimum. maximum, mean and median. Frankly, I don’t understand the whole line.I hope, you can help me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19270cbe07d35ddeac3ca3df5eaf9287f9e00b9e.jpeg" data-download-href="/uploads/short-url/3AvBeo8OVaCDTZKlMAo9sCx9urk.jpeg?dl=1" title="Segment Statistics - Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19270cbe07d35ddeac3ca3df5eaf9287f9e00b9e_2_690x289.jpeg" alt="Segment Statistics - Volume" data-base62-sha1="3AvBeo8OVaCDTZKlMAo9sCx9urk" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19270cbe07d35ddeac3ca3df5eaf9287f9e00b9e_2_690x289.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19270cbe07d35ddeac3ca3df5eaf9287f9e00b9e_2_1035x433.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19270cbe07d35ddeac3ca3df5eaf9287f9e00b9e_2_1380x578.jpeg 2x" data-dominant-color="615F65"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment Statistics - Volume</span><span class="informations">1680×705 363 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-06-28 19:51 UTC)

<p>You can find description of the metrics here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>

---
