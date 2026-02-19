---
topic_id: 34595
title: "Reconstruct 4D Cine Mri From Different Groups"
date: 2024-02-28
url: https://discourse.slicer.org/t/34595
---

# Reconstruct 4D cine-MRI from different groups

**Topic ID**: 34595
**Date**: 2024-02-28
**URL**: https://discourse.slicer.org/t/reconstruct-4d-cine-mri-from-different-groups/34595

---

## Post #1 by @minniti (2024-02-28 13:29 UTC)

<p>hello,<br>
I am trying to reconstruct a 4D view of a ventricle givens some medicals mri.<br>
I found a previous discussion (<a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/Reconstruct4DCineMRI.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerHeart/Docs/Reconstruct4DCineMRI.md at master · SlicerHeart/SlicerHeart · GitHub</a>)).<br>
The problem is that I have 14 different slices each on containing 30 frames but they are separated in 14 different groups (1 for each slice).<br>
I was trying to apply the procedure suggested in the previous discussion, but I cannot load all the images together.<br>
How can I solve it? I need to have all the volume and time frame in one unique file right? Or does exist another way to do it?<br>
Thanks a lot for your patience</p>

---

## Post #2 by @pieper (2024-02-28 16:00 UTC)

<p>You’ll need to provide more detail about your data, like whether it is in DICOM or some other format.</p>

---

## Post #3 by @minniti (2024-02-28 20:09 UTC)

<p>yes the file are dicom</p>

---
