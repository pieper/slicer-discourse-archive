---
topic_id: 2076
title: "T2 Map Multi Volume Related Questions"
date: 2018-02-13
url: https://discourse.slicer.org/t/2076
---

# T2 Map Multi-volume related questions

**Topic ID**: 2076
**Date**: 2018-02-13
**URL**: https://discourse.slicer.org/t/t2-map-multi-volume-related-questions/2076

---

## Post #1 by @brhoom (2018-02-13 10:57 UTC)

<p>Operating system: Ubuntu 16<br>
Slicer version: 4.8<br>
Expected behavior:  Display volume information and an image<br>
Actual behavior: Slicer displays a white image and crash when opening the “Volume” Module</p>
<p>Dear all,<br>
I have a CD contains a DICOM of MRI T2 Map Volume. I converted the contents to nrrd to do some experience. This produces 9 volumes:  imgT2MAP_0 to imgT2MAP_7 (8 separate files nrrd files) and one nrrd file  imgT2MAP of type vtkMRMLMultiVolumeNode.</p>
<p>When I open the last file in Slicer it display an image but it does not show voxel values in the Data Probe. Instead it displays “8 components”. My question is how this image is represented with these 8 values? what are the gray values in the shown image?</p>
<p>I tried to do some computation e.g. generate the first image  imgT2MAP_0 from  imgT2MAP by taking only the first value from the vector. The code runs but I got a white image, when I open the resulted volume in “Volume” Slicer crashes. Here is the code (forgive my dirty coding as I wrote in a  hurry):</p>
<pre><code>    v = self.inputSelector.currentNode()
    # get image properties 
    vd=v.GetImageData()
    sz=vd.GetDimensions()
    sp= v.GetSpacing()
    og= v.GetOrigin()
    dm = vtk.vtkMatrix4x4()
    v.GetIJKToRASDirectionMatrix(dm)
    va = slicer.util.array(v.GetID())    
    tp =  vd.GetScalarType()

    img=vtk.vtkImageData()
    img.SetDimensions(sz)
    img.AllocateScalars(tp, 1)
    thresholder=vtk.vtkImageThreshold()
    thresholder.SetInputData(img)
    thresholder.SetInValue(0)
    thresholder.SetOutValue(0)        
    vn=slicer.vtkMRMLScalarVolumeNode()
    vn.SetSpacing(sp)
    vn.SetOrigin(og) 
    vn.SetIJKToRASDirectionMatrix(dm)     
    vn.SetImageDataConnection(thresholder.GetOutputPort())
    vn.SetName("imgT2MapOutput")      
    
    # Add volume to scene
    slicer.mrmlScene.AddNode(vn)
    displayNode=slicer.vtkMRMLScalarVolumeDisplayNode()
    slicer.mrmlScene.AddNode(displayNode)
    colorNode = slicer.util.getNode('Grey')
    displayNode.SetAndObserveColorNodeID(colorNode.GetID())
    vn.SetAndObserveDisplayNodeID(displayNode.GetID())
    vn.CreateDefaultStorageNode()
     
     
    vm = slicer.util.getNode("imgT2MapOutPut")
    vmd=vm.GetImageData()
    vma = slicer.util.array(vm.GetID())    
   
    for k in xrange(0, sz[0]):  
        for j in xrange(0,sz[1]):
            for i in xrange(0, sz[2]):
                vc= va[i,j,k]
                vma [i,j,k] =  vc[0] 
     
    vm.Modified()  
</code></pre>
<p>Please help me to find out what makes this strange output and slicer crash in the previous code. Also, I would like to know if there is a better way to do the same thing e.g. using iterators instead of loops.<br>
Thanks!</p>

---

## Post #2 by @lassoan (2018-02-13 15:17 UTC)

<p>You can load 4D nrrd files if Sequences module is installed. In <code>Add data</code> dialog, choose <code>Volume sequence</code> for the data set. If you use .seq.nrrd extension instead of just .nrrd then <code>Volume sequence</code> will be selected by default.</p>

---

## Post #3 by @brhoom (2018-02-13 22:22 UTC)

<p>Hi Andras and thanks for your reply,</p>
<ul>
<li>I installed the sequence extension.</li>
<li>I changed the file by adding .seq and load the volume as you described.</li>
<li>In Volume Module. The volume type is changed.</li>
</ul>
<p>This is helpful for viewing but I still can not do computations e.g. generate different nodes from the sequence or compute T2 mapping. Could you please check the code I wrote and help with mentioned issues.</p>
<p>Best!<br>
Ibraheem</p>

---

