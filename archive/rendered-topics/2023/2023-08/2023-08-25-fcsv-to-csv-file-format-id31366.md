---
topic_id: 31366
title: "Fcsv To Csv File Format"
date: 2023-08-25
url: https://discourse.slicer.org/t/31366
---

# Fcsv to csv file format

**Topic ID**: 31366
**Date**: 2023-08-25
**URL**: https://discourse.slicer.org/t/fcsv-to-csv-file-format/31366

---

## Post #1 by @Vignesh_Chakravarthy (2023-08-25 16:58 UTC)

<p>Hi guys,</p>
<p>Please let me know how to convert fscv to csv file in 3d slicer. I need the landmarks as csv file. However, I can see that the file formats available are .json, .fcsv. Please help me.</p>
<p>Thanks,<br>
Vignesh</p>

---

## Post #2 by @muratmaga (2023-08-25 18:09 UTC)

<p>Go to the Markups module, expand the import/export option (towards the bottom of the tabs), export as a table, and then save that table as a csv file using the file save dialog.</p>
<p>Note that if you do not save your Markups as JSON, you may not be able to recover everything from the exported CSV file (that only contains the coordinates of the control points).</p>

---

## Post #3 by @M111 (2023-08-26 17:26 UTC)

<p>Hi, thank you for your response. I followed your instructions; export as a table, but I can’t see the SVG format. Can you, please, post a photo?</p>

---

## Post #4 by @muratmaga (2023-08-26 17:39 UTC)

<p>There is no SVG format to export? SVG is a graphics format, why do you want to export your coordinates as a SVG?</p>

---

## Post #5 by @M111 (2023-08-27 09:34 UTC)

<p>Sorry, I  confused SVG and CSV.</p>

---

## Post #6 by @Vignesh_Chakravarthy (2023-08-28 15:08 UTC)

<p>Thanks again for the prompt response, Dr. Murat! Have a great day!!</p>

---
