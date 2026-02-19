---
topic_id: 27717
title: "Slicercustomapptemplate Build Error"
date: 2023-02-09
url: https://discourse.slicer.org/t/27717
---

# SlicerCustomAppTemplate Build Error

**Topic ID**: 27717
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/slicercustomapptemplate-build-error/27717

---

## Post #1 by @Kaubert (2023-02-09 09:18 UTC)

<p>Hi there,</p>
<p>I am having trouble building SlicerCustomAppTemplate while I am not encountering any errors when building the <a href="https://github.com/Slicer/Slicer" rel="noopener nofollow ugc">latest version of Slicer</a>.</p>
<p>Here is my configuration:</p>
<p>Windows 11<br>
Cmake 3.22.4<br>
Qt 5.15.2<br>
Visual Studio 2022</p>
<p>As defined <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">here</a>, I downloaded the source folder of SlicerCustomAppTemplate via :<br>
<em>pip install cookiecutter jinja2-github</em><br>
<em>cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate</em></p>
<p>Here I do not change anything in the source folder.</p>
<p>To build I am following steps mentioned <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#configure-and-build-slicer" rel="noopener nofollow ugc">Here</a>.</p>
<p>Build error indicates inability to open ‘vtkSlicerSceneViewsModuleLogic.lib’</p>
<p>The Configuration, Generation and Build log files could be find <a href="https://isitwin2022-my.sharepoint.com/:f:/g/personal/kevin_aubert_isitwin_com/EjbbUg0E4z9Pl9gv6IFMhzEBt8PHIYvTQSPXRx3OuRDCaA?e=BV9zvv" rel="noopener nofollow ugc">Here</a>  as well as errors from Visual Studio.</p>
<p>Can you please help me to solve this error ?<br>
Thank you</p>

---

## Post #2 by @lassoan (2023-02-15 06:19 UTC)

<p>Have a look at the first error. All the other may be consequences of the first one.</p>
<p>As I see, this is the first error:</p>
<pre><code class="lang-auto">14&gt;  Syntax error in cmake code at
14&gt;
14&gt;    C:/D/S5D/slicersources-build/CTKAppLauncherLib-prefix/tmp/CTKAppLauncherLib-cache-Debug.cmake:19
14&gt;
14&gt;  when parsing string
14&gt;
14&gt;    C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5
14&gt;
14&gt;  Invalid escape sequence \Q
</code></pre>
<p>It means that somewhere you specified Qt path using Windows separators () instead of cross-platform separators (/). The backslash was interpreted somewhere as escape character, which caused the build error.</p>
<p>Try using <code>C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5</code> as Qt path.</p>

---

## Post #3 by @Kaubert (2023-02-15 12:54 UTC)

<p>Dear Lassoan,</p>
<p>Thank you for your response !<br>
I’m now able to build SlicerCAT in 5.2.1 version without errors.</p>
<p>Best regards,<br>
Kevin</p>

---

## Post #6 by @jcfr (2023-02-22 14:14 UTC)

<aside class="quote no-group" data-username="Kaubert" data-post="1" data-topic="27717">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kaubert/48/18283_2.png" class="avatar"> Kaubert:</div>
<blockquote>
<p>Build error indicates inability to open ‘vtkSlicerSceneViewsModuleLogic.lib’</p>
</blockquote>
</aside>
<p>This was tentatively addressed in <a href="https://github.com/Slicer/Slicer/commit/d4723511cc7d19d8ed1f447a13f749a18e317baf">Slicer@d4723511c</a> integrated through <a href="https://github.com/Slicer/Slicer/pull/6790">PR-6790</a>, as we are also experiencing a similar error in a custom application when doing a clean build, I am looking into this.</p>

---

## Post #7 by @jcfr (2023-02-23 04:48 UTC)

<p>This should be fixed in <a href="https://github.com/Slicer/Slicer/pull/6834">PR-6834</a> that will be integrated shortly.</p>

---
