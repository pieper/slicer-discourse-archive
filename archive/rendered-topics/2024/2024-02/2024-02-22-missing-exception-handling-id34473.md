---
topic_id: 34473
title: "Missing Exception Handling"
date: 2024-02-22
url: https://discourse.slicer.org/t/34473
---

# Missing exception handling

**Topic ID**: 34473
**Date**: 2024-02-22
**URL**: https://discourse.slicer.org/t/missing-exception-handling/34473

---

## Post #1 by @Heiko_Stark (2024-02-22 11:45 UTC)

<p>Slicer is not able to load a malformed nii.gz file in 5.6.1, which is possible with version 4.8. Missing error message: only visible in logging window and cryptic. A meaningful error message or more tolerant loading would be welcome (malformed files will occur again and again).</p>
<p>“Slicer has caught an application error, please save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: /work/Stable/Slicer-0-build/ITK/Modules/IO/NIFTI/src/itkNiftiImageIO.cxx:2100:\nITK ERROR: ITK only supports orthonormal direction cosines.  No orthonormal definition found!”</p>

---

## Post #2 by @pieper (2024-02-22 15:56 UTC)

<p>Thanks for reporting this.  It’s probably good that newer versions of ITK are more careful about interpreting nifti variants, as this has been an ongoing source of confusion.  I don’t think we should push back in that, but instead offer a more robust nifti loader that as you suggest is more user-friendly in pointing out bad data and offering loading solutions.  This would be a chance to handle other variants nifti types, like time series.</p>
<p>I did a prototype of a <a href="https://github.com/SlicerDMRI/SlicerDMRI/compare/master...pieper:SlicerDMRI:nifiio">python-based reader for diffusion MRI</a> that could be used as a starting point.  It would be great if people who rely on nifti in their workflows could pick up and generalize this to support their needs.  Perhaps even a dedicated module like <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219">RawImageGuess</a> or <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks</a> would help people deal with some not-uncommon issues like left-right flip, qform/sform disagreement, or making use of intent types.</p>

---
