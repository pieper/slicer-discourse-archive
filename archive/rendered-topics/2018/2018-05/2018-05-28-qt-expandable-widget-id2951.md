---
topic_id: 2951
title: "Qt Expandable Widget"
date: 2018-05-28
url: https://discourse.slicer.org/t/2951
---

# Qt Expandable Widget

**Topic ID**: 2951
**Date**: 2018-05-28
**URL**: https://discourse.slicer.org/t/qt-expandable-widget/2951

---

## Post #1 by @Hikmat (2018-05-28 16:23 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1</p>
<p>Hi,</p>
<p>I would like to remove this “slider” feature but I am not sure what the widget is called.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afe78406181057ed842d88603191a1816e1f8207.png" alt="image" data-base62-sha1="p67zNMuK8YMBxeULOOjIqrODv6f" width="494" height="107"></p>
<p>I have tried to spot it in this extensive list but to no avail: <a href="http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html" rel="noopener nofollow ugc">http://pyqt.sourceforge.net/Docs/PyQt5/QtWidgets.html</a></p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-05-29 01:53 UTC)

<p>This looks like a ctkExpandableWidget. Where do you see this?</p>

---

## Post #3 by @Hikmat (2018-05-29 13:55 UTC)

<p>Yes, thank you Andras, it was indeed a ctkExpandableWidget.<br>
It is in Segment Editor and I only needed the Undo / Redo buttons.</p>

---

## Post #4 by @lassoan (2018-05-29 17:09 UTC)

<p>You can also hide the entire widget and just call its undo() and redo() methods (<a href="http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html">http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html</a>).</p>

---
