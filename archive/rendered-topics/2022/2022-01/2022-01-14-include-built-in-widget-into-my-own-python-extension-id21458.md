---
topic_id: 21458
title: "Include Built In Widget Into My Own Python Extension"
date: 2022-01-14
url: https://discourse.slicer.org/t/21458
---

# Include built-in widget into my own Python extension

**Topic ID**: 21458
**Date**: 2022-01-14
**URL**: https://discourse.slicer.org/t/include-built-in-widget-into-my-own-python-extension/21458

---

## Post #1 by @CsatiZoltan (2022-01-14 03:30 UTC)

<p>Hi,</p>
<p>I want to develop a simple extension in Python. One step involves placing points on the 3D scene. I realized that the fiducial markup is perfect for my use case, so I want to add that icon, along with the logic it implements, into my own frame. The idea is to simply add the pushbutton widget<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b317f484fd202fd4d9155cef63b0aaf3728860.png" alt="fiducial" data-base62-sha1="2OgMfdDu7TSrBstX8NjKby2kOn6" width="71" height="31"><br>
and also the list that keeps track of the points the user creates:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9bf26f2e767b441315a2988f1aabf7df1b12426.png" alt="list" data-base62-sha1="sMJvOvAqyNe8A8BteGKNF2odLsa" width="599" height="180"><br>
but not the other markup tools (line markup, angle markup, etc.).<br>
Where can I find these two widgets? I looked for them in the <a href="https://apidocs.slicer.org/master/group__Slicer__QtModules__Markups.html" rel="noopener nofollow ugc">API docs</a> and in the <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Markups" rel="noopener nofollow ugc">source code folder</a>, but could not figure out how to import them as Python modules, so that I can use them from within Python.</p>
<p>Thanks,<br>
Zoltan</p>

---

## Post #2 by @mikebind (2022-01-14 22:59 UTC)

<p>Take a look at <a href="https://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html" class="inline-onebox">Slicer: qSlicerMarkupsPlaceWidget Class Reference</a>.  This widget can handle creating and selecting a fiducial node and toggling placement mode for points. One common stumbling point is that you need to set the mrml scene before the widget will be functional. This can be done in Qt Designer when you are setting up the UI by connecting the module widget’s <code>mrmlSceneChanged(vtkMRMLScene*)</code> signal to the MRML widget’s <code>setMRMLScene(vtkMRMLScene*)</code> slot.  Or it could be done in your module’s <code>setup</code> function.</p>

---

## Post #3 by @Lin (2022-01-15 12:35 UTC)

<p>That’s very useful to me. I’ll try on my projects.</p>

---

## Post #4 by @CsatiZoltan (2022-01-16 20:38 UTC)

<p>Thank you. Although I connected the proper signal to the proper slot, the widget is not activated. This is strange because the same workflow works for the <a href="https://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html" rel="noopener nofollow ugc"><code>qSlicerSimpleMarkupsWidget</code></a> widget.</p>
<p>More importantly, can I modify an already existing widget (e.g. by removing certain parts it) without recompilation? I am afraid I can’t because the <em>Markups</em> module is implemented in C++.</p>

---

## Post #5 by @mikebind (2022-01-18 18:48 UTC)

<p>Markups place widgets also require an active current markups node to be activated (sorry I omitted that in the first answer, I forgot!).  Here is an example of setting that:</p>
<pre><code class="lang-auto">myFiducialNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'F')
w = slicer.qSlicerMarkupsPlaceWidget()
w.setMRMLScene(slicer.mrmlScene)
w.show() # not active yet
w.setCurrentNode(myFiducialNode) # now it is active
</code></pre>
<aside class="quote no-group" data-username="CsatiZoltan" data-post="4" data-topic="21458">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/csatizoltan/48/13807_2.png" class="avatar"> CsatiZoltan:</div>
<blockquote>
<p>More importantly, can I modify an already existing widget (e.g. by removing certain parts it) without recompilation? I am afraid I can’t because the <em>Markups</em> module is implemented in C++.</p>
</blockquote>
</aside>
<p>You can control whether parts of the widget are shown or not from Python without recompilation.  All qt widgets have <code>hide()</code> and <code>show()</code> functions, so if you want to hide a part of the custom widget you just need to find that part and invoke its <code>hide()</code> method. For example, if you wanted to hide the color picker button, the following would work:</p>
<pre><code class="lang-auto"># w is the markups place widget we set up above
childrenList = w.children()
colorButton = childrenList[8] 
colorButton.hide()
</code></pre>
<p>I found that the color button was the child with index 8 by just inspecting the list of the widget’s children (I don’t know a more efficient way to do that and I’m not that familiar with Qt, but it is not very much work to look through the full list).</p>

---

## Post #6 by @lassoan (2022-01-19 02:54 UTC)

<p>Getting a button by index is very fragile. It is safer to retrieve a button object by name, for example:</p>
<pre><code class="lang-python">colorButton = slicer.util.findChild(w, 'ColorButton')
</code></pre>
<p>But the safest is to use the public API of the widget. For example, you can make the widget only show a place button like this:</p>
<pre><code class="lang-python">w.buttonsVisible = False
w.placeButton().show()
</code></pre>
<p>Not all the buttons are exposed on the public API. We could change that, but was not needed until now.</p>

---
