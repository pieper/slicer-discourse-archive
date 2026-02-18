# How to observe the change of a vector in an object in real time when the object is rotating

**Topic ID**: 35862
**Date**: 2024-05-02
**URL**: https://discourse.slicer.org/t/how-to-observe-the-change-of-a-vector-in-an-object-in-real-time-when-the-object-is-rotating/35862

---

## Post #1 by @Cathy123 (2024-05-02 05:41 UTC)

<p>I try to programme with python to detect the changes of a vector in the object in real time.<br>
I have a volume in the scene, and there is a tranform node M on it. a is a vector in the object, when the object was rotating, the vector a was also rotating with b = a*M. so now I want to detect the vector b in real-time when M was changing. How can I write code with python , thank you.</p>

---

## Post #2 by @pieper (2024-05-02 14:55 UTC)

<p>You can add an observer to the transform node.  Search the script repository for <code>AddObserver</code> and you’ll find lots of examples.</p>

---

## Post #3 by @Cathy123 (2024-05-03 05:51 UTC)

<p>I have tried but the detected vector can’t change in real time.<br>
my code is as following:</p>
<pre><code class="lang-auto">def monitorAndAdjustTransform(self):
        print("onTransformModified called") #test
        if not self.transformNode:
            return
        vtkMatrix = vtk.vtkMatrix4x4()
        self.transformNode.GetMatrixTransformToWorld(vtkMatrix)
        
        npMatrix = np.array([[vtkMatrix.GetElement(i, j) for j in range(4)] for i in range(4)])
        normal_vector = np.array([-0.19911008, 0.16549629, 0.96590173])
        transformed_vector = np.dot(npMatrix[:3, :3], normal_vector)
        
        target_vector1 = np.array([0, 0, 1])
        target_vector2 = np.array([0, 0, -1])

         # calculate np.dot 
        dot1 = np.dot(transformed_vector, target_vector1)
        dot2 = np.dot(transformed_vector, target_vector2)
        print("Transformed vector: ", transformed_vector)
        print("Dot product with (0,0,1): ", dot1)
        print("Dot product with (0,0,-1): ", dot2)
        
        # set threshold
        threshold = 0.97 

        if abs(dot1) &gt;= threshold or abs(dot2) &gt;= threshold:
            print("Normal vector is aligned with Z-axis, limiting Y-axis rotation")
            npMatrix[0, 1] = max(0, npMatrix[0, 1])
            npMatrix[2, 1] = max(0, npMatrix[2, 1])
            
            for i in range(4):
                for j in range(4):
                    vtkMatrix.SetElement(i, j, npMatrix[i, j])
            self.transformNode.SetMatrixTransformToParent(vtkMatrix)                                               

def loadNextFile(self):
        #---Load the next NRRD file from the list and remove the previous one.
        # Check if there are more files to load
        if self.currentFileIndex &lt; len(self.nrrdFiles):
            filePath = self.nrrdFiles[self.currentFileIndex]
            volumeNode = slicer.util.loadVolume(filePath)
            self.currentFileIndex += 1

            # Enable volume rendering for the loaded volume
            if volumeNode:
                self.applyCustomColorMap()
                self.initializeVolumeRendering()
                #self.enableVolumeRendering(volumeNode)
                #-----
                #self.onApplyTransformClicked()
                volumeName = volumeNode.GetName()
                #print("viewname:", volumeName)
                self.update3DViewerTextAnnotation(volumeName) 
                self.transformNode = slicer.vtkMRMLLinearTransformNode()
                self.transformNode.SetName('LinearTransform')
                slicer.mrmlScene.AddNode(self.transformNode)
                
                # Apply the transform node to the volume node
                volumeNode.SetAndObserveTransformNodeID(self.transformNode.GetID())
                self.transformNode.CreateDefaultDisplayNodes()
                self.transformNode.GetDisplayNode().SetEditorVisibility(True)

                # detect
                self.initializeTransformMonitoring()
                slicer.mrmlScene.Modified()# update scence
                slicer.app.processEvents()
</code></pre>
<p>The detect function was integrated to loadnrrdfile function, but can’t be effect, could you please help me check.</p>

---

## Post #4 by @pieper (2024-05-03 15:50 UTC)

<p>Looks like you need a line like this:</p>
<pre><code class="lang-auto">self.transformNode.AddObserver(self.transformNode.TransformModifiedEvent, self. monitorAndAdjustTransform)
</code></pre>

---

