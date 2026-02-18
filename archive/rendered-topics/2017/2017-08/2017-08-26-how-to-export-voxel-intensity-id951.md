# How to export voxel intensity

**Topic ID**: 951
**Date**: 2017-08-26
**URL**: https://discourse.slicer.org/t/how-to-export-voxel-intensity/951

---

## Post #1 by @happyle123456 (2017-08-26 02:49 UTC)

<p>Operating system:windows 7<br>
Slicer version:both slicer 4.6 and 4.7<br>
I made a segmentation and clip a volume with module,then how can i get the intensity value of each voxel list in a spreadsheet?the coordinate is not necessary.thanks</p>

---

## Post #2 by @lassoan (2017-08-26 03:03 UTC)

<p>Probably Segment statistics module provides this information. If not, then please describe in more detail what exactly you would need.</p>

---

## Post #3 by @happyle123456 (2017-08-26 03:22 UTC)

<p>I need the data of every voxel which have been shown at data probe,just simply a list of voxel value,coordinate included is fine,but not the statistical parametre of them.<br>
maybe it would be like:<br>
x,y,z,value<br>
…<br>
…<br>
…</p>

---

## Post #4 by @lassoan (2017-08-26 04:26 UTC)

<p>Probably the simplest would be to get the volume as a numpy array and then write out the voxel indices and values you are interested in. Something like this (this outputs all voxels that has value &gt;260):</p>
<pre>
import numpy as np
voxelArray = slicer.util.arrayFromVolume(getNode('MRHead'))
indices = np.where(voxelArray&gt;260)
numberOfVoxels = len(indices[0])
for pointIndex in range(numberOfVoxels):
  i = indices[0][pointIndex]
  j = indices[1][pointIndex]
  k = indices[2][pointIndex]
  print("%d %d %d %d" % (i, j, k, voxelArray[i,j,k]))
</pre>
<p>See some more examples in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume</a></p>
<p>If you need physical (RAS) coordinates instead of voxel coordinates (IJK) then you have to multiply the (x,y,z,1) vector from the left with the volume’s IJKToRAS matrix.</p>

---

## Post #5 by @happyle123456 (2017-08-26 06:58 UTC)

<p>it’s awesome,thank you very much,it’a great help:smiley:<img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=5" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #6 by @CostasP (2019-03-12 15:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="951">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you need physical (RAS) coordinates instead of voxel coordinates (IJK) then you have to multiply the (x,y,z,1) vector from the left with the volume’s IJKToRAS matrix.</p>
</blockquote>
</aside>
<p>I still try to convert ijk to LPS? Is it possible to provide an example for the vector multiplication? Thanks in advance</p>

---

## Post #7 by @lassoan (2019-03-13 13:43 UTC)

<p>Search for “ijktoras.multiplypoint” in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">Slicer script repository</a> for examples.</p>

---

## Post #8 by @lassoan (2020-04-23 23:57 UTC)

<p>A post was split to a new topic: <a href="/t/get-image-intensity-histogram-of-a-segment/11277">Get image intensity histogram of a segment</a></p>

---

## Post #9 by @Saima (2020-05-01 08:38 UTC)

<p>Hi Andras,<br>
I used the arrayfromvolume to get the voxel intensities for an mri. but when i use the same mri to get the voxel intensities outside slicer using python and reading nrrd file I get different intensities.</p>
<p>Do you have any idea why its happening?</p>
<p>thank you</p>
<p>Regards,<br>
Saima safdar</p>

---

## Post #10 by @lassoan (2020-05-01 13:56 UTC)

<p>NRRD file format is very simple, so it is unlikely that different values are decoded from the file. Probably you just read the value from a different location. There are two conventions for voxel indexing (IJK vs. KJI), so try reversing order of voxel coordinates. Also note that internally Slicer uses RAS physical coordinate system, while LPS coordinate system is used in files, so if you want to use physical coordinate values that are displayed in Slicer then you need to invert the first two coordinates.</p>

