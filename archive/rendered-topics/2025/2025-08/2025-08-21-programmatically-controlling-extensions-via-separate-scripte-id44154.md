---
topic_id: 44154
title: "Programmatically Controlling Extensions Via Separate Scripte"
date: 2025-08-21
url: https://discourse.slicer.org/t/44154
---

# Programmatically controlling extensions via separate scripted extension

**Topic ID**: 44154
**Date**: 2025-08-21
**URL**: https://discourse.slicer.org/t/programmatically-controlling-extensions-via-separate-scripted-extension/44154

---

## Post #1 by @ruffsl (2025-08-21 01:19 UTC)

<p>Is it possible to programmatically control the state of other 3D Slicer extensions via my own scripted extension using the python API? Such as trigger UI events or update their internal state?</p>
<p>E.g: when restoring Slicer from a saved MRML Scene, some extensions need manual prodding to resume operation, such as <code>SlicerOpenIGTLink</code> when activating an existing connection:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/Widgets/Resources/UI/qSlicerIGTLConnectorPropertyWidget.ui#L81-L83">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/Widgets/Resources/UI/qSlicerIGTLConnectorPropertyWidget.ui#L81-L83" target="_blank" rel="noopener nofollow ugc">github.com/openigtlink/SlicerOpenIGTLink</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/Widgets/Resources/UI/qSlicerIGTLConnectorPropertyWidget.ui#L81-L83" target="_blank" rel="noopener nofollow ugc">OpenIGTLinkIF/Widgets/Resources/UI/qSlicerIGTLConnectorPropertyWidget.ui</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/Widgets/Resources/UI/qSlicerIGTLConnectorPropertyWidget.ui#L81-L83" rel="noopener nofollow ugc"><code>f806007cc</code></a>
</div>



    <pre class="onebox"><code class="lang-ui">
      <ol class="start lines" start="81" style="counter-reset: li-counter 80 ;">
          <li>&lt;widget class="QCheckBox" name="ConnectorStateCheckBox"&gt;</li>
          <li> &lt;property name="text"&gt;</li>
          <li>  &lt;string&gt;Active&lt;/string&gt;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Or with <code>SlicerIGT</code> to enable Bullseye View Mode for multiple Scene Cameras:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L64-L65">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L64-L65" target="_blank" rel="noopener nofollow ugc">github.com/SlicerIGT/SlicerIGT</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L64-L65" target="_blank" rel="noopener nofollow ugc">Viewpoint/Viewpoint.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/Viewpoint/Viewpoint.py#L64-L65" rel="noopener nofollow ugc"><code>cc9678a9b</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="64" style="counter-reset: li-counter 63 ;">
          <li>self.toggleBullseyeButtonTextState0 = _("Enable Bullseye View Mode")</li>
          <li>self.toggleBullseyeButtonTextState1 = _("Disable Bullseye View Mode")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Rather than necessitating the user to navigate to there respective extension panels and enable these function after startup, I’d like to script a simple one click button to resume these behaviors.</p>
<hr>
<p>It also seems that the Vewpoint extension included in SlicerIGT doesn’t save all its own settings with the MRML Scene, so I’d like to re-initialize those camera control parameters as well.</p>
<p>I’m guessing I could rewrite these IGT features internal to my own extension, but I’d prefer to reuse the existing extensions for simpler user control override and existing interactive workflows.</p>

---

## Post #2 by @pieper (2025-08-21 17:35 UTC)

<p>Yes, it’s very common to interact with different modules, even ones that come from other extensions.  It’s best practice to interact through MRML and parameter nodes, but usually you can import the module and access the Logic classes.  If the module doesn’t expose parameter nodes or logic methods you can technically access the GUI but it’s not the way we like to do things.  If you are working on a longer term project you might propose changes to the modules you are using to have them expose the functionality you need.</p>

---

## Post #3 by @ruffsl (2025-08-21 19:28 UTC)

<p>Thanks for good pointers!</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="44154">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>best practice to interact through MRML and parameter nodes</p>
</blockquote>
</aside>
<p>Is there discovery process to inspect what parameter nodes are available through MRML?<br>
I.e. is there an option for Slicer to show what node my mouse is hovering over or interacting with?</p>
<p>I looked for anything related to <code>SlicerOpenIGTLink</code> or just <code>IGT</code>, and found:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; nodes = slicer.mrmlScene.GetNodes()
&gt;&gt;&gt; for node in nodes:
  print(node)
