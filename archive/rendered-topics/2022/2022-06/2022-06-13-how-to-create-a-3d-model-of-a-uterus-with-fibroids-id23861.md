# how to create a 3d model of a uterus with fibroids?

**Topic ID**: 23861
**Date**: 2022-06-13
**URL**: https://discourse.slicer.org/t/how-to-create-a-3d-model-of-a-uterus-with-fibroids/23861

---

## Post #1 by @Dr.Karpov (2022-06-13 19:57 UTC)

<p>Hello colleagues.  I am an obstetrician-gynecologist.  I want to create a 3D model of a uterus with fibroids, but I can’t do it due to the lack of technical knowledge of the program.  Perhaps someone knows how to solve my problem and share step by step instructions for creating a 3d model of the uterus.  Thank you.</p>

---

## Post #2 by @edwardwang1 (2022-06-13 20:06 UTC)

<p>Do you have a scan of a specific uterus that you want to use?</p>
<p>If so, you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" rel="noopener nofollow ugc">Segment Editor</a> Module to contour/segment the uterus/fibroids, then use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" rel="noopener nofollow ugc">Segmentations</a> Module to Export it as a 3D file (such as an STL)</p>

---

## Post #3 by @Dr.Karpov (2022-06-13 20:18 UTC)

<p>yes i have DICOM files from MRI</p>

---

## Post #4 by @Dr.Karpov (2022-06-13 20:20 UTC)

<p>Thanks for the advice, I’ll try and write if it worked or not.</p>

---

## Post #5 by @Fullcalf42 (2022-06-15 02:33 UTC)

<p>How did it go? What will be the format of your presentation?</p>

---

## Post #6 by @Dr.Karpov (2022-06-22 18:48 UTC)

<p>I can not separate the uterus from the surrounding organs within clear boundaries. Perhaps someone can give advice on what kind of tool and how to clearly highlight the uterus in 3d?</p>

---
