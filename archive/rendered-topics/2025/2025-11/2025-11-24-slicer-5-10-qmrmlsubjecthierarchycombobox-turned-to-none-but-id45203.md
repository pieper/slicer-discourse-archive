---
topic_id: 45203
title: "Slicer 5 10 Qmrmlsubjecthierarchycombobox Turned To None But"
date: 2025-11-24
url: https://discourse.slicer.org/t/45203
---

# Slicer 5.10 qMRMLSubjectHierarchyComboBox turned to 'None' but no issue with 5.8.1

**Topic ID**: 45203
**Date**: 2025-11-24
**URL**: https://discourse.slicer.org/t/slicer-5-10-qmrmlsubjecthierarchycombobox-turned-to-none-but-no-issue-with-5-8-1/45203

---

## Post #1 by @chz31 (2025-11-24 05:53 UTC)

<p>Dear all,</p>
<p>In a new Extension I recently made <a href="https://github.com/chz31/SlicerOrbitSurgerySim" rel="noopener nofollow ugc">SlicerOrbitSurgerySim</a> (installable in Extension Manager in Slicer 5.10), when I run a function called <a href="https://github.com/chz31/SlicerOrbitSurgerySim/blob/f0c672fe00a5b5daf7aeb4ad984c073aaef5776c/PlateRegistration/PlateRegistration.py#L662" rel="noopener nofollow ugc">onInitialRegistrationPushButton</a> from the <a href="https://github.com/chz31/SlicerOrbitSurgerySim/blob/main/PlateRegistration/PlateRegistration.py" rel="noopener nofollow ugc">plateRegistration</a> module, the node selectors (<code>qMRMLSubjectHierarchyComboBox</code>) were set up to <code>None</code>, which then set all the connected parameterNode objects to <code>None</code>. <strong>However, I only encountered the issue in the new Slicer 5.10 and previous Slicer 5.9.1, not in Slicer 5.8.1.</strong></p>
<p>In the script, each <code>qMRMLSubjectHierarchyComboBox</code> is connected to a parameter node, which is also connect to a function for connecting to a parameter node and also enable/disable visualization.</p>
<p>For example, a fiducial selector below is connected to a function: <code>self.ui.orbitFiducialSelector.connect(“currentItemChanged(vtkIdType)”, self.onSelectOrbitLmNode)</code><br>
In the <code>onSelectOrbitLmNode</code> function, the object is then connect to a parameter node:</p>
<pre><code class="lang-auto">def onSelectOrbitLmNode(self):
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    try:
        orbitLmId = self.ui.orbitFiducialSelector.currentItem()
        self._parameterNode.orbitLm = shNode.GetItemDataNode(orbitLmId)
        self._parameterNode.orbitLm.GetDisplayNode().SetVisibility(True)
    except:
        pass
