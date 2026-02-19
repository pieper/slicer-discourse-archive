---
topic_id: 13971
title: "Segmenting Ge Voluson Ultrasound Image"
date: 2020-10-09
url: https://discourse.slicer.org/t/13971
---

# Segmenting GE Voluson ultrasound image

**Topic ID**: 13971
**Date**: 2020-10-09
**URL**: https://discourse.slicer.org/t/segmenting-ge-voluson-ultrasound-image/13971

---

## Post #1 by @Davide (2020-10-09 17:44 UTC)

<p>I have loaded a dicom file from a GE Voluson S8 but Im not able to segment the volume. Any suggestion?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b87584afceb07ffdf2dfb1a5b3b5d38ad200ba8.jpeg" data-download-href="/uploads/short-url/aM9MH0zmP5ZntRM0qjK8AUxrxgc.jpeg?dl=1" title="fetal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b87584afceb07ffdf2dfb1a5b3b5d38ad200ba8_2_664x500.jpeg" alt="fetal" data-base62-sha1="aM9MH0zmP5ZntRM0qjK8AUxrxgc" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b87584afceb07ffdf2dfb1a5b3b5d38ad200ba8_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4b87584afceb07ffdf2dfb1a5b3b5d38ad200ba8_2_996x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b87584afceb07ffdf2dfb1a5b3b5d38ad200ba8.jpeg 2x" data-dominant-color="2F2F38"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fetal</span><span class="informations">1134×853 57.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-10-10 02:29 UTC)

<p>This looks like a screen capture video, not a 3D/4D volume (most keepsake ultrasounds are saved like this). This cannot be segmented as a volumetric image - you cannot create 3D model from it, 3D print it, etc.</p>

---

## Post #3 by @Davide (2020-10-13 22:27 UTC)

<p>Thank you Andras! We will check the eport options form the ultrasound machine.</p>

---

## Post #4 by @Tflaxman (2022-10-20 01:25 UTC)

<p>Hello,<br>
I am new to the process and tried the same thing as above. Did you find an export option that worked?<br>
Thanks,</p>

---

## Post #5 by @MartinNA (2023-06-17 00:06 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/amkkyaavt3jmpcrbavf67/h?dl=0&amp;rlkey=h64e5zgxtjq65xptwihvdxtqc">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/amkkyaavt3jmpcrbavf67/h?dl=0&amp;rlkey=h64e5zgxtjq65xptwihvdxtqc" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-folder-dropbox-landscape.png" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://www.dropbox.com/scl/fo/amkkyaavt3jmpcrbavf67/h?dl=0&amp;rlkey=h64e5zgxtjq65xptwihvdxtqc" target="_blank" rel="noopener nofollow ugc">Doctor_Retana</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hi<br>
I have a similar problem, I have .vol files from a voluson S8 ultrasound, the doctor gave me the files via USB, when I pass them to slicer an error appears and that it cannot load them. I don’t know if anyone has had the same problem and how do I solve it.</p>

---

## Post #6 by @lizuolin (2024-03-02 01:48 UTC)

<p>If you want to use 3D imaging in GE, you need to export the 4dv format from the machine, and you can only open the file using the software created by their company, and then perform image post-processing.</p>

---
