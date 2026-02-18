# Question regarding error on initial launch of python extension, but not subsequent reloads of the same script

**Topic ID**: 24527
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/question-regarding-error-on-initial-launch-of-python-extension-but-not-subsequent-reloads-of-the-same-script/24527

---

## Post #1 by @Kevin.Kn (2022-07-27 16:38 UTC)

<p>I currently have a script that gives an error on open, or whenever I change the output image of the gui. Otherwise, after that first error and a reload, I can run the extension perfectly.</p>
<p>It results in the following error:</p>
<pre><code class="lang-auto">line 297, in updateParameterNodeFromGUI self._parameterNode.SetNodeReferenceID("noduleMarkupPlacementObj", self.ui.noduleSeedPlacementObject.currentNodeID)
AttributeError: qSlicerSimpleMarkupsWidget has no attribute named 'currentNodeID'
</code></pre>
<p>The lines regarding this code were based on the original example extension wizard python file, which does not give me the error on first launch of that code. I have my modified version of that code, in the same format, which Is why I am confused on the error message showing up on opening the extension, and when I am choosing/creating an output image.</p>
<p>The following four lines are the only time that currentNodeID is referenced.</p>
<pre><code class="lang-auto">  def updateParameterNodeFromGUI(self, caller=None, event=None):
    """
    This method is called when the user makes any change in the GUI.
    The changes are saved into the parameter node (so that they are restored when the scene is saved and loaded).
    """

    if self._parameterNode is None or self._updatingGUIFromParameterNode:
      return

    wasModified = self._parameterNode.StartModify()  # Modify all properties in a single batch

    self._parameterNode.SetNodeReferenceID("InputVolume", self.ui.inputSelector.currentNodeID)
    self._parameterNode.SetNodeReferenceID("OutputVolume", self.ui.outputSelector.currentNodeID)
    self._parameterNode.SetNodeReferenceID("noduleMarkupPlacementObj", self.ui.noduleSeedPlacementObject.currentNodeID)
    self._parameterNode.SetNodeReferenceID("backgroundMarkupPlacementObj", self.ui.backgroundSeedPlacementObject.currentNodeID)
</code></pre>
<p>Is it possibly throwing the error because the markup nodes havent been instantiated beacuse there has been no user input? If that is the case, what would be some suggestions to fix/make this more user friendly</p>
<p>Thanks in advance</p>

---
