---
topic_id: 24720
title: "App Quit While Operating On Big Volume"
date: 2022-08-11
url: https://discourse.slicer.org/t/24720
---

# App quit while operating on big volume

**Topic ID**: 24720
**Date**: 2022-08-11
**URL**: https://discourse.slicer.org/t/app-quit-while-operating-on-big-volume/24720

---

## Post #1 by @allenzhuang975 (2022-08-11 20:12 UTC)

<p>Problem report for Slicer 5.0.3 win-amd64: [please describe expected and actual behavior]</p>
<p>Volume was about 674 x 674 x 1974. When I rotating the volumes in the cener windows, the app crushed, and every time. It takes up about 5G memory.</p>
<p>[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2022-08-11 11:50:35<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.0.3 (revision 30893 / 7ea0f43) win-amd64 - installed release<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 19044, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 20362 MB physical, 30362 MB virtual<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: E:/Users/admin/AppData/Local/NA-MIC/Slicer 5.0.3/bin<br>
[DEBUG][Qt] 11.08.2022 11:50:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 11.08.2022 11:50:37 [Python] (E:\Users\admin\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 11.08.2022 11:50:37 [Python] (E:\Users\admin\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 11.08.2022 11:50:37 [Python] (E:\Users\admin\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 11.08.2022 11:50:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #2 by @lassoan (2022-08-11 20:17 UTC)

<p>If the application crashed while rotating a volume rendered image in the 3D view then it means that your GPU took too long time to render an image (caused a TDR error) and so Windows terminated the application. You have many options to resolve the issue as described in this post:</p>
<aside class="quote quote-modified" data-post="7" data-topic="17032">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/enabling-volume-rendering-for-a-large-volume-makes-the-application-crash/17032/7">Enabling volume rendering for a large volume makes the application crash</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This indicates that you get a TDR error: the operating system shuts down applications that keep the graphics card busy for too long. This happens because the size of the volume is too large for your GPU to comfortably handle. There are several ways to work around this: 

Option A: Run the code snippet above to split the volume to smaller chunks (that way you have a better chance that the graphics card will not be unresponsive for too long) or increase TDR delay in the registry.
Option B: Crop a…
  </blockquote>
</aside>


---

## Post #3 by @allenzhuang975 (2022-08-12 03:12 UTC)

<aside class="quote no-group" data-username="Enabling volume rendering for a large volume makes the application crash" data-post="7" data-topic="17032">
<div class="title">
<div class="quote-controls"></div>
<a href="https://discourse.slicer.org/t/enabling-volume-rendering-for-a-large-volume-makes-the-application-crash/17032/7">Enabling volume rendering for a large volume makes the application crash</a></div>
<blockquote>
<p>TDR delay</p>
</blockquote>
</aside>
<p>Thank you for your reply. After I have done the following, it seems to work.</p>
<ol>
<li>
<p>Set DWORD value 0x10 named TdrDelay at path : HKLM\System\CurrentControlSet\Control\GraphicsDriver\</p>
</li>
<li>
<p>Restarted Windows 10,</p>
</li>
</ol>

---
