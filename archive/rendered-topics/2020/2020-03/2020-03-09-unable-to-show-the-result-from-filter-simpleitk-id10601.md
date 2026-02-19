---
topic_id: 10601
title: "Unable To Show The Result From Filter Simpleitk"
date: 2020-03-09
url: https://discourse.slicer.org/t/10601
---

# Unable to show the result from filter - SimpleITK

**Topic ID**: 10601
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/unable-to-show-the-result-from-filter-simpleitk/10601

---

## Post #1 by @siaeleni (2020-03-09 15:59 UTC)

<p>Hello,<br>
What I am trying to achieve is to apply BinaryMorphologicalOpeningImageFilter to a vtkMRMLModelNode.</p>
<p>These are the steps that I follow:</p>
<ol>
<li>Add the stl model as Segmentation into Slicer</li>
<li>Convert Segmentation into vtkMRMLLabelMapVolumeNode and then into vtkMRMLScalarVolumeNode</li>
<li>Apply the filter to the Volume</li>
</ol>
<blockquote>
<p>import SimpleITK as sitk<br>
import sitkUtils as su</p>
<p>seg = slicer.util.getNode(‘segm’)<br>
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’,‘LabelMap’)<br>
outputvolumenode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLScalarVolumeNode”, ‘OutputVolume’)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(seg, labelmapVolumeNode)<br>
sef = slicer.modules.volumes.logic().CreateScalarVolumeFromVolume(slicer.mrmlScene,outputvolumenode, labelmapVolumeNode)</p>
<p>filter = sitk.BinaryMorphologicalOpeningImageFilter()<br>
filter.SetKernelRadius((1,1,1))<br>
su.PullVolumeFromSlicer(outputvolumenode)<br>
result = filter.Execute(im)</p>
</blockquote>
<p>But I am not sure how should I display the result into a vtkMRMLModelNode to Slicer and verify that the filter is working.<br>
Thanks</p>

---

## Post #2 by @pieper (2020-03-09 18:51 UTC)

<p>Hi <a class="mention" href="/u/siaeleni">@siaeleni</a> -</p>
<p>It looks like you missing the conversion of the slicer volume to a simpleitk image - this code should help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK</a></p>
<pre><code class="lang-auto"># Run processing
inputImage = sitkUtils.PullVolumeFromSlicer(inputVolumeNode)
filter = sitk.SignedMaurerDistanceMapImageFilter()
outputImage = filter.Execute(inputImage)
sitkUtils.PushVolumeToSlicer(outputImage, outputVolumeNode)
</code></pre>

---
