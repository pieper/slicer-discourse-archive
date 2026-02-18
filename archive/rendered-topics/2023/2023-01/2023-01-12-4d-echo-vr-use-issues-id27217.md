# 4D Echo VR use issues

**Topic ID**: 27217
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/4d-echo-vr-use-issues/27217

---

## Post #1 by @rlinke (2023-01-12 20:21 UTC)

<p>I wanted to reach out about our recent challenges viewing 4D echo in VR utilizing Slicer. We are able to get the 3D data into Slicer, but we are only getting one time point of the cardiac cycle. We are taking 3D acquisitions scanned on a Philips-EpiQ echo machine. We are exporting the data from the machine as Dicom converting it in Philips Qlab software to cartesian dicom and then pulling into 3D Slicer for 3D visualization. We have also tried to load the dicom export directly from the machine into Slicer with the same results. Any help would be much appreciated!</p>

---

## Post #2 by @rlinke (2023-02-10 16:41 UTC)

<p>Is anyone having success with Philips Echo machines and using Slicer to view Valves in VR?</p>

---

## Post #3 by @lassoan (2023-02-15 06:58 UTC)

<p>Yes, we use Philips QLab-exported 4D ultrasound volumes every day.</p>
<p>By VR do you mean volume rendering or virtual reality?</p>

---

## Post #4 by @rlinke (2023-02-20 13:44 UTC)

<p>Virtual Reality. We get beautiful volume renders, but for some reason we are not getting more than a single phase.</p>

---

## Post #5 by @rlinke (2023-08-24 14:10 UTC)

<p>Good morning Andras. We have tried multiple studies and have had no luck. Can I ask your specific workflow on how you transfer images to Qlab and what export file type you select in Qlab?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2023-08-24 14:59 UTC)

<p>See detailed instructions for QLab export <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#import-philips-4d-cardiac-images">here</a>.</p>

---

## Post #7 by @rlinke (2023-08-24 15:48 UTC)

<p>We just went through the process step by step and I am unable to upload the Qlab exported file using the Dicom import function. I have to use the Data import. It appears a a single dicom file not a folder with multiple files inside. Does this help shed any light onto our issue? I have the same issue if I try to use the Philips patcher. Does this give you any indicator as to what might be wrong? We truly appreciate the assistance!</p>

---

## Post #8 by @lassoan (2023-08-24 15:54 UTC)

<p>You need to remove the unpatched file from the database, patch the file, then import it. The DICOM Patcher module can also write a .nrrd file that you can load directly (without the DICOM module).</p>

---
