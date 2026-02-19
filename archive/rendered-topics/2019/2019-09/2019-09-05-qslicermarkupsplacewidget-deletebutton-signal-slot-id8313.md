---
topic_id: 8313
title: "Qslicermarkupsplacewidget Deletebutton Signal Slot"
date: 2019-09-05
url: https://discourse.slicer.org/t/8313
---

# qSlicerMarkupsPlaceWidget().deleteButton signal/slot?

**Topic ID**: 8313
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/qslicermarkupsplacewidget-deletebutton-signal-slot/8313

---

## Post #1 by @Greydon_Gilmore (2019-09-05 17:35 UTC)

<p>Hi!</p>
<p>I am using <code>slicer.qSlicerMarkupsPlaceWidget()</code> in my scripted module. I give the user an option to delete the placed point by making the <code>deleteButton</code> active. I would like to emit a signal when the delete button is pressed in order to clear a coordinate widget that displays the fiducial coordinates relative to MCP.</p>
<p>Is there a signal/slot for the <code>deleteButton()</code>?</p>
<p>Thanks,<br>
Greydon</p>

---

## Post #2 by @lassoan (2019-09-05 18:33 UTC)

<p>There are various ways to delete a markup (e.g., hover over the markup and hit Delete), so I would not recommend to observe delete button click. Instead, you can observe changes in the MRML node.</p>

---

## Post #3 by @Greydon_Gilmore (2019-09-11 01:58 UTC)

<p>That will work! Thank you.</p>

---
