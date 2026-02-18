# Uploading a Volume from scratch, but too large a volume causes a crash

**Topic ID**: 3470
**Date**: 2018-07-12
**URL**: https://discourse.slicer.org/t/uploading-a-volume-from-scratch-but-too-large-a-volume-causes-a-crash/3470

---

## Post #1 by @Troy (2018-07-12 14:56 UTC)

<p>Hello, I’ve been working on writing a code to read in Seiman’s format PET and CT scans, and I’ve got the majority of the code written. Currently, it reads in PET images with no issues, and I can adjust and view them. However, when I try to load in a CT data set, which is much larger (496x496x496 as opposed to 128x128x159), A couple lines in the code cause my program to crash.</p>
<p>I load in the file as a numpy array and then use a slightly adjusted code I found in the forums by Csaba, which I’ll paste below:<br>
importer = vtk.vtkImageImport()</p>
<pre><code>    importer.CopyImportVoidPointer(img, img.nbytes)
    setDataType = 'importer.SetDataScalarTypeTo' + 'Float' + '()'
    eval(setDataType)
    importer.SetNumberOfScalarComponents(1)
    importer.SetWholeExtent(0,img.shape[0]-1,0,img.shape[1]-1,0,img.shape[2]-1)
    importer.SetDataExtentToWholeExtent()
    importer.Update()
    volume = slicer.vtkMRMLScalarVolumeNode()
    volume.SetName("image")
    volume.SetAndObserveImageData(importer.GetOutput())
    slicer.mrmlScene.AddNode(volume)
    volumeDisplayNode = 0
    volumeDisplayNode = slicer.vtkMRMLScalarVolumeDisplayNode()
    slicer.mrmlScene.AddNode(volumeDisplayNode)
    greyColorTable = slicer.util.getNode('Grey')
    volumeDisplayNode.SetAndObserveColorNodeID(greyColorTable.GetID())

    volume.SetAndObserveDisplayNodeID(volumeDisplayNode.GetID())
    volume.SetSpacing(xrat,yrat,zrat)
    selectionNode = slicer.app.applicationLogic().GetSelectionNode()
    selectionNode.SetReferenceActiveVolumeID(volume.GetID())
    slicer.app.applicationLogic().PropagateVolumeSelection(0)
</code></pre>
<p>Via trial and error I’ve isolated the two lines that cause the crash as:</p>
<pre><code>    volume.SetAndObserveDisplayNodeID(volumeDisplayNode.GetID())
</code></pre>
<p>and</p>
<pre><code>    slicer.app.applicationLogic().PropagateVolumeSelection(0)
</code></pre>
<p>Obviously (or maybe not, I’m not sure), without these two lines the image doesn’t show, but nor does it crash. I don’t personally know too much about slicer, but have experience programming in python. Is there another way I can represent the data so that it doesn’t take up too much space so slicer can read it? Alternatively, is there another function I can use to cause slicer to display the volume. Any advice would be appreciated! Thanks!</p>

---

## Post #2 by @pieper (2018-07-12 15:12 UTC)

<p>Hi <a class="mention" href="/u/troy">@Troy</a> -</p>
<p>Using void pointers can be crash-prone if you don’t have the datatypes or sizes just right.</p>
<p>Probably better to work with numpy arrays - you can see an example of creating a volume node and filling it with a numpy array here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>
<p>(BTW, are the PET and CT not in DICOM?  Typically the DICOM data would load without needing a custom script.  Memory shouldn’t be an issue for most scans and computers).</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @Troy (2018-07-12 18:50 UTC)

<p>Hi Steve,</p>
<p>These particular files aren’t DICOM, to convert it there’s an extra step that I’m trying to circumvent by writing this. And I start by creating numpy arrays, and then change those arrays in the above code. Is there an easier way to display and work with numpy arrays than that code? Sorry, I’m new to a lot of the libraries for Slicer</p>

---

## Post #4 by @pieper (2018-07-12 21:15 UTC)

<aside class="quote no-group" data-username="Troy" data-post="3" data-topic="3470">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/85f322/48.png" class="avatar"> Troy:</div>
<blockquote>
<p>Is there an easier way to display and work with numpy arrays than that code?</p>
</blockquote>
</aside>
<p>Yes, here is the code from the page I linked above - it creates a scalar volume node and displays it.  Much simpler <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"> :</p>
<pre><code class="lang-auto">import numpy as np
import math

def some_func(x, y, z):
  return 0.5*x*x + 0.3*y*y + 0.5*z*z

a = np.fromfunction(some_func,(30,20,15))

volumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
volumeNode.CreateDefaultDisplayNodes()
updateVolumeFromArray(volumeNode, a)
setSliceViewerLayers(background=volumeNode)
</code></pre>

---

## Post #5 by @Troy (2018-07-19 21:44 UTC)

<p>Perfect, that worked great! Thank you!</p>

---
