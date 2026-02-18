# DICOM image size

**Topic ID**: 10069
**Date**: 2020-02-02
**URL**: https://discourse.slicer.org/t/dicom-image-size/10069

---

## Post #1 by @Ramya_C (2020-02-02 12:06 UTC)

<p>Is there a way to check the DICOM image size (dimensions, length) in 3D slicer ?</p>
<p>May I know how to do it.<br>
Thanks</p>

---

## Post #2 by @pieper (2020-02-02 14:52 UTC)

<p>Before loading you can right click in the DICOM browser and look at the header (metadata).  Or after loading you can look at the Volume Information section of the Volumes module.</p>

---

## Post #3 by @Ramya_C (2020-02-03 00:19 UTC)

<p>Thanks for reply.<br>
However when I print the 3D model, the output model dimension seems to be small than the DICOM image size.<br>
May I know what could be the issue ?</p>

---

## Post #4 by @lassoan (2020-02-03 02:30 UTC)

<p>Did you import the images into Slicer directly from DICOM? What imaging modality was it (CT, MRI, CBCT, microCT, ultrasound, …)?</p>
<p>When you imported the STL file into your 3D printing software, did you set millimeter as length unit in the file?</p>

---

## Post #5 by @Ramya_C (2020-02-03 03:02 UTC)

<p>Yes I tried to import the images from DICOM.<br>
It was CT imaging modality.<br>
The final 3D printed output seems to be 20% less than actual image size.</p>

---

## Post #6 by @lassoan (2020-02-03 03:19 UTC)

<p>If you measure some length on the object in Slicer (using line or ruler tool) does the displayed value correspond to the correct physical size or to the size of the 3D-printed object?</p>

---

## Post #7 by @timeanddoctor (2020-02-03 04:25 UTC)

<p>I really agree with lassoan. And which software was used to slice the stl to gcode. You should check the each step from 3d construction to the last printing model.</p>

---

## Post #8 by @Ramya_C (2020-02-03 04:49 UTC)

<p>Thank you for all replies.<br>
I measured the physical size of specimen to 3D printed object. There is a difference of 20% in the 3d printed when compared to origin object.<br>
I have been using magics and 3D slicer to create STL files.<br>
However, we are not sure how come the object is reduced in size when it is printed.</p>

---

## Post #9 by @timeanddoctor (2020-02-03 05:17 UTC)

<p>What is the last size of the file before slice(printer software)?</p>
<p>The printer software maybe changed the scale automatic when the model is larger than the boundary of the max printing area.</p>

---

## Post #10 by @Ramya_C (2020-02-03 05:53 UTC)

<p>Can you help me to check this.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7801a248624e408cc83e41d86f161993e81ff95b.png" alt="image" data-base62-sha1="h7CNq4pN8ygiGGfLixU7GFTI9yb" width="687" height="313"><br>
Is the image origin indicate the dimension of the DICOM image ?<br>
How to calculate image dimension here ?</p>

---

## Post #11 by @Ramya_C (2020-02-03 05:54 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7801a248624e408cc83e41d86f161993e81ff95b.png" alt="image" data-base62-sha1="h7CNq4pN8ygiGGfLixU7GFTI9yb" width="687" height="313"><br>
Is the image origin indicate the dimension of the DICOM image ?<br>
How to calculate image dimension here ?</p>

---

## Post #12 by @Juicy (2020-02-03 07:24 UTC)

<p>The values above look reasonable to me. Although to be sure you would need to compare them to the DICOM metadata.</p>
<p>The Axial images are 512x512 pixels and each pixel is 0.4746mm x 0.4746mm so the size of the image should be 243mm x 243mm (512 x 0.4746 = 243mm).</p>
<p>The slice spacing is 0.6mm and there are 427 images so the volume should be 0.6 x 427mm = 256mm in the superior - inferior direction.</p>
<p>But to keep things simple you should follow what lassoan said earlier and you should measure between two points on the model in slicer and see if this matches the 3d printed model. If the measurements in slicer are what you would expect but the 3d printed model is still smaller then the problem isnt in slicer, it must be something downstream like a scaling issue in the 3d printer software etc.</p>

---

## Post #13 by @Ramya_C (2020-02-04 00:41 UTC)

<p>Thanks all for the replies.<br>
However  I checked wit the 3d printer settings, we havenot done any scaling down before we print.<br>
The issue is the files created in STL format using 3D slicer has somehow shrink the dimension to 18cm. The original dimension is 24.2 cm.So we are not sure how the shrinking or size reduction happen.</p>
<p>The image dimensions after segmentation is 24.2cm which is same as the dimension of DICOM file. However the images in the STL file is 18cm, which is lesser compared to original. Is there anything that has caused the image shrink ?</p>

---

## Post #14 by @pieper (2020-02-04 00:59 UTC)

<p>I don’t know of anything that would cause that behavior.</p>
<p>Are you able to replicate the issue on public data?  If so can you post the exact steps?</p>

---

## Post #15 by @Ramya_C (2020-02-04 01:43 UTC)

<p>[quote=“Ramya_C, post:13, topic:10069, full:true”]<br>
Thanks all for the replies.<br>
However I checked wit the 3d printer settings, we havenot done any scaling down before we print.<br>
Thanks all for the replies.<br>
However I checked wit the 3d printer settings, we havenot done any scaling down before we print.<br>
The issue is the files created in STL format using 3D slicer has somehow shrink the dimension to 18cm. The original dimension is 24.2 cm.So we are not sure how the shrinking or size reduction happen.</p>
<p>The image dimensions after segmentation is 24.2cm which is same as the dimension of DICOM file. However the images in the STL file is 18cm, which is lesser compared to original. Is there anything that has caused the image shrink ?</p>

---

## Post #16 by @lassoan (2020-02-04 02:10 UTC)

<p>In the˝Export segment to files" window, did you change the “Size scale” value from the original 1.0? If you load the exported STL file back into Slicer, is its size correct? If you load the STL file into MeshLab and measure it there, is the size correct?</p>

---

## Post #17 by @JanWitowski (2020-02-04 16:10 UTC)

<p>Also, is there any way you could share your source image, segmentation .seg.nrrd file and exported STL for us to replicate the segmentation/export part?</p>

---

## Post #18 by @timeanddoctor (2020-02-05 05:47 UTC)

<p>Can you update the DICOM?</p>

---
