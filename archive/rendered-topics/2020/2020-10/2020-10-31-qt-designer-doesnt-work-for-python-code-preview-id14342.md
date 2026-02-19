---
topic_id: 14342
title: "Qt Designer Doesnt Work For Python Code Preview"
date: 2020-10-31
url: https://discourse.slicer.org/t/14342
---

# Qt Designer doesn't work for Python code preview

**Topic ID**: 14342
**Date**: 2020-10-31
**URL**: https://discourse.slicer.org/t/qt-designer-doesnt-work-for-python-code-preview/14342

---

## Post #1 by @mau_igna_06 (2020-10-31 01:18 UTC)

<p>The error happens as follows:<br>
Create “NewExtension” with Extension Wizard<br>
Add Module to Extension “NewModule”<br>
Go to Modules combobox, go to Examples-&gt;NewModule<br>
Go to Edit UI (Qt Designer opens)<br>
Go to Form-&gt;View Python Code…</p>
<p>It gives the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7e4ec8da721e5e149af258e4bebca1a59f9e304.png" data-download-href="/uploads/short-url/qeNQmyEauWber4i1G0vIBUIvLtW.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7e4ec8da721e5e149af258e4bebca1a59f9e304_2_651x500.png" alt="error" data-base62-sha1="qeNQmyEauWber4i1G0vIBUIvLtW" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7e4ec8da721e5e149af258e4bebca1a59f9e304_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7e4ec8da721e5e149af258e4bebca1a59f9e304_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7e4ec8da721e5e149af258e4bebca1a59f9e304.png 2x" data-dominant-color="D4D4D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1280×983 98.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-10-31 01:36 UTC)

<p>What Slicer version and operating system do you use? Have you built Slicer yourself?</p>

---

## Post #3 by @mau_igna_06 (2020-10-31 14:10 UTC)

<p>Slicer version is 4.11.20200930 and Windows version is Windows 10 Pro x64.<br>
I haven’t built Slicer myself because I wasn’t able to get the dependencies going. This is the installer version</p>

---

## Post #4 by @lassoan (2020-10-31 17:42 UTC)

<p>Can you check if it works in the latest Slicer Preview Release? (there were some fixes related to this)</p>
<p>The Preview Release still has a few major issues, but you may just use its Qt Designer.</p>

---

## Post #5 by @mau_igna_06 (2020-10-31 18:05 UTC)

<p>Yes, Andras. I have checked and it doesn’t work on the Preview Release.<br>
Also if you select Form-&gt;View C++ Code… it shows the same error.</p>

---

## Post #6 by @lassoan (2020-10-31 18:39 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="14342">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Go to Form-&gt;View Python Code…</p>
</blockquote>
</aside>
<p>I’ve just realized that you are trying to generate some Python code. This is not needed! In Slicer, we developed a much simpler method for using .ui files in Python directly, using <code>slicer.util.loadUI</code> and <code>slicer.util.childWidgetVariables</code> functions, as it is shown in the module template.</p>
<p>You get the error because Python code generation requires the <code>uic</code> compiler, which we don’t bundle with Slicer, as it should not be necessary.</p>

---

## Post #7 by @mau_igna_06 (2020-10-31 20:49 UTC)

<p>Thank you Andras for clarifing the matter. I wanted to review the code because I wanted to make a coded UI but no problem, I’ll stick to .ui desing in Qt Designer.<br>
Is there a tutorial to create a script with .ui GUI? because I don’t know what to write in some methods that are automatically created and <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc" rel="noopener nofollow ugc">this</a> tutorial I’m using creates the UI through code and looks much simpler</p>

---

## Post #8 by @lassoan (2020-12-16 06:03 UTC)

<p>Using the designer reduces the size of a scripted module by 20-30%. Having less code means less code to debug and maintain. Using a visual designer also allows the developer on nicer, more intuitive GUI, while generating from code tends to result in GUI that the developer can create more easily, but it is worse for the users. I would recommend <a href="https://slicer--5344.org.readthedocs.build/en/5344/developer_guide/api.html#id1">this</a> developer tutorial.</p>

---

## Post #9 by @mau_igna_06 (2020-12-16 15:19 UTC)

<p>Thank you Andras. I checked it out a little bit but I’ll read it more carefully when I have a little more time. Until now I was only using <a href="https://apidocs.slicer.org/master/" rel="noopener nofollow ugc">this</a> to check out classes definitions and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">this</a> for some code examples. Now I have another resourse <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---
