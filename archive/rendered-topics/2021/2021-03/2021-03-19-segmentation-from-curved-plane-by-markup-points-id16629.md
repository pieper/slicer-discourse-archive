---
topic_id: 16629
title: "Segmentation From Curved Plane By Markup Points"
date: 2021-03-19
url: https://discourse.slicer.org/t/16629
---

# Segmentation from curved plane by markup points

**Topic ID**: 16629
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/segmentation-from-curved-plane-by-markup-points/16629

---

## Post #1 by @hubelef (2021-03-19 05:02 UTC)

<p>Operating system: Mac OS 10.13<br>
Slicer version: 4.11.20200930<br>
Expected behavior: separate segmented volume in two segmented volume by a curved plane (drawn by markup points)<br>
Actual behavior:<br>
I am nuclear medicine physician and I am interested in quantification in nuclear medicine imaging.<br>
For instance, I use Chest Imaging Platform (CIP) extension for interactive lung lobe segmentation.<br>
=&gt; I would like to do the same in liver imaging ie create segmentation in abdominal injected CT based on markup points.</p>
<blockquote>
<p>how can I get a curved plane from the markup points (like in CIP extension) ?<br>
how can I use such a curved plan to separate the pre-segmented whole liver in segments ? For instance I would like to, first, segment the whole liver (threshold +/- growing seeds) and then separate the left/right liver with a curved plane from markup points. Then I could again separate the different segments (1 to 8) with the same method (markup points that delimit a curved plane).<br>
Thank you for your help,<br>
Best regards,<br>
Fabrice Hubele</p>
</blockquote>

---

## Post #2 by @lassoan (2021-03-19 05:29 UTC)

<p>You can create curved surfaces driven by control points using Surface Cut effect in Segment Editor (provided by SegmentEditorExtraEffects extension). If you want to specify more concave surfaces then you may generate a model using MarkupsToModel extension (with Convexity&gt;0 and Force convex output disabled) and import the resulting surface in to segmentation. These tools have been used successfully to split the liver into segments.</p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is currently working on a new curved markups plane type for liver resections, which might be also useful for you.</p>

---

## Post #3 by @hubelef (2021-03-22 19:59 UTC)

<p>Thank you very much for your response.<br>
I apologize because I forgot to ask how to draw a curved plane from markup points in different slice levels ie 2-3 points at the top of the liver (red view), 2-3 points at another z level (still red view but another slice). By the way, how a plane can split a segmented volume in two parts.<br>
I installed the SegmentEitorExtraEffects extension that gives really cool extension : thank you so much for improving this powerful tool.</p>

---

## Post #4 by @lassoan (2021-03-23 05:14 UTC)

<p>I am not sure if you still have some questions. If you do, then please provide some more details, and preferable screenshots to illustrate what you would like to achieve.</p>

---

## Post #5 by @hubelef (2021-04-02 15:38 UTC)

<p>thank you for your response. Yes in fact, I probably mis explained my target, here it is in image : <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09d2cc9dd1e160cedcd1312e9f9102288234cf6a.jpeg" data-download-href="/uploads/short-url/1oTVOYkgBLPoiqLoSmFK0BtS2EO.jpeg?dl=1" title="curved_segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d2cc9dd1e160cedcd1312e9f9102288234cf6a_2_690x487.jpeg" alt="curved_segmentation" data-base62-sha1="1oTVOYkgBLPoiqLoSmFK0BtS2EO" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d2cc9dd1e160cedcd1312e9f9102288234cf6a_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d2cc9dd1e160cedcd1312e9f9102288234cf6a_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09d2cc9dd1e160cedcd1312e9f9102288234cf6a_2_1380x974.jpeg 2x" data-dominant-color="F9FAFA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">curved_segmentation</span><span class="informations">3466×2448 432 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Also I have a second question : how can I make relative threshold (percentage) based on a local maximum ? : <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ce64215b5452b992c6b92d16f3d267eeb2afc97.jpeg" data-download-href="/uploads/short-url/k6saDRxd2oAPGVtpx7ID2VhAu9x.jpeg?dl=1" title="relative_threshold" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ce64215b5452b992c6b92d16f3d267eeb2afc97_2_690x487.jpeg" alt="relative_threshold" data-base62-sha1="k6saDRxd2oAPGVtpx7ID2VhAu9x" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ce64215b5452b992c6b92d16f3d267eeb2afc97_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ce64215b5452b992c6b92d16f3d267eeb2afc97_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ce64215b5452b992c6b92d16f3d267eeb2afc97_2_1380x974.jpeg 2x" data-dominant-color="FCFCFD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">relative_threshold</span><span class="informations">3467×2448 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>  Thank you very much for your help</p>

