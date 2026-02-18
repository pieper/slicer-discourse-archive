# Brain MRI Gray Matter Segmentation

**Topic ID**: 23718
**Date**: 2022-06-05
**URL**: https://discourse.slicer.org/t/brain-mri-gray-matter-segmentation/23718

---

## Post #1 by @klippert (2022-06-05 22:33 UTC)

<p>Dear Community,</p>
<p>I’m just a 3d printing nerd looking to print my brain from MRI/DCOM files.  I’ve been able to extract my brain using HD-BET and Swiss Skull Stripper. Now I’m trying to just isolate the gray matter/cerebral cortex/folds, etc.  However, when I use thresholding in segment editor on the extracted brain segment, I can’t seem to get the structure definition on the sides/rear (too smooth) of my brain as shown in the pics.</p>
<p>If anyone has a step by step tutorial I would greatly appreciated it.  I’m just trying to develop a recipe to 3d print brains for myself and family.</p>
<p>I found a brain logistic segmentation extension in the attached pic.  This appears to isolate gray/white matter in 3d slicer, but not sure how to install it?  I don’t see it in the list of extensions inside 3d slicer, but I guess there is a way to download the python files, but not that familiar with how to install manually and what sub directory to add it to?</p>
<p>Any help would be appreciated.</p>
<p>Thanks,<br>
Kurt</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1cf77167e9bc051cf85d6e63dc0c63d6273c7dd.jpeg" data-download-href="/uploads/short-url/wdBVdScWpjRBmVdbVs2sQCE6Kzr.jpeg?dl=1" title="IMG_4418" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1cf77167e9bc051cf85d6e63dc0c63d6273c7dd_2_666x500.jpeg" alt="IMG_4418" data-base62-sha1="wdBVdScWpjRBmVdbVs2sQCE6Kzr" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1cf77167e9bc051cf85d6e63dc0c63d6273c7dd_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1cf77167e9bc051cf85d6e63dc0c63d6273c7dd_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1cf77167e9bc051cf85d6e63dc0c63d6273c7dd_2_1332x1000.jpeg 2x" data-dominant-color="757F97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4418</span><span class="informations">1920×1440 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcc53aba9317723d73de5140a095a55063a08c2d.jpeg" data-download-href="/uploads/short-url/A46SQshfAmMUxjIfpWKUqmOsTq5.jpeg?dl=1" title="IMG_4420" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcc53aba9317723d73de5140a095a55063a08c2d_2_666x500.jpeg" alt="IMG_4420" data-base62-sha1="A46SQshfAmMUxjIfpWKUqmOsTq5" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcc53aba9317723d73de5140a095a55063a08c2d_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcc53aba9317723d73de5140a095a55063a08c2d_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcc53aba9317723d73de5140a095a55063a08c2d_2_1332x1000.jpeg 2x" data-dominant-color="5670BC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4420</span><span class="informations">1920×1440 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7921f052f9f4d1137ca8710be380cbab784f7888.jpeg" data-download-href="/uploads/short-url/hhAudxY7vxqhx6BiRQZI0eqIak8.jpeg?dl=1" title="IMG_4417" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7921f052f9f4d1137ca8710be380cbab784f7888_2_666x500.jpeg" alt="IMG_4417" data-base62-sha1="hhAudxY7vxqhx6BiRQZI0eqIak8" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7921f052f9f4d1137ca8710be380cbab784f7888_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7921f052f9f4d1137ca8710be380cbab784f7888_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7921f052f9f4d1137ca8710be380cbab784f7888_2_1332x1000.jpeg 2x" data-dominant-color="747C95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4417</span><span class="informations">1920×1440 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/982e610cb60f48fb4330f599444533a39534d8ab.jpeg" data-download-href="/uploads/short-url/lIfWq5QghrfISXbGABB4zoEOhfl.jpeg?dl=1" title="IMG_4419" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/982e610cb60f48fb4330f599444533a39534d8ab_2_666x500.jpeg" alt="IMG_4419" data-base62-sha1="lIfWq5QghrfISXbGABB4zoEOhfl" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/982e610cb60f48fb4330f599444533a39534d8ab_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/982e610cb60f48fb4330f599444533a39534d8ab_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/982e610cb60f48fb4330f599444533a39534d8ab_2_1332x1000.jpeg 2x" data-dominant-color="6179BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4419</span><span class="informations">1920×1440 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-06-05 22:48 UTC)

