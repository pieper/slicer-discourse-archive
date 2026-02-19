---
topic_id: 14854
title: "Collision Detection Capabilities In 3D Slicer"
date: 2020-12-02
url: https://discourse.slicer.org/t/14854
---

# Collision Detection Capabilities in 3D Slicer

**Topic ID**: 14854
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/collision-detection-capabilities-in-3d-slicer/14854

---

## Post #1 by @Hikmat (2020-12-02 19:59 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.2</p>
<p>Hi,</p>
<p>I am working on a project that involves the incorporation of collision detection capabilities, to be applied to neurosurgical robotics applications.</p>
<p>Currently, the project is at its infancy, where I am attempting to model objects of interest in 3D Slicer and to explore collision detection features and capabilities.</p>
<p>I have built a module in Slicer to serve as a basic framework for such exploratory work. It involves the creation and loading of primitive <code>vtkMRMLModelNode</code> 3D objects into the scene, meant to simulate a neurosurgical setting (sphere = critical brain anatomy, rod = robotic arm).</p>
<p>The user can manipulate either object in 3D space by reorienting it and modifying its position and size. The module interface is as shown:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78c07d3faa9359c4811d32bed99c9fc9a96fe39b.png" data-download-href="/uploads/short-url/hedHzt9Zqwv9io4H7U3jNbzjuFZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78c07d3faa9359c4811d32bed99c9fc9a96fe39b_2_690x287.png" alt="image" data-base62-sha1="hedHzt9Zqwv9io4H7U3jNbzjuFZ" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78c07d3faa9359c4811d32bed99c9fc9a96fe39b_2_690x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78c07d3faa9359c4811d32bed99c9fc9a96fe39b_2_1035x430.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78c07d3faa9359c4811d32bed99c9fc9a96fe39b_2_1380x574.png 2x" data-dominant-color="C1C4E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×798 43.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>The goal is to be able to detect the collision as displayed above in the Slicer scene.</strong></p>
<p>The question becomes then: are there any existing techniques, tools, libraries/classes, or extensions that could provide collision detection coverage?</p>
<p>Thank you,<br>
Hikmat</p>

---

## Post #2 by @cpinter (2020-12-02 21:56 UTC)

<p>In the SlicerRT extension there is a module that uses collision detection. The filter doing it, and which you can use for your project is <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SlicerRtCommon/vtkCollisionDetectionFilter.h">vtkCollisionDetectionFilter</a>. There was ongoing work to integrate it in VTK, but I’m not sure if it has been finished. The module using it, and which can serve as an example, is <a href="https://github.com/SlicerRt/SlicerRT/tree/master/RoomsEyeView">RoomsEyeView</a>.</p>

---

## Post #3 by @Hikmat (2021-03-19 21:03 UTC)

<p>Thank you very much for the reply and for the examples provided. Work on this project had grinded to a halt due to other competing priorities, but has emerged back to the forefront.</p>
<p>Hence, I would like to pose some follow-up questions:</p>
<ol>
<li>
<p>This is somewhat of a sanity check, but my understanding is that the <code>vtkCollisionDetectionFilter</code> is not a standalone function, i.e., given that it does not seem to be integrated into VTK, I cannot simply call it as I would for say, model creation (e.g. <code>vtk.vtkSphereSource</code>).</p>
<p>Rather, it seems to me that I will have to clone the repo referenced (<code>SlicerRT/SlicerRtCommon</code>), containing all the relevant scripts and files of the <code>vtkCollisionDetectionFilter</code>, and then source them into my project (as was done by the <code>RoomsEyeView</code> module). Is my understanding correct?</p>
</li>
<li>
<p>The scripts and functions comprising the <code>vtkCollisionDetectionFilter</code> are written in C++, as was the <code>RoomsEyeView</code> example module sourcing it, hence simplifying integration and function calls to collision detection features.</p>
<p>However, my code framework as described in my original post (i.e. consisting of widget instantiation of drop-down menus, sliders, event handling, and population of the Slicer scene with geometrical objects) is written in Python.</p>
<p>As such, this poses integration challenges as I will need to make calls to the C++ <code>vtkCollisionDetectionFilter</code> functions from my Python framework. I have looked into invoking Python bindings such as <code>ctypes</code> and <code>SWIG</code>, but such translation schemes seem somewhat intimidating to a novice like me.</p>
<p>Hence, I am wondering whether there may be a simpler solution that will allow me to leverage the <code>vtkCollisionDetectionFilter</code> functions (written in C++) into my Slicer programming development work that has been done in Python.</p>
</li>
</ol>
<p>Thank you,<br>
Hikmat</p>