---

## Post #6 by @pieper (2021-04-02 22:09 UTC)

<p>For the first question is this something like what you are building <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> ?</p>
<p>Regarding your second question, that’s a mode I also want to implement for a PET project I’m involved with.  Probably it can just be a simple segment editor effect that would be used as follows: use the Paint (or any tool) to draw anything that is possibly lesion and then the effect would calculate the max value of the background in that segment and then only keep the places where the background are 41% of that max.  I’m not sure when I get around to it, but I will probably add it to the PETIndiC extension.  As part of that I’ll also try to fix up some of the PET-related extensions that aren’t building with the current preview version of Slicer.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="http://qiicr.org/assets/img/favicon-32x32.png" class="site-icon" width="16" height="16">
      <a href="http://qiicr.org/tool/PETIndiC/" target="_blank" rel="noopener">QIICR</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="http://qiicr.org/tool/PETIndiC/" target="_blank" rel="noopener">PET-IndiC: PET quantification</a></h3>

<p>3D Slicer extension for quantifying uptake in PET</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2021-04-03 00:36 UTC)

<p>We developed the “Surface cut” effect for segmenting liver segments. The effect is available in SegmentEditorExtraEffects extension.</p>
<aside class="quote no-group" data-username="hubelef" data-post="5" data-topic="16629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/e36b37/48.png" class="avatar"> hubelef:</div>
<blockquote>
<p>Also I have a second question : how can I make relative threshold (percentage) based on a local maximum ? :</p>
</blockquote>
</aside>
<p>If you want to do this to avoid relying on absolute density values, then you may be much better off with other tools that rely on intensity differences, such as Grow from seeds, Fast marching, or Watershed.</p>
<p>If you are sure that going with a fixed threshold value is the best then there are some tools that you can leverage. First of all, maximum value is very sensitive - a single noisy voxel can cause large error, so you want to work with the entire histogram.</p>
<ul>
<li>There are 10 automatic threshold computation methods in Threshold effect / Automatic threshold, which uses the entire histogram.</li>
<li>You can also compute a local histogram by drawing a region in any of the slice views. It automatically extracts the histogram’s lower/upper bound and average and you can set the threshold range based on these values. If you confirm on a number of examples that instead of using the lower/upper/average, something like a specific percentile, or percentage of maximum (more robustly: 95th percentile), or something similar work better then we can add such an option there.</li>
</ul>

---

## Post #8 by @pieper (2021-04-03 14:46 UTC)

<p>I agree with the issues you pointed out, that SUVmax can be noisy and that a global threshold may be more robust, but I’ve been told that the 41% of local SUVmax is common in the clinical literature so we should at least support and make it easy to use.  It may get surpassed by other measures when more evidence is accumulated.  Global methods are complicated in PET because of non-disease related metabolism.</p>

---

## Post #9 by @lassoan (2021-04-03 17:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="16629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>41% of local SUVmax is common in the clinical literature</p>
</blockquote>
</aside>
<p>I see. If there are commonly used clinical methods then they need to be implemented as they are, because there may be decades of accumulated data and experience using that specific metric.</p>
<p>How the region is specified for the local maximum computation? Is it the local maximum value in the selected 3D blob? If yes, then I agree that it is a very specific algorithm that is probably the best to implent in a PET extension.</p>

---

## Post #10 by @pieper (2021-04-03 18:40 UTC)

