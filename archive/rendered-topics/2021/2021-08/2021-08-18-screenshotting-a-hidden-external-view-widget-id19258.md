---
topic_id: 19258
title: "Screenshotting A Hidden External View Widget"
date: 2021-08-18
url: https://discourse.slicer.org/t/19258
---

# Screenshotting a hidden external view widget

**Topic ID**: 19258
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/screenshotting-a-hidden-external-view-widget/19258

---

## Post #1 by @nathanbmnt (2021-08-18 15:24 UTC)

<p>Hello,<br>
I have an external view widget I created with the code <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout" rel="noopener nofollow ugc">here</a> but I never call viewWidget.show() because I want it hidden from the user.</p>
<p>If I try to get a screenshot of the external slice view widget with <code>vtkWindowToImageFilter</code> the vtkImage is of size 0,0,1. If I use <code>img = ctk.ctkWidgetsUtils.grabWidget</code> the image is the right size and shows the colored scroll bar on top, but the slice image is completely black.</p>
<p>I always call slicer.app.processEvents and <code>view_widget.sliceView().forceRender()</code> before screenshotting but it still doesn’t function. Any suggestions?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02b21ad3d4291f34f203a7c12e801577c6b4b7c4.png" alt="image" data-base62-sha1="nQxE9vuZF3gwQiqxCoz2CsMZ5q" width="538" height="474"></p>

---

## Post #2 by @lassoan (2021-08-18 18:13 UTC)

<p>You may need to show the widget at least once to complete its initialization. You might also need to temporarily show it when you take a screenshot, in which case you could try set the window position outside of the screen or below the main window to prevent it from popping up for the user.</p>

---

## Post #3 by @nathanbmnt (2021-08-18 19:03 UTC)

<p>Showing the widget and then immediately hiding it right after creation does not work unfortunately. I can however screenshot when the widget is outside of the monitor bounds, so I’ve just used qwidget.setGeometry to put it out of bounds</p>

---
