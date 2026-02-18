# 3D+t - Longitudinal Volume Comparison - is there an option?

**Topic ID**: 30981
**Date**: 2023-08-04
**URL**: https://discourse.slicer.org/t/3d-t-longitudinal-volume-comparison-is-there-an-option/30981

---

## Post #1 by @SlicerDicer (2023-08-04 17:56 UTC)

<p>Hello everyone,</p>
<p>thank you very much for your time, I have been enjoying Slicer and its features very much.</p>
<p>Similarly to <a href="https://discourse.slicer.org/t/link-views-in-three-over-three-configuration/24564">Linking_Views</a>, I have been using the CompareVolume Feature for registered images, and it is very helpful.</p>
<p>In a current project I am working on, we need to have another dimension (which is time, so 3D+t).<br>
While we can load multiple volumes in the view (similar to the link we shared), we would like to have an option where we can use a slider in the time domain, only having one view  / or one timepoint(i.e. axial-sag-cor, and a slider for the time). This allows one to select a specific slice (i.e. to explore growth of a lesion), and to quickly jump between the different timepoints.</p>
<p>Can this be done, and if not how easy would it be to be implement (I am thinking of collaboration here).</p>
<p>Best regards!</p>

---

## Post #2 by @pieper (2023-08-04 20:43 UTC)

<p>You should be able to use CompareVolumes together with Sequences for this.  If you set up the Proxy nodes to as the volume in CompareVolumes it should automatically update.  Let us know how it goes for you.</p>

---

## Post #3 by @lassoan (2023-08-05 10:31 UTC)

<p>You may need to modify in application settings / DICOM to load time sequences as “volume sequence" (not MultiVolume). You can browse Sequences using the sequence browser toolbar.</p>
<p>You can compare two time points by loading the same time sequence twice. Or - if the sequence is very large or you are low in memory - you can load the sequence only once and then create a “sequence browser” in Sequences module and add the loaded sequence to that browser. Each browser allo s you to show one time point of thr sequence.</p>

---
