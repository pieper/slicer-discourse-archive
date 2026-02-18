# Intensities histogram of a segmented area

**Topic ID**: 2164
**Date**: 2018-02-24
**URL**: https://discourse.slicer.org/t/intensities-histogram-of-a-segmented-area/2164

---

## Post #1 by @Diana (2018-02-24 09:08 UTC)

<p>Hello,</p>
<p>please is there any way, how to get the histogram of intensities of only a bordered area by segmentation? I am working with MRI scans, one is 3D and serves for the segmantation of an organ and the second, which is only 3 slices, is a relaxation map. I would like to obtain intensities histograms of chosen organs and compare pathological and physiological values</p>
<p>many thanks</p>

---

## Post #2 by @lassoan (2018-02-25 21:45 UTC)

<p>You can use Mask Volume effect (in SegmentEditorExtraEffects extension) to blank out areas of a volume that is outside of a segment. You can then use VTK or numpy to compute histogram (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_histogram_plot_of_a_volume">example of computing and displaying histogram of a volume in Python</a>) .</p>

---

## Post #3 by @JoostJM (2018-02-26 09:22 UTC)

<p>Additionally, if you want to compare healthy and pathological using statistics calculated on the histograms, you can use the SlicerRadiomics extension, which is the Slicer module for PyRadiomics. Features in class “FirstOrder” are the histogram features and are calculated on the histogram of the Region of Interest, which you can define using segments or binary label maps.</p>

---

## Post #4 by @Diana (2018-02-26 14:32 UTC)

<p>Thank you very much for your reply!</p>
<p>I would like to ask one more thing: can I really blank out areas out of my volume of interest? They become black and that causes a big column in the histogram and I would like them to be of no value</p>

---

## Post #5 by @lassoan (2018-02-26 14:37 UTC)

<p>You can set the “blanking” intensity to any value and then ignore that value in the histogram.</p>

---

## Post #6 by @drusmanbashir (2018-03-05 18:07 UTC)

<p>Hi Diana,<br>
I did something similar for my data. Assuming you start with a Volume node named ‘inputVolumeNode’ and draw a segmentation ROI on it (default name ‘Segmentation’) the following code should do it for you. Caveat: You need the latest nightly build of slicer to draw the plot :</p>
<p>import SimpleITK as sitk<br>
import sitkUtils<br>
import numpy as np</p>
<p>newScalarNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’) <span class="hashtag">#to</span> be used later<br>
seg = getNode(‘Segmentation’)</p>
<p><span class="hashtag">#create</span> a temporary labelmap<br>
labelMapNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)</p>
<p><span class="hashtag">#using</span> reference volume will match the geometry<br>
ids = vtk.vtkStringArray()<br>
seg.GetSegmentation().GetSegmentIDs(ids)<br>
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg,ids,labelMapNode,inputVolumeNode)</p>
<p>mif = sitk.MaskImageFilter()<br>
mif.SetOutsideValue(-1234) <span class="hashtag">#custom</span> dummy value that’s recognizable</p>
<p>roiSITK = sitkUtils.PullVolumeFromSlicer(inputVolumeNode)<br>
maskSITK = sitkUtils.PullVolumeFromSlicer(labelMapNode)<br>
final = mif.Execute(roiSITK,maskSITK)</p>
<p>sitkUtils.PushVolumeToSlicer(final,newScalarNode)</p>
<p><span class="hashtag">#creating</span> histogram  &lt;-------------- from this onwards the code is from slicer scripts webpage</p>
<p>np_tmp = arrayFromVolume(newScalarNode)<br>
np_tmp=np_tmp[np_tmp!=-1234] # flattens the array and removes selected outside label values<br>
histogram = np.histogram(np_tmp, bins=50)</p>
<p><span class="hashtag">#Save</span> results to a new table node<br>
tableNode=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”)<br>
updateTableFromArray(tableNode, histogram)<br>
tableNode.GetTable().GetColumn(0).SetName(“Count”)<br>
tableNode.GetTable().GetColumn(1).SetName(“Intensity”)</p>
<p><span class="hashtag">#Create</span> plot   ------  DOES  NOT EXIST ON PRE VERSION 4.9 !</p>
<p>plotSeriesNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLPlotSeriesNode”, newScalarNode.GetName() + ’ histogram’)<br>
plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())<br>
plotSeriesNode.SetXColumnName(“Intensity”)<br>
plotSeriesNode.SetYColumnName(“Count”)<br>
plotSeriesNode.SetPlotType(plotSeriesNode.PlotTypeScatterBar)<br>
plotSeriesNode.SetColor(0, 0.6, 1.0)</p>
<p><span class="hashtag">#Create</span> chart and add plot<br>
plotChartNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLPlotChartNode”)<br>
plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())<br>
plotChartNode.YAxisRangeAutoOff()<br>
plotChartNode.SetYAxisRange(0, 500000)</p>
<p><span class="hashtag">#Show</span> plot in layout<br>
slicer.modules.plots.logic().ShowChartInLayout(plotChartNode)</p>

