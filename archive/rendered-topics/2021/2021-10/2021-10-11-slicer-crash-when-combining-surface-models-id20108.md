# Slicer crash when combining surface models

**Topic ID**: 20108
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/slicer-crash-when-combining-surface-models/20108

---

## Post #1 by @mikebind (2021-10-11 22:58 UTC)

<p>I have a reproducible Slicer crash when trying to combine two surface models using the Combine Models module. The models were both created by converting from segmentation segments, and one of them has been cut using the Plane Cut capabilities of Dynamic Modeler.  I have tried running the “Clean” and “Compute Surface Normals” with auto-orient steps from the Surface Toolbox on each model, but still get a crash when trying to combine them.   Any suggestions?  The model files are available <a href="https://www.dropbox.com/sh/ael0c6hw8xs7nb8/AABuDKGnZUGQ0o47gjTzQlsRa?dl=0" rel="noopener nofollow ugc">here</a> if anyone is willing to take a look at them.  Thanks!</p>

---

## Post #2 by @lassoan (2021-10-13 03:00 UTC)

<p>Combine models module is a thin wrapper over <a href="https://github.com/zippy84/vtkbool">vtkbool</a>. Please report the issue there and for future reference, add a link here to the bug report.</p>

---

## Post #3 by @mikebind (2021-10-13 16:50 UTC)

<p>Thanks, I reported this at <a href="https://github.com/zippy84/vtkbool/issues/46" class="inline-onebox" rel="noopener nofollow ugc">Crash on combining certain models · Issue #46 · zippy84/vtkbool · GitHub</a></p>

---

## Post #4 by @JuanPinera (2024-08-30 14:04 UTC)

<p>Hi Andras,</p>
<p>We encountered this same error in the past, and over time you managed to fix it in the 5.0.x versions. In those versions, when “Combine Models” encounters an error, it generates an empty model, and Slicer continues working. However, I recently tried updating to the Stable 5.6.2 version and am experiencing the same problem as before when an error occurs, Slicer closes.</p>
<p>I understand this was a bug that was previously fixed and has now reappeared. Is there anything I can do to resolve this?</p>

---

## Post #5 by @lassoan (2024-08-30 18:43 UTC)

<p>A <a href="https://github.com/PerkLab/SlicerSandbox/pull/33">workaround is already available in Sandbox extension</a> that you can easily apply to your Combine Models module. We haven’t integrated it because a <a href="https://github.com/zippy84/vtkbool/issues/43#issuecomment-2286445279">better fix was provided in vtkbool</a>.</p>
<p>If the vtkbool fix works then we’ll use that and drop the workaround in the Sandbox. Testing this takes some time, so have to wait a few weeks (or you can help out by building Slicer and the Sandbox extension and testing if the vtkbool fix solves your problem).</p>

---
