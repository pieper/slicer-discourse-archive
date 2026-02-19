---
topic_id: 1933
title: "Turn Off All Smoothing In Segmentation"
date: 2018-01-25
url: https://discourse.slicer.org/t/1933
---

# Turn off all smoothing in segmentation

**Topic ID**: 1933
**Date**: 2018-01-25
**URL**: https://discourse.slicer.org/t/turn-off-all-smoothing-in-segmentation/1933

---

## Post #1 by @leomigfer (2018-01-25 17:24 UTC)

<p>O.S. Win 10 - 64bit<br>
Version: 4.8.1</p>
<p>Hi there,</p>
<p>We are willing to apply this software to segment the thalamus and need to correct segmentation errors on a pixel-by-pixel basis. For this reason, we need to abolish any possible type of smoothing on the source image. Is that by any means possible?</p>
<p>With very best wishes and many thanks in advance,</p>
<p>Leonardo</p>

---

## Post #2 by @cpinter (2018-01-25 18:08 UTC)

<p>No smoothing is done on the segmentation (the edited labelmap, which is the master representation) without user intervention. The 3D model is smoothed, but it is only extra visualization. You can turn off model smoothing using the Set surface smoothing option under the arrow next to the Show 3D button in Segment Editor.</p>

---

## Post #3 by @pieper (2018-01-25 18:50 UTC)

