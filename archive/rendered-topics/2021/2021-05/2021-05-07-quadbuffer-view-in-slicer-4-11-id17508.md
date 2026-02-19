---
topic_id: 17508
title: "Quadbuffer View In Slicer 4 11"
date: 2021-05-07
url: https://discourse.slicer.org/t/17508
---

# QuadBuffer view in Slicer 4.11

**Topic ID**: 17508
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/quadbuffer-view-in-slicer-4-11/17508

---

## Post #1 by @MarineC (2021-05-07 14:41 UTC)

<p>Hi everyone,</p>
<p>I wanted to try the “quad buffer” display on Slicer 4.11.20210226 but unfortunatly it didn’t work for me…<br>
What I did was enabling Quad Buffer Stereo settings for my graphic card (AMD FirePro, using Win 10 btw) before launching Slicer.<br>
However, when I launched Slicer to test it out, nothing happened when I clicked on the QuadBuffer button (whereas when I test Red/Blue the image changes). I tried Stereoscopic player to see if my computer was the problem but this worked well.</p>
<p>Do you know if I missed something ? A module to install or anything ?<br>
Went through the forum to see if the problem as already been solved but found nothing, sorry if I missed a relevant topic.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2021-05-07 14:59 UTC)

<p>Hi <a class="mention" href="/u/marinec">@MarineC</a>  - I don’t think that mode is used very much so it may not be working in the current Slicer/VTK combination or build settings.  Best thing to debug would be to see if the vtk code itself is supporting that mode by building a small vtk app against a local build of Slicer’s vtk (or perhaps you can try enabling it using a python program running in Slicer - not sure if that’s possible since there might be compile time options required).</p>

---

## Post #3 by @MarineC (2021-05-10 08:57 UTC)

<p>Hello again,</p>
<p>Thanks for your answer ! If I understood correctly I should try to do my own QuadBuffer plugin based on VTK, to see if it is still possible to do this kind of rendering using VTK. And then compare it to the actual plugin?<br>
I guess that looking at what changes has been made between Slicer 4.8 (where the module worked) and 4.11 would be too hard/time consuming?</p>

---

## Post #4 by @pieper (2021-05-10 14:55 UTC)

<aside class="quote no-group" data-username="MarineC" data-post="3" data-topic="17508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/779978/48.png" class="avatar"> MarineC:</div>
<blockquote>
<p>f I understood correctly I should try to do my own QuadBuffer plugin based on VTK, to see if it is still possible to do this kind of rendering using VTK. And then compare it to the actual plugin?</p>
</blockquote>
</aside>
<p>Yes, basically.  What I meant was that if you build your own Slicer locally you will get a VTK-build directory that is built using Slicer’s version and settings.  Using that you should be able to compile a small demo program and see if you can enable QuadBuffering.  From there you will know what the requirements are.  I haven’t followed the details but there are interactions between VTK and Qt that determine which opengl settings are possible.  For QuadBuffering you may need to create a vtk render window that’s not in a QWidget and hook that to the Slicer rendering code.</p>

---

## Post #5 by @MarineC (2021-05-11 15:10 UTC)

<p>So I built Slicer 4.11 from source (the branch 4.11 from the github) and indeed there is an error when clicking on the No stereo button AFTER clicking on the quadbuffer button:</p>
<p><code>Warning: In C:\S4\S4R\VTK\Rendering\Core\vtkRenderWindow.cxx, line 240</code><br>
<code>vtkGenericOpenGLRenderWindow (00000185F9811E80): Adjusting stereo mode on a window that does not support stereo type CrystalEyes is not possible. </code></p>
<p>Don’t know why it is not showing this message the first time I clicked on it… And as my competences in C++ are limited, I still wanted to see if and how it was working on version 4.8.0.<br>
So I tried building Slicer 4.8.0 from source too, as I know QuadBuffer is working there, so I could get any info on what I should do. Hovewer another error spawned while trying to generate the cmake file :</p>
<p><code>Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE)</code><br>
<code>CMake Error at CMakeLists.txt:151 (message):      error: Install SVN and try to re-configure </code></p>
<p>I know this error has nothing to do with this topic but I encountered it while trying to get infos about the quadbuffer view. It appears only with this branch I am created using tag v4.8.x…<br>
I can create another topic and explain this problem more in depths there if you want. Or just stop trying building 3DSlicer 4.8.x if you think it won’t help me.</p>
<p>Anyway I will look further into the vtkRenderWindow.cxx file to see what I can get from there and try to create my own rendering window.</p>
<p>Thanks for the help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @MarineC (2021-05-11 15:21 UTC)

<p>Sorry just thought about something, maybe the SVN error it is due to versions not compatible (my CMake may be too new for this version of Slicer) between actual dependencies and the old Slicer.</p>
<p>Still I can move this part of my messages to a diff topic if you want.</p>
<p>Sorry for the inconvenience <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>

---

## Post #7 by @pieper (2021-05-11 17:42 UTC)

<p>Hi Marine - I suggest you don’t try building 4.8 from source.  It could require some work to make it compatible with modern cmake and compilers (missing svn might be just the first of many issues).</p>
<p>Better to focus your work on getting the VTK that Slicer uses to work with QuadBuffer mode.</p>
<p>Since you have the current Slicer code compiled you are in good shape to do further investigation.  I’d suggest you try a simple example from <a href="https://kitware.github.io/vtk-examples/site/">VTK Examples</a>, read all the google search results you can find about CrystalEyes mode (like <a href="https://vtk.org/pipermail/vtkusers/2018-June/102069.html">this one</a>), and see if you can get it to work outside of Slicer and then see if you can replicate that inside of Slicer.</p>

---

## Post #8 by @MarineC (2021-06-03 14:57 UTC)

