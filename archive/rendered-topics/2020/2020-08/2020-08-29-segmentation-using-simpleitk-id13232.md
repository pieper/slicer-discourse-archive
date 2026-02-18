# Segmentation Using SimpleITK

**Topic ID**: 13232
**Date**: 2020-08-29
**URL**: https://discourse.slicer.org/t/segmentation-using-simpleitk/13232

---

## Post #1 by @Fereshte_J (2020-08-29 14:12 UTC)

<p>Hello, I wanted to know whether it is possible to create a mask for an image using simpleitk and use that mask to show the segmented region in slicer jupyter kernel.<br>
thank you.</p>

---

## Post #2 by @lassoan (2020-08-29 14:21 UTC)

<p>This easily doable in two steps:</p>
<ul>
<li>push/pull volume node to/from SimpleITK using sitkUtils (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK">example</a>)</li>
<li>convert the volume node to/from segmentation node (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D">example</a>)</li>
</ul>
<p>There are several Segment Editor effects that use SimpleITK, which can serve as a complete example (that even show how to implement interactive segmentation tools, which require some user input):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L106-L133" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L106-L133" target="_blank" rel="noopener">lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L106-L133</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="106" style="counter-reset: li-counter 105 ;">
<li>
</li>
<li># Run segmentation algorithm
</li>
<li>import SimpleITK as sitk
</li>
<li>import sitkUtils
</li>
<li># Read input data from Slicer into SimpleITK
</li>
<li>labelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))
</li>
<li>backgroundImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(masterVolumeNode.GetName()))
</li>
<li># Run watershed filter
</li>
<li>featureImage = sitk.GradientMagnitudeRecursiveGaussian(backgroundImage, float(self.scriptedEffect.doubleParameter("ObjectScaleMm")))
</li>
<li>del backgroundImage
</li>
<li>f = sitk.MorphologicalWatershedFromMarkersImageFilter()
</li>
<li>f.SetMarkWatershedLine(False)
</li>
<li>f.SetFullyConnected(False)
</li>
<li>labelImage = f.Execute(featureImage, labelImage)
</li>
<li>del featureImage
</li>
<li># Pixel type of watershed output is the same as the input. Convert it to int16 now.
</li>
<li>if labelImage.GetPixelID() != sitk.sitkInt16:
</li>
<li>  labelImage = sitk.Cast(labelImage, sitk.sitkInt16)
</li>
<li># Write result from SimpleITK to Slicer. This currently performs a deep copy of the bulk data.
</li>
<li>sitk.WriteImage(labelImage, sitkUtils.GetSlicerITKReadWriteAddress(mergedLabelmapNode.GetName()))
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py#L106-L133" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Fereshte_J (2020-08-31 05:12 UTC)

<p>Thank you for your reply. However, I have another problem. I am using a UNET neural network to segment a series of CT images and save the segmented image as a different file. When I use matplotlib to show the segmented image, the regions of interest are clearly visible with a distinct color, however when I import the image into the slicer and display it is nothing like the segmented one. I have attached the plots from matplotlib and slicer. Can you help me to be able to display the segmented image in the slicer, too?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/701450d1e4976012e84849c4f195eea63aff4a11.jpeg" data-download-href="/uploads/short-url/fZv0b50t7spAlQw895JJHy790wF.jpeg?dl=1" title="matplotlib" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/701450d1e4976012e84849c4f195eea63aff4a11_2_550x500.jpeg" alt="matplotlib" data-base62-sha1="fZv0b50t7spAlQw895JJHy790wF" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/701450d1e4976012e84849c4f195eea63aff4a11_2_550x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/701450d1e4976012e84849c4f195eea63aff4a11.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/701450d1e4976012e84849c4f195eea63aff4a11.jpeg 2x" data-dominant-color="7A7D7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">matplotlib</span><span class="informations">593×539 18.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a2238a60e57170cf2e65aff0383ec9eef3fb29c.jpeg" alt="slicer" data-base62-sha1="jHZd01F75Gb8NfSD0VvhONrvgnO" width="337" height="440"></p>

---

## Post #4 by @lassoan (2020-09-01 02:58 UTC)

<aside class="quote no-group" data-username="Fereshte_J" data-post="3" data-topic="13232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fereshte_j/48/7898_2.png" class="avatar"> Fereshte_J:</div>
<blockquote>
<p>segment a series of CT images and save the segmented image as a different file</p>
</blockquote>
</aside>
<p>Can you send this saved image (upload somewhere and post the link)?</p>
<aside class="quote no-group" data-username="Fereshte_J" data-post="3" data-topic="13232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fereshte_j/48/7898_2.png" class="avatar"> Fereshte_J:</div>
<blockquote>
<p>when I import the image into the slicer and display it is nothing like the segmented one</p>
</blockquote>
</aside>
<p>How do you do this exactly?</p>

---
