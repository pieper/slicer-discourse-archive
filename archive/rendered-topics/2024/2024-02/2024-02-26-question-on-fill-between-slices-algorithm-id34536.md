# Question on Fill Between Slices algorithm

**Topic ID**: 34536
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/question-on-fill-between-slices-algorithm/34536

---

## Post #1 by @MJamal (2024-02-26 05:48 UTC)

<p>Hello again,</p>
<p>I have a question regarding the “fill between slices” operation. When I perform this operation, I don’t see a smooth surface in the 3D view when clicking “show 3D.” It appears that the preview model has a lot of irregularities in the surface. Please find the attached screen capture and video that demonstrate how I generated the preview.</p>
<p>Video Reference: <a href="https://drive.google.com/file/d/1VySIn1fupz2qXyzk-Q772jGaaOM5HRa9/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">FillBetweenSlices.mp4 - Google Drive</a><br>
Screen Capture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94c995e95151cce0a541b02b7427125e4f6c9afa.jpeg" data-download-href="/uploads/short-url/leeyLzNpDCR0ioYp0WXnm4YihFo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94c995e95151cce0a541b02b7427125e4f6c9afa_2_482x500.jpeg" alt="image" data-base62-sha1="leeyLzNpDCR0ioYp0WXnm4YihFo" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94c995e95151cce0a541b02b7427125e4f6c9afa_2_482x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94c995e95151cce0a541b02b7427125e4f6c9afa.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94c995e95151cce0a541b02b7427125e4f6c9afa.jpeg 2x" data-dominant-color="808FA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">611×633 44.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @MJamal (2024-02-27 05:13 UTC)

<p>Additionally, in the preview, the top and bottom slices are not as smooth as when using a round paintbrush. It’s noticeable that there are many triangles in the top and bottom slices surface, and the fill between slices appears to have a somewhat rectangular surface.</p>
<p>So, my question is: why doesn’t it have a smooth slope?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> Any thoughts?</p>

---

## Post #3 by @muratmaga (2024-02-27 05:19 UTC)

<p>Try resampling the data to isotropic resolution using the CropVolume before you start the segmentation. In the video you skipped that step (MRHead has anisotropic voxel spacing, 1x1x1.3mm). That should help.</p>
<p>You can also increase the resolution of the segmentation using the <code>Segment Geometry</code> option, and oversample.</p>

---

## Post #4 by @MJamal (2024-02-27 08:43 UTC)

<p>Hello <a class="mention" href="/u/muratmaga">@muratmaga</a>,</p>
<p>Thank you for the suggestion. I’ve implemented your proposed solution and noticed a significant reduction in the number of triangles and the steps on the surface.</p>
<p>I have one more question. As you can see in the following images, the FIRST and LAST slices are circular then I’ve applied the multiple slice edit in the output, intermediate interpolated slices appear to have a square shape.</p>
<p>Image-1:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/043b2f7c815a1012ca25074e4714750b83cdbe07.jpeg" data-download-href="/uploads/short-url/BqIhrT3FIhaVQgEK4XgbD8d5ZR.jpeg?dl=1" title="fbs1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043b2f7c815a1012ca25074e4714750b83cdbe07_2_630x500.jpeg" alt="fbs1" data-base62-sha1="BqIhrT3FIhaVQgEK4XgbD8d5ZR" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043b2f7c815a1012ca25074e4714750b83cdbe07_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/043b2f7c815a1012ca25074e4714750b83cdbe07_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/043b2f7c815a1012ca25074e4714750b83cdbe07.jpeg 2x" data-dominant-color="5F5A59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fbs1</span><span class="informations">1244×986 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image-2:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b9c988e69a4e96974a0ee1edce8a726caed307.jpeg" data-download-href="/uploads/short-url/cEU40Qxc7OvIVQQS7FJrrwvfy7l.jpeg?dl=1" title="fbs2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b9c988e69a4e96974a0ee1edce8a726caed307_2_630x500.jpeg" alt="fbs2" data-base62-sha1="cEU40Qxc7OvIVQQS7FJrrwvfy7l" width="630" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b9c988e69a4e96974a0ee1edce8a726caed307_2_630x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b9c988e69a4e96974a0ee1edce8a726caed307_2_945x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b9c988e69a4e96974a0ee1edce8a726caed307.jpeg 2x" data-dominant-color="5B5858"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fbs2</span><span class="informations">1250×991 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image-3:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bad88c05f0cdc8f096994b750756d8d9b2431020.jpeg" data-download-href="/uploads/short-url/qEUL4vBuKgktlLvdRi3JZb918Wc.jpeg?dl=1" title="fbs3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bad88c05f0cdc8f096994b750756d8d9b2431020_2_629x500.jpeg" alt="fbs3" data-base62-sha1="qEUL4vBuKgktlLvdRi3JZb918Wc" width="629" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bad88c05f0cdc8f096994b750756d8d9b2431020_2_629x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bad88c05f0cdc8f096994b750756d8d9b2431020_2_943x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bad88c05f0cdc8f096994b750756d8d9b2431020.jpeg 2x" data-dominant-color="605B5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fbs3</span><span class="informations">1247×991 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Eventually it should be tapered cone like interpolation as shown in the below GIF:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b7c8a57b4beac0fb5e35fac759955e6637b5df.gif" alt="SlicerCapture" data-base62-sha1="dNBAHYtt7iFH9yo2tNse7Uwx3cP" width="496" height="500" class="animated"></p>
<p>How to address this issue?</p>

