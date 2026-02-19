---
topic_id: 1582
title: "Trying To Run Test From Loadable Module Outside Of Slicer So"
date: 2017-12-03
url: https://discourse.slicer.org/t/1582
---

# Trying to run test from loadable module (outside of Slicer source tree)

**Topic ID**: 1582
**Date**: 2017-12-03
**URL**: https://discourse.slicer.org/t/trying-to-run-test-from-loadable-module-outside-of-slicer-source-tree/1582

---

## Post #1 by @SolidusAbi (2017-12-03 19:53 UTC)

<p>Hi everyone,</p>
<p>I’m trying to develop a loadable module outside of Slicer source tree using a configuration based on the wiki tutorial. I have gotten to import the module and compile in QtCreator but I have a problem running the test.</p>
<p>In the first time, when I run the test, it tries to call to ‘<a href="http://slicerqt.py" rel="nofollow noopener">slicerqt.py</a>’ in the module bin directory instead of in the Slicer directory. I created a LauncheSettings.ini based in the Slicer’s launcher settings file but It does not look for in the correct directory although I created the SLICER_HOME variable. Anyway, I created that variable in QtCreator’s enviroment and It works but during the execution console throws multiple errors about import python command.</p>
<p><strong>Here i let you the first lines from Console:</strong><br>
Traceback (most recent call last):<br>
File “”, line 7, in <br>
File “/home/abian/Datos/Slicer/Slicer-Build-Debug/Slicer-build/bin/Python/slicer/slicerqt.py”, line 4, in <br>
import ctk<br>
ImportError: No module named ctk<br>
Traceback (most recent call last):<br>
File “”, line 7, in <br>
File “/home/abian/Datos/Slicer/Slicer-Build-Debug/Slicer-build/bin/Python/slicer/slicerqt-with-tcl.py”, line 42, in <br>
slicer.sliceWidgets = {}<br>
NameError: name ‘slicer’ is not defined<br>
ImportError: No module named slicer</p>
<p>I don’t sure where is the problem but I’m trying to run the generic test that ExtensionWizard script created. If someone can help me, I will be grateful.</p>
<p>I’m working on Ubuntu 16.04, Slicer 4.9 compiled with Qt 5.9.2 and GCC 5.4. If you need it, the QtCreator version is 4.4.1.</p>
<p>Thanks!!!</p>

---

## Post #2 by @pieper (2017-12-05 00:34 UTC)

<p>Looks like ctk didn’t build or wasn’t found at startup.</p>
<p>Best thing would be to get the standard build of Slicer working and then introduce your loadable module using the --additional-module-paths command line option or by setting the module preferences.</p>
<p>You shouldn’t ever need to set SLICER_HOME directly (always use <a href="https://github.com/commontk/AppLauncher">the launcher</a> instead).</p>
<p>HTH</p>

---

## Post #3 by @SolidusAbi (2017-12-06 16:58 UTC)

<p>Thanks for your answer. The  --additional-module-paths command line works perfectly but my idea was not to use the standard build in order to avoid to load every modules, maybe i need to debug my module and the waiting for slicer to start could be annoying.</p>
<p>I was debugging slicer to understand the launcher setting and to check if it is selecting the correct file. I saw that SLICER_HOME variable is changed by my LauncherSetting.ini value but he ignored it and it still looking for in the wrong directory.</p>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
IOError: [Errno 2] No such file or directory: '/mnt/Aux/Slicer/Extensions/MyExtension-Build-Debug/bin/Python/slicer/slicerqt.py'
Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
IOError: [Errno 2] No such file or directory: '/mnt/Aux/Slicer/Extensions/MyExtension-Build-Debug/bin/Python/slicer/slicerqt-with-tcl.py
</code></pre>
<p>I attached captures of my LauncherSetting.ini: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3464a4f64908044818c25078c356bf598b7f85d.png" data-download-href="/uploads/short-url/u91lev4Toqmn7eVDOU8qN2oOmBv.png?dl=1" title="Screenshot_20171206_164825" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3464a4f64908044818c25078c356bf598b7f85d_2_690x445.png" alt="Screenshot_20171206_164825" data-base62-sha1="u91lev4Toqmn7eVDOU8qN2oOmBv" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3464a4f64908044818c25078c356bf598b7f85d_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3464a4f64908044818c25078c356bf598b7f85d_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3464a4f64908044818c25078c356bf598b7f85d_2_1380x890.png 2x" data-dominant-color="FBF6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20171206_164825</span><span class="informations">1423×919 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Anyway, i can work with the --additional-module-paths command line but i want to know why i cant use the generic test generated by the ExtensionWIzard.</p>

---

## Post #4 by @lassoan (2017-12-06 20:02 UTC)

<aside class="quote no-group" data-username="SolidusAbi" data-post="3" data-topic="1582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/solidusabi/48/585_2.png" class="avatar"> SolidusAbi:</div>
<blockquote>
<p>waiting for slicer to start could be annoying.</p>
</blockquote>
</aside>
<p>Slicer startup time should be under 10 seconds, but if that’s too much then when you build Slicer you can specify a list of modules to exclude from build.</p>

---

## Post #5 by @pieper (2017-12-07 13:06 UTC)

<aside class="quote no-group" data-username="SolidusAbi" data-post="3" data-topic="1582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/solidusabi/48/585_2.png" class="avatar"> SolidusAbi:</div>
<blockquote>
<p>i cant use the generic test generated by the ExtensionWIzard.</p>
</blockquote>
</aside>
<p>Maybe something needs to be fixed - if you start with a standard build and create a loadable extension with the wizard you should be able to run the tests.</p>

---

## Post #6 by @SolidusAbi (2017-12-07 16:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="1582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer startup time should be under 10 seconds</p>
</blockquote>
</aside>
<p>Hi Andras,</p>
<p>In my case, i want to use volumes from Slicer and I am debugging in order to understand better the Slicer architecture and how works the volumes module. In debug, Slicer startup time take a little bit more time.</p>
<p>Anyway, I could take a build excluding modules that I will not use. Thanks for your answer.</p>

---

## Post #7 by @SolidusAbi (2017-12-07 16:05 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="1582">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Maybe something needs to be fixed - if you start with a standard build and create a loadable extension with the wizard you should be able to run the tests.</p>
</blockquote>
</aside>
<p>I will try to use the extension inside of Slicer source tree… Maybe my problem is due to the configuration of my extension outside of the slicer.</p>

---
