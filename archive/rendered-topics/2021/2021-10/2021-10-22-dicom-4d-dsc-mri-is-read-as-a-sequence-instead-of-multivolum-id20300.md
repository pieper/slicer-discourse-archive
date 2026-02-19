---
topic_id: 20300
title: "Dicom 4D Dsc Mri Is Read As A Sequence Instead Of Multivolum"
date: 2021-10-22
url: https://discourse.slicer.org/t/20300
---

# DICOM 4D DSC MRI is read as a Sequence instead of MultiVolume

**Topic ID**: 20300
**Date**: 2021-10-22
**URL**: https://discourse.slicer.org/t/dicom-4d-dsc-mri-is-read-as-a-sequence-instead-of-multivolume/20300

---

## Post #1 by @kliron (2021-10-22 13:52 UTC)

<p>The title is pretty self-explanatory. I have a time series of 3D Volumes (DSC perfusion MRI images) and try to load them in 3D Slicer (latest stable version 4.11.20210226). This is something I have done successfully before, multiple times. When I switch to MultiVolume Explorer module no MRLMultiVolume is found in the drop-down “Input mutlivolume” menu. I only see the first slice from my series. When I switch to the Sequences module, I see a list of 1000 images (that’s the correct number of images what would otherwise be a MultiVolume of 50 images per frame). Is there a way to combine those images into a MultiVolume that 3D Slicer understands and can work with?</p>

---

## Post #2 by @lassoan (2021-10-22 13:58 UTC)

<p>We are in the process of replacing MultiVolume with the more generic Sequences infrastructure. Since there are a few features that havnot been ported to Sequences yet, we haven’t removed MultiVolume, and you can still choose to load time series as either a Volume Sequence or a Multivolume (if you check the “Advanced” checkbox in the DICOM browsee). You can also change how time series are loaded by default in Application Settings.</p>
<p>What feature do you use in MultiVolume that you don’t find for Volume Sequences?</p>

---

## Post #3 by @kliron (2021-10-22 19:37 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, I was able to load my series as a MultiVolume with your help. What I find useful in MultiVolume is that series are separated into time steps where in each step the entire 3D brain volume can be scrolled through. So I can quickly move back and forth through time with the slider and space through mouse scrolling. Sequences instead load the entire series as a flat list of slices where I need to remember the exact index in the list where the first slice of a specific time point of interest exists.</p>
<p>I am also having a problem with the Sequences module not “focusing” on my slices correctly in the slice viewer window. When I step to the next slice, the window is all black background and the slider on top is either all the way to the right or to the left. I need to pull the slider to the middle for it to “focus” on my slice correctly. This may have to do with the fact that in some exams slices are not equally spaced, I’m not sure, but this problem does not exist with MultiVolume.</p>

---

## Post #4 by @lassoan (2021-11-29 14:19 UTC)

<aside class="quote no-group" data-username="kliron" data-post="3" data-topic="20300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/c6cbf5/48.png" class="avatar"> kliron:</div>
<blockquote>
<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, I was able to load my series as a MultiVolume with your help. What I find useful in MultiVolume is that series are separated into time steps where in each step the entire 3D brain volume can be scrolled through. So I can quickly move back and forth through time with the slider and space through mouse scrolling. Sequences instead load the entire series as a flat list of slices where I need to remember the exact index in the list where the first slice of a specific time point of interest exists.</p>
</blockquote>
</aside>
<p>Volume Sequences and MultiVolume both provide browsing of 3D volumes. They are both provided by the “MultiVolumeImporterPlugin” DICOM plugin. The single-slice representation is loaded by “DICOMImageSequencePlugin”.</p>
<aside class="quote no-group" data-username="kliron" data-post="3" data-topic="20300">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/c6cbf5/48.png" class="avatar"> kliron:</div>
<blockquote>
<p>I am also having a problem with the Sequences module not “focusing” on my slices correctly in the slice viewer window. When I step to the next slice, the window is all black background and the slider on top is either all the way to the right or to the left. I need to pull the slider to the middle for it to “focus” on my slice correctly. This may have to do with the fact that in some exams slices are not equally spaced, I’m not sure, but this problem does not exist with MultiVolume.</p>
</blockquote>
</aside>
<p>Sequences module can browse both volumes (the same way as MultiVolume exlorer module) and single moving slices (imported by DICOMImageSequencePlugin). Usually moving slices are less useful, but if you want to browse moving slices then you need to make the slice views automatically move where the slices go. You can make the slices follow the images by using “Volume reslice driver” module in SlicerIGT extension.</p>
<p>If you have 4D volumes acquired with with parallel slices with varying slice spacing then an AcquisitionTransform is supposed to be created, which transforms each slice into its correct position. If you acquire images with rotating slices then you can need to load it using the DICOMImageSequencePlugin and use the “Reconstruct 4D cine MRI” module in SlicerHeart extension to reconstruct 4D volume (sequence of 3D Cartesian volumes).</p>

---
