---
topic_id: 17490
title: "Findchild Is Not An Attribute"
date: 2021-05-06
url: https://discourse.slicer.org/t/17490
---

# `findChild` is not an attribute

**Topic ID**: 17490
**Date**: 2021-05-06
**URL**: https://discourse.slicer.org/t/findchild-is-not-an-attribute/17490

---

## Post #1 by @joachim (2021-05-06 10:54 UTC)

<p>I downloaded the latest build (<em>4.13.0-2021-05-04</em>) and now my <code>.slicerrc.py</code> is not working. This is because I’m trying to reach a button of <code>SegmentEditorWidget</code>:</p>
<pre><code>show3DButton = getModuleGui( 'SegmentEditor' ).findChild( 'ctkMenuButton', 'Show3DButton' )
</code></pre>
<p>Why does this happen? There is a <a href="https://doc.qt.io/qtforpython-5/PySide2/QtCore/QObject.html#PySide2.QtCore.PySide2.QtCore.QObject.findChild" rel="noopener nofollow ugc">findChild() method of QObject</a> (which the module widget should inherit from as far as I know). And it looks like <a href="https://github.com/Slicer/Slicer/search?l=Python&amp;q=findChild" rel="noopener nofollow ugc">Slicer is using findChild()</a> also. It did work with <em>4.13.0-2021-01-20</em></p>
<p><strong>PS:</strong> I see that <code>getModuleGui()</code> is deprecated in favour of <code>getModuleWidget()</code>, but that doesn’t work neither.</p>

---

## Post #2 by @cpinter (2021-05-06 12:44 UTC)

<p>Try <code>slicer.util.getModuleWidget('SegmentEditor')</code></p>
<p>Update: It won’t work either with your findChild, but this will:</p>
<p><code>slicer.util.getModuleWidget('SegmentEditor').editor.findChild( 'ctkMenuButton', 'Show3DButton' )</code></p>

---

## Post #3 by @joachim (2021-05-07 08:41 UTC)

<p>That worked. Thanks!</p>
<p>So it looks like the class <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Scripted/SegmentEditor/SegmentEditor.py#L38" rel="noopener nofollow ugc"><code>SegmentEditorWidget</code></a> implemented in Python is no longer a <code>QWidget</code>, but instead contain <a href="http://apidocs.slicer.org/master/classqSlicerSegmentationsModuleWidget.html" rel="noopener nofollow ugc"><code>qSlicerSegmentationsModuleWidget</code></a> as a member <code>editor</code>. What’s behind this change? It is strange that <code>getModuleWidget()</code> is not returning a (Q)widget (but it did so before).</p>
<p>Is there an API documentation of the Python interface to Slicer? It is not easy to understand how the classes are intended to work.</p>
<p>BTW, do the Python-implemented classes dropping the prefixes <em>vtk/mrml/q</em> etc. as the C++ classes have?</p>

---

## Post #4 by @cpinter (2021-05-07 09:45 UTC)

<p>The <code>SegmentEditorWidget</code> class has had the <code>editor</code> member since the <a href="https://github.com/Slicer/Slicer/commit/3ab0eab7cb41e23634c8f8f2b789b6531f0b6605">first commit</a>, so in that sense nothing changed. The reason for this difference is <a href="https://github.com/Slicer/Slicer/commit/96510eb8ea2f89345428fe032bf2924ba03299e7">this commit</a> in <code>slicer.util</code>, which for scripted module widgets returns the actual Python class instead of the C++ wrapper. The reason it worked for you is most probably that the Qt widgets in the editor module transitively had this C++ class as parent, however the Python widget class is not a QWidget.</p>
<p>I don’t think there is a complete Python API doc. You can use the C++ Doxygen in conjunction with the source code itself. And since Python works via interpreter, you can try everything first in Slicer’s Python interactor, and you can see what is available using the auto-complete function, and get documentation for the functions using <code>help(className.functionName)</code>.</p>

---

## Post #5 by @joachim (2021-05-14 11:40 UTC)

<p>Thank you! I’ve been using the C++ API (and source code) alot while learning Python scripting. Luckily I have a lot of C++ knowledge (but no Python, so I have actually learnt Python through Slicer <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:">).</p>
<p>It looks like the Python wrapping of C++ use the same naming and therefore prefixes <em>vtk</em>/<em>mrml</em>/<em>q</em>/<em>etc</em>). But are the Python-only classes like <code>SegmentEditorWidget</code> using no prefixes, so this is a way to differate between C++ and Python-only classes?</p>

---

## Post #6 by @cpinter (2021-05-14 12:45 UTC)

<p>I would say yes. As far as I know all C++ classes start with <code>vtk</code> or <code>q</code>, while all of the Python classes start with capital letter and generally without such prefix.</p>

---
