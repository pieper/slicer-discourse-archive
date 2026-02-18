# How to detect the event when one fiducial is clicked (focused) and how to set the state of this?

**Topic ID**: 19119
**Date**: 2021-08-09
**URL**: https://discourse.slicer.org/t/how-to-detect-the-event-when-one-fiducial-is-clicked-focused-and-how-to-set-the-state-of-this/19119

---

## Post #1 by @slicer (2021-08-09 13:59 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>When we click a fiducial in the view window, this fiducial will be focused and three views will be adjusted according to this fiducial. I want to ask how to detect this event when clicking a fiducial in python interactor? Also, I want to ask how to set this state for a particular fiducial, let’s say, seems like clicking it?</p>
<p>Hope for your help.</p>

---

## Post #2 by @lassoan (2021-08-09 23:56 UTC)

<p>You can change the interaction → widget event translation so that left-click is mapped to a custom widget event that you observe (see example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#assign-custom-actions-to-markups">here</a>). You need to remember vr the original translation and do the julep-to-slice and your custom actions in your callback function.</p>

---
