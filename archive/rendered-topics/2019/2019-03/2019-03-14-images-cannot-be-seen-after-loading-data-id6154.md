---
topic_id: 6154
title: "Images Cannot Be Seen After Loading Data"
date: 2019-03-14
url: https://discourse.slicer.org/t/6154
---

# Images cannot be seen after loading data

**Topic ID**: 6154
**Date**: 2019-03-14
**URL**: https://discourse.slicer.org/t/images-cannot-be-seen-after-loading-data/6154

---

## Post #1 by @mrtnh (2019-03-14 23:27 UTC)

<p>Problem report for Slicer 4.10.1 win-amd64: [please describe expected and actual behavior]</p>
<p>expected: see the images after loading the data<br>
actual: data are loaded but no images can be seen</p>
<p>Hi,<br>
I have just installed the 3D Slicer and wanted to go through the tutorials but I can not see any images after lodading the MRHead data from the Slicer Welcome tutorial (or from other tutorials). In the log messages there are many ERRORs saying “GLEW could not be initialized”, few saying “Hardware does not support the number of textures defined.” and several WARNINGs saying “versionFunctions: Not supported on OpenGL ES”.</p>
<p>I would be grateful for pointing me to what could be wrong or how to fix this.</p>
<p>Thank you.<br>
Martin</p>

---

## Post #2 by @lassoan (2019-03-14 23:46 UTC)

<p>It might be possible that your computer does not meet minimum graphics requirement (graphics card with support of OpenGL 3.2 or higher). What computer do you use (operating system, CPU, graphics card)?</p>

---

## Post #3 by @mrtnh (2019-03-15 02:50 UTC)

<p>Thank you for such a quick response.</p>
<p>According to OpenGL Extensions Viewer 5.1.4, my notebook has Intel HD Graphics 4400, OpenGL version 4.3. Computer has Windows 7 Home Premium, Intel Core i5-4210U CPU <span class="mention">@1.70</span> GHz, 8 GB RAM.</p>
<p>But the 3D Slicer Bug report says something about OpenGL2:<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Session start time …: 2019-03-14 16:40:41<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Slicer version …: 4.10.1 (revision 27931) win-amd64 - installed release<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Operating system …: Windows / 7 / Service Pack 1 (Build 7601) - 64-bit<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Memory …: 8064 MB physical, 8221 MB virtual<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 14.03.2019 16:40:41 [] (unknown:0) - Additional module paths …: (none)</p>
<p>Thank you for your help.</p>

---

## Post #4 by @lassoan (2019-03-15 22:12 UTC)

<p>This computer has a chipset that is 5 generations behind the current ones. Since early versions of integrated Intel video cards had many issues, recent Slicer versions might not be compatible with it. Also, even Microsoft has stopped general support of Windows7 a long time ago - let alone driver or application developers.</p>
<p>If you upgrade your video card drivers and/or your operating system to Windows10 then you might have a chance that it’ll start working.</p>

---

## Post #5 by @mrtnh (2019-03-17 02:21 UTC)

<p>Thank you. I have not realized that I am so behind the current technology… Updating the video drivers was not enough so I will try newer computer.</p>

---
