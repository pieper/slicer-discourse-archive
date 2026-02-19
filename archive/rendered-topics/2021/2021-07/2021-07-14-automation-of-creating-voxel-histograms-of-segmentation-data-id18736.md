---
topic_id: 18736
title: "Automation Of Creating Voxel Histograms Of Segmentation Data"
date: 2021-07-14
url: https://discourse.slicer.org/t/18736
---

# Automation of creating voxel histograms of segmentation data

**Topic ID**: 18736
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/automation-of-creating-voxel-histograms-of-segmentation-data/18736

---

## Post #1 by @Griffin (2021-07-14 17:15 UTC)

<p>I am fairly new to 3d slicer but I am trying to figure out how and I automate or speed up the process of getting a histogram of voxel data from a segmented section. I have been able to do this for one segment at a time through 3d slicer’s own python interactor using the code<br>
at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>. But I want to be able to make a python function that loops through files in a directory and spits out either data or a histogram for each one. If anyone has any ideas about how to do this or where I should look to learn more about this that would be much appreciated.</p>

---

## Post #2 by @lassoan (2021-07-14 17:25 UTC)

<p>You can run the code snippet in a loop that iterates through files in a folder. You can find Python many tutorials on the web on <a href="https://www.google.ca/search?q=python+iterate+through+files+in+folder">how get filenames in a folder in Python</a>.</p>

---

## Post #3 by @Griffin (2021-07-14 17:44 UTC)

<p>Great! Thank you! And just to clarify, would I be looping through those files from within slicer 3d’s python interactor, or is it possible to do it from a third party code editor like pycharm or vscode?</p>

---

## Post #4 by @lassoan (2021-07-14 19:59 UTC)

<p>You can do it from anywhere - interactively copy-pasting into Slicer’s Python console, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#run-a-python-script-file-in-the-slicer-environment">running a Python script from the command line</a>, in a <a href="https://github.com/Slicer/SlicerJupyter">Jupyter notebook</a>. You can also use <a href="https://github.com/SlicerRt/SlicerDebuggingTools">PyCharm or Visual Studio Code for development and interactive debugging</a>.</p>
<p>The only unusual in Slicer’s Python environment is that most of the classes are instantiated by the Slicer application, therefore if you just set PythonSlicer.exe as your Python interpreter (instead of launching the Slicer application and attaching a Python debugger to it) then you’ll only have a small fraction of the features available.</p>

---
