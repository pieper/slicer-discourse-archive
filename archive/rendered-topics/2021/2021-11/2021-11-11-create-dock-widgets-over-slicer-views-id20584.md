# Create dock widgets over Slicer views

**Topic ID**: 20584
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/create-dock-widgets-over-slicer-views/20584

---

## Post #1 by @mau_igna_06 (2021-11-11 17:26 UTC)

<p>Hi.</p>
<p>I’m having problems implementing a floating (unmovable) widget container over the views like in these images:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6be9078ada3d2ba1f997d5096b589592d45106ce.jpeg" data-download-href="/uploads/short-url/foClRCt8QVirH2AGUQ5WI5dXGEu.jpeg?dl=1" title="gui5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6be9078ada3d2ba1f997d5096b589592d45106ce_2_666x500.jpeg" alt="gui5" data-base62-sha1="foClRCt8QVirH2AGUQ5WI5dXGEu" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6be9078ada3d2ba1f997d5096b589592d45106ce_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6be9078ada3d2ba1f997d5096b589592d45106ce_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6be9078ada3d2ba1f997d5096b589592d45106ce.jpeg 2x" data-dominant-color="2E4C5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gui5</span><span class="informations">1280×960 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7a1006eca10f2a0b83b422b8180770ba494af9b.jpeg" data-download-href="/uploads/short-url/stZXAF3sJzXceTJUqfdNXE6U031.jpeg?dl=1" title="gui4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a1006eca10f2a0b83b422b8180770ba494af9b_2_666x500.jpeg" alt="gui4" data-base62-sha1="stZXAF3sJzXceTJUqfdNXE6U031" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a1006eca10f2a0b83b422b8180770ba494af9b_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a1006eca10f2a0b83b422b8180770ba494af9b_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7a1006eca10f2a0b83b422b8180770ba494af9b.jpeg 2x" data-dominant-color="354956"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gui4</span><span class="informations">1280×960 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc79bc6e27e8e1284e87b239fc99fe16b7ff4ff8.jpeg" data-download-href="/uploads/short-url/qTkA83xCLQNyAmGi9qbCCLBYvH2.jpeg?dl=1" title="gui3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc79bc6e27e8e1284e87b239fc99fe16b7ff4ff8_2_666x500.jpeg" alt="gui3" data-base62-sha1="qTkA83xCLQNyAmGi9qbCCLBYvH2" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc79bc6e27e8e1284e87b239fc99fe16b7ff4ff8_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc79bc6e27e8e1284e87b239fc99fe16b7ff4ff8_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc79bc6e27e8e1284e87b239fc99fe16b7ff4ff8.jpeg 2x" data-dominant-color="354C5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gui3</span><span class="informations">1280×960 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e642688d9201320ec668ddffa59badecb10e297.jpeg" data-download-href="/uploads/short-url/i26JqPW8B4zI9IUkB4PHII9OY6P.jpeg?dl=1" title="gui2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e642688d9201320ec668ddffa59badecb10e297_2_666x500.jpeg" alt="gui2" data-base62-sha1="i26JqPW8B4zI9IUkB4PHII9OY6P" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e642688d9201320ec668ddffa59badecb10e297_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e642688d9201320ec668ddffa59badecb10e297_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e642688d9201320ec668ddffa59badecb10e297.jpeg 2x" data-dominant-color="384C5A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gui2</span><span class="informations">1280×960 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efcda4e1bde92ca5a74d47fabe14d1858c9a6494.jpeg" data-download-href="/uploads/short-url/ydoHLbHI8QOndj95FqKzzgdIWsQ.jpeg?dl=1" title="gui1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efcda4e1bde92ca5a74d47fabe14d1858c9a6494_2_666x500.jpeg" alt="gui1" data-base62-sha1="ydoHLbHI8QOndj95FqKzzgdIWsQ" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efcda4e1bde92ca5a74d47fabe14d1858c9a6494_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efcda4e1bde92ca5a74d47fabe14d1858c9a6494_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efcda4e1bde92ca5a74d47fabe14d1858c9a6494.jpeg 2x" data-dominant-color="394D5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">gui1</span><span class="informations">1280×960 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see the floating widgets appear over the views (3D and slices) and I think they should have a fixed relative position with reference to the corresponding view in case of mainWindow moveEvent or resizeEvent.<br>
They should appear on click of the toolbar on the left but that I think I know how to do.</p>
<p>Let me show you the approaches I tried without success:</p>
<ul>
<li>Use QMenu:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4746c6eea6d30fa63fa4e6de00054d7fc45915cc.png" data-download-href="/uploads/short-url/aaxxscrCjVJE0FcD6m1bIejDeoc.png?dl=1" title="QMenuTest" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4746c6eea6d30fa63fa4e6de00054d7fc45915cc_2_690x365.png" alt="QMenuTest" data-base62-sha1="aaxxscrCjVJE0FcD6m1bIejDeoc" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4746c6eea6d30fa63fa4e6de00054d7fc45915cc_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4746c6eea6d30fa63fa4e6de00054d7fc45915cc_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4746c6eea6d30fa63fa4e6de00054d7fc45915cc.png 2x" data-dominant-color="A3A2A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">QMenuTest</span><span class="informations">1366×724 62.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<pre><code class="lang-auto">#sliceViewMenu
toolButton = qt.QToolButton()
toolButton.setText('R')
slicer.app.layoutManager().sliceWidget("Red").sliceController().barLayout().insertWidget(0,toolButton)