</code></pre>
<p>I found that, in <a href="https://github.com/chz31/SlicerOrbitSurgerySim/blob/f0c672fe00a5b5daf7aeb4ad984c073aaef5776c/PlateRegistration/PlateRegistration.py#L662" rel="noopener nofollow ugc">onInitialRegistrationPushButton</a> function, after creating a folder, and pass a parameterNode object into the folder (lines 704-711) like:</p>
<pre><code class="lang-auto">plateModelItem = self.folderNode.GetItemByDataNode(self._parameterNode.rigidRegisteredPlateModel)
self.folderNode.SetItemParent(plateModelItem, self.plateRegistrationFolder)
</code></pre>
<p>All <code>qMRMLSubjectHierarchyComboBox</code> would be set to <strong><code>None</code></strong>, and so did the parameterNode.</p>
<p>The current solution I found is to the UI signal by adding the below four lines before line 710 (i.e., before adding any item to the folder) in <a href="https://github.com/chz31/SlicerOrbitSurgerySim/blob/main/PlateRegistration/PlateRegistration.py#L390" rel="noopener nofollow ugc">plateRegistration.py</a>:</p>
<pre><code class="lang-auto">blockers = [
    qt.QSignalBlocker(self.ui.inputOrbitModelSelector),
    qt.QSignalBlocker(self.ui.orbitFiducialSelector),
    qt.QSignalBlocker(self.ui.plateModelSelector),
    qt.QSignalBlocker(self.ui.plateFiducialSelector),
]
</code></pre>
<p>It would be a bit difficult to directly debug the original module script. But it could be replicated by install SlicerOrbitSurgerySim from Extension Manager, restart Slicer, go to Sample Data, download the plateRegistration Sample Data and populate the combo boxes and click “initial registration”.</p>
<p><strong>I tried to create a demo module for replicate this issue</strong>, hopefully it recaptured the issue properly. <strong>Here is the</strong> <a href="https://drive.google.com/file/d/1mbbdnrAhIKQYUCexFb70UZEDMGWuM-Gw/view?usp=sharing" rel="noopener nofollow ugc">testing module</a><strong>.</strong></p>
<p><strong>To replicate, download the zipped module, install the demo extension in Slicer 5.10.0 using Extension Wizard.</strong></p>
<p><strong>After that, use the Markups module to create a point list, and click ‘Subject hierarchy folder test’ button at the very bottom (ignore everything else). You should see that the qt combo box at the first row changed to ‘None’.</strong></p>
<p>This shouldn’t be the case. This module simply select a markup node in the first row’s qtMRMLSubjectHierarchyComboBox <code>inputSelector</code> and pass it to a parameter node as below:</p>
<pre><code class="lang-auto"># Connections
self.ui.inputSelector.connect("currentItemChanged(vtkIdType)", self.onInputSelector)
self.ui.inputSelector.setMRMLScene(slicer.mrmlScene)
self.ui.inputSelector.setNodeTypes(['vtkMRMLMarkupsFiducialNode'])
</code></pre>
<pre><code class="lang-auto">def onInputSelector(self):
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    try:
        inputLmId = self.ui.inputSelector.currentItem()
        self._parameterNode.inputLM = shNode.GetItemDataNode(inputLmId)
        self._parameterNode.inputLM.GetDisplayNode().SetVisibility(True)
    except:
        pass
</code></pre>
<p>Afterwards, the subjectHierarchy folder test simply created a folder and pass <code>self._parameterNode.inputLM</code> into the folder.</p>
<pre><code class="lang-auto">def onShTestButton(self) -&gt; None:
    """
    Test for the bug: move a parameter-node-referenced node into a SubjectHierarchy folder
    and see if parameter node / selectors get reset to None.
    """
    print("\n=== SubjectHierarchy folder test ===")

    # Make sure we have a parameter node
    if not self._parameterNode:
        print("No parameter node yet; initializing.")
        self.initializeParameterNode()

    p = self._parameterNode

    # Ensure we have an input volume
    inputNode = p.inputLM
    if not inputNode:
        inputNode = self.ui.inputSelector.currentNode()
        if inputNode:
            p.inputLM = inputNode

    if not inputNode:
        print("ERROR: No input volume selected; cannot proceed with test.")
        return

    # Create a SubjectHierarchy folder and move the parameter node under it
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    sceneItemID = shNode.GetSceneItemID()

    folderName = "ParamNodeSHTestFolder"
    folderItemID = shNode.CreateFolderItem(sceneItemID, folderName)

    # print(f"Created folder item: {folderItemID} with name '{folderName}'")

    itemID = shNode.GetItemByDataNode(p.inputLM)

    shNode.SetItemParent(itemID, folderItemID)
    print(f'parameter node orbitLm check 7 {p.inputLM}')

</code></pre>
<p>In Slicer 5.10.0, the <code>qtMRMLSubjectHierarchyComboBox</code> would be turned to None.</p>
<p>What I found that disturbed the <code>qtMRMLSubjectHierarchyComboBox (inputSelector)</code> is probably due to the combox was connected to the <code>onInputSelector</code> function to connect it with a parameter node. If I disable the <code>onInputSelector</code> function at line 255 connected to the <code>inputSelector</code> as well as the connection at line 179, the combo box stopped switched to <code>None</code> anymore.</p>
<p>Again, in Slicer 5.8.1, there was no such issue.</p>
<p>Sorry, the explanation and error replication is lengthy. I could not find a shorter way to explain it. Also, interestingly, this error only appeared at the first run. If I ran the same module in the same scene again, the issue would not occur.</p>
<p>Thanks for looking at it!</p>

---