---

## Post #4 by @cpinter (2021-03-22 14:31 UTC)

<ol>
<li>
<p>Yes it is part of SlicerRT currently. There have been initiatives for integrating it to VTK (see for example <a href="https://public.kitware.com/pipermail/vtk-developers/2018-May/036127.html">here</a>), but I don’t think it has been finished. You can either use SlicerRT, or you can decide to just copy this filter to your project. It would be cleaner to rely on SlicerRT (maintenance in only one place), but if you do not use anything else from there, then it is understandable if you copy these two files to your own purpose.</p>
</li>
<li>
<pre><code class="lang-auto"> import vtkSlicerRtCommonPython
 collisionDetection = vtkSlicerRtCommonPython.vtkCollisionDetectionFilter()
</code></pre>
</li>
</ol>

---

## Post #5 by @lassoan (2021-03-23 06:09 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="14854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Yes it is part of SlicerRT currently. There have been initiatives for integrating it to VTK (see for example <a href="https://public.kitware.com/pipermail/vtk-developers/2018-May/036127.html">here</a>),</p>
</blockquote>
</aside>
<p><code>vtk.vtkCollisionDetectionFilter()</code> is available in recent Slicer Preview Releases.</p>

---

## Post #6 by @cpinter (2021-03-23 10:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Good to know, thanks!</p>

---

## Post #7 by @Hikmat (2021-03-30 04:23 UTC)

<p>Thank you very much for the reply and for the guidance provided so far.</p>
<p>Indeed, the line of code <code>import vtkSlicerRtCommonPython</code> works in the Python Interactor (clean return), provided that I have the SlicerRT extension installed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f22589f11541fc91aa7c4baca90ae6f84e519f78.png" data-download-href="/uploads/short-url/yy7YpIj5zQW3GmXbbhGFVnErZFe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f22589f11541fc91aa7c4baca90ae6f84e519f78_2_690x61.png" alt="image" data-base62-sha1="yy7YpIj5zQW3GmXbbhGFVnErZFe" width="690" height="61" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f22589f11541fc91aa7c4baca90ae6f84e519f78_2_690x61.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f22589f11541fc91aa7c4baca90ae6f84e519f78_2_1035x91.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f22589f11541fc91aa7c4baca90ae6f84e519f78_2_1380x122.png 2x" data-dominant-color="FAFAFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×172 8.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I try to include this import line in my script, Slicer is not able to recognize it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e21e514cb4bfa398790170d5af0899f1b7e17f7.jpeg" data-download-href="/uploads/short-url/dqJv69oxnBe8nnIsRrVYSe0H3XV.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e21e514cb4bfa398790170d5af0899f1b7e17f7_2_690x62.jpeg" alt="error" data-base62-sha1="dqJv69oxnBe8nnIsRrVYSe0H3XV" width="690" height="62" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e21e514cb4bfa398790170d5af0899f1b7e17f7_2_690x62.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e21e514cb4bfa398790170d5af0899f1b7e17f7_2_1035x93.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e21e514cb4bfa398790170d5af0899f1b7e17f7_2_1380x124.jpeg 2x" data-dominant-color="FCF9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×174 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried modifying the import statement in my script to point it to the SlicerRT repo folder cloned in my workspace as follows: <code>from SlicerRT.SlicerRtCommon import vtkSlicerRtCommonPython</code>. Yet this gives me the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd71a22fba628ddcde53c60d5c225ec9aba4876f.png" data-download-href="/uploads/short-url/r1THrjgsqUPaLiuEwZGQeqm6dbx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd71a22fba628ddcde53c60d5c225ec9aba4876f.png" alt="image" data-base62-sha1="r1THrjgsqUPaLiuEwZGQeqm6dbx" width="690" height="61" data-dominant-color="FEF9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×172 7.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How would I be able to make this import in my script?</p>

