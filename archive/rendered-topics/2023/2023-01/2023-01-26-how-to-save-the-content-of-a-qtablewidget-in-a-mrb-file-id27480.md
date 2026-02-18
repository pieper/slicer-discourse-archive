# How to save the content of a qTableWidget in a MRB file?

**Topic ID**: 27480
**Date**: 2023-01-26
**URL**: https://discourse.slicer.org/t/how-to-save-the-content-of-a-qtablewidget-in-a-mrb-file/27480

---

## Post #1 by @JessevdO (2023-01-26 15:58 UTC)

<p>Hello,</p>
<p>I would like to know how to save the content of a qTableWidget in a MRB file?</p>
<p>For research I am doing, I have written a scripted loadable module which enables me to do all my measurements and save everything information I need from one subject in a single MRB file. This includes pre operative segmentation of perforator vessels, segmentation of the bone, and the measurments I conduct in the operation theatre.</p>
<p>Since I am also required to save qualitative data, I have created a qTableWidget in a slicer module extension in which I can save the required data. However, when I save the whole scene in an MRB file, the data in the table is lost.</p>
<p>Is there any way to save this, or is there a better method I could use?</p>

---

## Post #2 by @pieper (2023-01-26 16:49 UTC)

<p>Instead of a <code>qTableWidget</code>, which is purely GUI, you can create a <code>vtkMRMLTableNode</code> which is part of the scene (saved/restored with the MRB).  You can display these natively with table (or plot) views in the Slicer interface (e.g. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#using-mrml-classes-only" class="inline-onebox">Script repository — 3D Slicer documentation</a>).</p>

---

## Post #3 by @lassoan (2023-01-26 23:14 UTC)

<p>You can also display the MRML table in your module widget using a <a href="https://apidocs.slicer.org/master/classqMRMLTableView.html">qMRMLTableView</a>. You can simply drag-and-drop this view into your module GUI in Qt designer and set the MRML scene and the table node you want to view/edit in it.</p>

---

## Post #4 by @JessevdO (2023-02-02 10:36 UTC)

<p>Thank you gentleman! That is exactly what I wanted <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
