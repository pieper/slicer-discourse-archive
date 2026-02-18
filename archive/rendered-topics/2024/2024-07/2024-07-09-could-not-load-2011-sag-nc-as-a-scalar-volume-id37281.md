# Could not load: 2011: SAG NC as a Scalar Volume

**Topic ID**: 37281
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/could-not-load-2011-sag-nc-as-a-scalar-volume/37281

---

## Post #1 by @Mike (2024-07-09 14:03 UTC)

<p>Hi this is my first post, I been trying to open this CT for over 3-5 days and I can’t open it, I have 5.6.1 Stable 3D Slicer version. I’m from Mexico and this TC was taken at Thailand.<br>
I can view Dicom Metadata but can´t open it. I tried using PACS Software to export it again (CD Software) but doesn’t work I need to convert it into a STL file for printing I have made alot of STLs but can’t open this one. Also tried to import .bmp images but I didn’t success with it, I don’t have too much experience with converting dicom files<br>
Here are 2 links:<br>
First one has the exported dicom files from Hospital that I asked again (just dicom files)<br>
The second link has everything from CD (software PACS to open CT, dicoms, etc).</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/7c45f2eae611331a50bdd8a1b95079d720240709063406/7c209a">
  <header class="source">
      <img src="https://wetransfer.com/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/7c45f2eae611331a50bdd8a1b95079d720240709063406/7c209a" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://wetransfer.com/downloads/7c45f2eae611331a50bdd8a1b95079d720240709063406/7c209a" target="_blank" rel="noopener nofollow ugc">Jaimie_DICOM</a></h3>

  <p>989 files sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/c74b112228f2b57a4ef326a164e6c38520240709064053/ca1c4e">
  <header class="source">
      <img src="https://wetransfer.com/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/c74b112228f2b57a4ef326a164e6c38520240709064053/ca1c4e" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://wetransfer.com/downloads/c74b112228f2b57a4ef326a164e6c38520240709064053/ca1c4e" target="_blank" rel="noopener nofollow ugc">CD</a></h3>

  <p>1060 files sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @Mike (2024-07-10 08:33 UTC)

<p>Update: Yesterday I tried patching multiple times but it says “examining… not  dicom file, skipped”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c5bd8bfa406761ef8f70feab796566d838b407.jpeg" data-download-href="/uploads/short-url/ndX0riK6wbfxc5O7BaKIpCukGrl.jpeg?dl=1" title="Sin título" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c5bd8bfa406761ef8f70feab796566d838b407_2_410x500.jpeg" alt="Sin título" data-base62-sha1="ndX0riK6wbfxc5O7BaKIpCukGrl" width="410" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c5bd8bfa406761ef8f70feab796566d838b407_2_410x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c5bd8bfa406761ef8f70feab796566d838b407.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c5bd8bfa406761ef8f70feab796566d838b407.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título</span><span class="informations">443×540 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2024-07-10 09:15 UTC)

<p>Have you tried the DICOM patcher module?<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html</a></p>

---

## Post #4 by @Mike (2024-07-11 05:26 UTC)

<p>Yes, it didn’t work (posted screenshot) says “Not DICOM file. Skipped”.</p>

---

## Post #5 by @pieper (2024-07-11 11:50 UTC)

<p>I couldn’t spend much time on it, but the files I looked at were missing the metaheaders, so they are very noncompliant.  I don’t know of a good solution for that.</p>

---

## Post #6 by @Mike (2024-07-13 04:47 UTC)

