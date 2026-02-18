# DICOM database not showing slice count

**Topic ID**: 25746
**Date**: 2022-10-18
**URL**: https://discourse.slicer.org/t/dicom-database-not-showing-slice-count/25746

---

## Post #1 by @Vincebisca (2022-10-18 07:41 UTC)

<p>Hi !</p>
<p>I have a little problem since I switched from 3D Slicer 4.11 to 5.0 : when I changed the version, the software recognized that I had an existing DICOM database loaded in 4.11 and uploaded it on 5.0. However, ever since, I don’t see the size and image count on any sequence in the database, even when adding new DICOMs (see image below). DO you know what it could come from? And how to fix it? Thanks !</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21243b9baf0ee7bbcc8bebe95ca1bac357a443d6.png" alt="image" data-base62-sha1="4JbnS4MX9dEpKXcBKwczb7JJyPI" width="206" height="189"></p>

---

## Post #2 by @cpinter (2022-10-18 10:53 UTC)

<p>I can see slice count in 5.1.0. If you specify a new, empty directory for DICOM database, and you import a CT in that empty database, do you see the slice count?</p>

---

## Post #3 by @Vincebisca (2022-10-18 11:31 UTC)

<p>Yes indeed, it works ! Thanks, gotta re-upload everything on the new database but that’s at least a solution, thanks !</p>

---

## Post #4 by @cpinter (2022-10-18 13:11 UTC)

<p>Well sorry you had to do it from scratch. Normally the DICOM database schema upgrade should work well, but apparently it did not in your case. Unfortunately it is super hard to debug… Anyway, glad it works.</p>

---