## Post #2 by @cpinter (2025-12-02 10:01 UTC)

<p>This might be an important issue, but you probably don’t get reactions because nobody here has time to process this really long message with the loose snippets. I have to admit that I don’t…</p>
<p>Please share a self-contained script that makes it easy to understand and reproduce the issue with the latest Slicer and one of us will probably investigate. Thank you!</p>

---

## Post #3 by @chz31 (2025-12-04 04:56 UTC)

<p>Thanks for pointing it out! Yes, I realized that it was indeed too long. The potential bug is a little weird, so I tried to add a bit background.</p>
<p>Basically, my original module created a subject hierarchy folder than add a parameter node under it. It then switched the qtMRMLSubjectHierarchy combo boxes linked to all parameter nodes to <code>None</code>, thus cleared those nodes. The issue only occurred in Slicer 3.10, not 3.8.1.</p>
<p><strong>Here is the</strong> <a href="https://drive.google.com/file/d/1mbbdnrAhIKQYUCexFb70UZEDMGWuM-Gw/view?usp=sharing" rel="noopener nofollow ugc">testing module</a> modified from the default Extension Wizard extension. I hope this one could recapture the bug.</p>
<p><strong>To replicate:</strong></p>
<ol>
<li>Download the zipped module (<a href="https://drive.google.com/file/d/1mbbdnrAhIKQYUCexFb70UZEDMGWuM-Gw/view?usp=sharing" rel="noopener nofollow ugc">link</a>), install the demo extension in Slicer 5.10.0 using Extension Wizard.</li>
<li>Switch to <code>test_paramNode</code> extension.</li>
<li>Use the Markups module to create a point list (could be an empty one),</li>
<li>Then select the markup node (default ‘F’ in the below screenshot) in the ‘input volume’ row (the first row; sorry I forgot to change the text), which is a <code>qtMRMLSubjectHierarchyComboBox</code>.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0077fbc7ec45c3d391b2addcf070e53fe3bcf142_2_690x82.png" alt="image" data-base62-sha1="493W6VnehNK1CpbsuCO8lkuxJE" width="690" height="82" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0077fbc7ec45c3d391b2addcf070e53fe3bcf142_2_690x82.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0077fbc7ec45c3d391b2addcf070e53fe3bcf142.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0077fbc7ec45c3d391b2addcf070e53fe3bcf142.png 2x" data-dominant-color="E7E8E9"></p>
<ol start="5">
<li>Ignore all other entries. Click the <code>‘SubjectHierarchy folder test’</code> button at the bottom.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a71dda665ebd428c6fb66219bd5f26f86520d5e4.png" alt="image" data-base62-sha1="nQnHfx4yJ4g7JbaWoSKY5FXG3OY" width="446" height="81"></p>
<ol start="6">
<li>You should see the ‘input Volume’ row that you selected the markup node turned to <code>None</code>.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0067496af83e0eaca8d93be5ef6fa21044bcae2c_2_690x88.png" alt="image" data-base62-sha1="3zi2jgNXpkZV0U4DmH7rmwROPO" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/0067496af83e0eaca8d93be5ef6fa21044bcae2c_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0067496af83e0eaca8d93be5ef6fa21044bcae2c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0067496af83e0eaca8d93be5ef6fa21044bcae2c.png 2x" data-dominant-color="E9EAEA"></p>
<p>################### Explanation ########################</p>
<p>However, this should not be the case.</p>
<p>This module simply created a folder ‘ParamNodeSHTestFolder’, pass the markup node to a parameter node, and save it under the folder (switch to the Data module you could see something like below):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/267a55181ac0b93407766dd98d8ecbd4e46b82b1_2_690x53.png" alt="image" data-base62-sha1="5uoeRUYW135fZy169TXVIingoO5" width="690" height="53" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/267a55181ac0b93407766dd98d8ecbd4e46b82b1_2_690x53.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/267a55181ac0b93407766dd98d8ecbd4e46b82b1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/267a55181ac0b93407766dd98d8ecbd4e46b82b1.png 2x" data-dominant-color="FCFBFB"></p>
<p>Here are the lines (255-262 in <code>test_paramNode.py</code> in the downloaded extension) pass the Markup node to the parameter node:</p>
<pre><code class="lang-auto">def onInputSelector(self):
    shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    try:
        inputLmId = self.ui.inputSelector.currentItem()
        self._parameterNode.inputLM = shNode.GetItemDataNode(inputLmId)
        self._parameterNode.inputLM.GetDisplayNode().SetVisibility(True)
    except:
        pass
