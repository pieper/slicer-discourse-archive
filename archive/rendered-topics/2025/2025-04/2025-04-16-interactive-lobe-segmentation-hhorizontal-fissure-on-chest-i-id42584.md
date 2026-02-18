# Interactive Lobe Segmentation hhorizontal fissure on Chest Imaging Platform

**Topic ID**: 42584
**Date**: 2025-04-16
**URL**: https://discourse.slicer.org/t/interactive-lobe-segmentation-hhorizontal-fissure-on-chest-imaging-platform/42584

---

## Post #1 by @Devanish (2025-04-16 11:50 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.6.2<br>
Expected behavior:</p>
<p>Trying to use Interactive Lung Segmentation of Chest Imaging Platform. Placed fiducials as suggested here:</p><aside class="onebox pdf" data-onebox-src="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf">
  <header class="source">

      <a href="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf" target="_blank" rel="noopener nofollow ugc">chestimagingplatform.org</a>
  </header>

  <article class="onebox-body">
    <a href="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf" target="_blank" rel="noopener nofollow ugc"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://chestimagingplatform.org/files/chestimagingplatform/files/interactivelobesegmentation_tutorial_pn.pdf" target="_blank" rel="noopener nofollow ugc">interactivelobesegmentation_tutorial_pn.pdf</a></h3>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It seemed to work fine 2 weeks ago.</p>
<p>Actual behavior:</p>
<p>But on 2 other CTs I have tried, it gives me completely horizontal fissures.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61fb6434b7180bb1d2fe0b6830bbf8ed36758e79.jpeg" data-download-href="/uploads/short-url/dYMUVTuOVxwJD18bOSI4g5Tdhwd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61fb6434b7180bb1d2fe0b6830bbf8ed36758e79_2_690x179.jpeg" alt="image" data-base62-sha1="dYMUVTuOVxwJD18bOSI4g5Tdhwd" width="690" height="179" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61fb6434b7180bb1d2fe0b6830bbf8ed36758e79_2_690x179.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61fb6434b7180bb1d2fe0b6830bbf8ed36758e79_2_1035x268.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61fb6434b7180bb1d2fe0b6830bbf8ed36758e79.jpeg 2x" data-dominant-color="6C6C67"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×323 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Which are inaccurate.</p>
<p>This is the log:</p>
<pre><code class="lang-auto">[Qt] When loading module "ParticlesDisplay" , the dependency "TractographyDisplay" failed to be loaded.

[Qt] vtkMRMLScalarVolumeNode does not have a LabelMap attribute anymore. Update your code according to https://www.slicer.org/w/index.php/Documentation/Labs/Segmentations#Module_update_instructions

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] vtkMRMLMarkupsNode::SetNthControlPointLabel failed: control point 0 does not exist

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] vtkMRMLMarkupsNode::SetNthControlPointLabel failed: control point 0 does not exist

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsNode.h, line 776

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsNode::RemoveMarkup method is deprecated, please use RemoveNthControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621570): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67623520): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] vtkMRMLMarkupsNode::SetNthControlPointLabel failed: control point 0 does not exist

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 185

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 106

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (0000022C67621A50): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] GetItemByDataNode: Invalid data node to find

[VTK] ItemModified: Invalid item ID given
</code></pre>
<p>Am I doing something wrong? Or the module itself is broken?</p>
<p>Thank you</p>

---