---

## Post #7 by @lassoan (2018-03-05 18:53 UTC)

<p>I’ve also implemented this exact feature - see here: <a href="https://discourse.slicer.org/t/histogram-of-volume-in-regions-defined-by-segments/2236/2?u=lassoan">Histogram of volume in regions defined by segments</a></p>
<p>Probably it is very similar to what <a class="mention" href="/u/drusmanbashir">@drusmanbashir</a> described above. Main difference is that I used SegmentEditorExtraEffects extension’s Mask Volume effect to do the masking, which is somewhat more complicated, but works even if the segmentation’s master volume is not the same as the volume where you need compute the histograms on. There is also a small difference in the blanking value computation: I retrieve scalar range from the volume and select a blanking value that lies just outside this range; then specify the valid range in np.histogram to make sure the histogram bin distribution is not affected by the blanking value.</p>

---

## Post #8 by @drusmanbashir (2018-03-05 21:58 UTC)

<p>Thanks a lot Andras,<br>
Your code appears to be a skeleton of a very useful module - one that would enable histogram visualisation of active segmentations.</p>
<p>Could you add a snipet that would update the histogram to reflect single axial view ROI (instead of entire segmentation map as current) stats as the user scrolls through the axial data? As a user I will also be interested to know the histogram of the current 2D circle I have just drawn over an object on the MRI image for example</p>
<p>Thanks<br>
USMAN.</p>

---

## Post #9 by @lassoan (2018-03-05 23:15 UTC)

<p>This is an example for slice-by-slice processing: <a href="https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02">https://gist.github.com/lassoan/d85be45b7284a3b4e580688fccdb1d02</a>. It shows that you can extract a single slice of a volume using numpy indexing. You can apply the same technique for histogram computation: you don’t pass the entire 3D array to np.histogram but you extract a slice first. So, with 2-3 extra lines of code you can get per-slice histograms.</p>

---

## Post #10 by @Diana (2018-03-06 09:18 UTC)

<p>Hello,</p>
<p>thank you for your replies! I am still working on my data, and you have already helped a lot, but there are still some things I would like to improve. When I want to compare I need some statistics of course, so I used the SlicerRadiomics extension. However, it works only if I re-segment the T1 map (it does not allow me to use the segmantation from the 3D volume on the T1 map), which I do in some cases anyway, because T1 maps and 3D volumes are a little bit shifted. Anyway, there is one more thing I would like to do: to unify the intensities range within the segments from 0 to 4000. That is the most frequent range I get, however sometimes it is different. I can set the number of bins, but that means the bins have different thickness. Can you help me work this out?</p>

---

## Post #11 by @lassoan (2018-03-06 14:17 UTC)

