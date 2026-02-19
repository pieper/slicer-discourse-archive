---
topic_id: 9967
title: "Gtract Windows 10"
date: 2020-01-27
url: https://discourse.slicer.org/t/9967
---

# GTRACT Windows 10

**Topic ID**: 9967
**Date**: 2020-01-27
**URL**: https://discourse.slicer.org/t/gtract-windows-10/9967

---

## Post #1 by @Adam1122 (2020-01-27 14:43 UTC)

<p>Hello all, I am trying to run GTRACT programs in Slicer 4.10.2. on Windows 10. I´ve downloaded the GTRACT folder: <a href="https://github.com/BRAINSia/BRAINSTools" rel="nofollow noopener">https://github.com/BRAINSia/BRAINSTools</a> . Please, could you advise me what next I should do to run GTRACT programs? Are GTRACT programs used in command line or in GUI as well?</p>
<p>Thanks a lot<br>
Adam</p>

---

## Post #2 by @pieper (2020-01-27 15:50 UTC)

<p>Not sure of the status of that - maybe best to start at Vince’s page: <a href="https://www.nitrc.org/projects/vmagnotta">https://www.nitrc.org/projects/vmagnotta</a></p>

---

## Post #3 by @Adam1122 (2020-01-27 18:24 UTC)

<p>Hello Steve, yeah I know. I downloaded the GTRACT set in this page <a href="https://www.nitrc.org/projects/vmagnotta" rel="nofollow noopener">https://www.nitrc.org/projects/vmagnotta</a>. How to run the GTRACT tools in 3D Slicer - can it be run through Command Line or in GUI as well? Where in the Slicer 4.10. folder should I put the GTRACT folder I downloaded? I am running on Windows 10. I am new to 3D Slicer so I´m sorry for these questions.</p>

---

## Post #4 by @pieper (2020-01-27 20:06 UTC)

<p>Hi Adam - You should probably try contacting Vince for details.  I believe GTRACT is a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules">command line module</a> that only uses ITK and C++ so it could be ported to the current Slicer if it hasn’t been already.</p>
<p>On the other hand if your goal is to do tractography you could also look at <a href="http://dmri.slicer.org/">SlicerDMRI</a>, which is actively maintained.</p>

---
