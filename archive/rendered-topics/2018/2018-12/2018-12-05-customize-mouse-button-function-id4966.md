---
topic_id: 4966
title: "Customize Mouse Button Function"
date: 2018-12-05
url: https://discourse.slicer.org/t/4966
---

# Customize mouse button function

**Topic ID**: 4966
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/customize-mouse-button-function/4966

---

## Post #1 by @Maciej84 (2018-12-05 08:02 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.9.0<br>
Expected behavior: Is it possible to change the default function of the mouse buttons?  In my clinical software right click and drag scrolls through the volume, while in 3Dslicer it zooms.  Would be great to be able to change these presets, rather than having to get used to several different interfaces.  Like wise, left-click and drag changes the windowing - which I hate because once I find a window that I’m happy with I generally don’t want it to change!</p>

---

## Post #2 by @pieper (2018-12-06 21:53 UTC)

<p>Hi -</p>
<p>Right now these functions are <a href="https://github.com/Slicer/Slicer/blob/7b289e7e64a9260df5e1f15eb20a00dc87e4f7a6/Libs/MRML/DisplayableManager/vtkSliceViewInteractorStyle.cxx" rel="nofollow noopener">hard coded in the interactor style code</a>.  It Should be possible to override this behavior with some python scripting, but there’s no GUI for it.  If you are interested in doing some programming let us know if you want ideas of how to get started.</p>
<p>One thing that you can do is lock the window/level for a Volume using the Volumes Module.  Not exactly what you asked for but it might help.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @brhoom (2018-12-06 22:14 UTC)

<p>Just a suggestion for future feature: to have number of customizations as themes that makes the interface looks and behaves similar to popular tools. I know some radiologists who do not like to use Slicer even for simple task like manual segmentation because it is not similar to what they use.</p>

---

## Post #4 by @Maciej84 (2018-12-11 11:50 UTC)

<p>Thanks Steve.  So looks like those mouse functions are fairly simply defined in that config file.  Was hoping that I could simply edit this file in notepad but clearly it’s not that simple!  Can’t even find such a file in my Slicer install directory.</p>
<p>Care to point me in the right direction?</p>

---

## Post #5 by @pieper (2018-12-15 16:50 UTC)

<aside class="quote no-group" data-username="Maciej84" data-post="4" data-topic="4966">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/6de8d8/48.png" class="avatar"> Maciej84:</div>
<blockquote>
<p>Care to point me in the right direction?</p>
</blockquote>
</aside>
<p>Note that I’m not saying this is a good idea, but if you want to experiment, you can do something like this in the python console:</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
rw = lm.sliceWidget('Red').sliceView().renderWindow()
style = vtk.vtkInteractorStyleUser()
rw.GetInteractor().SetInteractorStyle(style)
def cb(a,b):
  print(a,b)
style.AddObserver("AnyEvent", cb)
</code></pre>
<p>From there you can change the callback function (cb) to do whatever you want, using the Slicer code linked above as a guide.  Of course a lot of things will break if you do this <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>I suppose if this is becomes a common enough request we could add hooks to do things like easily filter events or remap key/mouse bindings.  Of course we’re reluctant because support and documentation could be much harder if everyone starts using different buttons.</p>

---

## Post #6 by @fbordignon (2020-01-29 13:49 UTC)

<p>Following this directions I’ve added custom actions just by adding a callback to a MouseWheelBackwardEvent instead of AnyEvent and not overriding the InteractorStyle.<br>
Thanks for the snippet.</p>
<p>In my case I wanted to distort the Y window scale if the shift key is pressed using the field of view:</p>
<pre><code>def cbBackward(interactorStyle,event):
  if interactorStyle.GetInteractor().GetShiftKey():
    fov = interactorStyle.GetSliceLogic().GetSliceNode().GetFieldOfView()
    interactorStyle.GetSliceLogic().GetSliceNode().SetFieldOfView(fov[0],fov[1]*1.2,fov[2]) 
</code></pre>
<p>and added the observer:</p>
<pre><code>interactorStyle = slicer.app.layoutManager().sliceWidget('Red').sliceView().sliceViewInteractorStyle()    
observeridbackward = interactorStyle.AddObserver("MouseWheelBackwardEvent", cbBackward)</code></pre>

---
