# No b0! Error with the brain masking process

**Topic ID**: 13448
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/no-b0-error-with-the-brain-masking-process/13448

---

## Post #1 by @Nicholas.jacobson (2020-09-11 18:35 UTC)

<p>Hello,<br>
We are starting to research Tractragraphy for 3d printing purposes and struggling to get the process started with our images. We have loaded all of our dwi images but run into a problem with the brain masking program returning an error saying we have no b0. We do indeed have a b0 in these files but something is getting lost. Is someone able to take a look at my files to help guide us back on tract?</p>

---

## Post #2 by @Nicholas.jacobson (2020-09-11 23:18 UTC)

<p>Update. My files contain a Multivolume, each direction as a separate scalar, and a DWI volume. Exploring the metadata shows there is more then one b0 and the rest are showing as b800. When loaded and exploring the node information I see a ton of data. However, when I explore the sample data, it reflects a very clear b0 and subsequent set of coordinates for each image. So something with my data is not translating. Any guidance is welcome.</p>

---

## Post #3 by @Chris_Rorden (2020-09-12 11:13 UTC)

<p>Can I suggest you try converting these images with <a href="https://github.com/rordenlab/dcm2niix/releases" rel="nofollow noopener">dcm2niix</a>. You could either run this directly from the command line, or you could install the Slicer Extension (select the View/ExtensionManager menu item and search for “SlicerDcm2nii”). Each vendor has their own method for <a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" rel="nofollow noopener">storing gradient information in a DICOM</a>, and each vendor has changed their storage over the years. Therefore, using a different conversion tool may help.</p>

---

## Post #4 by @Nicholas.jacobson (2020-09-14 15:57 UTC)

<p>That worked! Thank you.</p>

---
