---
topic_id: 13365
title: "Cannot Zoom And Scroll In Slice View Slicelets"
date: 2020-09-07
url: https://discourse.slicer.org/t/13365
---

# Cannot zoom and scroll in slice view(slicelets)

**Topic ID**: 13365
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/cannot-zoom-and-scroll-in-slice-view-slicelets/13365

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-07 07:11 UTC)

<p>I created a slicelet of custom layouts that has three slice nodes.<br>
But I am not able to zoom into the slice view or scroll through the imgaes. Why is this happening?</p>

---

## Post #2 by @lassoan (2020-09-07 14:47 UTC)

<p>The widget needs access to the slice logics. If you want to create a widget outside the view layout then you can follow this example (for latest Slicer preview release):</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout</a></p>
<p>Note that the recommended way of implementing slicelets is to define custom layout within the standard layout manager (and not to create standalone widgets). See details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #3 by @Chintha_Siva_Prasad (2020-09-07 15:02 UTC)

<p>I am getting a None object slicer.app.applicationLogic().GetSliceLogics() from this slice logics.</p>

---

## Post #4 by @lassoan (2020-09-07 15:04 UTC)

<p>Please follow the guidance in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a>, i.e., use Slicer’s main window (do not call <code>--no-main-window</code>) and also make sure your code runs after the application startup is completed (you can observe the startup completed signal - <code>    slicer.app.connect("startupCompleted()", self.onStartupCompleted)</code>).</p>

---

## Post #5 by @Chintha_Siva_Prasad (2020-09-08 04:06 UTC)

<p>I want to run my application without the main window.</p>

---

## Post #6 by @lassoan (2020-09-08 12:01 UTC)

<p>Application behavior and setup is very different when there is a main window compared to when there is no main window. If you want to show any GUI elements but not all the widgets, then you can still show the main window but hide unwanted elements (or creating a custom application, where you have full control over what is added to the main window). Supporting a redundant no-main-window mode for displaying GUI would cost a lot of extra development, test, and maintenance effort that we rather invest into new features and fixes.</p>
<p>We still support no-main-window mode for simple scripts that do not use any widget classes.</p>
<p>What main widow element you would like to hide? Maybe we could add a simple-main-window mode that would not show menu, toolbar, and status bar by default.</p>

---
