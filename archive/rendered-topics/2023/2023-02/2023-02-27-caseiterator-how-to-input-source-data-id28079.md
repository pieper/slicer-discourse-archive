# CaseIterator - how to input source data

**Topic ID**: 28079
**Date**: 2023-02-27
**URL**: https://discourse.slicer.org/t/caseiterator-how-to-input-source-data/28079

---

## Post #1 by @ummmcam (2023-02-27 22:14 UTC)

<p>Can anyone help me figure out how to create a usable csv for caseiterator? I created a csv with the headers specified in the module. If I import the file into Slicer I can get it to show up in the table list.</p>
<p>I added a few lines referencing the DICOMs I have saved on my filesystem. Is there a way to reference DICOM files in a database? Using a base/relative path? Either way, my path of C:/path/to/dicom  yields the error: “Error loading batch! Unable to find column “path” (key root)”.</p>
<p>Sorry if this is a newb question. Just getting started.</p>

---

## Post #2 by @pieper (2023-02-27 23:10 UTC)

<p><a href="https://github.com/JoostJM/SlicerCaseIterator#example">Here’s an example</a> for creating a csv.</p>
<p>I don’t think CaseIterator handles DICOM, but <a href="https://discourse.slicer.org/t/slicer-often-crashes-when-running-with-python-script-in-loading/23719/11">this example</a> shows converting scalar volumes from the database to nii files and you could create a csv for those.</p>

---