<aside class="quote no-group" data-username="Diana" data-post="10" data-topic="2164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diana/48/3454_2.png" class="avatar"> Diana:</div>
<blockquote>
<p>When I want to compare I need some statistics of course, so I used the SlicerRadiomics extension. However, it works only if I re-segment the T1 map (it does not allow me to use the segmantation from the 3D volume on the T1 map)</p>
</blockquote>
</aside>
<p>You can export segmentation to a labelmap in Segmentations module, Import/Export section.</p>
<aside class="quote no-group" data-username="Diana" data-post="10" data-topic="2164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diana/48/3454_2.png" class="avatar"> Diana:</div>
<blockquote>
<p>unify the intensities range within the segments from 0 to 4000</p>
</blockquote>
</aside>
<p>To solve this, you can set bin range and width in numpy.histogram by <code>bins</code> and <code>range</code> parameters for all histograms, instead of relying on automatic bin generation.</p>

---

## Post #12 by @JoostJM (2018-03-06 17:05 UTC)

<p>Dear Diana,</p>
<p>What type of configuration are you using? On which version of slicer?<br>
In the the latest version of SlicerRadiomics, the mask correction is set to True by default (allowing you to re-use your segmentation).</p>
<p>If that is not the case, but you are able to provide a parameter file customization, you can also use it that way (by specifying a configuration file which has the setting “correctMask” set to true). See <a href="http://pyradiomics.readthedocs.io/en/latest/customization.html#parameter-file" rel="nofollow noopener">here</a> for more information on building a parameter file</p>

---

## Post #13 by @JoostJM (2018-03-06 17:08 UTC)

<p>Moreover, If you feed the image and segmentation to PyRadiomics, for histogram statistics, no discretization is applied (i.e. a bin width fixed to 1). Exception is uniformity and entropy, for that you’d need to set the bin width (default 25). Therefore, you would not need to unify your intensities.</p>
<p>example for a configuration file you can use (paste this in a text file and store with extension “.yml”):</p>
<pre><code class="lang-auto">settings:
  binWidth: 1
  correctMask: true

imageType:
  Original: {}

featureClass:
  firstorder:
</code></pre>

---

## Post #14 by @lassoan (2018-03-06 17:32 UTC)

<aside class="quote no-group" data-username="JoostJM" data-post="13" data-topic="2164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joostjm/48/1091_2.png" class="avatar"> JoostJM:</div>
<blockquote>
<p>no discretization is applied (i.e. a bin width fixed to 1)</p>
</blockquote>
</aside>
<p>Images may need smaller bin size (e.g., your entire scalar range may be between 0.0-1.0 if scalar type is float or double) or larger bin size (image is rescaled when loaded and there can be many intensity values that no voxel data is assigned to; so you could have large gaps, very noisy histogram if you use bin size = 1.0). So, in general, a fixed bin size of 1 is probably not an optimal choice.</p>

---

## Post #15 by @JoostJM (2018-03-07 09:11 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, you are correct. In that sense, mentioning bin width fixed to 1 is incorrect. In the actual code no discretization is applied, and it is therefore equivalent to calculating on a histogram with the number of bins equal to the number of unique gray values in the ROI. In fact, it just uses the values directly in calculating the features (it does not first make a histogram).</p>

---

## Post #16 by @Diana (2018-03-15 12:24 UTC)

<p>Hello, sorry for the belated reply. I am using the version 4.9. from the date 03.04. The reason why I think it does not work is that the relaxation map consists only of 3 slices, whereas the segmentation is from a 3d volume and it spatially exceeds the relaxation map. What I would like to do is to extract from the segmentation only the three slices, is it possible? So far, I resegmented the maps, but that is not ideal, because only the middle slice is segmented properly, the outer two are not (is it because there are no points above and below, so the algorithm “can’t grow” in these directions?) - I did not want the segmentation to exceed my ROI<br>
thank you for your replies</p>

---

## Post #17 by @lassoan (2018-03-16 00:10 UTC)

<aside class="quote no-group" data-username="Diana" data-post="16" data-topic="2164">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diana/48/3454_2.png" class="avatar"> Diana:</div>
<blockquote>
<p>What I would like to do is to extract from the segmentation only the three slices, is it possible?</p>
</blockquote>
</aside>
<p>When you export your segmentation to a labelmap (in Segmentations module, export section) then in the advanced section select your relaxation map as “Reference volume”. The exported labelmap will have exactly the same size, spacing, and direction as the relaxation map.</p>

---
