---
topic_id: 19326
title: "Get Popup Widget Of A 3D View"
date: 2021-08-23
url: https://discourse.slicer.org/t/19326
---

# Get popup widget of a 3D view

**Topic ID**: 19326
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/get-popup-widget-of-a-3d-view/19326

---

## Post #1 by @keri (2021-08-23 17:13 UTC)

<p>Hi,</p>
<p>As I can see there is <code>qMRMLThreeDViewControllerWidget.ui</code> wich is popup widget when one clicks on pin button of a three D view.</p>
<p>I want to add there some buttons.</p>
<p>To do that I need to get instance of it <code>qMRMLThreeDViewControllerWidget</code>.</p>
<p>There is a method <code>LayoutManager-&gt;threeDWidget(0)-&gt;threeDController()</code> wich returns <code>qMRMLThreeDViewControllerWidget*</code> but this returns the whole 3D widget instead. There are also some other methods (displayed on the picture) but there is no one that would return me <code>ctkPopupWidget</code> (it is initialized in <code>qMRMLViewControllerBar.cxx</code>). Pin button is connected to the slot wich arises popup widget but I can’t see a way to get instance of it…</p>
<p>Was it done intensionally?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c70c769a9e6c5c13af82ca354f56af5134fe20d5.png" alt="image" data-base62-sha1="soRIAfX1BnkpphCTJy9qjKP6dnf" width="676" height="246"></p>

---

## Post #2 by @lassoan (2021-08-24 23:53 UTC)

<p>There are convenience methods for getting higher-level widgets and after that you can use standard Qt introspection to access lower-level widgets. For example, you can add a button to the view controller widget like this:</p>
<pre data-code-wrap="python"><code class="lang-python">controllerWidget = slicer.app.layoutManager().threeDWidget(0).threeDController()
buttonLayout = slicer.util.findChild(controllerWidget, 'qMRMLThreeDViewControllerWidget').layout()

button = qt.QToolButton()
button.text="test"
buttonLayout.addWidget(button)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f982e7c9a9e258f1ceecb3fdc060f86946f74248.png" data-download-href="/uploads/short-url/zBhlVFC6OuiFxjWYYEAZvl4KuyA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f982e7c9a9e258f1ceecb3fdc060f86946f74248.png" alt="image" data-base62-sha1="zBhlVFC6OuiFxjWYYEAZvl4KuyA" width="690" height="332" data-dominant-color="C4C5E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">714×344 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can get a list of all child widgets of a widget by using <code>slicer.util.findChildren()</code>:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; findChildren(controllerWidget)
[qMRMLThreeDViewControllerWidget(0x1a6d22e27a0) ,
ctkPopupWidget(0x1a6d2496ff0, name="qMRMLThreeDViewControllerWidget") ,
QToolButton(0x1a689cca530) ,
ctkButtonGroup (ctkButtonGroup at: 0x000001A6D245A870),
QActionGroup (QActionGroup at: 0x000001A6D245A370),
QMenu(0x1a6d2498830) ,
QAction(0x1a6d245a470 text="More" toolTip="More" menuRole=TextHeuristicRole visible=true) ,
QMenu(0x1a6d2498b70, name="rulerMenu") ,
QAction(0x1a6d245a3b0 text="" menuRole=TextHeuristicRole visible=true) ,
QAction(0x1a6d245a6d0 text="Ruler" toolTip="Ruler" menuRole=TextHeuristicRole visible=true) ,
... 
]
</code></pre>

---

## Post #3 by @keri (2021-08-24 23:57 UTC)

<p>Thank you very much! I always forget about slicer’s <code>util</code> class</p>
<p>Also probably we could add a method to <code>controllerWidget</code> wich returns <code>ctkPopupWidget</code>? That should be quite simple and useful I think…</p>
<p>I could make a PR if needed</p>

---

## Post #4 by @keri (2021-08-26 01:06 UTC)

<p>By the way I just tested and to do almost the same in C++ I needed call <code>findChild</code> template with <code>ctkPopupWidget*</code> type:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">  ctkPopupWidget* popupWidget = controller-&gt;
      findChild&lt;ctkPopupWidget*&gt;("qMRMLThreeDViewControllerWidget");

  QGridLayout* gridLayout = qobject_cast&lt;QGridLayout*&gt;(popupWidget-&gt;layout()); // don't know why but this returns me NULL

  QToolButton* cubeAxesToolBtn = new QToolButton(popupWidget);

