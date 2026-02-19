---
topic_id: 13163
title: "Loading Philips 3D Us"
date: 2020-08-25
url: https://discourse.slicer.org/t/13163
---

# Loading Philips 3D US

**Topic ID**: 13163
**Date**: 2020-08-25
**URL**: https://discourse.slicer.org/t/loading-philips-3d-us/13163

---

## Post #1 by @Rodrigo_Visconti (2020-08-25 22:49 UTC)

<p>I tried to load this file but it seems to be distorted. I can’t save in the cartesian dicom with the Philips software. There’s a way to correct it?<br>
<a href="https://1drv.ms/u/s!AngD48X_D6KrgaQZHV83Zit8bPm_0g" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/u/s!AngD48X_D6KrgaQZHV83Zit8bPm_0g</a></p>

---

## Post #2 by @Rodrigo_Visconti (2020-10-05 11:43 UTC)

<p>I didn’t got a response. There’s some way to fix this image?</p>

---

## Post #3 by @issakomi (2020-10-05 17:10 UTC)

<p>The DICOM file is formally <em>Ultrasound Multi-frame Image Storage</em> , but in fact some private Philips format with tons of private tags. Seems to be <em>Native 3D Cartesian</em> (see 0x200d,0x2005). I think i could guess spacing from private tags, looks like<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04641e92b4b9dd6a1e31853ab8d58ec0b340d73.jpeg" data-download-href="/uploads/short-url/w01tIro5vCiprMxn4XiQaaSzeQr.jpeg?dl=1" title="20201005-190140" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04641e92b4b9dd6a1e31853ab8d58ec0b340d73_2_497x500.jpeg" alt="20201005-190140" data-base62-sha1="w01tIro5vCiprMxn4XiQaaSzeQr" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04641e92b4b9dd6a1e31853ab8d58ec0b340d73_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04641e92b4b9dd6a1e31853ab8d58ec0b340d73.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04641e92b4b9dd6a1e31853ab8d58ec0b340d73.jpeg 2x" data-dominant-color="4D4F52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20201005-190140</span><span class="informations">712×716 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7161ca1928859c381272cd6af5b0ff0c90b73cb0.png" data-download-href="/uploads/short-url/gb1sXt2F3y0FpnNnD8Y3aQvtL1K.png?dl=1" title="v" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7161ca1928859c381272cd6af5b0ff0c90b73cb0_2_690x76.png" alt="v" data-base62-sha1="gb1sXt2F3y0FpnNnD8Y3aQvtL1K" width="690" height="76" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7161ca1928859c381272cd6af5b0ff0c90b73cb0_2_690x76.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7161ca1928859c381272cd6af5b0ff0c90b73cb0_2_1035x114.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7161ca1928859c381272cd6af5b0ff0c90b73cb0.png 2x" data-dominant-color="5D6269"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">v</span><span class="informations">1302×145 38.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is MHA file (is not compressed, so bigger as original compressed DICOM image) and i set origin and orientation to default (you might examine private tags)</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1jC1MMs84zxa25yffzailmEcw0zG9l3Wd/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1jC1MMs84zxa25yffzailmEcw0zG9l3Wd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1jC1MMs84zxa25yffzailmEcw0zG9l3Wd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1jC1MMs84zxa25yffzailmEcw0zG9l3Wd/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">20201005-185100.mha</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2020-10-05 17:26 UTC)

<p>The file loads correctly for me with Slicer Stable Release, if SlicerHeart extension is installed:</p>
<ul>
<li>Go to DICOM module</li>
<li>Drag-and-drop the file to the application window (this imports the file immediately into the DICOM database)</li>
<li>Double-click on the patient (or study or series) to load the image</li>
</ul>

---

## Post #5 by @issakomi (2020-10-05 17:30 UTC)

<p>i have drag-and-dropped, spacing was wrong</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89da425a9677dd9f456a8995ddd68854f95c28bd.jpeg" data-download-href="/uploads/short-url/jFv1XxQJtcuZdvfU2jRx7UtHMSN.jpeg?dl=1" title="Screenshot at 2020-10-05 19-29-57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89da425a9677dd9f456a8995ddd68854f95c28bd_2_690x368.jpeg" alt="Screenshot at 2020-10-05 19-29-57" data-base62-sha1="jFv1XxQJtcuZdvfU2jRx7UtHMSN" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89da425a9677dd9f456a8995ddd68854f95c28bd_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89da425a9677dd9f456a8995ddd68854f95c28bd_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89da425a9677dd9f456a8995ddd68854f95c28bd_2_1380x736.jpeg 2x" data-dominant-color="A6A7C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-10-05 19-29-57</span><span class="informations">1920×1026 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>may be not found that extension, thanks</p>

