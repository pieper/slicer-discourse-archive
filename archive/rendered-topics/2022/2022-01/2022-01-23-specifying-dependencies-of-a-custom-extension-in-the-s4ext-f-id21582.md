---
topic_id: 21582
title: "Specifying Dependencies Of A Custom Extension In The S4Ext F"
date: 2022-01-23
url: https://discourse.slicer.org/t/21582
---

# Specifying dependencies of a custom extension in the .s4ext file

**Topic ID**: 21582
**Date**: 2022-01-23
**URL**: https://discourse.slicer.org/t/specifying-dependencies-of-a-custom-extension-in-the-s4ext-file/21582

---

## Post #1 by @koeglfryderyk (2022-01-23 16:21 UTC)

<p>I’m making a custom extension that contains the SimpleMarkupsWidget. Does this mean that my extension depends on the Markups module and I have to specify this as a dependency in the .s4ext file in my pull request?</p>

---

## Post #2 by @jamesobutler (2022-01-23 17:14 UTC)

<p>The .s4ext is describing build dependencies of the extension, but more specifically the other extensions that it depends upon. <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/lassoan">@lassoan</a> can confirm, but this comment in the .s4ext should probably be clarified to list the dependent extension names rather than the name of dependent modules.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Utilities/Templates/Extensions/extension_description.s4ext.in#L12-L15">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Utilities/Templates/Extensions/extension_description.s4ext.in#L12-L15" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Utilities/Templates/Extensions/extension_description.s4ext.in#L12-L15" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Utilities/Templates/Extensions/extension_description.s4ext.in#L12-L15</a></h4>



    <pre class="onebox">      <code class="lang-in">
        <ol class="start lines" start="12" style="counter-reset: li-counter 11 ;">
            <li># list dependencies</li>
            <li># - These should be names of other modules that have .s4ext files</li>
            <li># - The dependencies will be built first</li>
            <li>depends ${MY_EXTENSION_DEPENDS}</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Your extension contains modules and for a given module you will want to specify dependent modules in the same type section as shown below. This makes sure certain modules are loaded first during startup so your module can appropriately import various things it might need during initialization. As in this linked example, the Segment Editor module depends on the Segmentations module and Subject Hierarchy module. In your case, your module would depend on the Markups module.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Modules/Scripted/SegmentEditor/SegmentEditor.py#L16">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Modules/Scripted/SegmentEditor/SegmentEditor.py#L16" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Modules/Scripted/SegmentEditor/SegmentEditor.py#L16" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/11a0ed812e1d96c8945eff987d602093d003b9e3/Modules/Scripted/SegmentEditor/SegmentEditor.py#L16</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="6" style="counter-reset: li-counter 5 ;">
            <li>
            </li>
<li>#</li>
            <li># SegmentEditor</li>
            <li>#</li>
            <li>class SegmentEditor(ScriptedLoadableModule):</li>
            <li>  def __init__(self, parent):</li>
            <li>    ScriptedLoadableModule.__init__(self, parent)</li>
            <li>    import string</li>
            <li>    self.parent.title = "Segment Editor"</li>
            <li>    self.parent.categories = ["", "Segmentation"]</li>
            <li class="selected">    self.parent.dependencies = ["Segmentations", "SubjectHierarchy"]</li>
            <li>    self.parent.contributors = ["Csaba Pinter (Queen's University), Andras Lasso (Queen's University)"]</li>
            <li>    self.parent.helpText = """</li>
            <li>This module allows editing segmentation objects by directly drawing and using segmentaiton tools on the contained segments.</li>
            <li>Representations other than the labelmap one (which is used for editing) are automatically updated real-time,</li>
            <li>so for example the closed surface can be visualized as edited in the 3D view.</li>
            <li>"""</li>
            <li>    self.parent.helpText += parent.defaultDocumentationLink</li>
            <li>    self.parent.acknowledgementText = """</li>
            <li>This work is part of SparKit project, funded by Cancer Care Ontario (CCO)'s ACRU program</li>
            <li>and Ontario Consortium for Adaptive Interventions in Radiation Oncology (OCAIRO).</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
