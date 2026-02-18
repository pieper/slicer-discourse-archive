# Accessing VolumeNode in loadable

**Topic ID**: 25580
**Date**: 2022-10-06
**URL**: https://discourse.slicer.org/t/accessing-volumenode-in-loadable/25580

---

## Post #1 by @leo (2022-10-06 15:51 UTC)

<p>I am currently attempting to implement this <a href="https://discourse.slicer.org/t/tracking-cursor-movements-to-access-voxel-values/24568/7">Python script</a> in a loadable module in order to acces voxels. My attempts until node ended always with my custom module breaking. My understanding right now is that the way I try to acces the MRMLVolumeNode might by the issue.<br>
<code> vtkMRMLVolumeNode* inputVolumeNode;</code><br>
<code>vtkWeakPointer&lt;vtkMRMLCrosshairNode&gt; crosshairNode;</code><br>
<code>vtkGeneralTransform* transform_ras_to_volume_ras;</code><br>
<code>double  ras[4] = { 0,0,0 };</code><br>
<code>vtkMRMLScene* scene;</code><br>
<code>double  ijk_point[4] = { 0, 0, 0, 1 };</code><br>
<code>vtkMRMLVolumeNode* volumeNode = vtkMRMLVolumeNode::SafeDownCast(scene-&gt;GetFirstNodeByName("MRHead"));</code><br>
as my program seems to be breaking at this last step.<br>
I have had a look a different ways to acces the data like in this case using vtkImageData to acces <a href="https://discourse.slicer.org/t/access-image-pixel-values-in-loadable/904">voxels</a> but still it remains unclear to me how it is performed here using currentNode.</p>

---

## Post #2 by @lassoan (2022-10-06 19:12 UTC)

<p>Do you have a node by the name <code>MRHead</code> in the scene?</p>
<p>What is your overall goal?</p>
<p>Would you like to use C++ to do some expensive computations? If yes, then you don’t need to mess with crosshairs and with getting a node from scene in C++, etc. Just write the computation code in C++ and call that from Python. The Python code would take care of everything (getting the current volume node, cursor position, etc.) except the lengthy computation. Or, you can compute quickly in Python, by operating on arrays and not on individual voxels, or using libraries, such as VTK, ITK, numpy, …</p>

---

## Post #3 by @leo (2022-10-10 15:46 UTC)

<p>Thankyou,  for your reply. Indeed I have a Volume by the name of MRHead in the scene. I would need to get the voxel values  at the mouse positions since I need to perform computation based on their Gray scale values and this would need to happen in a fast running loop. Have you got any recommendations for resources or different paths to take?</p>

---
