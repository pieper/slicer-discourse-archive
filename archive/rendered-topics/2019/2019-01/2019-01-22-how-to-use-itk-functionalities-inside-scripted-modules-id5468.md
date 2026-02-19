---
topic_id: 5468
title: "How To Use Itk Functionalities Inside Scripted Modules"
date: 2019-01-22
url: https://discourse.slicer.org/t/5468
---

# How to use ITK functionalities inside scripted modules

**Topic ID**: 5468
**Date**: 2019-01-22
**URL**: https://discourse.slicer.org/t/how-to-use-itk-functionalities-inside-scripted-modules/5468

---

## Post #1 by @MachadoL (2019-01-22 18:09 UTC)

<p>Operating system: Linux Mint 18<br>
Slicer version: 4.10<br>
Expected behavior: Import ITK to be recognized<br>
Actual behavior: Cmake crashes when configuring and generating.</p>
<p>Hi guys,</p>
<p>I’d like to know how can i use ITK package inside my (python) scripted module for 3d Slicer 4.10.<br>
I created the standard extension using extension wizard and then try to modify the .py file inserting “Import itk” comand in the file’s header. However, I can’t go further because CMake start to bug in the configuration errors in the configuring/generating step.<br>
Sometimes, I can config., gen. and make. But then when I open 3DSlicer, it cannot even find the module on its module options.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2019-01-22 18:31 UTC)

<p>You can use ITK proper in CLI modules or C++ loadable modules, while in scripted modules you can use ITK via its more user-friendly <a href="http://www.simpleitk.org/" rel="nofollow noopener">SimpleITK</a> interface.</p>

---

## Post #3 by @MachadoL (2019-01-22 20:01 UTC)

<p>Great. I imported SimpleITK and it worked.</p>
<p>But would I install a random python package that I maybe interested in using inside python script?</p>
<p>Thank you, Lasso.</p>

---

## Post #4 by @lassoan (2019-01-22 21:00 UTC)

<p>Currently, you cannot install arbitrary Python packages on all operating systems, but hopefully in 1-2 months you’ll be able to do that. See some information in this topic: <a href="https://discourse.slicer.org/t/rpy2-pip-installation-fails/4883" class="inline-onebox">Rpy2 pip installation fails</a>.</p>

---
