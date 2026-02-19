---
topic_id: 21393
title: "Import Slicer Doesnt Work In Python Script"
date: 2022-01-10
url: https://discourse.slicer.org/t/21393
---

# import slicer doesn't work in python script

**Topic ID**: 21393
**Date**: 2022-01-10
**URL**: https://discourse.slicer.org/t/import-slicer-doesnt-work-in-python-script/21393

---

## Post #1 by @MJJ (2022-01-10 21:16 UTC)

<p>I want to automate generating a scene using python.<br>
I’ve created a .py file.<br>
But when I run:<br>
<code>import slicer</code><br>
I get the following error:<br>
<code>ModuleNotFoundError: No module named 'slicer'</code></p>
<p>If i load the slicer application it works fine, but I want to be able to build a scene file and add transform and link data to it, etc. from a python script without having to open the application.<br>
Is this possible?</p>
<p>Maybe I just dont have something installed?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2022-01-10 23:29 UTC)

<p>Some things can be done using the <code>PythonSlicer</code> command and others can be done with the <code>--no-main-window</code> and <code>--python-script</code> options to the Slicer executable.  Both are limited compared to the full app with rendering and all modules available so a lot depends on what exactly you need to do.</p>

---

## Post #3 by @MJJ (2022-02-03 22:24 UTC)

<p>Thanks. that seems to be sufficient for my purposes!</p>

---
