# How to get pixel value and coordinate from nrrd file

**Topic ID**: 7030
**Date**: 2019-06-04
**URL**: https://discourse.slicer.org/t/how-to-get-pixel-value-and-coordinate-from-nrrd-file/7030

---

## Post #1 by @kscript (2019-06-04 23:36 UTC)

<p>So I make nrrd file. In this file has Annotation Data using 3D Slicer.</p>
<p>I want to get pixel coordinate and pixel value from this file.</p>
<p>I modified the code with reference to the source of this link, but I did not get any results.</p>
<p><a href="https://stackoverflow.com/questions/39687295/python-dicom-getting-pixel-value-from-dicom-file" rel="nofollow noopener">python dicom – getting pixel value from dicom file</a></p>
<p>I really couldn’t find any information so any helpful resources would be appreciated as well. Thank you.</p>

---

## Post #2 by @lassoan (2019-06-05 01:26 UTC)

<p>These examples in the script repository should help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_markup_fiducial_RAS_coordinates_from_volume_voxel_coordinates</a></p>

---

## Post #3 by @kscript (2019-06-05 02:41 UTC)

<p>Thanks reply.</p>
<p>This code need to use python interaction in 3D Slicer. Right??</p>

---

## Post #4 by @lassoan (2019-06-05 02:55 UTC)

<aside class="quote no-group" data-username="kscript" data-post="3" data-topic="7030">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ec9cab/48.png" class="avatar"> kscript:</div>
<blockquote>
<p>This code need to use python interaction in 3D Slicer. Right??</p>
</blockquote>
</aside>
<p>You need to run the code in Slicer’s Python environment. You probably don’t need to show Slicer GUI - you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_run_slicer_operations_from_a_batch_script.3F">run your script from the command-line</a>.</p>

---

## Post #5 by @kscript (2019-06-05 03:15 UTC)

<p>Oh I can see array!</p>
<p>And i want to know each array’s all information.</p>
<p>now we can see like this.<br>
[[[0 0 0 …, 0 0 0]<br>
[0 0 0 …, 0 0 0]<br>
[0 0 0 …, 0 0 0]</p>
<p>i want to remove … this part and i want to print all arrya elements.</p>
<p>and  i save result to txt file. but result is same.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/238b1c2919ac499c1c36ae4ca44cb223cee58d84.png" data-download-href="/uploads/short-url/54qKHzvGxjrWPpaQZpEEOGCMPDC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/238b1c2919ac499c1c36ae4ca44cb223cee58d84.png" alt="image" data-base62-sha1="54qKHzvGxjrWPpaQZpEEOGCMPDC" width="690" height="396" data-dominant-color="FBFDFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">719×413 5.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2019-06-05 14:01 UTC)

<p>Writing out 3D volume to text file is a bad idea (large file, slow to read/write, potential data loss due to limited precision), but here is a complete example just to show how easy it is to do:</p>
<pre><code class="lang-auto"># Get some image data
import SampleData
volumeNode=SampleData.SampleDataLogic().downloadMRHead()

# Get voxels as numpy array
volumeArray=slicer.util.arrayFromVolume(volumeNode)

# Write voxels to text file
import numpy as np
with file('c:/tmp/test.txt', 'w') as outfile:
  for data_slice in volumeArray:
    np.savetxt(outfile, data_slice, fmt='%-7.2f')
</code></pre>
<p>If you want to write in a different format then search for Python code examples on the web.</p>

---
