# How to crop and save a cropped volume as one file?

**Topic ID**: 1654
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/how-to-crop-and-save-a-cropped-volume-as-one-file/1654

---

## Post #1 by @MichelODU (2017-12-12 22:17 UTC)

<p>Hello,</p>
<p>I have a really large DICOM dataset of a spine surgery patient, and I would like to crop it as well as save the cropped volume as a single mhd or nrrd file. When I try to do this, it produces a nrrd file for the first few slices, and each of them is massive (looks like a bug). I am trying to save in voxel format rather interpolating format… Is it possible to use Slicer that way to save a single volumetric file?</p>
<p>Btw, my problem with landmarks turns out to be that Slicer considers the orientation of the image axes while my deformable surface model program doesn’t (not an IJK vs RAS issue). I need to save it as a file format such as mhd that does not preserve the axes orientation, then acquire the landmarks with that volume.</p>
<p>Best wishes,</p>
<p>Michel</p>

---

## Post #2 by @lassoan (2017-12-12 22:39 UTC)

<aside class="quote no-group" data-username="MichelODU" data-post="1" data-topic="1654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbce88/48.png" class="avatar"> MichelODU:</div>
<blockquote>
<p>really large DICOM dataset of a spine surgery patient</p>
</blockquote>
</aside>
<p>Is it a CT? What are the dimensions and voxel size?</p>
<aside class="quote no-group" data-username="MichelODU" data-post="1" data-topic="1654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbce88/48.png" class="avatar"> MichelODU:</div>
<blockquote>
<p>for the first few slices, and each of them is massive</p>
</blockquote>
</aside>
<p>Do you mean the slices are interpolated to a much finer resolution?</p>
<aside class="quote no-group" data-username="MichelODU" data-post="1" data-topic="1654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbce88/48.png" class="avatar"> MichelODU:</div>
<blockquote>
<p>Is it possible to use Slicer that way to save a single volumetric file</p>
</blockquote>
</aside>
<p>Yes. This is a very common task.</p>
<aside class="quote no-group" data-username="MichelODU" data-post="1" data-topic="1654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bbce88/48.png" class="avatar"> MichelODU:</div>
<blockquote>
<p>Slicer considers the orientation of the image axes while my deformable surface model program doesn’t</p>
</blockquote>
</aside>
<p>Axis direction is just as important as image origin and spacing. It must be taken into account when processing an image. MetaIO image (mhd, mha), nrrd, nifti,… all store axis directions.</p>

---
