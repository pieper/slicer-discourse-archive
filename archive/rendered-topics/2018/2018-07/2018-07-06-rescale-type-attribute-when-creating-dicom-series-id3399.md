---
topic_id: 3399
title: "Rescale Type Attribute When Creating Dicom Series"
date: 2018-07-06
url: https://discourse.slicer.org/t/3399
---

# Rescale type attribute when creating DICOM series

**Topic ID**: 3399
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/rescale-type-attribute-when-creating-dicom-series/3399

---

## Post #1 by @awagner (2018-07-06 11:51 UTC)

<p>Hello,</p>
<p>I’m using Slicer to create a downsampled CT series, and I was able to do that just fine, except that it appears the “Rescale type” attribute was changed from HU to US. Due to that I cannot export the images anymore in the other program I’m using (Treatment Planning Station).</p>
<p>Is there any way to keep this attribute unchanged, or to revert it back to its original value ?</p>
<p>Thanks !</p>
<p>Antoine</p>

---

## Post #2 by @pieper (2018-07-06 20:34 UTC)

<p>Good question - I guess you mean <a href="https://dicom.innolitics.com/ciods/ct-image/ct-image/00281054">this attribute</a>. I don’t know that we have any easy want to control for that right now.</p>
<p>Probably the best I can suggest  would be to write a small loop using pydicom or directly use dcmodify to change the tag in each file.</p>

---

## Post #3 by @lassoan (2018-07-06 21:06 UTC)

<p>There are a couple of ways to export DICOM series from Slicer. What method do you use?</p>

---

## Post #4 by @awagner (2018-07-09 07:44 UTC)

<p>Hi,</p>
<p>Thanks Steve, yes this is the attribute (0028,1054). I’m not familiar with pydicom but I’ll give it a try. In the meantime I was able to do it on another program (Dicomworks) but it would ne nice and easier to do it from Slicer.</p>
<p>Andras, to export I simply go to the data menu to display the subject hierarchy, then right-click the volume and select “Export to Dicom…”</p>

---

## Post #5 by @lassoan (2018-07-09 19:18 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> <a class="mention" href="/u/cpinter">@cpinter</a> Do you know if there is a reason why rescale type is set to US during DICOM export? Could the value be changed to HU?</p>

---