---

## Post #8 by @cpinter (2021-03-30 09:12 UTC)

<p>As <a class="mention" href="/u/lassoan">@lassoan</a> pointed out, the filter is available in VTK, simply using <code>vtk.vtkCollisionDetectionFilter()</code>.</p>
<p>To answer your question specifically, I suspect that your module is imported before SlicerRT. Try just importing it in the function in which you use it. Also make sure that both SlicerRT and your module are added at the same time (sorry if too trivial but one can miss trivial stuff easily, I know that from experience)</p>

---

## Post #9 by @Hikmat (2021-03-31 01:14 UTC)

<p>Thank you for your continual help and guidance. Yes, I did look into <a class="mention" href="/u/lassoan">@lassoan</a>’s comment regarding the filter being available in VTK. Yet I am not sure if I understood it correctly, because it does not work when I tried running it in the Python Interactor:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc3b5012d1785145344d2eabe7fd167830676a11.png" data-download-href="/uploads/short-url/zZloM75ZauR8coogae2qdVFoPCx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc3b5012d1785145344d2eabe7fd167830676a11.png" alt="image" data-base62-sha1="zZloM75ZauR8coogae2qdVFoPCx" width="690" height="66" data-dominant-color="FCF9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×184 8.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, the comment was prefaced by this expecting to work in the latest Slicer Preview release (4.13), yet I am on the stable release version (4.11). So perhaps I will have to upgrade and install the latest Slicer Preview release version and test it out there.</p>
<p>As for the import not being picked up by my module, indeed, it most likely has to do with me not being diligent enough with trivial module management. I am not sure if I understand the comment though, regarding adding SlicerRT and my module (Neurosurgical Robotics) at the same time, but this is my current setup:</p>
<p><strong>Module Script</strong>:<br>
My imports are listed out at the top of my script as shown below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4292b57e4a07851c14a1797227863e1718929ea7.png" data-download-href="/uploads/short-url/9uVPNPjsdvuXOzsWS2qMUfzhL8P.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4292b57e4a07851c14a1797227863e1718929ea7.png" alt="image" data-base62-sha1="9uVPNPjsdvuXOzsWS2qMUfzhL8P" width="522" height="500" data-dominant-color="F6F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">891×853 40.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Module Loading Management:</strong><br>
I believe I do have it set up such that my module (CollisionDetection) is being imported after SlicerRT. If I understand correctly, this can be verified by the order in which the two modules are listed in the Application Settings → Modules window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8e6c8a76972ab5f4c276cb07895ac4ba02966c.png" data-download-href="/uploads/short-url/d3WAGRT11bQ1WPgVeo9GQ76rHgU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8e6c8a76972ab5f4c276cb07895ac4ba02966c_2_690x181.png" alt="image" data-base62-sha1="d3WAGRT11bQ1WPgVeo9GQ76rHgU" width="690" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8e6c8a76972ab5f4c276cb07895ac4ba02966c_2_690x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8e6c8a76972ab5f4c276cb07895ac4ba02966c_2_1035x271.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8e6c8a76972ab5f4c276cb07895ac4ba02966c_2_1380x362.png 2x" data-dominant-color="E9ECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×506 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In addition, my module appears to be loaded in after the SlicerRT extension:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c4086a62d697b15c8f70d9071121cf74bc337b.png" data-download-href="/uploads/short-url/kWlHY5mHmeim5zU35laO73uZR1h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c4086a62d697b15c8f70d9071121cf74bc337b_2_690x368.png" alt="image" data-base62-sha1="kWlHY5mHmeim5zU35laO73uZR1h" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c4086a62d697b15c8f70d9071121cf74bc337b_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c4086a62d697b15c8f70d9071121cf74bc337b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c4086a62d697b15c8f70d9071121cf74bc337b.png 2x" data-dominant-color="E2E3EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×511 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Module Directory Workspace</strong><br>
I have my directory workspace structured as follows: my module script <code>CollisionDetectionFramework.py</code> is contained in the folder <code>collisionDetection</code>, with the SlicerRT project cloned and located in the same folder, such that import accesses to the SlicerRT module can be made:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688dcc5412947c04c7bead043b3d3b732071d577.png" data-download-href="/uploads/short-url/eUVsoQZOWlp2M1anDx1JufxNrqn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688dcc5412947c04c7bead043b3d3b732071d577_2_690x199.png" alt="image" data-base62-sha1="eUVsoQZOWlp2M1anDx1JufxNrqn" width="690" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688dcc5412947c04c7bead043b3d3b732071d577_2_690x199.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/688dcc5412947c04c7bead043b3d3b732071d577_2_1035x298.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688dcc5412947c04c7bead043b3d3b732071d577.png 2x" data-dominant-color="F6F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1062×307 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hopefully this is enough information for you to be able to diagnose the issue here. Thank you.</p>

