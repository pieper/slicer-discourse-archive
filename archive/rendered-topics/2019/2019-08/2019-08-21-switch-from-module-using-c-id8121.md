---
topic_id: 8121
title: "Switch From Module Using C"
date: 2019-08-21
url: https://discourse.slicer.org/t/8121
---

# Switch from module using c++

**Topic ID**: 8121
**Date**: 2019-08-21
**URL**: https://discourse.slicer.org/t/switch-from-module-using-c/8121

---

## Post #1 by @rbahegne (2019-08-21 13:54 UTC)

<p>Hello,</p>
<p>Seems simple but i did not find how to switch module programatically.</p>
<p>Let’s say i receive a signal containing data, then i create a node, fill it correctly. How can switch automatically to the module “data” ?</p>
<p>Can I also change the node visibility ?</p>

---

## Post #2 by @lassoan (2019-08-21 15:50 UTC)

<p>In general, a module should not initiate switching to another module, as each module should implement a particular feature completely. If you are working on a module that performs a complex workflow then you can place all relevant widgets in your module GUI.</p>
<p>For example, if you want to show a data tree then you don’t switch to the data module, just add a data tree to the widget of your module:</p>
<pre><code class="lang-python">v = slicer.qMRMLSubjectHierarchyTreeView()
v.setMRMLScene(slicer.mrmlScene)
v.show()
</code></pre>
<p>You can customize what columns are shown in the tree, filter which items are displayed, define actions that are performed when the user selects an item, etc.</p>
<p>If you still think that switching modules is appropriate (e.g., at the end of your workflow), you can do what is done in the Welcome module:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SlicerWelcome/qSlicerWelcomeModuleWidget.cxx#L156-L180" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SlicerWelcome/qSlicerWelcomeModuleWidget.cxx#L156-L180" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/SlicerWelcome/qSlicerWelcomeModuleWidget.cxx#L156-L180</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="156" style="counter-reset: li-counter 155 ;">
<li>bool qSlicerWelcomeModuleWidgetPrivate::selectModule(const QString&amp; moduleName)</li>
<li>{</li>
<li>  Q_Q(qSlicerWelcomeModuleWidget);</li>
<li>  qSlicerModuleManager * moduleManager = qSlicerCoreApplication::application()-&gt;moduleManager();</li>
<li>  if (!moduleManager)</li>
<li>    {</li>
<li>    return false;</li>
<li>    }</li>
<li>  qSlicerAbstractCoreModule * module = moduleManager-&gt;module(moduleName);</li>
<li>  if(!module)</li>
<li>    {</li>
<li>    QMessageBox::warning(</li>
<li>          q, qSlicerWelcomeModuleWidget::tr("Raising %1 Module:").arg(moduleName),</li>
<li>          qSlicerWelcomeModuleWidget::tr("Unfortunately, this requested module is not available in this Slicer session."),</li>
<li>          QMessageBox::Ok);</li>
<li>    return false;</li>
<li>    }</li>
<li>  qSlicerLayoutManager * layoutManager = qSlicerApplication::application()-&gt;layoutManager();</li>
<li>  if (!layoutManager)</li>
<li>    {</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SlicerWelcome/qSlicerWelcomeModuleWidget.cxx#L156-L180" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @rbahegne (2019-10-07 14:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8121">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example, if you want to show a data tree then you don’t switch to the data module, just add a data tree to the widget of your module:</p>
<pre><code class="lang-auto">v = slicer.qMRMLSubjectHierarchyTreeView()
v.setMRMLScene(slicer.mrmlScene)
v.show()
</code></pre>
</blockquote>
</aside>
<p>Hello indeed maybe it’s the best solution, but i did not manage to get it work.</p>
<p>I added qMRMLSubjectHierarchyTreeView to my module widget but i couldn’t get to the actual dataTree. What would be a C++ equivalent of v = slicer.qMRMLSubjectHierarchyTreeView(), i did not found a tree view in qSlicerApplication::**** .</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2019-10-07 17:04 UTC)

<p>If you start Qt designer (<code>Slicer.exe --designer</code>) then qMRMLSubjectHierarchyTreeView should show up in the widget list and you can just drag-and-drop it into your GUI.</p>

---

## Post #5 by @rbahegne (2019-10-08 07:43 UTC)

<p>Yes, but my question was more about how connect my GUI treeview to the original data module one.</p>

---

## Post #6 by @lassoan (2019-10-08 11:45 UTC)

<p>There is no need to connect the widgets to each other, just set the scene in the widget.</p>

---

## Post #7 by @rbahegne (2019-10-08 14:18 UTC)

<p>OK, thank you it works nicely indeed.</p>

---
