---
topic_id: 21462
title: "Problem Saving With Nrrd Format"
date: 2022-01-14
url: https://discourse.slicer.org/t/21462
---

# Problem saving with .nrrd format

**Topic ID**: 21462
**Date**: 2022-01-14
**URL**: https://discourse.slicer.org/t/problem-saving-with-nrrd-format/21462

---

## Post #1 by @Francesca_Lo_Iacono (2022-01-14 09:19 UTC)

<p>Hi guys!</p>
<p>I have a problem. I’m segmenting left ventricle in two parts: left ventricle wall and left ventricle cavity. As output I need an .nrrd format. The problem is that saving the segmentation as “.nrrd” format and doesn’t allow me to see the two different segmentation.</p>
<p>What I want to obtain is a .nrrd filen containing both ROIs. How can I do ?</p>
<p>Attached a picture of the segmented frame and a picture of the .nrrd file that I obtain saving.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a0568a27c5f7ae3401c4cd86a09fbbf629de190.png" alt="Schermata 2022-01-14 alle 10.17.05" data-base62-sha1="1qEmuObt27Zf1YPu9iACLVOn7uE" width="442" height="374"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8545fb2c6b844eecc8b63749988fde6cb4511dd.png" alt="Schermata 2022-01-14 alle 10.17.30" data-base62-sha1="o16Z4MoXxUpOqTo6m9BPXJAlGNv" width="488" height="392"></p>

---

## Post #2 by @lassoan (2022-01-14 15:44 UTC)

<p>The screenshot above indicates that the nrrd file is loaded as a scalar volume, not as a segmentation.</p>
<p>A <code>.nrrd</code> file can store several different kinds of image-like data, such as scalar volume, labelmap volume, segmentation, displacement field, etc. When you load a nrrd file then you need to tell Slicer of how you want it to load the data. You have two options:</p>
<ul>
<li>Use composite file extension (such as <code>something.seg.nrrd</code>, <code>something.label.nrrd</code>) to indicate what kind of data is stored in the file. This is the recommended method.</li>
<li>Select the desired data type in “Description” column in the “Add file” window when you load the file.</li>
</ul>

---

## Post #4 by @Francesca_Lo_Iacono (2022-01-14 16:12 UTC)

<p>Thank you! I have loaded it as a segmentation but now I cannot see the segmentation</p>

---

## Post #5 by @lassoan (2022-01-14 17:30 UTC)

<p>If you just load the segmentation file and there is no underlying image then maybe you just cannot scroll the slice view where the segmentation is (because the slice offset slider bounds are determined by the loaded volume). Load the segmented volume; and then load the nrrd file as segmentation and see if you can find the segmented slice.</p>
<p>If the segmentation does not show up then try with the latest Slicer Preview Release (just in case there was some bug that have been resolved since the latest Slicer Stable Release was created).</p>
<p>If it still does not work as expected then please upload the nrrd file somewhere (dropbox, OneDrive, Google drive,…) and post the link so that I can have a look what you have in the file.</p>

---
