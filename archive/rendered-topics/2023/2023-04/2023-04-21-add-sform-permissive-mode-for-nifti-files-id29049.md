# Add SFORM_Permissive mode for nifti files

**Topic ID**: 29049
**Date**: 2023-04-21
**URL**: https://discourse.slicer.org/t/add-sform-permissive-mode-for-nifti-files/29049

---

## Post #1 by @Alexander_Kagan (2023-04-21 14:20 UTC)

<p>I currently have an issue with opening a large number of nifti ct scans from the dataset i’m working on (totalsegmentator dataset). it throws an error: “itk only supports orthonormal direction cosines. no orthonormal definition found”. its because more restrictive checks on the input file thay’ve added in the last itk versions: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/3994" class="inline-onebox" rel="noopener nofollow ugc">Nifti files with non-orthonormal directional cosines should be read and the error changed to a warning. · Issue #3994 · InsightSoftwareConsortium/ITK · GitHub</a><br>
Recently they have pushed a permissive mode to their code: <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/4009" class="inline-onebox" rel="noopener nofollow ugc">ENH: Added permissive mode to NIFTI reader by vfonov · Pull Request #4009 · InsightSoftwareConsortium/ITK · GitHub</a></p>
<p>Please, add the permissive_mode to the itk version sdslicer works with<br>
Is there any way i could update it manualy on my local installation of the 3d slicer?</p>
<p>thanks in advance</p>

---

## Post #2 by @pieper (2023-04-21 18:21 UTC)

<p>Hi - did you try with the latest preview version of Slicer?  I believe we resolved all these issues.</p>

---

## Post #3 by @jamesobutler (2023-04-21 18:47 UTC)

<p>The linked ITK PR that was recently merged would need to have the commits ba knotted to the Slicer ITK fork branch <a href="https://github.com/Slicer/ITK/commits/slicer-v5.3rc04-2022-09-19-62eb5ca" class="inline-onebox" rel="noopener nofollow ugc">Commits · Slicer/ITK · GitHub</a> or we move forward to use latest ITK code.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you know how you plan to proceed with finalizing the work associated with <a href="https://github.com/Slicer/ITK/commit/69e52f05c482012b95228c3fe46f299b1735ca99" class="inline-onebox" rel="noopener nofollow ugc">COMP: Add support for customizing ITK namespace (draft) · Slicer/ITK@69e52f0 · GitHub</a>. Would we keep carrying over these type of changes when we update Slicer’s ITK and SimpleITK versions?</p>

---