myMenu = qt.QMenu(toolButton)
toolButton.setMenu(myMenu)

toolButton.setPopupMode(qt.QToolButton.InstantPopup)

widget = qt.QWidget()
layout = qt.QVBoxLayout(widget)
pushButtonPlus = qt.QPushButton('+',widget)
slider = qt.QSlider(widget)
pushButtonMinus = qt.QPushButton('-',widget)
layout.addWidget(pushButtonPlus)
layout.addWidget(slider)
layout.setAlignment(slider, qt.Qt.AlignHCenter)
layout.addWidget(pushButtonMinus)

widgetAction = qt.QWidgetAction(myMenu)
widgetAction.setDefaultWidget(widget)

myMenu.addAction(widgetAction)
</code></pre>
<p>But you can’t have more that one menu shown at a time. So this doesn’t work.</p>
<ul>
<li>Use ctkPopUpWidget (like the one on the pinButton of the sliceController) and set True to PinUp</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/431b984243a4e4a9a71f521c1f458945168c9557.png" data-download-href="/uploads/short-url/9zF6WCf14zK1y06rSOGnxgitfO7.png?dl=1" title="ctkPopUpWidgetTest" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/431b984243a4e4a9a71f521c1f458945168c9557_2_690x362.png" alt="ctkPopUpWidgetTest" data-base62-sha1="9zF6WCf14zK1y06rSOGnxgitfO7" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/431b984243a4e4a9a71f521c1f458945168c9557_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/431b984243a4e4a9a71f521c1f458945168c9557_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/431b984243a4e4a9a71f521c1f458945168c9557.png 2x" data-dominant-color="B1B1B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ctkPopUpWidgetTest</span><span class="informations">1366×718 64.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">ControllerLayout = slicer.app.layoutManager().sliceWidget("Yellow").sliceController().layout()

PopupWidget = ctk.ctkPopupWidget(slicer.app.layoutManager().sliceWidget("Yellow").sliceController())
PopupWidget.setSizePolicy(qt.QSizePolicy.Minimum, qt.QSizePolicy.Minimum)
ControllerLayout.addWidget(PopupWidget)
PopupWidget.setWindowFlags(PopupWidget.windowFlags() &amp; ~qt.Qt.ToolTip)

