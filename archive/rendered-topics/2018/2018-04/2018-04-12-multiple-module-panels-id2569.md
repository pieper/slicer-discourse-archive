# Multiple module panels

**Topic ID**: 2569
**Date**: 2018-04-12
**URL**: https://discourse.slicer.org/t/multiple-module-panels/2569

---

## Post #1 by @rhgmn (2018-04-12 13:29 UTC)

<p>Hello,</p>
<p>I do my best to develop extensions that are modular so that I can use them for many different tasks. However, the division in functionality results in me having to switch modules in the module panel frequently, which is time consuming and tedious.</p>
<p>I was wondering if there was ever interest in enabling the creation of multiple dockable/floating module panels instead of just the single module panel + backward/forward/recent navigation widgets that currently exist. I think it would be useful for users that must perform a task multiple times that requires three or more distinct modules over its course.</p>
<p>I understand that I could build this functionality into my own modules with persistent dialogs, but I think this problem may occur for more than just me, and it also would be better solved if these widgets were able to have the current module panel widget’s docking functionality.</p>
<p>Rachel</p>

---

## Post #2 by @pieper (2018-04-12 15:24 UTC)

<p>Hi Rachel -</p>
<p>For now it’s pretty easy to show any module widget as a floating window with code like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; ww = slicer.modules.addscalarvolumes.widgetRepresentation()
&gt;&gt;&gt; ww.show()
</code></pre>
<p>It will get re-docked to the mainwindow if the user selects that module from the module menu, but otherwise it should be usable.  These could also be put into a new layout for grouping them.</p>
<p>It would be nice to have some conventions for this.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @lassoan (2018-04-12 16:46 UTC)

<p>In the last decade, we’ve used Slicer for probably over a hundred different projects. We’ve found that projects go through several phases and current Slicer capabilities are generally satisfy needs for each phase:</p>
<ol>
<li>Engineering prototyping</li>
</ol>
<p>Use Slicer as is, to find a suitable workflow. In this phase, we experiment with a large number of modules, use it in various combinations. We certainly switch between many modules while using Slicer this way. Module selector controls (previous, next, history) and search (hit Ctrl+F, type part of module name, then hit Enter) can make switches relatively painless.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0eb4c4d5211613eab83b0631428ac69a05e80cb.png" alt="image" data-base62-sha1="mXywb9dnh6bfDlmrPnSBS7eB13R" width="411" height="177"></p>
<ol start="2">
<li>Clinical prototyping</li>
</ol>
<p>Once a clinically acceptable workflow is determined, we develop scripted module, which sets up the scene (create transforms, set default visualization options, etc.) and provides a user interface that makes all necessary features available in one place. These prototypes are still mostly used by researchers or engineers because you can still get lost among the many features and options available, but the software can be used quite efficiently (number of clicks to achieve a certain operation is already minimized).</p>
<ol start="3">
<li>Clinical use</li>
</ol>
<p>Once a prototypes proves to be clinically useful, you can create a custom application (slicelet) from your module by disabling/hiding all unnecessary features, customizing branding (replace Slicer logo, etc. with your own company logo), further optimizing your custom module. in this phase, you also need to produce a fair amount of documentation, test results, etc. for obtaining regulatory approval. In this stage, the software is simple enough so that it can be operated by clinicians who are not experienced Slicer users.</p>
<hr>
<p>Showing multiple module user interfaces at once:</p>
<ul>
<li>might slightly help in some cases in engineering prototyping phase, but usability is not really a focus of this phase anyway. In this phase, you spend your time with figuring out what modules to use, with what settings, with what combination of other modules.</li>
<li>is not a usable approach for clinical prototyping (or later) phase, as you would need to do a lot of manual work (setting up the scene, arranging module user interfaces, paying attention to use modules in the correct order, etc).</li>
</ul>
<p>Since this feature would have narrow use case and could potentially make the user interface very complicated, there is very little incentive to implement it.</p>

---

## Post #4 by @pieper (2018-04-12 17:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="2569">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We certainly switch between many modules while using Slicer this way. Module selector controls (previous, next, history) and search (hit Ctrl+F, type part of module name, then hit Enter) can make switches relatively painless.</p>
</blockquote>
</aside>
<p>Also you can move back and forth through the module history.  On the mac it is command-left-arrow and command-right-arrow.  I think it’s control-left and control-right on the windows (can someone confirm?).  I don’t see this on the wiki but we can add it.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/KeyboardShortcuts#Navigating_Application" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/KeyboardShortcuts#Navigating_Application</a></p>

---

## Post #5 by @lassoan (2018-04-12 19:39 UTC)

<p>I’ve just tried and Ctrl + Left/Right arrow switches between modules on Windows (unless you are in an text editor or other widget that uses this shortcut).</p>
<p>Thanks <span class="mention">@piper</span>, I’ve learnt something new about Slicer today!</p>

---

## Post #6 by @pieper (2018-04-12 22:31 UTC)

<p>Great!</p>
<p>Thanks for confirming - I updated the wiki (4.8 and Nightly) with this info.</p>

---
