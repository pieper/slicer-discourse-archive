# qSlicerMarkupsPlaceWidget widget disappearing

**Topic ID**: 29956
**Date**: 2023-06-10
**URL**: https://discourse.slicer.org/t/qslicermarkupsplacewidget-widget-disappearing/29956

---

## Post #1 by @Patrick_Li (2023-06-10 04:19 UTC)

<p>I’m currently working on a custom Python scripted module. I’m currently trying to create a button that creates a module GUI that allows users to place control points to create a curve. The code I’m using is from the repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-button-to-module-gui-to-activate-control-point-placement" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#add-a-button-to-module-gui-to-activate-control-point-placement</a></p>
<p>However, when I press the button, a blank pop-up rapidly appears then disappears. Here’s a video of what happens, though the appearing/disappearing occurs too quickly to be seen.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6cd5e1a30147eaab083806c7b432d97b44a2758.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6cd5e1a30147eaab083806c7b432d97b44a2758.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6cd5e1a30147eaab083806c7b432d97b44a2758.mp4</a>
    </source></video>
  </div><p></p>
<p>The code for the button is in a function that I’ve connected to the button.</p>
<pre><code>    self.ui.addNodule.connect('clicked(bool)', self.onAddNodule)

def onAddNodule(self):
    """
    Run processing when user clicks "Add" button for Nodule.
    """
    result = qt.QInputDialog().getText(None, "Add Nodule", "Enter nodule name")
    if result != "" and not self.ui.noduleList.findItems(result, qt.Qt.MatchExactly):
        self.ui.noduleList.addItem(result)

    w = slicer.qSlicerMarkupsPlaceWidget()
    w.setMRMLScene(slicer.mrmlScene)
    markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsClosedCurveNode")
    w.setCurrentNode(slicer.mrmlScene.GetNodeByID(markupsNode.GetID()))
    # Hide all buttons and only show place button
    # w.buttonsVisible=False
    w.placeButton().show()

    w.show()
</code></pre>

---

## Post #2 by @Patrick_Li (2023-06-10 04:20 UTC)

<p>Notably, the markup appears in the subject hierarchy, showing that the code is executed.</p>

---

## Post #3 by @jamesobutler (2023-06-10 04:43 UTC)

<p>What you are experiencing is a general python behavior. You are creating an object such as a qSlicerMarkupsPlaceWidget and assigning it to a local variable within the scope of onAddNodule. Everything is executed in that function as you observe by the creation of the node and the showing of the place widget pop-up. Once it finishes executing it clears those local references which is why you immediately see the pop-up close.</p>
<p>I suggest that you search online for your preferred learning style as it relates to how python variables are used locally within functions or more globally across a class.</p>

---

## Post #4 by @pearsonm (2023-06-10 07:50 UTC)

<p>You can embed a qSlicerMarkupsPlaceWidget in your GUI. There is an example of this in LungCTSegmenter in the <a href="https://github.com/rbumm/SlicerLungCTAnalyzer#lung-ct-analyzer" rel="noopener nofollow ugc">Lung CT Analyzer</a> module.</p>

---
