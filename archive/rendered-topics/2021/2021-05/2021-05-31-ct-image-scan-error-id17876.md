# CT Image Scan Error

**Topic ID**: 17876
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/ct-image-scan-error/17876

---

## Post #1 by @caesarsalad (2021-05-31 01:02 UTC)

<p>Hello,<br>
I’m trying to load a series of dcm files for a CT scan, but I’m getting an error as follows:</p>
<p>511: 1 [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution.</p>
<p>512: 2 [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution.</p>
<p>513: 3 [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution.</p>
<p>514: 4 [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution.</p>
<p>555: VR [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</p>
<p>Reference image in series does not contain geometry information. Please use caution.</p>
<p>999: Dose Report [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.</p>
<p>Would there be any suggestions for this error?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-05-31 01:25 UTC)

<p>Series number above 100 typically indicates secondary capture or reprocessed images, which are rarely useful for data analysis. You can safely ignore these and just use the original/primary images (with series number below 100).</p>

---

## Post #3 by @caesarsalad (2021-05-31 02:05 UTC)

<p>Hello sir,</p>
<p>I cannot seem to fix the error, would you mind taking a look at the CT data below? For some reason I seem to be getting only one .dcm image on display. I very much appreciate your time sir.</p>
<aside class="onebox googledrive">
  <header class="source">

      <a href="https://drive.google.com/file/d/1l580zFyep4G1KJY6Gc3eP2GCsZAN9y81/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1l580zFyep4G1KJY6Gc3eP2GCsZAN9y81/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1l580zFyep4G1KJY6Gc3eP2GCsZAN9y81/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">CT.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2021-05-31 02:53 UTC)

<p>I was able to load the 6xx series numbers correctly using the latest Slicer Preview Release:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49d1c1b991eb3bf66e21ff0dea4e55ba5a349c8e.jpeg" data-download-href="/uploads/short-url/ax2fWdAtPcRxNfYQrMe4X0Z34kK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49d1c1b991eb3bf66e21ff0dea4e55ba5a349c8e_2_690x418.jpeg" alt="image" data-base62-sha1="ax2fWdAtPcRxNfYQrMe4X0Z34kK" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49d1c1b991eb3bf66e21ff0dea4e55ba5a349c8e_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49d1c1b991eb3bf66e21ff0dea4e55ba5a349c8e_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/49d1c1b991eb3bf66e21ff0dea4e55ba5a349c8e_2_1380x836.jpeg 2x" data-dominant-color="ADABAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1369 571 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These are all reprocessed images, but since you don’t have any original/primary images in your zip file, these are the only ones you can use.</p>

---
