---
topic_id: 5656
title: "How To Export Segmentation As Masks Jpgs"
date: 2019-02-06
url: https://discourse.slicer.org/t/5656
---

# How to export segmentation as masks (.jpgs?)

**Topic ID**: 5656
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/how-to-export-segmentation-as-masks-jpgs/5656

---

## Post #1 by @Arcsecond (2019-02-06 03:57 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.10.1<br>
I have as input DICOM files and I want to export the segmentations on those files in the form of a mask. The intended use is to load the masks into a numpy array for further use.</p>

---

## Post #2 by @muratmaga (2019-02-06 04:45 UTC)

<p>Using Segmentation module you can convert your segments to a label map, and then save it as a JPG/PNG series at the Save Dialog box.</p>

---

## Post #3 by @cpinter (2019-02-06 14:24 UTC)

<p>Why do you need a stack of jpgs just to load them into a numpy array? You can do all that in Slicer using the python interactor. To get the numpy array for a volume you can use this function<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L779" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L779" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L779</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="769" style="counter-reset: li-counter 768 ;">
<li>if isinstance(node, slicer.vtkMRMLVolumeNode):</li>
<li>  return arrayFromVolume(node)</li>
<li>elif isinstance(node, slicer.vtkMRMLModelNode):</li>
<li>  return arrayFromModelPoints(node)</li>
<li>elif isinstance(node, slicer.vtkMRMLGridTransformNode):</li>
<li>  return arrayFromGridTransform(node)</li>
<li>
</li>
<li># TODO: accessors for other node types: polydata (verts, polys...), colors</li>
<li>return None</li>
<li>
</li>
<li class="selected">def arrayFromVolume(volumeNode):</li>
<li>"""Return voxel array from volume node as numpy array.</li>
<li>Voxels values are not copied. Voxel values in the volume node can be modified</li>
<li>by changing values in the numpy array.</li>
<li>After all modifications has been completed, call :py:meth:`arrayFromVolumeModified`.</li>
<li>
</li>
<li>.. warning:: Memory area of the returned array is managed by VTK, therefore</li>
<li>  values in the array may be changed, but the array must not be reallocated</li>
<li>  (change array size, shallow-copy content from other array most likely causes</li>
<li>  application crash). To allow arbitrary numpy operations on a volume array:</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
(slicer.util.arrayFromVolume)<br>
You’ll need to do this on the labelmap you exported from the segmentation.</p>
<p>Btw you can also export segmentations to labelmaps in the Data module (right-click segmentation and you’ll find the option in the menu).</p>

---

## Post #4 by @Arcsecond (2019-02-07 23:20 UTC)

<p>I see, thank you so much! I wasn’t familiar with the python interactor.</p>

---

## Post #5 by @Neda (2020-07-06 16:46 UTC)

<p>I saved the input image (2D) and the segment as mask both in nrrd format and I load them in python for further processing but the dimension of these two images are different and so the mask actually does not match the original image. Could you please tell me how I can save them separately in the same dimension so that they are perfectly registered as shown in the Slicer viewer? Thanks in advance</p>

---

## Post #6 by @Neda (2020-07-06 17:02 UTC)

<p>It is solved, I had to deactivate compressing while saving data!</p>

---

## Post #7 by @muratmaga (2020-07-06 18:20 UTC)

<p>That’s strange. Compression should have no impact on the dimensions of the volume saved. Did you change the Slicer version recently? The newer versions should save the labelmap to the full extend of the volume.</p>

---

## Post #8 by @Neda (2020-07-07 06:34 UTC)

<p>I am using the nightly 4.11.0 (2020.06.20). And I am saving the segmentation itself (in nrrd format) not the labelmap.</p>

---

## Post #9 by @Neda (2020-07-07 14:22 UTC)

<p>I am actually having problem saving the segmentation in other formats (e.g. .png). I can easily save the input dicom file (2D image) as .png image but when I want to save the labelmap in .png I get this error: “cannot write data file”.<br>
I appreciate if you would let me know how to solve this issue.</p>

---

## Post #10 by @lassoan (2020-07-07 17:55 UTC)

<p>I would not recommend to save 3D image or segmentation as a series of jpg/png/bmp. Instead, use the following file formats:</p>
<ul>
<li>for lossless saving (save all metadata, including position, orientation, spacing), save as nrrd</li>
<li>for saving training data for deep learning network, save into numpy array file from script</li>
<li>for papers, presentations, you can save as image series or video using Screen Capture module</li>
</ul>

---

## Post #11 by @Manoj.V_Khatokar (2021-04-21 15:59 UTC)

<p>I am facing the same issue of saving the label maps as a series of (jpg or png) images. I mainly need this kind of series for training a neural network . How do I save the label maps in jpg series ?</p>

---

## Post #12 by @muratmaga (2021-04-21 16:03 UTC)

<p>Slicer does not allow you saving volumes as 2D image sequences. See <a class="mention" href="/u/lassoan">@lassoan</a> answer for your options.</p>

---

## Post #13 by @lassoan (2021-04-21 16:49 UTC)

<p>You will find a lot of tutorials that use PNG images as input, because using PNGs as inputs makes sense when the images are natively stored as individual 8 or 24-bit RGB images.</p>
<p>However, once a medical image is reconstructed into 3D volume from DICOM files, it is natively stored in nrrd or nifti format. I would recommend to check out <a href="https://monai.io/">monai</a> and its <a href="https://github.com/Project-MONAI/tutorials">tutorials</a> to learn how to use 3D medical images for deep learning training.</p>

---
