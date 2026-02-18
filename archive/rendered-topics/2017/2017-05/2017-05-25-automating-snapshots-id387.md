# Automating snapshots

**Topic ID**: 387
**Date**: 2017-05-25
**URL**: https://discourse.slicer.org/t/automating-snapshots/387

---

## Post #1 by @gbook (2017-05-25 18:33 UTC)

<p>I’m displaying a freesurfer surface, and applying a LUT from a text file to display different colors. However, I have a few hundred LUTs that I need to apply and take screenshots of each. Is it possible to automate slicer to do that?</p>

---

## Post #2 by @pieper (2017-05-25 18:59 UTC)

<p>It’s always possible to write a python script for things like that, but there’s nothing quite like that built in.</p>

---

## Post #3 by @lassoan (2017-05-25 21:50 UTC)

<p>It is really easy to implement batch processing with Slicer. You have two options:</p>
<ul>
<li>A. Create a bash/batch file that iterates through files and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer">launches Slicer</a> with each argument.</li>
<li>B. Manually launch Slicer and run a Python script that <a href="http://www.tutorialspoint.com/python/os_walk.htm">walks through the files</a> and performs the loading/processing/export operations that you need.</li>
</ul>
<p>How to load data, create screenshots: The slicer <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> should give you lots of complete examples for implementing common operations. A few specific hints:</p>
<ul>
<li>Load data from file using slicer.util.load…() methods: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">slicer.util.loadVolume</a>, <a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=loadmodel#slicer.util.loadModel">slicer.util.loadModel</a>, etc.</li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">Save screen capture of selected views using ScreenCapture module</a></li>
</ul>
<p>Feel free to ask any questions, we should be able to respond very quickly.</p>

---
