# Grow From Seeds Leaks

**Topic ID**: 26382
**Date**: 2022-11-22
**URL**: https://discourse.slicer.org/t/grow-from-seeds-leaks/26382

---

## Post #1 by @Vincebisca (2022-11-22 16:46 UTC)

<p>Hi !</p>
<p>I have noticed a recuring problem when I try to use the Grow From Seeds method. I am trying to segment a hip articulation. For that, I tried Grow From Seeds constrained in a range of intensity. I placed the seeds on each bone and initialize. However, I often find leaks in the first results of segmentation, like such :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c05c55d9fe41f4582ecaf52da2680ce359534d6a.jpeg" data-download-href="/uploads/short-url/rrHv7mYv6e9D7XpniQf26pukAKm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05c55d9fe41f4582ecaf52da2680ce359534d6a_2_690x428.jpeg" alt="image" data-base62-sha1="rrHv7mYv6e9D7XpniQf26pukAKm" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05c55d9fe41f4582ecaf52da2680ce359534d6a_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c05c55d9fe41f4582ecaf52da2680ce359534d6a_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c05c55d9fe41f4582ecaf52da2680ce359534d6a.jpeg 2x" data-dominant-color="8D8A8B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×856 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(the darker shades are the seeding)</p>
<p>I tried to correct it by modifying the Seed Locality Factor, up to 10, but it doesn’t change.</p>
<p>I also use Watershed which usually leaks a bit less. But watershed can’t be constrained in a mask and tends to pick up the cartilage and create junctions between the models. Also I’m interested in segmenting only the cortical bone (hence the constrain on intensity range) which I can’t seem to do with watershed.</p>
<p>I know that I can modify the seeds over and over until I get the right result, but I was wondering if there is some way to improve the initial result for these kind of light leaks.</p>
<p>If anyone has a solution or a trick to help improve that workflow It would be helpful ! Thanks !</p>

---

## Post #2 by @pieper (2022-11-22 18:08 UTC)

<p>Yes, that’s a tricky structure to capture with Grow from Seeds.</p>
<p>Machine learning techniques are starting to work well for this class of problems.  This tool might give an initial good result that could be refined (e.g. with Grow from Seeds) if you need higher resolution:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/wasserth/TotalSegmentator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/wasserth/TotalSegmentator" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/35d73a7274d2aadb316dbdde43af96d631ab67eafbd36d19d72ede763e93339b/wasserth/TotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/wasserth/TotalSegmentator" target="_blank" rel="noopener">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104...</a></h3>

  <p>Tool for robust segmentation of 104 important anatomical structures in CT images - GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104 important anatomical structures in CT images</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @gaoyi.cn (2022-11-23 00:42 UTC)

<p>Hi,</p>
<p>It seems that you are using the region obtained from thresholding as the seeds? If so that may have a drawback that the seeds are too close the to expected boundary.</p>
<p>As a general rule of thumb for the seeding location, I would put the seeds more or less at the “center” of the expected target. So when these seeds “grow out”, it has relatively equal chance in all directions.</p>
<p>If possible could you try this idea in placing the target seeds manually in the “center” of the target?</p>
<p>For the background seeds, usually, I would put in each 2D view a surrounding fence of them around the expected target. But not too close to the expected boundary too. Otherwise these seeds would “leak into the target” causing under-segment.</p>
<p>Let me know if this helps.</p>
<p>Best,</p>
<p>yi</p>

---

## Post #4 by @lassoan (2022-11-23 02:46 UTC)

<p>Propagation on the surface of another segment happens because there is no smoothing constraint in the grow-cut algorithm (in contrast, watershed and most neural networks have some inherent smoothing). Lack of smoothing means potential for very high accuracy and ability to represent arbitrarily complex shapes, but it also means that the results are more susceptible to noise and artifacts.</p>
<p>Most of the time you can remove this surface noise by applying smoothing after region growing, using Smoothing effect Median or Joint smoothing method.</p>

---

## Post #5 by @Vincebisca (2022-11-23 08:59 UTC)

<p>This seems fascinating ! I tried the online version with an abdominal CT and the result is really interesting ! The details were kind of rough tho but as you say, by eroding the result I might use them as seeds for Grow From Seeds or Watershed. Do you know if there is a way to integrate this tool in a Python script in 3D Slicer to produce segments instead of individual nii.gz files?</p>
<p>Thank you very much for this link, it is really interesting !</p>

---

## Post #6 by @Vincebisca (2022-11-23 09:12 UTC)

<p>Hello,</p>
<p>Thank you for your feedback ! Yes, my seeds are from a thresholding based method. I try to generate seeds automatically and for now a threshold based method did the trick. I agree with the drawback you mention, I already eroded the seeds to drive them away from the expected boundary.</p>
<p>I tried the method you suggested, although as I mentionned, I’m interested in constraining the propagation to an editable area, so I don’t need a background.</p>
<p>I painted seeds with 3D brush more central to the segments, but the result is fairly the same :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/544d82c3eab72e0ac4d55caa84f66aa704903a5f.jpeg" data-download-href="/uploads/short-url/c1MaLut8dZMqdaNBeITUfIbEIkD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/544d82c3eab72e0ac4d55caa84f66aa704903a5f_2_690x449.jpeg" alt="image" data-base62-sha1="c1MaLut8dZMqdaNBeITUfIbEIkD" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/544d82c3eab72e0ac4d55caa84f66aa704903a5f_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/544d82c3eab72e0ac4d55caa84f66aa704903a5f_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/544d82c3eab72e0ac4d55caa84f66aa704903a5f_2_1380x898.jpeg 2x" data-dominant-color="62635F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1381×900 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Darker shades are the seeds.</p>
<p>Maybe I did it wrong… However, the idea in my case would be to have seeds generated by a script, so manual painting would kind of defeat the purpose.</p>
<p>Thank you very much for your feedback ! I will search for a way to drive seeds farther away from the expected boundaries !</p>
<p>Vincent</p>

