# Support for pathology DICOM

**Topic ID**: 42248
**Date**: 2025-03-21
**URL**: https://discourse.slicer.org/t/support-for-pathology-dicom/42248

---

## Post #1 by @dzenanz (2025-03-21 16:22 UTC)

<p>I tried loading some DICOM microscopy images from <a href="https://zenodo.org/records/12689994" rel="noopener nofollow ugc">IDC</a>, but Slicer does not open them properly. <a href="https://github.com/DigitalSlideArchive/digital_slide_archive/" rel="noopener nofollow ugc">HistomicsTK</a> does open some of them (bigger files). Is this the format <a href="https://discourse.slicer.org/t/fail-to-load-a-big-tiff-stack/4832/8">mentioned</a> long ago by <a class="mention" href="/u/pieper">@pieper</a>? Am I missing some Slicer extension? Does <a class="mention" href="/u/fedorov">@fedorov</a> have some advice?</p>

---

## Post #2 by @fedorov (2025-03-21 17:04 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="1" data-topic="42248">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>but Slicer does not open them properly</p>
</blockquote>
</aside>
<p>I am not surprised by this. I’ve seen some demos in the past, but I am not sure how robust or maintained those are, if still available in some extensions.</p>
<aside class="quote no-group" data-username="dzenanz" data-post="1" data-topic="42248">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p><a href="https://github.com/DigitalSlideArchive/digital_slide_archive/">HistomicsTK</a> does open some of them (bigger files).</p>
</blockquote>
</aside>
<p>Can you give more details? Can you share pointers to the samples from IDC that open and do not open in HistomicsTK? Any errors? Ideally, it would be great to continue IDC-related discussions in the <a href="https://discourse.canceridc.dev/">IDC forum</a>.</p>
<aside class="quote no-group" data-username="dzenanz" data-post="1" data-topic="42248">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>Is this the format <a href="https://discourse.slicer.org/t/fail-to-load-a-big-tiff-stack/4832/8">mentioned</a> long ago by <a class="mention" href="/u/pieper">@pieper</a>?</p>
</blockquote>
</aside>
<p>IDC digital pathology images are stored as DICOM Whole Slide Imaging (WSI) objects. All of those images in IDC right now are <a href="https://learn.canceridc.dev/dicom/dicom-tiff-dual-personality-files">dual personality DICOM-TIFF</a>, which means that each file can be loaded by either DICOM or TIFF reader. A caveat is that DICOM represents each layer of the pyramid as a separate instance/file, so it is not a 1-to-1 mapping to the original TIFF that contains the entire pyramid in a single file. Overall, I encourage ignoring the TIFF part and work with those files as just DICOM WSI.</p>
<p>At this point, DICOM WSI is supported natively by several open source tools, including <a href="https://openslide.org/formats/dicom/">OpenSlide</a>, BioFormats <a href="https://bio-formats.readthedocs.io/en/stable/users/comlinetools/conversion.html">bfconvert</a> and <a href="https://github.com/imi-bigpicture/wsidicom">wsidicom</a>. I would be very surprised if none of those libraries is already in use by HistomicsTK, so perhaps it would not be a big effort to fix this.</p>

---

## Post #3 by @pieper (2025-03-21 17:16 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> what operations did you have in mind?</p>
<p>You may want to look at SlicerBigImage:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/gaoyi/SlicerBigImage">
  <header class="source">

      <a href="https://github.com/gaoyi/SlicerBigImage" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/85f2e8ce67acd23e7a0b7e275d33762a/gaoyi/SlicerBigImage" class="thumbnail">

  <h3><a href="https://github.com/gaoyi/SlicerBigImage" target="_blank" rel="noopener">GitHub - gaoyi/SlicerBigImage: Large (GB and above) scale microscopic image...</a></h3>

    <p><span class="github-repo-description">Large (GB and above) scale microscopic image computing using 3D Slicer</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @dzenanz (2025-03-21 18:33 UTC)

<p>I have BigImage extension you pointed out Steve, but it did not help.</p>

---

## Post #5 by @dzenanz (2025-03-21 18:42 UTC)

