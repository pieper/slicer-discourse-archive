# How to color volume node use lookup table or other method?

**Topic ID**: 32552
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/how-to-color-volume-node-use-lookup-table-or-other-method/32552

---

## Post #1 by @jay1987 (2023-11-02 09:22 UTC)

<p>i have a volume with voxel data value like 0.0001,0.001,0.02,0.1,1,the boss wants to map the voxel data value use log function like 0.0001 maps to log(0.0001),0.02 maps to log(0,02),and than color the volume using jet . the boss also wants to show voxel data in data probe module with the origin value like 0.0001 ,0.02,is is possible to implement such function using slicer script?</p>

---

## Post #2 by @lassoan (2023-11-02 15:33 UTC)

<p>You can create a color node that assigns the desired colors to any voxel value. You can take colors from the “jet” color table (<code>ColdToHotRainbow</code> in Slicer) and assign it to logarithmic values as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend">this example</a>. They key is not to use a color table (that has colors defined at regular intervals in linear space), but a color transfer function (that can assign colors to arbitrary intensity values).</p>

---

## Post #3 by @jay1987 (2023-11-03 03:18 UTC)

<p>thank you lassoan , i use the code you mentioned，it succeed with sample volume like the effect below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67a28dfea090c1871c020e5400d450004d7ff92e.png" data-download-href="/uploads/short-url/eMNrYv6zMpaA7Yk0IdwvoVL3zXw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a28dfea090c1871c020e5400d450004d7ff92e_2_690x331.png" alt="image" data-base62-sha1="eMNrYv6zMpaA7Yk0IdwvoVL3zXw" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a28dfea090c1871c020e5400d450004d7ff92e_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a28dfea090c1871c020e5400d450004d7ff92e_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67a28dfea090c1871c020e5400d450004d7ff92e.png 2x" data-dominant-color="515F5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1267×609 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
but with sparse data ， the same code is failed with the effect below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/142788adcc1529954a7035c2ecb05281d49a2c1a.png" data-download-href="/uploads/short-url/2Sifwy6oYCxClrHxOHiGTkVvmwG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/142788adcc1529954a7035c2ecb05281d49a2c1a_2_690x331.png" alt="image" data-base62-sha1="2Sifwy6oYCxClrHxOHiGTkVvmwG" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/142788adcc1529954a7035c2ecb05281d49a2c1a_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/142788adcc1529954a7035c2ecb05281d49a2c1a_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/142788adcc1529954a7035c2ecb05281d49a2c1a.png 2x" data-dominant-color="2D2DB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1265×607 22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i have tried many ways to solved the problem but all failed . is there a way to color the data i linked below?</p>

---

## Post #4 by @jay1987 (2023-11-03 03:18 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fi/11pfr4z43ob0sytcs4loa/ktrans.nrrd?rlkey=eg06kqypc016oipi9uoh20ba4&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fi/11pfr4z43ob0sytcs4loa/ktrans.nrrd?rlkey=eg06kqypc016oipi9uoh20ba4&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-unknown-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/scl/fi/11pfr4z43ob0sytcs4loa/ktrans.nrrd?rlkey=eg06kqypc016oipi9uoh20ba4&amp;dl=0" target="_blank" rel="noopener nofollow ugc">ktrans.nrrd</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