---

## Post #5 by @muratmaga (2024-02-27 16:44 UTC)

<p>Not sure. try turning of the smoothing for the model creation (under the show 3D options).</p>

---

## Post #6 by @MJamal (2024-02-28 05:52 UTC)

<p>I tried disabling the smoothing option, but it didn’t work.:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1s-yn4Ton9KK5TolSNyxI_-CO0s7GwEja/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1s-yn4Ton9KK5TolSNyxI_-CO0s7GwEja/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1s-yn4Ton9KK5TolSNyxI_-CO0s7GwEja/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1s-yn4Ton9KK5TolSNyxI_-CO0s7GwEja/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">36235232.mp4</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2024-02-28 06:11 UTC)

<p>The diamond-shaped cross-section is just a result of how distance is estimated by a series of morphological operations (one voxel dilation in diagonal direction is 1.44x longer than in sideways, therefore repeated dilations result in a diamond shape). You can find more detailed description of the algorithm at <a href="https://insight-journal.org/browse/publication/977">https://insight-journal.org/browse/publication/977</a></p>
<p>You can switch to a distance transform based dilation instead of repeated morphological dilations, which will provide more rounded cross-sections. For this, you just need to add a single line to SegmentEditorFillBetweenSlicesEffect.py:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a2020c790f222fd9aae589bf8bca98bd02f37695/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorFillBetweenSlicesEffect.py#L52">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a2020c790f222fd9aae589bf8bca98bd02f37695/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorFillBetweenSlicesEffect.py#L52" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a2020c790f222fd9aae589bf8bca98bd02f37695/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorFillBetweenSlicesEffect.py#L52" target="_blank" rel="noopener">Slicer/Slicer/blob/a2020c790f222fd9aae589bf8bca98bd02f37695/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorFillBetweenSlicesEffect.py#L52</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="42" style="counter-reset: li-counter 41 ;">
          <li>&lt;li&gt;The complete segmentation will be created by interpolating segmentations in empty slices.</li>
          <li>&lt;/ul&gt;&lt;p&gt;</li>
          <li>Masking settings are ignored. If segments overlap, segment higher in the segments table will have priority.</li>
          <li>The effect uses  &lt;a href="https://insight-journal.org/browse/publication/977"&gt;morphological contour interpolation method&lt;/a&gt;.</li>
          <li>&lt;p&gt;""")</li>
          <li></li>
          <li>    def computePreviewLabelmap(self, mergedImage, outputLabelmap):</li>
          <li>        import vtkITK</li>
          <li></li>
          <li>        interpolator = vtkITK.vtkITKMorphologicalContourInterpolator()</li>
          <li class="selected">        interpolator.SetInputData(mergedImage)</li>
          <li>        interpolator.Update()</li>
          <li>        outputLabelmap.DeepCopy(interpolator.GetOutput())</li>
          <li>        imageToWorld = vtk.vtkMatrix4x4()</li>
          <li>        mergedImage.GetImageToWorldMatrix(imageToWorld)</li>
          <li>        outputLabelmap.SetImageToWorldMatrix(imageToWorld)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Before <code>SetInputData(...)</code> line, add this line:</p>
<pre data-code-wrap="python"><code class="lang-python">interpolator.SetUseDistanceTransform(True)
</code></pre>
<p>However, in general these small details should not matter: wherever you don’t find the interpolated contour to be accurate enough, you can segment an additional slice there (and the 3D interpolation result will be updated automatically).</p>
<p>If you want to reconstruct a surface from extremely sparse contours using linear interpolation then you can use SlicerRT module’s planar contour to closed surface converter rule. This is used when importing DICOM RT structure sets, or when converting <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py">OsiriX ROIs to segmentations</a>.</p>
<p>If you want to reconstruct a tubular surface then the easiest may be to use vtkTubeFilter.</p>
<p>What is your use case? Why do you attempt to reconstruct a 3D surface from cross-sections that are so extremely far from each other?</p>

---

## Post #8 by @MJamal (2024-04-10 12:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your suggestions.</p>
<table>
  <tbody><tr>
    <th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9bacf9703bf8cd81b22fb02cdf3a01aca7af96d.png" data-download-href="/uploads/short-url/oduVQubz7NztAplnlUuG5KUnAPX.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9bacf9703bf8cd81b22fb02cdf3a01aca7af96d_2_690x400.png" data-base62-sha1="oduVQubz7NztAplnlUuG5KUnAPX" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9bacf9703bf8cd81b22fb02cdf3a01aca7af96d_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9bacf9703bf8cd81b22fb02cdf3a01aca7af96d_2_1035x600.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9bacf9703bf8cd81b22fb02cdf3a01aca7af96d.png 2x" data-dominant-color="9296C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1287×747 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
    <th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aab3e77d6aada96e3bfb7d2998f88f38f818a974.png" data-download-href="/uploads/short-url/om6C0DOGVssBEryDU14a0av8tzm.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab3e77d6aada96e3bfb7d2998f88f38f818a974_2_690x403.png" data-base62-sha1="om6C0DOGVssBEryDU14a0av8tzm" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab3e77d6aada96e3bfb7d2998f88f38f818a974_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab3e77d6aada96e3bfb7d2998f88f38f818a974_2_1035x604.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aab3e77d6aada96e3bfb7d2998f88f38f818a974.png 2x" data-dominant-color="9298C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1285×751 86.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
  </tr>
</tbody></table>
<p>I tried distance transform-based dilation, but I don’t see much difference in the voxel dilations as shown in the above images. Yes, if we look from the top view of the model, we see somewhat rounded cross-sections better than compared to the previous approach.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="34536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to reconstruct a tubular surface, then the easiest way may be to use vtkTubeFilter.</p>
</blockquote>
</aside>
<p>Yes, I want to reconstruct tubular surfaces but with varying radii. For example, consider the sideway figures below. Imagine the white lines as the diameter of a round brush. What I want is to reconstruct a tubular-like surface between these slices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8672816ff7756bd136432c3ccc6e5d9e2b2358d.png" data-download-href="/uploads/short-url/zrtqkqDOONT66wlKCFmW3nnHqSp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8672816ff7756bd136432c3ccc6e5d9e2b2358d_2_690x209.png" alt="image" data-base62-sha1="zrtqkqDOONT66wlKCFmW3nnHqSp" width="690" height="209" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8672816ff7756bd136432c3ccc6e5d9e2b2358d_2_690x209.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8672816ff7756bd136432c3ccc6e5d9e2b2358d_2_1035x313.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8672816ff7756bd136432c3ccc6e5d9e2b2358d.png 2x" data-dominant-color="131414"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1256×382 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="34536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your use case? Why are you attempting to reconstruct a 3D surface from cross-sections that are so extremely far from each other?</p>
</blockquote>
</aside>
<p>For the resulting model to be accurate when using a round paint brush, the filled area between the slices, specifically the surface, should have a rounded cross-section.</p>

---

## Post #9 by @lassoan (2024-04-10 13:43 UTC)

<p>Probably adding <code>interpolator.SetUseBallStructuringElement(True)</code> will provide the result you expect. We may make it the default, as it indeed a more natural-looking interpolation when segmented slices are very far from each other.</p>

---

## Post #10 by @MJamal (2024-04-10 14:18 UTC)

<p>Unfortunately, the result still looks the same to me after setting this to True.</p>
<p>Here’s the output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68da4e1f1130fee6d56a5f31c5de1d6c089b698d.png" data-download-href="/uploads/short-url/eXzna29s1bSDgi8SKKXGhFMVRP7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68da4e1f1130fee6d56a5f31c5de1d6c089b698d_2_233x250.png" alt="image" data-base62-sha1="eXzna29s1bSDgi8SKKXGhFMVRP7" width="233" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68da4e1f1130fee6d56a5f31c5de1d6c089b698d_2_233x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68da4e1f1130fee6d56a5f31c5de1d6c089b698d_2_349x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68da4e1f1130fee6d56a5f31c5de1d6c089b698d_2_466x500.png 2x" data-dominant-color="98A0BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×752 47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was expecting the surface to be like this (marked in orange):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54280faa42caf29790308dac5ac4d11946595063.png" data-download-href="/uploads/short-url/c0tWaxjZ4iqen6AB9UISjhOLJGX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54280faa42caf29790308dac5ac4d11946595063_2_233x250.png" alt="image" data-base62-sha1="c0tWaxjZ4iqen6AB9UISjhOLJGX" width="233" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54280faa42caf29790308dac5ac4d11946595063_2_233x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54280faa42caf29790308dac5ac4d11946595063_2_349x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54280faa42caf29790308dac5ac4d11946595063_2_466x500.png 2x" data-dominant-color="939BBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">502×538 44.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2024-04-10 18:38 UTC)

<p>I compared all the combinations of the two flags and it seems that actually UseDistanceTransform gives the best result.</p>
<p>UseDistanceTransform = False, UseBallStructuringElement = False:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4baf286ee3d45d3d29b2bc0af26fd376244e4e5.jpeg" data-download-href="/uploads/short-url/wDroyPCuFlVm0OIHjBrKx7r0lXT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4baf286ee3d45d3d29b2bc0af26fd376244e4e5_2_690x373.jpeg" alt="image" data-base62-sha1="wDroyPCuFlVm0OIHjBrKx7r0lXT" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4baf286ee3d45d3d29b2bc0af26fd376244e4e5_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4baf286ee3d45d3d29b2bc0af26fd376244e4e5_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4baf286ee3d45d3d29b2bc0af26fd376244e4e5_2_1380x746.jpeg 2x" data-dominant-color="717584"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1415×766 60.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>UseDistanceTransform = False, UseBallStructuringElement = True:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb9dbc9e1c04640c0812af50db3501235d7c102f.jpeg" data-download-href="/uploads/short-url/t3gSjnGyAh3AbrGdKfFqL3fO59J.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9dbc9e1c04640c0812af50db3501235d7c102f_2_690x377.jpeg" alt="image" data-base62-sha1="t3gSjnGyAh3AbrGdKfFqL3fO59J" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9dbc9e1c04640c0812af50db3501235d7c102f_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9dbc9e1c04640c0812af50db3501235d7c102f_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb9dbc9e1c04640c0812af50db3501235d7c102f_2_1380x754.jpeg 2x" data-dominant-color="717585"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1415×774 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>UseDistanceTransform = True (UseBallStructuringElement value does not make any difference):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b4a31049607c903f131f228a464cc3a200877c8.jpeg" data-download-href="/uploads/short-url/6aXu7a1kFTfqwc5x37nWcapmUGs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4a31049607c903f131f228a464cc3a200877c8_2_690x378.jpeg" alt="image" data-base62-sha1="6aXu7a1kFTfqwc5x37nWcapmUGs" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4a31049607c903f131f228a464cc3a200877c8_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4a31049607c903f131f228a464cc3a200877c8_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b4a31049607c903f131f228a464cc3a200877c8_2_1380x756.jpeg 2x" data-dominant-color="717585"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1411×773 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @MJamal (2024-04-13 14:53 UTC)

<p>I tried the flag <code>UseDistanceTransform</code> in 5.6.2, and hopefully, it is giving me expected results.</p>
<table>
<tbody><tr>
<th>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75dfef8f13dc99f34870fd1cc6231617de32ff0a.jpeg" data-download-href="/uploads/short-url/gOLDWqvc77d4xKG0r0kHrvXa40W.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75dfef8f13dc99f34870fd1cc6231617de32ff0a_2_690x446.jpeg" data-base62-sha1="gOLDWqvc77d4xKG0r0kHrvXa40W" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75dfef8f13dc99f34870fd1cc6231617de32ff0a_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75dfef8f13dc99f34870fd1cc6231617de32ff0a_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75dfef8f13dc99f34870fd1cc6231617de32ff0a.jpeg 2x" data-dominant-color="47494F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1378×892 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
</th>
<th>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/555c3d69b739a8ae06c2f019b574177b8373c49a.jpeg" data-download-href="/uploads/short-url/cb8cTKedWjN24diXLf1mJVECS9A.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/555c3d69b739a8ae06c2f019b574177b8373c49a_2_690x445.jpeg" data-base62-sha1="cb8cTKedWjN24diXLf1mJVECS9A" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/555c3d69b739a8ae06c2f019b574177b8373c49a_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/555c3d69b739a8ae06c2f019b574177b8373c49a_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/555c3d69b739a8ae06c2f019b574177b8373c49a.jpeg 2x" data-dominant-color="47494F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1377×890 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
</th>
</tr>
<tr>
<td>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c5c0603ec72e44dd28e44101235ff23791412d9.png" data-download-href="/uploads/short-url/fsAJ1FSA4zBv7uys2TWbr0tDHGF.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5c0603ec72e44dd28e44101235ff23791412d9_2_690x448.png" data-base62-sha1="fsAJ1FSA4zBv7uys2TWbr0tDHGF" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5c0603ec72e44dd28e44101235ff23791412d9_2_690x448.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5c0603ec72e44dd28e44101235ff23791412d9_2_1035x672.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5c0603ec72e44dd28e44101235ff23791412d9_2_1380x896.png 2x" data-dominant-color="989BD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1380×896 61.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
</td>
<td>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/540207fb584668697274f9080f7581deeb43fa4f.jpeg" data-download-href="/uploads/short-url/bZastxIgz9y7WiKC2xR8Jx6iEEf.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540207fb584668697274f9080f7581deeb43fa4f_2_690x445.jpeg" data-base62-sha1="bZastxIgz9y7WiKC2xR8Jx6iEEf" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540207fb584668697274f9080f7581deeb43fa4f_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540207fb584668697274f9080f7581deeb43fa4f_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/540207fb584668697274f9080f7581deeb43fa4f_2_1380x890.jpeg 2x" data-dominant-color="373934"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1380×891 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>
</td>
</tr>
</tbody></table>
<p>However, if we look into the sagittal view, you will notice the surface looks like something Concave. Also, in the top view of 3D, it seems like the filled area is squeezed from anterior and posterior (which I believe results in the Concave-like surface).</p>
<p>I wonder if there is any underlying parameter affecting the surface, or if the algorithm itself produces this type of surface?</p>

---

## Post #13 by @lassoan (2024-04-13 15:42 UTC)

<p>This output looks very good. The smoothness is intentional (you don’t want linear interpolation, as it would result in discontinuity in surface normal directions).</p>
<p>The cross-section is slightly oval because of the distance map is computed without taking spacing into account. Normally this is not visible because segmented slices are at a reasonable distance, while in your case it is extreme (it is almost impossible that an interpolation algorithm would correctly guess a 3D shape from such extremely sparse data) and you interpolate on axial slices and the spacing is uniform within a slice (but MRHead is an unusual image where the image spacing is slightly larger along the LR axis).</p>
<p>I would recommend to add contours more closer to each other and consider resampling your image to isotropic spacing (which is useful for 3D segmentation anyway).</p>
<p>While in practice ignoring the image spacing for the distance transform should not be a problem, you can still request a fix <a href="https://github.com/KitwareMedical/ITKMorphologicalContourInterpolation/issues">here</a> and see what the developers say.</p>

---
