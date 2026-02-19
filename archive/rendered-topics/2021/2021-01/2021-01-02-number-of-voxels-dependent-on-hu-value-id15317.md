---
topic_id: 15317
title: "Number Of Voxels Dependent On Hu Value"
date: 2021-01-02
url: https://discourse.slicer.org/t/15317
---

# Number of voxels dependent on HU value

**Topic ID**: 15317
**Date**: 2021-01-02
**URL**: https://discourse.slicer.org/t/number-of-voxels-dependent-on-hu-value/15317

---

## Post #1 by @seymakandemir (2021-01-02 20:23 UTC)

<p>Hi all,</p>
<p>I created a segment of volume and got the histogram of segment. What I need to do next is to have statistical data about segment such as; How many voxels above/under 2000 HU value? And their percentage?<br>
I could again create 2 segments with 2000 being the boundary, but I just need the number. Is there a way that I can assing the number of voxels under 2000 HU to a variable in possibly Python Interactor.</p>
<p>Best regards.</p>
<p>Code im using:</p>
<pre data-code-wrap="python"><code class="lang-python">##just histogram
import numpy as np
import SampleData 

masterVolumeNode=getNode('inputVolumeNode')
segmentationNode=getNode('Segmentation')



# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()   #segment editor modulüne erişmek için
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)    #segmentation
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)    #segmentvolume

# Set up masking parameters
segmentEditorWidget.setActiveEffectByName("Mask volume")   #mask volume kısmı histogram için segmentasyonu masklemelisin
effect = segmentEditorWidget.activeEffect()
# set fill value to be outside the valid intensity range
intensityRange = masterVolumeNode.GetImageData().GetScalarRange()
effect.setParameter("FillValue", str(intensityRange[0]-1))
# Blank out voxels that are outside the segment
effect.setParameter("Operation", "FILL_OUTSIDE")
# Create a volume that will store temporary masked volumes
maskedVolume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "Temporary masked volume")
effect.self().outputVolumeSelector.setCurrentNode(maskedVolume)

# Create chart
plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode", "Histogram")



# Create histogram plot data series for each masked volume
for segmentIndex in range(segmentationNode.GetSegmentation().GetNumberOfSegments()):#for segmentIndex in segmentsayisi
  # Set active segment
  segmentID = segmentationNode.GetSegmentation().GetNthSegmentID(segmentIndex)
  segmentEditorWidget.setCurrentSegmentID(segmentID)
  # Apply mask
  effect.self().onApply()
  # Compute histogram values
  histogram = np.histogram(arrayFromVolume(maskedVolume), bins=400, range=intensityRange)
  # Save results to a new table node
  segment = segmentationNode.GetSegmentation().GetNthSegment(segmentIndex)
  tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", segment.GetName() + " histogram table")
  updateTableFromArray(tableNode, histogram)
  tableNode.GetTable().GetColumn(0).SetName("Count")
  tableNode.GetTable().GetColumn(1).SetName("Intensity")
  # Create new plot data series node
  plotSeriesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", segment.GetName() + " histogram")
  plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
  plotSeriesNode.SetXColumnName("Intensity")
  plotSeriesNode.SetYColumnName("Count")
  plotSeriesNode.SetPlotType(slicer.vtkMRMLPlotSeriesNode.PlotTypeScatter)
  plotSeriesNode.SetMarkerStyle(slicer.vtkMRMLPlotSeriesNode.MarkerStyleNone)
  plotSeriesNode.SetUniqueColor()
  # Add plot to chart
  plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())

# Show chart in layout
slicer.modules.plots.logic().ShowChartInLayout(plotChartNode)

