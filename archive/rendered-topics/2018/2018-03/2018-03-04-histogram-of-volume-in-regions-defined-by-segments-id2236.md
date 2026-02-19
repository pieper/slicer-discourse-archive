---
topic_id: 2236
title: "Histogram Of Volume In Regions Defined By Segments"
date: 2018-03-04
url: https://discourse.slicer.org/t/2236
---

# Histogram of volume in regions defined by segments

**Topic ID**: 2236
**Date**: 2018-03-04
**URL**: https://discourse.slicer.org/t/histogram-of-volume-in-regions-defined-by-segments/2236

---

## Post #1 by @drusmanbashir (2018-03-04 15:11 UTC)

<p>Hi.<br>
I am trying to apply a mask (LabelMap) to a volume in slicer to plot histograms of intensities within the masked region of interest. The necessary requisite is that I do all this programmatically using segmentation map (without using the GUI to export it to label Map). So the label map i get from code below is already confined to segmentation map bounding box (and not the entire volume as you would get if you exported the segmentation map):</p>
<pre><code class="lang-python">seg = getNode('Segmentation')
labelMapNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelMapNode)
</code></pre>
<p>Before applying the mask to the ROI, i am trying to crop the ROI but failing (believe it can be done using VTK filters but using the crop image filter (i have the code) was also failing):</p>
<pre><code class="lang-python">#========= GETTING MASK ARRAY FROM LABELMAP TO NUMPY ==========
maskSize = labelMapNode.GetImageData().GetDimensions()
mask = labelMapNode.GetImageData().GetPointData().GetScalars()
vtk_mask= vtk_to_numpy(mask)
roi_size  = labelMapNode.GetImageData().GetDimensions()
mask = vtk_mask.reshape(roi_size)   

#====COORDINATES OF MASK ARRAY RELATIVE TO THE MAIN IMAGE ===========
location_mask = mat.MultiplyDoublePoint(labelMapNode.GetOrigin()+(1,))
location_mask =  np.array(location_mask).astype(int)[:3]


#============ GETTING BOUNDED REGION OF INTEREST FROM MAIN VOLUME
roi =  img[location_mask[0]:location_mask[0]+roi_size[0],
    location_mask[1]:location_mask[1]+roi_size[1],
    location_mask[2]:location_mask[2]+roi_size[2]]


#=============== CONVERTING ROI INTO A NEW VOLUME NODE========================
outputVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')

sitkImageOutput = sitk.GetImageFromArray(roi)
sitkUtils.PushVolumeToSlicer(sitkImageOutput, outputVolumeNode)
outputVolumeNode.SetOrigin(inputVolumeNode.GetOrigin())
outputVolumeNode.SetSpacing(inputVolumeNode.GetSpacing())
</code></pre>
<p>The resulting ROI inside slicer just looks very strange and seems to have gaps in it. Is there some interpolation step there? I am sure there is an easier way to do this using filters and i will appreciate the help. The goal is to draw a histogram based on ROI.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-03-04 22:33 UTC)

<p>Here is a complete example that does exactly what you need (computes histogram for each region of a volume defined by a segment). It use Mask volume effect of SegmentEditorExtraEffects extension, so you need to install that extension.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f">
  <header class="source">

      <a href="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f" target="_blank" rel="noopener">https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f</a></h4>

  <h5>MaskVolumeHistogramPlot.py</h5>
  <pre><code class="Python"># Generate input data
################################################

import SampleData
import numpy as np

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()
</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/2f5071c562108dac8efe277c78f2620f" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47b47195187995cf668f498f1f9f5557c1285c26.jpeg" data-download-href="/uploads/short-url/aekuWWLY6olSS7T2QPEBE6u29Po.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47b47195187995cf668f498f1f9f5557c1285c26_2_601x500.jpg" alt="image" data-base62-sha1="aekuWWLY6olSS7T2QPEBE6u29Po" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47b47195187995cf668f498f1f9f5557c1285c26_2_601x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47b47195187995cf668f498f1f9f5557c1285c26_2_901x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47b47195187995cf668f498f1f9f5557c1285c26_2_1202x1000.jpg 2x" data-dominant-color="626361"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2026×1684 538 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @hherhold (2018-03-05 00:02 UTC)

