# CT scan Dicom 3D rendering not displayed

**Topic ID**: 40321
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/ct-scan-dicom-3d-rendering-not-displayed/40321

---

## Post #1 by @Dimitri_Gouvoussis (2024-11-21 22:19 UTC)

<p>Hello, I have a confocal, spatial, and axial view but I cannot get a 3D view to render. What step am I missing?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5c8f7a33c451853bf94108d8593db725154e04f.jpeg" data-download-href="/uploads/short-url/z4jy9ejsNMo6DQYo2XQpVcomsbB.jpeg?dl=1" title="IMG_0577" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8f7a33c451853bf94108d8593db725154e04f_2_666x500.jpeg" alt="IMG_0577" data-base62-sha1="z4jy9ejsNMo6DQYo2XQpVcomsbB" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8f7a33c451853bf94108d8593db725154e04f_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8f7a33c451853bf94108d8593db725154e04f_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8f7a33c451853bf94108d8593db725154e04f_2_1332x1000.jpeg 2x" data-dominant-color="6D6A79"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0577</span><span class="informations">4032×3024 2.11 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-11-21 22:24 UTC)

<p>You need to enable volume rendering to see it in the 3D view.  Drag the volume from the data module onto the 3D view.</p>

---

## Post #3 by @Dimitri_Gouvoussis (2024-11-22 17:29 UTC)

<p>Hello, thank you for responding. I tried to drag the loaded data in the 3D view but nothing occured. Is there another step for enabling 3D view? This is my view from the data window:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26c541f923d38bb81997fb8f48d14b980a36dd88.jpeg" data-download-href="/uploads/short-url/5wYLwGmZBz64erOJwsE8CHAmgn6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26c541f923d38bb81997fb8f48d14b980a36dd88_2_690x373.jpeg" alt="image" data-base62-sha1="5wYLwGmZBz64erOJwsE8CHAmgn6" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26c541f923d38bb81997fb8f48d14b980a36dd88_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26c541f923d38bb81997fb8f48d14b980a36dd88_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26c541f923d38bb81997fb8f48d14b980a36dd88_2_1380x746.jpeg 2x" data-dominant-color="37363A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2251×1219 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-11-22 17:32 UTC)

<p>I don’t think you have clinical dataset so maybe it is not using a good preset. Go to the Volume Rendering module and try different presets and see if you can get something to show up in the 3D viewer.</p>
<p>if not, then perhaps your data is too big for your GPU. Go to the Volumes module and tell us what the dimensions and the data type of your images.</p>

---

## Post #5 by @Dimitri_Gouvoussis (2024-11-22 17:52 UTC)

<p>Thank you for your response, I followed your recommendations and the 1st image is what dispalyed. I tried with multiple presets and the visual remained the same. I also tried changing the rendering with CPU and GPU ray casting but did not see any effect. I have attached my dimensions as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a77f5926037c886a292b9082ab9ed32c6a1555c6.png" data-download-href="/uploads/short-url/nTKzX96gIO6a0co072vq3r30E6y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77f5926037c886a292b9082ab9ed32c6a1555c6_2_690x355.png" alt="image" data-base62-sha1="nTKzX96gIO6a0co072vq3r30E6y" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77f5926037c886a292b9082ab9ed32c6a1555c6_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77f5926037c886a292b9082ab9ed32c6a1555c6_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a77f5926037c886a292b9082ab9ed32c6a1555c6_2_1380x710.png 2x" data-dominant-color="3B393B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2235×1153 454 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05444aef3447d21125ac463b1723150c511f42f6.png" data-download-href="/uploads/short-url/KAHDsyGjQZNjQspd6dMw3rYLQO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05444aef3447d21125ac463b1723150c511f42f6.png" alt="image" data-base62-sha1="KAHDsyGjQZNjQspd6dMw3rYLQO" width="471" height="500" data-dominant-color="353535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1039×1101 30.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2024-11-22 18:28 UTC)

<p>I am not seeing anything unusual about the size of the data, almost all recent GPUs should be able to handle this.</p>
<p>It is harder to see, but I think your dataset is under a non-linear transform. 3D viewer does not display this in real-time. You can right click on the transform grid next to the serioes description and choose harden.</p>
<p>Then try again.</p>

---
