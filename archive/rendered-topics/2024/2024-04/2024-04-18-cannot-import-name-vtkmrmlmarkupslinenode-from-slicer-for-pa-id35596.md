---
topic_id: 35596
title: "Cannot Import Name Vtkmrmlmarkupslinenode From Slicer For Pa"
date: 2024-04-18
url: https://discourse.slicer.org/t/35596
---

# Cannot import name 'vtkMRMLMarkupsLineNode' from 'slicer' for ParameterNode definition

**Topic ID**: 35596
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/cannot-import-name-vtkmrmlmarkupslinenode-from-slicer-for-parameternode-definition/35596

---

## Post #1 by @arkhanna (2024-04-18 11:37 UTC)

<p>Hello Slicer community! I am trying to make a simple Slicer (5.6.2) extension that requires the user to select a markup line from a dropdown list. I use the Qt designer to create a qMRMLNodeComboBox and set nodeTypes to vtkMRMLMarkupsLineNode. The example extension .py file created by the Extension Wizard includes a section for “Parameter Node” specification (wrapped with <span class="mention">@parameterNodeWrapper</span>) that type checks input parameters. I specify that the inputVolume is of type vtkMRMLScalarVolumeNode with <code>inputVolume: vtkMRMLScalarVolumeNode</code>. The vtkMRMLScalarVolumeNode type is imported from slicer with from <code>slicer import vtkMRMLScalarVolumeNode</code>. This works as expected.</p>
<p>However, when I try to specify the type of another parameter inputLine of type vtkMRMLMarkupsLineNode with <code>inputLine: vtkMRMLMarkupsLineNode</code> and add vtkMRMLMarkupsLineNode to the slicer import statement, I get an error upon launching Slicer that says <code>Cannot import name 'vtkMRMLMarkupsLineNode' from 'slicer'</code>. What am I missing here?</p>

---

## Post #2 by @cpinter (2024-04-18 19:05 UTC)

<aside class="quote no-group" data-username="arkhanna" data-post="1" data-topic="35596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arkhanna/48/70085_2.png" class="avatar"> arkhanna:</div>
<blockquote>
<p>and add vtkMRMLMarkupsLineNode to the slicer import statement</p>
</blockquote>
</aside>
<p>I don’t think you need this. Simply use <code>slicer.vtkMRMLMarkupsLineNode</code>.</p>

---

## Post #3 by @mikebind (2024-04-19 00:16 UTC)

<p>What you tried should work.  Make sure that you don’t have any typos in the name;  I am forever accidentally typing <code>vkt</code> instead of <code>vtk</code>, or you might miss the <code>s</code> in <code>Markups</code>.  I doublechecked that there’s nothing funny about <code>vtkMRMLMarkupsLineNode</code> specifically:  the following imports without error for me on Slicer 5.6.1</p>
<pre><code class="lang-auto">from slicer import (
    vtkMRMLScalarVolumeNode, 
    vtkMRMLMarkupsROINode, 
    vtkMRMLMarkupsLineNode, 
    vtkMRMLMarkupsFiducialNode, 
    vtkMRMLSegmentationNode
)
</code></pre>
<p><a class="mention" href="/u/cpinter">@cpinter</a>’s suggestion should work equivalently well<br>
<code>inputLine: slicer.vtkMRMLMarkupsLineNode</code><br>
The import really just saves you having to type <code>slicer.</code> all the time.</p>

---
