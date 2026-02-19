---
topic_id: 4913
title: "Custom Application Does Not Open Module At Startup"
date: 2018-11-29
url: https://discourse.slicer.org/t/4913
---

# Custom application does not open module at startup

**Topic ID**: 4913
**Date**: 2018-11-29
**URL**: https://discourse.slicer.org/t/custom-application-does-not-open-module-at-startup/4913

---

## Post #1 by @mschumaker (2018-11-29 23:40 UTC)

<p>I’ve compiled a custom application using the most recent Slicer commit on MacOS. In my superbuild CMakeList.txt file, I specify a default home module, currently set to Welcome:</p>
<blockquote>
<p>set(Slicer_DEFAULT_HOME_MODULE “Welcome”)</p>
</blockquote>
<p>When I run the application, both from the command line and after packaging, no module is opened at startup. Is this the expected behaviour? Is there somewhere else I need to set the module that should be opened at startup?</p>

---

## Post #2 by @cpinter (2018-11-30 00:03 UTC)

<p>Based on what I know it should work as you expect it to work. However, usually we don’t specify this in a CMakeLists.txt file, but we use this at the time of CMake configuration. So this would be a cmake argument like this</p>
<pre><code>-DSlicer_DEFAULT_HOME_MODULE:STRING="Welcome"</code></pre>

---

## Post #3 by @lassoan (2018-11-30 00:30 UTC)

<p>I can confirm, too, that <code>set(Slicer_DEFAULT_HOME_MODULE “Welcome”)</code> works. You would include it in the top-level CMakeLists.txt file if you use the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="nofollow noopener">custom application template</a>. Note that the in the custom application template, “Welcome” module is disabled, so you either need to remove it from the disabled list or choose another home module.</p>

---

## Post #4 by @mschumaker (2018-11-30 16:36 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="4913" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Based on what I know it should work as you expect it to work. However, usually we don’t specify this in a CMakeLists.txt file, but we use this at the time of CMake configuration. So this would be a cmake argument like this</p>
<pre><code class="lang-auto">-DSlicer_DEFAULT_HOME_MODULE:STRING="Welcome"
</code></pre>
</blockquote>
</aside>
<p>Thanks, I tested setting it in the GUI instead. Though I guess that won’t do much good if my CMakeLists sets the module to be disabled!</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="4913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I can confirm, too, that <code>set(Slicer_DEFAULT_HOME_MODULE “Welcome”)</code> works. You would include it in the top-level CMakeLists.txt file if you use the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">custom application template</a>. Note that the in the custom application template, “Welcome” module is disabled, so you either need to remove it from the disabled list or choose another home module.</p>
</blockquote>
</aside>
<p>Thank you. I’m trying a clean build now, with Data as the default module.</p>

---

## Post #5 by @mschumaker (2018-11-30 17:09 UTC)

<p>Another thing to note is that I’m hiding all of the toolbars in my custom application qAppMainWindow.cxx setupUi method:</p>
<blockquote>
<p>// Hide the toolbars<br>
this-&gt;MainToolBar-&gt;setVisible(false);<br>
this-&gt;ModuleSelectorToolBar-&gt;setVisible(false);<br>
this-&gt;ModuleToolBar-&gt;setVisible(false);<br>
this-&gt;ViewToolBar-&gt;setVisible(false);<br>
this-&gt;MouseModeToolBar-&gt;setVisible(false);<br>
this-&gt;CaptureToolBar-&gt;setVisible(false);<br>
this-&gt;ViewersToolBar-&gt;setVisible(false);<br>
this-&gt;DialogToolBar-&gt;setVisible(false);</p>
</blockquote>
<p>Does this interfere with the creation of the qSlicerModuleManager?</p>

---

## Post #6 by @cpinter (2018-11-30 17:11 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="4" data-topic="4913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Though I guess that won’t do much good if my CMakeLists sets the module to be disabled!</p>
</blockquote>
</aside>
<p>Right, I missed the part that this is for a custom application. My bad…</p>

---

## Post #7 by @mschumaker (2018-11-30 17:14 UTC)