layout = qt.QVBoxLayout(PopupWidget)
pushButtonPlus = qt.QPushButton('+',PopupWidget)
slider = qt.QSlider(PopupWidget)
pushButtonMinus = qt.QPushButton('-',PopupWidget)
layout.addWidget(pushButtonPlus)
layout.addWidget(slider)
layout.setAlignment(slider, qt.Qt.AlignHCenter)
layout.addWidget(pushButtonMinus)
PopupWidget.pinPopup(True)
</code></pre>
<p>But the horizontalLayout the popup widget is in makes it as large as the sliceController widget. So this approach doesn’t work either.</p>
<p>There were <a href="https://stackoverflow.com/questions/50224587/approach-to-create-floating-box-ui-in-qt" rel="noopener nofollow ugc">suggestions</a> to derive the mainWindow class to change resizeEvent and moveEvent, or create a showDockWidgets function but I can’t follow them because the mainWindow is owned by Slicer. <a href="https://stackoverflow.com/questions/28147360/qt-widget-displayed-over-other-widgets" rel="noopener nofollow ugc">This one</a> may also be handy.</p>
<p><a href="https://qgis.org/api/3.4/classQgsFloatingWidget.html" rel="noopener nofollow ugc">QgsFloatingWidget</a> widget appears to describe what I need.</p>
<p>Any guidance regarding the implementation of this would be greatly appreciated.</p>

---

## Post #2 by @jamesobutler (2021-11-11 17:59 UTC)

<p>Floating QWidgets I think is something not primarily in the design structure for Qt. It seems like QWidgets are primarily designed to have a parent that is some QLayout and floating widgets don’t really have a layout parent. I can really only think about using actual <a href="https://doc.qt.io/qt-5/qdockwidget.html" rel="noopener nofollow ugc">QDockWidgets</a> such as the behavior of the Module panel area or the Python Interactor. Those are dock widgets which can be docked or set to float. They would float over the entire main window though and just over some specific widget like an individual slice view.</p>
<p>You showcase actions for</p>
<ul>
<li>Adjusting Window/Level</li>
<li>Panning the volume in the view</li>
<li>Zooming the volume in the view</li>
<li>Rotating the volume in the view</li>
<li>Flipping the volume in the view</li>
</ul>
<p>What are the motivations for the design of floating widgets?</p>
<ul>
<li>Is it to establish familiarity to the other program you showcase?</li>
<li>Is it not acceptable to use Slicer’s left module panel area for these actions? The other program simply doesn’t have a design with an area for other widgets so they have to be temporarily floated on top of the slice view.</li>
<li>Are you hiding the Slicer left module panel area to maximize the Slice viewers area which then requires you to float widgets on top of the slice views?</li>
<li>Is a 3 button mouse not being used which would otherwise support zoom/pan/etc actions without visible widgets?</li>
<li>Are you optimizing for a touch screen interface where a mouse is not present?</li>
</ul>

---

## Post #3 by @mau_igna_06 (2021-11-11 18:19 UTC)

<p>Can the containers (QDockWidget) be moved, if the mainWindow of Slicer is moved, automatically? or if it is resized adapt to that?</p>
<p>Another way could be to derive qMRMLSliceWidget and be set up the floating widget there. Can you give guidance regarding the implementation of this? I think I would need to remake all the layouts to use my_qMRMLSliceWidget also.</p>
<p>To answer your questions:</p>
<blockquote>
<p>Is it to establish familiarity to the other program you showcase?</p>
</blockquote>
<p>I think so.</p>
<blockquote>
<p>Is it not acceptable to use Slicer’s left module panel area for these actions? The other program simply doesn’t have a design with an area for other widgets so they have to be temporarily floated on top of the slice view.</p>
</blockquote>
<p>I think design is more comfortable to the users if they use a touchscreen</p>
<blockquote>
<p>Are you hiding the Slicer left module panel area to maximize the Slice viewers area which then requires you to float widgets on top of the slice views?</p>
</blockquote>
<p>The left module panel area is already used for the workflow. I will add the toolbar (left-side) that is shown in the images, that will steal little bit of space but is acceptable. We cannot have widgets for the showcase actions that are not floating over the views because there is not space.</p>
<blockquote>
<p>Is a 3 button mouse not being used which would otherwise support zoom/pan/etc actions without visible widgets?</p>
</blockquote>
<p>The GUI must be compatible with touchscreens and it would require users to buy specific hardware.</p>
<blockquote>
<p>Are you optimizing for a touch screen interface where a mouse is not present?</p>
</blockquote>
<p>Not optimizing but making it usable enough. So the software is good for mouse and good for touchscreen.</p>