//  gridLayout-&gt;addWidget(cubeAxesToolBtn, 0, 4);  // as I can't yet cast layout to gridLayout then I comment this
  popupWidget-&gt;layout()-&gt;addWidget(cubeAxesToolBtn);
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443799632f5b184ffa5eb36dff5bed4ee617a53b.png" alt="image" data-base62-sha1="9JtAuOGO3eyY1KciYWqwUWnQgPh" width="309" height="127"></p>
<p>How do you think if I create PR where I add a method <code>getPopupWidget()</code> to <code>qMRMLThreeDViewControllerWidget</code> that would return <code>popupWidget</code>?<br>
Because it is very intuitive to have a guess that there should be some method that returns that popup widget. And if there is no such method then it is difficult to understand who is the parent and the type of that widget… As for me without you I would not solve that simple task <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>The same I could do with <code>qMRMLSliceControllerWidget</code>.</p>

---

## Post #5 by @lassoan (2021-08-26 04:20 UTC)

<p>We try not to expose too much of the low-level Slicer API because that would limits us in how we can add features without breaking backward compatibility. When you don’t find an accessor for some low-level features then it usually means “Do Not Open - No User Serviceable Parts Inside” (we don’t make a commitment to maintain the API, we don’t want to troubleshoot problems due to developers changing those parts, etc.). It happens sometimes that some APIs just has not yet been considered to be exposed (there was no need for it).</p>
<p>The popup widget is fairly high-level and stable (not expected to change a lot in the near future), so it might be OK to add an accessor for it, but I would rather do it if at the same time you introduce a mechanism that allows customization of the button list more cleanly. It does not make sense to remove low-level Qt method calls to get the widget, if you still need to execute a number of similarly low-level calls to make any changes in the buttons.</p>

---

## Post #6 by @keri (2021-08-26 08:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="19326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but I would rather do it if at the same time you introduce a mechanism that allows customization of the button list more cleanly.</p>
</blockquote>
</aside>
<p>For example in my case I need to move some tollbuttons inside grid layout. I’m going to add a zoomer that zooms selected region rectangle (in VTK examples there is such tool). I would like to settle all zoom buttons near each other. To do that I’m going to use <a href="https://doc.qt.io/qt-5/qlayout.html#replaceWidget" rel="noopener nofollow ugc">QLayout::replaceWidget()</a> in pair with <code>findChild()</code> (I have not tried yet I think it should work) to find a specific tool button. I don’t know what mechanism could I introduce… Maybe you have some ideas/examples?</p>

---

## Post #7 by @lassoan (2021-08-26 15:38 UTC)

<p>The API could be similar to how you can specify:</p>
<ul>
<li>Segment Editor effects: you can register new effects, specify order of effects, and choose to show only those effects that you included in the ordered list</li>
<li>subject hierarchy view context menu items: you can register new actions, specify their “weight” that determines their position and grouping in the list, and you can provide a whitelist of actions using allowedViewContextMenuActionNames</li>
</ul>
<p>You would need some kind of factory mechanism that would allow creating new actions in each 3D view automatically.</p>

---

## Post #8 by @keri (2021-08-26 18:51 UTC)

<p>I think I’m not ready yet to implement that. Let’s pospone that…</p>

---

## Post #9 by @slicer365 (2021-08-30 14:43 UTC)

<p>How do I want to add a command to this button and where should I operate it?</p>
<p>I don’t know how to program.</p>
<p>I just want to add a simple command to the new button, such as click it ,then get setDataProbeVisible(0)</p>

---

## Post #10 by @lassoan (2021-08-30 14:45 UTC)

<p><a class="mention" href="/u/slicer365">@slicer365</a> what would you like to achieve? Make Data probe hidden by default?</p>

---

## Post #11 by @slicer365 (2021-08-30 14:51 UTC)

<p>Yes, of course, I can add this code to the startup py file,</p>
<p>but when I use the slicer, I want to restart DataProbe,</p>
<p>I need to reopen the Python and the input code, which is a bit complicated,</p>
<p>I want to directly add the function to a small widget .</p>

---

## Post #12 by @lassoan (2021-08-30 14:52 UTC)

<p>Would simply collapsing the Data Probe instead of hiding it solve the issue?</p>

---

## Post #13 by @slicer365 (2021-08-30 14:57 UTC)

