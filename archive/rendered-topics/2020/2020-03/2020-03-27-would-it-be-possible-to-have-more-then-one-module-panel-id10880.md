# Would it be possible to have more then one module panel?

**Topic ID**: 10880
**Date**: 2020-03-27
**URL**: https://discourse.slicer.org/t/would-it-be-possible-to-have-more-then-one-module-panel/10880

---

## Post #1 by @muratmaga (2020-03-27 20:01 UTC)

<p>I sometimes want to have two (or even more) module tabs open to interact with multiple modules at the same time (as oppose to using the arrows to go back and forth). With the ability of undocking the modules tab, and with multiple screen setups, it think this actually kind of makes sense.</p>
<p>In such case I guess the Module selection drop down needs to be part of the module panel, as oppose to menu bar to enable module selection in each panel independently.</p>

---

## Post #2 by @lassoan (2020-03-28 01:34 UTC)

<p>If the module history and favorite modules on toolbar are not convenient enough (e.g., because you want to perform the same workflow multiple times) then having one more module panel would not help much. Instead, you can get more much more convenient, polished GUI by creating a custom scripted module You should be able to put together a GUI panel from the readily available high-level widgets in  a few ten minutes using Qt Designer. Potentially you don’t need to write any code, just drag-and-drop the widgets and connect the signals in Qt designer. You only need to write code if you want to run specific processing functions when a button is clicked.</p>
<p>I would be also reluctant to enable unlimited module panels (e.g., dockable panels) because when you look at applications that take this approach, they all end up being extremely hard to use. We get lots of complaints that Slicer is hard to learn, so I would rather work on things that would take us in that direction.</p>

---

## Post #3 by @muratmaga (2020-03-28 03:06 UTC)

<p>Thanks Andras. I do not know anything about QT Designer. Looking at this page it seems it is more suitable for custom build? <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner</a></p>
<p>But somehow we can use it in a scripted module?</p>

---

## Post #4 by @pieper (2020-03-29 15:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="10880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But somehow we can use it in a scripted module?</p>
</blockquote>
</aside>
<p>It’s part of the current scripted module template.  In developer mode you can start designer on the module with a single click.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would be also reluctant to enable unlimited module panels (e.g., dockable panels) because when you look at applications that take this approach, they all end up being extremely hard to use.</p>
</blockquote>
</aside>
<p>Qt Designer itself starts out with a bunch of panels.  Do you find that hard to use?  I think they did it for the same reason Murat wants it, so you don’t need so many clicks to get what you need.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="10880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I sometimes want to have two (or even more) module tabs open to interact with multiple modules at the same time (as oppose to using the arrows to go back and forth).</p>
</blockquote>
</aside>
<p>If you want to try it out, you can go to the module and then type in the following (replace <code>annotations</code> with the name of the module you want to pop out).  If it basically works we could make a hot key or small button for this.</p>
<pre><code class="lang-auto">slicer.modules.annotations.widgetRepresentation().setParent(None)
slicer.modules.annotations.widgetRepresentation().show()
</code></pre>

---

## Post #5 by @muratmaga (2020-03-30 03:42 UTC)

<p>Thanks Steve. This looks good.</p>

---

## Post #6 by @muratmaga (2020-04-01 16:20 UTC)

<p>Actually, while this popups up the module, the module itself is not functional. I am trying particularly with the Markups module, and you can’t see the control points, nor modify their color/size etc with the popup Markups module, while the docked one in the main module panel works fine.</p>

---

## Post #7 by @pieper (2020-04-01 16:50 UTC)

<p>That’s weird -  Volume Rendering works fine.  Probably Markups and maybe other modules have some other logic that makes it not work in this mode.  Does it work for other modules you use often and if so, do you like the mode well enough that we should take it past this prototype stage (e.g. add a button or hotkey for this).</p>

---

## Post #8 by @jcfr (2020-04-01 17:14 UTC)

<p>If you would like to create an other widget representation for an existing module, it could be done like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; markups_module_widget = slicer.modules.annotations.createNewWidgetRepresentation()
&gt;&gt;&gt; markups_module_widget.setMRMLScene(slicer.mrmlScene)
&gt;&gt;&gt; markups_module_widget.show()
</code></pre>
<p>Next would be to ensure <code>enter()/exit()</code> method can be called from python and this should allow to have the module UI updated.</p>
<p>Doing so (instead of re-parenting) ensures the existing module panel will work as expected.</p>

---

## Post #9 by @smrolfe (2020-04-01 17:52 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> this works perfectly!</p>

---

## Post #10 by @Greydon_Gilmore (2021-01-29 04:26 UTC)

<p>Found this thread really cool, never knew about this functionality before. I have been playing around with the pop out and wanted to add another point. If you want the pop-out window to stay always on top you can add:</p>
<pre><code class="lang-auto">markups_module_widget.setWindowFlag(qt.Qt.WindowStaysOnTopHint)
</code></pre>
<p>This will ensure whatever window you have floating will stay on top of the main panel.</p>

---

## Post #11 by @lassoan (2021-01-29 04:46 UTC)

<p>I would recommend to put all widgets into the window layout (you can add any number of dockable widgets), because popups can get very confusing. For example,when you switch between applications (Alt+Tab) then it is quite random what ends up being visible and where.</p>
<p>See for example the <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/NodeInfo/NodeInfo.py">NodeInfo module</a> if you want to learn how to place additional dockable widgets in the main window.</p>

---

## Post #12 by @Greydon_Gilmore (2021-01-29 04:50 UTC)

<p>I have always just built UI files and loaded them with <code>slicer.util.loadUI()</code>. I never thought about accessing them though the <code>slicer.modules</code> module before. I’ll check out the Nodeinfo module!</p>

---

## Post #13 by @Greydon_Gilmore (2021-01-29 04:59 UTC)

<p>In the NodeInfo module I notced this <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/086d5b4ba78bd25f99a9bf6484a3c9452181fde8/NodeInfo/NodeInfo.py#L97" rel="noopener nofollow ugc">signal/slot syntax</a>. Is there a reason not to use the newer syntax <code>self.showInfoButton.clicked.connect(self.onShowInfoClicked)</code>?</p>

---

## Post #14 by @lassoan (2021-01-29 05:06 UTC)

<p>I’m not sure what you are referring to exactly, because you should not insert a completely different module’s GUI in your own module GUI. It would contain lots of irrelevant components. Instead, you can have a look at the module GUI and just add those widgets to your module that are relevant to your workflow (with all the customization you need).</p>
<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="13" data-topic="10880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>In the NodeInfo module I notced this <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/086d5b4ba78bd25f99a9bf6484a3c9452181fde8/NodeInfo/NodeInfo.py#L97">signal/slot syntax</a>. Is there a reason not to use the newer syntax</p>
</blockquote>
</aside>
<p>I tend to prefer optimizing the code for readability (make it clear that it is a signal, make it clear what arguments it provides), so in general I would choose this syntax:</p>
<pre><code>self.showInfoButton.connect('clicked(bool)', self.onShowInfoClicked)
</code></pre>
<p>instead of this:</p>
<pre><code>self.showInfoButton.clicked.connect(self.onShowInfoClicked)
</code></pre>
<p>but if both work then it is up to you to choose.</p>

---

## Post #15 by @Greydon_Gilmore (2021-01-29 05:12 UTC)

<p>I only meant that I never realized I could access my own modules with <code>slicer.modules.myModuleWidget.mySubWidget</code>. I have just been using the other syntax style for signals/slots so was curious to know.</p>

---
