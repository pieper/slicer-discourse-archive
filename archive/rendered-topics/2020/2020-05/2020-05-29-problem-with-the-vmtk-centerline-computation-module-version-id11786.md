---
topic_id: 11786
title: "Problem With The Vmtk Centerline Computation Module Version"
date: 2020-05-29
url: https://discourse.slicer.org/t/11786
---

# Problem with the VMTK Centerline Computation module version

**Topic ID**: 11786
**Date**: 2020-05-29
**URL**: https://discourse.slicer.org/t/problem-with-the-vmtk-centerline-computation-module-version/11786

---

## Post #1 by @Jerome_Szewczyk (2020-05-29 18:53 UTC)

<p>Operating system:windows10<br>
Slicer version:4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi every one,<br>
I recently installed the “VMTK Centerline Computation” module using the extension manager interface. But the module I got seems to have functionalities in reduced number compared to those presented on the wiki : “Modules: VMTK in 3D Slicer Tutorial: Coronary Artery Centerline Extraction”. In particular I can not place target seeds on my model. Is that a matter of version ?<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2020-05-29 23:53 UTC)

<p>Try a recent Slicer Preview Release and let us know if you still have questions. Describe what you would like to achieve, what did you do, what you expected to happen, and what happened instead.</p>

---

## Post #3 by @Jerome_Szewczyk (2020-06-03 08:23 UTC)

<p>Sorry Andras for my lake of clarity. Actually, I segmented a biliary tree from RMI images :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9a557db231455a961080b148b28b77b0ade589c.png" alt="image" data-base62-sha1="zCt8rT4WU9kIQbyKd2U5PNunxbC" width="268" height="250"><br>
Then I extracted its centerlines. For that I went to the 'VMTK centerline computation’ module. I defined an origine seed and ran the extraction. The result is pretty good, I get all the lines for the tree as a whole. My issue is that I would like to extract the lines one by one, in each branch independently starting from the origine seed I placed at the bottom of the main duct. It seems difficult as I can’t specify any target seed at the top of the branch I am interested in, this functionality seems not proposed on my panel (no fiducial command associated to ‘centerline endpoints’) :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b986d0e7b6da4f0bca7e30b3d4d1e311c8338a2d.png" alt="image" data-base62-sha1="qtfaN4KvFYyZRf0XIdIvBom9gS1" width="311" height="277"><br>
Do I have to activate something ? Sgould I load a new version of the VMTK extension ?<br>
Thanks in advance.</p>

---
