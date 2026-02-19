---
topic_id: 4172
title: "Regarding H5 File Format"
date: 2018-09-23
url: https://discourse.slicer.org/t/4172
---

# Regarding .h5 file format

**Topic ID**: 4172
**Date**: 2018-09-23
**URL**: https://discourse.slicer.org/t/regarding-h5-file-format/4172

---

## Post #1 by @jamieng (2018-09-23 13:09 UTC)

<p>Hello,</p>
<p>May I know if .h5 file formats are editable in 3D Slicer to perform segmentation?<br>
If it is not, may I know if it is possible to easily convert the file to a compatible and editable format in 3D Slicer?<br>
Thank you so much!</p>

---

## Post #2 by @lassoan (2018-09-23 22:27 UTC)

<p>HDF5 format is just a container. Slicer can read ITK transforms from HDF5 (and maybe images, too, through ITK IO classes). What information is stored in the HDF5 files? What software did you use to create them?</p>

---

## Post #3 by @jamieng (2018-09-24 07:03 UTC)

<p>I want to obtain high resolution MRI scans of the knee to perform segmentation in 3D Slicer. My supervisor recommended me this website <a href="http://mridata.org/" rel="nofollow noopener">http://mridata.org/</a> , however the files are of the .h5 format.</p>
<p>Thank you so much for replying!</p>

---

## Post #4 by @rkikinis (2018-09-24 09:52 UTC)

<p>Try this</p>
<p><a href="https://www.spl.harvard.edu/publications/item/view/1953" rel="nofollow noopener">https://www.spl.harvard.edu/publications/item/view/1953</a></p>

---

## Post #5 by @Mihail_Isakov (2018-09-24 12:42 UTC)

<p>Data sets from <a href="http://mridata.org" rel="nofollow noopener">mridata.org</a> are k-space data in ISMRMRD format in HDF5 container<br>
<a href="http://mriquestions.com/what-is-k-space.html" rel="nofollow noopener">http://mriquestions.com/what-is-k-space.html</a><br>
Images have to be reconstructed first (HDF5 files can theoretically contain reconstructed images too, AFAIK they do not have reconstructed images). S. <a href="http://mridata.org" rel="nofollow noopener">mridata.org</a>’s FAQ, there are python tools, i played with in the past (just for curiosity with test data set testdata.h5) it is no so easy to reconstruct real data sets, but surely possible. Probably not what you need.<br>
Regards</p>

---

## Post #6 by @Mihail_Isakov (2018-09-25 16:43 UTC)

<p><a class="mention" href="/u/jamieng">@jamieng</a></p>
<p>FYI, another MR knee study</p>
<p><a>ftp://medical.nema.org/medical/dicom/DataSets/WG16/Philips/ClassicSingleFrame/Knee/</a></p>

---
