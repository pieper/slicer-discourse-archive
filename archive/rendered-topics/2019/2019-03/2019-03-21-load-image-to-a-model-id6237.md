---
topic_id: 6237
title: "Load Image To A Model"
date: 2019-03-21
url: https://discourse.slicer.org/t/6237
---

# Load image to a model

**Topic ID**: 6237
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/load-image-to-a-model/6237

---

## Post #1 by @Alex1 (2019-03-21 12:56 UTC)

<p>Hi all,<br>
Sorry to bother you with my question. I’m new to Slicer and I’m trying to write a scripted python module. I’m trying to recognize MRI images by a deep-learning model. I have already loaded my model and I’m now trying to load my image to my module. My image is a single image in jpg format. I tried this:</p>
<blockquote>
<p>name=slicer.mrmlScene.GetNodeByID(imagename)<br>
img=cv2.imread(name)<br>
x = cv2.resize((img), (224, 224), interpolation=cv2.INTER_CUBIC) / 255.0</p>
</blockquote>
<p>it didn’t work, I don’t think it read the image.What is the correct way of implementing this?(by the way, I have already installed cv2)</p>
<p>Thanks,<br>
Alex</p>

---

## Post #2 by @adamrankin (2019-03-21 13:29 UTC)

<p>You’ve got a couple options.</p>
<p>Read the file directly from disk (not recommended), using conventional <code>cv2.imread(&lt;fullPathToFile&gt;)</code></p>
<p>If you’ve loaded the image into Slicer, then you can do</p>
<pre><code class="lang-python">import cv2
from vtk.util import numpy_support

imageNode =  slicer.util.getNode('&lt;nameOfJpgImageWithoutExtension&gt;')
vtk_image = imageNode.GetImageData()
np_image = numpy_support.vtk_to_numpy(vtk_image.GetPointData().GetScalars())
dims = vtk_image.GetDimensions()
np_image.reshape(dims[0], dims[1], dims[2])
</code></pre>
<p>See this link <a href="https://stackoverflow.com/questions/12754971/how-to-convert-a-3d-vtkdataset-into-a-numpy-array" rel="nofollow noopener">https://stackoverflow.com/questions/12754971/how-to-convert-a-3d-vtkdataset-into-a-numpy-array</a> for more information.</p>
<p>cv2 python bindings use numpy arrays as their images.</p>

---

## Post #3 by @lassoan (2019-03-21 18:19 UTC)

<p>You can also load an image directly to a volume node:</p>
<pre><code>volumeNode = slicer.util.loadVolume('path/to/myimage.jpg')</code></pre>

---
