# Segment Editor source code

**Topic ID**: 5845
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/segment-editor-source-code/5845

---

## Post #1 by @dp1991 (2019-02-20 14:07 UTC)

<p>Hello friends,<br>
I have a question<br>
How can I use " Segment Editor " ( 3d slicer module), in VS2015 C++  ??<br>
I need the  source code of this module<br>
Can anyone help me ??</p>

---

## Post #2 by @jamesobutler (2019-02-20 15:08 UTC)

<p>Segment Editor is a Slicer scripted module written in python (see code <a href="https://github.com/Slicer/Slicer/blob/2e5dcf178d0d26d359a10437aa16223e3a594e2f/Modules/Scripted/SegmentEditor/SegmentEditor.py" rel="nofollow noopener">here</a>).  Some editor effects are written in C++ (see code <a href="https://github.com/Slicer/Slicer/tree/4c0b0b15276aedc0e12d77e2227536426979d773/Modules/Loadable/Segmentations/EditorEffects" rel="nofollow noopener">here</a>) and some are written in python (see code <a href="https://github.com/Slicer/Slicer/tree/e72ef376ddb0bf1e8d52d080c2355620ac3b4abf/Modules/Loadable/Segmentations/EditorEffects/Python" rel="nofollow noopener">here</a>).</p>
<p>What is the end goal that you are trying to accomplish?  There are people on the forum that will be able to better support you with some extra information.</p>

---

## Post #3 by @cpinter (2019-02-20 15:12 UTC)

<p>And for usage, please check out these tutorials: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #4 by @dp1991 (2019-02-23 05:03 UTC)

<p>Hi<br>
thank u for your answers.<br>
i need to edit segmentation in all 3d view ( axial , sagittal , coronal )<br>
exactly like this  <a href="https://youtu.be/BJoIexIvtGo" rel="nofollow noopener">https://youtu.be/BJoIexIvtGo</a><br>
i need source code for this in C++ and VS215 and ITK and VTK<br>
(I apologize , my English language is not well ) <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=6" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #5 by @lassoan (2019-02-23 05:21 UTC)

<p>See links to the source code above.</p>

---

## Post #6 by @dp1991 (2019-02-24 06:19 UTC)

<p>I need source code of  "paint " in segment editor<br>
at c++ and vs2015<br>
steps of my program<br>
1 - load dicom image ( ITK or VTK )<br>
2 - manual segmentation 3d view " axial sagittal coronal "<br>
exactly like 3d slicer…</p>

---

## Post #7 by @lassoan (2019-02-24 13:49 UTC)

<aside class="quote no-group" data-username="dp1991" data-post="6" data-topic="5845">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dp1991/48/3142_2.png" class="avatar"> dp1991:</div>
<blockquote>
<p>exactly like 3d slicer</p>
</blockquote>
</aside>
<p>If you need a software that works exactly like 3D Slicer then it seems reasonable to use 3D Slicer. We put a lot of work into making Slicer appearance and behavior completely customizable for any particular workflow, so you don’t need to start a new project from scratch.</p>
<p>We allow usage of Slicer source code for any purpose in any project, so if you want to create a new software application the you are free to do so. However, we don’t have the capacity to actively help you in those efforts.</p>

---

## Post #8 by @cpinter (2019-02-24 17:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="5845">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you need a software that works exactly like 3D Slicer then it seems reasonable to use 3D Slicer.</p>
</blockquote>
</aside>
<p>Indeed, doesn’t seem like a crazy idea at all <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><a class="mention" href="/u/dp1991">@dp1991</a> If you want to create an application that uses 3D Slicer features but is less complex and more fitted to your workflow, then you can develop a slicelet. Here’s the documentation:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a><br>
And here’s an example that works well, and is freely available:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerRt/GelDosimetryAnalysis">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/GelDosimetryAnalysis" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/a543d5eeb1e55cb6afc395088952d5cffde39bce9e4b2d1b01b4a6605a2755e3/SlicerRt/GelDosimetryAnalysis" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerRt/GelDosimetryAnalysis" target="_blank" rel="noopener">GitHub - SlicerRt/GelDosimetryAnalysis: 3D Slicer extension containing a...</a></h3>

  <p>3D Slicer extension containing a slicelet that covers the gel dosimetry analysis workflow used in commissioning new radiation techniques and to validate the accuracy of radiation treatment by enabl...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or if you want to use Slicer in an application that “doesn’t look like Slicer”, then you can create a SlicerCustomApp:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/5b6f8f0ec331b474e0e31bbae48b9d7865b118945590f0ba7a02feed32fe4371/KitwareMedical/SlicerCustomAppTemplate" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a...</a></h3>

  <p>Template to be used as a starting point for creating a custom 3D Slicer application - GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @dp1991 (2019-02-25 05:11 UTC)

<p>I will writing new software  that manual segmentation is one part of this software<br>
i need to edit or draw segmentation in 3 view (axial coronal sagittal) and display result in 3d space<br>
i saw " edit segmentation " is useful for this purpose<br>
i write my program in  VisualStudion2015 and C++ language programming<br>
so I need source code of  " edit segmentation " in c++ and visual studio<br>
( I again apologize for my English language  and very thank u for your guidance and helps )</p>

---

## Post #10 by @pieper (2019-02-25 12:20 UTC)

<p>Hi <a class="mention" href="/u/dp1991">@dp1991</a> - thanks for providing more details.  I think you’ll find a lot of helpful resources at the slicer, vtk, itk, and related web sites that could help with a project to write a program in C++ for viewing and segmenting 3D data.  As Andras and Csaba have pointed out, 3D Slicer already provides a fully open source implementation of a wide range of features and is fully customizable.  We hope you find it useful either as-is or as inspiration for whatever you choose to write.</p>
<p>Since it sounds like you are new to this field, I would also suggest you base your work on 3D Slicer as an existing platform rather than reinventing something very similar from the ground up.</p>

---

## Post #11 by @dp1991 (2019-02-26 05:23 UTC)

<p>thanks for all answers …<img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=6" title=":rose:" class="emoji" alt=":rose:"><img src="https://emoji.discourse-cdn.com/twitter/rose.png?v=6" title=":rose:" class="emoji" alt=":rose:"></p>

---