<p>Hi!<br>
Thanks for your help, I managed to make a small widget display things in quadbuffer mode using VTK!</p>
<p>To implement this on Slicer, I thought I would use the View Controllers module as a template but I’m a noob on C++, so I had trouble understanding the structure of the module. I saw the 3d part of the view is handled line 123 of the qSlicerViewControllersModuleWidget.cxx file.<br>
So my guess is, if I want to use my own parameters for the render window, I have to wire my widget to the node in charge of rendering the model in 3d? And same for the interactor? Hence, I would “just” need to remplace the mapper+actor I created with the actual 3d model from Slicer.</p>
<p>Did my best explaining it, sorry if it’s fuzzy <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>

---

## Post #9 by @pieper (2021-06-09 14:08 UTC)

<p>That sounds like great progress <a class="mention" href="/u/marinec">@MarineC</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>It could help if you post your progress to a github repository for reference.</p>
<p>If you have a pure VTK example, then the next step is to make a Qt version.  There are some issues related to setting up OpenGL in Qt vs VTK, and if you can get that working to meet your QuadBuffer requirements you will be most of the way there.</p>
<p>Once you know how to make that work as expected, then the same settings would need to be exposed through <a href="https://github.com/commontk/CTK">CTK</a>, which is the layer at which Slicer’s Qt/VTK functionality is implemented.  At that point Slicer can be adapted to use or not use these settings to suit the users needs and available hardware.</p>

---

## Post #10 by @MarineC (2021-06-09 16:14 UTC)

<p>Here is <a href="https://github.com/Lazarius2160/Internship_master1" rel="noopener nofollow ugc">my repo</a>, tried to tidy it up a bit <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>I think I used both vtk and Qt to make my widget working (it’s on my repo), and as I found out it was possible to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-3d-view-outside-the-view-layout" rel="noopener nofollow ugc">Show a 3D view outside the view layout</a>, so now I am trying to create a new 3D widget to display into in Quad Buffer. Which means I have to :</p>
<ul>
<li>see how I can create a <a href="https://vtk.org/doc/nightly/html/classQVTKOpenGLStereoWidget.html" rel="noopener nofollow ugc">QVTKOpenGLStereoWidget</a> instead of a <a href="http://apidocs.slicer.org/master/classqMRMLThreeDWidget.html#aa489037124728d003ccc34b1c4207517" rel="noopener nofollow ugc">qMRMLThreeDWidget</a> to render the widget in quadbuff,</li>
<li>see how I can change the parameters of the renderwindow inside that widget.</li>
</ul>
<p>I saw it deals with <a href="http://apidocs.slicer.org/master/classvtkMRMLViewDisplayableManager.html" rel="noopener nofollow ugc">vtkMRMLViewDisplayableManager</a> among others, but for now I don’t know where I can change the parameters of the render window exactly.<br>
Do you think its something about CTK? Never used it, I’ll have a look. Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #11 by @pieper (2021-06-09 17:03 UTC)

<p>Looks like you are on a good track.  I haven’t worked on this layer much myself in the current incarnation, and even then not for several years so I’m not sure which aspects you will need to touch.  The CTK layer handles some of the initializations and event management that might be needed if you are in the Slicer layout, but if your ZSpace window is the outside of the app and taking up the full screen it may be possible to bypass CTK, but there may be some impact on the interactive widgets (i.e. markups).  Good luck <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #12 by @MarineC (2021-06-14 11:54 UTC)

<p>Indeed as you said, in order to change settings in the render window, I needed to use the <a href="http://www.commontk.org/docs/html/classctkVTKRenderView.html" rel="noopener nofollow ugc">CTK layer</a> !<br>
I’ll create another topic to see if someone knows if I can use a QVTKOpenGLStereoWidget instead of a qMRMLThreeDWidget in Slicer.<br>
Thanks for the help!</p>

---

## Post #13 by @lassoan (2021-06-16 21:06 UTC)

<p>You will keep using qMRMLThreeDWidget, you’ll just need to change the Qt widget that hosts the VTK renderer. CTK has build options to choose what widget to use as a basis for qMRMLThreeDWidget. QVTKOpenGLStereoWidget has issues in certain situations (e.g., when it is placed in a scrolling window - see discussions on the VTK forum) but as an experiment you can try to use it as a base class (and it should be possible to find solutions for using this widget as a base class for some special views).</p>

---

## Post #14 by @MarineC (2021-06-18 09:52 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> !</p>
<p>Yes unfortunatly I know about the problems regarding QVTKOpenGLStereoWidget. I’ve tried different type of widgets such as the Native one with what I though been the proper options, however, as it does not support stereo by design as I’ve understood, I cannot use it at all.</p>
<p>About CTK, I’ve found inside the <a href="http://www.commontk.org/docs/html/classctkVTKAbstractView.html" rel="noopener nofollow ugc">ctkVTKAbstractView.cpp</a> file that the function <em>init</em> would create a  ctkVTKOpenGLNativeWidget. So, does it mean I have to modify that method, so my init method would create a stereo widget instead of a native one?<br>
I may be looking at the wrong place, from what you said I though I would have to change some parameters in a method, and not reimplement it. But, for now, I did not found which class/method I would need. If you have any idea where I can look at it would be very useful to me.</p>
<p>Thanks for the help!</p>

---

## Post #15 by @lassoan (2021-06-18 19:50 UTC)

<p>In ctkVTKOpenGLNativeWidget.h there are already two options (selected by CMake configuration options) for choosing between QVTKOpenGLNativeWidget and QVTKOpenGLWidget. You can add a third option there or just change QVTKOpenGLNativeWidget to QVTKOpenGLStereoWidget as a test.</p>

---
