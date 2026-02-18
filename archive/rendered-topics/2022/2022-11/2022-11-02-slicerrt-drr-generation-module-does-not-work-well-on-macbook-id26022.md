# SlicerRT DRR generation module does not work well on macbook

**Topic ID**: 26022
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/slicerrt-drr-generation-module-does-not-work-well-on-macbook/26022

---

## Post #1 by @suzume (2022-11-02 07:44 UTC)

<p>Operating system:mac os 13.0<br>
Slicer version:5.0.3<br>
Expected behavior: I want to use the “DRR generation” module in plastimatch. However, the generation results are always black. All of the setting parameters are default. And this module can be used normally in my Windows system.  How can I normally use it in the macOS system?<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba743b6c435f7f34161a86bcb9a27a89aa377043.jpeg" data-download-href="/uploads/short-url/qBrPOkqM60uSaMSRXs2Png7FOtd.jpeg?dl=1" title="截屏2022-11-02 15.22.31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba743b6c435f7f34161a86bcb9a27a89aa377043_2_690x428.jpeg" alt="截屏2022-11-02 15.22.31" data-base62-sha1="qBrPOkqM60uSaMSRXs2Png7FOtd" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba743b6c435f7f34161a86bcb9a27a89aa377043_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba743b6c435f7f34161a86bcb9a27a89aa377043_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba743b6c435f7f34161a86bcb9a27a89aa377043_2_1380x856.jpeg 2x" data-dominant-color="919299"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-11-02 15.22.31</span><span class="informations">1920×1191 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d029424aac15056481e2c5dd4c5b3713a31b0556.png" data-download-href="/uploads/short-url/tHtI47FvitDSgL8tj2E1Vq6aEh8.png?dl=1" title="截屏2022-11-02 15.23.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d029424aac15056481e2c5dd4c5b3713a31b0556_2_690x431.png" alt="截屏2022-11-02 15.23.10" data-base62-sha1="tHtI47FvitDSgL8tj2E1Vq6aEh8" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d029424aac15056481e2c5dd4c5b3713a31b0556_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d029424aac15056481e2c5dd4c5b3713a31b0556_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d029424aac15056481e2c5dd4c5b3713a31b0556_2_1380x862.png 2x" data-dominant-color="7C7D84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-11-02 15.23.10</span><span class="informations">2880×1800 462 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2022-11-02 12:08 UTC)

<p>Are you observing the same error on macOS as you mentioned on your previous thread:</p>
<aside class="quote quote-modified" data-post="1" data-topic="25448">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/suzume/48/16794_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/errors-when-using-drr-generator/25448">Errors when using DRR Generator</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Mac OS system 
Slicer version: Slice 5.0.3 
Expected behavior: When I using DRR Generator tool, there is always an error occurred! 
The error message is : " The message detail is: 
Exception thrown in event: /Volumes/D/S/S-0-build/ITK/Modules/IO/NRRD/src/itkNrrdImageIO.cxx:1118: 
ITK ERROR: NrrdImageIO(0x7f96d87621b0): Write: Error writing output_fixed.nrrd: 
[nrrd] nrrdSave: couldn’t fopen(“output_fixed.nrrd”,“wb”): Read-only file system" 
Is there anyone else met this error b…
  </blockquote>
</aside>


---

## Post #3 by @suzume (2022-11-02 13:48 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20">Would you mind please telling me which file I should change the permission?<br>
I have tried change the read and write permissions of the files circled in red in the picture below. However, the problem still exist.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fe119a31125edf7cf36b2f5d358ab813c5f6903.png" data-download-href="/uploads/short-url/dGbDl7LQnLLoiAyEgxCpYdUadMv.png?dl=1" title="截屏2022-11-02 21.42.46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fe119a31125edf7cf36b2f5d358ab813c5f6903_2_690x430.png" alt="截屏2022-11-02 21.42.46" data-base62-sha1="dGbDl7LQnLLoiAyEgxCpYdUadMv" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fe119a31125edf7cf36b2f5d358ab813c5f6903_2_690x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fe119a31125edf7cf36b2f5d358ab813c5f6903_2_1035x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fe119a31125edf7cf36b2f5d358ab813c5f6903_2_1380x860.png 2x" data-dominant-color="EEEFF2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-11-02 21.42.46</span><span class="informations">2880×1796 491 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @fieldr4 (2022-11-03 18:26 UTC)

