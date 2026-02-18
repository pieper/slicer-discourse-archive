# Setting window icon for floating module widget?

**Topic ID**: 9819
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/setting-window-icon-for-floating-module-widget/9819

---

## Post #1 by @brynpitt (2020-01-14 23:02 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>Hi all–</p>
<p>I have created a module (using the ScriptedLoadableModule template), and I am trying to add a button to the widget GUI that sets the window to full screen.</p>
<p>As part of that, I would also like to set the module widget to float and also change the module window icon to a custom icon. I am able to achieve the desired appearance when launching Slicer with a custom launch script using this code:</p>
<blockquote>
<p>slicer.util.mainWindow().showFullScreen<br>
slicer.modules.mymodule.widgetRepresentation().show()<br>
slicer.modules.mymodule.widgetRepresentation().setWindowIcon(qt.QIcon(customIconFilePath))</p>
</blockquote>
<p>However, once I have opened my module in the module panel in Slicer, the above code that works in the launch script doesn’t show my module in a floating window (but the code runs without error). I assume this has something to do with the fact that my module is already open in the model panel. Is there a way to get around this issue? I would really like to be able to achieve the desired appearance by clicking a button in my module’s GUI rather than launching in full screen.</p>
<p>FYI, I tried to achieve the desired appearance by floating the module panel (after my module was already open in the module panel). Here’s an excerpt of the relevant code:</p>
<blockquote>
<p>slicer.util.mainWindow().showFullScreen<br>
moduleBrowser = slicer.util.mainWindow().findChild(“QDockWidget”, “PanelDockWidget”)<br>
moduleBrowser.setFloating(True)<br>
moduleBrowser.setWindowIcon(qt.QIcon(customIconFilePath))</p>
</blockquote>
<p>This code runs without error, but I have two issues:</p>
<ol>
<li>
<p>The floating module panel includes the Data Probe and a large Slicer logo. (I’d rather not have those things in the window.)</p>
</li>
<li>
<p>The window icon doesn’t actually change. (No window icon appears at all.)</p>
</li>
</ol>
<p>Can anyone tell me how I can achieve my desired appearance when executing code via a button in the module widget GUI? This is a minor issue, but I would still greatly appreciate any help!</p>
<p>Thanks in advance,<br>
EBP</p>

---

## Post #2 by @pieper (2020-01-15 00:45 UTC)

<p>You might try setting the parent to None like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L701-L702" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerAnimator/blob/master/Animator/Animator.py#L701-L702" target="_blank">pieper/SlicerAnimator/blob/master/Animator/Animator.py#L701-L702</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="701" style="counter-reset: li-counter 700 ;">
<li>threeDWidget.setParent(None)</li>
<li>threeDWidget.show()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2020-01-15 01:54 UTC)

<aside class="quote no-group" data-username="brynpitt" data-post="1" data-topic="9819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e99b99/48.png" class="avatar"> brynpitt:</div>
<blockquote>
<p>slicer.util.mainWindow().showFullScreen</p>
</blockquote>
</aside>
<p>Full-screen applications are rendered completely differently than windowed applications. If you experience any strange rendering then make the application window maximized and hide the frame but not make the application full-screen.</p>
<aside class="quote no-group" data-username="brynpitt" data-post="1" data-topic="9819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e99b99/48.png" class="avatar"> brynpitt:</div>
<blockquote>
<p>The floating module panel includes the Data Probe and a large Slicer logo. (I’d rather not have those things in the window.)</p>
</blockquote>
</aside>
<p>There are helper functions that you can use to show/hide different components of the application GUI. You have even more control over everything if you implement a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets#Custom_Slicer_application">custom application</a>.</p>
<aside class="quote no-group" data-username="brynpitt" data-post="1" data-topic="9819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e99b99/48.png" class="avatar"> brynpitt:</div>
<blockquote>
<p>The window icon doesn’t actually change. (No window icon appears at all.)</p>
</blockquote>
</aside>
<p>The module panel is a QDockWidget, which does not have a window icon. You can of course always override the paint function and create a custom widget that does paint itself with an icon.</p>
<aside class="quote no-group" data-username="brynpitt" data-post="1" data-topic="9819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e99b99/48.png" class="avatar"> brynpitt:</div>
<blockquote>
<p>how I can achieve my desired appearance</p>
</blockquote>
</aside>
<p>From a textual description it is hard to catch what is the desired appearance. Posting a few screenshots, showing what you want and what you get would help a lot in understanding it.</p>

---

## Post #4 by @brynpitt (2020-01-21 15:59 UTC)

<p>Using setParent(None) fixed my issue!</p>
<p>To help future users who might have a similar issue, here is a screen shot of my desired behavior (using the Data module as an example):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/056a1d6e3adf52afeb73306719787e96d8fb6f78.png" data-download-href="/uploads/short-url/LTJJnH543U4FIpBPj2EH5cgTKo.png?dl=1" title="slicer_prnt_scrn" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/056a1d6e3adf52afeb73306719787e96d8fb6f78_2_345x193.png" alt="slicer_prnt_scrn" data-base62-sha1="LTJJnH543U4FIpBPj2EH5cgTKo" width="345" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/056a1d6e3adf52afeb73306719787e96d8fb6f78_2_345x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/056a1d6e3adf52afeb73306719787e96d8fb6f78_2_517x289.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/056a1d6e3adf52afeb73306719787e96d8fb6f78_2_690x386.png 2x" data-dominant-color="BABCE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_prnt_scrn</span><span class="informations">2562×1440 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This issue I was having was that if the target modules (the Data module in the example) was already open in the Module Browser (which is set to be invisible), then</p>
<blockquote>
<p>slicer.modules.data.widgetRepresentation().show()</p>
</blockquote>
<p>would not show the Data module as desired. This issue was fixed using <a class="mention" href="/u/pieper">@pieper</a>’s suggestion:</p>
<blockquote>
<p>slicer.modules.data.widgetRepresentation().setParent(None)</p>
</blockquote>
<p>before showing the module. I could then change the window icon as desired (not shown in the screen shot above).</p>
<p>Thanks for the help!</p>

---
