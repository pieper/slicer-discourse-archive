# Landmark to .ply misalignment when reloaded for editing

**Topic ID**: 45995
**Date**: 2026-01-30
**URL**: https://discourse.slicer.org/t/landmark-to-ply-misalignment-when-reloaded-for-editing/45995

---

## Post #1 by @emmm_m (2026-01-30 03:16 UTC)

<p>When I reload a saved markup file to it’s original .ply file to adjust a point which was incorrectly placed, the points appear entirely offset from the orientation of the scan. It appears as though the points are at about a 45 degree counterclockwise rotation from their original placement. Is there a way to fix this without redoing the entire file?</p>

---

## Post #2 by @muratmaga (2026-01-30 03:19 UTC)

<p>Where did you do the landmark and how did you save it? You shouldn’t have this type of problem if you did in Slicer.</p>

---

## Post #3 by @emmm_m (2026-01-30 03:27 UTC)

<p>landmarked in slicer and saved as a mrk.json file</p>

---

## Post #4 by @muratmaga (2026-01-30 03:30 UTC)

<p>I can’t replicate this on my end. When I load a model, create landmarks, save as mrk.json and then reload them everything lines up correctly.</p>
<p>Whats the version of the Slicer you are using? Is the model generated in slicer (e.g. from a segmentation) or is it external to Slicer? Is possible that model was under a transform while you are landmarking it (or vice versa)?</p>

---

## Post #5 by @emmm_m (2026-01-30 03:36 UTC)

<p>I am using model 5.10.0</p>
<p>This is the first time the issue has happened despite opening similar files for edits prior in that launch of the application. There were no transformations applied. and the model was created from a laser scan turned into a.ply in blender.</p>

---

## Post #6 by @muratmaga (2026-01-30 03:38 UTC)

<p>In a new slicer session, if you load that model, put some landmarks and save and reload them does it replicate (ie they are still off)?</p>
<p>Sorry I can’t think of what might do that beyond being under a transform.</p>

---
