---
topic_id: 34952
title: "3Dslicer To Three Js"
date: 2024-03-18
url: https://discourse.slicer.org/t/34952
---

# 3Dslicer to three.js

**Topic ID**: 34952
**Date**: 2024-03-18
**URL**: https://discourse.slicer.org/t/3dslicer-to-three-js/34952

---

## Post #1 by @Young_Wang (2024-03-18 12:20 UTC)

<p>Hi Everyone,</p>
<p>I’ve recently started a personal project to showcase 3D volumes on the web using three.js. Currently, I’m in the process of refining my workflow, and I wanted to share my current steps with you all. I came across openPlan, though I haven’t had the chance to explore it yet.</p>
<ol>
<li>Convert 3D data from a customized format to DICOM.</li>
<li>3Dslicer to read the DICOM files for further processing.</li>
<li>Export the processed DICOM data and import it into Blender using OrtogOnBlender.</li>
<li>Finally, export the Blender scene and integrate it into a web environment using three.js.</li>
</ol>
<p>I’m curious if anyone else has tackled a similar project in the past and would greatly appreciate any insights or advice you might have to offer.</p>
<p>Best,</p>

---

## Post #2 by @lassoan (2024-03-18 14:48 UTC)

<p>I would recommend to use <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/README.md">OpenAnatomy extension to export to glTF format</a> and visualize it directly using <a href="http://3dviewer.net">3dviewer.net</a> web viewer (see for example how it can view a <a href="https://3dviewer.net/#model=https://www.dropbox.com/s/38arwo2uhzu0ydg/SPL-Abdominal-Atlas.gltf?dl=0">segmentation directly exported from Slicer</a>).</p>
<p>You can discuss this with others who are doing similar websites - see for example this topic:</p>
<aside class="quote" data-post="18" data-topic="34782">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafael_v_monteiro/48/16558_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/presents-the-brazilian-fauna-virtual-anatomic-collection/34782/18">Presents the 'Brazilian Fauna Virtual Anatomic Collection'</a> <a class="badge-category__wrapper " href="/c/community/success-stories/29"><span data-category-id="29" style="--category-badge-color: #92278F; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos."><span class="badge-category__name">Success stories</span></span></a>
  </div>
  <blockquote>
    Got the problems. I have to think if it is functional to reopen a no-transparency model when user click on measure tool. 
But I certainly will have a try in the ColorizeModel to address these questions. 
Thank you very much, best regards, 
Rafa
  </blockquote>
</aside>

<p>I’m not sure if it is worth spending a whole lot of time with three.js because its primary intended use is not scientific visualization. It has some pretty significant limitations, such as <a href="https://threejs.org/manual/#en/transparency">it cannot render semi-transparent surfaces correctly</a>, its volume rendering is very primitive, and it does not have basic tools built in, such as image slice rendering (in case anyone wants to look at the original image data). Now that VTK can run in the web browser, it seems to make more sense to use VTK-based viewers. A nice example is Kitware’s <a href="https://volview.kitware.com/">VolView</a>. We also plan to make more and more of Slicer directly usable in a web browser, leveraging VTK and webassembly. So, already in the short term, but especially in the long term, you may be better off if you remain in the scientific/medical image computing software ecosystem and keep using VTK (outside of Slicer now, but possibly within Slicer in a few years) instead of switching to three.js.</p>
<p>Regarding Blender: Blender will always remain a more powerful 3D modeling tool for artistic visualization, but most of the scientific use cases should be possible to cover just as well (and in many cases better) by VTK-based applications, such as Slicer or ParaView. You can already do a lot of modeling and set up of nice visualizations in Slicer; and if you miss any specific features then let’s discuss them, because they may be easy to add - as they may already exist in VTK and just need to be exposed.</p>

---

## Post #3 by @Young_Wang (2024-03-18 14:52 UTC)

<p>I appreciate the detailed answer and thank you for those suggestions!</p>

---
