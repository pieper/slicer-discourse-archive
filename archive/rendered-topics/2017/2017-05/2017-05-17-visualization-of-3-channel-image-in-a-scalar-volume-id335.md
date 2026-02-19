---
topic_id: 335
title: "Visualization Of 3 Channel Image In A Scalar Volume"
date: 2017-05-17
url: https://discourse.slicer.org/t/335
---

# Visualization of 3 Channel image in a scalar volume

**Topic ID**: 335
**Date**: 2017-05-17
**URL**: https://discourse.slicer.org/t/visualization-of-3-channel-image-in-a-scalar-volume/335

---

## Post #1 by @samira (2017-05-17 19:54 UTC)

<p>Hi All,</p>
<p>I am currently writing a loadable module to generate a colormap and overlay it on top of a BMode image and I want to show the final image in the Slice view window.<br>
However, my final vtkImage has three channels the slicer shows it as a gray image.<br>
When I save the current scalar volume to a .jpg file is colored.<br>
The volume info of the volume shows it has 3 channels and scalar range is between 0 and 255.<br>
Do you have any idea how I can visualize the colored image in the Slicer?<br>
Here is my code to create the scalar volume:</p>
<pre><code>vtkSmartPointer&lt;vtkMRMLScalarVolumeNode&gt; colormapVol = vtkSmartPointer&lt;vtkMRMLScalarVolumeNode&gt;::New();

colormapVol = u_logic-&gt;ApplyColormap(InputNode);

this-&gt;GetMRMLScene()-&gt;AddNode(colormapVol.GetPointer());

vtkNew&lt;vtkMRMLScalarVolumeDisplayNode&gt; colormapDisplay;
this-&gt;GetMRMLScene()-&gt;AddNode(colormapDisplay.GetPointer());
colormapVol-&gt;SetAndObserveDisplayNodeID(colormapDisplay-&gt;GetID());
</code></pre>
<p>Thanks,<br>
Samira</p>

---

## Post #2 by @pieper (2017-05-18 16:53 UTC)

<p>If you want to do a color image you need to make a vtkMRMLVectorVolume node.</p>

---

## Post #3 by @samira (2017-05-18 22:17 UTC)

<p>That worked thank you.</p>

---
