---
topic_id: 3282
title: "Slicer As Front Gui And Supercomputer As Computing Engine"
date: 2018-06-25
url: https://discourse.slicer.org/t/3282
---

# Slicer as front gui and supercomputer as computing engine

**Topic ID**: 3282
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/slicer-as-front-gui-and-supercomputer-as-computing-engine/3282

---

## Post #1 by @LGKicon_NYU (2018-06-25 16:32 UTC)

<p>Operating system: front end is windows 10, backend is red hat linux<br>
Slicer version: 4.9 night<br>
Expected behavior: na<br>
Actual behavior: na</p>
<p>both storage and computer engine is a HPC.  Slicer is used as GUI installed on my desktop.</p>

---

## Post #2 by @lassoan (2018-06-25 16:33 UTC)

<p>What would you like to achieve? Do you have any specific question, any specific problem to solve?</p>

---

## Post #3 by @LGKicon_NYU (2018-06-25 16:41 UTC)

<p>Thank you Andras.<br>
This is what I’d like to achieve:  install Slicer on my windows 10 desktop, install pyRadiomics (and other extensions) on a supercomputer that I have an account.  All patient images will be pushed and saved on the super computer.<br>
The questions are is this possible?  And if yes how to configure.<br>
thanks,<br>
Tom</p>

---

## Post #4 by @ihnorton (2018-06-25 18:15 UTC)

<p>Slicer and pyradiomics should definitely run on a Windows 10 computer.</p>
<p>Without more information (operating system, batch job control software, etc.) it is very hard to give any concrete suggestions about using Slicer with an HPC system. Most HPC systems in the world run Linux, and Slicer can be built for Linux; the nightly builds may run on some newer systems (CentOS 7 equivalent), but given the heterogeneity of Linux it is often necessary to build from source.</p>
<p>If you are looking for a backend database to store data, or run batch/HPC-scale compute jobs, then some projects you might want to look at include: <a href="https://girder.readthedocs.io/en/latest/">Girder</a>, <a href="https://www.xnat.org/">XNAT</a>, and <a href="https://nipype.readthedocs.io/en/latest/">Nipype</a> (among many others).</p>

---
