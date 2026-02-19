---
topic_id: 9515
title: "Self Registration"
date: 2019-12-16
url: https://discourse.slicer.org/t/9515
---

# Self-registration?

**Topic ID**: 9515
**Date**: 2019-12-16
**URL**: https://discourse.slicer.org/t/self-registration/9515

---

## Post #1 by @Nathan (2019-12-16 14:30 UTC)

<p>Often in multi-slice MRI, the acquisitions of every other image are acquired separately. Whenthe patient moves between acquisitions, 3D reconstructions are problematic.</p>
<p>I am going through images of patients with tremor where such motion is common. Is there a slicer module to register every-other image to each other?</p>
<p>I’ve tried searching for this but haven’t found the right keywords.</p>
<p>-N</p>

---

## Post #2 by @pieper (2019-12-16 14:44 UTC)

<p>I don’t think we have anything specific for that in Slicer.  If you look for <code>motion correction</code> for MRI you’ll find a lot of tools from the fMRI community that address that problem.  We used to do some fMRI in Slicer, but there are already so many good tools we didn’t see a need to duplicate efforts.</p>

---

## Post #3 by @lassoan (2019-12-19 20:22 UTC)

<p>Do you have patient motion while a 3D volume is being acquired, or between acquisitions of 3D volumes? You can use “Sequence registration” extension for motion-compensation of 3D volumes, but we don’t have convenient solution to align 2D images within an image stack.</p>

---

## Post #4 by @Nathan (2019-12-23 19:18 UTC)

<p>Unfortunately the motion is within the image stack. I’ll try making two series each with every other image and registering them.</p>

---

## Post #5 by @lassoan (2019-12-23 19:33 UTC)

<p>You may be able to load each timepoint as a separate volume if you enable loading DICOM subseries by time (menu: Edit / Application settings / DICOM / Allow loading subseries by time -&gt; enable), then in DICOM module, enable “Advanced” mode, click “Examine”, and then choose the time points that you would like to load. It is possible that each frame will show up as a separate timepoint, but it is worth a try.</p>
<p>If you can share an example data set (phantom or anonymized data set) then we may can try if we can find an easy way to load these.</p>

---
