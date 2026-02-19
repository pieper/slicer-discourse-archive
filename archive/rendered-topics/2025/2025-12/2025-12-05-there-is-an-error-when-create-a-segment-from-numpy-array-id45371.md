---
topic_id: 45371
title: "There Is An Error When Create A Segment From Numpy Array"
date: 2025-12-05
url: https://discourse.slicer.org/t/45371
---

# There is an error when create a segment from numpy array

**Topic ID**: 45371
**Date**: 2025-12-05
**URL**: https://discourse.slicer.org/t/there-is-an-error-when-create-a-segment-from-numpy-array/45371

---

## Post #1 by @zhutouzjq (2025-12-05 06:21 UTC)

<p>hellow, everyone.</p>
<p>i want to creat a segment from a numpy array. and i found the python code in script repository as following.</p>
<pre><code class="lang-auto">volumeNode = getNode('MRHead')
segmentationNode = getNode('Segmentation')
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')

# Get segment as numpy array
segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)

# Modify the segmentation
segmentArray[:] = 0  # clear the segmentation
segmentArray[ slicer.util.arrayFromVolume(volumeNode) &gt; 80 ] = 1  # create segment by simple thresholding of an image
segmentArray[20:80, 40:90, 30:70] = 1  # fill a rectangular region using numpy indexing
slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId, volumeNode)
</code></pre>
<p>in my own extension, the code line “volumeNode = getNode(‘MRHead’)” was be replaced by a qMRMLNodeCombobox in the nodetypes called “vtkMRMLScalarVolumeNode“.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd291ee7788b413b162a31462def1f214bbfbe04.png" data-download-href="/uploads/short-url/vytCxPyNb3rScQgcq1lD981KSEs.png?dl=1" title="无标题1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd291ee7788b413b162a31462def1f214bbfbe04.png" alt="无标题1" data-base62-sha1="vytCxPyNb3rScQgcq1lD981KSEs" width="690" height="295" data-dominant-color="DEDFD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题1</span><span class="informations">922×395 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the code line “segmentationNode = getNode(‘Segmentation’)“ was be replaced by a qMRMLNodeCombobox in the nodetypes called “vtkMRMLSegmentationNode“.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc5df90c4508ea369fd6c29e9d52b4e557c6db4.png" data-download-href="/uploads/short-url/8Ot4aFRTU1zQ4Og3vuD9hw5K08A.png?dl=1" title="无标题3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dc5df90c4508ea369fd6c29e9d52b4e557c6db4.png" alt="无标题3" data-base62-sha1="8Ot4aFRTU1zQ4Og3vuD9hw5K08A" width="690" height="288" data-dominant-color="DEDFD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题3</span><span class="informations">922×386 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and i convert the “inputSelector“ and “inputsegmentation“ into def process as following.</p>
<blockquote>
<pre><code>def onApplyButton(self) -&gt; None:

    """Run processing when user clicks "Apply" button."""

    with slicer.util.tryWithErrorDisplay(\_("Failed to compute results."), waitCursor=True):

        \# Compute output

        self.logic.process(self.ui.inputSelector.currentNode(), self.ui.imageThresholdSliderWidget.value, 

                           self.ui.inputlowerpoint.currentNode(), self.ui.inputmidpoint.currentNode(),

                           self.ui.inputupperpoint.currentNode(), self.ui.inputsegmentation.currentNode())
</code></pre>
</blockquote>
<blockquote>
<p>class cutcalciLogic(ScriptedLoadableModuleLogic):</p>
<pre><code>"""This class should implement all the actual

computation done by your module.  The interface

should be such that other python code can import

this class and make use of the functionality without

requiring an instance of the Widget.

Uses ScriptedLoadableModuleLogic base class, available at:

https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py

"""



def \__init_\_(self) -&gt; None:

    """Called when the logic class is instantiated. Can be used for initializing member variables."""

    ScriptedLoadableModuleLogic.\__init_\_(self)



def getParameterNode(self):

    return cutcalciParameterNode(super().getParameterNode())



def getFiducialKJI(self, inputpoint, volume):    

def get_vascular_up2low(self, image, upperpoint, lowerpoint, CT_value):

def get_vascular_low2up(self, image, lowerpoint, upperpoint, CT_value):

def check_vascular(self, vascular_array, lowerpoint):

def get_vascular(self, image, upperpoint, midpoint, lowerpoint):

    vascular_array= self.get_vascular_up2low(image, upperpoint, lowerpoint, CT_value= 130)

    while self.check_vascular(vascular_array, lowerpoint)==0:

        vascular_array_1= self.get_vascular_low2up(image, midpoint, upperpoint)

        vascular_array_2= self.get_vascular_up2low(image, midpoint, lowerpoint)

        vascular_array= vascular_array+ vascular_array_1+ vascular_array_2

    return vascular_array

def process(self,

            inputVolume: vtkMRMLScalarVolumeNode,

            imageThreshold: float,

            inputlowerpoint,

            inputmidpoint,

            inputupperpoint,

            inputsegmentation,

            showResult: bool = True) -&gt; None:

    if not inputVolume:

        raise ValueError("Input volume is invalid")

    lowerpoint= self.getFiducialKJI(inputlowerpoint, inputVolume)

    midpoint= self.getFiducialKJI(inputmidpoint, inputVolume)

    upperpoint= self.getFiducialKJI(inputupperpoint, inputVolume)

    image_array= slicer.util.arrayFromVolume(inputVolume)

    #vascular_array= self.get_vascular(image_array,upperpoint, midpoint, lowerpoint)

    segmentId = inputsegmentation.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')

    print(lowerpoint)

    \# Get segment as numpy array

    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(inputsegmentation, segmentId, inputVolume) **#there is an error in this code line**

    \# Modify the segmentation

    #segmentArray\[:\] = 0  # clear the segmentation

    #segmentArray\[ slicer.util.arrayFromVolume(inputVolume) &gt; 80 \] = 1  # create segment by simple thresholding of an image

    #segmentArray\[20:80, 40:90, 30:70\] = 1  # fill a rectangular region using numpy indexing

    #slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, inputsegmentation, segmentId, inputVolume)
