---
topic_id: 11424
title: "Register Uct Scans With Conventional Ct Scan"
date: 2020-05-05
url: https://discourse.slicer.org/t/11424
---

# Register uCT scans with conventional CT scan

**Topic ID**: 11424
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/register-uct-scans-with-conventional-ct-scan/11424

---

## Post #1 by @sfglio (2020-05-05 20:27 UTC)

<p>I am trying to register a microCT scan of an implant with a conv. CT of the same implant within the jaw.</p>
<p>I transformed the microCT scan to the correct position however the final 3d-3d registration fails. Even when I resample the microCT image to the same voxel sizes (which means a significant reduction of the visualization of the implant).</p>
<p>I also tried elastix modul.<br>
So my question is, whether there is a chance at all to automatically register them or is manual the best I can achieve?<br>
I uploaded an example of the manual transformation outcome…</p>
<p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1bbyujqBUzwa6_YAa5aKvTc-cc_dOHiIu/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:128/67;"><img src="https://lh4.googleusercontent.com/pc5UIbXyK1_2fIQJUifAV9_-3ilyPG8aZCiu1l1brAyZB-obV0FQElyZMGG9Z3c=w1200-h630-p" class="thumbnail" width="128" height="67"></div>

<h3><a href="https://drive.google.com/file/d/1bbyujqBUzwa6_YAa5aKvTc-cc_dOHiIu/view?usp=sharing" target="_blank" rel="nofollow noopener">Bildschirmfoto 2020-05-05 um 21.57.21.png</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1tRwwGqDS9vkb5pInToNogzDG5im9t0_V/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:128/67;"><img src="https://lh6.googleusercontent.com/zgQEgI7hBU4DzNkQb8zjTpt_l50oUhRTFBXBFeuRRGuDRd0HvRAlq1HmcnDX3qE=w1200-h630-p" class="thumbnail" width="128" height="67"></div>

<h3><a href="https://drive.google.com/file/d/1tRwwGqDS9vkb5pInToNogzDG5im9t0_V/view?usp=sharing" target="_blank" rel="nofollow noopener">Bildschirmfoto 2020-05-05 um 21.56.22.png</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1pn1qd9nj8qE9IZ4rZ41FzLy1LQ_JcrYB/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:128/67;"><img src="https://lh4.googleusercontent.com/8pCeOf1hIUM74IjAQUOdt__j4p_hDZCA-hDM5T0UPPwqGqleoVXG0XCQkUEC4T4=w1200-h630-p" class="thumbnail" width="128" height="67"></div>

<h3><a href="https://drive.google.com/file/d/1pn1qd9nj8qE9IZ4rZ41FzLy1LQ_JcrYB/view?usp=sharing" target="_blank" rel="nofollow noopener">Bildschirmfoto 2020-05-05 um 21.57.07.png</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Kind regards</p>

---

## Post #2 by @sfglio (2020-05-24 13:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0ba1f599df8369adc036e187b01352cd84829121.jpeg" data-download-href="/uploads/short-url/1EUfpp6FSXjzVN0cqeFJ9l8SJHj.jpeg?dl=1" title="Bildschirmfoto 2020-05-24 um 15.23.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ba1f599df8369adc036e187b01352cd84829121_2_690x266.jpeg" alt="Bildschirmfoto 2020-05-24 um 15.23.06" data-base62-sha1="1EUfpp6FSXjzVN0cqeFJ9l8SJHj" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ba1f599df8369adc036e187b01352cd84829121_2_690x266.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ba1f599df8369adc036e187b01352cd84829121_2_1035x399.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ba1f599df8369adc036e187b01352cd84829121_2_1380x532.jpeg 2x" data-dominant-color="444A44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-05-24 um 15.23.06</span><span class="informations">1988×768 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I remove the rest of the unsegmented area?<br>
I am only interested in the segmented implant and want to remove all other grey values!</p>
<p>The mask tool lets me only fill the voxels with a different intensity…</p>

---

## Post #3 by @lassoan (2020-05-24 14:32 UTC)

<p>Shape of an image array is always a box and you need to set <em>some</em> value in each voxel of the array.</p>
<p>What would you like to achieve with the registration?<br>
Does the registration need to recover rotation around the long axis of the implant?</p>

---

## Post #4 by @sfglio (2020-05-24 16:52 UTC)

<p>Yes the registration would need to recover the rotation around the long axis of the implant.</p>
<ol>
<li>
<p>I want to register the uCT scan of the implant with the same implant in a jaw from a conventional CT scan. For the registration I need to mask out everything except the implant, which seems to work with the mask tool.</p>
</li>
<li>
<p>After the registration, I want to transfer the implant position to a CT scan from a jaw without any implants, i.e. fuse 2 scalar volumes using add scalar volumes.<br>
I tried substract scalar vol (because faster compared to add) which results in a “black” implant in the ct scan of the jaw, however I get deteriorated voxels around the “black” implant in the extent of a box which I want to avoid.</p>
</li>
</ol>
<p>Is there an option for “transparent” voxels, so that the voxels of the other CT scan are not changed around the “blanked out” implant.<br>
Finally, I would prefer the add scalar vol option as I would need the implant in the CT scan to be as in uCT.</p>

---

## Post #5 by @lassoan (2020-05-24 18:29 UTC)

<p>There is no need for “transparent” voxels, just set voxel values outside the implant to 0. Adding/subtracting 0 will not alter the volume.</p>
<p>You can use Threshold scalar volume to set values outside a chosen intensity range to 0.</p>
<p>If you want to fine-tune what happens at the implant’s boundary then you can use Segment Editor’s Mask volume effect (provided by SegmentEditorExtraEffects extension).</p>

---
