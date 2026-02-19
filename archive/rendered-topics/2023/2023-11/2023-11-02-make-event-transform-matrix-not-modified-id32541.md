---
topic_id: 32541
title: "Make Event Transform Matrix Not Modified"
date: 2023-11-02
url: https://discourse.slicer.org/t/32541
---

# Make event Transform matrix not modified

**Topic ID**: 32541
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/make-event-transform-matrix-not-modified/32541

---

## Post #1 by @park (2023-11-02 02:59 UTC)

<p>Hi all</p>
<p>I would like to track a specific transform matrix and change the Qt label to ‘on’ when it changing and to ‘off’ when it doesn’t.</p>
<p>I’ve implemented the code below, but is there a more efficient way?</p>
<p>I’m particularly concerned about the while loop causing performance issues in the program.</p>
<p>Thanks</p>
<pre><code class="lang-auto">        ReferenceToTrackerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "ReferenceToTracker")
        TranCenterToRefernceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "TranCenterToReferenc")
        StylusTipToReferenceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "StylusTipToReference")

        needleNode.SetAndObserveTransformNodeID(StylusTipToReferenceNode.GetID())

        self.lastMatrix = [np.zeros((4, 4)), np.zeros((4, 4)), np.zeros((4, 4))] 
        transformMatrix = vtk.vtkMatrix4x4()
        def checkTransformNode(node, lastMatrix):
            
            name = node.GetName()
            node.GetMatrixTransformToWorld(transformMatrix)
            matrix_arr_origin = np.zeros((4, 4))

            for i in range(0, 4):
                for j in range(0, 4):
                    matrix_arr_origin[i, j] = (transformMatrix.GetElement(i, j))
            
            if np.array_equal(lastMatrix, matrix_arr_origin):
                if name== "ReferenceToTracker":
                    self.ui.referenceLabel.setText("Reference Off")
                    self.ui.referenceLabel.setStyleSheet("color: #FA8072; width: 15px; ")
                elif name== "TranCenterToReferenc":
                    self.ui.transducerLabel.setText("Transducer Off")
                    self.ui.transducerLabel.setStyleSheet("color: #FA8072; width: 15px; ")
                elif name== "StylusTipToReference":
                    self.ui.stylusLabel.setText("Stylus Off")                    
                    self.ui.stylusLabel.setStyleSheet("color: #FA8072; width: 15px; ")
            else:
                if name== "ReferenceToTracker":
                    self.ui.referenceLabel.setText("Reference On")
                    self.ui.referenceLabel.setStyleSheet("color: #4D69E8; width: 15px; ")
                elif name== "TranCenterToReferenc":
                    self.ui.transducerLabel.setText("Transducer On")
                    self.ui.transducerLabel.setStyleSheet("color: #4D69E8; width: 15px; ")
                elif name== "StylusTipToReference":
                    self.ui.stylusLabel.setText("Stylus On")
                    self.ui.stylusLabel.setStyleSheet("color: #4D69E8; width: 15px; ")
                    
            # save current matrix
            if name== "ReferenceToTracker":
                self.lastMatrix[0] = matrix_arr_origin
            elif name== "TranCenterToReferenc":
                self.lastMatrix[1] = matrix_arr_origin
            elif name== "StylusTipToReference":
                self.lastMatrix[2] = matrix_arr_origin

        timer = QTimer()
        timer.timeout.connect(lambda: checkTransformNode(ReferenceToTrackerNode, self.lastMatrix[0]))
        timer.timeout.connect(lambda: checkTransformNode(TranCenterToRefernceNode, self.lastMatrix[1]))
        timer.timeout.connect(lambda: checkTransformNode(StylusTipToReferenceNode, self.lastMatrix[2]))
        timer.start(100)
        
        # start event loop 
        while True:
            slicer.app.processEvents() 

</code></pre>

---

## Post #2 by @lassoan (2023-11-02 03:10 UTC)

<p>You can use the “Watchdog” module in SlicerIGT extension to monitor a transform node and display a message when it is not being continuously updated anymore (and optionally play a sound signal, too). This can be used for example for warning the user when an optical tracker marker is occluded. You can also add an observer to the vtkMRMLWatchdogNode to get a notification in your module when status of a transform changes.</p>

---

## Post #3 by @park (2023-11-02 04:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="32541">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkMRMLWatchdogNode</p>
</blockquote>
</aside>
<p>The documentation for vtkMRMLWatchdogNode is limited, so could you provide more examples? I attempted to create it like this, but the process seems too fast, and on-off events are occurring repetitively.</p>
<p><code>ReferenceToTrackerNode.AddObserver(slicer.vtkMRMLWatchdogNode.TransformModifiedEvent, lambda caller, event: checkTransformNode(caller, event, self.lastMatrix[0]))</code></p>

---

## Post #4 by @lassoan (2023-11-02 04:44 UTC)

<p>You need to observe the watchdog node. The nodes are quite well documented, except maybe a few properties that are mostly self-explaining, see:</p>
<ul>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/Watchdog/MRML/vtkMRMLWatchdogNode.h">https://github.com/SlicerIGT/SlicerIGT/blob/master/Watchdog/MRML/vtkMRMLWatchdogNode.h</a></li>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/Watchdog/MRML/vtkMRMLWatchdogDisplayNode.h">https://github.com/SlicerIGT/SlicerIGT/blob/master/Watchdog/MRML/vtkMRMLWatchdogDisplayNode.h</a></li>
</ul>
<p>However, I would recommend to start with just using the GUI. Normally you don’t need to write any code to use this module, as you can configure what transforms are observed, what messages are displayed and where, and save the scene. You can save all other configuration settings (transform hierarchy, display options of all nodes, OpenIGTLink connection information, etc.) in the scene as well. When you want to start navigation then it is enough to load the scene and everything should work.</p>

---
