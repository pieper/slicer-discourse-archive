# Any way to read or export from an iSite CD Direct disc?

**Topic ID**: 3787
**Date**: 2018-08-15
**URL**: https://discourse.slicer.org/t/any-way-to-read-or-export-from-an-isite-cd-direct-disc/3787

---

## Post #1 by @ermatlock (2018-08-15 14:36 UTC)

<p>I received a radiology disc using iSite CD Direct 3.5 Media viewer. I am unable to access the imaging through Slicer or any other dicom viewer. The included iSite Media Viewer app does not seem to allow dicom export. Is there any way to access these files so that I can bring them into Slicer?</p>

---

## Post #2 by @ermatlock (2018-08-16 14:44 UTC)

<p>I have resorted to saving each slice as a .jpg and am able to load into slicer. However, without the measurement data the image is not quite right. Still looking for any pointers. Thanks.</p>

---

## Post #3 by @lassoan (2018-08-16 15:03 UTC)

<p>What kind of data are you trying to load? Can you share a non-patient data set?</p>

---

## Post #4 by @ermatlock (2018-08-16 20:22 UTC)

<p>It’s an mri of a right leg. I have the images in png format. I was able to get the axial to work after some tweaking. The coronal and sagittal sets are loading with impropoer orientation at the moment.<a href="https://www.dropbox.com/sh/yg7yg7tms2zn8p9/AAAB1U6D8mCK1kGQWv_xzP50a?dl=0" rel="nofollow noopener">mri datasets</a></p>

---

## Post #5 by @lassoan (2018-08-21 21:01 UTC)

<p>Series of png files can certainly be loaded, but after that you need to fix up the voxel size and image orientation (see instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F">here</a>), and image quality may not be optimal (since depth of exported images is limited to 8 bits per channel).</p>
<p>Are you sure you don’t have original images on the CD (in DICOM format)? How did you try to load the original images from the CD?</p>

---

## Post #6 by @ermatlock (2018-08-22 15:04 UTC)

<p>I appreciate you getting back to me. I was able to get the files to load successfully and have got some passable results. The studies themselves are limited but it works. I’d ultimately like to figure out how to register the separate axial, sagittal and coronal studies into one volume but they still all load to the axial plane. The cd uses a hobbled isite viewer and the disk has no dicom files. Instead there are .dts files inside which as far as i can tell is only readable by the included viewer. If you know of any way to read those files let me know.</p>

---

## Post #7 by @lassoan (2018-08-22 15:37 UTC)

<p>I’ve searched the web about .dts files and it seems that old versions of Philps iSite software were only able to save files in proprietary format that only the iSite viewer can use. Newer versions can also save DICOM files. If maximum image quality and reliability of physical size is important then I would recommend to request another export of the data set, in DICOM format.</p>
<p>Acquisition of 3 highly anisotropic MRI volumes is quite common, as they are well suited for humans reviewing them on 2D screens. However, they are barely usable for 3D reconstruction and analysis. See more details in this post: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2?u=lassoan">Combining volumes - what am I missing?</a></p>

---
