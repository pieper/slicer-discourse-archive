# 3D Slicer show nrrd file

**Topic ID**: 30334
**Date**: 2023-07-01
**URL**: https://discourse.slicer.org/t/3d-slicer-show-nrrd-file/30334

---

## Post #1 by @mazurkin.daniel (2023-07-01 10:18 UTC)

<p>Hello! I’m rewriting the DICOMWebBrowser extension to display a model from VolumeRendering with a selected study when starting 3D Slicer from console. How can I achieve this display? Currently, an MRMLNode is added, but I have to press a display button (I’ve attached a screenshot). How can I make it so that I don’t have to press the display button? I’ve attached the source code.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/262955c89a7d7abe3986342e968c1a6124d101a8.png" data-download-href="/uploads/short-url/5rAHDNXCyaMyp2WYTo9baMPnDPW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262955c89a7d7abe3986342e968c1a6124d101a8_2_690x73.png" alt="image" data-base62-sha1="5rAHDNXCyaMyp2WYTo9baMPnDPW" width="690" height="73" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262955c89a7d7abe3986342e968c1a6124d101a8_2_690x73.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/262955c89a7d7abe3986342e968c1a6124d101a8_2_1035x109.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/262955c89a7d7abe3986342e968c1a6124d101a8.png 2x" data-dominant-color="E9EAED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1102×117 5.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
MySourceCode for this task:</p>
<pre><code class="lang-auto">import slicer

logic = slicer.modules.volumerendering.logic()

scene = slicer.mrmlScene

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', 'VolumeTest_1')

slicer.util.loadVolume('/home/danil/Документы/SlicerDICOMDatabase/DICOMwebLocal/7867c209a99ade387bac05b4999d78cd/1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.729.0.2TSE5512512.nrrd', {'name': 'VolumeTest_1'})

slicer.mrmlScene.AddNode(volumeNode)

displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(logic)
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
</code></pre>
<p>import slicer</p>
<p>logic = slicer.modules.volumerendering.logic()</p>
<p>scene = slicer.mrmlScene</p>
<p>volumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’, ‘VolumeTest_1’)</p>
<p>slicer.util.loadVolume(‘/home/danil/Документы/SlicerDICOMDatabase/DICOMwebLocal/7867c209a99ade387bac05b4999d78cd/1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.729.0.2TSE5512512.nrrd’, {‘name’: ‘VolumeTest_1’})</p>
<p>slicer.mrmlScene.AddNode(volumeNode)</p>
<p>displayNode = logic.CreateVolumeRenderingDisplayNode()<br>
displayNode.UnRegister(logic)<br>
slicer.mrmlScene.AddNode(displayNode)<br>
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())<br>
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)</p>
<pre><code class="lang-auto"></code></pre>

---

## Post #2 by @mazurkin (2023-07-03 07:30 UTC)

<p>Make with help VolumeNode from module “Data” with help <a href="https://slicer.readthedocs.io/en/v4.11/developer_guide/modules/volumerendering.html" class="inline-onebox" rel="noopener nofollow ugc">Volume rendering — 3D Slicer documentation</a></p>

---

## Post #3 by @mazurkin.daniel (2023-07-03 08:24 UTC)

<p>Help this source code:</p>
<pre><code class="lang-auto">data_display = slicer.util.loadVolume('/home/danil/test_dicom/1.nrrd')
logic = slicer.modules.volumerendering.logic()
volumeNode = slicer.mrmlScene.GetNodeByID(data_display.GetID())
displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(logic)
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
</code></pre>

---