<p>Hi Andras,</p>
<p>The plotting part of this is really similar to something I was trying to get working in a module I’ve been working on - is vtkMRMLPlotSeriesNode new? When I try to make one in a nightly from January, Slicer crashes.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #4 by @lassoan (2018-03-05 00:08 UTC)

<p>Yes, Plots module is fully reworked and vastly improved 1-2 weeks ago. The example script above requires these changes.</p>

---

## Post #5 by @tenzin_kunkyab (2019-07-12 19:34 UTC)

<p>Hi Lassoan,</p>
<p>Thank you for sharing this, if I want to do it on my own CT dicom images, how can I change the code ?</p>
<p>best<br>
Tenzin</p>

---

## Post #6 by @tenzin_kunkyab (2019-07-12 19:51 UTC)

<p>Basically what I would like to ask is how can I use this python file into the 3d slicer and my second question is how can I change the code to use my own volume and segmentation.</p>
<p>best<br>
Tenzin</p>

---

## Post #7 by @tenzin_kunkyab (2019-07-12 20:22 UTC)

<p>And also last thing is that I am using segment editor on 3d slicer, so I would like to be able to get the histogram of the segmentation that I just draw.</p>
<p>best<br>
Tenzin</p>

---

## Post #8 by @lassoan (2019-07-12 22:42 UTC)

<p>You can use the code by copy-pasting it to Slicer’s Python console (hit Ctrl-3 to display it). If you want to write automated processing code then skip the first part that generates test data and provide your nodes as input instead.</p>
<p>There is now an effect called “Split volume” that extracts each segmented region into a separate volume. You may use this effect and then for each extracted volume you can find the histogram in Volumes module (or compute histogram for these already masked volumes by a few numpy commands).</p>

---

## Post #9 by @das (2019-09-02 21:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SegmentEditorExtraEffects</p>
</blockquote>
</aside>
<p>Hello Prof Lasso,<br>
Thank you so much for this. My students and I have been struggling with doing this for weeks. I will like to install SegmentEditorExtraEffects via Extension Manager in version 4.10.2<br>
Meanwhile, I will like to request for the steps involved in computing histogram for each region of a volume defined by a segment. Secondly, I would not mind any materials that will help me in exploring the full power of SegmentEditorExtraEffects.<br>
Many thanks.<br>
Michael</p>

---

## Post #10 by @lassoan (2019-09-03 17:14 UTC)

<aside class="quote no-group" data-username="das" data-post="9" data-topic="2236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/das/48/67119_2.png" class="avatar"> das:</div>
<blockquote>
<p>I will like to install SegmentEditorExtraEffects via Extension Manager in version 4.10.2</p>
</blockquote>
</aside>
<p>It is available in the Extension Manager. If you have trouble installing it then please describe what you do, what you expect to happen, and what happens instead.</p>
<aside class="quote no-group" data-username="das" data-post="9" data-topic="2236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/das/48/67119_2.png" class="avatar"> das:</div>
<blockquote>
<p>I will like to request for the steps involved in computing histogram for each region of a volume defined by a segment.</p>
</blockquote>
</aside>
<p>You can use the script referenced above. if you have your own image and segmentation then skip lines above <code># Perform analysis</code> and make sure <code>segmentationNode</code> and <code>masterVolumeNode</code> variables are set to your data nodes.</p>
<aside class="quote no-group" data-username="das" data-post="9" data-topic="2236">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/das/48/67119_2.png" class="avatar"> das:</div>
<blockquote>
<p>I would not mind any materials that will help me in exploring the full power of SegmentEditorExtraEffects</p>
</blockquote>
</aside>
<p>These are just some additional effects for Segment Editor module. You can find tutorials about Segment Editor <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">here</a>.</p>

---
