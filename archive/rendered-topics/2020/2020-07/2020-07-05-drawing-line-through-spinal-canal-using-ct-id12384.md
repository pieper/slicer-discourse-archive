# Drawing line through spinal canal using CT

**Topic ID**: 12384
**Date**: 2020-07-05
**URL**: https://discourse.slicer.org/t/drawing-line-through-spinal-canal-using-ct/12384

---

## Post #1 by @bz78 (2020-07-05 15:20 UTC)

<p>Hi all,</p>
<p>Is there an automatic way to draw a cranio-caudal line (using CurveMaker) through the spinal canal using CT slices? We are able to easily generate a detailed 3D model of the vertebral column by thresholding and isolating an island, but need a programmatic way of placing fiducials within the central canal (perhaps at the centroid) for a clinical research project. Currently, our method is to just eyeball the center of the canal on axial/sagittal slices, which is slow and inaccurate.</p>
<p>Thanks so much! Given that this is my first post, I apologize for breaking any forum conventions.<br>
Bryan</p>

---

## Post #2 by @pieper (2020-07-05 16:15 UTC)

<p>Good first post question <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  Maybe post some screenshots so we have an idea of the data you are working with and what your segmentations look like so far.</p>
<p>If you can get a reasonable segmentation of the spinal canal you might be able to use the VMTK extension for that:  <a href="https://github.com/vmtk/SlicerExtension-VMTK">https://github.com/vmtk/SlicerExtension-VMTK</a></p>

---

## Post #3 by @bz78 (2020-07-06 00:21 UTC)

<p>Hi Steve, thanks for your reply!</p>
<p>Here is a screenshot of a sample CT with a minimal model of what we are able to do so far. I placed 5 fiducials, 3 of which are shown on the sagittal slice, just to illustrate a rough curve (blue). Ideally we want to have as many points as is reasonable because we want to measure the curvature at precise locations along the spinal cord for a ton of spine CTs.</p>
<p>The centerline function in the VMTK extension looks like it could be exactly what we need. Unfortunately, I’m not sure the best way to segment the isolated central canal. The adjacent tissue density is too uniform, so any of my attempts to threshold give pretty useless segmentations. This seems like an entirely separate problem than my original question about drawing a centerline (which seems to be solved). But do you have any suggestions for how we could get a reasonable segmentation of the central canal itself?</p>
<p>For now, it doesn’t really matter that the vertebrae are not entirely thresholded since the representation of the vertebral column is currently purely illustrative. I originally thought we could use it to extract a position within the hypodense canal, but that does not seem feasible.</p>
<p>We appreciate the help - thanks for looking after this forum, Steve! I’ll mark your original post as the solution to my original problem!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4e23468971a61492381bd4c3e897999737a8011.jpeg" data-download-href="/uploads/short-url/pOaAkOzjobZLw1iYbOptWB0NrAl.jpeg?dl=1" title="Screen Shot 2020-07-05 at 7.59.32 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e23468971a61492381bd4c3e897999737a8011_2_690x340.jpeg" alt="Screen Shot 2020-07-05 at 7.59.32 PM" data-base62-sha1="pOaAkOzjobZLw1iYbOptWB0NrAl" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e23468971a61492381bd4c3e897999737a8011_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e23468971a61492381bd4c3e897999737a8011_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b4e23468971a61492381bd4c3e897999737a8011_2_1380x680.jpeg 2x" data-dominant-color="929298"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-05 at 7.59.32 PM</span><span class="informations">1920×948 393 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-07-06 05:13 UTC)