---

## Post #10 by @cpinter (2021-03-31 09:51 UTC)

<p>Yes, definitely use the latest version please.</p>
<p>The line <code>import SlicerRT.SlicerRtCommon import vtkSlicerRtCommonPython</code> won’t work. See my above comments about why.</p>

---

## Post #11 by @Hikmat (2021-04-01 04:32 UTC)

<p>Thank you so much for the help and guidance so far. I am now able to access the VTK collision detection filter through my module script as well as make function calls to it!</p>
<p>Currently; however, I am trying to figure out the set of function calls I will need to make through the filter to detect collisions between my simplistic VTK model objects.</p>
<p>I have studied the code in the RoomsEyeView module to get a sense of the function calls needed to set up collision detection. My understanding is summarized as follows:</p>
<ol>
<li>Instantiate the VTK collision detection filter</li>
<li>Define the models to be passed in as inputs</li>
<li><strong>Set the transforms required</strong></li>
<li>Return the number of contacts detected</li>
</ol>
<p>Step 3 is where my understanding of the code is weak, given that the SlicerRT environment is much more complicated than mine, with many different models and reference systems. My module is populated with only a sphere and a rod for simulation purposes, and I am not quite sure what transforms I would need to specify or create.</p>
<p>The code block below is what I have tried so far (ignoring the need for setting transforms), and the function call to <code>GetNumberOfContacts()</code> causes Slicer 4.13 to crash:</p>
<blockquote>
<p><code>collisionDetection = vtk.vtkCollisionDetectionFilter()</code><br>
<code>input1 = slicer.mrmlScene.GetFirstNodeByName("Input Model 1")</code><br>
<code>input2 = slicer.mrmlScene.GetFirstNodeByName("Input Model 2")</code><br>
<code>collisionDetection.SetInputData(0, input1.GetPolyData())</code><br>
<code>collisionDetection.SetInputData(1, input2.GetPolyData())</code><br>
<code>numContacts = collisionDetection.GetNumberOfContacts()</code></p>
</blockquote>
<p>My assumption is that this code crashes on me because I have not set the transforms required through <code>collisionDetection.SetTransform()</code>, since I do not understand what parameters I would need to pass in or what this function call is doing.</p>
<p>The SlicerRT example seems to set the transforms required by making calls to <code>SlicerIECTransformLogic</code> and calling <code>GetTransformNodeBetween()</code> between the object model of interest and the reference frame RAS. My understanding here is weak though, since I can’t see why this is necessary or what transforms would be needed.</p>
<p>Hence, my follow-up questions are the following:</p>
<ol>
<li>What transforms would I need to set/pass in to the collision filter (and presumably create beforehand)?</li>
<li>The <code>SlicerIECTransformLogic</code> routines are a bit intimidating since I don’t fully understand what’s going on. How could I go about creating these transforms or getting the necessary transforms between two frames in a simpler manner?</li>
</ol>

---

## Post #12 by @Mik (2021-04-02 13:28 UTC)

<aside class="quote no-group" data-username="Hikmat" data-post="11" data-topic="14854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>What transforms would I need to set/pass in to the collision filter (and presumably create beforehand)?</p>
</blockquote>
</aside>
<p>There are many examples on <a href="https://kitware.github.io/vtk-examples/site/Python/Visualization/CollisionDetection/" rel="noopener nofollow ugc">VTK site</a>. The collision example has two spheres: sphere0 is moving and it has a transform0 as a transformation data, sphere1 is stationary and it has simple identity matrix.</p>

