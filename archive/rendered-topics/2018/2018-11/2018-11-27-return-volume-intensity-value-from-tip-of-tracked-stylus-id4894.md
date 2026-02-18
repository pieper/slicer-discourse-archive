# Return volume intensity value from tip of tracked stylus

**Topic ID**: 4894
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/return-volume-intensity-value-from-tip-of-tracked-stylus/4894

---

## Post #1 by @banderies (2018-11-27 19:06 UTC)

<p>Hello all,</p>
<p>I am using a Polaris Vicra and SlicerIGT to track a NDI stylus/pointer, and I would like to return the intensity value from a volume at the tip of the stylus (the StylusTipToStylus transform). I am sure that there is a built in function for this, but have been unable to locate it. I would greatly appreciate it if someone could point me in the right direction.</p>
<p>Thanks and best regards,<br>
Barrett</p>

---

## Post #2 by @lassoan (2018-11-28 05:52 UTC)

<p>These two examples should contain all that you need:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_transform_is_modified" rel="nofollow noopener">Observe a transform, get RAS (world) position</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" rel="nofollow noopener">Get voxel value from RAS position</a></li>
</ul>

---

## Post #3 by @banderies (2018-12-03 03:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> That worked, thanks!</p>

---
