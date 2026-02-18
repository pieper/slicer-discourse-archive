# How does the aortic diameter in cross-section analysis calculated?

**Topic ID**: 14653
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/how-does-the-aortic-diameter-in-cross-section-analysis-calculated/14653

---

## Post #1 by @chendong9416 (2020-11-17 02:48 UTC)

<p>Hi, i just want to know how the aortic diameter shown in cross-section analysis (after extract centerline)  is calculated, thanks.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/874dc178f6f42f13f66bb36eaf37559bb9629d46.png" data-download-href="/uploads/short-url/jiX343bchFS2QQfinoEme8kOIuy.png?dl=1" title="捕获1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/874dc178f6f42f13f66bb36eaf37559bb9629d46_2_690x277.png" alt="捕获1" data-base62-sha1="jiX343bchFS2QQfinoEme8kOIuy" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/874dc178f6f42f13f66bb36eaf37559bb9629d46_2_690x277.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/874dc178f6f42f13f66bb36eaf37559bb9629d46_2_1035x415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/874dc178f6f42f13f66bb36eaf37559bb9629d46.png 2x" data-dominant-color="888787"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获1</span><span class="informations">1232×495 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-11-17 05:28 UTC)

<p>Cross-section is computed by extract centerline module, using <a href="http://www.vmtk.org/">VMTK</a>.</p>

---

## Post #3 by @chendong9416 (2020-11-17 05:38 UTC)

<p>sorry, i mean does the aortic diameter shown in the cross-section analysis refer to  (1) from anterior to posterior wall (APD), (2) from right to left lateral wall (transD), (3) maximal diameter in any direction (axialDmax) or (4) perpendicular to axialDmax (shortaxisD)?</p>

---

## Post #4 by @lassoan (2020-11-17 05:41 UTC)

<p>Vessel diameter is computed as diameter of maximal inscribed sphere. See VMTK documentation for details.</p>

---

## Post #5 by @chendong9416 (2020-11-17 06:02 UTC)

<p>how can i get the VMTK documentation?</p>

---

## Post #6 by @lassoan (2020-11-17 06:03 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="http://www.vmtk.org/resources/favicon.ico" class="site-icon" width="16" height="16">
      <a href="http://www.vmtk.org/documentation/" target="_blank" rel="noopener">vmtk.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="http://www.vmtk.org/documentation/" target="_blank" rel="noopener">Learn vmtk | vmtk - the Vascular Modelling Toolkit</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @chendong9416 (2020-11-17 06:26 UTC)

<p>sorry to say that i didn’t find any information about “diameter” in VMTK documentation,  another questioin is how can i show the line measuring the diameter in the image of cross-section analysis?</p>

---

## Post #8 by @chir.set (2020-11-17 08:24 UTC)

<p>It’s an average diameter. The question of a static line does not convey much relevance, and is not involved by VMTK computation. Around the centerline at any point, you can draw as many lines as you want, each with a different diameter. The average diameter has sufficient clinical meaning. Think of it as : “at this point, the lumen is a circle with such diameter”.</p>

---

## Post #9 by @chendong9416 (2020-11-17 08:39 UTC)

<ol>
<li>I think it’s worthy to find out, cause we may need to define it in furture papper</li>
<li>I would like to accept the average diameter explanation, but how does it calculated?it is an average diameter from what?</li>
</ol>

---

## Post #10 by @JohnMiles (2020-11-18 12:05 UTC)

<p>Great topic, useful and explicit, thanks! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
