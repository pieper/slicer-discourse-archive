# Why is the number of voxels different from the number of matrices?

**Topic ID**: 7134
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/why-is-the-number-of-voxels-different-from-the-number-of-matrices/7134

---

## Post #1 by @kscript (2019-06-12 09:55 UTC)

<p>Hello everybody</p>
<p>I am working on making the volume data of the segmentation nrrd extension an Array List.</p>
<p>I have solved the method of creating an Array, but there is one question.</p>
<p>The size of the image I use is 501x501x500 and the total number of voxels is 125,500,500.</p>
<p>However, the total number of voxels produced by Array is about twice the output.</p>
<p>I wonder why.</p>
<p>I attached the code I used.</p>
<p>Thanks.</p>
<pre><code>import numpy as np
volumeNode = getNode('Segmentation-label_1')
volumeArray = slicer.util.arrayFromVolume(volumeNode)
a = volumeArray
np.savetxt('C:\\Users\\admin\\Documents\\label8.txt',a,fmt='%5s')</code></pre>

---

## Post #2 by @lassoan (2019-06-12 15:30 UTC)

<p>You retrieve the numpy array content correctly but then you write it out to file incorrectly (you write it as a byte array, and since each voxel is stored as int16, you get two numbers for each voxel). Writing out a 3D array as text file should be avoided (it takes about 100x more time to read and write, takes much more space than necessary, not clear how to interpret the data, no other software in the world would expect input data in that format, etc.). But if you really must do it then you need to flatten the array first and then write it out:</p>
<pre><code>np.savetxt('C:\\tmp\\label8.txt', a.flatten(), fmt="%d")
</code></pre>
<p>But again, don’t do it. Instead, save the labelmap volume directly from the volume, in a standard file format, such as nrrd:</p>
<pre><code>slicer.util.saveNode(volumeNode, "c:/tmp/labels.nrrd")</code></pre>

---

## Post #3 by @kscript (2019-06-12 23:42 UTC)

<p>I have previously saved the volumeNode as an nrrd file, as you said. And I ran the above code.</p>
<p>Anyway I saved file using your method.</p>
<p><code>slicer.util.saveNode(volumeNode, "c:/tmp/labels.nrrd")</code></p>
<p>but if i using thins method i cannot get color method.</p>
<p>My ultimate goal is to:</p>
<p>I have two nrrd files, one nrrd file contains medical imaging information,<br>
Another nrrd file contains only information from the Labelmap.<br>
The first method combines the two nrrd files, the second method takes the coordinates of the Labelmap and tries to color the coordinates to another nrrd file.<br>
For the second method, I have stored the labelmap as text and see if it is accessible.<br>
Is there a way to combine two nrrd files in 3D Slicer?</p>

---

## Post #4 by @lassoan (2019-06-13 14:27 UTC)

<p>You can save the input scalar image and the segmentation as two separate nrrd files. What software are you going to use to read/process these images?</p>

---

## Post #5 by @kscript (2019-06-13 23:32 UTC)

<p>I want to make Convolution Neural Network using nrrd file.</p>
<p>That’s why I want to combine the Segmentation File and the Original data File.</p>

---

## Post #6 by @lassoan (2019-06-14 03:21 UTC)

<p>Do you mean you would like to mix the input image and ground truth segmentation into one image? This should not be necessary.</p>

---

## Post #7 by @kscript (2019-06-14 05:32 UTC)

<p>Umm… I don’t understand why not necessary.</p>
<p>I want to auto annotation software using deep learning. So i labeling in image’s some part.<br>
if i make a deep learning model that time input file is patient’s nrrd file. reasult is annotation on image.<br>
So i think to combine two files works necessary</p>

---
