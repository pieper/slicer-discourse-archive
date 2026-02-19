---
topic_id: 13598
title: "Slicer Cant Find Latest Opengl Drivers In Aws Workspaces"
date: 2020-09-22
url: https://discourse.slicer.org/t/13598
---

# slicer can't find latest OpenGL drivers in AWS workspaces

**Topic ID**: 13598
**Date**: 2020-09-22
**URL**: https://discourse.slicer.org/t/slicer-cant-find-latest-opengl-drivers-in-aws-workspaces/13598

---

## Post #1 by @ashish_mahabal (2020-09-22 01:14 UTC)

<p>Operating system: Linux (AWS workspaces Power Pro x86_64)<br>
Slicer version: 4.10.2<br>
Expected behavior: Display dicom images<br>
Actual behavior: Error message about not finding latest OpenGL drivers despite those being present on the system.</p>
<p>Unable to find OpenGL 3.2<br>
However, on the terminal when I do:</p>
<blockquote>
<p>glxinfo | grep OpenGL<br>
I get core profile and version string as 3.3<br>
I do get ES profile version string as OpenGL ES 2.0 Mesa 18.3.4</p>
</blockquote>
<p>Not sure how to make slicer find the latest version of OpenGL</p>
<p>Help appreciated.</p>
<p>Let me know if I can provide any more details. Right now the dicom images load but do not show up (are not seen).</p>
<p>Thanks!<br>
ashish</p>

---

## Post #2 by @lassoan (2020-09-22 01:21 UTC)

<p>Do other OpenGL applications work, such as <code>glxgears</code> test?<br>
Please also try with latest Slicer Preview Release.</p>

---

## Post #3 by @pieper (2020-09-22 12:24 UTC)

<p>I’ve run Slicer on AWS Workspace with Windows and it works fine, with GPU support.</p>
<p>GPU OpenGL on Linux is always tricky, so maybe Workspaces doesn’t provide the right hooks.</p>
<p>If Google Cloud is an option for you, <a href="https://github.com/QIICR/SlicerGCPSetup">these instructions work well for me.</a></p>
<p>Probably the same approach would work fine with EC2 as well.</p>

---

## Post #4 by @ashish_mahabal (2020-09-23 17:56 UTC)

<p>Will try that. Thanks for pointing it out. I was not aware of it. (Though it may end up being unconnected with the slicer part).</p>

---

## Post #5 by @ashish_mahabal (2020-09-23 17:57 UTC)

<p>Thank you, Steve. Google cloud or using a windows machine is not an option in this case as there are a lot of other projects that use this configuration.</p>

---

## Post #6 by @pieper (2020-09-23 18:21 UTC)

<p>What OS do you use on AWS Workspaces?  There’s a good change standard drivers will work, so long as you configure them right.</p>

---
