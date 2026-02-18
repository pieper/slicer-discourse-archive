# Add a label to the 3D glyph

**Topic ID**: 24171
**Date**: 2022-07-04
**URL**: https://discourse.slicer.org/t/add-a-label-to-the-3d-glyph/24171

---

## Post #1 by @riep (2022-07-04 15:31 UTC)

<p>Hi all,<br>
I am using the 3D glyph to orient and position a plane. It would be interesting to me to be able to add a label on the red axis, for instance (see figure, where a “P” is always visible along the red axis).<br>
I have tried using a MRML markup fiducial and updating its position according to the transform matrix of the plane node. But it would be cleaner to implement something at a lower level (in vtk).<br>
Could you please advise me on this topic if you have already done similar things?</p>
<p>Thank you very much for any help!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86165b5fdeb46ab49a43614f32e6f5981794218a.png" alt="Screenshot from 2022-07-04 17-24-05" data-base62-sha1="j8bSAOAgqZpvQdqFNGg2d6qBTrI" width="469" height="380"></p>

---

## Post #2 by @lassoan (2022-07-06 00:55 UTC)

<p>I see that this feature would be useful but it is not currently available. It would be nice if you could implement it.</p>
<p>It would require storing axis names in the <code>vtkMRMLMarkupsNode</code> and display in <code>vtkSlicerMarkupsWidgetRepresentation</code>.</p>

---

## Post #3 by @riep (2022-07-06 06:13 UTC)

<p>Thanks this will definitely help me to implement this.</p>

---

## Post #4 by @cpinter (2023-06-02 08:19 UTC)

<p>Just to follow up, we have a basic implementation working (also thanks to <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> for his help with 2D visibility of the labels), and after some cleanup I’ll do a PR soon.</p>

---
