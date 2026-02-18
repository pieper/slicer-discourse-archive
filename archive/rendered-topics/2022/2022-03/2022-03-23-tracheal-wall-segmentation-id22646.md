# Tracheal wall segmentation

**Topic ID**: 22646
**Date**: 2022-03-23
**URL**: https://discourse.slicer.org/t/tracheal-wall-segmentation/22646

---

## Post #1 by @Eserval (2022-03-23 01:14 UTC)

<p>Hello everyone,</p>
<p>I’m trying to expand the usage of Slicer in tracheal stenotic disease. For that, it would be necessary to segment the tracheal wall with its thickness. The workflows that I use to segment the airway are based on extracting the air column and do not fit very well for that purpose.</p>
<p>Does anyone have some tips for that?</p>
<p>Best</p>

---

## Post #2 by @rbumm (2022-03-23 10:59 UTC)

<p>Hi,<br>
I would suggest doing</p>
<ul>
<li>
<p>a grow from seeds inner airway segmentation first</p>
</li>
<li>
<p>then grow this segmentation by 3 mm</p>
</li>
<li>
<p>then create a new segment “trachea wall”</p>
</li>
<li>
<p>threshold the wall so that it becomes visible in the segment editor</p>
</li>
<li>
<p>Set masking to “Inside Segment 1” (your enlarged airway) and “Allow overlap”, then “Apply” thresholding</p>
</li>
<li>
<p>shrink back your initial inner airway segmentation by 3 mm</p>
</li>
<li>
<p>do some fine tuning</p>
</li>
</ul>
<p>Example:<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9842175ab230687384130943ac7d7bd7bd2a4de9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9842175ab230687384130943ac7d7bd7bd2a4de9.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9842175ab230687384130943ac7d7bd7bd2a4de9.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #3 by @Eserval (2022-03-24 20:03 UTC)

<p>Thanks again Rudolf ! It works very well. I think we have the limitation of the exam resolution. Maybe its impossibel o isolate the tracheal rings for example. Sometimes in older patients when we have calcificatios it seens to be easier.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa2f74bd92ab26eefa1050f25ede296940af37f3.jpeg" data-download-href="/uploads/short-url/ohwQkqQCmr1ilOVUaVjSpC7enl1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa2f74bd92ab26eefa1050f25ede296940af37f3_2_690x326.jpeg" alt="image" data-base62-sha1="ohwQkqQCmr1ilOVUaVjSpC7enl1" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa2f74bd92ab26eefa1050f25ede296940af37f3_2_690x326.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa2f74bd92ab26eefa1050f25ede296940af37f3_2_1035x489.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa2f74bd92ab26eefa1050f25ede296940af37f3_2_1380x652.jpeg 2x" data-dominant-color="9A9795"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×908 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @rbumm (2022-03-24 20:40 UTC)

<p>Thanks for the update - you can reduce the smoothing of your tracheal wall segmentation by left-clicking and expanding the “Show 3D button”  and reducing the “Surface smoothing” to 0.3 or 0.2 - this should help you to get more tracheal ring details</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae555f476fb49948a2da3f63936b3450a34a40a4.png" data-download-href="/uploads/short-url/oSdZjoVo2hNQUixvp767rIq5pt2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae555f476fb49948a2da3f63936b3450a34a40a4.png" alt="image" data-base62-sha1="oSdZjoVo2hNQUixvp767rIq5pt2" width="690" height="288" data-dominant-color="D5D6D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×292 21.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