<p>Also for the background image you can turn off interpolation to see the original voxel values (interpolation button shown here <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Slice_Viewers">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/MainApplicationGUI#Slice_Viewers</a>)</p>

---

## Post #4 by @lassoan (2018-01-25 19:03 UTC)

<aside class="quote no-group" data-username="leomigfer" data-post="1" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/35a633/48.png" class="avatar"> leomigfer:</div>
<blockquote>
<p>segment the thalamus and need to correct segmentation errors on a pixel-by-pixel basis</p>
</blockquote>
</aside>
<p>In general, if it makes significant difference if a single voxel is inside/outside of a segment then it indicates that the data processing workflow is not optimal for segmentation. Most processing and visualization algorithms assume that the image resolution is much finer than size of details in the structures of interest - if you violate this assumption then you’ll get suboptimal results. Increasing image acquisition resolution is often not feasible, but it is not a problem: you can still resample your input volume (preferably to cubic voxel size) before you segment it to avoid problems associated with insufficient image resolution.</p>
<p>You can use <code>Crop volume</code> module to resample with smaller, cubic voxels (<code>Isotropic spacing</code> enabled, <code>Spacing scale</code> set to &lt; 1, <code>Interpolator</code> set to <code>B-spline</code>) and crop to the region of interest (to make sure the output image will not get too big due to the smaller voxel size).</p>

---

## Post #5 by @gcsharp (2018-01-25 18:12 UTC)

<p>Probably you are referring to the interpolation in slice view that is enabled by default.</p>
<p>In the volumes module, in the display tab, there is a check button “Interpolate” which you can deactivate.</p>

---

## Post #6 by @leomigfer (2018-02-01 13:15 UTC)

<p>Thank you for advice!</p>

---

## Post #7 by @Leon (2019-08-01 11:32 UTC)

<p>About this 3D surface smoothing; I know that when you export your 3D surface smoothed segment as a STL, the viewport smoothing is also applied on the final exported STL.<br>
But what method is used for this smoothing? Which algorithm and settings do I have to use to perform the same smoothing on for instance a labelmap?<br>
In other words; can exactly the same procedure be done afterwards and how?</p>
<p>Or is that a well kept secret? <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>
<p>I’m asking this because I’m trying to mimic a smoothing method that’s used by the applications ‘Mimics’ and ‘3D-Matic’ (both products of Materialise). It’s proprietary software, so they won’t let you how they do their thing. <img src="https://emoji.discourse-cdn.com/twitter/zipper_mouth_face.png?v=9" title=":zipper_mouth_face:" class="emoji" alt=":zipper_mouth_face:"></p>

---

## Post #8 by @cpinter (2019-08-01 14:00 UTC)

<p>Smoothing is not actually applied when exporting. Whatever you have as closed surface representation, that is what is exported. If you disable smoothing when editing, then it won’t be smoothed.</p>
<p>Nothing is a secret in Slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Flying edges is used for smoothing. See usage here<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L181" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L181" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L181</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="171" style="counter-reset: li-counter 170 ;">
<li>
</li>
<li>
</li>
<li>  // Run marching cubes</li>
<li>
</li>
<li>#if VTK_MAJOR_VERSION &gt;= 9 || (VTK_MAJOR_VERSION &gt;= 8 &amp;&amp; VTK_MINOR_VERSION &gt;= 2)</li>
<li>  // Normals computation in vtkDiscreteFlyingEdges3D is faster than computing normals in a subsequent</li>
<li>  // vtkPolyDataNormals filter. However, if smoothing step is applied after vtkDiscreteFlyingEdges3D then</li>
<li>  // computing normals after smoothing provides smoother surfaces.</li>
<li>  bool marchingCubesComputesSurfaceNormals = (computeSurfaceNormals &gt; 0) &amp;&amp; (smoothingFactor &lt;= 0);</li>
<li>
</li>
<li class="selected">  vtkSmartPointer&lt;vtkDiscreteFlyingEdges3D&gt; marchingCubes = vtkSmartPointer&lt;vtkDiscreteFlyingEdges3D&gt;::New();</li>
<li>#else</li>
<li>  bool marchingCubesComputesSurfaceNormals = false;</li>
<li>  vtkSmartPointer&lt;vtkDiscreteMarchingCubes&gt; marchingCubes = vtkSmartPointer&lt;vtkDiscreteMarchingCubes&gt;::New();</li>
<li>#endif</li>
<li>  marchingCubes-&gt;SetInputData(binaryLabelmapWithIdentityGeometry);</li>
<li>  const int labelmapFillValue = binaryLabelmapWithIdentityGeometry-&gt;GetScalarRange()[1]; // max value</li>
<li>  marchingCubes-&gt;GenerateValues(1, labelmapFillValue, labelmapFillValue);</li>
<li>  marchingCubes-&gt;ComputeGradientsOff();</li>
<li>  marchingCubes-&gt;SetComputeNormals(marchingCubesComputesSurfaceNormals);</li>
<li>  marchingCubes-&gt;ComputeScalarsOff();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
and the method here<br>
<a href="https://vtk.org/doc/nightly/html/classvtkDiscreteFlyingEdges3D.html" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkDiscreteFlyingEdges3D.html</a> (scroll down for the description)</p>

---

## Post #9 by @lassoan (2019-08-01 14:49 UTC)

<p>Most of the smoothing is provided vtkWindowedSincPolyDataFilter applied on the flying edges output:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L217" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L217" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L217</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="207" style="counter-reset: li-counter 206 ;">
<li>  decimator-&gt;SplittingOff();</li>
<li>  decimator-&gt;PreserveTopologyOn();</li>
<li>  decimator-&gt;SetMaximumError(1);</li>
<li>  decimator-&gt;SetTargetReduction(decimationFactor);</li>
<li>  decimator-&gt;Update();</li>
<li>  processingResult = decimator-&gt;GetOutput();</li>
<li>  }</li>
<li>
</li>
<li>if (smoothingFactor &gt; 0)</li>
<li>  {</li>
<li class="selected">  vtkSmartPointer&lt;vtkWindowedSincPolyDataFilter&gt; smoother = vtkSmartPointer&lt;vtkWindowedSincPolyDataFilter&gt;::New();</li>
<li>  smoother-&gt;SetInputData(processingResult);</li>
<li>  smoother-&gt;SetNumberOfIterations(20); // based on VTK documentation ("Ten or twenty iterations is all the is usually necessary")</li>
<li>  // This formula maps:</li>
<li>  // 0.0  -&gt; 1.0   (almost no smoothing)</li>
<li>  // 0.25 -&gt; 0.1   (average smoothing)</li>
<li>  // 0.5  -&gt; 0.01  (more smoothing)</li>
<li>  // 1.0  -&gt; 0.001 (very strong smoothing)</li>
<li>  double passBand = pow(10.0, -4.0*smoothingFactor);</li>
<li>  smoother-&gt;SetPassBand(passBand);</li>
<li>  smoother-&gt;BoundarySmoothingOff();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Xiaojie_Guo (2023-08-07 06:42 UTC)

<p>May I change the smoothing method for the closed surface?</p>

---

## Post #11 by @lassoan (2023-08-07 08:05 UTC)

<p>Yes! This is an underutilized feature in the segmentation infrastructure: you can specify any number of alternative conversion rule(s) that can get from a binary labelmap to a closed surface representation. The conversion path with the smallest cost is used by default, but to can choose alternative path when you click on Update in the representation list in Segmentations module.</p>
<p>What algorithm do you have in mind?</p>

---

## Post #12 by @Xiaojie_Guo (2023-08-07 08:23 UTC)

<p>Is it the method you said? It seems some parameters can be changed, but the method can’t be changed to another smoothing one. Actually, I just want to see the segmentation result without any postprocessing like the example from <a href="https://examples.vtk.org/site/Python/Medical/GenerateCubesFromLabels/" rel="noopener nofollow ugc">VTK</a>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19c02c0178c5307696042089e4da4b5876e6a832.png" data-download-href="/uploads/short-url/3FNF79QCE0tD5Hnlhuoq2v57tgC.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19c02c0178c5307696042089e4da4b5876e6a832.png" alt="图片" data-base62-sha1="3FNF79QCE0tD5Hnlhuoq2v57tgC" width="529" height="500" data-dominant-color="EFF3F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">762×720 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @cpinter (2023-08-07 14:05 UTC)

<p>You can turn off smoothing very easily in Segment Editor, see <code>Show 3D</code> option in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options">documentation</a>.</p>
<p>For existing segmentations you just change the smoothing factor to 0 (see second parameter in the red box in your screenshot).</p>

---

## Post #14 by @ruili (2023-11-22 16:11 UTC)

<p>Hello! Do you know if there is a way to change the default setting so that it always sets the smoothing factor to 0?</p>

---

## Post #15 by @lassoan (2023-11-22 18:10 UTC)

<p>Smoothing step is part of the reconstruction. It is not some optional postprocessing step that you may or may not want to have. If you don’t apply smoothing then you will get a surface corrupted with aliasing artifacts (staircases), which are not there in the continuous signal. Therefore, <strong>you should not disable smoothing by default</strong>.</p>
<p>Of course, you can do everything in Slicer. So, if you decide that you always want to have artifacts in the reconstructed surface then you can change the default by adding these lines to your <code>.slicerrc.py</code> file:</p>
<pre data-code-wrap="python"><code class="lang-python"># Note: running this code is not recommended, as it introduces artifacts in the reconstructed surface
defaultSegmentationNode = slicer.vtkMRMLSegmentationNode()
defaultSegmentationNode.GetSegmentation().SetConversionParameter("Smoothing factor", "-0.5")  # use negative number to make it easy to enable smoothing
slicer.mrmlScene.AddDefaultNode(defaultSegmentationNode)
</code></pre>

---

## Post #17 by @rbumm (2023-11-23 01:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In general, if it makes significant difference if a single voxel is inside/outside of a segment then it indicates that the data processing workflow is not optimal for segmentation. Most processing and visualization algorithms assume that the image resolution is much finer than size of details in the structures of interest - if you violate this assumption then you’ll get suboptimal results. Increasing image acquisition resolution is often not feasible, but it is not a problem: you can still resample your input volume (preferably to cubic voxel size) before you segment it to avoid problems associated with insufficient image resolution.</p>
<p>You can use <code>Crop volume</code> module to resample with smaller, cubic voxels (<code>Isotropic spacing</code> enabled, <code>Spacing scale</code> set to &lt; 1, <code>Interpolator</code> set to <code>B-spline</code>) and crop to the region of interest (to make sure the output image will not get too big due to the smaller voxel size).</p>
</blockquote>
</aside>
<p>This is wise and useful information that should be prominently placed somewhere.</p>

---

## Post #18 by @chir.set (2023-11-23 11:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you don’t apply smoothing then you will get a surface corrupted with aliasing artifacts (staircases),</p>
</blockquote>
</aside>
<p>This is still a confusing topic. Please consider the 2 images below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba989a999efdb95478c90b5590767080c0dd32c2.png" data-download-href="/uploads/short-url/qCHLeBS5Skg0Wea9H4ISmaUn3jk.png?dl=1" title="Smooth_0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba989a999efdb95478c90b5590767080c0dd32c2_2_690x322.png" alt="Smooth_0" data-base62-sha1="qCHLeBS5Skg0Wea9H4ISmaUn3jk" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba989a999efdb95478c90b5590767080c0dd32c2_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba989a999efdb95478c90b5590767080c0dd32c2_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba989a999efdb95478c90b5590767080c0dd32c2_2_1380x644.png 2x" data-dominant-color="302E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Smooth_0</span><span class="informations">1386×647 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19db31189f9b1e38104c300e4d47bf3d8ee9cccc.png" data-download-href="/uploads/short-url/3GJyhGAjZBrmnQD33Zda8kOr4Nm.png?dl=1" title="Smooth_50" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19db31189f9b1e38104c300e4d47bf3d8ee9cccc_2_690x322.png" alt="Smooth_50" data-base62-sha1="3GJyhGAjZBrmnQD33Zda8kOr4Nm" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19db31189f9b1e38104c300e4d47bf3d8ee9cccc_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19db31189f9b1e38104c300e4d47bf3d8ee9cccc_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19db31189f9b1e38104c300e4d47bf3d8ee9cccc_2_1380x644.png 2x" data-dominant-color="302E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Smooth_50</span><span class="informations">1386×647 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the first one, there is no surface smoothing in 3D. In the second image, surface smoothing is at default 0.5.</p>
<p>We see that the contrasted structure is better filled without surface smoothing in the the 3D view. The slice view outlines the contrast as reference.</p>
<p>Should we consider that surface smoothing should be applied in 2D views to remove what is considered as artifacts? But the contrast pleads against this.</p>

---

## Post #19 by @ruili (2023-11-23 11:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">defaultSegmentationNode = slicer.vtkMRMLSegmentationNode()
defaultSegmentationNode.GetSegmentation().SetConversionParameter("Smoothing factor", "-0.5")  # use negative number to make it easy to enable smoothing
slicer.mrmlScene.AddDefaultNode(defaultSegmentationNode)
</code></pre>
</blockquote>
</aside>
<p>Yes it is indeed due to scenarios like this one that I did not want to have any smoothing. I tried the code suggested:</p>
<pre><code class="lang-auto">defaultSegmentationNode = slicer.vtkMRMLSegmentationNode()
defaultSegmentationNode.GetSegmentation().SetConversionParameter("Smoothing factor", "-0.5")  # use negative number to make it easy to enable smoothing
slicer.mrmlScene.AddDefaultNode(defaultSegmentationNode)
</code></pre>
<p>However, it did not work as I hoped. I want to make it so that whenever I load a segmentation and click “Show 3D” the visualisation has a smoothing factor of 0. However, after adding this code to .slicerrc.py, the default smoothing factor is still 0.5. I really want to change this default setting as in my workflow I have to load many segmentation files, and each time I have the change the smoothing factor manually.</p>

---

## Post #20 by @chir.set (2023-11-23 11:46 UTC)

<aside class="quote no-group" data-username="ruili" data-post="19" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>after adding this code to .slicerrc.py</p>
</blockquote>
</aside>
<p>Did you restart Slicer after updating .slicerrc.py?</p>

---

## Post #21 by @ruili (2023-11-23 11:48 UTC)

<p>Yes I did. I also tried running those codes in the python console inside slicer to ensure that they were applied, but neither worked.</p>

---

## Post #22 by @chir.set (2023-11-23 11:55 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="18" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>But the contrast pleads against this.</p>
</blockquote>
</aside>
<p>I’m wondering if the smoothing algorithm can dilate (red) rather than shrink (blue).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4346cec346c6f731d6b43166fe564fdc38f7ed44.png" data-download-href="/uploads/short-url/9B9H6wUKnpR6Pk3kyVbpFM42rAM.png?dl=1" title="Smooth_50_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346cec346c6f731d6b43166fe564fdc38f7ed44_2_690x322.png" alt="Smooth_50_1" data-base62-sha1="9B9H6wUKnpR6Pk3kyVbpFM42rAM" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346cec346c6f731d6b43166fe564fdc38f7ed44_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346cec346c6f731d6b43166fe564fdc38f7ed44_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/4346cec346c6f731d6b43166fe564fdc38f7ed44_2_1380x644.png 2x" data-dominant-color="302E2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Smooth_50_1</span><span class="informations">1386×647 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @lassoan (2023-11-23 12:32 UTC)

<aside class="quote no-group" data-username="ruili" data-post="19" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>However, it did not work as I hoped. I want to make it so that whenever I load a segmentation and click “Show 3D” the visualisation has a smoothing factor of 0.</p>
</blockquote>
</aside>
<p>The code above does not affect any segmentations that you already created. You can change all the existing nodes as well (e.g., add a function that is called each time a node is added to the the scene and change the smoothing) but instead of solving the underlying problem you would just replace it with a different issue.</p>
<aside class="quote no-group" data-username="chir.set" data-post="22" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I’m wondering if the smoothing algorithm can dilate (red) rather than shrink (blue).</p>
</blockquote>
</aside>
<p>The windowed since smoothing filter performs low-pass filtering, so it does not dilate or shrink the surface. However, if the voxels are to large and not not cube-shaped (the resolution of thr image is too coarse and a isotropic) then the filter may fail to reproduce the original continuous surface.</p>
<p>If there is any significant change in the overall shape of the segments due to the 3D reconstruction (isosurface extraction + smoothing) then most likely the resolution of the segmentation is not sufficient to represent that fine level of detail.</p>
<p>To solve this, you can resample the segmentation to have finer resolution (and probaly you also want the resolution to be isotropic). You can also experiment with slightly decreasing the smoothing factor to see if you can preserve all the details while removing the surface artifacts. Finally, you may also try the new surface nets based surface reconstruction that is available in the latest Slicer Preview Releases.</p>

---

## Post #24 by @chir.set (2023-11-23 19:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can resample the segmentation to have finer resolution</p>
</blockquote>
</aside>
<p>This does the trick. Thank you very much for this insight.</p>
<p>I’ve resampled a cropped portion of ‘Panoramix-cropped’ to 0.3 x 0.3 x 0.3 mm spacing and segmented again. The default surface smoothing factor of 0.5 is quite consistent with the slice view outline as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92a48dfe851ea2d310b8a02644b459b5510b97c9.png" data-download-href="/uploads/short-url/kVggzZRiM9ilXrvb8JXVcvnuOZr.png?dl=1" title="Smooth_isovoxel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92a48dfe851ea2d310b8a02644b459b5510b97c9_2_690x256.png" alt="Smooth_isovoxel" data-base62-sha1="kVggzZRiM9ilXrvb8JXVcvnuOZr" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92a48dfe851ea2d310b8a02644b459b5510b97c9_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92a48dfe851ea2d310b8a02644b459b5510b97c9_2_1035x384.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92a48dfe851ea2d310b8a02644b459b5510b97c9.png 2x" data-dominant-color="222021"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Smooth_isovoxel</span><span class="informations">1246×463 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As for surface net, a visual change is observed in the form of a shrinking of the segment in the 3D view with the ‘Faster’ option only. The ‘Fast’ option didn’t seem to do anything. Are these two independent surface smoothing techniques? Or is the ‘Faster’ option the real one, requiring the ‘Fast’ option to be on?</p>
<p><a class="mention" href="/u/ruili">@ruili</a> I fear you should re-segment everything again <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #25 by @lassoan (2023-11-23 20:44 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="24" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>As for surface net, a visual change is observed in the form of a shrinking of the segment in the 3D view with the ‘Faster’ option only. The ‘Fast’ option didn’t seem to do anything. Are these two independent surface smoothing techniques? Or is the ‘Faster’ option the real one, requiring the ‘Fast’ option to be on?</p>
</blockquote>
</aside>
<p><code>Fast</code> option uses the same windowed sinc smoothing filter (same as with the default flying edges surface extraction method). <code>Faster</code> option uses a different algorithm that performs smoothing during surface extraction, which is faster but less accurate. You can ask for more details in the <a href="https://discourse.slicer.org/t/new-surface-model-generation-method-surfacenets/32430">topic where the feature was announced</a>.</p>
<aside class="quote no-group" data-username="chir.set" data-post="24" data-topic="1933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I fear you should re-segment everything again</p>
</blockquote>
</aside>
<p>It might not be necessary to redo the complete segmentation. You can change the segmentation geometry and apply slight smoothing (e.g., using joint smoothing) and see if the result is satisfactory. It may not be optimal because some details may be lost that could have been present if the segmentation were performed at finer resolution from the beginning.</p>

---
