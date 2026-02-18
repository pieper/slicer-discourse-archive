# How to disable the Add Data Dialog when dragging and dropping an .mrml file into Slicer?

**Topic ID**: 10131
**Date**: 2020-02-05
**URL**: https://discourse.slicer.org/t/how-to-disable-the-add-data-dialog-when-dragging-and-dropping-an-mrml-file-into-slicer/10131

---

## Post #1 by @Vincent_C (2020-02-05 21:34 UTC)

<p>Hi there,</p>
<p>How can I disable the add data dialog window when I drag and drop .mrml files into Slicer? Is there a command I can put into slicerrc.py to prevent the dialog pop-up window from appearing everytime and drag and drop?<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/559c5ee6fd223198d473346e3a3d569adcfa966d.png" alt="Adddatadialog" data-base62-sha1="cdlBFYr7tQx9oCoFlsa3Hx8jLjf" width="536" height="282"></p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-02-05 21:57 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> just mentioned something about needing to do this in her own custom app - maybe she can comment, but I don’t think it was something one could override in python but I could be wrong on that.</p>

---

## Post #3 by @jamesobutler (2020-02-06 03:06 UTC)

<p>Recently I did some overriding of the drop event in Python. See this post <a href="https://discourse.slicer.org/t/add-drag-and-drop-import-to-slicelet/9382/4" class="inline-onebox">Add Drag and drop import to slicelet?</a></p>

---

## Post #4 by @lassoan (2020-02-06 04:19 UTC)

<p>This is very useful, thanks a lot! I’ve used it now to make DICOM loading simpler: if you drag-and-drop files or folders while DICOM module is active then they will be always loaded as DICOM (the user does not have to choose) - see <a href="https://github.com/Slicer/Slicer/pull/1316">https://github.com/Slicer/Slicer/pull/1316</a></p>

---
