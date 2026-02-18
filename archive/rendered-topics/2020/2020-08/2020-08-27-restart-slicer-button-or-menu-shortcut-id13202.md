# Restart Slicer button or menu shortcut

**Topic ID**: 13202
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/restart-slicer-button-or-menu-shortcut/13202

---

## Post #1 by @ezgimercan (2020-08-27 18:42 UTC)

<p>Just wondering if there are plans to add a shortcut menu item for researting Slicer? I often find myself closing the app and re-openning it during the development of a module or even using modules under development. I am not aware of a shortcut for restarting Slicer - only when new extensions are installed or certain menu items are changed it prompts and automatic restart. I think it would be good to have a menu item for it - unless there is good reason not to.</p>

---

## Post #2 by @lassoan (2020-08-27 19:13 UTC)

<p>Restart button is shown at the top at all scripted module’s GUI.</p>
<p>If you just want to restart without touching your mouse, then you can type <code>restart()</code> in the Python console.</p>
<p>If typing restart is too much then you can specify a shortcut (that you can put into your startup .slicerrc.py file). For example, restart Slicer on <kbd>Ctrl+Shift+R</kbd>:</p>
<pre><code class="lang-python">shortcut = qt.QShortcut(qt.QKeySequence("Ctrl+Shift+R"), slicer.util.mainWindow())
shortcut.connect('activated()', slicer.util.restart)
</code></pre>

---

## Post #3 by @muratmaga (2020-08-27 19:29 UTC)

<p>Just to add what Andras said, I think you need to enable “Developer Mode” from the Application Settings for the button to show up.</p>

---

## Post #4 by @ezgimercan (2020-08-27 19:36 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a>. This is useful. I will use this shortcut a lot.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, yes it is enabled for me but I was thinking of a more general case: if users get errors in python interactor when using scripted modules or they mess up other settings in the scene, the cleanest way is to restart the Slicer. For example, when I used “Lights” module, it messed up lights for any volume rendering then on. Cleaning the scene does not solve this. I need to restart the Slicer.</p>
<p>I think having “Restart Slicer” in File menu would be nice for all users.</p>

---

## Post #5 by @lassoan (2020-08-27 20:33 UTC)

<p>Making it easier for users to restart Slicer would fragment the user community into two groups: those who know that they need to restart Slicer at certain times; and those who don’t know this. I would much rather have a more uniform user community, who don’t suppress errors by frequent restarts, and report any potential errors that they encounter due to prolonged use of the application.</p>
<p>Developers are a different category. They can mess up things up, so allowing restart makes sense for them.</p>

---

## Post #7 by @JHud (2022-05-06 10:02 UTC)

<p>I was having problems finding the .slicerrc.py. If this file is not on your machine you can create it in Application Settings, under Application startup Script, click the folder icon and the script will be created in the specified path.</p>

---