</code></pre>
<p>Here are the lines (314-325 <code>test_paramNode.py</code>) that added the selected Markup node to the created folder ‘ParamNodeSHTestFolder’</p>
<pre><code class="lang-auto">p = self._parameterNode
# Create a SubjectHierarchy folder and move thresholdedVolume under it
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
    sceneItemID = shNode.GetSceneItemID()

folderName = "ParamNodeSHTestFolder"
folderItemID = shNode.CreateFolderItem(sceneItemID, folderName)

#Add to folder
itemID = shNode.GetItemByDataNode(p.inputLM)
shNode.SetItemParent(itemID, folderItemID)
</code></pre>
<p>Hope this clearer. Thanks for looking at the issue!</p>

---

## Post #4 by @cpinter (2025-12-15 11:01 UTC)

<p>I understand more or less, but reproducing the issue is still quite complicated (need to download stuff, dig the relevant parts in a larger file etc.).</p>
<p>Sorry but if it’s not too much to ask, could you please provide a simple self-containing example? A code snippet that I can paste into the python console. That snippet can simply show the selector in a new window, it doesn’t need to be part of a module. Thank you so much!</p>

---

## Post #5 by @chz31 (2025-12-22 17:34 UTC)

<p>Sorry for the late response. Thank you very much for your advice and time!</p>
<p>Yes. Initially, I could not repeat the same bug directly in the Python console but only in an extension. After some tests, the snippet finally worked and could repeat the same issue:</p>
<p>To run with the snippet below, in a <strong>fresh Slicer 5.10 scene</strong>,</p>
<ol>
<li>Create a markup fiducial node</li>
<li>Copy-paste the below snippet in the Python console,</li>
<li>In the pop-up GUI, select the node in the combo box, and click the button below it.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18969db1e0c28a7944d6cd266ee2aeed03a25aec.png" data-download-href="/uploads/short-url/3vw9sumMTB4URS0fzqMwI0XG2Di.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18969db1e0c28a7944d6cd266ee2aeed03a25aec.png" alt="image" data-base62-sha1="3vw9sumMTB4URS0fzqMwI0XG2Di" width="357" height="146"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">477×195 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><span class="hashtag-raw">#Copy-paste</span> below snippet in the Python console:</p>
<pre><code class="lang-auto">import slicer, qt
from slicer.parameterNodeWrapper import parameterNodeWrapper

@parameterNodeWrapper
class SHTestParameters:
    selectedFiducial: slicer.vtkMRMLMarkupsFiducialNode

dialog = qt.QDialog(slicer.util.mainWindow())
dialog.setWindowTitle("SHComboBox move -&gt; GUI reset -&gt; Param wipe test")
layout = qt.QVBoxLayout(dialog)

shComboBox = slicer.qMRMLSubjectHierarchyComboBox()
shComboBox.nodeTypes = ["vtkMRMLMarkupsFiducialNode"]
shComboBox.noneEnabled = True
shComboBox.setMRMLScene(slicer.mrmlScene)

layout.addWidget(qt.QLabel("Select a fiducial (SubjectHierarchyComboBox):"))
layout.addWidget(shComboBox)

runButton = qt.QPushButton("Move selected node into folder (triggers reset)")
layout.addWidget(runButton)

parameterNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScriptedModuleNode", "SHCombo_ParamNode_Test")
parameter = SHTestParameters(parameterNode)

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

def printState(tag):
    print(f"\n[{tag}]")
    print("  shComboBox.currentItem():", shComboBox.currentItem())
    print("  shComboBox.currentNode():", shComboBox.currentNode())
    print("  parameter.selectedFiducial:", parameter.selectedFiducial)

# sync combo box to the parameter node similar to the original module
def onComboChanged(itemId):
    node = shNode.GetItemDataNode(itemId)
    parameter.selectedFiducial = node
    printState("Combo changed (GUI-&gt;param sync fired)")

