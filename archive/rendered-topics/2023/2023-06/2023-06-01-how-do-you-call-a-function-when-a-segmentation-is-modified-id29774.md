# How do you call a function when a segmentation is modified?

**Topic ID**: 29774
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/how-do-you-call-a-function-when-a-segmentation-is-modified/29774

---

## Post #1 by @Guillaumeee (2023-06-01 14:51 UTC)

<p>Hello,</p>
<p>I’m looking to create an observer that will allow me to call a method when the segmentation is modified via the segment editor.</p>
<p>Here’s a class I’ve created:</p>
<pre><code class="lang-python">import slicer
from vtk import vtkCommand

class SegmentationWatcher:
    SAVE_FOLDER = 'tmp'
    def __init__(self, extension_path: str, segmentationNode):
        self.__extension_path = extension_path
        self.segmentationNode = segmentationNode
        self.callbackObject = None

    def segmentationModifiedCallback(self, caller, event):
        print("Modified")

    def startWatching(self):
        if self.callbackObject is None:
            self.callbackObject = self.segmentationNode.AddObserver(vtkCommand.ModifiedEvent, self.segmentationModifiedCallback)

    def stopWatching(self):
        if self.callbackObject:
            self.segmentationNode.RemoveObserver(self.callbackObject)
            self.callbackObject = None
</code></pre>
<p>However, the function is never called. I deduced that the event was not good.<br>
I saw that the SegmentationModifiedCallbackCommand attribute existed.</p>
<p>So I did this:</p>
<pre><code class="lang-python">import slicer

class SegmentationWatcher:
    SAVE_FOLDER = 'tmp'
    def __init__(self, extension_path: str, segmentationNode):
        self.__extension_path = extension_path
        self.segmentationNode = segmentationNode
        self.callbackObject = None

    def segmentationModifiedCallback(self, caller, event):
        print("Modified")

    def startWatching(self):
        if self.callbackObject is None:
            self.callbackObject = self.segmentationNode.AddObserver(slicer.vtkMRMLSegmentationNode.SegmentationModifiedCallbackCommand,
                                                                    self.segmentationModifiedCallback)

    def stopWatching(self):
        if self.callbackObject:
            self.segmentationNode.RemoveObserver(self.callbackObject)
            self.callbackObject = None
</code></pre>
<p>But I have this error :</p>
<pre><code class="lang-auto">AttributeError: 'MRMLCore.vtkMRMLSegmentationNode' object has no attribute 'SegmentationModifiedCallbackCommand'
</code></pre>
<p>This is normal because the attribute is protected. I’ve tried to make the class an inheritance of slicer.vtkMRMLSegmentationNode but I still have error.</p>
<p>I’d like to know if it’s possible to access it or if another method is more interesting?</p>
<p>Thank you very much in advance for your help and have a nice day!</p>

---

## Post #2 by @Sunderlandkyl (2023-06-01 15:57 UTC)

<p>I think that you are looking for <a href="https://apidocs.slicer.org/main/classvtkMRMLSegmentationNode.html#af9c38e41e18005c0448a257f5dfb85c4add8f2a12345ec147a14cb87758130e8b" rel="noopener nofollow ugc">vtkMRMLSegmentationNode::SegmentationChangedEvent</a>.</p>

---

## Post #3 by @cpinter (2023-06-02 08:44 UTC)

<p>I tend to use this event:</p>
<p><code>segmentationNode.AddObserver(slicer.vtkSegmentation.RepresentationModified, self.onSegmentContentModified)</code></p>
<p>In this case the callback looks like this so you can see which segment was just modified:</p>
<pre><code class="lang-auto">  @vtk.calldata_type(vtk.VTK_STRING)
  def onSegmentContentModified(self, caller, eventId, callData=None):
    segmentID = callData
    ...
</code></pre>
<p>Also just for completeness I checked SegmentationChangedEvent and it seems to be for something else:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/5e7d60c87711a14902f9001330321e1e494a7e6b/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L303">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/5e7d60c87711a14902f9001330321e1e494a7e6b/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L303" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5e7d60c87711a14902f9001330321e1e494a7e6b/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L303" target="_blank" rel="noopener">Slicer/Slicer/blob/5e7d60c87711a14902f9001330321e1e494a7e6b/Libs/MRML/Core/vtkMRMLSegmentationNode.h#L303</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="293" style="counter-reset: li-counter 292 ;">
          <li>  vtkSetMacro(SegmentListFilterOptions, std::string);</li>
          <li>  vtkGetMacro(SegmentListFilterOptions, std::string);</li>
          <li>
          </li>
<li>  /// The vtkMRMLColorTableNode that is used to convert to and from labelmap representations.</li>
          <li>  /// If a segment name matches the name of a color in the table, then the value of the color will be used as the labelmap value</li>
          <li>  /// for the segment when exporting the segmentation to labelmap.</li>
          <li>  void SetLabelmapConversionColorTableNodeID(const char* labelmapConversionColorTableNodeID);</li>
          <li>  vtkMRMLColorTableNode* GetLabelmapConversionColorTableNode();</li>
          <li>
          </li>
<li>  /// ReferenceImageGeometryChangedEvent is fired when the ReferenceImageGeometry node reference is Added, Modified, or Removed</li>
          <li class="selected">  /// SegmentationChangedEvent is fired when a different vtkSegmentation object is set into the node.</li>
          <li>  enum</li>
          <li>  {</li>
          <li>    ReferenceImageGeometryChangedEvent = 23000,</li>
          <li>    SegmentationChangedEvent</li>
          <li>  };</li>
          <li>
          </li>
<li>protected:</li>
          <li>  /// Set segmentation object</li>
          <li>  vtkSetObjectMacro(Segmentation, vtkSegmentation);</li>
          <li>
      </li>
</ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