---

## Post #4 by @jamesobutler (2021-11-11 18:29 UTC)

<p>It’s an interesting use case of Slicer if touch is the primary input. I don’t think a lot of Slicer design has considered this in the past.</p>
<p>Does the touchscreen support multi touch gestures? Or is it simple input only?</p>
<p>For example in the following linked post there is a video of pinch-to-zoom and rotating working which may avoid the need for individual buttons that do the same.</p>
<aside class="quote" data-post="1" data-topic="7557">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/touchscreen-and-trackpad-interactions/7557">Touchscreen and trackpad interactions</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Interaction with 2D and 3D views using touchscreen and MacOS trackpad is now included in the latest nightly release. 

If anyone has a chance to try them and would like to give feedback or suggestions, it would be appreciated.
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2021-11-12 05:27 UTC)

<p>On Windows, multitouch gestures work very well in 3D views to rotate, pan, zoom, spin. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> worked quite a lot on optimizing usability with a pen, too. On macOS, the rotate, pan, zoom, spin multitouch gestures are available on the touchpad.</p>
<p>It is a very interesting discussion. There are a number of projects where ease of use for newcomers is one of the most important design driver. For these cases, discoverability of the features via large, impossible-to-miss buttons is useful.</p>
<p>Rendering a Qt widget over a VTK render window will be always risky (may break with any VTK or Qt update), but it might work, so it is worth a try. We know that floating windows are problematic (the current floating window has problems with some window managers in certain situations - for example when alt-tabbing between applications). It would be much safer to add a button bar on the top or side of the render window.</p>
<p><a class="mention" href="/u/ungi">@ungi</a> you have implemented a few nice designs that addresses similar requirements. Could you tell about your experiences?</p>

---

## Post #6 by @ungi (2021-11-12 12:08 UTC)

<p>The solution I’ve seen from <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is to add a QToolButton to the view controller area, and then create a ctkPopupWidget with the tool button as parent. Then the popup widget does not span across the width of the view but shows floating like in the photos of <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>. This is the same as the pin button on the 3D views that pops up a floating widget and the size is limited to its contents.<br>
The problems are of course the same too. Sometimes the floating widget appears on the main monitor when Slicer is opened on the second monitor, they sometimes stay on the screen when Slicer is minimized, they show up earlier/later compared to the view, etc.<br>
These problems can be so annoying that in another project we added “floating” widgets on a widget that has the same background color as the view and positioned right above the view. So unless you have something behind the widgets in the view, it gives the impression that that the buttons are floating in the view. I know that’s not an ideal solution either, but it looks better.<br>
It would be nice if either Qt or VTK offered a stable solution to float widgets in views. It’s quite common in commercial applications. It is possible that those applications don’t have a stable solution either, but they have better control over what application is opened on what screen, they don’t switch between applications, and they keep underlying libraries on the same version.</p>

---

## Post #7 by @joanne40226 (2022-04-01 12:08 UTC)

<p>Hi, sorry to interrupt. I encountered the exactly same problem as you do. I wonder if the problem was fixed in the end? Thank you so much.</p>

---

## Post #8 by @mau_igna_06 (2022-04-01 13:42 UTC)

<p>It was done like it was explained here by Tamas</p>

---

## Post #9 by @apparrilla (2024-02-03 11:23 UTC)

<p>I want to add some toggle buttons just over 3dView to control some items visibility. It should be something similar but more simple as this.<br>
Qt is bit complex to me to manage and I undertand what <a class="mention" href="/u/ungi">@ungi</a> explain but I don´t know how to code it.<br>
Do you have any example to start with?</p>
<p>Thanks in advance!</p>

