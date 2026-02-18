# Segment Editor Causes Freeze

**Topic ID**: 32821
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/segment-editor-causes-freeze/32821

---

## Post #1 by @KiraKiralina (2023-11-14 20:26 UTC)

<p>Hi all,</p>
<p>3D Slicer keeps throwing this error when I load it up. Once it does, it acts normally until I try to edit a segment, and then it freezes on me. I’ve tried everything I can think of to fix this and can’t.</p>
<p>The only thing I can think of is that I’m using a file made with an older version of Slicer. The computer I’m on is more than capable of handling a file of the size I’m using. I’ve tried redownloading files, restarting the computer, and making a new file. The new file never causes any problems, but I’d rather not lose all my work to this point.</p>
<p>Does anyone have any idea what’s going on?</p>
<pre><code class="lang-auto">- Error: Loading C:/Users/923653585/Downloads/Old Octo Brain/Old Unzipped Octo Brain/Old Current Octo Brain/2023-10-31-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLScalarVolumeNode (00000217D7E2FFA0): vtkMRMLStorableNode::UpdateScene failed: Failed to read node dual-stain_bimac_PTAIKI_36kV_6um_2k__rec0276_2 (vtkMRMLScalarVolumeNode3) using storage node vtkMRMLVolumeArchetypeStorageNode3.

- Error: Loading C:/Users/923653585/Downloads/Old Octo Brain/Old Unzipped Octo Brain/Old Current Octo Brain/2023-10-31-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLScalarVolumeNode (00000217D7E2A570): vtkMRMLStorableNode::UpdateScene failed: Failed to read node dual-stain_bimac_PTAIKI_36kV_6um_2k__rec0276_3 (vtkMRMLScalarVolumeNode6) using storage node vtkMRMLVolumeArchetypeStorageNode7.

- Error: Loading C:/Users/923653585/Downloads/Old Octo Brain/Old Unzipped Octo Brain/Old Current Octo Brain/2023-10-31-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLLinearTransformNode (00000217DC88D1C0): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Transform_DualStain_PTAIKI_1_1 (vtkMRMLLinearTransformNode8) using storage node vtkMRMLTransformStorageNode5.

- Error: Loading C:/Users/923653585/Downloads/Old Octo Brain/Old Unzipped Octo Brain/Old Current Octo Brain/2023-10-31-Scene.mrml - ERROR: In vtkMRMLStorableNode.cxx, line 326

vtkMRMLLinearTransformNode (00000217DC88E840): vtkMRMLStorableNode::UpdateScene failed: Failed to read node Transform_DualStain_PTAIKI_1_2 (vtkMRMLLinearTransformNode9) using storage node vtkMRMLTransformStorageNode6.
</code></pre>

---

## Post #2 by @lassoan (2023-11-14 20:29 UTC)

<p>We try to keep backward compatibility with older scenes, but if the scene was created by an application several major versions behind then you may need to load with an older Slicer version and save the scene again to update the scene file. However, it may be easier to just unzip the scene file and load the data objects (images, transforms, etc.) in the latest Slicer version.</p>

---

## Post #3 by @KiraKiralina (2023-11-16 17:06 UTC)

<p>That seems to have fixed it! Thank you so much!</p>

---