<p>Update: Found a solution, exported to JPG or BMP from the CD’s software and imported it as multiple images in Slicer 3D and exported it as STL, it is not 1:1 scale but I escalated it measuring in the TC and Blender. Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65669b92403385638ab92d1b5b71a98356ba350.jpeg" data-download-href="/uploads/short-url/z9cAZFH1HGDhvnrd56Tx9qO9DXi.jpeg?dl=1" title="Sin título2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65669b92403385638ab92d1b5b71a98356ba350_2_690x372.jpeg" alt="Sin título2" data-base62-sha1="z9cAZFH1HGDhvnrd56Tx9qO9DXi" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65669b92403385638ab92d1b5b71a98356ba350_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f65669b92403385638ab92d1b5b71a98356ba350_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f65669b92403385638ab92d1b5b71a98356ba350.jpeg 2x" data-dominant-color="7C7C7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título2</span><span class="informations">1065×575 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Mike (2024-07-13 04:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/291650287cdd2bc7b06c8e9e812daf446fd28e3d.jpeg" data-download-href="/uploads/short-url/5RtnG6TJohbOQWDi0peToCfdQxD.jpeg?dl=1" title="Sin título3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291650287cdd2bc7b06c8e9e812daf446fd28e3d_2_666x500.jpeg" alt="Sin título3" data-base62-sha1="5RtnG6TJohbOQWDi0peToCfdQxD" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291650287cdd2bc7b06c8e9e812daf446fd28e3d_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291650287cdd2bc7b06c8e9e812daf446fd28e3d_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291650287cdd2bc7b06c8e9e812daf446fd28e3d_2_1332x1000.jpeg 2x" data-dominant-color="535251"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título3</span><span class="informations">1600×1200 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5696d48cc184a2d771b29e5a1810686eef60127.jpeg" data-download-href="/uploads/short-url/nBiEQ2juGeeXiP56pSt9Au7lXrF.jpeg?dl=1" title="Sin título4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5696d48cc184a2d771b29e5a1810686eef60127_2_666x500.jpeg" alt="Sin título4" data-base62-sha1="nBiEQ2juGeeXiP56pSt9Au7lXrF" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5696d48cc184a2d771b29e5a1810686eef60127_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5696d48cc184a2d771b29e5a1810686eef60127_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5696d48cc184a2d771b29e5a1810686eef60127_2_1332x1000.jpeg 2x" data-dominant-color="595857"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título4</span><span class="informations">1600×1200 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fc997d055fb2548d5acd8554cdf61bb8b9eb9e0.jpeg" data-download-href="/uploads/short-url/bnPD8qvIYHBFSbhlqwWMWyOHu1y.jpeg?dl=1" title="Sin título5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc997d055fb2548d5acd8554cdf61bb8b9eb9e0_2_690x372.jpeg" alt="Sin título5" data-base62-sha1="bnPD8qvIYHBFSbhlqwWMWyOHu1y" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc997d055fb2548d5acd8554cdf61bb8b9eb9e0_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc997d055fb2548d5acd8554cdf61bb8b9eb9e0_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fc997d055fb2548d5acd8554cdf61bb8b9eb9e0_2_1380x744.jpeg 2x" data-dominant-color="232323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título5</span><span class="informations">1913×1033 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63aa8308966d3847ace2bf929ebe53c1cb2580ed.jpeg" data-download-href="/uploads/short-url/edGAy8YEfMUr6u6PVvbtHFjqLjn.jpeg?dl=1" title="Sin título6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63aa8308966d3847ace2bf929ebe53c1cb2580ed_2_551x500.jpeg" alt="Sin título6" data-base62-sha1="edGAy8YEfMUr6u6PVvbtHFjqLjn" width="551" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63aa8308966d3847ace2bf929ebe53c1cb2580ed_2_551x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63aa8308966d3847ace2bf929ebe53c1cb2580ed_2_826x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63aa8308966d3847ace2bf929ebe53c1cb2580ed.jpeg 2x" data-dominant-color="5D5C5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título6</span><span class="informations">1007×913 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/738d09b456de72433a87ac108a8e56073a003643.jpeg" data-download-href="/uploads/short-url/gud5305aDh8m60Tcwu4NdiPbISD.jpeg?dl=1" title="Sin título7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738d09b456de72433a87ac108a8e56073a003643_2_690x359.jpeg" alt="Sin título7" data-base62-sha1="gud5305aDh8m60Tcwu4NdiPbISD" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738d09b456de72433a87ac108a8e56073a003643_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738d09b456de72433a87ac108a8e56073a003643_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738d09b456de72433a87ac108a8e56073a003643_2_1380x718.jpeg 2x" data-dominant-color="424241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sin título7</span><span class="informations">1867×973 356 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
