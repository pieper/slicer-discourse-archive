# Rescale slope and rescale intercept information on a Nifti image

**Topic ID**: 43882
**Date**: 2025-07-29
**URL**: https://discourse.slicer.org/t/rescale-slope-and-rescale-intercept-information-on-a-nifti-image/43882

---

## Post #1 by @imbeatriz (2025-07-29 12:28 UTC)

<p>Hi everyone,</p>
<p>I have PET images that were originally in DICOM format but have been converted to NIfTI using 3D Slicer. Unfortunately, I have no access to the original DICOM files.</p>
<p>I’m trying to determine whether the images are already scaled in Bq/mL. Does 3D Slicer apply the rescale slope and intercept during the DICOM to NIfTI conversion? And is there still a way to check the original rescale slope and intercept values after conversion?</p>
<p>Thank you in advance</p>

---

## Post #2 by @cpinter (2025-07-29 14:07 UTC)

<p>Slicer applies the rescale/intercept values to the volume, and then these values are “lost”, meaning that they are not kept anywhere other than the original DICOM tags. So when you save it to Nifti, there will be no way to recover them.</p>
<p>I’m almost certain about this, but I haven’t checked the code, so maybe if someone else can confirm this… Thanks.</p>

---

## Post #3 by @imbeatriz (2025-07-29 14:24 UTC)

<p>Hi,</p>
<p>Thank you for the information. Do you know another way I could possibly check if the image is already in Bq/mL?</p>

---

## Post #4 by @cpinter (2025-07-29 16:04 UTC)

<p>I know very little about PET. What I’d do is check the scalar range, but not sure if there are other units in the same or adjacent magnitude. In any case I think confirming it 100% objectively is not possible.</p>

---

## Post #5 by @pieper (2025-07-30 16:33 UTC)

<p>In the raw dicom pet study I have seen there are often two series, one with uncorrected (raw) data, and one with attenuation correction applied.  There’s a <a href="https://dicom.innolitics.com/ciods/enhanced-pet-image/enhanced-pet-corrections/00189759">dicom tag indicating which is</a> is which, but of course this won’t be in your nifti file so you can’t really know unless the filename somehow indicates it (e.g. the corrected one may have ‘ac’ in the series description which is sometimes in the filename).  Also there are different ways that it may have been mapped to SUV, which you may not be able to easily detect without knowing the full history of the data.</p>

---
