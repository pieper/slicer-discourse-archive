# MRI intensity normalization

**Topic ID**: 4830
**Date**: 2018-11-21
**URL**: https://discourse.slicer.org/t/mri-intensity-normalization/4830

---

## Post #1 by @TingtingYu (2018-11-21 08:26 UTC)

<p>Hi,</p>
<p>I am wondering how to apply “μ±3σ” normalization method in 3D slicer. I found a filter named “NormalizeImageFilter” which normalize an image by setting its mean to zero and variance to one. Can I modify this “NormalizeImageFilter” and turn it into  “μ±3σ” normalization method.</p>
<p>I am also reading a paper written by Schwier_et_al.,2018, this paper mentions that “Basic normalization was performed by scaling and shifting the values of the whole image to a mean signal value of 300 and a standard deviation of 100”, is that “μ±3σ” normalization method?</p>
<p>Best,<br>
Tingting<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affc54b7fa1a3dbb888d5022198707e7b8ca4d9a.png" data-download-href="/uploads/short-url/p6QaMj9iCLkAQBFIpqooSABQDGy.png?dl=1" title="Title" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affc54b7fa1a3dbb888d5022198707e7b8ca4d9a.png" alt="Title" data-base62-sha1="p6QaMj9iCLkAQBFIpqooSABQDGy" width="690" height="193" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Title</span><span class="informations">952×267 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Radiologist00 (2023-06-11 21:02 UTC)

<p>I’m having the same problem, can anyone help me, thanks in advance</p>

---

## Post #3 by @rbumm (2023-06-13 05:27 UTC)

<p>This paper includes a method that we developed for CT normalization recently.<br>
Sources are available online.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.researchsquare.com/article/rs-3027617/v3">
  <header class="source">
      <img src="https://www.researchsquare.com/static/favicons/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://www.researchsquare.com/article/rs-3027617/v3" target="_blank" rel="noopener">researchsquare.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.researchsquare.com/article/rs-3027617/v3" target="_blank" rel="noopener">From Voxels to Prognosis: AI-Driven Quantitative Chest CT Analysis Forecasts...</a></h3>

  <p>Background: The current study aimed to investigate the distribution and extent of lung involvement in patients with COVID-19, assess the relationship between lung involvement and the need for intensive care unit (ICU) admission and compare the...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Radiologist00 (2023-06-13 05:59 UTC)

<p>Thank you for your answer, but it was a simple thing I wanted to ask. When we use the ‘normalize imaging filter’ option in the 3D slicer, do outlier pixels are removed, is there a different outlier option?</p>

---

## Post #5 by @rbumm (2023-06-13 06:13 UTC)

<aside class="quote no-group" data-username="Radiologist00" data-post="4" data-topic="4830">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/82dd89/48.png" class="avatar"> Radiologist00:</div>
<blockquote>
<p>do outlier pixels are removed, is there a different outlier option?</p>
</blockquote>
</aside>
<p>GPT 3.5:</p>
<p>In 3D Slicer, the “Normalize” imaging filter is primarily used to rescale the intensity values of an image to a specific range, typically between 0 and 1. This filter does not specifically target outlier pixels.</p>
<p>If you want to remove outlier pixels from your image, you would typically use a different filtering technique or algorithm. 3D Slicer offers various image processing filters that can help with outlier removal, such as median filtering, mean filtering, or Gaussian filtering. These filters can smooth the image and reduce the impact of outliers.</p>
<p>Additionally, you can apply advanced statistical methods or custom algorithms to specifically identify and remove outlier pixels. These methods often involve analyzing the distribution of pixel intensities and determining a threshold or criterion for identifying outliers.</p>
<p>In summary, the “Normalize” filter in 3D Slicer is not designed to remove outlier pixels. To address outliers, you would need to explore other filtering techniques or utilize statistical methods tailored for outlier detection and removal.</p>

---