<p>The way it was described to me, the radiologist drags out a rectangular ROI in the slice that looks hottest and gets the max from that and then that is used to get the 41% cutoff for that lesion.  Sometimes people might use SUVpeak, which is like a top percentile or similar to minimize the effect of noise.</p>
<p>For Slicer I was imagining the workflow being something like overpainting the suspected lesion segment and then applying the threshold operation based on the data in that segment (in 3D).</p>
<p>In this use case the challenge apparently is that lesions are typically very hot in the baseline scans but become harder to distinguish as they respond to therapy.</p>
<p>In any case I’ll go through all the PET-related extensions to get them building on the preview release.  From a first look it shouldn’t be too hard.</p>

---

## Post #11 by @hubelef (2021-04-03 19:33 UTC)

<p>That is exactly what we’re doing in clinical use : drag a ROI (spherical for instance, but the paint effect could also be used) and then get the 41% (or another value, typically 40 to 43 % based on old studies) maximum value threshold (based on the SUV or from native series as computing SUV from native series is linear). I agree that this is not a very powerful way to get a segmentation but this a classical way in nuclear medicine  (PET imaging, with hot spots). Also, the Metabolic Tumor Volume (MTV), ie the volume based on this segmentation is a parameter used in therapeutic essais (Lymphoma for instance).<br>
Also, we use this relative threshold in order to make segmentation on PET metabolic imaging and then we send the segmentation to our radiotherapeute (rtstruct) before radiotherapie : the segmentation is called BTV (biological target volume).<br>
Tell me if I can do something (test), comparison / validation with clinical software or whatever.</p>

---

## Post #12 by @lassoan (2021-04-03 23:05 UTC)

<aside class="quote no-group" data-username="hubelef" data-post="11" data-topic="16629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/e36b37/48.png" class="avatar"> hubelef:</div>
<blockquote>
<p>That is exactly what we’re doing in clinical use : drag a ROI (spherical for instance, but the paint effect could also be used) and then get the 41% (or another value, typically 40 to 43 % based on old studies) maximum value threshold (based on the SUV or from native series as computing SUV from native series is linear)</p>
</blockquote>
</aside>
<p>Great! This is almost the same that is already implemented in Threshold effect’s “Local histogram” section. The only missing feature is to choose a percentile value (currently, you can choose the threshold to be at the global minimum/maximum, local minimum/maximum, or local average, but not at a specific percentage).</p>
<p>Moreover, there is an even better tool that you can use, the <strong>Local threshold</strong> effect. You just specify how you want to set the threshold (e.g., 43th percentile to maximum; in the example video below it will be still just average to maximum, because the percentile option does not exist yet), click-and-drag in the image to draw the ROI, and then Ctrl-click to add a segment at that position:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6007acb2d8c8cf3a4e62f4cb26c499118e630651.mp4">
  </div><p></p>

---

## Post #13 by @RafaelPalomar (2021-04-06 13:28 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="16629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For the first question is this something like what you are building <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> ?</p>
</blockquote>
</aside>
<p>Hello. This is similar to what I’m currently working on, but not exactly the same use case. If I understood correctly, <a class="mention" href="/u/hubelef">@hubelef</a> you would like to obtain the Couinaud division of the liver using curved planes? We are working on a curved plane for planning liver resections. The difference is that we don’t manage interactions between resection curved planes (e.g., intersections and differences) that you would need in your approach. We want to tackle segments classification based on classification of portal vein models which should be more precise and less tedious; but this will come after we implement the resection.</p>
<p>Our plan is to release a Slicer Extension for this, but can’t say yet when this would be available.</p>

---

## Post #14 by @zhang_ming (2023-01-09 13:57 UTC)

<p>hello, <strong>Local threshold</strong>  from which extension? I’m looking for the solution to analyze the PET，plz. thank you</p>

---

## Post #15 by @zhang_ming (2023-01-09 14:40 UTC)

<p>SegmentEditorExtraEffects ,lol I found it. but can this set threshold of PET/CT’s SUVmax 40%?</p>

---
