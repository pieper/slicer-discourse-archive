---
topic_id: 27356
title: "Load Directory Leaves Off A File"
date: 2023-01-19
url: https://discourse.slicer.org/t/27356
---

# Load Directory Leaves Off a File

**Topic ID**: 27356
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/load-directory-leaves-off-a-file/27356

---

## Post #1 by @rhodesdante (2023-01-19 16:35 UTC)

<p>I was trying to use the     Add Data → Choose Directory to Add    button to load in some .nrrd files, but every time I try this, the loader always misses a single file. I checked the log, and it gives the error “There is more than one file, use the vtkITKArchetypeImageSeriesReader instead” as soon as the files begin to load. There is nothing unique in name or content about the file that is missing, and the others import just fine. Is this a bug in the importer? Thanks for your help</p>

---

## Post #2 by @pieper (2023-01-19 16:43 UTC)

<p>Please let us know the names of the files in question.  Sometimes the heuristics in the readers will try to treat multiple files as one volume to reflect the way some people organize their data across files (e.g. using filename numbers to indicate that a series of image files form a volume).</p>

---

## Post #3 by @rhodesdante (2023-01-19 17:16 UTC)

<p>I wasn’t able to load in exactly the same files, but I found a new set and posted their names below. I had a similar issue in that the files “PatientX_RLGB_Long_plac1_vol2_diag” and “PatientX_RLGB_Long_plac1_vol3_diag” were missing, though this time no error was thrown.</p>
<p>PatientX_RLGB_Long_plac1_vol1_diag.nrrd<br>
PatientX_RLGB_Long_plac1_vol1_MPLL.nrrd<br>
PatientX_RLGB_Long_plac1_vol2_diag.nrrd<br>
PatientX_RLGB_Long_plac1_vol2_MPLL.nrrd<br>
PatientX_RLGB_Long_plac1_vol3_diag.nrrd<br>
PatientX_RLGB_Long_plac1_vol3_MPLL.nrrd<br>
PatientX_RLGB_Long_plac2_vol1_diag.nrrd<br>
PatientX_RLGB_Long_plac2_vol1_MPLL.nrrd<br>
PatientX_RLGB_Long_plac2_vol2_diag.nrrd<br>
PatientX_RLGB_Long_plac2_vol2_MPLL.nrrd<br>
PatientX_RLGB_Long_plac2_vol3_diag.nrrd<br>
PatientX_RLGB_Long_plac2_vol3_MPLL.nrrd<br>
PatientX_RLGB_Long_plac3_vol1_MPLL.nrrd<br>
PatientX_RLGB_Long_plac3_vol2_MPLL.nrrd<br>
PatientX_RLGB_Long_plac3_vol3_MPLL.nrrd<br>
PatientX_RLGB_Long_plac4_vol1_MPLL.nrrd<br>
PatientX_RLGB_Long_plac4_vol2_MPLL.nrrd<br>
PatientX_RLGB_Long_plac4_vol3_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac1_vol1_diag.nrrd<br>
PatientX_RLGB_Transverse_plac1_vol1_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac1_vol2_diag.nrrd<br>
PatientX_RLGB_Transverse_plac1_vol2_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac1_vol3_diag.nrrd<br>
PatientX_RLGB_Transverse_plac1_vol3_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac2_vol1_diag.nrrd<br>
PatientX_RLGB_Transverse_plac2_vol1_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac2_vol2_diag.nrrd<br>
PatientX_RLGB_Transverse_plac2_vol2_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac2_vol3_diag.nrrd<br>
PatientX_RLGB_Transverse_plac2_vol3_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac3_vol1_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac3_vol2_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac3_vol3_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac4_vol1_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac4_vol2_MPLL.nrrd<br>
PatientX_RLGB_Transverse_plac4_vol3_MPLL.nrrd</p>

---

## Post #4 by @pieper (2023-01-19 18:54 UTC)

<p>yes, these are the kinds of filenames that may trigger the grouping heuristics.  Probably the easiest is to just put the files into separate directories to load.</p>

---

## Post #5 by @rhodesdante (2023-01-19 21:17 UTC)

<p>I appreciate the information that these kinds of filenames trigger grouping heuristics. For my use case, it would be best if the files could be in the same directory. Are there any specific rules about filenames that I can consider so I don’t set off the grouping heuristics during load? Thanks!</p>

---

## Post #6 by @pieper (2023-01-19 21:34 UTC)

<p>Yeah, I don’t like the heuristics much either but they are buried deep in some of the code to support some edge use cases in the community of 20 or so years ago.  Maybe it’s time form them to be turned off or made optional.  If you could file an issue github with a description of the problem and the example files that were problematic for you it would stay on the radar, but FYI we don’t currently have dedicated funding for fixes at that level.</p>
<p>For now, one option could be to use a custom load function in python to copy the files to individual temp directories before loading.  This is just a few lines of code and probably won’t add much overhead unless your files are very large.</p>

---
