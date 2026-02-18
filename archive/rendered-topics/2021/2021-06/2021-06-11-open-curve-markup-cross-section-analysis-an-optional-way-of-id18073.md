# Open curve markup+cross-section analysis：an optional way of the centerline extraction and measurement of vessel?

**Topic ID**: 18073
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/open-curve-markup-cross-section-analysis-an-optional-way-of-the-centerline-extraction-and-measurement-of-vessel/18073

---

## Post #1 by @chendong9416 (2021-06-11 08:37 UTC)

<p>Now in 3D slicer, the best way for the measurement of aorta is segmentation + centerline extraction + cross-section analysis, however, it is not fitted for some type of aortic disease (intramural hematoma for example), and not fitted for CTA with low quality, other software (such as osirix/3 mensio) offer a better way,  recently i find that open curve markup+cross-section analysis was similar to the way of osirix and 3 mensio, but i’m not sure if it is reasonable in technical aspect, and i wonder if it is possible to make this combination a semi-auto workflow? thanks for your answer!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/282cad0eb697aab26c1c8bf89a51b7c255ce304e.jpeg" data-download-href="/uploads/short-url/5JoODsY84ymQArzRylSKotLW7jo.jpeg?dl=1" title="1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/282cad0eb697aab26c1c8bf89a51b7c255ce304e_2_690x306.jpeg" alt="1.PNG" data-base62-sha1="5JoODsY84ymQArzRylSKotLW7jo" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/282cad0eb697aab26c1c8bf89a51b7c255ce304e_2_690x306.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/282cad0eb697aab26c1c8bf89a51b7c255ce304e_2_1035x459.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/282cad0eb697aab26c1c8bf89a51b7c255ce304e_2_1380x612.jpeg 2x" data-dominant-color="A7A7AC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1.PNG</span><span class="informations">3836×1702 677 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c87da86165ae816711d8615f850de75a22f0e074.jpeg" data-download-href="/uploads/short-url/sBCIiILZmzRucBH7t0JSnzwvcbO.jpeg?dl=1" title="2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c87da86165ae816711d8615f850de75a22f0e074_2_343x499.jpeg" alt="2.PNG" data-base62-sha1="sBCIiILZmzRucBH7t0JSnzwvcbO" width="343" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c87da86165ae816711d8615f850de75a22f0e074_2_343x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c87da86165ae816711d8615f850de75a22f0e074_2_514x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c87da86165ae816711d8615f850de75a22f0e074_2_686x998.jpeg 2x" data-dominant-color="717070"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2.PNG</span><span class="informations">1132×1649 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2021-06-11 10:33 UTC)

<aside class="quote no-group" data-username="chendong9416" data-post="1" data-topic="18073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p>semi-auto workflow</p>
</blockquote>
</aside>
<p>You might segment the hematoma, merge the two models and compute a new centerline. Now segmenting anything with low intensity may be challenging and not repeatable.</p>

---

## Post #3 by @lassoan (2021-06-11 20:53 UTC)

<p>Slicer offers various segmentation tools which can make your centerline extraction much faster if the contrast compared to surrounding structures is good. If you have incomplete filling or low contrast then it may be easier to just draw the open curve manually instead of spending time with segmentation. You can decide which approach is more appropriate for each case.</p>
<p>You can also implement a simple Python scripted module that brings together features from multiple modules: single-click vessel segmentation from Segment Editor’s Local threshold effect, followed by automatic centerline extraction, and curved planar reformatting or cross-section analysis. This would allow you to complete your workflow without switching between modules, with minimum number of clicks.</p>

---

## Post #4 by @chendong9416 (2021-06-12 00:14 UTC)

<p>thanks, my problem was solved</p>

---

## Post #5 by @chir.set (2021-06-13 17:55 UTC)

<p>As an exercise, I segmented manually the thrombus of a complex abdominal aortic aneurysm, and its lumen, as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5485161bd78a18237d8da50a808721e72884bddc.jpeg" data-download-href="/uploads/short-url/c3Hf6UDiAhaeoaliCWETx50fKag.jpeg?dl=1" title="complex_aneurysm_lumen_thrombus" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5485161bd78a18237d8da50a808721e72884bddc_2_591x500.jpeg" alt="complex_aneurysm_lumen_thrombus" data-base62-sha1="c3Hf6UDiAhaeoaliCWETx50fKag" width="591" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5485161bd78a18237d8da50a808721e72884bddc_2_591x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5485161bd78a18237d8da50a808721e72884bddc_2_886x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5485161bd78a18237d8da50a808721e72884bddc.jpeg 2x" data-dominant-color="292220"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">complex_aneurysm_lumen_thrombus</span><span class="informations">1099×929 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It involved :</p>
<ul>
<li>local threshold, for the contrasted lumen</li>
<li>threshold, for masking the thrombus intensities</li>
<li>paint the thrombus manually</li>
<li>remove small islands</li>
<li>fill holes, with the model conversion steps</li>
<li>smoothing</li>
<li>logical operation, to add the lumen and thrombus segments</li>
<li>centerline extraction</li>
</ul>
<p>It took about 30 minutes. It should be shorter for less complex structures, or for small amount of thrombus as in your image.</p>
<p>My conclusion is that it’s more satisfactory than expecting a fully algorithmic method (kind of, it’s always complex code behind the scene). It may even be shorter that correcting leaks of fully algorithmic tools like Grow from seeds or Flood filling.</p>
<p>It’s not a magical approach, and cannot be used on a daily basis, but on a per-case basis. At least, the expected final result is there.</p>
<p>Regards.</p>

---

## Post #6 by @chendong9416 (2021-06-14 00:54 UTC)

<p>the result is good, but as you said, it is for case, not for daily basis, the approach I said provided a reasonable and faster way, it is fitted especially when you have hundreds of cases to handle, thanks anyway</p>

---

## Post #7 by @lassoan (2021-06-16 23:03 UTC)

<p>Note that if you know what exactly you want to do then you can probably automate the process that <a class="mention" href="/u/chir.set">@chir.set</a> described so that you can complete it in a few minutes instead of 30 minutes. We did this for example for the <a href="https://youtu.be/v1-L_niLZxQ">COVID lung CT segmentation module</a>.</p>
<p>For this, you need to develop a custom module that leads the user through the workflow and automates the steps as much as possible. Developing such a module could take a few days, may be up to a few weeks (if you want a lot of features or if the software developer is new to Slicer). The cost of this development should be negligible if you want to use this tool on a daily basis.</p>

---
