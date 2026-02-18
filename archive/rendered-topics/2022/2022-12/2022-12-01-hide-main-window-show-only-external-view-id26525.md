# Hide main window - Show only external view

**Topic ID**: 26525
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/hide-main-window-show-only-external-view/26525

---

## Post #1 by @lucas_sd (2022-12-01 03:01 UTC)

<p>Hi everybody,</p>
<p>Im running my module from the terminal using --no-main-window, and I wondering if its possible to show just an external view like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout" rel="noopener nofollow ugc">that</a>.</p>
<p>The idea is run the module from the terminal with 3dS in the back, in some moment the external view appears (necessary to put a point), then close it and continue with the rest of the process.</p>
<p>Thanks for your help, Lucas.</p>

---

## Post #2 by @lassoan (2022-12-01 03:30 UTC)

<p>I would recommend to use the main window, as it makes everything much simpler (and allows you to switch back to the full Slicer GUI for testing and troubleshooting very easily).</p>
<p>You can hide unnecessary decoration of the window using <code>slicer.util.set...Visible</code> functions:</p>
<pre><code class="lang-python">showFull = False  # set it to True to show the full Slicer GUI
slicer.util.setMenuBarsVisible(showFull)
slicer.util.setStatusBarVisible(showFull)
slicer.util.setToolbarsVisible(showFull)
slicer.util.findChild(None, "PanelDockWidget").setVisible(showFull)
</code></pre>
<p>See more information on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">Slicelet page</a>.</p>

---

## Post #3 by @lucas_sd (2022-12-02 18:39 UTC)

<p>HI Andras, the idea is start the module from the console and open the 3dS GU just to take some points and close it.</p>
<p>I wonder if its possible run the process like that:</p>
<ul>
<li>Run my module from my terminal with 3dS --no-main-window.</li>
<li>In some moment of the process the module opens 3dS GUI.</li>
<li>The user take some points, and then the module closes  3dS GUI.</li>
<li>The module continues with the rest.</li>
</ul>
<p>I dont know if its possible (and how) to open and close the GUI when I started with --no-main-window.</p>
<p>Thanks, Lucas.</p>

---

## Post #4 by @lassoan (2022-12-03 05:19 UTC)

<p>I don’t think you can create a main window later, but what you can do is to hide the main window right after it is created. It will just pop up for a fraction of a second. If you don’t want the main window to appear even for a very short time then I think you need to implement a custom application and change the main window initialization.</p>
<p>You can also keep a running Slicer in the background and just send commands to execute using web requests (executed by the WebServer module). This has the advantage that Slicer has to be started only once when the computer starts (or the first time it is needed) and it can stay hidden in the background until it is needed to display something.</p>

---
