---
topic_id: 9794
title: "Automated Rigid 6 Dof Registration"
date: 2020-01-13
url: https://discourse.slicer.org/t/9794
---

# Automated rigid (6 DOF) registration

**Topic ID**: 9794
**Date**: 2020-01-13
**URL**: https://discourse.slicer.org/t/automated-rigid-6-dof-registration/9794

---

## Post #1 by @Fang_Cao (2020-01-13 13:57 UTC)

<p>Hello,</p>
<p>I am new to 3D slicer and want to take a look at the algorithm of automated rigid registration for different modalities (ex. T1 and T2 images of MRI) on the same subject in 3D slicer. The problem is I could not find related information in the latest version. The only thing I found is in version 3.6</p>
<p><a href="https://www.slicer.org/wiki/Modules:RigidRegistration-Documentation-3.6" rel="nofollow noopener">https://www.slicer.org/wiki/Modules:RigidRegistration-Documentation-3.6</a></p>
<p>It has a test file</p>
<p><a href="http://www.na-mic.org/ViewVC/index.cgi/trunk/Applications/CLI/Testing/RigidRegistrationTest.cxx" rel="nofollow noopener">RigidRegistrationTest.cxx</a></p>
<p>but no longer available. And the</p>
<p>Source Code: <a href="http://www.na-mic.org/ViewVC/index.cgi/trunk/Applications/CLI/LinearRegistration.cxx" rel="nofollow noopener">C++ Source</a> and <a href="http://www.na-mic.org/ViewVC/index.cgi/trunk/Applications/CLI/LinearRegistration.xml" rel="nofollow noopener">XML Description</a></p>
<p>do not exist either.</p>
<p>Can anyone give me a clue?</p>
<p>Best regards,<br>
Fang</p>

---

## Post #2 by @aiden.zhu (2020-01-13 15:15 UTC)

<p>Hi Fang, You may search “registration” (not just “rigid registration”) in this community to see a lot of helpful clues.</p>

---

## Post #3 by @Fang_Cao (2020-01-13 15:27 UTC)

<p>Could you be more specific? I am trying to find the source code or doxygen of 3D slicer for rigid registration on multi-modalities and single subject. Thanks.</p>

---

## Post #4 by @muratmaga (2020-01-13 15:48 UTC)

<p><a href="https://www.slicer.org/wiki/Modules:BRAINSFit" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Modules:BRAINSFit</a></p>

---

## Post #5 by @lassoan (2020-01-15 02:05 UTC)

<p>I would also recommend <a href="https://github.com/lassoan/SlicerElastix">SlicerElastix</a>. Its default rigid and non-rigid presets usually work without any parameter tuning. If you use BRAINS then you typically need to spend some time with finding parameter settings that provide meaningful results.</p>

---
