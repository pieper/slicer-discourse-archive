---
topic_id: 42074
title: "Issue With Visualizing 3D Movie After Converting Raw Dicom T"
date: 2025-03-11
url: https://discourse.slicer.org/t/42074
---

# Issue with Visualizing 3D Movie After Converting Raw DICOM to Cartesian DICOM in 3D Slice

**Topic ID**: 42074
**Date**: 2025-03-11
**URL**: https://discourse.slicer.org/t/issue-with-visualizing-3d-movie-after-converting-raw-dicom-to-cartesian-dicom-in-3d-slice/42074

---

## Post #1 by @federica-pixel (2025-03-11 17:20 UTC)

<p>I came across information on converting 3D TEE data from raw DICOM to Cartesian DICOM using GE software. I am currently trying to achieve this and would greatly appreciate your insights.</p>
<p>First, I downloaded SlicerHeart in the 3D Slicer 5.9 software.<br>
I then requested access to the Image3dAPI from GE and installed it on my Windows machine. Specifically, I unzipped the downloaded file and copied the bin64 folder of GE_CVUS_Loader-3.39.3 into the bin folder of 3D Slicer 5.9.</p>
<p>Next, I successfully ran the following command with administrative privileges to register the loader DLL in the Windows registry:</p>
<pre><code>regsvr32 Image3dLoaderGe.dll
</code></pre>
<p>After that, in the <strong>Python console of 3D Slicer</strong>, I ran the following code:</p>
<pre><code class="lang-auto">import comtypes.client

try:
    loader = comtypes.client.CreateObject("GEHC_CARD_US.Image3dFileLoader")
    print("Loader object created successfully!")
except Exception as e:
    print(f"Failed to create loader object: {e}")
</code></pre>
<p>The <strong>loader object was created successfully</strong>.</p>
<p>Then, the 3D movie is the only one that not appear:</p>
<p>Despite everything working so far, the <strong>3D movie does not appear</strong> in 3D Slicer.<br>
However, if I upload the same file in other software like EchoPac or MicroDicom, it works properly.</p>
<p>Has anyone encountered this issue before? Is there an additional step required to visualize the 3D movie in 3D Slicer?</p>
<p>Any help would be greatly appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef99444889a531f9aa716feb6b247c5f93fcc81.png" data-download-href="/uploads/short-url/rfrriu2gGM7wF9lyoNCN2ZcOeQx.png?dl=1" title="Immagine1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef99444889a531f9aa716feb6b247c5f93fcc81_2_690x143.png" alt="Immagine1" data-base62-sha1="rfrriu2gGM7wF9lyoNCN2ZcOeQx" width="690" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bef99444889a531f9aa716feb6b247c5f93fcc81_2_690x143.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef99444889a531f9aa716feb6b247c5f93fcc81.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef99444889a531f9aa716feb6b247c5f93fcc81.png 2x" data-dominant-color="EEEEF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Immagine1</span><span class="informations">964×200 72.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ebe47ef32b2695961c1bcc45adc16666da6a536.png" data-download-href="/uploads/short-url/8X3hfQC6Wy3eWTwz86MoUzEAxb8.png?dl=1" title="Immagine2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ebe47ef32b2695961c1bcc45adc16666da6a536_2_690x249.png" alt="Immagine2" data-base62-sha1="8X3hfQC6Wy3eWTwz86MoUzEAxb8" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ebe47ef32b2695961c1bcc45adc16666da6a536_2_690x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ebe47ef32b2695961c1bcc45adc16666da6a536.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ebe47ef32b2695961c1bcc45adc16666da6a536.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Immagine2</span><span class="informations">964×348 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf3557c4c840f37b732b5969ffc261852ffcf83.png" data-download-href="/uploads/short-url/tf4K9T2tuT1Q6AgaODSUrLp7XGP.png?dl=1" title="Immagine3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccf3557c4c840f37b732b5969ffc261852ffcf83_2_690x354.png" alt="Immagine3" data-base62-sha1="tf4K9T2tuT1Q6AgaODSUrLp7XGP" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccf3557c4c840f37b732b5969ffc261852ffcf83_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf3557c4c840f37b732b5969ffc261852ffcf83.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf3557c4c840f37b732b5969ffc261852ffcf83.png 2x" data-dominant-color="AAAAB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Immagine3</span><span class="informations">964×495 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @federica-pixel (2025-03-12 11:58 UTC)

<p>To provide more context, here is the link to the raw DICOM data (downloaded from EchoPac) I am trying to load:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/336vxnp3s8au8z4m43obb/AIQkWuIaIPriPhDdWZPPSRk?rlkey=93ba6rkd9bv8oe7ebyidr8sr9&amp;st=ccyt7zc7&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/336vxnp3s8au8z4m43obb/AIQkWuIaIPriPhDdWZPPSRk?rlkey=93ba6rkd9bv8oe7ebyidr8sr9&amp;st=ccyt7zc7&amp;dl=0" target="_blank" rel="noopener nofollow ugc">dropbox.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.dropbox.com/scl/fo/336vxnp3s8au8z4m43obb/AIQkWuIaIPriPhDdWZPPSRk?rlkey=93ba6rkd9bv8oe7ebyidr8sr9&amp;st=ccyt7zc7&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2025-03-14 02:39 UTC)

<p>Everything looks good. You have loaded the 3D volume successfully! The easiest way to show this in 3D is to go to Data module and <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">drag-and-drop the image volume into the 3D view</a>. You can get even nicer results if you use the <code>Echo volume render</code> module of SliceHeart.</p>
<p>Echo volume rendering settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32df70de60f0815e3e276d254f6427bad21d421a.jpeg" data-download-href="/uploads/short-url/7g2AN8ATrJ5G3OYovPgMEaV61sK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32df70de60f0815e3e276d254f6427bad21d421a_2_690x359.jpeg" alt="image" data-base62-sha1="7g2AN8ATrJ5G3OYovPgMEaV61sK" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32df70de60f0815e3e276d254f6427bad21d421a_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32df70de60f0815e3e276d254f6427bad21d421a_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32df70de60f0815e3e276d254f6427bad21d421a_2_1380x718.jpeg 2x" data-dominant-color="3C3936"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×999 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Echo Volume rendering video:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d092edfb65c9a6b62bc1d68185a94594ba9cf242.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/415a3ccc4d20e2cb9f39088c85ec0a3dbac8cf6e.jpeg" data-video-base62-sha1="tL86Lp9DGaJQO6mTyHrH4fP07dM.mp4">
  </div><p></p>
<p>Microdicom and other basic viewers just replay the <em>screenshots</em> of the rendering. That looks nice but has very limited use, because you cannot rotate the view, you cannot do any measurements, analysis, 3D segmentation, etc. The screenshots look like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5500c47b3ca21134d7ae19a449d7d054a9be42a9.jpeg" data-download-href="/uploads/short-url/c7YedF9e784TOfEBAMGTiXTE03v.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5500c47b3ca21134d7ae19a449d7d054a9be42a9_2_690x385.jpeg" alt="image" data-base62-sha1="c7YedF9e784TOfEBAMGTiXTE03v" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5500c47b3ca21134d7ae19a449d7d054a9be42a9_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5500c47b3ca21134d7ae19a449d7d054a9be42a9_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/5500c47b3ca21134d7ae19a449d7d054a9be42a9_2_1380x770.jpeg 2x" data-dominant-color="231F1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1074 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @federica-pixel (2025-03-20 12:20 UTC)

<p>Thanks so much! It is working properly now</p>

---
