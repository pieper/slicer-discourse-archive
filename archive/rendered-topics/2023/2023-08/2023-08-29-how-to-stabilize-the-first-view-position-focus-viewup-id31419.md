---
topic_id: 31419
title: "How To Stabilize The First View Position Focus Viewup"
date: 2023-08-29
url: https://discourse.slicer.org/t/31419
---

# How to stabilize the first view（position/focus/ViewUp）

**Topic ID**: 31419
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/how-to-stabilize-the-first-view-position-focus-viewup/31419

---

## Post #1 by @slicer365 (2023-08-29 09:45 UTC)

<p>I used the Endoscopy module to create a first-view analog navigation,</p>
<p>and to demonstrate, I’m using a point as a guide,</p>
<p>when I move this point, the 3D view suddenly changes, especially when the position of the point moves to the left or right.</p>
<p>The following is part of the code, which mainly adds an observer to the selected point, then obtains the position of the point in real time, and takes the latest two positions as the camera position and focus position, and the viewUp position is fixed.</p>
<p>I mainly hope it can turn smoothly.</p>
<p>I know this is caused by a change in the vector direction of the camera position and focus, so I want to find a solution.</p>
<pre><code class="lang-auto">    def addPos(self,caller,event):
        position=[0,0,0]
        transNode=self.ui.markSelector.currentNode()
        
        transNode.GetNthControlPointPosition(0, position)
        
        self.transList.append(position)
        if len(self.transList)&gt;2:
            self.transList=self.transList[-2:]
        
            cameraPosition = self.transList[0]
 
            wasModified = self.cameraNode.StartModify()
           
            self.camera.SetPosition(cameraPosition)
            focalPointPosition = self.transList[1]
            
            self.camera.SetFocalPoint(*focalPointPosition)
            self.camera.OrthogonalizeViewUp()
           #self.camera.SetViewUp()
           
            self.cameraNode.EndModify(wasModified)
            self.cameraNode.ResetClippingRange()

    def startNav(self):
    
        navNode=self.ui.markSelector.currentNode()

        if navNode:
        
            navNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,self.addPos)
        else:
            pass
</code></pre>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158d15a61dc0f40d839a0f4037cd07bb8c82fb9f.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158d15a61dc0f40d839a0f4037cd07bb8c82fb9f.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158d15a61dc0f40d839a0f4037cd07bb8c82fb9f.mp4</a>
    </video>
  </div><p></p>

---

## Post #2 by @pieper (2023-08-31 19:53 UTC)

<p>It looks like something else is also trying to set the view.  Maybe if you can create a fully self-contained example script it would help.</p>

---

## Post #3 by @slicer365 (2023-09-02 00:50 UTC)

<p>Thank you, Mr Pieper, I solved the problem.</p>
<p>The problem is caused by the camera position being too close to the focus position.</p>
<p>I increased the distance between the camera and the focus, and it looked much more stable.</p>
<p>Although it’s still a little shaky.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e35db7be0a974a9f933eb534e86cd9294c02750d.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e35db7be0a974a9f933eb534e86cd9294c02750d.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e35db7be0a974a9f933eb534e86cd9294c02750d.mp4</a>
    </video>
  </div><p></p>

---
