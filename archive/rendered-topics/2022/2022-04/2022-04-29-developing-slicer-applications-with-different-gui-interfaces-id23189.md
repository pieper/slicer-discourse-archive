---
topic_id: 23189
title: "Developing Slicer Applications With Different Gui Interfaces"
date: 2022-04-29
url: https://discourse.slicer.org/t/23189
---

# Developing slicer applications with different GUI interfaces based on slicer

**Topic ID**: 23189
**Date**: 2022-04-29
**URL**: https://discourse.slicer.org/t/developing-slicer-applications-with-different-gui-interfaces-based-on-slicer/23189

---

## Post #1 by @zhiyuan (2022-04-29 06:33 UTC)

<p>I am a graduate student from China who studies biomedical image processing. Recently, I have a research project that needs to cut the surface of the segmented 3D medical image, which can just use some functions of 3D slicer. Therefore, I would like to ask whether I can develop my own slicer application based on our 3dslicer. The appeal is that when I open the EXE file, The interface displays not the original slicer interface, but the GUI interface that I redefined according to my own needs. If I can, what do I need to do? I tried the code of quicksegment in the forum. I downloaded the zip into my pycharm environment. When running, it shows that I don’t have VTK, QT and other packages, but I PIP these packages from anaconda, and it will show that I can’t find packages. Therefore, I don’t know, How to develop your own slicer application? Can you give me a tutorial or example? Thank you very much![forum]This is a(<a href="https://discourse.slicer.org/t/creating-a-3d-slicer-extension-with-minimal-programming-skills/17208/33" class="inline-onebox">Creating a 3D Slicer extension with minimal programming skills - #33 by rbumm</a>) I watch</p>

---

## Post #2 by @qiqi5210 (2022-04-29 07:06 UTC)

<p>You can create a script module. If you want to complete a specific workflow, only change the interface of some slicers, such as the module interface on the left side of the window. In this way, the workload will be much smaller, and there is no need to build slicer</p>

---

## Post #3 by @zhiyuan (2022-04-29 09:18 UTC)

<p>How should I change the slicer interface? I just came into contact with this software and don’t quite understand it</p>

---

## Post #4 by @qiqi5210 (2022-04-29 09:45 UTC)

<p><a href="https://data.kitware.com/#collection/568a9db98d777f429eac8eab/folder/5b0724188d777f15ebe1f55b" class="onebox" target="_blank" rel="noopener nofollow ugc">https://data.kitware.com/#collection/568a9db98d777f429eac8eab/folder/5b0724188d777f15ebe1f55b</a><br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.10/Training#Tutorials_for_software_developers</a><br>
You can look at these two links in Python. Of course, you’d better spend another day or two learning pyqt.</p>

---

## Post #5 by @ebrahim (2022-04-29 13:03 UTC)

<aside class="quote no-group" data-username="zhiyuan" data-post="1" data-topic="23189">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/a87d85/48.png" class="avatar"> zhiyuan:</div>
<blockquote>
<p>The interface displays not the original slicer interface, but the GUI interface that I redefined according to my own needs.</p>
</blockquote>
</aside>
<p>For this level of customization you may also want to consider the more involved possibility of making a Slicer Custom App.</p>
<ul>
<li><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">use this cookiecutter to create a custom app</a></li>
<li><a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">learn more about it here</a></li>
</ul>
<p>Starting by making a scripted module makes sense. If you find that you need more customization, then you can look into SlicerCAT.</p>

---