<p>Can you show the settings that you have selected in “Process Parameters” dropdown? I encountered a similar problem when I had “pgm” or “pfm” selected instead of “raw.” Should already be “raw” if you set all parameters to their default values, but I thought it’d be worth mentioning.</p>

---

## Post #5 by @suzume (2022-11-04 02:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/446a79367584a1a8ab6ae3702ae6715a01ee62a8.png" data-download-href="/uploads/short-url/9LeAm3VCsJEsAQ7Nz0cTIUvUiMg.png?dl=1" title="截屏2022-11-04 09.52.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/446a79367584a1a8ab6ae3702ae6715a01ee62a8_2_690x344.png" alt="截屏2022-11-04 09.52.29" data-base62-sha1="9LeAm3VCsJEsAQ7Nz0cTIUvUiMg" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/446a79367584a1a8ab6ae3702ae6715a01ee62a8_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/446a79367584a1a8ab6ae3702ae6715a01ee62a8_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/446a79367584a1a8ab6ae3702ae6715a01ee62a8_2_1380x688.png 2x" data-dominant-color="878A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-11-04 09.52.29</span><span class="informations">2030×1014 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks for your remind. I have checked the “Process Parameters” and it’s “raw” <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2022-11-06 04:20 UTC)

<p>Have you <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#mac">installed Slicer</a>? Is your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#temporary-directory">temporary directory</a> writable?</p>

---

## Post #7 by @suzume (2022-11-07 07:21 UTC)

<p>Yes, I have installed Slicer. I check the temporary directory and it’s writable.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81ecf72412ea724ffd185029c497d2be98fb98e1.png" data-download-href="/uploads/short-url/ixnhXCsxzUXzcC7ORJIzAkv2k6Z.png?dl=1" title="截屏2022-11-07 15.19.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ecf72412ea724ffd185029c497d2be98fb98e1_2_690x443.png" alt="截屏2022-11-07 15.19.06" data-base62-sha1="ixnhXCsxzUXzcC7ORJIzAkv2k6Z" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ecf72412ea724ffd185029c497d2be98fb98e1_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81ecf72412ea724ffd185029c497d2be98fb98e1_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81ecf72412ea724ffd185029c497d2be98fb98e1.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-11-07 15.19.06</span><span class="informations">1168×750 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39323bae8bae9116004f91cd9ef138974a13b83f.jpeg" data-download-href="/uploads/short-url/89YQ4cZwkydqBfuETmWguThsMQn.jpeg?dl=1" title="截屏2022-11-07 15.18.51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39323bae8bae9116004f91cd9ef138974a13b83f_2_252x499.jpeg" alt="截屏2022-11-07 15.18.51" data-base62-sha1="89YQ4cZwkydqBfuETmWguThsMQn" width="252" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39323bae8bae9116004f91cd9ef138974a13b83f_2_252x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39323bae8bae9116004f91cd9ef138974a13b83f_2_378x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39323bae8bae9116004f91cd9ef138974a13b83f_2_504x998.jpeg 2x" data-dominant-color="EAEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2022-11-07 15.18.51</span><span class="informations">802×1588 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2022-11-07 17:39 UTC)

<p>Could somebody check if this behavior is reproducible on any macOS device? Just install SlicerRT, go to “DRR generation” module, select an input and output volume, and click Apply.</p>

---

## Post #9 by @pieper (2022-11-07 20:55 UTC)