---

## Post #7 by @Vincebisca (2022-11-23 09:19 UTC)

<p>Thank you prof Lasso for these informations. I thought that the seed locality factor in grow from seed would work similarily to the object scale in watershed. If I understand what you said, this doesn’t seem to be the case.</p>
<p>I tried a bit of smoothing and it helps a bit. Thank you ! The downside is that it’s a post-processing operation. Hence the Grow From Seeds needs to be applied first, losing the ability to adjust the seeds if smoothing is not enough… I need to see how I can incorporate smoothing operations in my workflow. Thank you for the tip !</p>

---

## Post #8 by @pieper (2022-11-23 18:28 UTC)

<p>Currently TotalSegmentator can be run independently from Slicer, but the results can be loaded and generally look very nice.  Follow their directions on the github page and run the highest resolution model for best results.  Use the flag, I think it’s <code>--ml</code>, to get a single .nii.gz file you can load as a segmentation.  Yes it should be possible then to use this as input to Grow from Seeds.  I’m not sure how it will do in the face of fractures or other pathology so please report back if you explore this path.</p>

---

## Post #9 by @Vincebisca (2022-11-24 08:37 UTC)

<p>Ok so it can ONLY be run independantly if I understand well. Would be really nice to have a way to use it in Slicer via python scripting. I don’t really know how these thing work.</p>
<p>It does not solde the leaky grow from seeds issue but it is a really nice piece of information that I didn’t have ! Thank you !</p>

---

## Post #10 by @rbumm (2022-11-24 12:57 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="9" data-topic="26382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>Ok so it can ONLY be run independantly if I understand well.</p>
</blockquote>
</aside>
<p>We have included a TotalSegmentator option in the current version of Lung CT Segmenter (Lung CT Analyzer extension) within 3D Slicer. The <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Step-2-Using-Lung-CT-Segmenter-with-AI#totalsegmentator" rel="noopener nofollow ugc">setup</a> is a bit tricky but should be automatic if you already got it going from the command line. You would have to use the “TotalSegmentator all” option on your even non-lung CT dataset and press “Start”. This will take several minutes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d992feff91f2f2e1bf59fb7b1ca63f9027b6cbae.png" data-download-href="/uploads/short-url/v2Ky1oUzWFeUjCIsf88p5Ig8KRw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d992feff91f2f2e1bf59fb7b1ca63f9027b6cbae.png" alt="image" data-base62-sha1="v2Ky1oUzWFeUjCIsf88p5Ig8KRw" width="552" height="500" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">666×603 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and find all &gt; 104 created segments - correctly named -  in “Data”. Just check their “visibility”:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f480e39dcc0b4ea73c5dbc0bff577e6f6db4c7d.png" alt="image" data-base62-sha1="4sJb9EIPWUEVv3CwA9sqb6ojiSV" width="636" height="126"></p>
<p>Having that call in “Lung CT Segmenter” only is probably not ideal. Maybe we should bundle all available pre-trained AI segmentation tools in a central extension …</p>

---

## Post #11 by @pieper (2022-11-24 19:09 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="10" data-topic="26382">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Maybe we should bundle all available pre-trained AI segmentation tools in a central extension …</p>
</blockquote>
</aside>
<p>Yes, this would be ideal as we have several tools that are already valuable to users.  A challenge is that they all have a bit different requirements and interfaces. Plus the field is evolving quickly so by the time we integrate one thing another promising tool emerges.  Also tasks that take more than a few minutes are often more convenient to use outside Slicer.  Still, an nice high end tool for users could be developed.</p>

---

## Post #12 by @lassoan (2022-11-25 06:13 UTC)

<p>TotalSegmentator deserves a separate Slicer extension, so I’ve added it now:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e5125fa931371c415f950d6a052a87d56a1ccaaffed992e24c971a82467733ea/lassoan/SlicerTotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerTotalSegmentator" target="_blank" rel="noopener">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body...</a></h3>

  <p>Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model - GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer usin...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/rbumm">@rbumm</a> you could use this TotalSegmentator extension from LungCTAnalyzer extension. If needed, we can refactor the module logic to allow you to do everything you need with just a few method calls.</p>

---

## Post #13 by @rbumm (2022-11-25 08:20 UTC)

<p>Where should I post technical feedback concerning the new extension <a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #14 by @lassoan (2022-11-25 14:02 UTC)

<p>You can submit issues in that repository - <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues" class="inline-onebox">Issues · lassoan/SlicerTotalSegmentator · GitHub</a></p>

---
