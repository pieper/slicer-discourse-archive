# Loading DICOM files

**Topic ID**: 11995
**Date**: 2020-06-11
**URL**: https://discourse.slicer.org/t/loading-dicom-files/11995

---

## Post #1 by @nsbosse (2020-06-11 21:37 UTC)

<p>Hi there, I have a few questions regarding the process for loading DICOM files.</p>
<p>Does Slicer’s DICOM reader apply the rescale slope/intercept prior to loading the intensity values into memory? What is the fallback strategy in the case when the DICOM header does not contain or has illegal rescale slope/intercept values?</p>
<p>Also, which class/method is responsible for loading DICOM images from disk? So far, I believe I’ve followed the code correctly from the AddArchetypeScalarVolume method in the vtkSlicerVolumesLogic.cxx file through to the ReadDataInternal method in the vtkMRMLVolumeArchetypeStorageNode class. It looks like there’s a vtkITKArchetypeImageSeriesReader that may load the data. Am I on the right track?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-06-11 23:50 UTC)

<p>Hi -</p>
<p>Yes, you are on exactly the right track for scalar volumes.  Slicer uses ITK to do the read, and if if there is rescale info in the header it is used.  If not I guess the values go straight through unchanged (you could check), but it’s a required tag so technically behavior is undefined.</p>
<p>Note that slicer lets you pick the GDCM or DCMTK implementations of ITK dicom, so the behavior might be slightly different (or rather, it is sometimes different in that they handle some border cases differently and that’s why we give you the option).</p>
<p>Note also that DICOMPlugin classes may interpret certain dicom instances differently, e.g. diffusion scans or segmentations, but the DICOMScalarVolume plugin uses the code you cited.</p>

---

## Post #3 by @nsbosse (2020-06-12 02:23 UTC)

<p>That’s helpful. Thanks a lot!<br>
Do you happen to know, would it be the DCMTKImageIO and GDCMImageIO classes that are responsible for doing the read from disk at the lowest level? I do see a read method in both classes, but I’m yet sure where they would be called from, so not positive yet.</p>

---

## Post #4 by @pieper (2020-06-12 12:10 UTC)

<p>Yes, those are the classes that are used in the end.  I agree the many layers can be quite hard to follow and reason about.  I suggest putting some breakpoints in those read methods and tracing through a bit to see what’s going on.</p>
<p>Do you have a particular issue you are investigating, or just learning?</p>

---

## Post #5 by @nsbosse (2020-06-12 15:11 UTC)

<p>Perfect. Thanks again. Personally, I’m learning. I’m a computer science co-op student. I’ve been trying to help my teammates verify some specifics about how DICOM files are loaded by studying the code from the point where it enters the C++ realm.</p>

---
