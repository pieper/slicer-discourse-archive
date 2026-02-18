# How to modify interpolation mesh grids

**Topic ID**: 4211
**Date**: 2018-09-27
**URL**: https://discourse.slicer.org/t/how-to-modify-interpolation-mesh-grids/4211

---

## Post #1 by @baverso (2018-09-27 15:03 UTC)

<p>Hello, I’d like to know if there are any modules which allow me to modify the interpolation grids? Please see the image below for various methods of alignment:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48a5e35321988519de1a2b395bac1b9340cd9886.png" data-download-href="/uploads/short-url/amFN3y2cEmK3jgTIy7aI3mrlbue.png?dl=1" title="10%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a5e35321988519de1a2b395bac1b9340cd9886_2_444x500.png" alt="10%20AM" data-base62-sha1="amFN3y2cEmK3jgTIy7aI3mrlbue" width="444" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a5e35321988519de1a2b395bac1b9340cd9886_2_444x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a5e35321988519de1a2b395bac1b9340cd9886_2_666x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a5e35321988519de1a2b395bac1b9340cd9886_2_888x1000.png 2x" data-dominant-color="F8F7F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10%20AM</span><span class="informations">1568×1764 402 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Source: Image biomarker standardisation initiative</p><aside class="onebox pdf" data-onebox-src="https://arxiv.org/pdf/1612.07003.pdf">
  <header class="source">

      <a href="https://arxiv.org/pdf/1612.07003.pdf" target="_blank" rel="noopener nofollow ugc">arxiv.org</a>
  </header>

  <article class="onebox-body">
    <a href="https://arxiv.org/pdf/1612.07003.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://arxiv.org/pdf/1612.07003.pdf" target="_blank" rel="noopener nofollow ugc">1612.07003.pdf</a></h3>

  <p class="filesize">1827.71 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If not in possible in the Slicer GUI, does ITK or VTK support this programmatically? Thank you for any assistance.</p>

---

## Post #2 by @lassoan (2018-09-27 18:21 UTC)

<p>Do you mean changing sampling grid of image volumes? In Slicer, we refer to it as resampling of volumes and there are many modules for this - see details here: <a href="https://www.slicer.org/wiki/Registration:Resampling">https://www.slicer.org/wiki/Registration:Resampling</a></p>

---

## Post #3 by @baverso (2018-09-27 19:01 UTC)

<p>Hi Andras, thank you for your response. I am familiar with the modification of the vowel spacing and various methods of interpolation, and it’s great that this functionality is available through several modules.</p>
<p>Once a volume has been down sampled with interpolation, the newly interpolated grid (as per the upper right picture) would likely represent the placement of the new voxels. If I desired to choose a method of alignment that is featured in the bottom pictures of my post, does a function exist at this time?</p>
<p>I do not believe one does after spending some time examining several resampling modules, but thought it may be worth asking. Perhaps in VTK or ITK?</p>

---

## Post #4 by @lassoan (2018-09-27 19:26 UTC)

<aside class="quote no-group" data-username="baverso" data-post="3" data-topic="4211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c5a1d2/48.png" class="avatar"> baverso:</div>
<blockquote>
<p>If I desired to choose a method of alignment that is featured in the bottom pictures of my post, does a function exist at this time?</p>
</blockquote>
</aside>
<p>Usually you need to specify the output geometry (image origin, spacing, axis directions), so you can easily implement any alignment strategy that you prefer.</p>
<p>Some modules offer resampling by a scaling factor and they need to choose some alignment strategy. For example “Crop volume” module can rescale the image and it aligns the pixel corners.</p>

---
