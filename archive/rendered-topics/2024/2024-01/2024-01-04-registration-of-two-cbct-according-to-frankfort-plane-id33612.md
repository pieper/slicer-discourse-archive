# Registration of two CBCT according to Frankfort plane

**Topic ID**: 33612
**Date**: 2024-01-04
**URL**: https://discourse.slicer.org/t/registration-of-two-cbct-according-to-frankfort-plane/33612

---

## Post #1 by @anasmh101 (2024-01-04 02:06 UTC)

<p>Hello everyone, I have problem in doing two head CBCTs registration (pre/post CBCTs) according to Frankfort plane to assess mandible deviation before and after orthodontic treatment, the end result of the registration is not according to Frankfort plane</p>
<p>my work flow is as follows</p>
<p>1- I align each DICOM file according to Frankfort plane separately using Transform module creating two linear transforms, one transform file for each image,</p>
<p>2- then I use Resample Scalar module, Lanczos as interpolation method to apply the Frankfort-plane alignment on DICOM files,</p>
<p>3- then I crop each (Frankfort plane) aligned CBCT according to their new orientation, then I save each aligned CBCT as GIPL format with their correspondent transform file</p>
<p>4-  in Data module , I attach each CBCT image with its correspondent transform file</p>
<p>5 - then I use landmark registration method to do the registration, assign the preCBCT as fixed volume and postCBCT as moving volume, however, the CBCTs are downloaded into the landmark registration module without their correspondent transform files, thus, the end result of the registration is not according to Frankfort plane.</p>
<p>after registration, I tried to re-attach each CBCT with its transform files, but the end result is worse.</p>
<p>what am I doing wrong ? how can I get two CBCTs superimposed according to Frankfort plane ? is their another preferred registration method for this purpose ?</p>

---

## Post #2 by @pieper (2024-01-04 13:47 UTC)

<p>Maybe you need to harden the transforms before step 5?</p>

---

## Post #3 by @anasmh101 (2024-01-06 01:00 UTC)

<p>thank you for pointing this out , I think hardening the transform is what I missed</p>

---
