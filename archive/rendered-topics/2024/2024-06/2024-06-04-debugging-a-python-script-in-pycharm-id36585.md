---
topic_id: 36585
title: "Debugging A Python Script In Pycharm"
date: 2024-06-04
url: https://discourse.slicer.org/t/36585
---

# Debugging a python script in pycharm

**Topic ID**: 36585
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/debugging-a-python-script-in-pycharm/36585

---

## Post #1 by @RomanStriker (2024-06-04 11:07 UTC)

<p>Hi,</p>
<p>I have a python script that I would like to debug step by step. I managed to attach Pycharm’s remote debugger to Slicer using these <a href="https://github.com/SlicerRt/SlicerDebuggingTools#instructions-for-pycharm" rel="noopener nofollow ugc">instructions</a>, however, I cannot run the python script in the Slicer GUI’s python console in debugging mode. The only way I have managed to run the script in debugging mode is by creating a custom module and add my code to the onApply() function of the module and press the Apply button. Is there a simpler way to debug python scripts?</p>

---

## Post #2 by @lassoan (2024-06-04 16:10 UTC)

<p>The debugger needs a file. So, copying your code snippet into a module is a good approach.</p>
<p>If you work with a code snippet (not saved in file) then you don’t need a debugger, as you can run the code step-by-step anyway.</p>

---
