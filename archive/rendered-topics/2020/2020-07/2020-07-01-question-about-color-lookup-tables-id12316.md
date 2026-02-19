---
topic_id: 12316
title: "Question About Color Lookup Tables"
date: 2020-07-01
url: https://discourse.slicer.org/t/12316
---

# Question about color lookup tables

**Topic ID**: 12316
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/question-about-color-lookup-tables/12316

---

## Post #1 by @rprueckl (2020-07-01 10:16 UTC)

<p>Hi,</p>
<p>I have a question about using color lookup tables. I wanted to display an atlas nifti file <a href="https://www.nitrc.org/frs/download.php/11403/WHS_SD_rat_atlas_v3.nii.gz" rel="noopener nofollow ugc">WHS_SD_rat_atlas_v3.nii.gz</a> in its original colors according to <a href="https://www.nitrc.org/frs/download.php/11404/WHS_SD_rat_atlas_v3.label" rel="noopener nofollow ugc">WHS_SD_rat_atlas_v3.label</a>.</p>
<p>I converted the lookup table to a Slicer lookup table and imported it:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c784e90e65cfb87e6d67a73cb216f13176e5862.png" data-download-href="/uploads/short-url/43R7MtsHTGdmo7KTAk3fCh7H3P4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c784e90e65cfb87e6d67a73cb216f13176e5862.png" alt="image" data-base62-sha1="43R7MtsHTGdmo7KTAk3fCh7H3P4" width="549" height="500" data-dominant-color="525355"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×525 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I changed the lookup table of the imported atlas volume to the imported lookup table, set its Window/Level settings to Manual Min/Max and the values to 0 and 164 (according to the volume information). This range also fits to the color indices of the lookup table.</p>
<p>Now, the scalars were not colored correctly. I made a dummy nifti using MATLAB to investigate:</p>
<pre><code class="lang-auto">V = zeros(165, 2, 2);
V(:, 1, 1) = linspace(0, 164, 165);
V=uint16(V);
niftiwrite(V,'path\to\testnifti.nii');
</code></pre>
<p>With the same slicer settings (lookup table, window/level settings), the result is as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef48a9f7c0900c8979a09da82ed16dbc15501135.png" data-download-href="/uploads/short-url/y8NNqrWcxZTNx44AvVfOnOJtF4N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef48a9f7c0900c8979a09da82ed16dbc15501135.png" alt="image" data-base62-sha1="y8NNqrWcxZTNx44AvVfOnOJtF4N" width="690" height="132" data-dominant-color="0F1311"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">944×181 2.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With this, I soon discovered, that the correct settings for Window/Level Manual Min/Max are 0 and 255 leading to this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48f6a87e4537b61af4628dd0cc80f52f77f41047.png" data-download-href="/uploads/short-url/apsQ7brSmyMdCJq6PSA8ffl87xZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48f6a87e4537b61af4628dd0cc80f52f77f41047.png" alt="image" data-base62-sha1="apsQ7brSmyMdCJq6PSA8ffl87xZ" width="690" height="126" data-dominant-color="0C110D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">945×173 2.83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I use the same settings for the atlas, it is displayed in its original colors.</p>
<p>The question is: Why 255?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2020-07-01 13:55 UTC)

<p>Can you share the Slicer color file that you generated? If you want 1:1 mapping then you need to set the scalar range to match the number of colors.</p>
<p>By the way, if you load a labelmap volume, then I think the color table is used as is - there is no intensity mapping.</p>
<p>Have you created a script that converted ITK-snap to Slicer color table? Can you share it?</p>

---

## Post #3 by @rprueckl (2020-07-01 14:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12316" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you share the Slicer color file that you generated? If you want 1:1 mapping then you need to set the scalar range to match the number of colors.</p>
</blockquote>
</aside>
<p>Sure - it can be downloaded from <a href="https://drive.google.com/file/d/1Q42V1SNnCXS76fvy7GapmkJIDaQ9knR8/view?usp=sharing" rel="noopener nofollow ugc">here</a>. This version contains entries for the missing color indices in the original file, as I was thinking that missing entries might be an issue here.</p>
<p>I was playing around with the scalar range - I guess that the standard (as depicted in the screenshot) should be fine.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12316" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By the way, if you load a labelmap volume, then I think the color table is used as is - there is no intensity mapping.</p>
</blockquote>
</aside>
<p>A labelmap volume was one of the first things that came into my mind in connection with atlas-related applications. However, the atlas in question is distributed as a nifti and I couldn’t find a way in my quick research to convert it to a labelmap volume. So I extract the desired regions with the segment editor (thresholding the relevant scalar). Is there a better way to do this?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12316" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you created a script that converted ITK-snap to Slicer color table? Can you share it?</p>
</blockquote>
</aside>
<p>No, I did this by hand.</p>

---

## Post #4 by @lassoan (2020-07-01 15:07 UTC)

<p>You can import a labelmap stored in a nifti file as described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html?highlight=labelmap#import-an-existing-segmentation-from-volume-file" class="onebox" target="_blank">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html?highlight=labelmap#import-an-existing-segmentation-from-volume-file</a></p>
<p>You can also convert a scalar volume to labelmap volume after you loaded it, by using “Convert to labelmap” in Volumes module / Volume information section.</p>

---

## Post #5 by @rprueckl (2020-07-01 15:38 UTC)

<p>Oh, thanks for this information - especially the first option is very nice. Additionally to having the segments available, it would be very advantageous to be able to also import colors and labels for the segments. This way, the atlas representation would be complete.</p>
<p>Unfortunately, the initial question about the color lookup table settings remains a mystery for me.</p>

---

## Post #6 by @lassoan (2020-07-02 05:37 UTC)

<p>One more tip: If you work with hundreds of segments then you must use Slicer-4.11, as it has huge performance improvements for managing such large segmentations. It also has search and filter to make it easy to select a subset of segments that you are working on. Right-click on the segment list and choose “Show filter bar” to enable this feature.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36d5c71b5042394b27fbd4d49a487d21edf5efdd.png" data-download-href="/uploads/short-url/7P5NBKFR1RwiP3JnZ78qLgzMPrn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36d5c71b5042394b27fbd4d49a487d21edf5efdd_2_584x499.png" alt="image" data-base62-sha1="7P5NBKFR1RwiP3JnZ78qLgzMPrn" width="584" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36d5c71b5042394b27fbd4d49a487d21edf5efdd_2_584x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/36d5c71b5042394b27fbd4d49a487d21edf5efdd_2_876x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36d5c71b5042394b27fbd4d49a487d21edf5efdd.png 2x" data-dominant-color="E8EAE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1164×995 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-10-01 22:20 UTC)

<p>A post was split to a new topic: <a href="/t/rendering-at-higher-than-8-bits-per-pixel/19961">Rendering at higher than 8 bits per pixel</a></p>

---
