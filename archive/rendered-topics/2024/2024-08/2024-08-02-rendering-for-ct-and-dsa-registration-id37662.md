---
topic_id: 37662
title: "Rendering For Ct And Dsa Registration"
date: 2024-08-02
url: https://discourse.slicer.org/t/37662
---

# Rendering for CT and dsa registration

**Topic ID**: 37662
**Date**: 2024-08-02
**URL**: https://discourse.slicer.org/t/rendering-for-ct-and-dsa-registration/37662

---

## Post #1 by @fqzhice (2024-08-02 07:09 UTC)

<p>I made registration from CT to DSA, The right-top image is generated after DRR projection.</p>
<p>i want to paint drr image on VR window, Also DSA video is on background layer. The user can move or rotate drr projected image manually.</p>
<pre><code class="lang-auto">// load projected image and convert vector to scalar volume node, 
// refer to vectortoscalar module
movedImage = "C:/PilotImage/Release/Slicer-build/bin/Release/bone.png";
QString cmd = QString(
"import vtk,slicer\n"
"inputVolumeNode=slicer.util.loadVolume('%1')\n"
"outputVolumeNode=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')\n"
"ijkToRAS = vtk.vtkMatrix4x4()\n"
"inputVolumeNode.GetIJKToRASMatrix(ijkToRAS)\n"
"outputVolumeNode.SetIJKToRASMatrix(ijkToRAS)\n"
"extract=vtk.vtkImageExtractComponents()\n"
"extract.SetInputConnection(inputVolumeNode.GetImageDataConnection())\n"
"extract.SetComponents(0, 1, 2)\n"
"luminance=vtk.vtkImageLuminance()\n"
"luminance.SetInputConnection(extract.GetOutputPort())\n"
"luminance.Update()\n"
"outputVolumeNode.SetImageDataConnection(luminance.GetOutputPort())\n"
"outputVolumeNode.CreateDefaultDisplayNodes()\n"
"outputVolumeNode.SetName('BoneProjected')\n"
"displayNode=outputVolumeNode.GetVolumeDisplayNode()\n"
"displayNode.SetAndObserveColorNodeID('vtkMRMLColorTableNodeYellow')\n"
"slicer.mrmlScene.AddDefaultNode(displayNode)\n").arg(movedImage);
qSlicerPythonManager* pythonManager = qSlicerApplication::application()-&gt;pythonManager();
pythonManager-&gt;executeString(cmd);

//render projected image
vtkMRMLScalarVolumeNode* projecedNode =  vtkMRMLScalarVolumeNode::SafeDownCast(
    d-&gt;scene-&gt;GetFirstNodeByName("BoneProjected"));
vtkImageData* imageData = projecedNode-&gt;GetImageData();
vtkImageActor* image_actor = vtkImageActor::New();
image_actor-&gt;SetInputData(imageData);
auto threeDWidget = qSlicerApplication::application()-&gt;layoutManager()-&gt;threeDWidget(0);
auto view = threeDWidget-&gt;threeDView();
vtkRenderer* foregroundRenderer = vtkRenderer::New();
foregroundRenderer-&gt;InteractiveOff();
foregroundRenderer-&gt;AddActor(image_actor);
foregroundRenderer-&gt;SetLayer(1);
vtkRenderWindow* renderWindow = view-&gt;renderWindow();
renderWindow-&gt;AddRenderer(foregroundRenderer);
return;
</code></pre>
<p>Result is as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c29086c15d6d66bf09f3456d7d3e0b82f10b682.jpeg" data-download-href="/uploads/short-url/6iEV7p2Wmd9hHRyTAjD03u9ayfo.jpeg?dl=1" title="20240802151430" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c29086c15d6d66bf09f3456d7d3e0b82f10b682_2_690x379.jpeg" alt="20240802151430" data-base62-sha1="6iEV7p2Wmd9hHRyTAjD03u9ayfo" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c29086c15d6d66bf09f3456d7d3e0b82f10b682_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c29086c15d6d66bf09f3456d7d3e0b82f10b682_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c29086c15d6d66bf09f3456d7d3e0b82f10b682_2_1380x758.jpeg 2x" data-dominant-color="39383A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240802151430</span><span class="informations">1467×806 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can i display the drr image correctly with suitable color and direction.</p>

---

## Post #3 by @fqzhice (2024-08-02 08:53 UTC)

<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>redSliceNode = slicer.mrmlScene.GetNodeByID(‘vtkMRMLSliceNodeRed’)\n</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td>redSliceNode.SetSliceVisible(True)\n</td>
</tr>
<tr>
<td></td>
<td>redSliceNode.AddThreeDViewID(‘vtkMRMLViewNode1’)\n</td>
</tr>
</tbody>
</table>
</div><p>I fixed it by this</p>

---
