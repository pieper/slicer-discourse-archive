---
topic_id: 10544
title: "Simple Way To Disable Data Probe For Some Modules"
date: 2020-03-04
url: https://discourse.slicer.org/t/10544
---

# Simple way to disable Data Probe for some modules

**Topic ID**: 10544
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/simple-way-to-disable-data-probe-for-some-modules/10544

---

## Post #1 by @giovform (2020-03-04 16:43 UTC)

<p>What would a good way to disable the Data Probe for some specific modules? Is there a utility function for that? Thank you!</p>

---

## Post #2 by @Sam_Horvath (2020-03-04 16:55 UTC)

<p>slicer.util has this function:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/ff1ddf56348592270badea02b0ecddfee23d9c7a/Base/Python/slicer/util.py#L2245" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ff1ddf56348592270badea02b0ecddfee23d9c7a/Base/Python/slicer/util.py#L2245" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/ff1ddf56348592270badea02b0ecddfee23d9c7a/Base/Python/slicer/util.py#L2245</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="2235" style="counter-reset: li-counter 2234 ;">
<li>def setApplicationLogoVisible(visible):</li>
<li>  """Show/hide application logo at the top of module panel."""</li>
<li>  widget = findChild(mainWindow(), "LogoLabel")</li>
<li>  widget.setVisible(visible)</li>
<li>
</li>
<li>def setModuleHelpSectionVisible(visible):</li>
<li>  """Show/hide Help section at the top of module panel."""</li>
<li>  modulePanel = findChild(mainWindow(), "ModulePanel")</li>
<li>  modulePanel.helpAndAcknowledgmentVisible = visible</li>
<li>
</li>
<li class="selected">def setDataProbeVisible(visible):</li>
<li>  """Show/hide Data probe at the bottom of module panel."""</li>
<li>  widget = findChild(mainWindow(), "DataProbeCollapsibleWidget")</li>
<li>  widget.setVisible(visible)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>which you can use with detecting when your module is entered/exited to hide the data probe.  This can be done by defining the enter() / exit() functions in your module.  See:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/2b25e080bce23609710ad87a82030d3fe01c4286/Modules/Scripted/SegmentEditor/SegmentEditor.py#L119" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/2b25e080bce23609710ad87a82030d3fe01c4286/Modules/Scripted/SegmentEditor/SegmentEditor.py#L119" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/2b25e080bce23609710ad87a82030d3fe01c4286/Modules/Scripted/SegmentEditor/SegmentEditor.py#L119</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="109" style="counter-reset: li-counter 108 ;">
<li>    if compositeNode.GetBackgroundVolumeID():</li>
<li>      return compositeNode.GetBackgroundVolumeID()</li>
<li>  # Use first background volume node in any of the displayed layouts</li>
<li>  for layoutName in layoutManager.sliceViewNames():</li>
<li>    compositeNode = self.getCompositeNode(layoutName)</li>
<li>    if compositeNode.GetForegroundVolumeID():</li>
<li>      return compositeNode.GetForegroundVolumeID()</li>
<li>  # Not found anything</li>
<li>  return None</li>
<li>
</li>
<li class="selected">def enter(self):</li>
<li>  """Runs whenever the module is reopened</li>
<li>  """</li>
<li>  if self.editor.turnOffLightboxes():</li>
<li>    slicer.util.warningDisplay('Segment Editor is not compatible with slice viewers in light box mode.'</li>
<li>      'Views are being reset.', windowTitle='Segment Editor')</li>
<li>
</li>
<li>  # Allow switching between effects and selected segment using keyboard shortcuts</li>
<li>  self.editor.installKeyboardShortcuts()</li>
<li>
</li>
<li>  # Set parameter set node if absent</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @giovform (2020-03-04 16:57 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="2" data-topic="10544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>def enter(self):</p>
</blockquote>
</aside>
<p>Thank you! Very simple.</p>

---

## Post #4 by @Tokai (2020-03-25 08:45 UTC)

<aside class="quote no-group quote-modified" data-username="Sam_Horvath" data-post="2" data-topic="10544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote></blockquote>
</aside>
<p>In the module panel you can disable and hide the help and acknowledgement section. Similarly for a active module, lets say ‘Landmarkregistration’ module, I want to hide the ‘local refinement’ and ‘Registration’, two collapsible frames. How can I do that?<br>
I understand somehow I have to find the name of those the widgets and then make visible false. But i could not find a way to find the names of those items.</p>

---