<p>Thanks for a detailed response Andrey. I was unaware they are dual DICOM/TIFF images. But renaming <code>M:\Dev\PSI\IDC\ccdi_mci\PBBHMD\2.25.89245761488191018377338178437808212829\SM_1.3.6.1.4.1.5962.99.1.852650165.48323970.1727429535925.4.0\21a0550d-a2ad-4345-9838-7be3d226a093.dcm</code> (part of <a href="https://zenodo.org/records/14009669" rel="noopener nofollow ugc">CCDI-MCI</a>) into .tif and drag/dropping into Slicer results in the same problematic wrong size/layout as when loading as DICOM:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6b068314e40a7d11d76a831cfddaf84cfc6b54a.jpeg" data-download-href="/uploads/short-url/slGulhIciy2dViaIxbexNLo5nUC.jpeg?dl=1" title="Screenshot 2025-03-21 14.38.30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6b068314e40a7d11d76a831cfddaf84cfc6b54a_2_690x418.jpeg" alt="Screenshot 2025-03-21 14.38.30" data-base62-sha1="slGulhIciy2dViaIxbexNLo5nUC" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6b068314e40a7d11d76a831cfddaf84cfc6b54a_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6b068314e40a7d11d76a831cfddaf84cfc6b54a_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6b068314e40a7d11d76a831cfddaf84cfc6b54a_2_1380x836.jpeg 2x" data-dominant-color="939198"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-03-21 14.38.30</span><span class="informations">1920×1165 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will follow-up with HistomicsTK-related post in IDC forum.</p>

---

## Post #6 by @fedorov (2025-03-21 18:56 UTC)

<p>If you just want to load images, it should work with the free open source QuPath <a href="https://qupath.github.io/">https://qupath.github.io/</a>, which wraps both of the aforementioned OpenSlide and Bioformats libraries, and can read DICOM WSI natively.</p>

---

## Post #7 by @curtislisle (2025-03-21 18:59 UTC)

<p>These microscopy and whole slide images from IDC are DICOM-WSI, not the radiology type of DICOM that ITK is expecting. These images need a library like openslide or wsi-dicom OR kitware’s large-image to read them and write out a selected resolution as a traditional TIFF for reading by ITK. They are basically multi-resolution TIFFs.</p>

---

## Post #8 by @pieper (2025-03-21 19:34 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> you still haven’t described what exactly you are trying to accomplish.</p>

---

## Post #9 by @dzenanz (2025-03-21 19:48 UTC)

<p>I am trying to view IDC microscopy images quickly and conveniently, preferably without installing much additional software.</p>

---

## Post #10 by @dzenanz (2025-03-21 20:40 UTC)

<p>I realized that the DICOM images HistomicsTK cannot open are the regular (radiology) ones, which Slicer can open.</p>
<p>The ultimate goal I was pursuing was finding paired stained/unstained microscopy images (ideally with segmented cancer cells, or with a stain which highlights the cancer cells). The follow-up IDC forum question is <a href="https://discourse.canceridc.dev/t/unstained-and-paired-microscopy-images/705" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #11 by @dzenanz (2025-03-25 16:00 UTC)

<p>I see a path forward. ITK remote module <a href="https://github.com/InsightSoftwareConsortium/ITKIOOpenSlide" rel="noopener nofollow ugc">IOOpenSlide</a> allows use of OpenSlide, <a href="https://github.com/openslide/openslide/releases/tag/v4.0.0" rel="noopener nofollow ugc">latest (4.0) release</a> of which supports DICOM-WSI standard. Their binary Windows distribution has a DLL, so work will be needed to integrate this. But there is hope. Most tests pass:</p>
<pre data-code-wrap="log"><code class="lang-log">1&gt;67% tests passed, 3 tests failed out of 9
1&gt;
1&gt;Label Time Summary:
1&gt;IOOpenSlide    =  32.35 sec*proc (9 tests)
1&gt;
1&gt;Total Test time (real) =  32.36 sec
1&gt;
1&gt;The following tests FAILED:
1&gt;	  3 - itkOpenSlideTestMetaData (Failed)                 IOOpenSlide
1&gt;	  8 - itkOpenSlideTestApproximateStreaming (Failed)     IOOpenSlide
1&gt;	  9 - itkOpenSlideTestStreaming (Failed)                IOOpenSlide
</code></pre>

---

## Post #12 by @dzenanz (2025-03-26 18:44 UTC)

<p>Good news: the test failures are due to using a different version of OpenSlide library.</p>

---
