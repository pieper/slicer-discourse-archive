# Is it possible to resample a volume along a different set of axes?

**Topic ID**: 21860
**Date**: 2022-02-08
**URL**: https://discourse.slicer.org/t/is-it-possible-to-resample-a-volume-along-a-different-set-of-axes/21860

---

## Post #1 by @MJJ (2022-02-08 22:55 UTC)

<p>I have a scalar volume.<br>
I want to resample this volume along a different set of axes using linear interpolation.<br>
Is this possible?<br>
If so, how?</p>
<p>I’ve looked into using <code>slicer.modules.resamplescalarvolume</code> but I can’t seem to figure out how to use it to get what I need.</p>

---

## Post #2 by @mikebind (2022-02-09 00:30 UTC)

<p>The “Crop Volume” module allows resampling as well as cropping.  The rectilinear ROI you specify defines the output image volume’s spatial extent and its orientation.  You can apply a transform to the ROI to rotate it with respect to the original image volume, or, if you are using a more recent preview release of Slicer, you can use the interactive markups ROI control handles for better manual control of the orientation.</p>

---
