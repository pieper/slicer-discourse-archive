# Save outcome to CSV file, multiple datasets

**Topic ID**: 23009
**Date**: 2022-04-19
**URL**: https://discourse.slicer.org/t/save-outcome-to-csv-file-multiple-datasets/23009

---

## Post #1 by @Hanne1234 (2022-04-19 06:34 UTC)

<p>For my research I want to extract the features of 40 different VOIs. Most ideally, I would like to save the outcome of the features automatically into a csv file. For 1 VOI this is no problem. But my question is,  is it possible to save the new outcome to the same csv file everytime the code is runned?<br>
So that I only have to change the name of the VOI, run the code 40 times and end up with 1 csv file with all the outcomes?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-06-28 02:59 UTC)

<p>You can automate all the steps that you do in the Slicer GUI using Python scripting. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Slicer Script Repository</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">Developer Tutorials</a> page are good starting points.</p>

---
