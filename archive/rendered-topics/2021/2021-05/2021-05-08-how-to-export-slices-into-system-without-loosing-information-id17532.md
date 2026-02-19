---
topic_id: 17532
title: "How To Export Slices Into System Without Loosing Information"
date: 2021-05-08
url: https://discourse.slicer.org/t/17532
---

# How to export slices into system without loosing information

**Topic ID**: 17532
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/how-to-export-slices-into-system-without-loosing-information/17532

---

## Post #1 by @pranaysingh (2021-05-08 15:53 UTC)

<p>Hi,</p>
<p>I want to save the slices of dicom files into my computer. The slices are parallel to the plane of the volume. What I was doing until now was using Screen capture module and save all the slices of a view(say, Coronal view) into the system. For saving all slices in one go, I called screen capture module using its python API in the CLI.</p>
<p>The issue is that the saved PNG files are saved as 8 bit unsigned integer pixels by the screen capture module, the data type of original dicom file is unsigned 16 bit. Therefore I am loosing information here.<br>
Is there a way I can save the slices without loosing information, keeping the data type at uint16 only.</p>
<p>Any idea would be of great help.</p>
<p>Thanks,<br>
Pranay</p>

---

## Post #2 by @lassoan (2021-05-10 04:10 UTC)

<p>You can get a volume node as a numpy array then write it to png slice by slice (see example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rasterize-a-model-and-save-it-to-a-series-of-image-files">here</a>). However, I would recommend to save in nrrd format for archival and use either use these nrrd files as input for your deep learning training or maybe save as numpy array. If you save as numpy array then you lose all metadata (so you won’t know the physical size and location of the slices anymore), but it might be OK if you keep track of this information by other means.</p>

---

## Post #3 by @pranaysingh (2021-05-10 07:10 UTC)

<p>Hi,</p>
<p>Thanks for the reply. Your suggested way of saving it as nrrd is helpful as I saw. But there are 2 problems I am facing:</p>
<ol>
<li>
<p>I saved nrrd using GUI. File &gt; Save. The nrrd file I got contains the slices of only Axial plane(the Red plane). For my object, I am interested in the coronal plane slices(the Green one). I am not able to find the option to tell the slicer to save nrrd of only Coronal views.</p>
</li>
<li>
<p>Even if I am able to do the above, the second problem is I want to rotate the slicer plane to a particular angle in the volume, that will change the view in all the 3 viewers(R, G and Y). I want to save nrrd files of those slices as well. Meaning, I want to save nrrd for different planes. But even when I am moving the plane in 3D and can see the views changing in the coronal view, when I save it using GUI like above, i get the nrrd for the default view everytime. What am i doing wrong?</p>
</li>
</ol>
<p>It would be great help if you could guide to the correct way of doing it.<br>
Thanks,<br>
Pranay</p>

---

## Post #5 by @pranaysingh (2021-05-10 09:46 UTC)

<p>What we are eventually trying to do is to save slices of various views of CT scans loaded from DICOM format data…</p>

---

## Post #6 by @lassoan (2021-05-10 12:57 UTC)

<p>You can extract arbitrarily oriented slices of a volume as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">this example</a>.</p>
<p>You may also use torchio or monai for generating training data sets from volumes.</p>

---

## Post #7 by @pranaysingh (2021-05-11 18:26 UTC)

<p>Hi,</p>
<p>Thanks for your reply, we tried what you suggested. It works but with a strange dependency. The size of the array returned by the function referred by you depends upon the window size of the Slicer app, or say the size of the views of R, G and Y opened in the app.</p>
<p>What we could infer is that all these methods have dependency on the view pipeline of the app.</p>
<p>Is there any other way to extract slices at different normals in a way that it is independent of what’s the size of the app window ?</p>
<p>Thanks</p>

---

## Post #8 by @NoobForSlicer (2021-05-11 18:46 UTC)

<p>Lassoan is right, Nrrd is a way better to archive and save data.</p>
<p>Separating volume into PNG slices makes no sense. Besides losing data and information in relation to voxel pixel conversion, you also lose directional and orientational info.</p>
<p>Also I do not undderstand why do you say that the nrrd contains ONLY the slices of red plane. It seems to me that we have a misunderstanding of what nrrd is.</p>
<p>Maybe I am wrong. NRRD file does not contain slices of this or that plane, it contains voxels which then are projected into three planes. There are no red plane slices or green plane slices.</p>
<p>There is a volume which contains many voxels and you can slice it with whichever plane you prefer.</p>
<p>It is just a really good format from my experience.</p>
<p>Please, I am a noob so I have no idea about these topics but can you tell me how can you save NRRD for particular slices? Is it not so that that is a volume format?</p>

---

## Post #9 by @NoobForSlicer (2021-05-11 18:48 UTC)

<p>But it is just so much easier to work and so clean, having one file instead of a sequence.</p>
<p>Everytime you load in a sequence of images you must set up the spacing for each plane, orientation, directions and there is always a chance that you might have a few settings wrong and will lose some information. Further more you as you just said, want to save slices of files of coronal plane, which then again once imported have to be projected into the horizontal plane but then again if done wrong you risk losing information upon import.</p>
<p>It is just so messy.</p>
<p>Nrrd solves that… Maybe I am a noob but… idk this format helped me a lot to have cleaner work</p>

---

## Post #10 by @LuckyLuke (2021-05-11 18:53 UTC)

<p>From my understanding nrrd format still saves slices in one plane but the header contains information like the directions and stuff. There is nothing so revolutionary about the nrrd!?</p>

---

## Post #11 by @lassoan (2021-05-11 19:31 UTC)

<p>There is certainly nothing revolutionary about nrrd, it just does what it is designed for - storing 2D/3D/4D images in 3D space with various scalar types and bit depth, with known origin, spacing, and axis directions.</p>
<p>We try to steer users away from using png and other consumer file formats because they are not designed for storing medical images and they do a very bad job at that: they cannot store 3D information, physical size, position, orientation, only support a few pixel types, etc.</p>
<p>Have a look at <a href="https://torchio.readthedocs.io/">torchio</a> and <a href="https://monai.io/">monai</a> for good examples of preprocessing 3D medical images to be used as training data for deep learning.</p>

---
