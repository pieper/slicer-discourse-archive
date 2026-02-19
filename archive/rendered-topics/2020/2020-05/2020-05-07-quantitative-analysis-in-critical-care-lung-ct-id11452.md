---
topic_id: 11452
title: "Quantitative Analysis In Critical Care Lung Ct"
date: 2020-05-07
url: https://discourse.slicer.org/t/11452
---

# Quantitative analysis in critical Care Lung CT

**Topic ID**: 11452
**Date**: 2020-05-07
**URL**: https://discourse.slicer.org/t/quantitative-analysis-in-critical-care-lung-ct/11452

---

## Post #1 by @titotitoide (2020-05-07 20:11 UTC)

<p>Hi everyone! First of all thanks for this amazing, stunning and overwhelming software.<br>
I am working with lung CT in critical care where usually patients are sick and have an abnormal lung CT with lung collapse and huge heterogeneities. When I use the parenchyma analysis module it fails to delineate the lung as a result of the important lung alterations it means, areas of lung collapse that has HU 0 +100 etc. For these reasons software are only capable of analyze the aereated lung areas excluding non aereated areas and therefore the final lung analysis is not real. Mi question is: How can I analyze the whole lung (including non aereated areas, fibrosis areas) to known the Kurtosis, Skewness and heterogeinity index ? Of course excluding the mediastinum etc.<br>
I include a picture in wich the automatic parenchyma analysis fails.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1d68eaa3aeb9799611d3f0cbd58587cfd675f04.jpeg" alt="Fail" data-base62-sha1="rELPZO66lTlMH0S7QykcVFQjQuE" width="399" height="421"></p>

---

## Post #2 by @pieper (2020-05-07 20:31 UTC)

<p>Hi -</p>
<p>Thanks for including the screenshot - that will help solicit ideas.  I agree, this one looks tough and you’ll probably need to resort to semi-automated techniques.  Probably Grow From Seeds in the Segment Editor module (using the nightly preview) is the best bet.  Given the noise and contrast similarity between the tissues I’m not sure if you’ll be able to get a completely satisfying result, but it’s worth trying.</p>

---

## Post #3 by @lassoan (2020-05-07 22:07 UTC)

<p>I agree, Grow from seeds most likely will work well.</p>
<p>If you find that you spend too much time with adjusting your seeds then you can may try “Fill between slices” effect. In this case, you need to segment about 10-15 slices and the Slicer creates a full segmentation by smoothly interpolating between them.</p>
<p>If you can share a few deidentified sample images then we can help you finding a very efficient segmentation workflow.</p>

---

## Post #4 by @rbumm (2020-12-16 21:26 UTC)

<p>Hi -<br>
With “Lung CT Analyzer” we have published a new Slicer extension which might help a lot here. You may want to take a closer look at it. You can freely define your thresholds for ventilated, infiltrated, and collapsed lung areas create dedicated segmentations, and calculate their individual volumes.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars0.githubusercontent.com/u/18140094?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/rbumm/SlicerLungCTAnalyzer" target="_blank" rel="noopener nofollow ugc">rbumm/SlicerLungCTAnalyzer</a></h3>


  <p><span class="label1">This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in chest CT examinations.   </span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you have questions let me know.</p>

---
