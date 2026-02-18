# Is camera linking broken in 4.10.1?

**Topic ID**: 5668
**Date**: 2019-02-07
**URL**: https://discourse.slicer.org/t/is-camera-linking-broken-in-4-10-1/5668

---

## Post #1 by @muratmaga (2019-02-07 04:41 UTC)

<p>I can’t seem to link cameras in dual view in 4.10.1<br>
Steps:<br>
Choose Dual 3D layout<br>
Switch to cameras module,<br>
View1 choose create new camera<br>
View2 choose camera_1 (or the newly created camera)<br>
Go back to View1 and see that there is no camera selected anymore. This is the warning given:</p>
<p>Warning: In D:\D\S\Slicer-4101\Libs\MRML\Core\vtkMRMLCameraNode.cxx, line 474</p>
<p>vtkMRMLCameraNode (00000221EC25DF60): SetActiveTag: vtkMRMLCameraNode3 found another node vtkMRMLCameraNode2 with the tag vtkMRMLViewNode2</p>

---

## Post #2 by @lassoan (2019-02-07 12:51 UTC)

<p>You can link cameras by clicking “Link/unlink…” button in the 3D view controller.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2519f5226d14265e9a6a1ab6e8dbddc1f438889.png" alt="image" data-base62-sha1="prtRCl1G5O9FTst9slHm02sr8A9" width="525" height="337"></p>
<p>I think camera linking by choosing the same camera in multiple views was an unintended side effect (maybe even a bug), because one camera is supposed to be linked with one view.</p>

---

## Post #3 by @muratmaga (2019-02-07 16:46 UTC)

<p>Thanks! So, I was using a bug as a feature, huh.</p>
<p>I tried the link, rotations and pans work fine, but not the zoom. Is that also intended?</p>

---
