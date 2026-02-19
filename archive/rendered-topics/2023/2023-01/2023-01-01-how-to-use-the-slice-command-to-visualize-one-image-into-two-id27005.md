---
topic_id: 27005
title: "How To Use The Slice Command To Visualize One Image Into Two"
date: 2023-01-01
url: https://discourse.slicer.org/t/27005
---

# How to use the slice command to visualize one image into two intersecting planes?

**Topic ID**: 27005
**Date**: 2023-01-01
**URL**: https://discourse.slicer.org/t/how-to-use-the-slice-command-to-visualize-one-image-into-two-intersecting-planes/27005

---

## Post #1 by @Yousef_Abohamra (2023-01-01 18:06 UTC)

<p>Hi, I need to visualize one image in two intersecting planes. The attached picture shows an example of what I want to do. However, it uses an equation (V = X.*exp(-X.^2-Y.^2-Z.^2)<img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> while I want to insert my image instead.</p>
<p>[X,Y,Z] = meshgrid(-2:.2:2);</p>
<p>V = X.*exp(-X.^2-Y.^2-Z.^2);</p>
<p>xslice = 0;</p>
<p>yslice = <span class="chcklst-box fa fa-square-o fa-fw"></span>;</p>
<p>zslice = 0;</p>
<p>slice(X,Y,Z,V,xslice,yslice,zslice)<br>
I’m using MATLAB but if it is easier to do it using 3D slice or any other software that will be fine for me.</p>
<p>Operating system:Windows<br>
Slicer version:I di not download it<br>
Expected behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8f8e67f3d4b32b4272d4a52abd723c4458fabbe.png" data-download-href="/uploads/short-url/sFSLa6jotHhYCUE6Nu8JOBuS3ts.png?dl=1" title="112" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8f8e67f3d4b32b4272d4a52abd723c4458fabbe_2_690x343.png" alt="112" data-base62-sha1="sFSLa6jotHhYCUE6Nu8JOBuS3ts" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8f8e67f3d4b32b4272d4a52abd723c4458fabbe_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8f8e67f3d4b32b4272d4a52abd723c4458fabbe_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8f8e67f3d4b32b4272d4a52abd723c4458fabbe_2_1380x686.png 2x" data-dominant-color="C4E6E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">112</span><span class="informations">1920×955 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Actual behavior:</p>

---

## Post #2 by @lassoan (2023-01-03 03:21 UTC)

<p>You can fill an array based on a 3D function in Python very similar as in Matlab, and then you can visualize the volume in Slicer by a few more additional lines:</p>
<pre data-code-wrap="python"><code class="lang-python"># Create 3D array V containing 3D function value
import numpy as np
X, Y, Z = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.2))
V = -X**2-Y**2-Z**2

# Create a Slicer volume node form the numpy array
volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
slicer.util.updateVolumeFromArray(volumeNode, V)

# Adjust visualization options
# Set color table to Viridis
volumeNode.CreateDefaultDisplayNodes()
volumeNode.GetDisplayNode().SetAndObserveColorNodeID('vtkMRMLColorTableNodeFileViridis.txt')
# Show volume in slice views
slicer.util.setSliceViewerLayers(background=volumeNode)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/401f798023c2ac3004763baee9554ff6c963851e.png" data-download-href="/uploads/short-url/99fZvPOsumQnTsRbsDxbWpA2Km2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/401f798023c2ac3004763baee9554ff6c963851e_2_690x485.png" alt="image" data-base62-sha1="99fZvPOsumQnTsRbsDxbWpA2Km2" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/401f798023c2ac3004763baee9554ff6c963851e_2_690x485.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/401f798023c2ac3004763baee9554ff6c963851e_2_1035x727.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/401f798023c2ac3004763baee9554ff6c963851e_2_1380x970.png 2x" data-dominant-color="537B5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1480×1042 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Yousef_Abohamra (2023-01-04 01:57 UTC)

<p>Thank you, Andras.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28fbc17619a3f0e9c995cb7b669fc16c32bb8c65.png" data-download-href="/uploads/short-url/5QytWp1XpH2HhQoWHF8SHphoCZn.png?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28fbc17619a3f0e9c995cb7b669fc16c32bb8c65_2_408x499.png" alt="12" data-base62-sha1="5QytWp1XpH2HhQoWHF8SHphoCZn" width="408" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28fbc17619a3f0e9c995cb7b669fc16c32bb8c65_2_408x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28fbc17619a3f0e9c995cb7b669fc16c32bb8c65_2_612x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28fbc17619a3f0e9c995cb7b669fc16c32bb8c65.png 2x" data-dominant-color="E4DFE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">660×807 68.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to use images instead of the plane equation. Please have a look at the attached picture.</p>

---
