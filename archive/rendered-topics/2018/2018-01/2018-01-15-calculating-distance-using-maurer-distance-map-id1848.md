---
topic_id: 1848
title: "Calculating Distance Using Maurer Distance Map"
date: 2018-01-15
url: https://discourse.slicer.org/t/1848
---

# Calculating distance using Maurer distance map

**Topic ID**: 1848
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/calculating-distance-using-maurer-distance-map/1848

---

## Post #1 by @tnguyen (2018-01-15 18:43 UTC)

<p>Hi everyone,</p>
<p>I’m trying to use Maurer 3D distance map to calculate the difference in size of a tumor before and after procedure (to estimate margin). I applied the signedmaurerdistancemap filter to the pre-procedure tumor, but how do I superimpose the post-procedure tumor onto this map and pull out the difference in distance of the tumor before and after procedure? Thank you</p>

---

## Post #2 by @lassoan (2018-01-15 20:01 UTC)

<p>You can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison">Segment Comparison</a> module and I think <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ChangeTracker">ChangeTracker</a> can do some quantifications like this, too.</p>
<p>Of course you can compute the distance map and do your custom visualization, too. Just choose the overlay as foreground volume and go to Volumes module to threshold the distance map and customize colormap and window width/level.</p>

---

## Post #3 by @tnguyen (2018-01-15 21:53 UTC)

<p>Thank you for replying!</p>
<p>I can’t seem to figure out how to use the Volume module to calculate the distance. I set the post-procedure tumor volume as the back ground, the pre-procedure tumor with 3D map as the foreground.  The active volume is also set as the pre-procedure tumor volume with 3D map. However, the Histogram section of the volume module doesn’t show any numbers (I presumed that this is where the histogram of distance data would show). Did I get anything wrong? (I also tried to switch the background and foreground but still no results in histogram section…)</p>

---

## Post #4 by @lassoan (2018-01-15 22:41 UTC)

<p>What exact would you like to compute? If you only need tumor volumes then you can get it from Segment Statistics module (after you segmented the tumor using Segment Editor).</p>

---

## Post #5 by @tnguyen (2018-01-15 22:57 UTC)

<p>I would like to compute the difference in distance between the pre procedure volume and the post procedure volume (to see if the procedure achieved adequate margin). I had some results using the Segment Comparison as you suggested (thank you!). I was just trying to learn how to compute the margin using the Maurer distance map.</p>

---

## Post #6 by @lassoan (2018-01-15 23:24 UTC)

<p>Distance is computed by Segment Comparison module. It computes metrics like maximum, 95th percentile, and median of the distance distribution.</p>

---

## Post #7 by @tnguyen (2018-01-16 01:10 UTC)

<p>Thank you for your suggestion, I will learn more about the Segment Comparison module!</p>

---

## Post #8 by @tnguyen (2018-01-16 16:07 UTC)

<p>I have been able to use Segment Comparison and got the maximum, 95th, and median distance just like you described. However, is there a way to extract all the distances between the two segments instead of just the three metrics above? I want to assess if the treatment zone has achieved enough margin around the pre-treatment tumor, so the minimum distance between these two segments is more important for this assessment.</p>
<p>I’ve been searching for awhile, and I found a link on github<br>
[<a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.cxx" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.cxx</a>]<br>
It seems like Segment Comparison module does calculate all the distances but only the max, 95th, and median are shown in Slicer. I have only been using Slicer for a couple weeks but I’m very much interested to learn more. Would you point me in the direction of extracting the distance histogram or just the minimum distance value?</p>

---

## Post #9 by @lassoan (2018-01-16 16:13 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Could you give advice on how to get the complete histogram?</p>

---

## Post #10 by @lassoan (2018-01-16 16:40 UTC)

<p>Note that you can also export segments to model nodes and use <code>Model to Model Distance</code> extension to get a model that has the computed distances for each point. You can display this model as a colored surface, you can export distances to numpy and compute basic stats, histogram, etc. and you can also save results into a table (.csv file) and plotting.</p>
<p>For example, you can get this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abbffc23deca81140348a5366d4a57bcc6c7684e.jpeg" data-download-href="/uploads/short-url/ovmYl9K92fJzVtq65fuM9aIIVoW.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_690x373.jpg" alt="image" data-base62-sha1="ovmYl9K92fJzVtq65fuM9aIIVoW" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_1380x746.jpg 2x" data-dominant-color="ACAAA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 451 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>By performing the steps described above and copy-pasting this script into the Python console:</p>
<pre><code>modelNode = getNode('VTK Output File')
distanceArrayName = "Signed"

# Get distances from point data
import numpy as np
distances = vtk.util.numpy_support.vtk_to_numpy(modelNode.GetPolyData().GetPointData().GetArray(distanceArrayName))

# Print basic stats
print("Minimum distance: %f" % min(distances))
print("Maximum distance: %f" % max(distances))
print("Mean distance: %f" % np.mean(distances))

# Compute histogram
histogram = np.histogram(distances, bins=100)

# Save results to a new table node
tableNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", modelNode.GetName() + " histogram")
updateTableFromArray(tableNode, histogram)
tableNode.GetTable().GetColumn(0).SetName("Count")
tableNode.GetTable().GetColumn(1).SetName("Intensity")

# Create plot

plotDataNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotDataNode")
plotDataNode.SetAndObserveTableNodeID(tableNode.GetID())
plotDataNode.SetXColumnName("Intensity")
plotDataNode.SetYColumnName("Count")

plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
plotChartNode.AddAndObservePlotDataNodeID(plotDataNode.GetID())
plotChartNode.SetAttribute("Type", "Bar") # delete this line for line plot

# Show plot in layout

layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpPlotView)
plotWidget = layoutManager.plotWidget(0)

