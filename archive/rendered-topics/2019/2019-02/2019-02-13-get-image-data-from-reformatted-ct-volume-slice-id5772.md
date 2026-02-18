# Get image data from reformatted CT volume slice

**Topic ID**: 5772
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/get-image-data-from-reformatted-ct-volume-slice/5772

---

## Post #1 by @DAVID_GARCIA_MATO (2019-02-13 23:45 UTC)

<p>Hello,</p>
<p>I need to get image data (meaning pixel/voxel values) from a reformatted CT volume slice.</p>
<p>I have developed a simple scripted module to load a CT volume and used the “Reformat” module in Slicer to reformat a CT slice to contain 3 predefined fiducials. Now, I would like to obtain the image data from that reformatted slice, meaning pixel/voxel values.</p>
<p>Is there a simple way to get that information?</p>
<p>I would really appreciate your help,</p>
<p>Thank you very much in advance,</p>
<p>Best,</p>
<p>David</p>

---

## Post #2 by @muratmaga (2019-02-14 07:04 UTC)

<p>arrayFromVolume is what you need I think. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume</a></p>
<p>in the example below, a is the integer array of pixel values for the MRHead.</p>
<p>import SampleData</p>
<p>sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadMRHead()<br>
a = arrayFromVolume(masterVolumeNode )</p>

---

## Post #3 by @DAVID_GARCIA_MATO (2019-02-18 16:37 UTC)

<p>Hi,</p>
<p>I have just tried that, but “arrayFromVolume” method gives me the whole volume (3D matrix). How can I get just the pixel values of my reformatted slice?</p>
<p>Thanks!</p>
<p>David</p>

---

## Post #4 by @cpinter (2019-02-18 17:53 UTC)

<p>What comes to mind are the transforms that take you from RAS to slice view XY or back, see these functions for example<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L340-L366" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L340-L366" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L340-L366</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="340" style="counter-reset: li-counter 339 ;">
<li>/// Convert RAS position to XY in-slice position</li>
<li>static QPoint rasToXy(double ras[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert RAS position to XY in-slice position, python accessor method</li>
<li>Q_INVOKABLE static QPoint rasToXy(QVector3D ras, qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XYZ slice view position to RAS position:</li>
<li>/// x,y uses slice (canvas) coordinate system and actually has a 3rd z component (index into the</li>
<li>/// slice you're looking at), hence xyToRAS is really performing xyzToRAS. RAS is patient world</li>
<li>/// coordinate system. Note the 1 is because the transform uses homogeneous coordinates.</li>
<li>static void xyzToRas(double inputXyz[3], double outputRas[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XYZ slice view position to RAS position, python accessor method</li>
<li>Q_INVOKABLE static QVector3D xyzToRas(QVector3D inputXyz, qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XY in-slice position to RAS position</li>
<li>static void xyToRas(QPoint xy, double outputRas[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XY in-slice position to RAS position</li>
<li>static void xyToRas(double xy[2], double outputRas[3], qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XY in-slice position to RAS position, python accessor method</li>
<li>Q_INVOKABLE static QVector3D xyToRas(QPoint xy, qMRMLSliceWidget* sliceWidget);</li>
<li>/// Convert XYZ slice view position to image IJK position, \sa xyzToRas</li>
<li>static void xyzToIjk(double inputXyz[3], int outputIjk[3], qMRMLSliceWidget* sliceWidget, vtkOrientedImageData* image);</li>
<li>/// Convert XYZ slice view position to image IJK position, python accessor method, \sa xyzToRas</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/qSlicerSegmentEditorAbstractEffect.h#L340-L366" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>This example might also be useful from the Threshold effect that takes the image from a slice view:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L382-L405" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L382-L405" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L382-L405</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="382" style="counter-reset: li-counter 381 ;">
<li>def setupPreviewDisplay(self):</li>
<li>  # Clear previous pipelines before setting up the new ones</li>
<li>  self.clearPreviewDisplay()</li>
<li>
</li>
<li>  layoutManager = slicer.app.layoutManager()</li>
<li>  if layoutManager is None:</li>
<li>    return</li>
<li>
</li>
<li>  # Add a pipeline for each 2D slice view</li>
<li>  for sliceViewName in layoutManager.sliceViewNames():</li>
<li>    sliceWidget = layoutManager.sliceWidget(sliceViewName)</li>
<li>    if not self.scriptedEffect.segmentationDisplayableInView(sliceWidget.mrmlSliceNode()):</li>
<li>      continue</li>
<li>    renderer = self.scriptedEffect.renderer(sliceWidget)</li>
<li>    if renderer is None:</li>
<li>      logging.error("setupPreviewDisplay: Failed to get renderer!")</li>
<li>      continue</li>
<li>
</li>
<li>    # Create pipeline</li>
<li>    pipeline = PreviewPipeline()</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L382-L405" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I’m not sure if there is anything specific to using the Reformat module that these ideas don’t take into account, but I hope this helps!</p>

---

## Post #5 by @DAVID_GARCIA_MATO (2019-02-18 18:19 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>!! I think that’s what I needed!</p>
<p>David</p>

---

## Post #6 by @lassoan (2019-02-20 14:08 UTC)

<p>There is also a short example showing how to get resliced image as a volume node and access it as a numpy array:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_reformatted_image_from_a_slice_viewer_as_numpy_array</a></p>

---

## Post #7 by @DAVID_GARCIA_MATO (2019-02-21 01:40 UTC)

<p>Quite useful! Thank you Andras!</p>

---
