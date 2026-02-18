# TotalSegmentator results computed in fast mode are rough

**Topic ID**: 28768
**Date**: 2023-01-26
**URL**: https://discourse.slicer.org/t/totalsegmentator-results-computed-in-fast-mode-are-rough/28768

---

## Post #1 by @Francesco_92 (2023-01-26 13:27 UTC)

<p>Hi Everyone. Thank you Andras Lasso for this beautiful work.<br>
I have a problem with total segmentator, please see the screenshot below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a00d085b09f3f9df332104fffc16fe28a794128.jpeg" data-download-href="/uploads/short-url/1quweioOsmHiIwOCPX63jnCEVw4.jpeg?dl=1" title="Roughness" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a00d085b09f3f9df332104fffc16fe28a794128_2_690x442.jpeg" alt="Roughness" data-base62-sha1="1quweioOsmHiIwOCPX63jnCEVw4" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a00d085b09f3f9df332104fffc16fe28a794128_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a00d085b09f3f9df332104fffc16fe28a794128_2_1035x663.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a00d085b09f3f9df332104fffc16fe28a794128_2_1380x884.jpeg 2x" data-dominant-color="443E40"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Roughness</span><span class="informations">1400×897 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Why the model is so rough? I have a GPU of 4 GB, maybe I have to use my CPU and wait one hour to have better outcomes? Or is it another problem?<br>
Thank you in advance,<br>
Francesco</p>

---

## Post #2 by @lassoan (2023-01-26 15:58 UTC)

<aside class="quote no-group" data-username="Francesco_92" data-post="1" data-topic="28768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/5daacb/48.png" class="avatar"> Francesco_92:</div>
<blockquote>
<p>Why the model is so rough? I have a GPU of 4 GB, maybe I have to use my CPU and wait one hour to have better outcomes?</p>
</blockquote>
</aside>
<p>Yes, exactly. A 4GB GPU is a solid device for visualization but does not meet hardware requirements for most deep learning applications.</p>
<p>If you want to get a GPU that can run most image segmentation models then I would recommend to get a one with at least 12GB RAM (such as an RTX 3060, it only costs around $600). If you want to a GPU that you can use for a few more years or you want to train your own models then you may consider getting one with 24GB memory (such as an RTX 3090, for about $2500).</p>
<p>If you don’t want to spend any money on new hardware then you can stay on the CPU and wait out the 10-30x longer computation times (40 minutes on CPU instead of 2 minutes on GPU). These long computation times are not tolerable if you want to use interactive segmentation methods or if you need to train models, but if you are using well-trained, robust, fully-automatic models then waiting an hour for a segmentation result should be fine in most cases. It would be still much faster than manual segmentation, while requiring zero manual effort.</p>

---

## Post #3 by @rbumm (2023-04-07 01:40 UTC)

<p>Just for the records, I am just working on a Windows 10 with GTX 970 with 4 GB video RAM and can totalsegment a rather thin-sliced lung CT ( ~ 100 MB nrrd) with lobe smoothing in 80.3 s</p>

---

## Post #4 by @Dave90 (2023-05-17 06:02 UTC)

<p>Hi Andras. is there anywhere in a document that isn’t just a forum post where minimum requirements are listed. i’m approaching our IT department separate to our Radiation Therapy department to ask for some hardware to do this work and they want to see what the minimum working specs would be.</p>
<p>don’t think they’ll be happy with a forum post reply.</p>

---

## Post #5 by @lassoan (2023-05-17 12:23 UTC)

<p>They can directly talk to package developers on this forum, so they should be happy, but you can find some specific data on GPU memory requirements here: <a href="https://github.com/wasserth/TotalSegmentator#resource-requirements" class="inline-onebox">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104 important anatomical structures in CT images</a></p>
<p>Based on specific images the GPU memory requirement for full-resolution segmentation is about 12GB, so if you want to be safe I then it could make sense to use a GPU with 16GB memory.</p>

---
