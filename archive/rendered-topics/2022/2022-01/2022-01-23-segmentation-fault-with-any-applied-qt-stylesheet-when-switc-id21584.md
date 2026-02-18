# Segmentation fault with any applied Qt stylesheet when switch off from Transform Module

**Topic ID**: 21584
**Date**: 2022-01-23
**URL**: https://discourse.slicer.org/t/segmentation-fault-with-any-applied-qt-stylesheet-when-switch-off-from-transform-module/21584

---

## Post #1 by @keri (2022-01-23 19:34 UTC)

<p>Hi,</p>
<p>On Ubuntu 20.04 if I try to apply Qt stylesheet (for example using <a href="https://github.com/PerkLab/SlicerSandbox" rel="noopener nofollow ugc">SandBox</a> style tester with these two default lines) and switch after that I switch to the Transform module and then switch to any other module I get segmentation fault. This makes Qt stylesheets unusable.</p>
<p>Does this happen only on Ubuntu?</p>
<p>I haven’t figured out why this happens only with Transform module but it seems that something related to applying style during <code>qSlicerModulePanel::removeModule</code>:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda25ea7297f81e3973887e07c2ab1175c09308c.jpeg" data-download-href="/uploads/short-url/r3A7hztA9jbOYoJLfzpNyz6JeEc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bda25ea7297f81e3973887e07c2ab1175c09308c.jpeg" alt="image" data-base62-sha1="r3A7hztA9jbOYoJLfzpNyz6JeEc" width="658" height="499" data-dominant-color="DFE1E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">903×686 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jcfr (2022-02-03 18:57 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:"></p>
<p>We should definitely understand the issue and address the problem.</p>
<p>To help move forward with this, could you:</p>
<ul>
<li>share a small standalone example allowing to reproduce the problem. It could be as simple as a list of steps to follow, and few lines that need to be copied into the python interactor</li>
<li>provide some context for reproducing:
<ul>
<li>can it be reproduced using the preview package available from <a href="https://download.slicer.org">https://download.slicer.org</a>
</li>
<li>is the issue specific to a build of Slicer (if yes, which version of Qt)</li>
</ul>
</li>
</ul>

---

## Post #3 by @keri (2022-02-03 19:23 UTC)

<p>Thank you for reply,</p>
<p>Steps to reproduce:</p>
<ol>
<li>from extension manager install <code>Sandbox</code> extension;</li>
<li>restart Slicer;</li>
<li>after the restart go to the <code>Modules-&gt;Developer Tools-&gt;StyleTester</code> and click on <code>Apply to Slicer</code> radiobutton and then click <code>Apply Style</code> pushbutton;</li>
<li>go to the <code>Modules-&gt;Transforms</code> (should be fine);</li>
<li>go to any other module (for example <code>Modules-&gt;Data</code>) or click <code>Previous modules</code> tool button (here I get segfault)</li>
</ol>
<p>This can be reproduced on Ubuntu 20.04 with Slicer downloaded from official web-site v4.13.0 built 2022-02-03 or with Slicer manually built with Qt 5.15.2 with GCC 9.3</p>

---

## Post #4 by @keri (2022-03-27 15:44 UTC)

<p>I just tested that on Windows and it seems that there is no such problem.<br>
But on Ubuntu I get segfault even with the newest Slicer version 2022-03-26</p>

---

## Post #5 by @ebrahim (2022-03-27 20:27 UTC)

<p>This might be the same thing I ran into with my slicer custom app here: <a href="https://github.com/KitwareMedical/lungair-desktop-application/issues/15" class="inline-onebox" rel="noopener nofollow ugc">crash when switching out of transforms module · Issue #15 · KitwareMedical/lungair-desktop-application · GitHub</a></p>

---

## Post #6 by @keri (2022-03-27 20:39 UTC)

<p>Yes I think we encountered the same crash.<br>
But it is not only about SlicerCAT but I can see this crash in Slicer app.<br>
Did you ran into this on Linux?</p>

---

## Post #7 by @ebrahim (2022-03-28 01:55 UTC)

<p>Yes, this was also on Ubuntu 20.04</p>

---

## Post #8 by @keri (2023-04-18 18:34 UTC)

<p>New investigations of that problem are <a href="https://github.com/KitwareMedical/lungair-desktop-application/issues/15#issuecomment-1513018055" rel="noopener nofollow ugc">described here</a>.</p>
<p>Appreciate if somebody take a look.</p>

---
