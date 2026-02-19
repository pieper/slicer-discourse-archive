---
topic_id: 30840
title: "Problem With Data Bases"
date: 2023-07-28
url: https://discourse.slicer.org/t/30840
---

# Problem with data bases 

**Topic ID**: 30840
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/problem-with-data-bases/30840

---

## Post #1 by @Mcgiler (2023-07-28 01:17 UTC)

<p>Hi,</p>
<p>Lately I changed the location of the DICOM files on my computer. Since then I’m not able to load patients because the file path is not existing.<br>
I was trying to remove the patients from the the DICOM database (by right click-&gt;delete) or by ‘remove all data sets’ (in the DICOM database settings) or to reinstall the program. All with no success.<br>
I was trying to just upload the new DICOM files again-did not help.</p>
<p>This is what I get in the Python Console:<br>
[Python] Warning: Warning: 481 of 481 selected files listed in the database cannot be found on disk.<br>
[Python] See python console for error message.<br>
[Qt] SQLITE ERROR: could not remove seriesInstanceUID 1.2.392.200036.9133.3.1.710358.4.20230501154541363<br>
[Qt] SQLITE ERROR: Unable to fetch row</p>
<p>is there a way to remove all patients from the database or change the files path?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @pieper (2023-07-28 01:23 UTC)

<p>An easy way would be to change the database directory (database setting at bottom of DICOM module) and then re-import the files of interest from their new location.</p>

---

## Post #3 by @Mcgiler (2023-07-28 11:49 UTC)

<p>Thank you for your replay</p>
<p>Unfortunately it’s not solving the problem.<br>
I’m also trying to create an new database in a new location but it failed.</p>
<p>Is there another way to remove data sets from the existing database? (not from the DICOM database settings)</p>
<p>thanks</p>

---