<p>Looks fine to me.  Tested on a mac pro.</p>
<p><a class="mention" href="/u/suzume">@suzume</a> check your Temporary directory to confirm it is read/write for you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c8d4f52cf78e53a3ab5f060a8d72490d3308d8.png" data-download-href="/uploads/short-url/qmG8mmPNxYTIPAaRJcIpEKHio2s.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8c8d4f52cf78e53a3ab5f060a8d72490d3308d8_2_690x144.png" alt="image" data-base62-sha1="qmG8mmPNxYTIPAaRJcIpEKHio2s" width="690" height="144" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8c8d4f52cf78e53a3ab5f060a8d72490d3308d8_2_690x144.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c8d4f52cf78e53a3ab5f060a8d72490d3308d8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c8d4f52cf78e53a3ab5f060a8d72490d3308d8.png 2x" data-dominant-color="DEDEE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">828×173 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64987bd26215619c6136e13e13aca730b8447c31.jpeg" data-download-href="/uploads/short-url/elUrom9LIq0J5wCCzFFoZ5M0x0d.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64987bd26215619c6136e13e13aca730b8447c31_2_690x447.jpeg" alt="image" data-base62-sha1="elUrom9LIq0J5wCCzFFoZ5M0x0d" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64987bd26215619c6136e13e13aca730b8447c31_2_690x447.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64987bd26215619c6136e13e13aca730b8447c31.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64987bd26215619c6136e13e13aca730b8447c31.jpeg 2x" data-dominant-color="898D8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">799×518 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here’s the log:</p>
<pre><code class="lang-auto">Found CommandLine Module, target is  /Applications/Slicer-5.0.3.app/Contents/Extensions-30893/SlicerRT/lib/Slicer-5.0/cli-modules/plastimatch_slicer_drr
ModuleType: CommandLineModule
DRR generation command line: 

/Applications/Slicer-5.0.3.app/Contents/Extensions-30893/SlicerRT/lib/Slicer-5.0/cli-modules/plastimatch_slicer_drr --sad 1000 --sid 1300 --vup -1,1.22465e-16,1.22465e-16 --normal -1.22465e-16,-1,2.22045e-16 --isocenter -1.7,21.1,12.2 --dim 2000,2000 --spacing 0.25,0.25 --subwindow 0,0,1999,1999 --autoscale --autoscaleRange 0,255 --exponential --thresholdBelow -1000 --threading cpu --huconversion preprocess --algorithm uniform --outputFormat raw --negative /private/var/folders/cn/kmqx4dm17gx4hrllqrmnkbp00000gn/T/Slicer-pieper/HJCJI_vtkMRMLScalarVolumeNodeB.nrrd /private/var/folders/cn/kmqx4dm17gx4hrllqrmnkbp00000gn/T/Slicer-pieper/HJCJI_vtkMRMLScalarVolumeNodeD.nrrd 

DRR generation standard output:

Src range = 0.590037 1.000000
Dst range = 0.000000 255.000000
Slope = 622.008057, Offset = -0.590037
I/O time: 0.040724 sec
Total time: 65.379 secs

DRR generation completed without errors

Loaded volume from file: /private/var/folders/cn/kmqx4dm17gx4hrllqrmnkbp00000gn/T/Slicer-pieper/HJCJI_vtkMRMLScalarVolumeNodeD.nrrd. Dimensions: 2000x2000x1. Number of components: 1. Pixel type: float.



</code></pre>

---

## Post #10 by @Fa20 (2024-09-12 17:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd412319d30a55eae8114bcc2c84e5cd5389fa18.png" data-download-href="/uploads/short-url/vzj4KpurFl5vVYm2LKBwyWrcgWY.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd412319d30a55eae8114bcc2c84e5cd5389fa18_2_690x331.png" alt="grafik" data-base62-sha1="vzj4KpurFl5vVYm2LKBwyWrcgWY" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd412319d30a55eae8114bcc2c84e5cd5389fa18_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd412319d30a55eae8114bcc2c84e5cd5389fa18_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd412319d30a55eae8114bcc2c84e5cd5389fa18_2_1380x662.png 2x" data-dominant-color="737378"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1680×806 51.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have the same Problem on windows10</p>

---

## Post #11 by @cpinter (2024-09-13 08:17 UTC)

<p>We fixed this module fairly recently. Please use the latest Slicer/SlicerRT if you don’t already. If it does not work in the latest version, then please create a ticket for it with a full log, complete list of steps, etc. Thanks!</p>

---
