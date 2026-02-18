# Extraction the vector components using python

**Topic ID**: 10394
**Date**: 2020-02-22
**URL**: https://discourse.slicer.org/t/extraction-the-vector-components-using-python/10394

---

## Post #1 by @aseman (2020-02-22 18:24 UTC)

<p>Operating system:Linux<br>
Slicer version:4.11.0<br>
Hi 3D Slicer experts and all<br>
I have a BSplin Transform which contains displacement fields. I want to extract its vector components. for this purpose I converted it to a volume node using Transforms module.[ my reference volume is a CT image with image dimensions of 512 *512 *173]. Therefore, the result was a volume node (renamed to Voluememasked) with image dimensions 512 *512 *173.<br>
for extraction I used the following commands in Slicer python interactor :</p>
<blockquote>
<blockquote>
<blockquote>
<p>import <a href="http://scipy.io" rel="noopener nofollow ugc">scipy.io</a> as sio<br>
nodeName= ‘Volumemasked’<br>
voxelArray = array(nodeName)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/aseman/Downloads/Slicer-4.11.0-2020-02-19-linux-amd64/bin/Python/slicer/util.py”, line 935, in array<br>
return arrayFromVolume(node)<br>
File “/home/aseman/Downloads/Slicer-4.11.0-2020-02-19-linux-amd64/bin/Python/slicer/util.py”, line 971, in arrayFromVolume<br>
narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars()).reshape(nshape)<br>
ValueError: cannot reshape array of size 136052736 into shape (173,512,512)</p>
</blockquote>
</blockquote>
</blockquote>
<p>how can I reshape it? can you help me?<br>
Thanks a lot</p>

---

## Post #2 by @Alex_Vergara (2020-02-22 18:40 UTC)

<p>this is a numpy stuf<br>
<code>136052736 = 3 * 173 * 512 * 512</code><br>
therefore you have 3 components in each voxel, redefine nshape like<br>
<code>nshape = [3, 73, 512, 512]</code><br>
then your reshape will work, to extract the x, y, z components do:<br>
<code>x, y, z = narray[0], narray[1], narray[2]</code><br>
if you want the vectors<br>
vec = zip(x, y, z)</p>

---

## Post #3 by @lassoan (2020-02-22 19:00 UTC)

<p>Thanks for reporting this, it seems that Slicer’s <code>array</code> helper function cannot get vector field from scalar volume. We should be able to fix it within a few days. In the meantime, you can change <code>arrayFromVolume</code> function in your util.py file as <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> suggested above.</p>

---

## Post #4 by @lassoan (2020-02-25 00:26 UTC)

<p>I have updated <code>arrayFromVolume</code> to work with any number of scalar components, regardless of using a scalar or vector volume. I’ve also updated Transforms module to save displacement vectors if a vector volume is selected as output, and save displacement magnitude values if a scalar volume is selected as output. Changes are available in latest Slicer Preview Release.</p>

---
