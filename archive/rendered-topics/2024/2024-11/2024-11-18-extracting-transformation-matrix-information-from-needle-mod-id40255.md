---
topic_id: 40255
title: "Extracting Transformation Matrix Information From Needle Mod"
date: 2024-11-18
url: https://discourse.slicer.org/t/40255
---

# Extracting transformation matrix information from needle models overlaid on ultrasound images

**Topic ID**: 40255
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/extracting-transformation-matrix-information-from-needle-models-overlaid-on-ultrasound-images/40255

---

## Post #1 by @Sangrok (2024-11-18 21:00 UTC)

<p>Hello.<br>
Using 3D Slicer, I implemented the registration of ultrasound images and OTS data, overlaying a cyan-colored needle model on the ultrasound images. As shown in the figure below, I want to extract the needle tip position and angle of the needle model in pixel coordinates relative to the ultrasound image.<br>
The extracted information is intended to be used as ground truth for evaluating the performance of an ultrasound-based needle detection algorithm.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1fe7d663eff59d477ee40f87b942b8700306286.jpeg" data-download-href="/uploads/short-url/ywMjmFsKq7pjqO2XCWepKSULOHc.jpeg?dl=1" title="Fig62" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fe7d663eff59d477ee40f87b942b8700306286_2_690x192.jpeg" alt="Fig62" data-base62-sha1="ywMjmFsKq7pjqO2XCWepKSULOHc" width="690" height="192" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fe7d663eff59d477ee40f87b942b8700306286_2_690x192.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fe7d663eff59d477ee40f87b942b8700306286_2_1035x288.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1fe7d663eff59d477ee40f87b942b8700306286_2_1380x384.jpeg 2x" data-dominant-color="4D4D50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fig62</span><span class="informations">3043×851 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Currently, the data hierarchy is as follows:</p>
<p>Image_Transducer             ← Ultrasound Image<br>
ProbeToImage                   ← Pointer Calibration Result<br>
└NeedleToProbe               ← OTS Data<br>
└NeedleTipToNeedle      ← Pivot Calibration Result<br>
└NeedleModel</p>
<p>I receive image data (Image_Transducer) from the ultrasound device and transformation matrix data (NeedleToProbe) from OTS using markers attached to the needle.<br>
Transformation matrices, such as NeedleTipToNeedle and ProbeToImage, have been calculated using pivot and pointer calibrations.<br>
I have been using the GetMatrixTransformToParent() function of the vtkMRMLTransformNode class in the Python console of 3D Slicer, but I am not obtaining the desired data. The extracted values are not in the pixel coordinate system of the ultrasound image.<br>
I need guidance on how to extract the desired information from the data.</p>

---
