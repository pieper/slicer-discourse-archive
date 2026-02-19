---
topic_id: 15204
title: "Creating A Lumen From An Stl File"
date: 2020-12-23
url: https://discourse.slicer.org/t/15204
---

# Creating a lumen from an STL file

**Topic ID**: 15204
**Date**: 2020-12-23
**URL**: https://discourse.slicer.org/t/creating-a-lumen-from-an-stl-file/15204

---

## Post #1 by @Andreas (2020-12-23 22:42 UTC)

<p>Hello everyone,</p>
<p>I attached cylinders to my vessel model using CAD software and saved them as STL file and printed them. I poured epoxy resin into the printed vessel model to recreate the lumen. Unfortunately, I did not save this segmentation.</p>
<p>Is it possible to reconstruct the lumen afterwards by means of an STL file?</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/2igve0mud6rwe9v/Segmentation_aci4%20zylindernew.STL?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/2igve0mud6rwe9v/Segmentation_aci4%20zylindernew.STL?dl=0" target="_blank" rel="noopener nofollow ugc">Segmentation_aci4 zylindernew.STL</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2021-01-06 00:12 UTC)

<p>I loaded the STL file as segmentation by selecting “Segmentation” in Description column in Add data dialog. Then set segmentation geometry, specifying spacing of 0.1mm. Added caps to the open ends and fixed holes due to the incorrectly attached inflow/outflow cylinders (to make the lumen a closed space). Finally, filled in the lumen using Islands effect / Add island.</p>
<p>You can download the result from here: <a href="https://1drv.ms/u/s!Arm_AFxB9yqHxOl-Slfi-afs1g2opQ?e=yNPqbu" class="inline-onebox">Microsoft OneDrive</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b702a83e379582640395faa163a001795bf9701.png" data-download-href="/uploads/short-url/aLm7KsQr2meiqi2wkGVF3g7Tsvn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b702a83e379582640395faa163a001795bf9701_2_489x500.png" alt="image" data-base62-sha1="aLm7KsQr2meiqi2wkGVF3g7Tsvn" width="489" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b702a83e379582640395faa163a001795bf9701_2_489x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b702a83e379582640395faa163a001795bf9701_2_733x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b702a83e379582640395faa163a001795bf9701_2_978x1000.png 2x" data-dominant-color="575668"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1088×1112 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Andreas (2021-01-06 01:15 UTC)

<p>Thank you very much for the detailed approach and editing of the file. You are a great support.</p>

---