shComboBox.connect("currentItemChanged(vtkIdType)", onComboChanged)

#Add the parameter node to a folder
def onRun():
    currentItemID = shComboBox.currentItem()
    if currentItemID == 0:
        print("No selection (currentItemID==0)")
        return

    # seed parameter node explicitly (like your "store orbitLm/plateLm first")
    parameter.selectedFiducial = shNode.GetItemDataNode(currentItemID)

    printState("BEFORE MOVE")

    folderItemID = shNode.CreateFolderItem(shNode.GetSceneItemID(), "SHCombo_TestFolder")
    shNode.SetItemParent(currentItemID, folderItemID)

    printState("AFTER MOVE (post SetItemParent)")

runButton.connect("clicked()", onRun)

dialog.show()
dialog.raise_()
dialog.activateWindow()


</code></pre>
<p>You should see that the node is put under a newly created folder, but the comboBox is reset to ‘None’</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23c40b0573f27914f6b5dde26aeaba1673959fd6.png" data-download-href="/uploads/short-url/56oJmUFew7zUVPXiKNzEsFv3QlU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23c40b0573f27914f6b5dde26aeaba1673959fd6.png" alt="image" data-base62-sha1="56oJmUFew7zUVPXiKNzEsFv3QlU" width="477" height="195"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">477×195 20.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In Python console, you should see parameter node set to None because the parameter node is synced with the combobox by <code>def onComboChanged</code> the as in the original module:</p>
<pre><code class="lang-auto">[AFTER MOVE (post SetItemParent)]
shComboBox.currentItem(): 0
shComboBox.currentNode(): None
parameter.selectedFiducial: None
</code></pre>
<p>Interestingly, in the same scene, when I simply ran the same function again, the combobox did not set to ‘None’ afterwards. The error only happened when run the function first time in a fresh Slicer scene.</p>
<p>Let me know if this one works.</p>

---

## Post #6 by @cpinter (2026-01-16 14:29 UTC)

<p>Thank you so much! Sorry for the long delay I’ll look at this asap.</p>

---

## Post #7 by @chz31 (2026-01-20 15:56 UTC)

<p>Thanks! I will also ask you during the PW as well.</p>

---

## Post #8 by @cpinter (2026-01-28 13:04 UTC)

<p>Here is a shortened version of your snippet that reproduces the issue the same way. It seems that the parameter node is not related to the bug. My theory is that it is an update issue in SH model, where the selection is cleared on reparenting the current item.</p>
<pre><code class="lang-auto">import slicer, qt

dialog = qt.QDialog(slicer.util.mainWindow())
layout = qt.QVBoxLayout(dialog)

shComboBox = slicer.qMRMLSubjectHierarchyComboBox()
shComboBox.nodeTypes = ["vtkMRMLMarkupsFiducialNode"]
shComboBox.noneEnabled = True
shComboBox.setMRMLScene(slicer.mrmlScene)

layout.addWidget(qt.QLabel("Select a fiducial (SubjectHierarchyComboBox):"))
layout.addWidget(shComboBox)

runButton = qt.QPushButton("Move selected node into folder (triggers reset)")
layout.addWidget(runButton)

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)

def printState(tag):
    print(f"\n[{tag}]")
    print("  shComboBox.currentItem():", shComboBox.currentItem())
    print("  shComboBox.currentNode():", repr(shComboBox.currentNode()))  

# Add the parameter node to a folder
def onRun():
    currentItemID = shComboBox.currentItem()
    if currentItemID == 0:
        print("No selection (currentItemID==0)")
        return

    printState("BEFORE MOVE")

    folderItemID = shNode.CreateFolderItem(shNode.GetSceneItemID(), "SHCombo_TestFolder")
    shNode.SetItemParent(currentItemID, folderItemID)

    printState("AFTER MOVE (post SetItemParent)")

runButton.clicked.connect(onRun)

dialog.show()
</code></pre>

---

## Post #9 by @cpinter (2026-01-28 15:00 UTC)

<p>Fix proposed in PR <a href="https://github.com/Slicer/Slicer/pull/9009" class="inline-onebox">BUG: Maintain selection in subject hierarchy after reparenting item by cpinter · Pull Request #9009 · Slicer/Slicer · GitHub</a></p>

---
