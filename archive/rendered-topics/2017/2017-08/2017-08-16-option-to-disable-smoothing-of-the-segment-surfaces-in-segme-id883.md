# Option to disable smoothing of the segment surfaces in Segment Editor

**Topic ID**: 883
**Date**: 2017-08-16
**URL**: https://discourse.slicer.org/t/option-to-disable-smoothing-of-the-segment-surfaces-in-segment-editor/883

---

## Post #1 by @fedorov (2017-08-16 19:33 UTC)

<p>I think it might be helpful to add an option to Segment Editor to disable smoothing of the surface when generating it from the label map representation. When regions are small, smoothing can lead to significant under-estimation of the boundary, as shown in the screenshot below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3826cc54a9f7b063ce79afb60fd4517bcdd72e5.jpeg" data-download-href="/uploads/short-url/nktge1aWmfs6esGGusb84Ts5pUV.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a3826cc54a9f7b063ce79afb60fd4517bcdd72e5_2_613x500.jpg" alt="image" data-base62-sha1="nktge1aWmfs6esGGusb84Ts5pUV" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a3826cc54a9f7b063ce79afb60fd4517bcdd72e5_2_613x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a3826cc54a9f7b063ce79afb60fd4517bcdd72e5_2_919x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a3826cc54a9f7b063ce79afb60fd4517bcdd72e5_2_1226x1000.jpg 2x" data-dominant-color="8D95AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1537×1253 412 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Of note, the option to disable smoothing was available in the legacy editor.</p>
<p>The segmentation dataset used in this example is publicly available in the <a href="https://wiki.cancerimagingarchive.net/display/Public/QIN-HEADNECK">TCIA QIN-HEADNECK collection</a>, and can be downloaded using the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/TCIABrowser">TCIABrowser extension</a>. You will need to install <a href="https://qiicr.gitbooks.io/quantitativereporting-guide/">Quantitative Reporting extension</a> first to be able to load DICOM SEG series. The details on patient/study/series are shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/480d4d0fda5f4dca7f84768fd30110d4d376e0d3.png" data-download-href="/uploads/short-url/ahoSgcC2lIIiyJ4QEvD41NL0JRV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/480d4d0fda5f4dca7f84768fd30110d4d376e0d3_2_690x468.png" alt="image" data-base62-sha1="ahoSgcC2lIIiyJ4QEvD41NL0JRV" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/480d4d0fda5f4dca7f84768fd30110d4d376e0d3_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/480d4d0fda5f4dca7f84768fd30110d4d376e0d3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/480d4d0fda5f4dca7f84768fd30110d4d376e0d3.png 2x" data-dominant-color="E5E9F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">769×522 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Lorensen (2017-08-16 20:25 UTC)

<p>What smoothing is used?</p>

---

## Post #3 by @lassoan (2017-08-16 20:31 UTC)

<p>It’s true that smoothing parameter requires a lot of clicks. I’ve added a ticket to the issue tracker to address it: <a href="https://issues.slicer.org/view.php?id=4415">https://issues.slicer.org/view.php?id=4415</a></p>

---

## Post #4 by @lassoan (2017-08-16 20:34 UTC)

<p>vtkWindowedSincPolyDataFilter is used, see the filter setup code here: <a href="https://github.com/Slicer/Slicer/blob/481873378dfbbdbe2b17db8feedf11496280b9ba/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L197-L212">https://github.com/Slicer/Slicer/blob/481873378dfbbdbe2b17db8feedf11496280b9ba/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L197-L212</a></p>
<p>Maybe we could normalize default PassBand cutoff frequency by the spacing of the input binary labelmap to not require any tuning based on the voxel size.</p>

---

## Post #5 by @Lorensen (2017-08-16 20:36 UTC)

<p>Have you considered a “cubes” display. It shows each vowel on the surface of the segmentation. Here is an example from the BWH Brain Atlas.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9d274166378c5be803e4f8aa8510c37f7100f36.png" data-download-href="/uploads/short-url/xmu8ZInEip9lYoZefEaKOgqduJw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d274166378c5be803e4f8aa8510c37f7100f36_2_690x363.png" alt="image" data-base62-sha1="xmu8ZInEip9lYoZefEaKOgqduJw" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d274166378c5be803e4f8aa8510c37f7100f36_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9d274166378c5be803e4f8aa8510c37f7100f36_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9d274166378c5be803e4f8aa8510c37f7100f36.png 2x" data-dominant-color="7D797B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1215×640 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The left image is smoothed, the right image shows cubes.</p>

---

## Post #6 by @lassoan (2017-08-16 20:41 UTC)

<p>I can imagine that for certain applications cube may be acceptable but it often provides very poor results (you cannot even make out the shape of a segment).</p>
<p>If smoothing is done right, it just removes artifacts due to finite resolution. If relevant details are lost as a result of smoothing (there is no smoothing factor that removes staircase artifacts without removing relevant details) then it means that a supersampled binary labelmap or a fractional labelmap has to be used.</p>

---

## Post #7 by @Lorensen (2017-08-16 20:43 UTC)

<p>Cubes are useful when editing, not as a final rep. You can see each vowel.</p>

---

## Post #8 by @Lorensen (2017-08-16 20:44 UTC)

<p>Not sure of the units. I always use .001 for bandpass</p>

---

## Post #9 by @Lorensen (2017-08-16 20:49 UTC)