---

## Post #10 by @mau_igna_06 (2024-02-03 16:47 UTC)

<p>Maybe try combining a QToolButton with a QMenu</p>

---

## Post #11 by @apparrilla (2024-02-03 18:55 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> .</p>
<p>I get stacked getting the main widget of the 3DView to add the button.<br>
Following your code:</p>
<pre><code class="lang-auto">controllerWidget = slicer.app.layoutManager().threeDWidget(0).threeDController()
buttonLayout = slicer.util.findChild(controllerWidget, 'qMRMLThreeDViewControllerWidget').layout()
button = qt.QToolButton()
button.text="test"
buttonLayout.addWidget(button)
</code></pre>
<p>I get a button in the controllerWidget like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c1ba4db82cbeb09923b495939bd2a046d6ead63.png" alt="image" data-base62-sha1="aRhvUuxaLG5M9m4SwH2oqdJAz5h" width="282" height="129"></p>
<p>How should be possible to add it to the mainWidget? And how to manage its possition? I really don´t need to move from here any more, maybe just show/hide it.</p>

---

## Post #12 by @mau_igna_06 (2024-02-03 22:40 UTC)

<p>I think you are in a good path. You’ll get it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @apparrilla (2024-02-04 23:36 UTC)

<p>Ok, I´m near but not as good looking as I should like…</p>
<p>My version from <a class="mention" href="/u/ungi">@ungi</a>, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> (thanks to all of them):</p>
<pre><code class="lang-auto">mainWidget = slicer.app.layoutManager().threeDWidget(0)
bar = slicer.util.findChild(mainWidget, 'BarWidget')
popupLayout = qt.QVBoxLayout()
popupWidget = ctk.ctkPopupWidget(bar)
popupWidget.setLayout(popupLayout)
popupWidget.pinPopup(True)
popupWidget.setVisible(True)
popupWidget.setFixedWidth(80)

playButton = qt.QToolButton()
playButton.text=""
playButton.setCheckable(True)
#playButton.connect('clicked(bool)', self.onPlayButton)
playButton.setIcon(qt.QIcon('c://Icons/play.png'))
playButton.setAutoRaise(True)
playButton.setIconSize(qt.QSize(70, 70))
popupLayout.addWidget(playButton)

pauseButton = qt.QToolButton()
pauseButton.text=""
pauseButton.setCheckable(True)
#pauseButton.connect('clicked(bool)', self.onPauseButton)
pauseButton.setIcon(qt.QIcon('c://Icons/pause.png'))
pauseButton.setAutoRaise(True)
pauseButton.setIconSize(qt.QSize(70, 70))
popupLayout.addWidget(pauseButton)

stopButton = qt.QToolButton()
stopButton.text=""
stopButton.setCheckable(True)
#stopButton.connect('clicked(bool)', self.onStopButton)
stopButton.setIcon(qt.QIcon('c://Icons/stop.png'))
stopButton.setAutoRaise(True)
stopButton.setIconSize(qt.QSize(70, 70))
popupLayout.addWidget(stopButton)
</code></pre>
<p>Result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a1f48e109508e2cc39b32b7c566e70b55975948.png" data-download-href="/uploads/short-url/60D50V64XisiVjvt0k0X0okUhcs.png?dl=1" title="Captura de pantalla 2024-02-05 002404" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a1f48e109508e2cc39b32b7c566e70b55975948_2_267x500.png" alt="Captura de pantalla 2024-02-05 002404" data-base62-sha1="60D50V64XisiVjvt0k0X0okUhcs" width="267" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a1f48e109508e2cc39b32b7c566e70b55975948_2_267x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a1f48e109508e2cc39b32b7c566e70b55975948_2_400x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a1f48e109508e2cc39b32b7c566e70b55975948_2_534x1000.png 2x" data-dominant-color="6A6A6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-02-05 002404</span><span class="informations">534×997 31.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I liked to be a transparent panel so I tried:</p>
<pre><code class="lang-auto">popupWidget.setStyleSheet("QWidget {background-color: transparent;}")
</code></pre>
<p>But result was even worst</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d82581109610abd624742e3cbcece76908c040a3.png" data-download-href="/uploads/short-url/uQ7u7PqM1i8rmBHI7vXrsAG0JOP.png?dl=1" title="Captura de pantalla 2024-02-05 002557" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d82581109610abd624742e3cbcece76908c040a3_2_243x499.png" alt="Captura de pantalla 2024-02-05 002557" data-base62-sha1="uQ7u7PqM1i8rmBHI7vXrsAG0JOP" width="243" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d82581109610abd624742e3cbcece76908c040a3_2_243x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d82581109610abd624742e3cbcece76908c040a3_2_364x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d82581109610abd624742e3cbcece76908c040a3.png 2x" data-dominant-color="5D5E62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-02-05 002557</span><span class="informations">435×895 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea how to fix transparency?<br>
Should be possible to move it a bit down and right?<br>
If transparency is not feasible, could be a rounded panel?<br>
Sorry, but Qt is hard to me…<br>
Thanks in advance!</p>