... 
vtkMRMLCrosshairNode (0x35d0b5f0)
  ID: vtkMRMLCrosshairNodedefault
  ClassName: vtkMRMLCrosshairNode
  Name: Crosshair
...
&gt;&gt;&gt; node = slicer.mrmlScene.GetFirstNodeByName('IGTLConnector')
&gt;&gt;&gt; print(node)
vtkMRMLIGTLConnectorNode (0x3cf120d0)
  ID: vtkMRMLIGTLConnectorNode1
  ClassName: vtkMRMLIGTLConnectorNode
  Name: IGTLConnector
  Debug: false
  MTime: 439420
  Description: (none)
  SingletonTag: (none)
  HideFromEditors: false
  Selectable: true
  Selected: false
  UndoEnabled: false
  Node references:
    incoming [incomingNodeRef]: vtkMRMLLinearTransformNode4 vtkMRMLLinearTransformNode5
    outgoing [outgoingNodeRef]: (none)
  Connector Type: CLIENT
  Server Hostname: localhost
  Server Port #: 18944
  State: CONNECTED
  Persistent: 0
  Restrict Device Name: 0
  Push Outgoing Message Flag: 0
  Check CRC: 1
  Number of outgoing nodes: 0
  Number of incoming nodes: 2
</code></pre>
<p>After using the internal python console as a REPEL, I found a working stop and start function:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; node.Stop()
1
&gt;&gt;&gt; node.Start()
1
[VTK] Connector is already running!
</code></pre>
<p>But where is this node interface documented or define in an extension codebase?<br>
Simply the header?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.h#L130-L133">
  <header class="source">

      <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.h#L130-L133" target="_blank" rel="noopener nofollow ugc">github.com/openigtlink/SlicerOpenIGTLink</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.h#L130-L133" target="_blank" rel="noopener nofollow ugc">OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/openigtlink/SlicerOpenIGTLink/blob/f806007ccc4b5c7cb6ea14979670a468b39c5a45/OpenIGTLinkIF/MRML/vtkMRMLIGTLConnectorNode.h#L130-L133" rel="noopener nofollow ugc"><code>f806007cc</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="130" style="counter-reset: li-counter 129 ;">
          <li></li>
          <li>int Start();</li>
          <li></li>
          <li>int Stop();</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>but usually you can import the module and access the Logic classes.</p>
</blockquote>
<p>Is that still feasible for a scripted extension when attempting to control a C++ extension?</p>
<p>In any case, I think I may have to do that for the <code>ViewpointInstance</code> class, as the extension is scripted, however I can’t find it among the MRML nodes while the Viewpoint extension is loaded and running.</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; nodes = slicer.mrmlScene.GetNodes()
&gt;&gt;&gt; for node in nodes:
  if 'viewpoint' in node.GetName().lower():
    print(node)
&gt;&gt;&gt; 
</code></pre>
<p>How should I go about getting a object handle for this extension class?</p>
<blockquote>
<p>If the module doesn’t expose parameter nodes or logic methods you can technically access the GUI but it’s not the way we like to do things.</p>
</blockquote>
<p>Understood. Although as a last resort, what would that look like in C++ &amp; Python for example?</p>
<blockquote>
<p>If you are working on a longer term project you might propose changes to the modules you are using to have them expose the functionality you need.</p>
</blockquote>
<p>Know of any reference PRs I could look at as an example? I’m still learning Slicer’s APIs and extension code layouts. Simply classes with a public <code>vtkMRMLNode</code> interface?</p>
<hr>
<p>In the short term, I’d also be fine with something like equivalent of an HTML iframe for QTM, where our custom extension could just render parts of another extension UI within its own pannel.</p>

---

## Post #4 by @pieper (2025-08-21 21:00 UTC)

<p>We try to make sure the core is reasonably documented (and even that’s hard) but the extensions can vary a lot.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">This documentation</a> describes a general method for exploring functionality, which is a few steps to follow but generally gets you to the right place in the source code.</p>
<p>It’s very common to use a widget from another module, but not all GUIs are broken out for easy reuse.</p>
<p>If you want to “drive the GUI” from a script you can look at how it’s done in the <a href="https://github.com/Slicer/Slicer/tree/main/Applications/SlicerApp/Testing/Python">SelfTests</a>, but again, that’s going to be fragile.</p>

---
