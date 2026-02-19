---
topic_id: 424
title: "Synchronize Slice Views Widgets With Widgets Created In The"
date: 2017-06-02
url: https://discourse.slicer.org/t/424
---

# Synchronize slice views widgets with widgets created in the Python console

**Topic ID**: 424
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/synchronize-slice-views-widgets-with-widgets-created-in-the-python-console/424

---

## Post #1 by @Fernando (2017-06-02 13:24 UTC)

<p>Hi all,</p>
<p>I would like to use Python to synchronize a custom <code>qMRMLNodeComboBox</code> with, for example, the Foreground combo box of the Green slice view. Same thing with a slider for the opacity. So when I modify the node in my combo box, the green slice is modified and vice versa. I tried creating a <code>qMRMLSliceControllerWidget</code> as in the <code>View Controllers</code> module, but most methods seem not to be wrapped in Python. Do you have any ideas?</p>

---

## Post #2 by @lassoan (2017-06-02 14:06 UTC)

<p>Let me know what methods you would like to use and I can make sure those are Python-wrapped.</p>
<p>If you only need a simple node selector, then just add an observer to the slice node to get notification about volume selection changes.</p>

---

## Post #3 by @Fernando (2017-06-02 14:25 UTC)

<p>What I tried to do is mimic <a href="https://github.com/Slicer/Slicer/blob/ff4a605ef55fdda4fbd8c20cee41e4b184461f72/Modules/Loadable/ViewControllers/qSlicerViewControllersModuleWidget.cxx#L85" rel="nofollow noopener">this method</a> in <code>View Controllers</code>, but I guess it’s easier to add an observer to the slice node. How can I find out the right observer to add?</p>

---

## Post #4 by @lassoan (2017-06-02 14:32 UTC)

<p>Probably the best is to check the source code of the view controller widgets:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L751-L754" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L751-L754" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L751-L754</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="751" style="counter-reset: li-counter 750 ;">
<li>this-&gt;qvtkReconnect(this-&gt;MRMLSliceCompositeNode,</li>
<li>                    sliceComposite,</li>
<li>                    vtkCommand::ModifiedEvent,</li>
<li>                    this, SLOT(updateWidgetFromMRMLSliceCompositeNode()));</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