## Post #4 by @lassoan (2018-02-13 23:20 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="3" data-topic="2076">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>generate different nodes from the sequence or compute T2 mapping</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/moselhy/SlicerSequenceRegistration">SequenceRegistration extension</a> for an example for how to access, create, and modify volume sequences.</p>
<p>Do you plan to improve <a href="https://github.com/gattia/Slicer-T2mapping">T2 mapping extension</a>?</p>

---

## Post #5 by @brhoom (2018-02-14 07:36 UTC)

<p>Thanks for the reply and the info.<br>
I didn’t know that there is already such an extension, why it does not appear in Slicer’s extension manager?</p>
<p>I was planning to use Scipy to do the fitting so at the end I have only one file python code to make a simple portable Slicer plugin.<br>
I will check the links today.</p>
<p>Still (for the sake of knowledge), I don’t know what cause the issues in the code above. If I change this line:</p>
<pre><code>vma [i,j,k] =  vc[0]  
</code></pre>
<p>To be something like</p>
<pre><code>vma [i,j,k] =  0 
</code></pre>
<p>or</p>
<pre><code>vma [i,j,k] =  4000
</code></pre>
<p>In both situations, Slicer does not crash when I load the resulted volume in “Volume” module. It crashes only when I try to assign voxel value from the multi volume. I printed the value of vc[0] and it looks like a single scalar value (not a vector).</p>

---

## Post #6 by @lassoan (2018-02-14 14:30 UTC)

<p>When you copy between numpy arrays, numpy tries to do shallow copies. During shallow copying, numpy reallocates memory and shares it between arrays, which is a prohibited operation on the VTK-managed array that slicer.util.array returns. See more information <a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume">here</a>.</p>

---

## Post #7 by @brhoom (2018-02-14 15:26 UTC)

<p>Now it works, thanks for your continuous support.<br>
<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #8 by @lassoan (2018-02-14 16:51 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="5" data-topic="2076">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>why it does not appear in Slicer’s extension manager?</p>
</blockquote>
</aside>
<p>T2Mapping extension was only added to the latest master version of Slicer, which currently in a transitioning phase and so not all extensions are available.</p>
<p>I’ve now added T2mapping to the latest stable (4.8.1) extension index, so the T2mapping extension should show up tomorrow in stable version’s extension manager.</p>

---

## Post #9 by @brhoom (2018-02-14 17:21 UTC)

<p>Thanks for your concern. The extension is useful. but there is only one issue that the result is not shown after computation, something like this should be added to the end of the python file (in my case, I am interested in the Spine sagittal view):</p>
<pre><code>yellow_logic = slicer.app.layoutManager().sliceWidget("Yellow").sliceLogic()
yellow_cn = yellow_logic.GetSliceCompositeNode()
yellow_cn.SetBackgroundVolumeID(T2outputVolume.GetID())
lm = slicer.app.layoutManager()
lm.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUpYellowSliceView)

# Fit slice to window
sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
layoutManager = slicer.app.layoutManager()
for sliceNode in sliceNodes.values():
    sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())
    if sliceWidget:
        sliceWidget.sliceLogic().FitSliceToAll()    
logging.info('Processing completed')

return True</code></pre>

---

## Post #10 by @nirotu (2018-02-14 18:20 UTC)

<p>Hi Andras:</p>
<p>I do not see T2mapping extension in extension manager. Please, let me know how to find and load it.</p>
<p>thanks</p>
<p>Nirotu</p>

---

## Post #11 by @lassoan (2018-02-14 18:22 UTC)

<aside class="quote no-group" data-username="nirotu" data-post="10" data-topic="2076">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/439d5e/48.png" class="avatar"> nirotu:</div>
<blockquote>
<p>I do not see T2mapping extension in extension manager</p>
</blockquote>
</aside>
<p>It will appear in the extension manager of Slicer-4.8.1 version tomorrow. For nightly builds (4.9.x) it should show up in a couple of days.</p>

---

## Post #12 by @lassoan (2018-02-14 18:25 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="9" data-topic="2076">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>the result is not shown after computation</p>
</blockquote>
</aside>
<p>If you have any suggestion to improve the extension, please <a href="https://github.com/gattia/Slicer-T2mapping/pulls">submit a pull request</a> with your proposed changes.</p>
<p>Note that to show an image in slice viewers, you can use <em><a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.setSliceViewerLayers">slicer.util.setSliceViewerLayers</a></em> command.</p>

---

## Post #13 by @nirotu (2018-02-14 18:33 UTC)

<p>Thank you, Andras.</p>
<p>A<br>
Nirotu</p>

---