---

## Post #6 by @lassoan (2020-10-05 17:36 UTC)

<p>Thanks a lot for checking this <a class="mention" href="/u/issakomi">@issakomi</a>. Yes, the default Scalar volume reader plugin cannot get the spacing correctly. You need to install SlicerHeart extension, as it has a plugin that can properly load Philips Epiq/Affinity 3D ultrasound images:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/811a0c614e97db25fbdd01c398a48763457d2f44.png" data-download-href="/uploads/short-url/iq5oVrIBKd16R0z5GJJqNTkx5DC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811a0c614e97db25fbdd01c398a48763457d2f44_2_632x499.png" alt="image" data-base62-sha1="iq5oVrIBKd16R0z5GJJqNTkx5DC" width="632" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811a0c614e97db25fbdd01c398a48763457d2f44_2_632x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811a0c614e97db25fbdd01c398a48763457d2f44_2_948x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/811a0c614e97db25fbdd01c398a48763457d2f44_2_1264x998.png 2x" data-dominant-color="414D57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1519×1201 60.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b09caf678751c81b90f8f5012b3827e2fafb019b.jpeg" data-download-href="/uploads/short-url/pcnJkRLKzWqUIIASCNdFEkGAMT9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b09caf678751c81b90f8f5012b3827e2fafb019b_2_690x440.jpeg" alt="image" data-base62-sha1="pcnJkRLKzWqUIIASCNdFEkGAMT9" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b09caf678751c81b90f8f5012b3827e2fafb019b_2_690x440.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b09caf678751c81b90f8f5012b3827e2fafb019b_2_1035x660.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b09caf678751c81b90f8f5012b3827e2fafb019b_2_1380x880.jpeg 2x" data-dominant-color="373739"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1440 623 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @issakomi (2020-10-05 17:38 UTC)

<p>Yes, works, the same spacing. Thanks.</p>

---

## Post #8 by @Rodrigo_Visconti (2020-10-05 23:54 UTC)

<p>It works for me too but seems distorted when compared to original image<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/aca62391ee41540891029645b3386c14f869123d.jpeg" data-download-href="/uploads/short-url/oDk4I0TqcKCUs84tzWQFAR2tCLH.jpeg?dl=1" title="20200804_094401" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca62391ee41540891029645b3386c14f869123d_2_690x335.jpeg" alt="20200804_094401" data-base62-sha1="oDk4I0TqcKCUs84tzWQFAR2tCLH" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca62391ee41540891029645b3386c14f869123d_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca62391ee41540891029645b3386c14f869123d_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca62391ee41540891029645b3386c14f869123d_2_1380x670.jpeg 2x" data-dominant-color="432E23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200804_094401</span><span class="informations">4032×1960 1.29 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Rodrigo_Visconti (2020-10-05 23:55 UTC)

<p>Look the difference between the printed and original picture <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d4276c3487e46ccfbf888857c9f91cee6422294.jpeg" data-download-href="/uploads/short-url/8JVwubVnMI6nkccjfINmExHv5kg.jpeg?dl=1" title="20201005_093413" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d4276c3487e46ccfbf888857c9f91cee6422294_2_500x500.jpeg" alt="20201005_093413" data-base62-sha1="8JVwubVnMI6nkccjfINmExHv5kg" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d4276c3487e46ccfbf888857c9f91cee6422294_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d4276c3487e46ccfbf888857c9f91cee6422294_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d4276c3487e46ccfbf888857c9f91cee6422294_2_1000x1000.jpeg 2x" data-dominant-color="9B7A6D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20201005_093413</span><span class="informations">2896×2896 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2020-10-06 00:24 UTC)

<p><a class="mention" href="/u/rodrigo_visconti">@Rodrigo_Visconti</a> What spacing values do you see in Volumes module’s Volume information section? You can load the image incorrectly if SlicerHeart is not installed or you don’t use DICOM module to import and load the image.</p>
<p>You can take an image with objects of known sizes and measure them in Slicer to verify that there is no distortion.</p>

---

## Post #11 by @Rodrigo_Visconti (2020-10-06 04:40 UTC)

<p>Thanks for the tips. I think it worked well this way</p>

---

## Post #12 by @lassoan (2022-02-19 18:57 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-load-siemens-3d-ultrasound-data/22070">How to load Siemens 3D ultrasound data</a></p>

---
