# Exporting 2 volumes as a stack of image files (PNG).

**Topic ID**: 20187
**Date**: 2021-10-16
**URL**: https://discourse.slicer.org/t/exporting-2-volumes-as-a-stack-of-image-files-png/20187

---

## Post #1 by @neuralnet (2021-10-16 22:29 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: N/A<br>
Actual behavior: N/A</p>
<p>Hi all,</p>
<p>I am very new to slicer and to medical imaging in general, so I apologize if this question is very obvious.</p>
<p>I have a pre-op MRI and post-op CT images for a patient. My goal is to display only the hardware from the CT, superimposed on the MRI.</p>
<p>I have already coregistered the images, and I have masked all the undesirable parts of the CT, isolating the hardware. When I look at my slices in the viewer in the three planes, what is displayed is perfect.</p>
<p>I was hoping to collect a stack of images (PNG or similar) from each view of the combined volumes. I was hoping to have each image be a slice through my volumes at a set slice separation. In the end I was hoping to have 3 image stacks: coronal, sagittal, transverse. In these images I am hoping to depict exactly what I see in the three viewing panels. My input images were not in DICOM format, but were NIFTI files.</p>
<p>Is this possible to do in a systematic way? I know that it is possible to capture a screenshot of a few slices, but I was hoping to generate all the images in one process.</p>
<p>Thank you so much for your help!</p>

---

## Post #2 by @pieper (2021-10-17 14:42 UTC)

<p>Sounds like the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html">ScreenCapture</a> module will do what you need.</p>

---

## Post #3 by @neuralnet (2021-11-12 22:25 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> , thank you so much for your reply. This did the trick! I appreciate it.</p>

---