<p>Maybe,</p>
<p>but there are many such small functions, such as setMenuBarsVisible(), setStatusBarVisible(0) and so on.</p>
<p>Seeing this discussion, I was wondering whether I can add this small piece of code to a certain button arbitrarily to achieve personalization</p>

---

## Post #14 by @lassoan (2021-08-30 15:11 UTC)

<p>You can collapse the Data Probe by default by adding this to the application startup script:</p>
<pre><code class="lang-python">findChild(mainWindow(), "DataProbeCollapsibleWidget").collapsed=True
</code></pre>
<p>If you find that the menu bar, status bar, etc. take up significant amount of space then it suggests that your application font is too large. You can set text scale in your operating system, or in Slicer application settings, or specify scaling by setting <code>QT_SCALE_FACTOR</code> environment variable (e.g., <code>set QT_SCALE_FACTOR=0.75</code>).</p>
<p>If you still want to hide all user interface elements then you are probably better off specifying a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures">keyboard shortcut</a> for it.</p>

---

## Post #15 by @joanne40226 (2022-03-31 07:10 UTC)

<p>Hi, sorry to interrupt. I wonder how to remove the existed widget/button under the pinButton? Thank you.</p>

---

## Post #16 by @keri (2022-03-31 13:05 UTC)

<p><a class="mention" href="/u/joanne40226">@joanne40226</a> hi,</p>
<p>There is a example of doing something similar, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-widgets-in-view-controller-bars" rel="noopener nofollow ugc">take a look</a></p>

---

## Post #18 by @joanne40226 (2022-04-01 04:38 UTC)

<p><a class="mention" href="/u/keri">@keri</a><br>
Thank you for your reply! However, I wonder how to remove the button “under” the pinButton, not the pintButton itself. I mean, i want some of the button “under” the pinButton to be removed and some added.</p>

---

## Post #19 by @keri (2022-04-01 11:07 UTC)

<p>I think you know that Slicer uses Qt for displaying GUI.<br>
All you can see are Qt widgets (<code>widget</code> is some base class for any GUI element in Qt)<br>
Qt GUI uses <code>parent-child</code> hierarchy (some kind of a tree structure I think).<br>
So if you have instance of a parent object, there a good chances to find child needed.</p>
<p>To find child needed you need to know some information about the child widget (probably button in your case) that you want to get.<br>
For example such information may be <code>objectName</code>, and/or the type of a widget (QPushButton, QToolButton etc, examples below).<br>
Then you can use these information for example using the syntax <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#hide-slicer-logo-from-main-window" rel="noopener nofollow ugc">slicer.util.findChild(parent ,“objectName”)</a><br>
Or <code>sliceController.findChild("QPushButton", "objectName")</code> (slicerController is supposed the parent in that case).<br>
Or probably <code>sliceController.pinButton().findChild(...)</code></p>
<p><strong>So the problem is how to get the information about the child?</strong></p>
<p>For example I usually look for a tooltip (by pointing the mouse cursor) of a widget that is located “close” to the widget I want to get. Or if I already know that the widget is a part of some module then I go to <a href="https://github.com/Slicer/Slicer" rel="noopener nofollow ugc">source code of Slicer</a> and in VSCode textual editor I paste the keyword (the tooltip for example).</p>
<p>Usually many Slicer’s widgets are “written” in QtDesigner thus you may want to find the <code>.ui</code> file containing some graphically displayed widgets. There you can find most of the information needed.</p>
<p>If you can’t find information about the child then you try to iterate the children and the if it fits you.<br>
Or you may ask on the forum what exactly the widget you want to find, probably for somebody it is not a problem to remember the object name of this widget.</p>
<p>And one note: in Slicer’s python interpreter you can press <code>TAB</code> button of the keyboard to get the hints about the methods of an object.<br>
For example:<br>
<code>sliceController.&lt;press TAB&gt;</code> a popup window will be shown<br>
or<br>
<code>dir(sliceController)</code> will print the info</p>
<p>But the most powerful method is to use <a href="https://github.com/Slicer/SlicerJupyter" rel="noopener nofollow ugc">SlicerJupyter</a><br>
There you can also use <code>TAB</code> or <code>SHIFT-TAB</code> to get hints. It is a good place to work/make mistakes/learn Slicer from python side</p>

---

## Post #20 by @joanne40226 (2022-04-03 02:41 UTC)

<p>Understood! Thank you so much.</p>

---