---

## Post #13 by @Hikmat (2021-04-06 02:57 UTC)

<p>Thank you very much for the reply and for the example provided. My case is similar, in that I have a sphere and a cube in the Slicer scene, but they are stationary VTK objects. They can; however, be translated by the user and moved around the scene.</p>
<p>I have tried following the example in how the transforms were set, but I still have Slicer 4.13 crashing on me upon the <code>GetNumberOfContacts()</code> function call.</p>
<p>This is what my code looks like so far:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed54b46dff3e889a34b574454766522a6ddeafb5.png" data-download-href="/uploads/short-url/xRwDF0BIrnMPznZDPmvWzg6JPKd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed54b46dff3e889a34b574454766522a6ddeafb5.png" alt="image" data-base62-sha1="xRwDF0BIrnMPznZDPmvWzg6JPKd" width="517" height="166" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">907×292 7.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The transforms <code>transform0</code> and <code>transform1</code> are initialized using <code>vtkTransform()</code> and are initially set to the centers of the VTK objects using <code>vtkTransform.Translate()</code>. As the user moves the objects around, I update the transforms for each object using <code>vtkTransform.Translate()</code> to have the transforms fixed to the center of the objects.</p>
<p>I tried printing the output of the collision filter using the <code>GetOutput()</code> call for one of my VTK objects, and this is the debug trace I get:</p>
<blockquote>
<p>vtkPolyData (000001E17CFD33F0)<br>
Debug: Off<br>
Modified Time: 418414<br>
Reference Count: 2<br>
Registered Events: (none)<br>
Information: 000001E1569BECA0<br>
Data Released: False<br>
Global Release Data: Off<br>
UpdateTime: 0<br>
Field Data:<br>
Debug: Off<br>
Modified Time: 418411<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Number Of Arrays: 0<br>
Number Of Components: 0<br>
Number Of Tuples: 0<br>
Number Of Points: 0<br>
Number Of Cells: 0<br>
Cell Data:<br>
Debug: Off<br>
Modified Time: 418414<br>
Reference Count: 1<br>
Registered Events:<br>
Registered Observers:<br>
vtkObserver (000001E15699F7D0)<br>
Event: 33<br>
EventName: ModifiedEvent<br>
Command: 000001E1569BEAC0<br>
Priority: 0<br>
Tag: 1<br>
Number Of Arrays: 0<br>
Number Of Components: 0<br>
Number Of Tuples: 0<br>
Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 1 1 1 )<br>
Interpolate Flags: ( 1 1 1 1 1 0 0 1 1 1 1 )<br>
Pass Through Flags: ( 1 1 1 1 1 1 1 1 1 1 1 )<br>
Scalars: (none)<br>
Vectors: (none)<br>
Normals: (none)<br>
TCoords: (none)<br>
Tensors: (none)<br>
GlobalIds: (none)<br>
PedigreeIds: (none)<br>
EdgeFlag: (none)<br>
Tangents: (none)<br>
RationalWeights: (none)<br>
HigherOrderDegrees: (none)<br>
Point Data:<br>
Debug: Off<br>
Modified Time: 418413<br>
Reference Count: 1<br>
Registered Events:<br>
Registered Observers:<br>
vtkObserver (000001E15699F710)<br>
Event: 33<br>
EventName: ModifiedEvent<br>
Command: 000001E1569BEAC0<br>
Priority: 0<br>
Tag: 1<br>
Number Of Arrays: 0<br>
Number Of Components: 0<br>
Number Of Tuples: 0<br>
Copy Tuple Flags: ( 1 1 1 1 1 0 1 1 1 1 1 )<br>
Interpolate Flags: ( 1 1 1 1 1 0 0 1 1 1 1 )<br>
Pass Through Flags: ( 1 1 1 1 1 1 1 1 1 1 1 )<br>
Scalars: (none)<br>
Vectors: (none)<br>
Normals: (none)<br>
TCoords: (none)<br>
Tensors: (none)<br>
GlobalIds: (none)<br>
PedigreeIds: (none)<br>
EdgeFlag: (none)<br>
Tangents: (none)<br>
RationalWeights: (none)<br>
HigherOrderDegrees: (none)<br>
Bounds:<br>
Xmin,Xmax: (1, -1)<br>
Ymin,Ymax: (1, -1)<br>
Zmin,Zmax: (1, -1)<br>
Compute Time: 0<br>
Editable: false<br>
Number Of Points: 0<br>
Point Coordinates: 0000000000000000<br>
PointLocator: 0000000000000000<br>
CellLocator: 0000000000000000<br>
Number Of Vertices: 0<br>
Number Of Lines: 0<br>
Number Of Polygons: 0<br>
Number Of Triangle Strips: 0<br>
Number Of Pieces: 1<br>
Piece: -1<br>
Ghost Level: 0</p>
</blockquote>
<p>Interestingly, it seems that all the values are ‘‘null’’, i.e. no geometrical properties of the VTK object seem to be captured or processed, with most values found to be 0.</p>
<p>I would appreciate any debugging help or insight into this matter. Thank you.</p>