<aside class="quote no-group" data-username="bz78" data-post="3" data-topic="12384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bz78/48/5964_2.png" class="avatar"> bz78:</div>
<blockquote>
<p>But do you have any suggestions for how we could get a reasonable segmentation of the central canal itself?</p>
</blockquote>
</aside>
<p>Soft tissue contrast on CT is not great, so in general it is hard to constraint region growing. However, this is a special case: the segmented object’s shape is smooth and it is only connected to similar-intensity regions through thin canals, so it is possible to prevent leaking via intensity and spatial connectivity and smoothness constraints implemented in “Local threshold” effect in Segment editor. Once the spinal canal is segmented, centerline extraction is fully automatic. See this video for step-by-step instructions:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="9c0-50kRz-U" data-video-title="Spinal canal centerline segmentation from CT" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=9c0-50kRz-U" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/9c0-50kRz-U/maxresdefault.jpg" title="Spinal canal centerline segmentation from CT" width="" height="">
  </a>
</div>

<p>What is the clinical application? If spinal canal centerline is only a surrogate and you are actually interested in measuring curvature and torsion of the spinal column then you may consider placing markup points on the facet joints (it should be very quick on volume rendering of bones) and computing the angles from these points.</p>

---

## Post #5 by @bz78 (2020-07-06 17:00 UTC)

<p>Local thresholding worked very well - it is difficult to fully prevent leaking but parameter tuning + smoothing should eventually do the trick for us. Thanks so much for pointing out this extension!</p>
<p>Broadly, the clinical application is to analyze spine biomechanics using flexion-extension CTs. You are absolutely correct that the spinal canal centerline is just a surrogate, although we are more interested in the properties of the spinal cord itself versus the vertebral column. That might be an irrelevant distinction, though, and using the facet joints as an alternative proxy is a really good idea. We might try all of these methods (eyeball, centerline, facet joint) and compare results.</p>
<p>Thanks so much to both of you! This was immensely helpful and time-saving.</p>

---

## Post #6 by @lassoan (2020-07-06 17:43 UTC)

<aside class="quote no-group" data-username="bz78" data-post="5" data-topic="12384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bz78/48/5964_2.png" class="avatar"> bz78:</div>
<blockquote>
<p>the clinical application is to analyze spine biomechanics using flexion-extension CTs</p>
</blockquote>
</aside>
<p>You might consider using ultrasound for 3D spine imaging, as you don’t need to worry about radiation dose and you can acquire images in any patient position (not just lying but standing, sitting, etc.). There is a Slicer-based prototype for this, which works quite well. <a class="mention" href="/u/ungi">@ungi</a> can give you more details if you were interested.</p>
<p>Here is an example of an ultrasound bone surface scan of a phantom (of course in patients there is a lot of signal from soft tissues over the bone, but the bone surface can be extracted using automatic filtering):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-video-start-time="133" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4&amp;t=133" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>


---

## Post #7 by @bz78 (2020-07-06 17:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="12384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Here is an example of an ultrasound bone surface scan of a phantom (of course in patients there is a lot of signal from soft tissues over the bone, but the bone surface can be extracted using automatic filtering):</p>
</blockquote>
</aside>
<p>Whoa, this is fascinating - are there any studies in your lab that use this as the primary model acquisition modality? I’m not sure we can relate this to the current CT analysis, but I think we might be able to generate an entirely new IRB study for this…</p>

---

## Post #8 by @lassoan (2020-07-06 20:42 UTC)

<p>Yes. The main idea is to make this replace CT and X-ray for monitoring scoliosis patients. If you have CT image then you can reconstruct the entire spinal column based on landmarks identified on ultrasound.</p>
<p><a class="mention" href="/u/ungi">@ungi</a> can you recommend a few papers that describe latest studies and developments?</p>

---

## Post #10 by @ungi (2020-07-07 14:29 UTC)

<p>This is our most recent paper on tracked ultrasound for spine curve measurements:<br>
<a href="http://perk.cs.queensu.ca/contents/automatic-spine-ultrasound-segmentation-scoliosis-visualization-and-measurement" class="onebox" target="_blank" rel="nofollow noopener">http://perk.cs.queensu.ca/contents/automatic-spine-ultrasound-segmentation-scoliosis-visualization-and-measurement</a><br>
All code and training data is public. I know there is minimal documentation, but and I’m happy to help if you have further questions.</p>

---
