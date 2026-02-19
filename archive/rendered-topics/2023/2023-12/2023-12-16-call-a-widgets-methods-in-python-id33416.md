---
topic_id: 33416
title: "Call A Widgets Methods In Python"
date: 2023-12-16
url: https://discourse.slicer.org/t/33416
---

# Call a widget's methods in Python

**Topic ID**: 33416
**Date**: 2023-12-16
**URL**: https://discourse.slicer.org/t/call-a-widgets-methods-in-python/33416

---

## Post #1 by @jhlegarreta (2023-12-16 20:03 UTC)

<p>Hello,</p>
<p>For the purposes of building a test, I am wondering whether there is a way to instantiate and call the methods from a class that inherits from <code>qSlicerWidget</code>​ (e.g. <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/Widgets/qSlicerTractographyDisplayWidget.h#L22" rel="noopener nofollow ugc"><code>qSlicerTractographyDisplayWidget</code>​</a>, which lives in <a href="https://github.com/SlicerDMRI/SlicerDMRI" rel="noopener nofollow ugc">SlicerDMRI</a>, and which has its Qt Designer UI file <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/Widgets/Resources/UI/qSlicerTractographyDisplayWidget.ui" rel="noopener nofollow ugc">here</a>) programmatically from Python.</p>
<p>I am able to do the below:</p>
<pre><code class="lang-auto">m = slicer.util.mainWindow()
m.moduleSelector().selectModule("TractographyDisplay")
display_widget = slicer.util.findChildren(name="qSlicerTractographyDisplayModuleWidget")[0]
</code></pre>
<p>but when trying to call any of the <code>qSlicerTractographyDisplayWidget</code> methods, e.g.:</p>
<pre><code class="lang-auto">opacity = display_widget.opacity()
display_widget.updateWidgetFromMRML()
</code></pre>
<p>it looks like I am querying the wrong object:</p>
<pre><code class="lang-auto">AttributeError: qSlicerTractographyDisplayWidget has no attribute named 'opacity'

AttributeError: qSlicerTractographyDisplayWidget has no attribute named 'updateWidgetFromMRML'
</code></pre>
<p>What am I missing?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-12-16 22:06 UTC)

<p>Hi - Qt methods are not wrapped by default.  Only things like slots and properties are available unless you put <code>Q_INVOKABLE</code> in front of the methods name you want to make available.</p>

---

## Post #3 by @jhlegarreta (2023-12-16 22:28 UTC)

<p>Thanks Steve.</p>
<p>Maybe I’m wrong, but calling a public slot, e.g. <code>setVisibility</code>:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/Widgets/qSlicerTractographyDisplayWidget.h#L54C8-L54C21">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/Widgets/qSlicerTractographyDisplayWidget.h#L54C8-L54C21" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/Widgets/qSlicerTractographyDisplayWidget.h#L54C8-L54C21" target="_blank" rel="noopener nofollow ugc">SlicerDMRI/SlicerDMRI/blob/master/Modules/Loadable/TractographyDisplay/Widgets/qSlicerTractographyDisplayWidget.h#L54C8-L54C21</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="54" style="counter-reset: li-counter 53 ;">
          <li>void setVisibility(bool);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>also results in the same error. Is there something else that I am missing?</p>

---

## Post #4 by @pieper (2023-12-17 11:57 UTC)

<p>There must be something wrong with either the wrapping or the way the wrapping libraries are being loaded in the extension.  You could look at how things work in the core, where QObject signals/slots/properties/invokables are available in python.  Maybe also look at other extensions that provide QObject/QWidget classes with wrapped methods.  It could be something in the way the cmake files are set up.</p>

---