plotViewNode = plotWidget.mrmlPlotViewNode()
plotViewNode.SetPlotChartNodeID(plotChartNode.GetID())
</code></pre>

---

## Post #11 by @cpinter (2018-01-16 17:43 UTC)

<p>There’s a class that can get the histogram of the model distances called <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkPolyDataDistanceHistogramFilter.h">vtkPolyDataDistanceHistogramFilter</a>. There is no user interface for that so python scripting is necessary. If you use Segment Editor then you can get the poly data from the segments, feed them to this class, and get the output as vtkTable, so tables and plots can be shown in Slicer. Let me know if you’d like me to provide actual code.</p>

---

## Post #12 by @tnguyen (2018-01-16 17:52 UTC)

<p>Yay! Thank you so much! I will try this and will update to let you know!</p>

---

## Post #13 by @tnguyen (2018-01-16 17:54 UTC)

<p>Hi Csaba,<br>
Yes please I would like the code if it’s not too much trouble, thanks so much for reply!</p>

---

## Post #14 by @cpinter (2018-01-16 18:30 UTC)

<p>Here you go:</p>
<pre><code>import vtkSlicerSegmentComparisonModuleLogicPython
polHist = vtkSlicerSegmentComparisonModuleLogicPython.vtkPolyDataDistanceHistogramFilter()
segNode = slicer.util.getNode('vtkMRMLSegmentationNode1')
poly1 = segNode.GetSegmentation().GetSegment('Segment_1').GetRepresentation(slicer.vtkSegmentationConverter.GetSegmentationClosedSurfaceRepresentationName())
poly2 = segNode.GetSegmentation().GetSegment('Segment_2').GetRepresentation(slicer.vtkSegmentationConverter.GetSegmentationClosedSurfaceRepresentationName())
polHist.SetInputReferencePolyData(poly1)
polHist.SetInputComparePolyData(poly2)
polHist.Update()
histTable = polHist.GetOutputHistogram()
tableNode = slicer.vtkMRMLTableNode()
tableNode.SetAndObserveTable(histTable)
slicer.mrmlScene.AddNode(tableNode)
</code></pre>
<p>Then you can save the table to csv with Save data dialog, or oyu can make a plot with it from Tables module.</p>
<p>Oh, and you need to install the SlicerRT extension first to have the Segment Comparison module if you haven’t.</p>

---

## Post #15 by @tnguyen (2018-01-16 22:39 UTC)

<p>Thank you so much for this, it works like magic!!! Now I will try to learn more about the method from Csaba</p>

---

## Post #16 by @tnguyen (2018-01-16 23:50 UTC)

<p>Hi Csaba,<br>
I calculated the Hausdorff distance and I put the code in the python console. But when I get to the fourth line, I get the below message (and when I paste the whole script in, slicer would crash).<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/182545fd5a743e035e98097e8e6dad5e3594e9e6.jpeg" data-download-href="/uploads/short-url/3rBjFdS82rU7fUeCy2GaT2qA7nU.jpg?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/182545fd5a743e035e98097e8e6dad5e3594e9e6_2_690x370.jpg" alt="12" data-base62-sha1="3rBjFdS82rU7fUeCy2GaT2qA7nU" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/182545fd5a743e035e98097e8e6dad5e3594e9e6_2_690x370.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/182545fd5a743e035e98097e8e6dad5e3594e9e6_2_1035x555.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/182545fd5a743e035e98097e8e6dad5e3594e9e6_2_1380x740.jpg 2x" data-dominant-color="BDBEBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">1920×1032 466 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @lassoan (2018-01-17 00:50 UTC)

<p>The problem is that incorrect segmentation node name is specified for slicer.util.getNode.</p>

---

## Post #18 by @cpinter (2018-01-17 14:45 UTC)

<p>I think the issue is not the segmentation node but the segment, because otherwise the error message would be “AttributeError: ‘NoneType’ object has no attribute ‘GetSegmentation’”. But in any case, any string literals in sample code should be double checked for your use case, because every Slicer scene is different. You can get the segment IDs like this:</p>
<pre><code>segmentIds = vtk.vtkStringArray()
segNode.GetSegmentation().GetSegmentIDs(segmentIds)
for i in xrange(segmentIds.GetNumberOfValues()):
  print segmentIds.GetValue(i)</code></pre>

---

## Post #19 by @tnguyen (2018-01-17 22:48 UTC)

<p>ah I see, thanks so much Csaba!</p>

---

## Post #20 by @ytaneja (2019-09-18 21:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="1848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example, you can get this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e.jpg" data-download-href="/uploads/short-url/ovmYl9K92fJzVtq65fuM9aIIVoW.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_690x373.jpg" alt="image" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/abbffc23deca81140348a5366d4a57bcc6c7684e_2_1380x746.jpg 2x" data-dominant-color="ACAAA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 451 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
</aside>
<p>What are the units that you have in the histogram? 1100 (pixels, mm, microns?) difference in the models</p>
<p>Thank you!</p>

---

## Post #21 by @lassoan (2019-09-18 22:33 UTC)

<aside class="quote no-group" data-username="ytaneja" data-post="20" data-topic="1848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/bbe5ce/48.png" class="avatar"> ytaneja:</div>
<blockquote>
<p>What are the units that you have in the histogram? 1100 (pixels, mm, microns?) difference in the models</p>
</blockquote>
</aside>
<p>It is a histogram. Y axis is count, which is the number of model points in that distance bin.</p>

---