---

## Post #14 by @Mik (2021-04-06 04:43 UTC)

<p>Do you update transforms and collision filter before calling GetNumberOfContacts method?</p>

---

## Post #15 by @Hikmat (2021-04-06 17:59 UTC)

<p>Yes, I do. The transforms are updated as the objects are moved around and upon the click of the ‘‘Detect Collision’’ button below, I then call <code>onCollisionDetection()</code> shown above. This then updates the collision filter before calling the <code>GetNumberOfContacts</code> method.</p>
<p>This is what my setup looks like, if it helps:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9bd8b0213bb541ddf805857ec3c959309847ae1.png" data-download-href="/uploads/short-url/sMG442aEIBVDF6pmsclIYvFPiPD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9bd8b0213bb541ddf805857ec3c959309847ae1_2_690x289.png" alt="image" data-base62-sha1="sMG442aEIBVDF6pmsclIYvFPiPD" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9bd8b0213bb541ddf805857ec3c959309847ae1_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9bd8b0213bb541ddf805857ec3c959309847ae1_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9bd8b0213bb541ddf805857ec3c959309847ae1_2_1380x578.png 2x" data-dominant-color="C5C7E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×805 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @Mik (2021-04-06 19:14 UTC)

<p>Did you try to run the VTK example? My suggestion is reproduce step-by-step the VTK example in your code and find what part doesn’t work.</p>
<p>For example part of the test algorithm for <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Beams/Logic/vtkSlicerMLCPositionLogic.cxx#L1013-L1132" rel="noopener nofollow ugc">MLC position</a> calculation that uses collision detection.</p>

---

## Post #17 by @Hikmat (2021-04-09 06:24 UTC)

<p>Thank you for the suggestion, I was able to reproduce the VTK example step-by-step in my Slicer environment and it indeed worked.</p>
<p>My scenario is a little different than the VTK example; however, in the sense that the user can move the objects around in the Slicer scene. In contrast, the VTK example has the objects a fixed distance apart and then proceeds to move one of the objects in a predetermined manner.</p>
<p>The MLC position example code was very helpful in revealing a step that I was missing, which was updating the collision filter through the <code>Update()</code> method.</p>
<p>With this fix, Slicer no longer crashes on me when I call <code>GetNumberOfContacts()</code>, but it is not reporting a collision between the objects, i.e. <code>GetNumberOfContacts()</code> returns 0 even though I have the objects oriented in a collision.</p>
<p>I suspect it has to do with the way I am setting my transforms, i.e. I am simply translating each transform to the center of its respective object using <code>Translate()</code>, and that may be inadequate for the purposes of passing it through the collision filter.</p>
<p>This is what my code look like so far, I would greatly appreciate some debug help:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d187a4ee8dee8d785854bb620435863e78ae450.png" data-download-href="/uploads/short-url/1RQEktHDOdFC8hhkcrW0Bhe2VqM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d187a4ee8dee8d785854bb620435863e78ae450.png" alt="image" data-base62-sha1="1RQEktHDOdFC8hhkcrW0Bhe2VqM" width="690" height="162" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1664×392 10.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @Mik (2021-04-09 08:32 UTC)

