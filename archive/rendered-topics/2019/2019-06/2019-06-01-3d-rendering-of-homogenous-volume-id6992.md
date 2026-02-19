---
topic_id: 6992
title: "3D Rendering Of Homogenous Volume"
date: 2019-06-01
url: https://discourse.slicer.org/t/6992
---

# 3d rendering of homogenous volume

**Topic ID**: 6992
**Date**: 2019-06-01
**URL**: https://discourse.slicer.org/t/3d-rendering-of-homogenous-volume/6992

---

## Post #1 by @asch (2019-06-01 22:16 UTC)

<p>Hi, I’m trying to render a uniform scalar volume in 3D using python scripting.<br>
I managed to load the volume and visualize it in the slice viewer, but in the 3D view the volume is completely transparent.<br>
The volume is filled with ones, hence the Scalar Range is [1,1].<br>
I tried to use the GUI, but I cannot play with the threshold and change it.<br>
Any suggestions?<br>
Thanks for your help,<br>
AS</p>
<p>Operating system: mac os and linux<br>
Slicer version: 4.10</p>

---

## Post #2 by @pieper (2019-06-02 20:19 UTC)

<p>Hi -</p>
<p>If the volume is truly all ones then what do you expect to see when you volume render it?</p>

---

## Post #3 by @asch (2019-06-04 12:44 UTC)

<p>Hi, I “expect” to see a uniform box (maybe white) against the dark background.<br>
The volume represents a tank of water through which charged particle are transported and deposit their energy. Such a water box is used in radiation therapy to verify a treatment plan prior to delivery to the patient. So the treatment plan is the same, but the patient CT scan is replaced with water.<br>
The dose map and the density map look like this in the Slice view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aba54b16cf0d44ae504e51ec60fdd673b7b2a0d.png" data-download-href="/uploads/short-url/8nwU7N9Y6HDjAyebgexG7YChDCB.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aba54b16cf0d44ae504e51ec60fdd673b7b2a0d_2_611x500.png" alt="screenshot" data-base62-sha1="8nwU7N9Y6HDjAyebgexG7YChDCB" width="611" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aba54b16cf0d44ae504e51ec60fdd673b7b2a0d_2_611x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aba54b16cf0d44ae504e51ec60fdd673b7b2a0d_2_916x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aba54b16cf0d44ae504e51ec60fdd673b7b2a0d.png 2x" data-dominant-color="323B4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">998×816 82.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-06-04 17:25 UTC)

<p>Volume rendering should work well if you load this discrete volume as a labelmap volume (or convert it to a labelmap volume in Volumes module). For scalar volumes, the volume renderer seems to require boundary voxels to be transparent.</p>
<p>Volume rendering may be an overkill for rendering a cube (unless you need volumetric semi-transparent “fog” effect). If displaying a hollow cube is enough then you can use an ROI box or you can create a model of a box - using SlicerIGT extension’s Create models module, or by writing a few lines of Python code (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_simple_surface_mesh_as_a_model_node" rel="nofollow noopener">example</a>). You may also load your volume as a segmentation node, which can be displayed both in 2D and 3D views, too.</p>

---
