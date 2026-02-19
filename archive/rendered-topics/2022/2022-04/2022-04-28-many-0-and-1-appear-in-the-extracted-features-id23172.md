---
topic_id: 23172
title: "Many 0 And 1 Appear In The Extracted Features"
date: 2022-04-28
url: https://discourse.slicer.org/t/23172
---

# Many 0 and 1 appear in the extracted features

**Topic ID**: 23172
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/many-0-and-1-appear-in-the-extracted-features/23172

---

## Post #1 by @lrc_09 (2022-04-28 14:45 UTC)

<p>Hi, I used Radiomics module  to extract PET image features. I set resampled voxel size to 1,1,1 and bin width to 64 based on the literatures , and the result shows that there are many 0 and 1 in GLCM, GLDM, GLRLM, GLSZM and NGTDM. I don’t know where the settings are wrong, can you help me check? Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9c422a1c6f05bd0bebc097730617597de31812d.jpeg" data-download-href="/uploads/short-url/xlZt2YwJMGa8XY9VTwZPuxLFmdD.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c422a1c6f05bd0bebc097730617597de31812d_2_690x384.jpeg" alt="1" data-base62-sha1="xlZt2YwJMGa8XY9VTwZPuxLFmdD" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c422a1c6f05bd0bebc097730617597de31812d_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c422a1c6f05bd0bebc097730617597de31812d_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e9c422a1c6f05bd0bebc097730617597de31812d_2_1380x768.jpeg 2x" data-dominant-color="393938"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1625×905 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3149a3932f8af326ae1e818a70272205e3445f0d.png" data-download-href="/uploads/short-url/721alcyJyDV2fGBpEMRlAqGgYvX.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3149a3932f8af326ae1e818a70272205e3445f0d_2_690x388.png" alt="2" data-base62-sha1="721alcyJyDV2fGBpEMRlAqGgYvX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3149a3932f8af326ae1e818a70272205e3445f0d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3149a3932f8af326ae1e818a70272205e3445f0d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3149a3932f8af326ae1e818a70272205e3445f0d_2_1380x776.png 2x" data-dominant-color="393938"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @JoostJM (2022-05-03 07:24 UTC)

<p>Hello <a class="mention" href="/u/lrc_09">@lrc_09</a>,</p>
<p>What you are seeing are typical results when extracting from a ‘flat region’. See the online PyRadiomics documentation for more details. TLDR: The binwidth parameter is set too large (default 25, which is too much for SUV values).</p>
<p>The ‘bin width’ of 64 from literature is incorrect, the 64 you encounter in literature is 64 bin<em>count</em>. In PyRadiomics we advise against using a fixed binCount, details for this are also found in the <a>PyRadiomics documentation</a>.</p>

---
