---
topic_id: 2607
title: "Is There Any Way To Use 3D Slicer Libraries And Make My Own"
date: 2018-04-17
url: https://discourse.slicer.org/t/2607
---

# Is there any way to use 3d slicer libraries and make my own GUI

**Topic ID**: 2607
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-use-3d-slicer-libraries-and-make-my-own-gui/2607

---

## Post #1 by @rasoul (2018-04-17 10:49 UTC)

<p>Operating system:Win 7<br>
Slicer version:4.8</p>
<p>I wanna to develop my own GUI that uses benefits of 3d_slicer and also ITK image processing classes. What should I do? Is it possible?</p>

---

## Post #2 by @adamrankin (2018-04-17 13:26 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #3 by @rasoul (2018-04-17 06:35 UTC)

<p>Hi every one<br>
I am new to slicer so my question maybe a beginner one,<br>
I wanna use libraries of slicer in c++ to use its benefits in my image processing program.<br>
For example I wanna have an Interface like what it is available in slicer to load my images, choose my ROI edit it and … .<br>
I have built ITK, VTK, Opencv and I hope I Would combine these three libraries with 3d_Slicer together.<br>
Is it possible?</p>

---

## Post #4 by @ihnorton (2018-04-17 13:30 UTC)

<p>See also:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers</a></p>
<p>Note that Slicer already builds ITK and VTK, and there is an OpenCV extension. Look at the examples of existing extensions at the link below, all of which should have links to the source code:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions</a></p>

---

## Post #5 by @rasoul (2018-04-17 14:15 UTC)

<p>thank you adamrankin, It seems what I am searching about.<br>
But two more questions:<br>
As I see Slicelets could help me to choose my image tools from 3d_slicer. Am I right? How? Is there more comprehensive tutorial?<br>
As I understand Slicelets should be used in python. Is there any c++ equivalent?</p>

---

## Post #6 by @rasoul (2018-04-17 14:21 UTC)

<p>Thanks a lot Nortron,<br>
But I wanna develop my own GUI using these libraries not using extensions. 3d_slicer give me too much more than I want. Do you have any suggestion? Is my way logical?</p>

---

## Post #7 by @ihnorton (2018-04-17 14:33 UTC)

<aside class="quote no-group" data-username="rasoul" data-post="6" data-topic="2607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rasoul/48/1493_2.png" class="avatar"> rasoul:</div>
<blockquote>
<p>But I wanna develop my own GUI using these libraries not using extensions. 3d_slicer give me too much more than I want. Do you have any suggestion? Is my way logical?</p>
</blockquote>
</aside>
<p>This is a really broad question. You need to learn Qt or another GUI framework, learn to build C++ code, etc. There are many tutorials on the internet. To start, see some nice links <code>@lassoan</code> just compiled <a href="https://discourse.slicer.org/t/a-free-biomedical-image-analysis-and-visualization-2-day-course/2584/10">here</a>.</p>
<p>We provide a lot of support for building modules <em>within Slicer</em>, and the goal is to make development faster and easier than building everything from scratch (especially if you use Python). If you want to do something else you are free to do that, of course – the code is all open source under a completely permissive license (BSD like) so you can use the pieces you need, under the license, or read the code to learn.</p>

---

## Post #8 by @lassoan (2018-04-17 21:32 UTC)

<p>For commercial applications we often replace the entire Slicer GUI, use customized main window, custom branding, etc. Even in these cases, custom code is still bundled with Slicer as an extension.</p>

---

## Post #9 by @rasoul (2018-04-18 07:40 UTC)

<p>Thanks lassoan,<br>
How we can do that?<br>
I mean replacing the entire Slicer GUI and customizing it but using Slicer image tools.</p>

---

## Post #10 by @rasoul (2018-04-18 07:45 UTC)

<p>Is it possible to use those pieces that I want in Qt or another GUI framework? Any useful link would be grateful.</p>

---

## Post #11 by @cpinter (2018-04-18 12:22 UTC)

<p>Both <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/adamrankin">@adamrankin</a> are talking about slicelets:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---

## Post #12 by @ihnorton (2018-04-18 13:06 UTC)

<p>There are many snippets to start from in the VTK examples, from the links listed by Andras. In particular:</p>
<p><a href="https://www.vtk.org/Wiki/VTK/Examples/Cxx/Qt" class="onebox" target="_blank">https://www.vtk.org/Wiki/VTK/Examples/Cxx/Qt</a></p>

---

## Post #13 by @rasoul (2018-04-19 07:50 UTC)

<p>I concluded from these comments that there is no way to use 3d_slicer libraries in c++. I can just use VTK and ITK libraries and make my GUI with Qt or use Slicelets to make GUI in python.<br>
Am I right?</p>

---

## Post #14 by @pieper (2018-04-19 12:37 UTC)

