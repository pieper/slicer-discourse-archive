# How to enable/disable the option of "interpolated cropped" inside "cropvolume" via python coding?

**Topic ID**: 32128
**Date**: 2023-10-10
**URL**: https://discourse.slicer.org/t/how-to-enable-disable-the-option-of-interpolated-cropped-inside-cropvolume-via-python-coding/32128

---

## Post #1 by @aiden.zhu (2023-10-10 05:18 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11<br>
Expected behavior:  would like to control enable/disable the option of “interpolated cropped”<br>
Actual behavior:</p>
<p>I am doing cropping volumes via python coding, use the following code to reach “cropvolume” ==&gt;<br>
cropVolumeNode = slicer.vtkMRMLCropVolumeParametersNode()<br>
cropVolumeNode.SetScene(slicer.mrmlScene)<br>
cropVolumeNode.SetIsotropicResampling(True)<br>
cropVolumeNode.SetSpacingScalingConst(1.0)<br>
slicer.mrmlScene.AddNode(cropVolumeNode)<br>
cropVolumeNode.SetName(‘NewlyCropped’)</p>
<p>so here how disable/enable the interpolation option for the cropvolume?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2023-10-10 10:41 UTC)

<p>You can get the list of all available parameters as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#get-list-of-parameter-names">here</a>.</p>

---

## Post #3 by @aiden.zhu (2025-09-11 13:36 UTC)

<p>Still get some issues with cropvolume while applying it via python-coding.</p>
<p>So what’s the best way or is there a quick way for users to check some ENUM or dictionary values? For example here, self.cropVolumeParametersNode.SetInterpolationMode(v_interpolation)</p>
<p>v_interpolation might be 0, 1, 2, 3, 4</p>
<p>How/where to check what interpolate-method each value represents? Say, here</p>
<p>value of 1 means “nearest neighbor” or “linear”?</p>
<p>Thanks a lot.</p>

---

## Post #4 by @aiden.zhu (2025-09-26 14:53 UTC)

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/CropVolume/MRML/vtkMRMLCropVolumeParametersNode.h">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/CropVolume/MRML/vtkMRMLCropVolumeParametersNode.h" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/CropVolume/MRML/vtkMRMLCropVolumeParametersNode.h" target="_blank" rel="noopener nofollow ugc">Modules/Loadable/CropVolume/MRML/vtkMRMLCropVolumeParametersNode.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/CropVolume/MRML/vtkMRMLCropVolumeParametersNode.h" rel="noopener nofollow ugc"><code>main</code></a>
</div>


      <pre><code class="lang-h">/*=auto=========================================================================

  Portions (c) Copyright 2005 Brigham and Women's Hospital (BWH) All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

=========================================================================auto=*/
// .NAME vtkMRMLVolumeRenderingParametersNode - MRML node for storing a slice through RAS space
// .SECTION Description
// This node stores the information about the currently selected volume
//
//

#ifndef __vtkMRMLCropVolumeParametersNode_h
#define __vtkMRMLCropVolumeParametersNode_h

#include "vtkMRML.h"
#include "vtkMRMLScene.h"
#include "vtkMRMLNode.h"
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/CropVolume/MRML/vtkMRMLCropVolumeParametersNode.h" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>public:<br>
enum<br>
{<br>
InterpolationNearestNeighbor = 1,<br>
InterpolationLinear = 2,<br>
InterpolationWindowedSinc = 3,<br>
InterpolationBSpline = 4<br>
};</p>
<p>enum<br>
{<br>
FitROIAlignToVolume = 0,   ///&lt; Before resizing the ROI, ROI orientation is adjusted to align with the axes of the input volume<br>
FitROIAlignToWorld = 1,    ///&lt; Before resizing the ROI, ROI orientation is adjusted to align with the world coordinate system axes<br>
FitROIKeepOrientation = 2, ///&lt; The ROI orientation is not modified during fitting<br>
FitROI_Last                ///&lt; PositionStatus_Last: indicates the end of the enum (int first = 0, int last = FitROI_Last)<br>
};</p>

---