<aside class="quote no-group" data-username="Hikmat" data-post="17" data-topic="14854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>I suspect it has to do with the way I am setting my transforms, i.e. I am simply translating each transform to the center of its respective object using <code>Translate()</code> , and that may be inadequate for the purposes of passing it through the collision filter.</p>
</blockquote>
</aside>
<p>I think you right. You can try to make a gap between your objects, and then use loop to change transform position of one object until it collides with another one. On each iteration of the loop you must update the transform and the collision filter and check number of contacts.</p>

---

## Post #19 by @lassoan (2021-04-19 13:08 UTC)

<p>If you call <code>GetPolyData()</code> or <code>GetMesh()</code> on a model node then it returns the mesh in the node’s local coordinate system, not transformed into the world coordinate system.</p>
<p>If you only apply linear transforms to your model nodes then you can retrieve that transform from the parent transform node of each model node and set that in the collision detection filter. This way collision detection is performed on the exact same arrangement that you see in the viewers.</p>

---

## Post #20 by @Hikmat (2021-05-08 18:30 UTC)

<p>Thank you for your feedback and suggestion!</p>
<p>Yes, this is the crux of the problem, in that I do not know how to extract the transforms from the model nodes so that I can pass them into the collision detection filter.</p>
<p>My application has model nodes being translated across the screen by the user, with the X, Y, and Z center coordinates updated accordingly using <code>SetCenter()</code>. How then would I be able to extract the resultant translations or the respective transforms associated with each model node?</p>
<p>The examples that I were provided with on the <a href="https://kitware.github.io/vtk-examples/site/Python/Visualization/CollisionDetection/" rel="noopener nofollow ugc">VTK site</a> and which I tried to follow consisted of initializing transforms, and then updating these transforms according to the translations, and then passing them through the filter. Yet there was a disconnect to me in how these transforms were related to or enforceable on the model nodes.</p>
<p>Therefore, what I need help in is figuring out what transforms to pass into the collision filter and how I can go about extracting them. Thank you!</p>

---

## Post #21 by @lassoan (2021-05-08 22:19 UTC)

<aside class="quote no-group" data-username="Hikmat" data-post="20" data-topic="14854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>Yes, this is the crux of the problem, in that I do not know how to extract the transforms from the model nodes so that I can pass them into the collision detection filter.</p>
</blockquote>
</aside>
<p>You can get transform using <code>transformNode.GetMatrixTransformToParent(transformMatrix)</code>. See many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Slicer script repository</a>.</p>

---

## Post #22 by @ferhue (2021-09-01 11:02 UTC)

<aside class="quote no-group" data-username="Hikmat" data-post="13" data-topic="14854">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ecccb3/48.png" class="avatar"> Hikmat:</div>
<blockquote>
<p>I have tried following the example in how the transforms were set, but I still have Slicer 4.13 crashing on me upon the <code>GetNumberOfContacts()</code> function call.</p>
</blockquote>
</aside>
<p>I experienced the same crash recently. I have filed a bug report:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/issues/18298">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18298" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>

  <article class="onebox-body">
    <img width="64" height="64" src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18298" target="_blank" rel="noopener nofollow ugc">vtkCollisionDetectionFilter segfault (#18298) · Issues · VTK / VTK · GitLab</a></h3>

  <p>When running this script in Python, I get a segmentation fault (core dumped)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/SlicerRT/issues/195">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/issues/195" target="_blank" rel="noopener nofollow ugc">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/195" target="_blank" rel="noopener nofollow ugc">vtkCollisionDetectionFilter out of sync with VTK</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-01" data-time="10:48:58" data-timezone="UTC">10:48AM - 01 Sep 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-09-01" data-time="18:38:19" data-timezone="UTC">06:38PM - 01 Sep 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/ferdymercury" target="_blank" rel="noopener nofollow ugc">
          <img alt="ferdymercury" src="https://avatars.githubusercontent.com/u/10653970?v=4" class="onebox-avatar-inline" width="20" height="20">
          ferdymercury
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">SlicerRT has an outdated vtkCollisionDetectionFilter class, that is now natively<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> part of VTK. It would be nice to migrate it to VTK to get also the latest bug fixes and reduce maintenance effort here in SlicerRT. See e.g. https://gitlab.kitware.com/vtk/vtk/-/issues/18298
Thanks!</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
