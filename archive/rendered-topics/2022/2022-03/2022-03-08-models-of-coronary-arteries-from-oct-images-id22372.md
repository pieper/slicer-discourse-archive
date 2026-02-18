# Models of coronary arteries from OCT images

**Topic ID**: 22372
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/models-of-coronary-arteries-from-oct-images/22372

---

## Post #1 by @mkozlowski (2022-03-08 15:03 UTC)

<p>Operating system: masOS High Sierra<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8</p>
<p>Hello!</p>
<p>I would like to ask for advice about preparation of 3D models of coronary arteries for printing based on OCT data. I’ve read the previous conversations that dealt with this topic but unfortunately did not find an answer. Basically I have uploaded DICOM data form OCT to Slicer. I have converted my images to grayscale. Then I did segmentation (watershed and some manual with paint) but have finally arrived at a very unsatisfactory result (see link for the file below). After reading some papers online it seems that the reason for this is that I have not taken into account the curvature of the vessel which can’t be extracted from OCT. Other people have extracted center lines of coronary arteries from coronary angiography, evenly divided the center line according to the number of pictures in the OCT and set a plane perpendicular to the center line at each point. Then each frame from OCT was supposedly placed in the corresponding plane. I have no idea what software they used. Is there any was to do the same thing in Slicer?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/wdt43opyi112md1/coronary%20model%20OCT.stl?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/wdt43opyi112md1/coronary%20model%20OCT.stl?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://www.dropbox.com/s/wdt43opyi112md1/coronary%20model%20OCT.stl?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @lassoan (2022-04-04 15:12 UTC)

<p>It is hard to tell from the end result what could have been done better. If you can share a typical image that you need to segment then we should be able to give advice.</p>

---
