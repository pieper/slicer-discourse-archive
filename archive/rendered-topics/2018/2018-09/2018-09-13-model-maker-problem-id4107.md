# Model maker problem

**Topic ID**: 4107
**Date**: 2018-09-13
**URL**: https://discourse.slicer.org/t/model-maker-problem/4107

---

## Post #1 by @Ghaddy (2018-09-13 18:17 UTC)

<p>Hi<br>
I am having a problem with the model maker tool with some files /not all/… once I open a .giple file it wont let me put any thing in input/volume so I can not hit apply to create segmented model.</p>
<p>I also noticed that the background in these files are gray.<br>
While in other files i have black background.</p>
<p>Attached is screen shot of the problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a017b17c99b2ba3f242766f90eb502d9bd48002c.jpeg" data-download-href="/uploads/short-url/mQf9N9GirZ8zKgNe6f829YJBzWI.jpeg?dl=1" title="3173260A-50F8-4258-A4C0-AB5A3CCDD646" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a017b17c99b2ba3f242766f90eb502d9bd48002c_2_666x500.jpeg" alt="3173260A-50F8-4258-A4C0-AB5A3CCDD646" data-base62-sha1="mQf9N9GirZ8zKgNe6f829YJBzWI" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a017b17c99b2ba3f242766f90eb502d9bd48002c_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a017b17c99b2ba3f242766f90eb502d9bd48002c_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a017b17c99b2ba3f242766f90eb502d9bd48002c_2_1332x1000.jpeg 2x" data-dominant-color="89888B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3173260A-50F8-4258-A4C0-AB5A3CCDD646</span><span class="informations">1600×1200 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The second one is when it is working correctly<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ad23e28f35c2ad5649391c5885c8e65681b79b7.jpeg" data-download-href="/uploads/short-url/m5BYmvtsQona16nDnc6XzhVKgpF.jpeg?dl=1" title="0E40EB77-1DA4-476B-B0CE-9BB906429902" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad23e28f35c2ad5649391c5885c8e65681b79b7_2_666x500.jpeg" alt="0E40EB77-1DA4-476B-B0CE-9BB906429902" data-base62-sha1="m5BYmvtsQona16nDnc6XzhVKgpF" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad23e28f35c2ad5649391c5885c8e65681b79b7_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad23e28f35c2ad5649391c5885c8e65681b79b7_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad23e28f35c2ad5649391c5885c8e65681b79b7_2_1332x1000.jpeg 2x" data-dominant-color="8B827D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0E40EB77-1DA4-476B-B0CE-9BB906429902</span><span class="informations">1600×1200 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thaaaank you</p>

---

## Post #2 by @lassoan (2018-09-13 18:22 UTC)

<aside class="quote no-group quote-modified" data-username="Ghaddy" data-post="1" data-topic="4107">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/3bc359/48.png" class="avatar"> Ghaddy:</div>
<blockquote>
<p>intensity segmenter tool</p>
</blockquote>
</aside>
<p>What intensity segmenter tool are you referring to?</p>
<aside class="quote no-group" data-username="Ghaddy" data-post="1" data-topic="4107">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/3bc359/48.png" class="avatar"> Ghaddy:</div>
<blockquote>
<p>once I open a .giple file it wont let me put any thing in input/volume so I can not hit apply to create segmented model</p>
</blockquote>
</aside>
<p>What is a .giple file? If it is an image volume file format then all you need to do is to indicate upon loading that you want this volume to be interpreted as a labelmap: in “Add data” dialog click “Show options” and check “LabelMap” checkbox.</p>

---

## Post #3 by @Ghaddy (2018-09-13 18:28 UTC)

<p>I am sooo sorry… I edited the title and the post, I meant Model maker tool.<br>
a -.gipl file is a -.dicom (CBCT file) file was converted to .gipl by using itk.Snap software.</p>

---

## Post #4 by @cpinter (2018-09-13 18:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4107">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What intensity segmenter tool are you referring to?</p>
</blockquote>
</aside>
<p>This is what I found:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/master/IntensitySegmenter.s4ext">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/IntensitySegmenter.s4ext" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/master/IntensitySegmenter.s4ext" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/master/IntensitySegmenter.s4ext</a></h4>


      <pre><code class="lang-s4ext">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/DCBIA-OrthoLab/IntensitySegmenter.git
scmrevision release

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends     NA

# Inner build directory (default is .)
build_subdirectory .

# homepage
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/IntensitySegmenter.s4ext" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
It’s a CLI module.</p>

---

## Post #5 by @cpinter (2018-09-13 18:44 UTC)

