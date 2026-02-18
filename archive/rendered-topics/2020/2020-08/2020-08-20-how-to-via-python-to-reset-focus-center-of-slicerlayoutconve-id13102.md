# How to, via python, to reset focus center of SlicerLayoutConventionalQuantitativeView

**Topic ID**: 13102
**Date**: 2020-08-20
**URL**: https://discourse.slicer.org/t/how-to-via-python-to-reset-focus-center-of-slicerlayoutconventionalquantitativeview/13102

---

## Post #1 by @aiden.zhu (2020-08-20 10:01 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.0<br>
Expected behavior: set up the focus/center of QuantitativeView<br>
Actual behavior:</p>
<p>Hi all,<br>
what’s the command/function to trigger doing the automatic centering of quantitativeview after setting-up as SlicerLayoutConventionalQuantitativeView = 24 ?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34e59bf5e7c2af8c440dcbd5f8074d1cd4ca1d0e.png" alt="image" data-base62-sha1="7xWLmCN8VZx7R41FlD69JcLJjoG" width="547" height="221"></p>
<p>Thanks a lot!<br>
Aiden</p>

---

## Post #2 by @aiden.zhu (2020-08-20 10:13 UTC)

<p>Aha, found it right away.</p>
<p>test = slicer.app.layoutManager().plotWidget(0).plotController()<br>
test.fitPlotToAxes()</p>

---
