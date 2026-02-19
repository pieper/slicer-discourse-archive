---
topic_id: 44845
title: "Decal Deca Store Export Applied Transformations Too"
date: 2025-10-22
url: https://discourse.slicer.org/t/44845
---

# DeCAL & DeCA ---> store / export applied transformations too?

**Topic ID**: 44845
**Date**: 2025-10-22
**URL**: https://discourse.slicer.org/t/decal-deca-store-export-applied-transformations-too/44845

---

## Post #1 by @MrMarkus (2025-10-22 15:05 UTC)

<p>Dear SlicerMorph team,</p>
<p>would it be possible to store / export the applied transformation too?</p>
<p>DeCAL / DeCA algorithm is already computing : 3D models are registered to the mean of the 3D models of interest. Hence,the information is already there = result of the registrations.</p>
<p>It would be nice if an UPDATE of DeCAL / DeCA could include this feature.</p>
<p>I would like to apply the resulting transformations to the volume data (not the model)<br>
in order to compare / visualize the different volumes and to be sure that I look at almost<br>
identical “planes”.</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2025-10-22 15:22 UTC)

<p>This came up during the development of the module and we decided not to implement it to keep the code and output simpler.</p>
<p>This is something you can easily do it yourself using something chatgpt (or better yet something like VSCode). I gave a prompt “identify where the finally correspondence and transformation is calculated, and save both forward and inverse transforms as Slicer’s in .h5 format” and resultant code looked functional.</p>
<p>You can then load this edited module and run things the way you want. If you encounter an error make sure to paste fully back and ask for a solution.</p>

---
