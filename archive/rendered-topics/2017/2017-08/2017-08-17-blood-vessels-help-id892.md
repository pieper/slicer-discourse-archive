---
topic_id: 892
title: "Blood Vessels Help"
date: 2017-08-17
url: https://discourse.slicer.org/t/892
---

# Blood Vessels (HELP)

**Topic ID**: 892
**Date**: 2017-08-17
**URL**: https://discourse.slicer.org/t/blood-vessels-help/892

---

## Post #1 by @Fefe (2017-08-17 19:56 UTC)

<p>Hi Guys, I know that there are a lot of topics but I’ve been trying to segment blood vessels. I’ve been trying to segment liver vessels, coronary artery and aorta for one week nonstop but I’am unsuccessful. I would like to know what is the best method for this one. I tried Vesselness Filtering, Level Set Segmentation and sometimes I don’t really know if I understand what I’m doing. Do you have guys some step-by-step manual how to do what I need ? Actually my main goal is to segment liver (done) then I would segment tumor which is located in the liver (done) and then I would finally segment the vessels which lead to the tumor. I’ve segmented liver and tumor already but I need the vessels. Thank you a lot for your response and I would appreciate it if anyone know the answer for my issue.</p>

---

## Post #2 by @pieper (2017-08-17 20:36 UTC)

<p>It would help if you provided some screenshots of the the data you are trying to segment and what kind of results you are getting.</p>
<p>Vessels in the liver can be hard to get, but if you have a good contrast enhanced CT they show up very well and should be possible to segment with thresholding.  Also a typical liver CTA will have multiple studies related to the different phases of contrast (arterial, venous…) <a href="http://www.radiologyassistant.nl/en/p52c04470dbd5c/ct-contrast-injection-and-protocols.html">This looks like a nice summary page.</a>)</p>

---

## Post #3 by @lassoan (2017-08-17 20:39 UTC)

<p>Do you use contrast agent? Without that, segmenting liver vessels is really hard. You can then use the Segment editor with vesselness filtering result as master volume and trace the vessels using Paint effect with thresholding. Level set is only for making the vessel segmentation result smoother, but it requires a reasonably good quality input, which you will not likely to get without contrast agent.</p>
<p><a class="mention" href="/u/lcoram">@lcoram</a> you have segmented a lot of liver images with Slicer, do you have any further advice?</p>

---

## Post #4 by @lcoram (2017-08-17 22:34 UTC)

<p>As Andras says, its rather difficult to segment vessels without contrast enhanced images.</p>
<p>Our repo is public now, so if you want to have a try at compiling and using our vessel segmentation module you can (I am still dealing with some bugs, code refactoring, documentation, etc. so its not really “released” yet):<br>
<a href="https://github.com/TheInterventionCentre/NorMIT-Plan/tree/feature/vessel_segmentation_integration" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/TheInterventionCentre/NorMIT-Plan/tree/feature/vessel_segmentation_integration</a><br>
You can let me know if you come across any problems, we hope to release a more tested version this fall (along with information about how to use the modules). Basically you can try preprocessing your image to increase the vessel contrast, then use the vessel segmentation section: select portal or hepatic and place 2 seeds (1st one higher in the vessel and 2nd one slightly lower down to give the algorithm a direction to start) and try running the segmentation.</p>
<p>A postdoctoral fellow has worked on the vessel segmentation algorithm that is implemented as an ITK filter. We have generally worked with contrast enhanced CT images… so the image preprocessing is tailored more towards that (but you can adjust the inputs and see if you can get something to work with non-contrast images).</p>

---

## Post #5 by @Fefe (2017-08-18 08:44 UTC)

<p>I think that there is a contrast agent but I’m not so skilled in this field because I’ve never segmented arteries or veins at all. So as <a class="mention" href="/u/lcoram">@lcoram</a> and <a class="mention" href="/u/lassoan">@lassoan</a> said I need contrast enhanced CT image, but I think that this one is contrast enhanced, do you agree ? So Guys the best way how to do what I need is to segment vessels by using Thresholding in the Segment Editor ? As I said, I’m not so skilled in this field so every advice is useful for me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb8a9795c17d6105d5cc8b65ee1eb15f78bea28.jpeg" data-download-href="/uploads/short-url/fNu9OpQ1pThKtT2YTtMeFrVD1Vu.jpg?dl=1" title="10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6eb8a9795c17d6105d5cc8b65ee1eb15f78bea28_2_555x500.jpg" alt="10" data-base62-sha1="fNu9OpQ1pThKtT2YTtMeFrVD1Vu" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6eb8a9795c17d6105d5cc8b65ee1eb15f78bea28_2_555x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6eb8a9795c17d6105d5cc8b65ee1eb15f78bea28_2_832x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6eb8a9795c17d6105d5cc8b65ee1eb15f78bea28_2_1110x1000.jpg 2x" data-dominant-color="8F8F8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10</span><span class="informations">2894×2604 1010 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lcoram (2017-08-18 15:41 UTC)

<p>Well, I am not sure how effective it is to segment the vessels with thresholding - but it could work if they are a differentiable enough intensity vs the parenchyma. Like I said previously, it may help to use certain ITK filters to preprocess the image to further enhance the vessel / parenchyma contrast. Our module implements a seed based vessel segmentation algorithm:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://link.springer.com/springerlink-static/409335052/images/favicon/favicon.ico" class="site-icon" width="48" height="48">
      <a href="https://link.springer.com/chapter/10.1007/978-3-319-11128-5_31" target="_blank" rel="nofollow noopener">SpringerLink</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:153/232;"><img src="https://static-content.springer.com/cover/book/978-3-319-11128-5.jpg" class="thumbnail" width="153" height="232"></div>

<h3><a href="https://link.springer.com/chapter/10.1007/978-3-319-11128-5_31" target="_blank" rel="nofollow noopener">Blood Vessel Segmentation and Centerline Tracking Using Local Structure Analysis</a></h3>

<p>Blood vessel visualization is important for improving planning and navigation of several interventional procedures. In this paper, we present a novel method for simultaneous blood vessel...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
You place seeds in the veins (portal or hepatic) and then the algorithm tries to move down the vessel tree. This may be more accurate / localized if you are segmenting vessels, vs the more general method of using thresholding.</p>

---
