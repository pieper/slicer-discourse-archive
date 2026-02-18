# Extracting vtk streamlines

**Topic ID**: 3840
**Date**: 2018-08-19
**URL**: https://discourse.slicer.org/t/extracting-vtk-streamlines/3840

---

## Post #1 by @Vinny (2018-08-19 23:36 UTC)

<p>Hi,</p>
<p>I have a set of streamlines in vtk format that I’ve imported into 3d Slicer and also created a spherical model of 2 mm radius in 3d Slicer and saved it in vtk format.  In the tri-planar views, I can see the cross section of the sphere in the axial/sagittal/coronal slices of the sphere model and the numerous points of the streamlines.  What I’d like to do is filter out, i.e., select, streamlines that pass through the spherical model.  Is there a module to do this in Slicer?  Or if it has to be done programmatically in Python, what are the best vtk classes to do this type of operation?</p>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2018-08-20 00:55 UTC)

<p>There are several options. Are the streamlines result of CFD simulation or tractography? Do you need to select lines that are passing through a certain location or it is OK to assign an ID number to each line and display lines in a specific ID range?</p>

---

## Post #3 by @Vinny (2018-08-20 01:01 UTC)

<p>these are tractography streamlines that were generated externally and i’d like to select a subset of these streamlines that pass through a sphere at defined location(s).</p>

---

## Post #4 by @rkikinis (2018-08-20 01:24 UTC)

<p>The tractography tools in the dMRI extension offer a variety of selection options out of the box, including brick shaped ROI’s that are customizable in shape and location.</p>

---

## Post #5 by @Vinny (2018-08-20 11:55 UTC)

<p>Thanks for your help, I will try this out.</p>

---

## Post #6 by @Vinny (2018-08-21 01:50 UTC)

<p>Hi,</p>
<p>I was able to utilize the tractography tools in the dMRI extension for the imported vtk streamlines.  I had generated a spherical model (in vtk format) in 3d Slicer and convert the sphere model into a label map in order to run tractography for these imported streamlines (using the Tractography ROI selection module).  Is there a way to select streamlines that pass through the model itself without having to convert it to a label map?  I noticed for the ‘Tractography seeding’ module, there is an option for use of a model as an input; however, it requires a DIffusionTensorVolume generated from the 3d Slicer workflow, which I don’t have.</p>
<p>Thanks</p>

---