# Delete temporary node
slicer.mrmlScene.RemoveNode(maskedVolume)
slicer.mrmlScene.RemoveNode(segmentEditorNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c83f8baf75f9ac6006497b82ae15459a19518ec.png" data-download-href="/uploads/short-url/k33AOfCUDwAGg6HpDKM31wVnhta.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c83f8baf75f9ac6006497b82ae15459a19518ec_2_690x370.png" alt="image" data-base62-sha1="k33AOfCUDwAGg6HpDKM31wVnhta" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c83f8baf75f9ac6006497b82ae15459a19518ec_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c83f8baf75f9ac6006497b82ae15459a19518ec_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c83f8baf75f9ac6006497b82ae15459a19518ec_2_1380x740.png 2x" data-dominant-color="B5B7B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pll_llq (2021-01-04 17:49 UTC)

<p>You can convert a volume masked by a segmentation to a numpy array with <code>slicer.util.arrayFromVolume</code> and compute the number from the array.</p>

---

## Post #3 by @lassoan (2021-01-04 22:20 UTC)

<p>You have already solved the problem. You can get the histogram with any resolution and then sum values of the histogram to get total number of voxels in a certain intensity range.</p>
<p>Alternatively, you can find a complete implementation of this feature as a module with a nice GUI in <a href="https://discourse.slicer.org/t/new-lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006">LungCTAnalyzer extension</a>: it computes volume of each region that is specified by voxel intensity range. It shows nice real-time preview, generates, PDF report, etc. To get started, you can use the module as is, just ignoring that takes “left lung” and “right lung” segments as inputs. You can put any other structure in those segments and you can specify any intensity range. If it is close enough to what you want to achieve, you can easily customize it to be more convenient and intuitive for your data sets - it is just a Python scripted module that you can modify with a text editor.</p>

---

## Post #5 by @seymakandemir (2021-01-05 10:30 UTC)

<aside class="quote no-group quote-post-not-found" data-username="seymakandemir" data-post="4" data-topic="15317">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/a5b964/48.png" class="avatar"> seymakandemir:</div>
<blockquote>
<p>I looked at the LungCT analyzer you mentioned. Using this module, I can get the maximum HU value of 1000. I could not use it because I wanted to work in a wider range.<br>
I changed the code to get the voxel number above and below 2000HU. I still couldn’t make it look like this percentage is below or above 2000HU.<br>
My modified code:</p>
</blockquote>
</aside>
<p>import numpy as np<br>
import SampleData<br>
masterVolumeNode=getNode(‘inputVolumeNode_masked’)<br>
segmentationNode=getNode(‘Segmentation’)</p>
<h1><a name="p-52453-create-segment-editor-to-get-access-to-effects-1" class="anchor" href="#p-52453-create-segment-editor-to-get-access-to-effects-1" aria-label="Heading link"></a>Create segment editor to get access to effects</h1>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()   <a class="hashtag-cooked" href="/tag/segment" data-type="tag" data-slug="segment" data-id="464" data-style-type="icon" data-icon="tag"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>segment</span></a> editor modulüne erişmek için</p>
<h1><a name="p-52453-to-show-segment-editor-widget-useful-for-debugging-segmenteditorwidgetshow-2" class="anchor" href="#p-52453-to-show-segment-editor-widget-useful-for-debugging-segmenteditorwidgetshow-2" aria-label="Heading link"></a>To show segment editor widget (useful for debugging): segmentEditorWidget.show()</h1>
<p>segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)    <a class="hashtag-cooked" href="/tag/segmentation" data-type="tag" data-slug="segmentation" data-id="8" data-style-type="icon" data-icon="tag"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>segmentation</span></a><br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)    <span class="hashtag-raw">#segmentvolume</span></p>
<h1><a name="p-52453-set-up-masking-parameters-3" class="anchor" href="#p-52453-set-up-masking-parameters-3" aria-label="Heading link"></a>Set up masking parameters</h1>
<p>segmentEditorWidget.setActiveEffectByName(“Mask volume”)   <span class="hashtag-raw">#mask</span> volume kısmı histogram için segmentasyonu masklemelisin<br>
effect = segmentEditorWidget.activeEffect()</p>
<h1><a name="p-52453-set-fill-value-to-be-outside-the-valid-intensity-range-4" class="anchor" href="#p-52453-set-fill-value-to-be-outside-the-valid-intensity-range-4" aria-label="Heading link"></a>set fill value to be outside the valid intensity range</h1>
<p>intensityRange = masterVolumeNode.GetImageData().GetScalarRange()<br>
effect.setParameter(“FillValue”, str(intensityRange[0]-1))</p>
<h1><a name="p-52453-blank-out-voxels-that-are-outside-the-segment-5" class="anchor" href="#p-52453-blank-out-voxels-that-are-outside-the-segment-5" aria-label="Heading link"></a>Blank out voxels that are outside the segment</h1>
<p>effect.setParameter(“Operation”, “FILL_OUTSIDE”)</p>
<h1><a name="p-52453-create-a-volume-that-will-store-temporary-masked-volumes-6" class="anchor" href="#p-52453-create-a-volume-that-will-store-temporary-masked-volumes-6" aria-label="Heading link"></a>Create a volume that will store temporary masked volumes</h1>
<p>maskedVolume = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, “Temporary masked volume”)<br>
effect.self().outputVolumeSelector.setCurrentNode(maskedVolume)</p>
<h1><a name="p-52453-create-chart-7" class="anchor" href="#p-52453-create-chart-7" aria-label="Heading link"></a>Create chart</h1>
<p><span class="hashtag-raw">#plotChartNode</span> = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLPlotChartNode”, “Histogram”)</p>
<h1><a name="p-52453-create-histogram-plot-data-series-for-each-masked-volume-8" class="anchor" href="#p-52453-create-histogram-plot-data-series-for-each-masked-volume-8" aria-label="Heading link"></a>Create histogram plot data series for each masked volume</h1>
<p>for segmentIndex in range(segmentationNode.GetSegmentation().GetNumberOfSegments()):<span class="hashtag-raw">#for</span> segmentIndex in segmentsayisi</p>
<h1><a name="p-52453-set-active-segment-9" class="anchor" href="#p-52453-set-active-segment-9" aria-label="Heading link"></a>Set active segment</h1>
<p>segmentID = segmentationNode.GetSegmentation().GetNthSegmentID(segmentIndex)<br>
segmentEditorWidget.setCurrentSegmentID(segmentID)</p>
<h1><a name="p-52453-apply-mask-10" class="anchor" href="#p-52453-apply-mask-10" aria-label="Heading link"></a>Apply mask</h1>
<p>effect.self().onApply()</p>
<h1><a name="p-52453-compute-histogram-values-11" class="anchor" href="#p-52453-compute-histogram-values-11" aria-label="Heading link"></a>Compute histogram values</h1>
<p>histogram_upper = np.histogram(arrayFromVolume(maskedVolume), bins=1, range=(2000,np.amax(intensityRange)))</p>
<h1><a name="p-52453-save-results-to-a-new-table-node-12" class="anchor" href="#p-52453-save-results-to-a-new-table-node-12" aria-label="Heading link"></a>Save results to a new table node</h1>
<p>segment = segmentationNode.GetSegmentation().GetNthSegment(segmentIndex)<br>
tableNode=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”, segment.GetName() + " histogram_upper table")<br>
updateTableFromArray(tableNode, histogram_upper)<br>
tableNode.GetTable().GetColumn(0).SetName(“Count”)<br>
tableNode.GetTable().GetColumn(1).SetName(“Intensity”)</p>
<h1><a name="p-52453-create-new-plot-data-series-node-13" class="anchor" href="#p-52453-create-new-plot-data-series-node-13" aria-label="Heading link"></a>Create new plot data series node</h1>
<p><span class="hashtag-raw">#histogram_lower</span><br>
histogram_lower= np.histogram(arrayFromVolume(maskedVolume), bins=1, range=(np.amin(intensityRange),1999))<br>
tableNode=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”, segment.GetName() + " histogram_lower table")<br>
updateTableFromArray(tableNode, histogram_lower)<br>
tableNode.GetTable().GetColumn(0).SetName(“Count”)<br>
tableNode.GetTable().GetColumn(1).SetName(“Intensity”)</p>
<h1><a name="p-52453-create-new-plot-data-series-node-14" class="anchor" href="#p-52453-create-new-plot-data-series-node-14" aria-label="Heading link"></a>Create new plot data series node</h1>
<h1><a name="p-52453-delete-temporary-node-15" class="anchor" href="#p-52453-delete-temporary-node-15" aria-label="Heading link"></a>Delete temporary node</h1>
<p>slicer.mrmlScene.RemoveNode(maskedVolume)<br>
slicer.mrmlScene.RemoveNode(segmentEditorNode)</p>
<p>Fig.1: Number of voxels under 2000HU<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60a3821227e256a9faba0b3610b1b6d9827443b0.png" data-download-href="/uploads/short-url/dMU9oRvzoGrWlBdCdWtfnCIiVl6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60a3821227e256a9faba0b3610b1b6d9827443b0_2_690x470.png" alt="image" data-base62-sha1="dMU9oRvzoGrWlBdCdWtfnCIiVl6" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60a3821227e256a9faba0b3610b1b6d9827443b0_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60a3821227e256a9faba0b3610b1b6d9827443b0_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60a3821227e256a9faba0b3610b1b6d9827443b0.png 2x" data-dominant-color="D6D8D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1105×753 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Fig.2: Number of voxels above 2000HU<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83cf31903f55cc8ccd035bd4996de0e9ac41d653.png" data-download-href="/uploads/short-url/iO2srXbdNdLBPb7WIWadguvVctR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83cf31903f55cc8ccd035bd4996de0e9ac41d653_2_684x500.png" alt="image" data-base62-sha1="iO2srXbdNdLBPb7WIWadguvVctR" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83cf31903f55cc8ccd035bd4996de0e9ac41d653_2_684x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83cf31903f55cc8ccd035bd4996de0e9ac41d653_2_1026x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83cf31903f55cc8ccd035bd4996de0e9ac41d653.png 2x" data-dominant-color="D8DADB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×768 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #6 by @seymakandemir (2021-01-05 10:33 UTC)

<p>Since I have just started using this program, I am not very familiar yet. I don’t know how to use this.<br>
Thank you</p>

---
