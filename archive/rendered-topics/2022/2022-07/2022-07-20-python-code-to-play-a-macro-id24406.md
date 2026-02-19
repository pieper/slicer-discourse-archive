---
topic_id: 24406
title: "Python Code To Play A Macro"
date: 2022-07-20
url: https://discourse.slicer.org/t/24406
---

# Python code to Play a Macro

**Topic ID**: 24406
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/python-code-to-play-a-macro/24406

---

## Post #1 by @Isabella_Romero (2022-07-20 09:26 UTC)

<p>Hi,</p>
<p>I have recorded a Macro in slicer and I would like to know if there is a Python command to play the Macro via the python interactor, instead of having to click on the button.</p>

---

## Post #2 by @lassoan (2022-07-21 17:39 UTC)

<p>Macro recording may seem like a good way to get start with automating Slicer, but the current Slicer macro recorder captures low-level events, which are not very useful. We have kind of left this feature behind: it seems there is no API for starting macro playback from Python, and I don’t think macro recording even works in latest Slicer versions.</p>
<p>Instead we use Python scripting for automating Slicer. With very few exceptions (such as this macro recorder) all user actions are accessible via Python commands. A good starting point is the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Script Repository</a> which contain complete examples of the most commonly needed actions.</p>

---

## Post #3 by @Isabella_Romero (2022-09-21 08:43 UTC)

<p>Thank you for your answer. I understand what you are saying, I am testing the use of the macro.<br>
I know there are ways to custom keyboard shortcuts for slicer, do you know how I can program a shortcut to “press” the Play Macro button?</p>

---
