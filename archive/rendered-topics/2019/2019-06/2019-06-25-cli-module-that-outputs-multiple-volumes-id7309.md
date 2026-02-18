# CLI module that outputs multiple volumes

**Topic ID**: 7309
**Date**: 2019-06-25
**URL**: https://discourse.slicer.org/t/cli-module-that-outputs-multiple-volumes/7309

---

## Post #1 by @kmanduca (2019-06-25 22:42 UTC)

<p>Operating system: linux<br>
Slicer version: 4.10.1<br>
Expected behavior: create 3 volumes from a CLI module<br>
Actual behavior: Slicer crashes</p>
<p>We’re trying to create a CLI module that reads from a directory of dicom files and outputs a DWI volume, a scalar volume, and a label map volume for the data set. The module loads and runs without error, but Slicer crashes after the module finishes before displaying any of the volumes.</p>
<p>Initially, we tried this with the CLI taking the directory as input and returning a single scalar volume, which worked as expected.</p>
<p>How can we create three volumes, including display properties for each, and return them from a CLI module?</p>
<p>Our XML definition file looks like:<br>
&lt;?xml version="1.0" encoding="utf-8"?&gt;<br>
<br>
phantom<br>
phantom_cli<br>
<br>
<a href="http://www.example.com/Slicer/Modules/phantom_cli" rel="nofollow noopener">http://www.example.com/Slicer/Modules/phantom_cli</a><br>
Slicer<br>
…<br>
…<br>
<br>
IO<br>
<br>
<br>
inputDir<br>
Input Directory<br>
input<br>
0<br>
<br>
<br>
<br>
outputDWIVolume<br>
Output DWI Volume<br>
output<br>
1<br>
<br>
<br>
<br>
outputVolume<br>
Output Scalar Volume<br>
output<br>
2<br>
<br>
<br>
<br>
outputVOIVolume<br>
Output Label Map Volume<br>
output<br>
3<br>
<br>
<br>
<br>
</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2019-06-26 02:25 UTC)

<p>Most likely one of the volumes is invalid. If I remember correctly, an invalid DWI volume can force Slicer to crash, so I would have a closer look at that first.</p>
<p>Enable “Developer mode” in Slicer application settings to make Slicer keep CLI input and output files (normally they are deleted when CLI execution is completed) and check if you can make Slicer crash by loading them manually (using menu: File / Add data).</p>

---

## Post #3 by @kmanduca (2019-06-27 20:39 UTC)

<p>Thanks for the reply, I’ve been looking specifically at the DWI volume:</p>
<p>If you open Slicer and run the CLI it runs without error, but displays this line several times before Slicer crashes:</p>
<pre><code>Input port 0 of algorithm vtkImageExtractComponents(0x8fdd970) has 0 connections but is not optional.
</code></pre>
<p>If you then restart Slicer and load the DWI volume through ‘Add data’ it loads without error, but if you try to show it in the 3D display it does this (without crashing):</p>
<pre><code>Failed to determine texture parameters. IF=0 F=6407 T=5121
</code></pre>
<p>The other nodes (Scalar and Label Map) both load without error and display normally. If you’ve been using Slicer with other modules, and then try to run the CLI it doesn’t crash and displays the Scalar Volume and the Label Map Volume, but when you try to display the DWI Volume it doesn’t update the display.</p>
<p>Our python code creating the DWI reads:</p>
<blockquote>
<pre><code>dwi_out = slicer.vtkMRMLNRRDStorageNode()
dwi_out.SetFileName(args.outputDWIVolume) 

dwi_node =  mrml.vtkMRMLDiffusionWeightedVolumeNode()
slicer.util.updateVolumeFromArray(dwi_node, dwi_array)      # dwi_array is created elsewhere and has shape 

# Update RAS matrix
ijktoras = vtk.vtkMatrix4x4()
ijktoras.SetElement(2,2,-1)
dwi_node.SetIJKToRASMatrix(ijktoras)

# Update origin and spacing
origin = (cs.pixel_x0_left_cm * -10, cs.pixel_y0_posterior_cm * -10, cs.min_superior_cm * -10)
spacing = (cs.pixel_spacing_cm * 10, cs.pixel_spacing_cm * 10, cs.spacing_between_slices_cm * 10)
dwi_node.SetOrigin(origin)
dwi_node.SetSpacing(spacing)

dwi_node.Modified()
dwi_out.WriteData(dwi_node)
</code></pre>
</blockquote>
<p>The scalar volume and label map are created with identical calls (except the type of volume node). Are we missing something in creating the DWI volume?</p>

---

## Post #4 by @lassoan (2019-06-28 22:28 UTC)

<p>DWI volume is much harder to create correctly. I would suggest to compare the file that you create to the DWI volume in SampleData module and make sure they are in the exact same format.</p>

---
