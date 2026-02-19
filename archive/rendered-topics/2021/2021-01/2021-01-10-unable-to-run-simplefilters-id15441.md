---
topic_id: 15441
title: "Unable To Run Simplefilters"
date: 2021-01-10
url: https://discourse.slicer.org/t/15441
---

# Unable to run SimpleFilters

**Topic ID**: 15441
**Date**: 2021-01-10
**URL**: https://discourse.slicer.org/t/unable-to-run-simplefilters/15441

---

## Post #1 by @Michal_Lenik (2021-01-10 16:39 UTC)

<p>When I try to run Simple Filters the window shows only help&amp;development system reported error that Simple Filters widget has no representation. Could I ask for help?</p>

---

## Post #2 by @lassoan (2021-01-10 17:36 UTC)

<p>It is probably because your username contain a special (non-ASCII) character. See more details here: <a href="https://github.com/Slicer/Slicer/issues/5383#issuecomment-757512228" class="inline-onebox">SimpleITK is not available on Windows if Slicer is installed in a path that contains special characters · Issue #5383 · Slicer/Slicer · GitHub</a></p>
<p>For now, I would recommend to reinstall Slicer at the step you need to choose the install location choose a path that does not contain any special characters.</p>

---

## Post #3 by @Michal_Lenik (2021-01-10 17:41 UTC)

<p>I didn’t create an account yet. At least no data in User settings is applied</p>

---

## Post #4 by @jamesobutler (2021-01-10 17:52 UTC)

<p>Does your OS (eg Windows, macOS, etc) username include the special character “ł” as in your name “Michał”?</p>

---

## Post #5 by @Michal_Lenik (2021-01-10 17:58 UTC)

<p>I just changed it to “l” but default folder still has “ł”</p>

---

## Post #6 by @lassoan (2021-01-10 18:06 UTC)

<p>Changing the username will probably not change the already created profile path (because doing so could break already installed software). I would expect that other software will have problems with your profile folder containing special characters, so it could make sense to create a new user with a simple username. If the goal is to make Slicer work with minimum effort, you can install it in a different location (for example, c:\Slicer).</p>

---
