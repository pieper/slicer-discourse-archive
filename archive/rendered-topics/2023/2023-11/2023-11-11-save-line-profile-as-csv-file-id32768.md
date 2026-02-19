---
topic_id: 32768
title: "Save Line Profile As Csv File"
date: 2023-11-11
url: https://discourse.slicer.org/t/32768
---

# Save line profile as CSV file

**Topic ID**: 32768
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/save-line-profile-as-csv-file/32768

---

## Post #1 by @Jonathan_Mbewe (2023-11-11 19:32 UTC)

<p>I’m running Slicer 5.4.0. I’ve just installed and updated the SandBox and SlicerRT extensions, but Line Profile does not appear as an option under ‘Modules’. Am I missing something?</p>

---

## Post #2 by @Jonathan_Mbewe (2023-11-12 08:19 UTC)

<p>So I found the Sandbox Line Profile module in Slicer 5.5.0 revision version, calculated an intensity profile using two methods: first by drawing a line and calculating the intensity in Line Profile, and secondly by drawing the line in Markup then calculating the intensity in Line Profile. There was no option to export the intensity table in Line Profile, and attempting to export it in Markup causes the application to crash.</p>
<p>Is there another way to export the profile to text file, say .csv?</p>

---

## Post #3 by @lassoan (2023-11-13 02:45 UTC)

<p>You can use File / Save to save the computed intensity profile as a .csv file. By default, the file format may be .tsv (tab-separated values), but you can click .csv (comma-separated values) instead. Excel can load both .tsv and .csv file formats.</p>

---