<p>No problem! I’ll see how this build goes once it’s done.</p>

---

## Post #8 by @jcfr (2018-11-30 18:22 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="5" data-topic="4913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Does this interfere with the creation of the qSlicerModuleManager?</p>
</blockquote>
</aside>
<p>No</p>
<aside class="quote no-group" data-username="mschumaker" data-post="1" data-topic="4913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>specify a default home module, currently set to Welcome</p>
</blockquote>
</aside>
<p>The default for custom application is expected to be “Home”. See <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/e8afb986dd07f47e6dfea2437723ec2b3b8ded43/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt#L42" class="inline-onebox">SlicerCustomAppTemplate/{{cookiecutter.project_name}}/CMakeLists.txt at e8afb986dd07f47e6dfea2437723ec2b3b8ded43 · KitwareMedical/SlicerCustomAppTemplate · GitHub</a></p>
<p>Changing the value in the <code>CMakeLists.txt</code> and re-configuring and re-building the project from the top-level will have the expected effect.<br>
Configuring the project passing <code>Slicer_DEFAULT_HOME_MODULE</code> option is also expected to change the value.</p>
<p>Ultimately the value is configured into the header <code>Slicer/CMake/vtkSlicerConfigure.h.in</code></p>

---

## Post #9 by @mschumaker (2018-11-30 18:58 UTC)

<p>Thank you - I can see where it should be set on line 14 of vtkSlicerConfigure.h.in, and the correct value appears in Slicer-build/vtkSlicerConfigure.h:</p>
<blockquote>
<p><span class="hashtag-raw">#define</span> Slicer_DEFAULT_HOME_MODULE “Data”</p>
</blockquote>
<p>However, I’ve tried building the full Superbuild again, and when I run the executable, it starts with a blank module panel.</p>
<p>The error log doesn’t have much in it:</p>
<blockquote>
<p>Debug, Python<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics</p>
</blockquote>
<blockquote>
<p>Warning, Qt<br>
libpng warning: iCCP: known incorrect sRGB profile</p>
</blockquote>
<blockquote>
<p>Debug, Qt<br>
Session start time …: 2018-11-30 13:49:09<br>
Slicer version …: 4.11.0-2018-11-14 (revision 60adeea) macosx-amd64 - not installed release<br>
PADPlanner2 version …: 1.2.0-2018-11-29 (revision 25c786a)<br>
Operating system …: Mac OS X / 10.12.6 / 16G1618 - 64-bit<br>
Memory …: 16384 MB physical, 1024 MB virtual<br>
CPU …: GenuineIntel Intel(R) Core™ i7-6567U CPU @ 3.30GHz, 2 cores, 4 logical processors<br>
VTK configuration …: OpenGL2 rendering, Sequential threading<br>
Developer mode enabled …: no<br>
Prefer executable CLI …: yes<br>
Additional module paths …: (none)</p>
</blockquote>
<p>What could be causing this?</p>

---

## Post #10 by @lassoan (2018-11-30 19:25 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="9" data-topic="4913">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>What could be causing this</p>
</blockquote>
</aside>
<p>In CMakeLists.txt files you only modify the default .ini file content. Delete the current .ini file if you want the application to start from default settings.</p>

---

## Post #11 by @mschumaker (2018-11-30 19:32 UTC)

<p>Ok. Which .ini file?</p>

---

## Post #12 by @lassoan (2018-11-30 19:43 UTC)

<p><em>customapplicationname</em>.ini</p>

---

## Post #15 by @lassoan (2018-11-30 20:14 UTC)

<p>Rebuilding anything will not have any effect. Application setting .ini is stored in the user’s profile:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Settings_file_location" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Settings_file_location</a></p>

---

## Post #16 by @mschumaker (2018-11-30 20:36 UTC)

<p>Ok, sorry, I didn’t know. I’ll delete those and try again.<br>
Thanks!</p>

---

## Post #17 by @mschumaker (2018-11-30 21:16 UTC)

<p>Excellent! Thank you. That solved it.</p>

---