<p>To produce the final smoothed models, you should process all labels at once. Segments that touch will remain touching after smoothing. If the entire volume is segmented, this will reduce the shrinkage.</p>
<p>This example does that.<br>
<a href="https://lorensen.github.io/VTKExamples/site//Cxx/Medical/GenerateModelsFromLabels/" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site//Cxx/Medical/GenerateModelsFromLabels/</a></p>

---

## Post #10 by @lassoan (2017-08-16 21:00 UTC)

<p>Segments are independent volumes that may even overlap each other, but we do use this joint smoothing technique when we apply smoothing to <em>modify</em> segments (to remove noise or segmentation errors). For <em>display</em>, we only apply just as much smoothing to remove staircase artifacts.</p>
<p>Do you think it would make a difference if we didn’t just smooth a structure as is but we add a “negative” structure around it and smooth together? (other than of course that the structure’s surface will not be treated as a boundary anymore, so BoundarySmoothing flag will have no effect)</p>

---

## Post #11 by @lassoan (2017-08-16 21:05 UTC)

<p>What filter do you use to generate the cubes display? Is it faster than marching cubes?</p>

---

## Post #12 by @fedorov (2017-08-16 21:05 UTC)

<p>Setting smoothing factor to 0 in the “Advanced segmentation conversion” setting produces the result I wanted to see in this example. I think adding a checkbox somewhere in Segment Editor that would effectively reset this parameter to 0 would be helpful, and would provide functionality equivalent to what was available in the old Editor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1fef2c7ba29420ff961a48ae94a7f5897a841f7.png" data-download-href="/uploads/short-url/ywNigUa6DsBKLx7KCusnuSO8GKb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fef2c7ba29420ff961a48ae94a7f5897a841f7_2_279x500.png" alt="image" data-base62-sha1="ywNigUa6DsBKLx7KCusnuSO8GKb" width="279" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fef2c7ba29420ff961a48ae94a7f5897a841f7_2_279x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1fef2c7ba29420ff961a48ae94a7f5897a841f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1fef2c7ba29420ff961a48ae94a7f5897a841f7.png 2x" data-dominant-color="EAECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">308×551 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Lorensen (2017-08-16 21:19 UTC)

<p>It’s fast. It does not use a filter. It converts point data to cell data.</p>
<p>See:<br>
<a href="https://lorensen.github.io/VTKExamples/site/Cxx/Medical/GenerateCubesFromLabels/" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Cxx/Medical/GenerateCubesFromLabels/</a></p>

---

## Post #14 by @Lorensen (2017-08-16 21:53 UTC)

<p>This version saves each model in a file. If could be convetted into a<br>
command line module.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lorensen/OpenAtlas/blob/master/Tools/GenerateCubesFromLabels.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lorensen/OpenAtlas/blob/master/Tools/GenerateCubesFromLabels.cxx" target="_blank" rel="nofollow noopener">lorensen/OpenAtlas/blob/master/Tools/GenerateCubesFromLabels.cxx</a></h4>
<pre><code class="lang-cxx">//
// GenerateModelsFromLabels
//   Usage: GenerateModelsFromLabels AtlasConfigFile StartLabel EndLabel
//          where
//          AtlasConfigFile is an atlas configuration file that defines
//            locations of various atlas file
//          StartLabel is the first label to be processed
//          EndLabel is the last label to be processed
//          NOTE: There can be gaps in the labeling. If a label does
//          not exist in the volume, it will be skipped.
//      
//
#include &lt;itkImageFileReader.h&gt;
#include &lt;itkOrientImageFilter.h&gt;
#include &lt;itkChangeInformationImageFilter.h&gt;
#include &lt;itkImageToVTKImageFilter.h&gt;
#include &lt;itksys/SystemTools.hxx&gt;

#include &lt;vtkPolyDataConnectivityFilter.h&gt;
#include &lt;vtkImageAccumulate.h&gt;
</code></pre>

  This file has been truncated. <a href="https://github.com/lorensen/OpenAtlas/blob/master/Tools/GenerateCubesFromLabels.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #15 by @lassoan (2017-08-16 22:55 UTC)

<p>Thank you, I’ll have a look at this.</p>

---

## Post #16 by @lassoan (2018-11-12 18:05 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I think adding a checkbox somewhere in Segment Editor that would effectively reset this parameter to 0 would be helpful</p>
</blockquote>
</aside>
<p>This is implemented now in Slicer <a href="https://github.com/Slicer/Slicer/commit/06ae9980af2c01a8f38ee2e7cfd930375f729b6d">master branch</a> and should be available in tomorrow’s nightly build. A checkbox is available directly in the “Show 3D” button’s menu:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fda2d861929e110207db1646ae654258ca05c099.png" data-download-href="/uploads/short-url/AbLH32mB2eewedNESAWHm36UxjX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fda2d861929e110207db1646ae654258ca05c099_2_690x228.png" alt="image" data-base62-sha1="AbLH32mB2eewedNESAWHm36UxjX" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fda2d861929e110207db1646ae654258ca05c099_2_690x228.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fda2d861929e110207db1646ae654258ca05c099_2_1035x342.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fda2d861929e110207db1646ae654258ca05c099.png 2x" data-dominant-color="DEE2E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×344 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @lassoan (2021-10-07 14:29 UTC)

<p>A post was merged into an existing topic: <a href="/t/surface-smoothing-and-exporting-model/1144/6">Surface smoothing and exporting model</a></p>

---