<p>What I’d suggest is to do the whole workflow in Slicer. It can import the CBCT, and you can do nice visualizations of it. Segment Editor is probably the most advanced freely available manual and semi-automated tools out there, which can save the result to STL, DICOM SEG, etc. If the Intensity Segmentation tool you referred to is essential to your work, then as <a class="mention" href="/u/lassoan">@lassoan</a> said in <a href="https://discourse.slicer.org/t/model-is-not-showing/4104">this thread</a> we can probably easily add it to Segment Editor as a new effect. You won’t even need to use Model Maker because Segment Editor takes care of the conversions internally.<br>
This is how such a workflow looks in Slicer: <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>
<p>Update: Making <a href="https://issues.slicer.org/view.php?id=4400#c15981">CLIs Segmentation enabled</a> would solve this problem too. Then there would be no need to add an effect for each segmenter CLI.</p>

---

## Post #6 by @Ghaddy (2018-09-13 19:02 UTC)

<p>I really appreciate your help…</p>
<p>Actually, the idea of my research is to measure the skeletal relapse after jaw surgery. I mean the movement happened between CBCT taken at T1 and another CBCT taken at T2.<br>
I had to do superimposition of theses 2 CBCTs or .dicom files using Dolphin Software (common software for orthodontist ) then export the result as reg.T2.dicom files.</p>
<p>I was told that I have to convert T1.dicom files and reg.T2.dicom files to T1.gipl + reg.T2.gibl files using ITk sanp first.<br>
Then use intensity segmenter tool from slicer.<br>
Then make a model for T1.vtk and reg.T2.vtk<br>
Then finally open these 2 files together in slicer with tool pick and paint + mesh stat to mesure the relapse.</p>
<p>I know it is a little bit complicated and time consuming but this what I was told by other resident.</p>
<p>I watch and read the stuff that you provided and hopefully it can be applied in my data.<br>
Thank you again and I really appreciate yoyr help</p>

---

## Post #7 by @cpinter (2018-09-13 19:07 UTC)

<p>You can do the superimposition (we call it registration) in Slicer too. I’d first try the SlicerElastix extension. If you have problems then “General Registration (BRAINS)” in Slicer is another very good registration module but harder to use (although there is a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">registration case library</a> that can help).</p>
<aside class="quote no-group" data-username="Ghaddy" data-post="6" data-topic="4107">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/3bc359/48.png" class="avatar"> Ghaddy:</div>
<blockquote>
<p>tool pick and paint + mesh stat</p>
</blockquote>
</aside>
<p>I don’t understand this part. Can you please elaborate on the measurement step?</p>

---

## Post #8 by @Ghaddy (2018-09-13 19:44 UTC)

<p>Thaanks, I will try this new way and see</p>
<p>pick 'n paint and mesh statistics tools are working together.<br>
once you have your final model.vtk opened by slicer… choose pick 'n paint tool and you can add more then one points and region of interest (ROI) on your model then go to tool mesh and statistics then adjust some settings then hit Run… you will get numbers or measurements (max., min., mean and SD)  that measure the distance between the point that you picked (basically the difference between T1 and T2 in specific point)</p>

---

## Post #9 by @lassoan (2018-09-13 20:41 UTC)

<p>Your workflow could be the following:</p>
<ul>
<li>import CBCT using DICOM module (or you can drag-and-drop the folder on application window to import a DICOM folder)</li>
<li>load volume from DICOM browser</li>
<li>segment volume using Segment editor module (you can segment bone using simple thresholding, maybe some smoothing, scissors, etc.)</li>
<li>export segmentation to model node using Segmentations module export section</li>
<li>continue with pick’n’paint and mesh statistics as before</li>
</ul>

---

## Post #10 by @hortakc (2022-09-28 19:12 UTC)

<p>Hello Ghaddy!<br>
I am trying to use the same methodology you mentioned.<br>
Were you able to figure out how to do the superimposition?<br>
I am supposed to follow the steps: conversion of Dicom files to GIPL in ITK, Resampling in 3D Slicer, and now Segment with Intensity Segmenter in 3D Slicer.<br>
I am stuck in this last step… when I try to apply the Range Files , it does not change or apply<br>
I used this range of files in Slicer 4.0, but now I only have Slicer 5.0.</p>

---

## Post #11 by @muratmaga (2022-09-28 21:21 UTC)

<p>This is a 4 year old thread. If you are using Slicer 5.0, you should use the segment editor and segmentation modules to do your model creation. See relevant documentation here:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>

---

## Post #12 by @hortakc (2022-09-29 15:43 UTC)

<p>Thank you!!! I will explore the modules you mentioned!</p>

---
