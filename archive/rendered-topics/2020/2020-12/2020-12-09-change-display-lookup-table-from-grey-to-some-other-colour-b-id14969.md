---
topic_id: 14969
title: "Change Display Lookup Table From Grey To Some Other Colour B"
date: 2020-12-09
url: https://discourse.slicer.org/t/14969
---

# Change Display Lookup Table from Grey to Some Other Colour by Default

**Topic ID**: 14969
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/change-display-lookup-table-from-grey-to-some-other-colour-by-default/14969

---

## Post #1 by @Jonathan_Lesage (2020-12-09 19:24 UTC)

<p>Hi There,</p>
<p>I need to use a specific colour map to view data meaning that whenever I open 3d Slicer I have to first go and change the Lookup Table from the default Grey to a colour table I’ve added called NDT. This isn’t a problem but adds some amount of time each time I load a new volume. For my purposes I will use this NDT colourmap 99% of the time and so it would be great to simply have it be the colourmap in the Lookup Table by default (like Grey is now).</p>
<p>Any chance this is possible?</p>
<p>Many Thanks,</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #2 by @lassoan (2020-12-09 20:49 UTC)

<p>You can change the default volume display node to use any color node you like:</p>
<pre><code class="lang-python">displayNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLScalarVolumeDisplayNode')
displayNode.UnRegister(None)
displayNode.SetAndObserveColorNodeID('vtkMRMLColorTableNodeRainbow')
slicer.mrmlScene.AddDefaultNode(displayNode)
</code></pre>
<p>If you want to use this setting in all your Slicer sessions, then add these lines to your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">application startup script</a>.</p>

---

## Post #3 by @Jonathan_Lesage (2020-12-09 21:22 UTC)

<p>Hi Andras,</p>
<p>Thank you for your quick response! After adding the code snippet above to my .slicerrc.py file, Slicer crashes when I load data. If it makes a difference I am loading .nrrd files.</p>
<p>Any further guidance would be greatly appreciated!</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #4 by @lassoan (2020-12-09 21:24 UTC)

<p>Do you have any problems if you load a sample data set (e.g., MRHead)?</p>
<p>What Slicer version do you use, on what operating system?</p>
<p>Do you see any errors in the application log? (menu: Help / Report a bug -&gt; select the log file of the previous session)</p>

---

## Post #5 by @Jonathan_Lesage (2020-12-10 18:05 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="14969">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">displayNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLScalarVolumeDisplayNode')
displayNode.SetAndObserveColorNodeID('vtkMRMLColorTableNodeRainbow')
slicer.mrmlScene.AddDefaultNode(displayNode)
</code></pre>
</blockquote>
</aside>
<p>Hi Andras,</p>
<p>When I load MRHead slicer doesn’t crash but the colour stays Grey.</p>
<p>I am currently using 4.10.1 on Windows 10.</p>
<p>When I try to load my own data again the log after crash gives the following:</p>
<p>[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-12-10 13:04:13<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.10.1 (revision 27931) win-amd64 - installed release<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16205 MB physical, 42113 MB virtual<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 10.12.2020 13:04:13 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 10.12.2020 13:04:15 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 10.12.2020 13:04:16 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.12.2020 13:04:16 [Python] (C:\Program Files\Slicer 4.10.1\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.12.2020 13:04:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 10.12.2020 13:04:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [C:/Users/jlesage/.slicerrc.py]<br>
[DEBUG][Qt] 10.12.2020 13:04:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Reformat”</p>

---

## Post #6 by @Jonathan_Lesage (2020-12-10 18:09 UTC)

<p>Hi Again,</p>
<p>I realise that the crash was related to the scene and annotation files in the directory I loaded, which happens for some reason when I save scenes sometimes.</p>
<p>When I remove these files and just load the nrrd file, slicer doesn’t crash, rather the volume is loaded in Grey as was the case with the MRHead nrrd file.</p>
<p>I think maybe I am missing something in else in the .slicerrc script?</p>
<ul>
<li>Jon</li>
</ul>

---

## Post #7 by @lassoan (2020-12-10 19:35 UTC)

<p>Slicer-4.10 is very old. This feature was not available then. You always need to use at the latest Slicer Stable Release.</p>

---

## Post #8 by @Jonathan_Lesage (2020-12-10 19:58 UTC)

<p>Hi Again Andras,</p>
<p>I’ve downloaded the latest stable release as you’ve suggested. This bit of code does not take effect. Even if I simply enter it in the PYTHON terminal in slicer itself the colour remains Grey.</p>
<p>Any ideas?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c70edb4c92a2997f14849cc7b5a5cfd5f064c482.png" data-download-href="/uploads/short-url/soWQvamtndWJeXOTsM1HdiB8pY6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c70edb4c92a2997f14849cc7b5a5cfd5f064c482.png" alt="image" data-base62-sha1="soWQvamtndWJeXOTsM1HdiB8pY6" width="690" height="45" data-dominant-color="E6E5FF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">710×47 2.24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2020-12-10 20:01 UTC)

<p>The code changes the default display node. It does not affect nodes that are already loaded into the scene. Try loading MRHead after you running the code snippet.</p>
<p>If you load data from DICOM then the display node may be created explicitly (bypassing the default node mechanism), I’ll have a look at this if it can be changed easily. In the meantime, you can take a slightly different approach and add an observer to the NodeAdded event of the scene and if a scalar volume display node is added then change the color node in it. Probably you can copy-paste the code from examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #10 by @lassoan (2020-12-10 20:14 UTC)

<p>I see that the colormap is overridden when you simply use “Add data” window. So, until default color node usage gets used consistently with all loading modes, you need to implement the the scene observation mechanism. You can start from <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_volume_rendering_automatically_when_a_volume_is_loaded">this</a> example and just modify a few lines (change the existing display node instead of creating a volume rendering display node).</p>

---

## Post #11 by @lassoan (2020-12-10 21:13 UTC)

<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/9c87ecb6b7a90411e1b379ceda0dcce36e8a9014">fixed the issue</a> in Slicer core: now color node specified in the default vtkMRMLScalarVolumeDisplayNode always takes precedence over hardcoded values specified in the color logic or volume node class. So, the 3-line code snippet will work in Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #12 by @Jonathan_Lesage (2020-12-11 19:17 UTC)

<p>Andras,</p>
<p>Many Thanks!!</p>

---
