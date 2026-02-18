# Compare two deformation fields

**Topic ID**: 13305
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/compare-two-deformation-fields/13305

---

## Post #1 by @mmtg (2020-09-02 19:46 UTC)

<p>Hello, hoping that this question hasn’t been answered elsewhere - having a hard time finding a solution. Not sure if this is a slicer question either, sorry if it isn’t</p>
<p>Let’s say that I have an image set with a known deformation field. I want to load it into various applications, perform a deformable registration, and then compare to the known dataset. I get dicoms out of this.</p>
<p>I was wondering if Slicer had a way to natively do this, quantitatively i.e., through a difference of transforms or something - or do I need to code this myself? I was just trying to avoid having to fiddle with the coordinate systems used and making sure that it was working correctly if there was already a solution out there. I tried using the python API and getting a numpy array of the grid transform but it seems to just spit out what was in the DICOM header adjusted for the difference between slicers coordinates and the dicom coordinate system. I think I need to get the physical location of each vector point to compare two deformation fields since different software use different control point locations.</p>
<p>Hopefully that makes sense, thanks for your help - sorry if this isn’t a slicer question!</p>

---
