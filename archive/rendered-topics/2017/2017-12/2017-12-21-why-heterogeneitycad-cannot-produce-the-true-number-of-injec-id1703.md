# Why HeterogeneityCAD cannot produce the true number of % injected dose value and gray levels in a normalized PET image?

**Topic ID**: 1703
**Date**: 2017-12-21
**URL**: https://discourse.slicer.org/t/why-heterogeneitycad-cannot-produce-the-true-number-of-injected-dose-value-and-gray-levels-in-a-normalized-pet-image/1703

---

## Post #1 by @MimiPoon (2017-12-21 20:39 UTC)

<p>Dear professors,</p>
<p>I have a set of PET images with intensity value normalized to % injected dose. The intensity range of the segmented tumor is around 0.450275 to 1.482173. I applied the heterogeneityCAD module to extract different features. The gray levels turned out to be 3, the minimum intensity is 0, the maximum intensity is 2, median intensity 0 and range 2. It appeared that it can only give results in whole digit rather than in decimal values. In the original PET images the number of gray levels is up to 100. How can I get back the values in decimal places?</p>
<p>Thanks!<br>
Mimi</p>

---

## Post #2 by @pieper (2017-12-21 23:05 UTC)

<p>Hi Mimi -</p>
<p>I’m not sure about HetrogeneityCAD, but you may also want to try SlicerRadiomics, as it is a newer project with updated methods.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @jayender (2017-12-22 00:26 UTC)

<p>Hi Mimi</p>
<p>The most probable reason is that you are providing the label map as your input in the field “Input Node:” instead of the PET volume node.</p>
<p>Jay</p>

---

## Post #4 by @MimiPoon (2017-12-22 01:00 UTC)

<p>Hi Jay,</p>
<p>No. I put the normalized PET volume in input node. If it is the label map, then there are only 2 kind of intensities, 0 &amp; 1.</p>
<p>Thanks!<br>
Mimi</p>

---

## Post #5 by @jayender (2017-12-22 01:39 UTC)

<p>Can you upload the deidentified dataset to Dropbox and send me the link. I can have a look at the issue.</p>
<p>Thanks<br>
Jay</p>

---

## Post #6 by @MimiPoon (2017-12-22 05:56 UTC)

<p>Hi Jay,</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/s3svrm8418h807m/ControlPETDay6Segmentation-labelLL.nrrd?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/s3svrm8418h807m/ControlPETDay6Segmentation-labelLL.nrrd?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/s3svrm8418h807m/ControlPETDay6Segmentation-labelLL.nrrd?dl=0" target="_blank" rel="noopener nofollow ugc">ControlPETDay6Segmentation-labelLL.nrrd</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/v3emsor63m465hz/Day6ControlPET%25IDLL.nrrd?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/v3emsor63m465hz/Day6ControlPET%25IDLL.nrrd?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/v3emsor63m465hz/Day6ControlPET%25IDLL.nrrd?dl=0" target="_blank" rel="noopener nofollow ugc">Day6ControlPET%IDLL.nrrd</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks!</p>
<p>Mimi</p>

---

## Post #7 by @fedorov (2017-12-22 17:21 UTC)

<p><a class="mention" href="/u/mimipoon">@MimiPoon</a> thank you for sharing the dataset!</p>
<p>I confirmed SlicerRadiomics (and the underlying <a href="http://pyradiomics.readthedocs.io/en/latest/">pyradiomics library</a>) has a similar issue, as apparently we do not handle properly bin width that is less than 1.</p>
<p>I reported the issue here so you can track the progress: <a href="https://github.com/Radiomics/pyradiomics/issues/327">https://github.com/Radiomics/pyradiomics/issues/327</a></p>

---

## Post #8 by @fedorov (2017-12-27 18:00 UTC)

<p><a class="mention" href="/u/mimipoon">@MimiPoon</a> I am sorry, I probably misled you by my earlier response.</p>
<p>First order features calculated by the Radiomics extension are represented by the floating point values. What I meant is that the values produced for the GLCM features are in integers only, and I am not sure if this is expected, or due to incorrect implementation of discretization.</p>
<p>After re-reading your post, I realized you were asking about first order features. Those appear to be correctly calculated with the Radiomics extension, see screenshot below for your sample dataset.</p>
<p>Please let us know if this resolves your question!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5557a03c84d77380e75957e183a5dbf214f82a8.png" data-download-href="/uploads/short-url/s9Hc3D37pJHK3iDVxv6mDMRGJG8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5557a03c84d77380e75957e183a5dbf214f82a8_2_589x500.png" alt="image" data-base62-sha1="s9Hc3D37pJHK3iDVxv6mDMRGJG8" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5557a03c84d77380e75957e183a5dbf214f82a8_2_589x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5557a03c84d77380e75957e183a5dbf214f82a8_2_883x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c5557a03c84d77380e75957e183a5dbf214f82a8_2_1178x1000.png 2x" data-dominant-color="BAB9B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×1027 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @fedorov (2017-12-27 18:32 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="1703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>the values produced for the GLCM features are in integers only</p>
</blockquote>
</aside>
<p>I traced down this problem, and updated the extension to fix it. If you use the Radiomics extension in the tomorrow’s nightly, or in the 4.8.1 tomorrow stable, you can get the updated version.</p>
<p>Currently the default bin size is set to 25, and the minimum bin size is limited to 0.01. Make sure you reduce the bin size in the settings, since otherwise you will not get meaningful values for your intensity range! If you think you need to use smaller bin size, let us know and we can update the extension to allow it.</p>
<p>Note that you can use <a href="http://pyradiomics.readthedocs.io/en/latest/">the pyradiomics library</a> directly to calculate the radiomics features from the command line, and configure feature extraction settings more flexibly.</p>
<p>Please let me know if there are any other issues related to the use of the Radiomics extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e18b99f9fc5a5d39359bf52d1f33286017ffd01.png" data-download-href="/uploads/short-url/b8Sdo9lPhR8izKwEiHYUbdMcLTP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e18b99f9fc5a5d39359bf52d1f33286017ffd01_2_690x470.png" alt="image" data-base62-sha1="b8Sdo9lPhR8izKwEiHYUbdMcLTP" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e18b99f9fc5a5d39359bf52d1f33286017ffd01_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e18b99f9fc5a5d39359bf52d1f33286017ffd01_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e18b99f9fc5a5d39359bf52d1f33286017ffd01_2_1380x940.png 2x" data-dominant-color="BDBDBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1575×1075 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @MimiPoon (2017-12-28 04:27 UTC)

<p>Dear Fedorov,</p>
<p>Thanks for your advice! Will try it tomorrow.</p>
<p>Mimi</p>

---
