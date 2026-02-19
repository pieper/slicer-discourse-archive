---
topic_id: 44227
title: "Cannot Import Name Vtkmrmlpathplannertrajectorynode At Launc"
date: 2025-08-28
url: https://discourse.slicer.org/t/44227
---

# Cannot import name 'vtkMRMLPathPlannerTrajectoryNode' at launch

**Topic ID**: 44227
**Date**: 2025-08-28
**URL**: https://discourse.slicer.org/t/cannot-import-name-vtkmrmlpathplannertrajectorynode-at-launch/44227

---

## Post #1 by @ruffsl (2025-08-28 01:29 UTC)

<p>I have a working scripted extension that enables a user to select a path within any chosen trajectory list, as generated via the separate PathExplorer widget from the SlicerIGT extension:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead1f4331c75e1ab7319118d74978abb8e00fe1d.png" data-download-href="/uploads/short-url/xvjyeR3o8W8w6Pwdesc2FdTghhH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead1f4331c75e1ab7319118d74978abb8e00fe1d.png" alt="image" data-base62-sha1="xvjyeR3o8W8w6Pwdesc2FdTghhH" width="581" height="284"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">581×284 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/tree/master/PathExplorer" class="inline-onebox" rel="noopener nofollow ugc">SlicerIGT/PathExplorer at master · SlicerIGT/SlicerIGT · GitHub</a></li>
</ul>
<p>However, after passing tests and restarting Slicer, I noticed a new <code>ImportError</code> during launch:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/slicer/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/opt/air_ws/src/slicer/AirIGT/AirGUI/AirGUI.py", line 19, in &lt;module&gt;
    from slicer import (
ImportError: cannot import name 'vtkMRMLPathPlannerTrajectoryNode' from 'slicer' (/opt/slicer/bin/Python/slicer/__init__.py)
[Qt] loadSourceAsModule - Failed to load file "/opt/air_ws/src/air-sandbox/src/slicer/AirIGT/AirGUI/AirGUI.py"  as module "AirGUI" !
[Qt] Fail to instantiate module  "AirGUI"
[Qt] The following modules failed to be instantiated:
[Qt]    AirGUI
</code></pre>
<p>I import <code>vtkMRMLPathPlannerTrajectoryNode</code> from PathExplorer for Parameter node typing:</p>
<pre data-code-wrap="python"><code class="lang-python">from slicer import (
    vtkMRMLMarkupsLineNode,
    vtkMRMLNode,
    vtkMRMLPathPlannerTrajectoryNode,
    vtkMRMLScalarVolumeNode,
)
</code></pre>
<pre data-code-wrap="python"><code class="lang-python">@parameterNodeWrapper
class AirGUIParameterNode:
    inputPaths: vtkMRMLPathPlannerTrajectoryNode
</code></pre>
<p>Providing convent integration with nodeTypes &amp; SlicerParameterName for the pathsSelector UI:</p>
<pre data-code-wrap="xml"><code class="lang-xml">       &lt;widget class="qMRMLNodeComboBox" name="pathsSelector"&gt;
        &lt;property name="toolTip"&gt;
         &lt;string&gt;Pick input paths.&lt;/string&gt;
        &lt;/property&gt;
        &lt;property name="nodeTypes"&gt;
         &lt;stringlist notr="true"&gt;
          &lt;string&gt;vtkMRMLPathPlannerTrajectoryNode&lt;/string&gt;
         &lt;/stringlist&gt;
        &lt;/property&gt;
        &lt;property name="addEnabled"&gt;
         &lt;bool&gt;false&lt;/bool&gt;
        &lt;/property&gt;
        &lt;property name="removeEnabled"&gt;
         &lt;bool&gt;false&lt;/bool&gt;
        &lt;/property&gt;
        &lt;property name="SlicerParameterName" stdset="0"&gt;
         &lt;string&gt;inputPaths&lt;/string&gt;
        &lt;/property&gt;
       &lt;/widget&gt;
</code></pre>
<ul>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/blob/cc9678a9b6f91aa9ffde3ff0176cad357335616f/PathExplorer/Resources/UI/qSlicerPathExplorerModuleWidget.ui#L33" class="inline-onebox" rel="noopener nofollow ugc">SlicerIGT/PathExplorer/Resources/UI/qSlicerPathExplorerModuleWidget.ui at cc9678a9b6f91aa9ffde3ff0176cad357335616f · SlicerIGT/SlicerIGT · GitHub</a></li>
</ul>
<p>Perhaps this results from some race conditions or lazily loaded imports? I did try declaring my external extension dependencies and moving/delaying the offending imports to inside my <code>AirGUIParameterNode</code> class as a work around for this limitation, but no dice. <img src="https://emoji.discourse-cdn.com/twitter/game_die.png?v=14" title=":game_die:" class="emoji" alt=":game_die:" loading="lazy" width="20" height="20"></p>
<pre data-code-wrap="python"><code class="lang-python">class AirGUI(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("Air GUI")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Wizards")]
        self.parent.dependencies = [
            "OpenIGTLinkIF",
            "PathExplorer",
        ]
</code></pre>
<p>Any recommendation for scripted modules using <code>vtkMRML</code> types from external C++ extentions?<br>
Thanks!</p>

---

## Post #2 by @ruffsl (2025-10-09 02:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , any suggested workarounds? Perhaps some kind of manual typecasting?</p>

---