<p>You can maybe try <a href="https://surfer.nmr.mgh.harvard.edu/">FreeSurfer</a> directly, or if it’s not working you can use <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/SynthSR">SynthSeg</a> and run the results through FreeSurfer.  You can work with the results <a href="https://discourse.slicer.org/t/new-extension-slicerfreesurfer/12751">in Slicer</a>.</p>

---

## Post #3 by @klippert (2022-06-06 03:05 UTC)

<p>I think this 3d slicer extension could isolate the gray matter and cortical structures.  However, I don’t see this extension in the extension module list inside 3d slicer v5.0.2 (Mac).</p>
<p>Brain Tissues Extension:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BrainTissuesExtension" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BrainTissuesExtension</a></p>
<p>Thanks,<br>
Kurt</p>

---

## Post #4 by @mau_igna_06 (2022-06-06 08:19 UTC)

<p>why don’t you try this one?</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/master/HDBrainExtraction.s4ext">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/HDBrainExtraction.s4ext" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/master/HDBrainExtraction.s4ext" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/master/HDBrainExtraction.s4ext</a></h4>


      <pre><code class="lang-s4ext">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager
scm git
scmurl https://github.com/lassoan/SlicerHDBrainExtraction.git
scmrevision main

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends PyTorch

# Inner build directory (default is ".")
build_subdirectory .

# homepage
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/HDBrainExtraction.s4ext" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>tyou can download it from the extesnsions manager</p>
<p>Mauro</p>

---

## Post #5 by @klippert (2022-06-06 13:43 UTC)

<p>The link you provided appears to be the HDBrainExtraction (HD-BET) Extension, that’s what I used to generate the skull stripped brain volume (in blue) in my pictures.  This is a great extension and easy to use, but I think it still retains portions of the meninges layers.  I’ve used the extracted/segmented volume from HD-BET and applied thresholding in segment editor to get the results in the pics attached, but I can’t seems to isolate just the gray matter in the rear/sides of the extracted brain.  So I’ve found a couple gray matter segmentation extensions, but they are not available in the extensions manager list in 3d slicer.</p>
<p>Are there any instructions on how to install an extension like “Brain Tissues” extension with code on Github into 3d Slicer manually? I’m assuming I would have to download the files from Github for the specific extension and copy to a folder on my Mac that 3d slicer would install?  Can I use “Extension Wizard” to load an extension manually?  I’m a coding novice, so have no clue.</p>
<p>Thanks,<br>
Kurt</p>

---

## Post #6 by @slicer365 (2022-06-06 23:48 UTC)

<p>I have installed this module, but it does’t work.  The last version was updated before 5 years.</p>

---

## Post #7 by @klippert (2022-06-07 01:29 UTC)

<p>Agreed, I was able to get it to load, but when it ran on my volume it did not isolate the gray matter. Any guidance on doing this in segment editor with thresholding or other method would be appreciated.</p>

---

## Post #8 by @mau_igna_06 (2022-06-07 09:17 UTC)

<p>Please see if this one it’s useful</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/2a2ba15f045e5bfcb5e86c455dea6d9e1d03c265/ARCHIVE/ROBEXBrainExtraction.s4ext">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/2a2ba15f045e5bfcb5e86c455dea6d9e1d03c265/ARCHIVE/ROBEXBrainExtraction.s4ext" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/2a2ba15f045e5bfcb5e86c455dea6d9e1d03c265/ARCHIVE/ROBEXBrainExtraction.s4ext" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/2a2ba15f045e5bfcb5e86c455dea6d9e1d03c265/ARCHIVE/ROBEXBrainExtraction.s4ext</a></h4>


      <pre><code class="lang-s4ext">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/CSIM-Toolkits/ROBEXBrainExtraction.git