</code></pre>
</blockquote>
<p>and when i reload and apply this extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de7c3a389df8add0b854d7cdb0aca5776dc74261.png" data-download-href="/uploads/short-url/vKc9zNiWJpdJtMXAOk2xBRq7zq1.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de7c3a389df8add0b854d7cdb0aca5776dc74261.png" alt="无标题" data-base62-sha1="vKc9zNiWJpdJtMXAOk2xBRq7zq1" width="690" height="354" data-dominant-color="E8E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">760×391 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>3D slicer tell me there is an error.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4794afde97f75321bd805efae7992e844c83aaf2.png" data-download-href="/uploads/short-url/adeszlLsD13q9XlBledQNTaMelA.png?dl=1" title="无标题4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4794afde97f75321bd805efae7992e844c83aaf2.png" alt="无标题4" data-base62-sha1="adeszlLsD13q9XlBledQNTaMelA" width="690" height="90" data-dominant-color="FAF9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题4</span><span class="informations">1001×131 5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “D:\program_file\Slicer 5.6.2\bin\Python\slicer\util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “D:/program_file/Slicer 5.6.2/cutcalci/cutcalci/cutcalci.py”, line 245, in onApplyButton<br>
self.logic.process(self.ui.inputSelector.currentNode(), self.ui.imageThresholdSliderWidget.value,<br>
File “D:/program_file/Slicer 5.6.2/cutcalci/cutcalci/cutcalci.py”, line 423, in process</p>
<h1>Get segment as numpy array</h1>
<p>File “D:\program_file\Slicer 5.6.2\bin\Python\slicer\util.py”, line 2138, in arrayFromSegmentBinaryLabelmap<br>
narray = slicer.util.arrayFromVolume(labelmapVolumeNode)<br>
File “D:\program_file\Slicer 5.6.2\bin\Python\slicer\util.py”, line 1742, in arrayFromVolume<br>
narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars()).reshape(nshape)<br>
File “D:\program_file\Slicer 5.6.2\bin\Lib\site-packages\vtkmodules\util\numpy_support.py”, line 215, in vtk_to_numpy<br>
typ = vtk_array.GetDataType()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetDataType’</p>
</blockquote>
<p>i’m sure that it is the code line “segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(inputsegmentation, segmentId, inputVolume) “ which causes this error. because there the KJI coordinate of lowerpoint can be printed in python console.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37ba07509e53e50bac9494f2b21d19df1a5bd2a6.png" data-download-href="/uploads/short-url/7WYPahDoAJm2YTU70Mc0ZQIEOUe.png?dl=1" title="无标题5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37ba07509e53e50bac9494f2b21d19df1a5bd2a6_2_689x198.png" alt="无标题5" data-base62-sha1="7WYPahDoAJm2YTU70Mc0ZQIEOUe" width="689" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37ba07509e53e50bac9494f2b21d19df1a5bd2a6_2_689x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37ba07509e53e50bac9494f2b21d19df1a5bd2a6_2_1033x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37ba07509e53e50bac9494f2b21d19df1a5bd2a6.png 2x" data-dominant-color="E9E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题5</span><span class="informations">1292×372 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>so, my problem is how to create a segment from numpy array successfully?</p>

---

## Post #2 by @pieper (2025-12-05 13:46 UTC)

<p>You should write small examples in the slicer python console to confirm the your assumptions step by step.  Or you can expose variables from within your module by assigning them into the global space with something like <code>slicer.modules.segmentationNode = segmentationNode</code> and then you can call methods on it to see what happens.</p>

---

## Post #3 by @zhutouzjq (2025-12-09 01:23 UTC)

<p>i know where is wrong in the code now.</p>
<p>in the code line “segmentId = inputsegmentation.GetSegmentation().GetSegmentIdBySegmentName(‘Segment_1’)“, the function “GetSegmentIdBySegmentName()“ won’t create a new segment in the existed segmentation but the effect of this function is to find a exised segment called “Segment_1“.</p>
<p>so, if you want use this code line, you need to create a new segment in segment editor and than use this code line to rewrite the segment with your own numpy array</p>

---

## Post #4 by @zhutouzjq (2025-12-09 02:32 UTC)

<p>further, i find in the following network link, there is a code line “addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)“ can create a new segment in chosen segmentation.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37">
  <header class="source">

      <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37</a></h4>

  <h5>SegmentByThresholding.py</h5>
  <pre><code class="Python"># Download a sample data set (chest CT)
import SampleData
masterVolumeNode = SampleData.SampleDataLogic().downloadCTChest()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects</code></pre>
   This file has been truncated. <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="noopener nofollow ugc">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and i alter this code line as “segmentId = inputsegmentation.GetSegmentation().AddEmptySegment(‘Segment_1’)“ to replace the orginal code line “segmentId = inputsegmentation.GetSegmentation().GetSegmentIdBySegmentName(‘Segment_1’)“</p>
<p>after reloading the extension, now i can create a new segment in the chosen segmentation.</p>

---
