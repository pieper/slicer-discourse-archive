---
topic_id: 10073
title: "Clip Segment Or Model Along A Plane"
date: 2020-02-02
url: https://discourse.slicer.org/t/10073
---

# clip segment or model along a plane

**Topic ID**: 10073
**Date**: 2020-02-02
**URL**: https://discourse.slicer.org/t/clip-segment-or-model-along-a-plane/10073

---

## Post #1 by @jpva (2020-02-02 20:44 UTC)

<p>Hello,<br>
I would like to clip a segment along a plane to see the internal structure of the both part of the clipped segment. With surface cut, I have difficulty to obtain a plane for the cut and I did not find a way to see the both part of the plane cut.<br>
By converting the segment to a model and using ModelClip, I have the ability to see both part of the clipped model but the surface are not rendered the way I would like. They disappear according to the angle of view. I guess that it may come from the model that is only surface and not solid inside (in Meshmixer there is an option : make solid to see correctly after a plane cut).<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ed468eff0fdad9f232a82f233c633fb78be1bd5.jpeg" data-download-href="/uploads/short-url/fOrBGI60SYxOg0iKg3Bk8JqSyoJ.jpeg?dl=1" title="model_cut_side2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ed468eff0fdad9f232a82f233c633fb78be1bd5_2_690x405.jpeg" alt="model_cut_side2" data-base62-sha1="fOrBGI60SYxOg0iKg3Bk8JqSyoJ" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ed468eff0fdad9f232a82f233c633fb78be1bd5_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ed468eff0fdad9f232a82f233c633fb78be1bd5_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ed468eff0fdad9f232a82f233c633fb78be1bd5_2_1380x810.jpeg 2x" data-dominant-color="95959B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model_cut_side2</span><span class="informations">3360×1974 657 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c227d71dbec1cb230a9299cf8145ae63a1e46c72.jpeg" data-download-href="/uploads/short-url/rHzZaUSWyUByS9ZiJdAnorlLnSa.jpeg?dl=1" title="model_cut_side1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c227d71dbec1cb230a9299cf8145ae63a1e46c72_2_690x405.jpeg" alt="model_cut_side1" data-base62-sha1="rHzZaUSWyUByS9ZiJdAnorlLnSa" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c227d71dbec1cb230a9299cf8145ae63a1e46c72_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c227d71dbec1cb230a9299cf8145ae63a1e46c72_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c227d71dbec1cb230a9299cf8145ae63a1e46c72_2_1380x810.jpeg 2x" data-dominant-color="96959B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model_cut_side1</span><span class="informations">3360×1974 651 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-02-02 20:48 UTC)

<aside class="quote no-group" data-username="jpva" data-post="1" data-topic="10073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/258eb7/48.png" class="avatar"> jpva:</div>
<blockquote>
<p>With surface cut, I have difficulty to obtain a plane for the cut</p>
</blockquote>
</aside>
<p>You can use Scissors effect. The last curve segment is always straight and you can also choose rectangular cutting shape. This will keep the structure solid.</p>
<aside class="quote no-group" data-username="jpva" data-post="1" data-topic="10073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/258eb7/48.png" class="avatar"> jpva:</div>
<blockquote>
<p>converting the segment to a model and using ModelClip, I have the ability to see both part of the clipped model</p>
</blockquote>
</aside>
<p>If you export to model (surface mesh) and cut it then the model won’t be closed anymore. Enable rendering of both sides (inside and outside) of the surface in Models module.</p>

---

## Post #3 by @jpva (2020-02-02 21:43 UTC)

<p>Thanks!</p>
<p>I was able to obtain the desired effect with the scissors but it is not very convenient when I have to redefine the plane cut (see the segment_cut picture) . The modelclip  module is more effecient for that. However, with the option of visible sides : all, I see both inside and outside surface but it is not closed at the section as it is with segment. Is there a way to create a model that looks like the segment cut  ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d31572ea6e0d39fe7992a9c344b00bc3d333ef3c.jpeg" data-download-href="/uploads/short-url/u7kHpWOAOrgNvHS0DMZ4rsO9AHG.jpeg?dl=1" title="Models_cut_visibleSides_all" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d31572ea6e0d39fe7992a9c344b00bc3d333ef3c_2_690x404.jpeg" alt="Models_cut_visibleSides_all" data-base62-sha1="u7kHpWOAOrgNvHS0DMZ4rsO9AHG" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d31572ea6e0d39fe7992a9c344b00bc3d333ef3c_2_690x404.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d31572ea6e0d39fe7992a9c344b00bc3d333ef3c_2_1035x606.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d31572ea6e0d39fe7992a9c344b00bc3d333ef3c_2_1380x808.jpeg 2x" data-dominant-color="8D9493"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Models_cut_visibleSides_all</span><span class="informations">3360×1972 681 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40bbefdeec4b06f4be521c44aae07cbe9b0907b9.jpeg" data-download-href="/uploads/short-url/9eFd669Ecj1WpGF3RUOkteAni5P.jpeg?dl=1" title="segment_cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40bbefdeec4b06f4be521c44aae07cbe9b0907b9_2_690x404.jpeg" alt="segment_cut" data-base62-sha1="9eFd669Ecj1WpGF3RUOkteAni5P" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40bbefdeec4b06f4be521c44aae07cbe9b0907b9_2_690x404.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40bbefdeec4b06f4be521c44aae07cbe9b0907b9_2_1035x606.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40bbefdeec4b06f4be521c44aae07cbe9b0907b9_2_1380x808.jpeg 2x" data-dominant-color="949497"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment_cut</span><span class="informations">3360×1972 853 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @timeanddoctor (2020-02-03 04:34 UTC)

<p>You can crop the volume with a ROI before segmentation.<br>
And the surface quality is associated with the resolution of DICOM of CTA</p>

---