## Post #5 by @Cathy123 (2024-05-03 16:55 UTC)

<p>I htried your code line, but it is not correct.<br>
I have changed my code with more function. now the problem is that it can’t automatically show the vector changing when I rotate the object with mouse. can you please help me check the problem?<br>
def loadNextFile(self):<br>
#—Load the next NRRD file from the list and remove the previous one.<br>
self.removeCurrentVolume()<br>
self.removeAllTransformNodesAndInteractionBoxes()</p>
<pre><code>    # Check if there are more files to load
    if self.currentFileIndex &lt; len(self.nrrdFiles):
        filePath = self.nrrdFiles[self.currentFileIndex]
        volumeNode = slicer.util.loadVolume(filePath)
        self.currentFileIndex += 1

        # Enable volume rendering for the loaded volume
        if volumeNode:
            self.applyCustomColorMap()
            self.initializeVolumeRendering()
    
            #-----
            #self.onApplyTransformClicked()
            volumeName = volumeNode.GetName()
            #print("viewname:", volumeName)
            self.update3DViewerTextAnnotation(volumeName)
            self.transformNode = slicer.vtkMRMLLinearTransformNode()
            self.transformNode.SetName('LinearTransform')
            slicer.mrmlScene.AddNode(self.transformNode)
            
            # Apply the transform node to the volume node
            volumeNode.SetAndObserveTransformNodeID(self.transformNode.GetID())
            self.transformNode.CreateDefaultDisplayNodes()
            self.transformNode.GetDisplayNode().SetEditorVisibility(True)

            # initialization
            self.initializeTransformMonitoring()
            self.testTriggerEvent()
            slicer.mrmlScene.Modified()# update scence
            slicer.app.processEvents()

            print("Transform node has been created and applied to the volume node.")  
            ##-----
    else:
        # Reset the index or inform the user all files have been loaded
        slicer.util.infoDisplay("No more NRRD files to load.", windowTitle='Info')

def testTriggerEvent(self):
    if self.transformNode:
        matrix = vtk.vtkMatrix4x4()
        matrix.Identity()
        matrix.SetElement(0, 0, 0.99)
        self.transformNode.SetMatrixTransformToParent(matrix)
        self.transformNode.Modified()  


def monitorAndAdjustTransform(self):
    print("onTransformModified called")  
    if not self.transformNode:
        return
    vtkMatrix = vtk.vtkMatrix4x4()
    self.transformNode.GetMatrixTransformToWorld(vtkMatrix)
    
    npMatrix = np.array([[vtkMatrix.GetElement(i, j) for j in range(4)] for i in range(4)])
    normal_vector = np.array([-0.19911008, 0.16549629, 0.96590173])
    transformed_vector = np.dot(npMatrix[:3, :3], normal_vector)
    
    target_vector1 = np.array([0, 0, 1])
    target_vector2 = np.array([0, 0, -1])
    dot1 = np.dot(transformed_vector, target_vector1)
    dot2 = np.dot(transformed_vector, target_vector2)
    print("Transformed vector: ", transformed_vector)
    print("Dot product with (0,0,1): ", dot1)
    print("Dot product with (0,0,-1): ", dot2)
    threshold = 0.97 

    if abs(dot1) &gt;= threshold or abs(dot2) &gt;= threshold:
        print("Normal vector is aligned with Z-axis, limiting Y-axis rotation")
        npMatrix[0, 1] = max(0, npMatrix[0, 1])
        npMatrix[2, 1] = max(0, npMatrix[2, 1])
        
        for i in range(4):
            for j in range(4):
                vtkMatrix.SetElement(i, j, npMatrix[i, j])
        self.transformNode.SetMatrixTransformToParent(vtkMatrix)


def cleanup(self):
    if self.transformNode and self.observerTag:
        self.transformNode.RemoveObserver(self.observerTag)
        self.observerTag = None

def onTransformModified(self, caller, event):
    print("Transform modified detected")
    self.monitorAndAdjustTransform()


def initializeTransformMonitoring(self):
    if self.transformNode:
        if self.observerTag:
            self.transformNode.RemoveObserver(self.observerTag)
    # add observer
        self.observerTag = self.transformNode.AddObserver(vtk.vtkCommand.ModifiedEvent, self.onTransformModified)
        print("detect")
</code></pre>

---

## Post #6 by @Cathy123 (2024-05-03 20:21 UTC)

<p>Hi Pieper,</p>
<p>I have got the answer from scipt repository.<br>
Thank you  so much.</p>

---