---

## Post #14 by @ungi (2024-02-05 14:46 UTC)

<p>Hi, this works for me to have transparent background (look at the setAttribute function). I’m not sure if you need to move the pop-up widget. You could just add padding and that will create a margin around the buttons because of the transparent background. Note that you may need to change the style of the button in different states, if you want to control the background in checked button state.</p>
<pre><code class="lang-auto">mainWidget = slicer.app.layoutManager().threeDWidget(0)
bar = slicer.util.findChild(mainWidget, 'BarWidget')
popupLayout = qt.QVBoxLayout()
popupWidget = ctk.ctkPopupWidget(bar)
popupWidget.setLayout(popupLayout)
popupWidget.pinPopup(True)
popupWidget.setVisible(True)
popupWidget.setFixedWidth(80)
popupWidget.setAttribute(qt.Qt.WA_TranslucentBackground)
popupWidget.setStyleSheet("QWidget {background-color: transparent;}")
playButton = qt.QToolButton()
playButton.text=""
playButton.setCheckable(True)
playButton.setIcon(qt.QIcon('c://Icons/play.png'))
playButton.setAutoRaise(True)
playButton.setIconSize(qt.QSize(70, 70))
popupLayout.addWidget(playButton)
</code></pre>

---

## Post #15 by @apparrilla (2024-02-05 21:32 UTC)

<p>Wondwerfull! It looks pretty fine… Thanks so much <a class="mention" href="/u/ungi">@ungi</a> .</p>
<p>For manage margins, I´ve made:</p>
<pre><code class="lang-auto">popupLayout.setContentsMargins(40,10,0,0) # (left,up,right,down)

playButton.setStyleSheet("QWidget:hover {background-color: transparent; border: none; padding:5px}")
</code></pre>
<p>I just find a problem…<br>
When I make:</p>
<blockquote>
<p>slicer.util.mainWindow().<strong>showFullScreen</strong>()</p>
</blockquote>
<p>PopupWidget <strong>is not visible.</strong><br>
It looks to be in another layer because when I took exit button and slicer.util.confirmOkCancelDisplay is popup, I can see it…</p>
<p>Thanks in advance again…</p>

---

## Post #16 by @ungi (2024-02-05 23:31 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="15" data-topic="20584">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>PopupWidget <strong>is not visible.</strong></p>
</blockquote>
</aside>
<p>That is why these popup widgets are generally not recommended. These occlusion problems happen regularly. Most times it is possible to find a workaround. But I don’t have experience with frameless main window. I hope you will find a solution.</p>

---

## Post #17 by @lassoan (2024-02-10 18:56 UTC)

<p><code>showFullScreen</code> is a very special display mode, it completely changes the behavior of the application. If you just want your application to use the whole screen then it is better to resize it.</p>

---