<aside class="quote no-group" data-username="rasoul" data-post="13" data-topic="2607" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rasoul/48/1493_2.png" class="avatar"> rasoul:</div>
<blockquote>
<p>I concluded from these comments that there is no way to use 3d_slicer libraries in c++. I can just use VTK and ITK libraries and make my GUI with Qt or use Slicelets to make GUI in python.</p>
<p>Am I right?</p>
</blockquote>
</aside>
<p>No, that’s not right - you can definitely write a new C++ application using any of the Slicer libraries.  You can look at the existing Slicer main application or at the corresponding tests as examples for how to structure an executable that links to the Slicer libraries.  Much of the core of Slicer is intentionally written to avoid dependencies on python (however some modules do require python).</p>
<p>Just to be clear, we suggest people consider Slicelets for most use case because there are many challenges when trying to package an application for installation on user computers, particularly if you wish to support cross-platform installation.  Slicelets allow you to leverage the significant infrastructure Slicer already provides.</p>
<p>The advantages of a non-Slicelet approach could be smaller installation package and faster startup times, so that’s worth considering if those are priorities for you.</p>

---

## Post #15 by @rasoul (2018-04-25 05:35 UTC)

<p>Thanks a lot pieper,<br>
Your answer was so hopefull. Could you please give me the example links that use 3dslicer C++ libraries?</p>
<p>I am searching for something like itk or opencv libraries usage.</p>
<p>Do you have any suggestion about combining itk and vtk librarues in a GUI?</p>

---

## Post #16 by @cpinter (2018-04-25 16:21 UTC)

<p>A C++ example for an application that uses Slicer libraries is SlicerApp:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp" target="_blank" rel="noopener">Slicer/Applications/SlicerApp at main · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp" target="_blank" rel="noopener">main/Applications/SlicerApp</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>ITK does not provide a GUI, and VTK provides viewers for 2D and 3D data visualization. You’ll need a generic UI toolkit like Qt to do your application. This is also what Slicer uses.</p>
<p>Can you please tell us the reason why you’re so reluctant to rely on Slicer to build your own GUI? It would be much simpler overall, and I’m sure you’d save a ton of time doing that.</p>

---

## Post #17 by @rasoul (2018-04-26 21:36 UTC)

<p>Thank you a lot <a class="mention" href="/u/cpinter">@cpinter</a>,<br>
I am searching to find a way to do <strong>“an application that is like a commercial one.”</strong> <a class="mention" href="/u/lassoan">@lassoan</a> said : " we often replace the entire Slicer GUI, use customized main window, custom branding, etc. Even in these cases, custom code is still bundled with Slicer as an extension."<br>
That’s so good, but I want to make something that is not an extension of Slicer because I think in this way I still have its main GUI.<br>
In another word <strong>It would be more beautiful if it would be independent of Slicer in GUI layer, But use its benefits in background layer.</strong></p>

---

## Post #18 by @lassoan (2018-04-27 03:27 UTC)

<p>You don’t need to change a single line in Slicer core to completely replace the user interface. You can just hide any or all user interface elements of the application and display yours instead.</p>
<p>However, if you work primarily in C++ then you can also replace the application main window instead of customizing it, as described here: <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">https://github.com/KitwareMedical/SlicerCustomAppTemplate</a></p>
<p>Either way, your modules will be built as an extension, the same way as many other built-in Slicer modules are. You just specify location of your extension’s source code in <code>Slicer_EXTENSION_SOURCE_DIRS</code> variable and your extension will be built into your application.</p>

---

## Post #19 by @Phong_Tran (2019-09-26 10:59 UTC)

<p>Hi,<br>
I am new to this world. I am in charge of developing a micro service which handles dicom files as input and output to frontend via RESTful API. I am not sure if I can use the 3D slicer library without QT GUI and import them to my service ?</p>

---

## Post #20 by @pieper (2019-09-27 22:42 UTC)

<p>Hi Phong -</p>
<p>Yes, you certainly can do this, but it’s not the main use case for which Slicer was created and you may find that some featured are not available.  Slicer’s code is layered, so you can access MRML (data) and Logic VTK classes.</p>
<p>In my experience most use cases probably require functionality that is only available in a full running Slicer, so it’s maybe not a “micro” service, but you can run slicer inside docker and expose whatever interface you want (e.g. VNC).</p>

---

## Post #21 by @lassoan (2019-09-28 12:34 UTC)

<p>DICOM indexing and database uses Qt (database is used to resolve cross-references between DICOM files). So, for loading complex data sets, such as radiation therapy plans or structured reports you need these Qt based classes, but showing GUI is not necessary.</p>

---

## Post #22 by @lassoan (2021-05-11 04:39 UTC)

<p>A post was split to a new topic: <a href="/t/slicelet-for-position-tracking/17558">Slicelet for position tracking</a></p>

---
