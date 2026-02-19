---
topic_id: 13018
title: "Display Text In A 3D View"
date: 2020-08-15
url: https://discourse.slicer.org/t/13018
---

# Display text in a 3D view

**Topic ID**: 13018
**Date**: 2020-08-15
**URL**: https://discourse.slicer.org/t/display-text-in-a-3d-view/13018

---

## Post #1 by @Pablo_Javier (2020-08-15 23:33 UTC)

<p>I want to display text in a 3D View, but I don’t want to use the Corner Annotation Module. I would like to create a text box in a 3D View (for example as a new model). Is it possible?<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2020-08-15 23:51 UTC)

<p>Markups fiducials can display text in 3D view at a specific 3D position. You can hide the markup point glyph and just show the text.</p>

---

## Post #3 by @Pablo_Javier (2020-08-16 01:33 UTC)

<p>Thank you, Andras. I’ve already tried the way you mention, but the thing is that I want it to look like a corner annotation. That´s why I was asking.</p>

---

## Post #4 by @lassoan (2020-08-16 02:07 UTC)

<p>If you want it to look like a corner annotation then it may be a good idea to use a corner annotation. Does it have any limitations that prevent you from using it?</p>
<p>Maybe you can have a look at the Watchdog module in SlicerIGT extension, which displays tool status information during surgical navigation in viewers, similarly to corner annotations, but with custom color, font size, and positioning.</p>

---

## Post #5 by @Pablo_Javier (2020-08-16 16:30 UTC)

<p>Sorry, I think I haven’t explained myself correctly. I created a Module which generates model objets. I need each model to display text information in the 3D View when the eye icon is open.</p>

---

## Post #6 by @lassoan (2020-08-16 17:17 UTC)

<p>Displaying text as polygon is really bad, due to occlusion. You can see it for yourself in Slicer-4.10 markup labels.</p>
<p>Can you draw a sketch or photoshop an image that show what you would like to achieve?</p>

---
