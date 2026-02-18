# How to hold a displaynode using python?

**Topic ID**: 34865
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/how-to-hold-a-displaynode-using-python/34865

---

## Post #1 by @ebin1234 (2024-03-13 12:57 UTC)

<p>Hello, I have a doubt in holding a displaynode using python. I have two buttons and two displaynodes… Each button set visibility of each displaynode.I press first button. It will set visibility of corresponding display node and hold it.Then  I press second button it will display both nodes.</p>

---

## Post #2 by @cpinter (2024-03-13 13:16 UTC)

<p>Your code is obviously not correct. However, without providing the code itself, nobody has a chance to help you.</p>

---

## Post #3 by @ebin1234 (2024-03-13 13:34 UTC)

<p>Hello, this is code contain three functions for three buttons and I have to hold the visibility of node after pressing each button . Here I used displaynode.hold(True). But it is not giving proper result.</p>
<pre data-code-wrap="python"><code class="lang-python">def showTransparentRendering(self, volumeNode, maxOpacity, gradientThreshold):
        """Make constant regions transparent and the entire volume somewhat transparent
        :param maxOpacity: lower value makes the volume more transparent overall
            (value is between 0.0 and 1.0)
        :param gradientThreshold: regions that has gradient value below this threshold will be made transparent
            (minimum value is 0.0, higher values make more tissues transparent, starting with soft tissues)
        """
        # Get/create volume rendering display node
        volRenLogic = slicer.modules.volumerendering.logic()
        displayNode = volRenLogic.GetFirstVolumeRenderingDisplayNode(volumeNode)
        if not displayNode:
            displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
        # Set up gradient vs opacity transfer function
        gradientOpacityTransferFunction = displayNode.GetVolumePropertyNode().GetVolumeProperty().GetGradientOpacity()
        gradientOpacityTransferFunction.RemoveAllPoints()
        gradientOpacityTransferFunction.AddPoint(300.0, 0.0)
        gradientOpacityTransferFunction.AddPoint(3070.0, maxOpacity)
        gradientOpacityTransferFunction.AddPoint(gradientThreshold+1, maxOpacity)
        TransferFunction=displayNode.GetVolumePropertyNode().GetVolumeProperty().GetScalarOpacity()
        TransferFunction.RemoveAllPoints()
        TransferFunction.AddPoint(300.0, 0.0)
        TransferFunction.AddPoint(3070.0, maxOpacity)
        TransferFunction.AddPoint(gradientThreshold+1, maxOpacity)
        displayNode.SetVisibility(True) 

    def onpushButton(self) -&gt; None:
        """
        Run processing when user clicks "First Rendering" button.

        Calling update_parameters fuction for updating display of r1,r2,r3 parameters.

        Parameters:
                 r1:float
                 r2:float
                 r3:float
                 

        """
   
        self.logic.process_1(self.ui.inputSelector)
        
        """ Storing corresponding nodes in r1,r2,r3 parameters."""
        r1 = slicer.mrmlScene.GetFirstNodeByName('220074_pelvis')
        r2 = slicer.mrmlScene.GetFirstNodeByName('220074_knee')
        r3 = slicer.mrmlScene.GetFirstNodeByName("220074_ankle")
       
        """ Setting current node to r1."""
        self.ui.inputSelector.setCurrentNode(r1)
        volRenLogic1 = slicer.modules.volumerendering.logic()
        displayNode1 = volRenLogic1.CreateDefaultVolumeRenderingNodes(r1)
        displayNode1.hold(True)
        volumePropertyNode = displayNode1.GetVolumePropertyNode()
        preset = volRenLogic1.GetPresetByName('CT-AAA')
        volumePropertyNode.Copy(preset)
        self.showTransparentRendering(r1, 1,300.0)
  

        """  Accessing the volume rendering module.
             Creating a display node. 
             Setting visibility of corresponding node.
        """
        volRenLogic2 = slicer.modules.volumerendering.logic()
        displayNode2 = volRenLogic2.CreateDefaultVolumeRenderingNodes(r2)
        displayNode2.SetVisibility(False)
        """  Accessing the volume rendering module.
             Creating a display node. 
             Setting visibility of corresponding node.
        """
        volRenLogic3 = slicer.modules.volumerendering.logic()
        displayNode3 = volRenLogic3.CreateDefaultVolumeRenderingNodes(r3)
        displayNode3.SetVisibility(False)

     
    
        """ Center and fit displayed content in 3D view in the direction of anterior position."""
        view = slicer.app.layoutManager().threeDWidget(0).threeDController()
        view.resetFocalPoint()
        view.lookFromAxis(ctk.ctkAxesWidget.Anterior)
        view.setOrthographicModeEnabled(True)
     

        
    def onpushButton_2(self) -&gt; None:
        """
        Run processing when user clicks "second Rendering" button.

        Calling update_parameters fuction for updating display of r1,r2,r3 parameters.

        Parameters:
                 r1:float
                 r2:float
                 r3:float
                 

        """
        
 
        self.logic.process_2(self.ui.inputSelector_1)

        """ Storing corresponding nodes in r1,r2,r3 parameters."""
        r1 = slicer.mrmlScene.GetFirstNodeByName('220074_pelvis')
        r2 = slicer.mrmlScene.GetFirstNodeByName('220074_knee')
        r3 = slicer.mrmlScene.GetFirstNodeByName("220074_ankle")
        """ Setting current node to r2."""
        self.ui.inputSelector_1.setCurrentNode(r2)
        volRenLogic2 = slicer.modules.volumerendering.logic()
        displayNode2 = volRenLogic2.CreateDefaultVolumeRenderingNodes(r2)
        displayNode2.hold(True)
        volumePropertyNode = displayNode2.GetVolumePropertyNode()
        preset = volRenLogic2.GetPresetByName('CT-AAA')
        volumePropertyNode.Copy(preset)
        self.showTransparentRendering(r2, 1, 300.0)
       
     
        """  Accessing the volume rendering module.
             Creating a display node. 
             Setting visibility of corresponding node.
        """
        volRenLogic1 = slicer.modules.volumerendering.logic()
        displayNode1 = volRenLogic1.CreateDefaultVolumeRenderingNodes(r1)
        displayNode1.SetVisibility(False)
        """  Accessing the volume rendering module.
             Creating a display node. 
             Setting visibility of corresponding node.
        """
        volRenLogic3 = slicer.modules.volumerendering.logic()
        displayNode3 = volRenLogic3.CreateDefaultVolumeRenderingNodes(r3)
        displayNode3.SetVisibility(False)
     
        """ Center and fit displayed content in 3D view in the direction of anterior position."""
        view1 = slicer.app.layoutManager().threeDWidget(0).threeDController()
        view1.resetFocalPoint()
        view1.lookFromAxis(ctk.ctkAxesWidget.Anterior)
        view1.setOrthographicModeEnabled(True)
   
       

        
  
        
    
    def onpushButton_3(self) -&gt; None:
        """
        Run processing when user clicks "Third Rendering" button.

        Calling update_parameters fuction for updating display of r1,r2,r3 parameters.

        Parameters:
                 r1:float
                 r2:float
                 r3:float
                 

        """

 
        self.logic.process_3(self.ui.inputSelector_2)
        
        """ Storing corresponding nodes in r1,r2,r3 parameters."""
        r1 = slicer.mrmlScene.GetFirstNodeByName('220074_pelvis')
        r2 = slicer.mrmlScene.GetFirstNodeByName('220074_knee')
        r3 = slicer.mrmlScene.GetFirstNodeByName("220074_ankle")
        """ Setting current node to r3."""
        self.ui.inputSelector_2.setCurrentNode(r3)
        volRenLogic3 = slicer.modules.volumerendering.logic()
        displayNode3 = volRenLogic3.CreateDefaultVolumeRenderingNodes(r3)
       
        volumePropertyNode = displayNode3.GetVolumePropertyNode()
        preset = volRenLogic3.GetPresetByName('CT-AAA')
        volumePropertyNode.Copy(preset)
        self.showTransparentRendering(r3, 1, 300.0)
   
        """  Accessing the volume rendering module.
             Creating a display node. 
             Setting visibility of corresponding node.
        """
        volRenLogic1 = slicer.modules.volumerendering.logic()
        displayNode1 = volRenLogic1.CreateDefaultVolumeRenderingNodes(r1)
        displayNode1.SetVisibility(False)
        """  Accessing the volume rendering module.
             Creating a display node. 
             Setting visibility of corresponding node.
        """
        volRenLogic3 = slicer.modules.volumerendering.logic()
        displayNode3 = volRenLogic3.CreateDefaultVolumeRenderingNodes(r2)
        displayNode3.SetVisibility(False)
        """ Center and fit displayed content in 3D view in the direction of anterior position."""
        view2 = slicer.app.layoutManager().threeDWidget(0).threeDController()
        view2.resetFocalPoint()
        view2.lookFromAxis(ctk.ctkAxesWidget.Anterior)
        view2.setOrthographicModeEnabled(True)
</code></pre>

---

## Post #4 by @cpinter (2024-03-14 12:34 UTC)

<p>Your code seems to be more complicated than it could be.</p>
<p>First of all, I suggest revising it carefully, because mixing up volume node numbers and display node numbers surely cause issues. For example<br>
<code>displayNode3 = volRenLogic3.CreateDefaultVolumeRenderingNodes(r2)</code><br>
Here you’ll think that <code>displayNode3</code> corresponds to volume <code>r3</code>, but it really corresponds to <code>r2</code>.</p>

---
