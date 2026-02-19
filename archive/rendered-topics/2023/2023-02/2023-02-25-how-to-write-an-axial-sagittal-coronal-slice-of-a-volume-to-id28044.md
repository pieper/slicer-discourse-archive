---
topic_id: 28044
title: "How To Write An Axial Sagittal Coronal Slice Of A Volume To"
date: 2023-02-25
url: https://discourse.slicer.org/t/28044
---

# How to write an axial/sagittal/coronal slice of a volume to DICOM file using Python script

**Topic ID**: 28044
**Date**: 2023-02-25
**URL**: https://discourse.slicer.org/t/how-to-write-an-axial-sagittal-coronal-slice-of-a-volume-to-dicom-file-using-python-script/28044

---

## Post #1 by @anhhtmsc (2023-02-25 02:19 UTC)

<p>Hello everyone,<br>
I want to write an axial/sagittal/coronal slice from a loaded volumeNode to a DICOM file using Python script. I tried to get the vtkImageData of the volumeNode and convert it to a sitkImage, then write one slice of it to a DICOM file using SimpleITK. Here is my code to do this. I get the function vtk2sitk() from this post: <a href="https://discourse.itk.org/t/vtk-to-simpleitk-conversion-in-python/4028" rel="noopener nofollow ugc">VTK to simpleITK conversion in Python</a></p>
<pre><code class="lang-auto">import SimpleITK as sitk
import vtk
import vtk.util.numpy_support as vtknp
import SampleData
import numpy as np
import time

def vtk2sitk(vtkimg):
    """Takes a VTK image, returns a SimpleITK image."""
    sd = vtkimg.GetPointData().GetScalars()
    npdata = vtknp.vtk_to_numpy(sd)

    dims = list(vtkimg.GetDimensions())
    origin = vtkimg.GetOrigin()
    spacing = vtkimg.GetSpacing()

    dims.reverse()
    npdata.shape = tuple(dims)

    sitkimg = sitk.GetImageFromArray(npdata)
    sitkimg.SetSpacing(spacing)
    sitkimg.SetOrigin(origin)

    if vtk.vtkVersion.GetVTKMajorVersion() &gt;= 9:
        direction = vtkimg.GetDirectionMatrix()
        d = []
        for y in range(3):
            for x in range(3):
                d.append(direction.GetElement(y, x))
        sitkimg.SetDirection(d)
    return sitkimg

volumeNode = SampleData.SampleDataLogic().downloadMRHead()
sitkImg = vtk2sitk(volumeNode.GetImageData())
tempPath = 'path_to_save_dicom_file' + f"/temp.{time.time()}.dcm"
sitk.WriteImage(sitkImg[99], tempPath)
</code></pre>
<p>The problem is that the output DICOM file has the wrong direction (rotated horizontally). What should I do to solve this problem? Maybe, how to get the sitkImg in the right direction?<br>
Thank you, everyone!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f54d88bac4b4956d83e61e7f6191ec892ac7fd6.jpeg" alt="img-00002-00001" data-base62-sha1="bjNv6fUXvjxYgqDRQ4LYjrtGxLg" width="256" height="130"></p>

---

## Post #2 by @pieper (2023-02-25 17:18 UTC)

<p>If you are doing this in Slicer, the easiest would be to use the Orient Scalar Volume module to reshuffle the pixels and the Create a DICOM Series module to create dicom.  Doing this with lower level tools will be more difficult and error prone as you’ve seen.</p>

---

## Post #3 by @anhhtmsc (2023-02-28 04:29 UTC)

<p>Thank you for your response. I tried to use the 2 modules: “Orient Scalar Volume”, “Create a DICOM Series” and it worked as expected, but the time it takes is too much. For example, with a DICOM series of size (361, 512, 512), it takes about 5 minutes to load and write the whole series in all directions. Here is the code I use:</p>
<pre><code class="lang-auto">volumeNode2 = slicer.mrmlScene.CreateNodeByClass("vtkMRMLScalarVolumeNode")
volumeNode2.UnRegister(None)  # to prevent memory leaks
volumeNode2.SetName(slicer.mrmlScene.GenerateUniqueName("OrientedVolumeNode"))
volumeNode2.SetHideFromEditors(False)
slicer.mrmlScene.AddNode(volumeNode2)
parameters = {'inputVolume1':volumeNode, 'outputVolume':volumeNode2, 'orientation':direction}
slicer.cli.run(slicer.modules.orientscalarvolume, None, parameters, True)
parameters = {'inputVolume':volumeNode2, 'dicomDirectory': savedPath}
slicer.cli.run(slicer.modules.createdicomseries, None, parameters, True)
slicer.mrmlScene.RemoveNode(volumeNode2)
del volumeNode2
</code></pre>
<p>I also tried to do the job in 3 directions simultaneously using <a href="https://docs.python.org/3/library/multiprocessing.html" rel="noopener nofollow ugc">multiprocessing.Pool</a>, but I got an error: “Error QObject::setParent: Cannot set parent, new parent is in a different thread”.</p>

---

## Post #4 by @anhhtmsc (2023-02-28 04:43 UTC)

<p>The purpose I want to do this is that I want to return the DICOM file instead of PNG image for a request similar to the ‘/slice’ request of the WebServer module (e.g: <a href="http://localhost:2016/slicer/slice?orientation=axial&amp;scrollTo=.6" rel="noopener nofollow ugc">http://localhost:2016/slicer/slice?orientation=axial&amp;scrollTo=.6</a>). For example, with a request slice?orientation=coronal&amp;index=99, I need to return the slice 99th of the series in coronal orientation. How can I do this effectively with Slicer 3D?</p>

---

## Post #5 by @pieper (2023-02-28 14:12 UTC)

<p>Do you need the data to be in dicom?  Or do you just need the pixels?  Do you want to access via the WebServer or in the Slicer python environment?  If just pixels in Slicer python, you can just get the numpy array and use indexing to extract what you need.</p>

---