---

## Post #11 by @Michele_Bailo (2021-02-25 16:39 UTC)

<p>Dear all,<br>
how should I write the same script in order to print the result in an external txt file?</p>
<p>thank you very much</p>

---

## Post #12 by @lassoan (2021-02-25 16:54 UTC)

<p>Since you get the voxels in a numpy array, you can use standard Python and numpy functions to write it to file.</p>
<p>An example is provided <a href="https://discourse.slicer.org/t/how-to-export-voxel-intensity/951/4">above</a>. Note that apart from the <code>slicer.util.arrayFromVolume</code> function to get the numpy array, everything else is plain Python and numpy.</p>

---

## Post #13 by @Michele_Bailo (2021-02-25 18:36 UTC)

<p>I tried with the following script but it only export one intensity value in the txt and not the whole list (as I would get with the print function). I don’t understand what I’m doing wrong:</p>
<p>import numpy as np<br>
voxelArray = slicer.util.arrayFromVolume(getNode(‘HImask-ADC’))<br>
indices = np.where(voxelArray&gt;0)<br>
numberOfVoxels = len(indices[0])<br>
for pointIndex in range(numberOfVoxels):<br>
i = indices[0][pointIndex]<br>
j = indices[1][pointIndex]<br>
k = indices[2][pointIndex]<br>
array_1d = np.array([voxelArray[i,j,k]])<br>
np.savetxt(“array_1d.txt”, array_1d, delimiter="," , fmt=’%.4f’)</p>

---

## Post #14 by @Lisa_Hung (2021-05-10 15:39 UTC)

<p>Hi Andreas,</p>
<p>I want to use the histogram data (<a href="https://discourse.slicer.org/t/get-image-intensity-histogram-of-a-segment/11277" class="inline-onebox">Get image intensity histogram of a segment</a>) to create a combined histogram of each variable in Graphpad, how would you suggest doing that? I have tried using the TSV file data but I just wanted to confirm that the table created in the TSV file creates the X column to be Hounsfield units and the Y to be the number of voxels, is this correct?</p>

---

## Post #15 by @lassoan (2021-05-10 20:48 UTC)

<p>I confirm that if the input volume voxel values are in Hounsfield units then the values along X axis of the image histogram are in Hounsfield units, too.</p>

---

## Post #16 by @Lisa_Hung (2021-05-13 09:38 UTC)

<p>Hi Andreas,</p>
<p>Thank you for your reply. Yes the input is CT data. Could I also confirm that the Y axis is the raw number of voxels?</p>

---

## Post #17 by @lassoan (2021-05-13 14:07 UTC)

<p>Yes, Y value is the number of voxels in that histogram bin.</p>

---

## Post #18 by @Nag (2022-12-05 20:04 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/michele_bailo">@Michele_Bailo</a>  I am trying to extract voxel data using the above code, but I am getting this error.<br>
Traceback (most recent call last):<br>
File “”, line 2, in <br>
File “D:\3D sclier\Slicer 5.3.0-2022-12-03\bin\Python\slicer\util.py”, line 1657, in arrayFromVolume<br>
vimage = volumeNode.GetImageData()<br>
AttributeError: ‘MRMLCore.vtkMRMLFolderDisplayNode’ object has no attribute ‘GetImageData’.<br>
Please anyone can help</p>

---

## Post #19 by @lassoan (2022-12-05 20:21 UTC)

<p>It seems that there are several nodes by the same name in the scene (the one you got was a subject hierarchy folder display node). Therefore, you either need to provide a more specific node name (you can rename the volume to give a more distinguishable name) or need to be more specific when you retrieve the node, for example by using this method:</p>
<pre><code class="lang-python">volumeNode = getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', 'HImask-ADC')
</code></pre>

---

## Post #20 by @Nag (2022-12-05 20:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you! I am new to python in the 3D slicer; I don’t know how to use it. Where can I learn more details about the voxel data export and the python syntax?</p>

---
