# How to obtain the complete center lines using VMTK?

**Topic ID**: 14068
**Date**: 2020-10-16
**URL**: https://discourse.slicer.org/t/how-to-obtain-the-complete-center-lines-using-vmtk/14068

---

## Post #1 by @KaryLiang (2020-10-16 03:57 UTC)

<p>Hello,</p>
<p>I’m trying to obtain center lines from airway using VMTK. After dilating the pixels of airway, i got most of the center line, including from the small airway, looks like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d3486438fd3115b01ddf054b8466c16fbd4f97b.png" alt="image" data-base62-sha1="b0ZiuY6AU38vKCZ85k3JmEw88Yj" width="455" height="500"></p>
<p>my problem is, why the center lines are broken in the middle? and what would be the best way to get a complete center lines?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3556d2cedc7e2697ed714f35ebc815072b0c0a0.png" alt="image" data-base62-sha1="u9xLQ81SjYdEkbHV5EnS28reyuk" width="468" height="500"></p>
<p>A similar problem seems to be happened here, the extract lines are not joined:<br>
[<a href="https://github.com/vmtk/vmtk/issues/355" class="inline-onebox" rel="noopener nofollow ugc">Problem about multiple source/target points for vtkvmtkPolyDataCenterlines · Issue #355 · vmtk/vmtk · GitHub</a>]</p>
<p>Please help or try to give some ideas how to achieve this. Thanks in advance.</p>

---

## Post #2 by @lassoan (2020-10-16 17:23 UTC)

<p>It seems to be specific to your data set. Could you post the original segmentation (but at least the input mesh) so that we can reproduce this?</p>

---

## Post #3 by @KaryLiang (2020-10-19 08:26 UTC)

<p>Thanks for your reply!</p>
<p>This is <a href="https://github.com/KaryLiang/AirwayTestData" rel="noopener nofollow ugc">the original segmenataion and script</a>.</p>

---

## Post #4 by @lassoan (2020-10-20 03:26 UTC)

<p>Summary: I’ve tested your data set and everything worked well if I made branches a bit thicker. VMTK’s centerline extraction cannot seem to be able to track down endpoints though narrow, pointy tips.</p>
<p>Details:</p>
<p>I’ve imported the mask into a segmentation node Slicer and ran it through VMTK extension’s Extract centerline module:</p>
<pre data-code-wrap="python"><code class="lang-python"># Load mask into labelmap volume
import numpy as np
d = np.load(r'c:\Users\andra\OneDrive\Projects\SlicerTesting5\20201019-AirwayNetworkAnalysis\PA000019.npz', allow_pickle=True)
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.util.updateVolumeFromArray(volumeNode, d['isoMask'])

# Convert labelmap volume to segmentation node
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode(volumeNode, segmentationNode)
segmentationNode.CreateClosedSurfaceRepresentation()
</code></pre>
<p>Automatic endpoint detection worked well:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daec62c6077c4a85c5c72e5a14a3f84f8b6cd6d8.jpeg" data-download-href="/uploads/short-url/veGxENzxbSFh3ggRKwPjBOZCY3e.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daec62c6077c4a85c5c72e5a14a3f84f8b6cd6d8_2_690x421.jpeg" alt="image" data-base62-sha1="veGxENzxbSFh3ggRKwPjBOZCY3e" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daec62c6077c4a85c5c72e5a14a3f84f8b6cd6d8_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daec62c6077c4a85c5c72e5a14a3f84f8b6cd6d8_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daec62c6077c4a85c5c72e5a14a3f84f8b6cd6d8_2_1380x842.jpeg 2x" data-dominant-color="696B81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1376 394 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Centerline detection did not succeed - path was not found to endpoints that were connected to the bronchial tree with a narrow branch/sharp tip:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51f118d7a898d3459b3865bcc799110d77b5853b.png" data-download-href="/uploads/short-url/bGTdPJ1kZL8oRBcdH3XdCoMtpMv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51f118d7a898d3459b3865bcc799110d77b5853b_2_690x420.png" alt="image" data-base62-sha1="bGTdPJ1kZL8oRBcdH3XdCoMtpMv" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51f118d7a898d3459b3865bcc799110d77b5853b_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51f118d7a898d3459b3865bcc799110d77b5853b_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51f118d7a898d3459b3865bcc799110d77b5853b_2_1380x840.png 2x" data-dominant-color="686C81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1375 487 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve fixed the narrow branches by oversampling the image by a factor of 2x (subdivide every voxel by 2x2x2) and applying Margin effect in Segment editor:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cd823e7091dbab151455d03976b96ef0cb85a39.png" data-download-href="/uploads/short-url/1PCO5SSHJ6fOiUzsvNBfBOeSr4B.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0cd823e7091dbab151455d03976b96ef0cb85a39_2_690x429.png" alt="image" data-base62-sha1="1PCO5SSHJ6fOiUzsvNBfBOeSr4B" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0cd823e7091dbab151455d03976b96ef0cb85a39_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0cd823e7091dbab151455d03976b96ef0cb85a39_2_1035x643.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0cd823e7091dbab151455d03976b96ef0cb85a39_2_1380x858.png 2x" data-dominant-color="565868"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1404 402 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b55b2742cccc4268bb6e8ba81f7a295e8e45e47b.png" data-download-href="/uploads/short-url/pSlItq2j2iIHxqTlC4uVcJRs2Sf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55b2742cccc4268bb6e8ba81f7a295e8e45e47b_2_690x419.png" alt="image" data-base62-sha1="pSlItq2j2iIHxqTlC4uVcJRs2Sf" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55b2742cccc4268bb6e8ba81f7a295e8e45e47b_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55b2742cccc4268bb6e8ba81f7a295e8e45e47b_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55b2742cccc4268bb6e8ba81f7a295e8e45e47b_2_1380x838.png 2x" data-dominant-color="676B80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 560 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this, centerline extraction worked flawlessly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3893e6198629048484eab72e5fcf9c3618416471.png" data-download-href="/uploads/short-url/84vBPiNSIjRwpPgcxwd6Cw7afDz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3893e6198629048484eab72e5fcf9c3618416471_2_690x419.png" alt="image" data-base62-sha1="84vBPiNSIjRwpPgcxwd6Cw7afDz" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3893e6198629048484eab72e5fcf9c3618416471_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3893e6198629048484eab72e5fcf9c3618416471_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3893e6198629048484eab72e5fcf9c3618416471_2_1380x838.png 2x" data-dominant-color="686B81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1372 558 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Original mask (in interactive web viewer):</p>
<iframe width="480" height="373" frameborder="0" marginheight="0" marginwidth="0" src="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/hbal6lgttrx6ekq/Original.zip">
</iframe>
<p>Dilated mask (in interactive web viewer):</p>
<iframe width="480" height="373" frameborder="0" marginheight="0" marginwidth="0" src="https://kitware.github.io/vtk-js/examples/OBJViewer/OBJViewer.html?fileURL=https://dl.dropboxusercontent.com/s/yo5v2usrogv2eu1/Dilated.zip">
</iframe>

---

## Post #5 by @perecanals (2021-04-26 16:41 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>. I had a similar problem when extracting centerlines from vascular bodies and, while I was able to solve the centerline extraction by growing the margins of the original segmentation, I would like to use the associated radius information, but of course it is now relative to the extruded model. Is there a quick way to recompute the radius associated to each centerline point relative to the original segmentation after extracting the centerline using the Grow margins trick?</p>
<p>Thank you,</p>

---

## Post #6 by @lassoan (2021-04-26 16:57 UTC)

<p>To represent vessels robustly (without thin vessels breaking up), segmentation voxel size has to be at least 3-5x smaller than the diameter of thinnest vessel of interest. If you are not interested in quantifying the vessel diameter then you fulfill this requirement by dilating the vessel segment.</p>
<p>To quantify vessel diameter accurately, segmentation voxel size has to be 5-10x smaller than the diameter of the thinnest vessel of interest. In this case you probably don’t want to change the physical size of the vessel, as it would interfere with the quantification. Therefore, you need to oversample the input volume before the segmentation (this is a bit simpler) or oversample the segmentation (this may be useful in special cases, but a bit more complicated).See step-by-step instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---

## Post #7 by @perecanals (2021-04-29 12:32 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>! I was not aware of these indications for quantitative analysis of the vessel’s characteristics.</p>
<p>I have been experimenting with several configurations for the resampling of the binary labelmap (I can’t change the resolution of the source image since I am segmenting it using a trained neural net) and I have been able to find configurations that, along with a smoothing filter, work reasonably well (although visually I can’t reach the same quality of the original segmentation).</p>
<p>However, I still run into the same problem of same problem of straight “centerlines” traveling outside the model in some cases (I attach a picture below).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8a7f3fc83c0d17d2ed2aa0c29a93021a4a729c9.jpeg" data-download-href="/uploads/short-url/xcaBSslqWErbR1bVWlx5eZKxIN3.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a7f3fc83c0d17d2ed2aa0c29a93021a4a729c9_2_406x500.jpeg" alt="error" data-base62-sha1="xcaBSslqWErbR1bVWlx5eZKxIN3" width="406" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a7f3fc83c0d17d2ed2aa0c29a93021a4a729c9_2_406x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a7f3fc83c0d17d2ed2aa0c29a93021a4a729c9_2_609x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8a7f3fc83c0d17d2ed2aa0c29a93021a4a729c9_2_812x1000.jpeg 2x" data-dominant-color="9199C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1330×1636 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have tried to snap the endpoints to the closest Voronoi Diagram point as you mention in <a href="https://discourse.slicer.org/t/vessel-tree-centerline-branch-extraction-using-vmtk/11867/23">this issue</a>, but it does not seem to change anything. I attach the code I used for the modification of the endpoints:</p>
<pre><code># Instance Extract Centerline Widget
extractCenterlineWidget = slicer.modules.extractcenterline.widgetRepresentation().self()

# Set up parameter node
parameterNode = slicer.mrmlScene.GetSingletonNode("ExtractCenterline", "vtkMRMLScriptedModuleNode")
extractCenterlineWidget.setParameterNode(parameterNode)

# Set up widget
extractCenterlineWidget.setup()

# Update from GUI to get segmentationNode as inputSurfaceNode
extractCenterlineWidget.updateParameterNodeFromGUI()
# Set network node reference to new empty node
extractCenterlineWidget._parameterNode.SetNodeReferenceID("InputSurface", segmentationNode.GetID())

# Autodetect endpoints
extractCenterlineWidget.onAutoDetectEndPoints()

extractCenterlineWidget.updateGUIFromParameterNode()

# Create new Surface model node for the centerline model
voronoiDiagramNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
# Set centerline node reference to new empty node
extractCenterlineWidget._parameterNode.SetNodeReferenceID("VoronoiDiagram", voronoiDiagramNode.GetID())
extractCenterlineWidget.onApplyButton()

endpointsNode = slicer.util.getNode(extractCenterlineWidget._parameterNode.GetNodeReferenceID("EndPoints"))

voronoiDiagramPointsArray = np.ndarray([voronoiDiagramNode.GetPolyData().GetNumberOfPoints() // 10, 3])
for idx in range(voronoiDiagramNode.GetPolyData().GetNumberOfPoints() // 10):
    voronoiDiagramPointsArray[idx] = voronoiDiagramNode.GetPolyData().GetPoints().GetPoint(idx * 10)

endpointsVoronoiNormArray = np.ndarray([endpointsNode.GetNumberOfMarkups(), voronoiDiagramNode.GetPolyData().GetNumberOfPoints() // 10])

for idx in range(endpointsNode.GetNumberOfMarkups()):
    for idx2 in range(voronoiDiagramNode.GetPolyData().GetNumberOfPoints() // 10):
        endpointsVoronoiNormArray[idx][idx2] = np.linalg.norm(endpointsNode.GetCurvePoints().GetPoint(idx) - voronoiDiagramPointsArray[idx2])
    
endpointsArgVoronoiNormArray = np.argmin(endpointsVoronoiNormArray, axis=1)

for idx in range(endpointsNode.GetNumberOfMarkups()):
    endpointsNode.GetCurvePoints().SetPoint(idx, voronoiDiagramNode.GetPolyData().GetPoints().GetPoint(endpointsArgVoronoiNormArray[idx] * 10))

extractCenterlineWidget.updateGUIFromParameterNode()

# Set network node reference to new empty node
extractCenterlineWidget._parameterNode.SetNodeReferenceID("InputSurface", segmentationNode.GetID())
# extractCenterlineWidget._parameterNode.SetNodeReferenceID("InputSurface", segmentationNode.GetID())
# Create new Surface model node for the centerline model
centerlineModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
# Set centerline node reference to new empty node
extractCenterlineWidget._parameterNode.SetNodeReferenceID("CenterlineModel", centerlineModelNode.GetID())
extractCenterlineWidget.onApplyButton()
</code></pre>
<p>Note that I only check one in every 10 points from the Voronoi diagram to speed up the computation. Do you see why the code would not work? I can provide more context if necessary. This basically assumes that you have a volume which you have segmented (and stored the segmentation in the segmentationNode).</p>
<p>Thank you again for your help.</p>

---

## Post #8 by @lassoan (2021-04-30 02:45 UTC)

<aside class="quote no-group" data-username="perecanals" data-post="7" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>I have been experimenting with several configurations for the resampling of the binary labelmap (I can’t change the resolution of the source image since I am segmenting it using a trained neural net</p>
</blockquote>
</aside>
<p>You change the resolution of the image after you loaded it into 3D Slicer. For example, you can use Crop volume module with a spacing scaling of 0.3-0.6. Since Slicer performs all nodes in physical space (images, models, curves, etc.), resampling does not affect quantification results (other than a finer-resolution image can represent small details more accurately).</p>
<aside class="quote no-group" data-username="perecanals" data-post="7" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>However, I still run into the same problem of same problem of straight “centerlines” traveling outside the model in some cases (I attach a picture below).</p>
</blockquote>
</aside>
<p>Thanks, this is useful information. Maybe you need to move the points further inside the Voronoi model.</p>

---

## Post #9 by @perecanals (2021-05-03 15:00 UTC)

<p>Thank you for your response!</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example, you can use Crop volume module with a spacing scaling of 0.3-0.6</p>
</blockquote>
</aside>
<p>That is exactly what I do (with the binary map, since my segmentation process is external to 3D Slicer). I use nearest neighbours, isotropic spacing and a scaling of 0.5. The resulting segment has a very rough surface (the cubic voxel shape is everywhere all over the outside), but following what you say I understand that that does not matter for the correct quantification of centerline measurements (e.g. radius). Am I correct here? It would be useful to skip the smoothing process if necessary, I am not completely sure if what you are saying</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe you need to move the points further inside the Voronoi model.</p>
</blockquote>
</aside>
<p>I tried moving them twice the distance towards the direction of the closest Voronoi diagram point, but that still does not change the resulting centerline sometimes.</p>
<p>I have ended up making a small function to relocate the endpoints to a nearby position further inside the segmentation. It selects a small region (10 * 10 * 10 voxels or so, this could be tuned further) around the endpoint and moves the endpoint to the centroid of the closest segment inside this region (since it is a randomly selected region several segments could be included). So far it has been flawless for me, and I haven’t had to use the Margins tool.</p>

---

## Post #10 by @lassoan (2021-05-04 17:04 UTC)

<aside class="quote no-group" data-username="perecanals" data-post="9" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>That is exactly what I do (with the binary map, since my segmentation process is external to 3D Slicer). I use nearest neighbours, isotropic spacing and a scaling of 0.5.</p>
</blockquote>
</aside>
<p>What I meant is to crop&amp;resample the input image, before segmentation.</p>
<p>If you already have a binary labelmap then resampling it with nearest neighbor method will not make the surface any smoother. To interpolate a labelmap so that you get smoother surface, you may need to use an anti-alias filter on the input (such as Gaussian smoothing), interpolate using a higher-order kernel (bilinear, bspline, sinc, …) and threshold the result. You may also try the “Resample image (BRAINS)” module that has a special “binary” mode for labelmap interpolation.</p>
<aside class="quote no-group" data-username="perecanals" data-post="9" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>So far it has been flawless for me, and I haven’t had to use the Margins tool.</p>
</blockquote>
</aside>
<p>This information is already useful, but it would be even better if you could share the resulting code so that others don’t have to reimplement this if they run into similar issues.</p>

---

## Post #11 by @perecanals (2021-05-05 13:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This information is already useful, but it would be even better if you could share the resulting code so that others don’t have to reimplement this if they run into similar issues.</p>
</blockquote>
</aside>
<p>Here it is:</p>
<pre><code>def robustEndPointDetection(endpoint, segmentation, aff, n=5):
    ''' Relocates automatically detected endpoints to the center of mass of the closest component
    inside a local region around the endpoint (defined by n).

    Takes the endpoint position, converts it to voxel coordinates with the affine matrix, then defines a region  
    of (2 * n) ^ 3 voxels centered around the endpoint. Then components inside the local region are treated 
    as separate objects. The minimum distance from theese objects to the endpoint is computed, and from 
    these, the object with the smallest distance to the endpoint is chosen to compute the centroid, which
    is converted back to RAS with the affine matrix.

    Arguments:
        - endpoint &lt;np.array&gt;: position of the endpoint in RAS coordinates.
        - segmentation &lt;np.array&gt;: numpy array corresponding to the croppedVolumeNode.
        - aff &lt;np.array&gt;: affine matrix corresponding ot he nifti file.
        - n &lt;int&gt;: defines size of the region around the endpoint that is analyzed for this method.

    Returns:
        - newEndpoint &lt;np.array&gt;: new position of the endpoint.

    '''

    from skimage.measure import regionprops, label
    from scipy import ndimage

    # Compute RAS coordinates in voxel coordinates with affine matrix 
    R0, A0, S0 = np.round(np.matmul(np.linalg.inv(aff), np.append(endpoint, 1.0))[:3]).astype(int)

    # Mask the segmentation (Only region of interest)
    maskedSegmentation = segmentation[np.max([0, S0 - n]): np.min([segmentation.shape[0], S0 + n]), 
                                      np.max([0, A0 - n]): np.min([segmentation.shape[1], A0 + n]),
                                      np.max([0, R0 - n]): np.min([segmentation.shape[2], R0 + n])]

    # Divide into different connected components
    labelMask = label(maskedSegmentation)

    labels = np.sort(np.unique(labelMask))
    labels = np.delete(labels, np.where([labels == 0]))

    labelMaskOneHot = np.zeros([len(labels), labelMask.shape[0], labelMask.shape[1], labelMask.shape[2]], dtype=np.uint8)
    for idx, label in enumerate(labels):
        labelMaskOneHot[idx][labelMask == label] = 1

    invertedLabelMaskOneHot = np.ones_like(labelMaskOneHot) - labelMaskOneHot

    # Get distance transform for each and get only closest component
    distanceLabels = np.empty_like(labels, dtype = np.float)
    for idx in range(len(labels)):
        distanceLabels[idx] = ndimage.distance_transform_edt(invertedLabelMaskOneHot[idx])[invertedLabelMaskOneHot.shape[1] // 2][invertedLabelMaskOneHot.shape[2] // 2][invertedLabelMaskOneHot.shape[3] // 2]

    mask = np.zeros_like(segmentation)
    mask[np.max([0, S0 - n]): np.min([segmentation.shape[0], S0 + n]), 
         np.max([0, A0 - n]): np.min([segmentation.shape[1], A0 + n]),
         np.max([0, R0 - n]): np.min([segmentation.shape[2], R0 + n])] = labelMaskOneHot[np.argmin(distanceLabels)]

    # Get the centroid of the foregroud region
    properties = regionprops(mask.astype(np.int), mask.astype(np.int))
    centerOfMass = np.array(properties[0].centroid)[[2, 1, 0]]

    # Return the new position of the endpoint as RAS coordinates
    return np.matmul(aff, np.append(centerOfMass, 1.0))[:3]
</code></pre>
<p>In my case, I get the affine matrix using the nibabel package, directly from the NIfTI file itself:</p>
<pre><code>aff = nib.load("/path/to/nifti.nii.gz").affine
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you already have a binary labelmap then resampling it with nearest neighbor method will not make the surface any smoother. To interpolate a labelmap so that you get smoother surface, you may need to use an anti-alias filter on the input (such as Gaussian smoothing), interpolate using a higher-order kernel (bilinear, bspline, sinc, …) and threshold the result.</p>
</blockquote>
</aside>
<p>I initially tried this, but the smoothing filters were either too aggressive on the small vessels (these would vanish) or too soft for larger vessels.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may also try the “Resample image (BRAINS)” module that has a special “binary” mode for labelmap interpolation.</p>
</blockquote>
</aside>
<p>I will investigate this further.</p>

---

## Post #12 by @lassoan (2021-05-11 04:49 UTC)

<p>For future reference: I’ve submitted a bug report for integrating this centerline endpoint adjustment algorithm into VMTK/SlicerVMTK - <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/26" class="inline-onebox">Extracted centerlines sometimes contain straight line segments · Issue #26 · vmtk/SlicerExtension-VMTK · GitHub</a></p>

---

## Post #13 by @perecanals (2021-05-11 11:54 UTC)

<aside class="quote no-group" data-username="perecanals" data-post="11" data-topic="14068">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/perecanals/48/9006_2.png" class="avatar"> perecanals:</div>
<blockquote>
<p>In my case, I get the affine matrix using the nibabel package, directly from the NIfTI file itself:</p>
<pre><code class="lang-auto">aff = nib.load("/path/to/nifti.nii.gz").affine
</code></pre>
</blockquote>
</aside>
<p>In order to get everything a little more wrapped up, I now extract the segmentation  numpy array from the labelmapVolumeNode associated with the segmentation node, and get the affine matrix from the same labelmapVolumeNode:</p>
<pre><code># Get volume node array from segmentation node
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode)
segmentationArray = slicer.util.arrayFromVolume(labelmapVolumeNode)

# Get affine matrix from segmentation labelMapVolumeNode
vtkAff = vtk.vtkMatrix4x4()
aff = np.eye(4)
labelmapVolumeNode.GetIJKToRASMatrix(vtkAff)
vtkAff.DeepCopy(aff.ravel(), vtkAff)
</code></pre>
<p>This solves a couple of small issues you can have in some occasions if you extract the affine matrix from the original NIfTI image, since you can apply some processing to the segmentation itself.</p>

---
