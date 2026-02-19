---
topic_id: 40412
title: "Extension For 2D X Ray Bone Segmentation"
date: 2024-11-27
url: https://discourse.slicer.org/t/40412
---

# Extension for 2D x-ray bone segmentation?

**Topic ID**: 40412
**Date**: 2024-11-27
**URL**: https://discourse.slicer.org/t/extension-for-2d-x-ray-bone-segmentation/40412

---

## Post #1 by @FelixBoenke (2024-11-27 17:18 UTC)

<p>I am currently working on a 2D X-ray segmentation task for long-leg radiographs using 3D Slicer.</p>
<p>To optimize my workflow and reduce the manual segmentation workload, I explored interactive segmentation models based on SAM-2 and the semi-automatic Segment Editor functions. Unfortunately, despite testing several extensions within 3D Slicer, I haven’t achieved satisfactory results for bone segmentation in 2D X-rays.<br>
As I am in the role of „clinician“ and my software skillset is limited, I am not shure wether those results can be attributed to the model not fitting the task, wrong settings or something else.</p>
<p>Does anyone know of any tools or methods specifically designed for accurate bone segmentation in 2D long-leg radiographs?</p>
<p>I greatly appreciate any insights or recommendations you might have!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54c3d0f97b29614e099d0ee794842ba4631bf558.jpeg" data-download-href="/uploads/short-url/c5RDNVn3AVVuU6uRUREeMDv6QI0.jpeg?dl=1" title="Bildschirmfoto 2024-11-27 um 15.55.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54c3d0f97b29614e099d0ee794842ba4631bf558_2_353x500.jpeg" alt="Bildschirmfoto 2024-11-27 um 15.55.27" data-base62-sha1="c5RDNVn3AVVuU6uRUREeMDv6QI0" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54c3d0f97b29614e099d0ee794842ba4631bf558_2_353x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54c3d0f97b29614e099d0ee794842ba4631bf558_2_529x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54c3d0f97b29614e099d0ee794842ba4631bf558_2_706x1000.jpeg 2x" data-dominant-color="A88B92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2024-11-27 um 15.55.27</span><span class="informations">1008×1426 67.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-11-27 19:15 UTC)

<p>We typically work with native 3D datasets, but the Grow from seeds option in the Segment Editor should work.  Did you try it?</p>
<p>Also there’s some work ongoing to integrate this method.  There are some results for hip xrays.  There’s a demo on huggingface where you can upload your own data to try.  If it works well report back and that’ll give extra inspiration to get it integrated with Slcier.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://scribbleprompt.csail.mit.edu/">
  <header class="source">
      <img src="https://scribbleprompt.csail.mit.edu/assets/favicon.ico" class="site-icon" width="" height="">

      <a href="https://scribbleprompt.csail.mit.edu/" target="_blank" rel="noopener">scribbleprompt.csail.mit.edu</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://scribbleprompt.csail.mit.edu/" target="_blank" rel="noopener">ScribblePrompt</a></h3>

  <p>ScribblePrompt: Fast and Flexible Interactive Segmentation for Any Biomedical Image</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
