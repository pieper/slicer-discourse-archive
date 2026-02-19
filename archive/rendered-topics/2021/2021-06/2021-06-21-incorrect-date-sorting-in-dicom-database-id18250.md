---
topic_id: 18250
title: "Incorrect Date Sorting In Dicom Database"
date: 2021-06-21
url: https://discourse.slicer.org/t/18250
---

# Incorrect Date Sorting in DICOM database

**Topic ID**: 18250
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/incorrect-date-sorting-in-dicom-database/18250

---

## Post #1 by @Alexander_Ling (2021-06-21 12:39 UTC)

<p>When I try to sort images that I’ve loaded into 3DSlicer’s DICOM database by “Last study date”, the column is sorted alphabetically rather than by date (i.e. all of the images taken on Mondays at the top, then images taken on Sundays, then Thursdays, etc.). I’m not sure if this is a bug per se, but it’s not particularly useful behavior. A screenshot is attached below with the days of the month obscured to further deidentify the data.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb354ed0747e4e84c25384ead8f5f052d944ca5e.jpeg" alt="Screenshot 2021-06-21 082916" data-base62-sha1="zQi3vOyyfivyu3zEcQElmKmDhzU" width="246" height="128"></p>

---

## Post #2 by @cpinter (2021-06-21 12:44 UTC)

<p>Please try the latest preview version. I have fixed this issue recently.</p>

---

## Post #3 by @Alexander_Ling (2021-06-21 12:50 UTC)

<p>Thank you for the quick reply! I just installed version 14.13.0 (revision 29990, built 2021-06-21), and the dates now sort correctly.</p>

---