scmrevision ac25d08

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends NA

# Inner build directory (default is ".")
build_subdirectory .

# homepage
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/2a2ba15f045e5bfcb5e86c455dea6d9e1d03c265/ARCHIVE/ROBEXBrainExtraction.s4ext" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @klippert (2022-06-07 14:02 UTC)

<p>Mauro, sorry for being so high maintenance, will ROBEX work on a Mac?  I’ve tried loading it and get this error, I just copied the extension file into a folder robex3 and used the extension wizard to “select extension” and directed it to the robex3 folder.  Do I need to download other files?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d9761561d8f7d64e7f748301ea93bb42bed39c.jpeg" data-download-href="/uploads/short-url/c6C0ZZpXwIm7PGYSvLSCdyRAjxy.jpeg?dl=1" title="IMG_4435" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d9761561d8f7d64e7f748301ea93bb42bed39c_2_666x500.jpeg" alt="IMG_4435" data-base62-sha1="c6C0ZZpXwIm7PGYSvLSCdyRAjxy" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d9761561d8f7d64e7f748301ea93bb42bed39c_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d9761561d8f7d64e7f748301ea93bb42bed39c_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d9761561d8f7d64e7f748301ea93bb42bed39c_2_1332x1000.jpeg 2x" data-dominant-color="8E9099"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4435</span><span class="informations">1920×1440 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bd1a86725df6c71bc01a77ac3f75b7ecad37357.jpeg" data-download-href="/uploads/short-url/mercg5X48uvMkk9Oov0jnqEMKQ7.jpeg?dl=1" title="IMG_4433" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bd1a86725df6c71bc01a77ac3f75b7ecad37357_2_666x500.jpeg" alt="IMG_4433" data-base62-sha1="mercg5X48uvMkk9Oov0jnqEMKQ7" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bd1a86725df6c71bc01a77ac3f75b7ecad37357_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bd1a86725df6c71bc01a77ac3f75b7ecad37357_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9bd1a86725df6c71bc01a77ac3f75b7ecad37357_2_1332x1000.jpeg 2x" data-dominant-color="8B8D9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4433</span><span class="informations">1920×1440 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ec0d22bf08974d5c07657e50d1ee53e911562e8.jpeg" data-download-href="/uploads/short-url/fNLDBxXfNLfVrReO1sdfjipb8iQ.jpeg?dl=1" title="IMG_4432" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec0d22bf08974d5c07657e50d1ee53e911562e8_2_666x500.jpeg" alt="IMG_4432" data-base62-sha1="fNLDBxXfNLfVrReO1sdfjipb8iQ" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec0d22bf08974d5c07657e50d1ee53e911562e8_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec0d22bf08974d5c07657e50d1ee53e911562e8_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ec0d22bf08974d5c07657e50d1ee53e911562e8_2_1332x1000.jpeg 2x" data-dominant-color="808490"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4432</span><span class="informations">1920×1440 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4dcb86c91cc956f09e867f5cf520af1f4d8ab75.jpeg" data-download-href="/uploads/short-url/nwrcb85lv4X19qBFflaCqNsFyNT.jpeg?dl=1" title="IMG_4434" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4dcb86c91cc956f09e867f5cf520af1f4d8ab75_2_666x500.jpeg" alt="IMG_4434" data-base62-sha1="nwrcb85lv4X19qBFflaCqNsFyNT" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4dcb86c91cc956f09e867f5cf520af1f4d8ab75_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4dcb86c91cc956f09e867f5cf520af1f4d8ab75_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4dcb86c91cc956f09e867f5cf520af1f4d8ab75_2_1332x1000.jpeg 2x" data-dominant-color="90929A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4434</span><span class="informations">1920×1440 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @mau_igna_06 (2022-06-07 16:42 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> do you think you could check why this twño brain extensions are apparently not working?</p>
<p>Thank you</p>

---

## Post #11 by @pieper (2022-06-07 16:51 UTC)

<p>That extension is several years old and apparently is not maintained.  Contacting the original authors could help.</p>
<p>I still suggest the methods I suggested earlier.</p>

---

## Post #12 by @jarrett-rushmore (2022-06-08 21:23 UTC)

<p>Hi Kurt,<br>
I agree with Steve and would suggest FreeSurfer.  Segmentation may not do super well at isolating a number of sulci and may make the brain look lisencephalic in parts, but the FreeSurfer produces surfaces that typically do a nice job and help to create useful segmentations. You can then import the surfaces and related segmentations using the FreeSurfer Importer Extension for Slicer, which is really really nice.  Good luck!<br>
Jarrett</p>

---

## Post #13 by @Mehran (2022-06-09 12:06 UTC)

<p>Hi, you can try our latest module to extract brain and segment GM/WM/CSF way better than freesurfer. You will find link to download and how to install as follow</p>
<div class="youtube-onebox lazy-video-container" data-video-id="gH4dkXm3B2E" data-video-title="TsallisBrainSegmentation: Brain MRI segmentation into White Matter, Grey Matter and CSF" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=gH4dkXm3B2E" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/gH4dkXm3B2E/maxresdefault.jpg" title="TsallisBrainSegmentation: Brain MRI segmentation into White Matter, Grey Matter and CSF" width="" height="">
  </a>
</div>


---

## Post #14 by @klippert (2022-06-11 04:33 UTC)

<p>Mehran,</p>
<p>Thanks for the link, I loaded TSALLIS extension and having some issues extracting the entire brain and then segmenting it to just get the gray matter.  I had to set the extraction parameter close to 0 to cover all the brain and still has holes. Then I’m not sure what segmentation values to use to just get the gray matter.  I then modified the segment output in segment editor and used the threshold function to create a 3d version, but it still has some areas in the rear/sides that are smooth. I like your extension, but think either my MRI/DCOM files are not high enough resolution or I just have incorrect settings in your extension?</p>
<p>Thanks,<br>
Kurt</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bba967d361a036b4f3195e61475620d7c43db659.jpeg" data-download-href="/uploads/short-url/qM8eFZRSwpHYvy2kL94diS4Px7X.jpeg?dl=1" title="IMG_4469" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bba967d361a036b4f3195e61475620d7c43db659_2_666x500.jpeg" alt="IMG_4469" data-base62-sha1="qM8eFZRSwpHYvy2kL94diS4Px7X" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bba967d361a036b4f3195e61475620d7c43db659_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bba967d361a036b4f3195e61475620d7c43db659_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bba967d361a036b4f3195e61475620d7c43db659_2_1332x1000.jpeg 2x" data-dominant-color="707384"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4469</span><span class="informations">1920×1440 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52892bf58e8052fc6556b59d6ae9ac887669f44b.jpeg" data-download-href="/uploads/short-url/bM92zZJwQOEJTa2PIwG3B41Vn1F.jpeg?dl=1" title="IMG_4468" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52892bf58e8052fc6556b59d6ae9ac887669f44b_2_666x500.jpeg" alt="IMG_4468" data-base62-sha1="bM92zZJwQOEJTa2PIwG3B41Vn1F" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52892bf58e8052fc6556b59d6ae9ac887669f44b_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52892bf58e8052fc6556b59d6ae9ac887669f44b_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52892bf58e8052fc6556b59d6ae9ac887669f44b_2_1332x1000.jpeg 2x" data-dominant-color="6E7080"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4468</span><span class="informations">1920×1440 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36beeeff00183a16568fc41040817f56c193ebc7.jpeg" data-download-href="/uploads/short-url/7OiR7bScyjoCs1KkrS6A7GfuXKT.jpeg?dl=1" title="IMG_4465" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36beeeff00183a16568fc41040817f56c193ebc7_2_666x500.jpeg" alt="IMG_4465" data-base62-sha1="7OiR7bScyjoCs1KkrS6A7GfuXKT" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36beeeff00183a16568fc41040817f56c193ebc7_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36beeeff00183a16568fc41040817f56c193ebc7_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36beeeff00183a16568fc41040817f56c193ebc7_2_1332x1000.jpeg 2x" data-dominant-color="707381"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4465</span><span class="informations">1920×1440 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d2dc28c4036c3d8b98ab594375f88ae64de9b0.jpeg" data-download-href="/uploads/short-url/wN76AcKRwrZLIH9EGAJRj0PboWI.jpeg?dl=1" title="IMG_4466" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d2dc28c4036c3d8b98ab594375f88ae64de9b0_2_666x500.jpeg" alt="IMG_4466" data-base62-sha1="wN76AcKRwrZLIH9EGAJRj0PboWI" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d2dc28c4036c3d8b98ab594375f88ae64de9b0_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d2dc28c4036c3d8b98ab594375f88ae64de9b0_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5d2dc28c4036c3d8b98ab594375f88ae64de9b0_2_1332x1000.jpeg 2x" data-dominant-color="6F7382"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4466</span><span class="informations">1920×1440 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41abaeb736460c66b52bc3f4027ed5d8658a1a18.jpeg" data-download-href="/uploads/short-url/9mWRxGJjfPv7X5wiVJOwib6Ww7S.jpeg?dl=1" title="IMG_4464" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41abaeb736460c66b52bc3f4027ed5d8658a1a18_2_666x500.jpeg" alt="IMG_4464" data-base62-sha1="9mWRxGJjfPv7X5wiVJOwib6Ww7S" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41abaeb736460c66b52bc3f4027ed5d8658a1a18_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41abaeb736460c66b52bc3f4027ed5d8658a1a18_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41abaeb736460c66b52bc3f4027ed5d8658a1a18_2_1332x1000.jpeg 2x" data-dominant-color="6F7282"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4464</span><span class="informations">1920×1440 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6697baf2c2a3f810e15640683fcd803b48c226fd.jpeg" data-download-href="/uploads/short-url/eDzMwfrymUJJle2B6RJJlCRbI5v.jpeg?dl=1" title="IMG_4462" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6697baf2c2a3f810e15640683fcd803b48c226fd_2_666x500.jpeg" alt="IMG_4462" data-base62-sha1="eDzMwfrymUJJle2B6RJJlCRbI5v" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6697baf2c2a3f810e15640683fcd803b48c226fd_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6697baf2c2a3f810e15640683fcd803b48c226fd_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6697baf2c2a3f810e15640683fcd803b48c226fd_2_1332x1000.jpeg 2x" data-dominant-color="727685"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4462</span><span class="informations">1920×1440 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f246d4d2b9323bc6ed2b4917201a65b3255ca827.jpeg" data-download-href="/uploads/short-url/yzhiNRP29sk913VSrsTKHdvF5yf.jpeg?dl=1" title="IMG_4459" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f246d4d2b9323bc6ed2b4917201a65b3255ca827_2_666x500.jpeg" alt="IMG_4459" data-base62-sha1="yzhiNRP29sk913VSrsTKHdvF5yf" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f246d4d2b9323bc6ed2b4917201a65b3255ca827_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f246d4d2b9323bc6ed2b4917201a65b3255ca827_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f246d4d2b9323bc6ed2b4917201a65b3255ca827_2_1332x1000.jpeg 2x" data-dominant-color="6C6E80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4459</span><span class="informations">1920×1440 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/997f030c4e9340b7099048391d90fc8db8094648.jpeg" data-download-href="/uploads/short-url/lTTaPFScOY0Baei8HwBI3rcxlfW.jpeg?dl=1" title="IMG_4460" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997f030c4e9340b7099048391d90fc8db8094648_2_666x500.jpeg" alt="IMG_4460" data-base62-sha1="lTTaPFScOY0Baei8HwBI3rcxlfW" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997f030c4e9340b7099048391d90fc8db8094648_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997f030c4e9340b7099048391d90fc8db8094648_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/997f030c4e9340b7099048391d90fc8db8094648_2_1332x1000.jpeg 2x" data-dominant-color="737686"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4460</span><span class="informations">1920×1440 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24370dc325b35b50540783def039000d5b3db4fb.jpeg" data-download-href="/uploads/short-url/5an8Kh6O6MxF7MsxKBcTk16zIzF.jpeg?dl=1" title="IMG_4461" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24370dc325b35b50540783def039000d5b3db4fb_2_666x500.jpeg" alt="IMG_4461" data-base62-sha1="5an8Kh6O6MxF7MsxKBcTk16zIzF" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24370dc325b35b50540783def039000d5b3db4fb_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24370dc325b35b50540783def039000d5b3db4fb_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24370dc325b35b50540783def039000d5b3db4fb_2_1332x1000.jpeg 2x" data-dominant-color="707383"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4461</span><span class="informations">1920×1440 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a875fcbe60d22724ae11bf62251304c2c63748f8.jpeg" data-download-href="/uploads/short-url/o2h06dlujRwJeSZ0F3ba7MPj0ne.jpeg?dl=1" title="IMG_4463" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a875fcbe60d22724ae11bf62251304c2c63748f8_2_666x500.jpeg" alt="IMG_4463" data-base62-sha1="o2h06dlujRwJeSZ0F3ba7MPj0ne" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a875fcbe60d22724ae11bf62251304c2c63748f8_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a875fcbe60d22724ae11bf62251304c2c63748f8_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a875fcbe60d22724ae11bf62251304c2c63748f8_2_1332x1000.jpeg 2x" data-dominant-color="747784"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4463</span><span class="informations">1920×1440 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @klippert (2022-06-11 05:15 UTC)

<p>Pics of 3d brain after using threshold on LabelMapVolume_1 output from Tsallis segmentation.</p>
<p>Tsallis Values:<br>
Extraction Parameter = 0.1<br>
q parameter = -0.64<br>
alpha = 0.5<br>
beta = 0.5<br>
gama = 0<br>
iteration = 1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c449b57cd9365147750a830b1a6074e409464ca.jpeg" data-download-href="/uploads/short-url/daeUPL37uf7op7NstoS6SHPTHmO.jpeg?dl=1" title="IMG_4483" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c449b57cd9365147750a830b1a6074e409464ca_2_666x500.jpeg" alt="IMG_4483" data-base62-sha1="daeUPL37uf7op7NstoS6SHPTHmO" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c449b57cd9365147750a830b1a6074e409464ca_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c449b57cd9365147750a830b1a6074e409464ca_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c449b57cd9365147750a830b1a6074e409464ca_2_1332x1000.jpeg 2x" data-dominant-color="797B8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4483</span><span class="informations">1920×1440 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47f9ba248136fe911f8c6ccf7c3b47710efb54b2.jpeg" data-download-href="/uploads/short-url/agIWaMh0OtydJlAyr3AO0SLeuLo.jpeg?dl=1" title="IMG_4481" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47f9ba248136fe911f8c6ccf7c3b47710efb54b2_2_666x500.jpeg" alt="IMG_4481" data-base62-sha1="agIWaMh0OtydJlAyr3AO0SLeuLo" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47f9ba248136fe911f8c6ccf7c3b47710efb54b2_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47f9ba248136fe911f8c6ccf7c3b47710efb54b2_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47f9ba248136fe911f8c6ccf7c3b47710efb54b2_2_1332x1000.jpeg 2x" data-dominant-color="7F8395"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4481</span><span class="informations">1920×1440 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28000d34d195bf51ff8c863f2cc0466b500c60a5.jpeg" data-download-href="/uploads/short-url/5HRcYIiU0E5WECbYMUvxPgduZ6t.jpeg?dl=1" title="IMG_4485" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28000d34d195bf51ff8c863f2cc0466b500c60a5_2_666x500.jpeg" alt="IMG_4485" data-base62-sha1="5HRcYIiU0E5WECbYMUvxPgduZ6t" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28000d34d195bf51ff8c863f2cc0466b500c60a5_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28000d34d195bf51ff8c863f2cc0466b500c60a5_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28000d34d195bf51ff8c863f2cc0466b500c60a5_2_1332x1000.jpeg 2x" data-dominant-color="757088"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4485</span><span class="informations">1920×1440 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db800845315eb33f9c86ff3b3c58cde4d79bd31f.jpeg" data-download-href="/uploads/short-url/vjMSbzwPjGuLgI3nkGRNETz3kgT.jpeg?dl=1" title="IMG_4484" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db800845315eb33f9c86ff3b3c58cde4d79bd31f_2_666x500.jpeg" alt="IMG_4484" data-base62-sha1="vjMSbzwPjGuLgI3nkGRNETz3kgT" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db800845315eb33f9c86ff3b3c58cde4d79bd31f_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db800845315eb33f9c86ff3b3c58cde4d79bd31f_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db800845315eb33f9c86ff3b3c58cde4d79bd31f_2_1332x1000.jpeg 2x" data-dominant-color="6B6C78"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4484</span><span class="informations">1920×1440 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d41b1763000f0926ab8c9d066ff09a6723b4452a.jpeg" data-download-href="/uploads/short-url/ugngxaHTFDtkm52FrEujGRrx1FM.jpeg?dl=1" title="IMG_4482" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d41b1763000f0926ab8c9d066ff09a6723b4452a_2_666x500.jpeg" alt="IMG_4482" data-base62-sha1="ugngxaHTFDtkm52FrEujGRrx1FM" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d41b1763000f0926ab8c9d066ff09a6723b4452a_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d41b1763000f0926ab8c9d066ff09a6723b4452a_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d41b1763000f0926ab8c9d066ff09a6723b4452a_2_1332x1000.jpeg 2x" data-dominant-color="7C8093"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4482</span><span class="informations">1920×1440 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f7c8e75d42cfbd8439b6c09ed60097ee9d87fb.jpeg" data-download-href="/uploads/short-url/iYhTXndiWYgM3uDvBMRPug1PMIr.jpeg?dl=1" title="IMG_4490" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84f7c8e75d42cfbd8439b6c09ed60097ee9d87fb_2_666x500.jpeg" alt="IMG_4490" data-base62-sha1="iYhTXndiWYgM3uDvBMRPug1PMIr" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84f7c8e75d42cfbd8439b6c09ed60097ee9d87fb_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84f7c8e75d42cfbd8439b6c09ed60097ee9d87fb_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84f7c8e75d42cfbd8439b6c09ed60097ee9d87fb_2_1332x1000.jpeg 2x" data-dominant-color="624472"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4490</span><span class="informations">1920×1440 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8b8d49d9be6fb9086d7f81ad897ba96a2b61cf8.jpeg" data-download-href="/uploads/short-url/qm7QPEppOlDMwPcuaMaJG5SW7J6.jpeg?dl=1" title="IMG_4488" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8b8d49d9be6fb9086d7f81ad897ba96a2b61cf8_2_666x500.jpeg" alt="IMG_4488" data-base62-sha1="qm7QPEppOlDMwPcuaMaJG5SW7J6" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8b8d49d9be6fb9086d7f81ad897ba96a2b61cf8_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8b8d49d9be6fb9086d7f81ad897ba96a2b61cf8_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8b8d49d9be6fb9086d7f81ad897ba96a2b61cf8_2_1332x1000.jpeg 2x" data-dominant-color="674879"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4488</span><span class="informations">1920×1440 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a1dcfc04ecda8c7a5f5344935746ec35e88aebb.jpeg" data-download-href="/uploads/short-url/lZnoSNNQ4lMHgzsLq15RKW9gStd.jpeg?dl=1" title="IMG_4489" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a1dcfc04ecda8c7a5f5344935746ec35e88aebb_2_666x500.jpeg" alt="IMG_4489" data-base62-sha1="lZnoSNNQ4lMHgzsLq15RKW9gStd" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a1dcfc04ecda8c7a5f5344935746ec35e88aebb_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a1dcfc04ecda8c7a5f5344935746ec35e88aebb_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9a1dcfc04ecda8c7a5f5344935746ec35e88aebb_2_1332x1000.jpeg 2x" data-dominant-color="6C487C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4489</span><span class="informations">1920×1440 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bbdfda6e7d8e70d867d599928f4dfb37ef229a7.jpeg" data-download-href="/uploads/short-url/1FSiWUa223Lqf6Wf352OfKjXch1.jpeg?dl=1" title="IMG_4486" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bbdfda6e7d8e70d867d599928f4dfb37ef229a7_2_666x500.jpeg" alt="IMG_4486" data-base62-sha1="1FSiWUa223Lqf6Wf352OfKjXch1" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bbdfda6e7d8e70d867d599928f4dfb37ef229a7_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bbdfda6e7d8e70d867d599928f4dfb37ef229a7_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bbdfda6e7d8e70d867d599928f4dfb37ef229a7_2_1332x1000.jpeg 2x" data-dominant-color="664773"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4486</span><span class="informations">1920×1440 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/359e4b15075d958e5c5eba15aee66e2229d47e14.jpeg" data-download-href="/uploads/short-url/7EkrL7CLLHmZQdanXWqD3L6OwL2.jpeg?dl=1" title="IMG_4487" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/359e4b15075d958e5c5eba15aee66e2229d47e14_2_666x500.jpeg" alt="IMG_4487" data-base62-sha1="7EkrL7CLLHmZQdanXWqD3L6OwL2" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/359e4b15075d958e5c5eba15aee66e2229d47e14_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/359e4b15075d958e5c5eba15aee66e2229d47e14_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/359e4b15075d958e5c5eba15aee66e2229d47e14_2_1332x1000.jpeg 2x" data-dominant-color="654378"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4487</span><span class="informations">1920×1440 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @Mehran (2022-06-12 13:50 UTC)

<p>Hi Kurt,<br>
It might be because of artifact or resolution that all brain is not extracted. You may use N4 Bias correction, noise remove, … to improve the results. If you want, you can send your image to have a look.<br>
Best,</p>

---

## Post #17 by @dr_usman_sani (2023-11-18 13:33 UTC)

<p>hi my question is not relevant to your querry but i am begginer how this happend that your T2 axial image is not distorted in other planes ( sagittal and coronal)i cannot get rid of leggo shaped/staircase artefact.</p>

---

## Post #18 by @drnoorfatima (2026-02-17 08:56 UTC)

<aside class="quote no-group" data-username="klippert" data-post="1" data-topic="23718">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/eb9ed0/48.png" class="avatar"> klippert:</div>
<blockquote>
<p>Dear Community,</p>
<p>I’m just a 3d printing nerd looking to print my brain from MRI/DCOM files. I’ve been able to extract my brain using HD-BET and Swiss Skull Stripper. Now I’m trying to just isolate the gray matter/cerebral cortex/folds, etc. However, when I use thresholding in segment editor on the extracted brain segment, I can’t seem to get the structure definition on the sides/rear (too smooth) of my brain as shown in the pics.</p>
<p>If anyone has a step by step tutorial I would greatly appreciated it. I’m just trying to develop a recipe to 3d print brains for myself and family.</p>
<p>I found a brain logistic segmentation extension in the attached pic. This appears to isolate gray/white matter in 3d slicer, but not sure how to install it? I don’t see it in the list of extensions inside 3d slicer, but I guess there is a way to download the python files, but not that familiar with how to install manually and what sub directory to add it to?</p>
<p>Any help would be appreciated.</p>
<p>Thanks,<br>
Kurt</p>
</blockquote>
</aside>
<p>Hi Kurt, what a cool project!</p>
<p>The smoothness issue you’re seeing on the sides and rear is actually a really common frustration with this workflow, thresholding alone isn’t designed to capture cortical surface detail well, especially the sulci and gyri. It’s not something you can fix just by adjusting the threshold values.</p>
<p>Getting the cortical folds to come out properly for 3D printing involves a few extra steps beyond what most tutorials cover, and the extension route you found has some compatibility nuances that trip people up.</p>
<p>I work with brain MRI segmentation and have done similar pipelines before. If you want I can take a look at what you have and point you in the right direction, feel free to DM me.</p>

---
