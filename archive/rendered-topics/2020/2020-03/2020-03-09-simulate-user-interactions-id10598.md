---
topic_id: 10598
title: "Simulate User Interactions"
date: 2020-03-09
url: https://discourse.slicer.org/t/10598
---

# Simulate user interactions

**Topic ID**: 10598
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/simulate-user-interactions/10598

---

## Post #1 by @Yash_Kumar_Gumashta (2020-03-09 13:18 UTC)

<p>Hello Experts,</p>
<p>I am an IT professional who is trying to simulate a healthcare environment on a large scale and hence we are using software to simulate that workload on our systems, So I am basically trying to get 3D slicer to open up a nrrd file &gt;&gt; Go to “Volume Rendering” &gt;&gt; Click on Volume &gt;&gt; Select a Preset &gt;&gt; Change rendering to GPU &gt;&gt; look at the 3D image for 30-45 seconds and close the application.</p>
<p>I was able to automate the workflow using some scripts and automated mouse movements, the result is pretty decent ( You can watch the script in action @ <a href="https://youtu.be/-DWZDO4e8ns" rel="nofollow noopener">https://youtu.be/-DWZDO4e8ns</a> ) but I was curious to know if I can simulate these steps using only Python or only keystrokes.</p>
<p>Regards,<br>
A new guy in 3D Slicer world</p>

---

## Post #2 by @lassoan (2020-03-09 13:24 UTC)

<p>There are several self-tests that perform complex workflows, including loading data, setting up various visualizations, and simulating keystrokes and mouse movement.</p>
<p>For example:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py">https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNA2012ProstateDemo.py">https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNA2012ProstateDemo.py</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNAQuantTutorial.py">https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNAQuantTutorial.py</a></li>
</ul>

---
