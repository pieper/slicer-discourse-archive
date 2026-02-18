# How Can I use python to get the status of a node's show/hides status in the "data" or "DICOM" module in the Subject hierarchy area?

**Topic ID**: 12786
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/how-can-i-use-python-to-get-the-status-of-a-nodes-show-hides-status-in-the-data-or-dicom-module-in-the-subject-hierarchy-area/12786

---

## Post #1 by @Tesla2687 (2020-07-30 05:41 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Using python to get the status of a node’s show/hides status in the “data” or “DICOM” module in the Subject hierarchy area?<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f389728721b96b1a878c88222cabcd9d575a0d61.jpeg" data-download-href="/uploads/short-url/yKqvj4hEw0a5N0KRMcAKAlPnugN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f389728721b96b1a878c88222cabcd9d575a0d61_2_690x347.jpeg" alt="image" data-base62-sha1="yKqvj4hEw0a5N0KRMcAKAlPnugN" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f389728721b96b1a878c88222cabcd9d575a0d61_2_690x347.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f389728721b96b1a878c88222cabcd9d575a0d61.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f389728721b96b1a878c88222cabcd9d575a0d61.jpeg 2x" data-dominant-color="B8BDC2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">861×434 78.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2020-07-30 08:32 UTC)

<p>Volumes work quite differently in terms of visibility than any other type, so simple <code>GetDisplayVisibility()</code> won’t work.</p>
<p>However, if you take a look at how the subject hierachy itself decides if it’s visible, that should help:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L353-L356" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L353-L356" target="_blank" rel="noopener">Slicer/Slicer/blob/master/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L353-L356</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="353" style="counter-reset: li-counter 352 ;">
<li>QSet&lt;vtkIdType&gt; shownVolumeItemIDs;</li>
<li>this-&gt;collectShownVolumes(shownVolumeItemIDs);</li>
<li>
</li><li>if (shownVolumeItemIDs.contains(itemID))</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Tesla2687 (2020-07-30 08:38 UTC)

<p>Hello cpinter,</p>
<p>Thank you very much for your help. I will try it later~</p>
<p>Tesla</p>

---

## Post #4 by @Tesla2687 (2020-07-30 23:59 UTC)

<p>Hi Csaba,</p>
<p>I can’t found a python api of this function. Because I am using python to develop.</p>
<p>Thanks again anyway.</p>
<p>Tesla</p>

---

## Post #5 by @Tesla2687 (2020-07-31 00:16 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view</a></p>
<p>In here I found an example may help, But I can’t make it work, is there anyone can help me to check if this block of example works or not?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9faa4717b7e04b2263a80a7021d52dd2568661f.png" data-download-href="/uploads/short-url/sOMY9XrAtHDWAtWYAVB0y3MY2MT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9faa4717b7e04b2263a80a7021d52dd2568661f_2_690x245.png" alt="image" data-base62-sha1="sOMY9XrAtHDWAtWYAVB0y3MY2MT" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9faa4717b7e04b2263a80a7021d52dd2568661f_2_690x245.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9faa4717b7e04b2263a80a7021d52dd2568661f_2_1035x367.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9faa4717b7e04b2263a80a7021d52dd2568661f_2_1380x490.png 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1448×515 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-07-31 02:53 UTC)

<p>If you are interested if a volume is visible in any of the slice views then you can iterate through the <code>vtkMRMLSliceCompositeNode</code> nodes in the scene and check if the volume matches the foreground or background volume, as you can see it in the code snippet that <a class="mention" href="/u/cpinter">@cpinter</a> referred to:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/100b7432cc6d31a1eb7f89a723e61f0d73eedd22/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L507-L526" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/100b7432cc6d31a1eb7f89a723e61f0d73eedd22/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L507-L526" target="_blank" rel="noopener">Slicer/Slicer/blob/100b7432cc6d31a1eb7f89a723e61f0d73eedd22/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L507-L526</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="507" style="counter-reset: li-counter 506 ;">
<li>vtkMRMLSliceCompositeNode* compositeNode = nullptr;</li>
<li>const int numberOfCompositeNodes = scene-&gt;GetNumberOfNodesByClass("vtkMRMLSliceCompositeNode");</li>
<li>for (int i=0; i&lt;numberOfCompositeNodes; i++)</li>
<li>  {</li>
<li>  compositeNode = vtkMRMLSliceCompositeNode::SafeDownCast( scene-&gt;GetNthNodeByClass( i, "vtkMRMLSliceCompositeNode" ) );</li>
<li>  if ( layer &amp; vtkMRMLApplicationLogic::BackgroundLayer</li>
<li>    &amp;&amp; compositeNode-&gt;GetBackgroundVolumeID() &amp;&amp; strcmp(compositeNode-&gt;GetBackgroundVolumeID(),"") )</li>
<li>    {</li>
<li>    shownVolumeItemIDs.insert(shNode-&gt;GetItemByDataNode( scene-&gt;GetNodeByID(compositeNode-&gt;GetBackgroundVolumeID())) );</li>
<li>    }</li>
<li>  if ( layer &amp; vtkMRMLApplicationLogic::ForegroundLayer</li>
<li>    &amp;&amp; compositeNode-&gt;GetForegroundVolumeID() &amp;&amp; strcmp(compositeNode-&gt;GetForegroundVolumeID(),"") )</li>
<li>    {</li>
<li>    shownVolumeItemIDs.insert(shNode-&gt;GetItemByDataNode( scene-&gt;GetNodeByID(compositeNode-&gt;GetForegroundVolumeID())) );</li>
<li>    }</li>
<li>  if ( layer &amp; vtkMRMLApplicationLogic::LabelLayer</li>
<li>    &amp;&amp; compositeNode-&gt;GetLabelVolumeID() &amp;&amp; strcmp(compositeNode-&gt;GetLabelVolumeID(),"") )</li>
<li>    {</li>
<li>    shownVolumeItemIDs.insert(shNode-&gt;GetItemByDataNode( scene-&gt;GetNodeByID(compositeNode-&gt;GetLabelVolumeID())) );</li>
<li>    }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>In Python, you can use this convenience method to get all the slice composite nodes:</p>
<pre><code>compositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')</code></pre>

---

## Post #7 by @Tesla2687 (2020-07-31 03:19 UTC)

<p>Hello lassoan,</p>
<p>Thank you very much, This method works well. According to your method, I Can get the current volumeNode by Script, like the picture shows below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7300df7cb7ead950e44de864bd4e7041997e7b32.png" data-download-href="/uploads/short-url/gpmMklYoTKLseB6vu9gfsX0Y6R4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7300df7cb7ead950e44de864bd4e7041997e7b32_2_690x183.png" alt="image" data-base62-sha1="gpmMklYoTKLseB6vu9gfsX0Y6R4" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7300df7cb7ead950e44de864bd4e7041997e7b32_2_690x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/7300df7cb7ead950e44de864bd4e7041997e7b32_2_1035x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7300df7cb7ead950e44de864bd4e7041997e7b32.png 2x" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1377×366 59.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Further more, I want to observe the ModifiedEvent (When the status changed from hide to show,or change to another volume). I failed to make it successful. Could you help me check is there any error in this function below?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e7a1f9d784dff2afeb3147dbba1cf95c991c66e.png" data-download-href="/uploads/short-url/244kDWiruhXWRpMvvlVJo6mpyay.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e7a1f9d784dff2afeb3147dbba1cf95c991c66e_2_690x172.png" alt="image" data-base62-sha1="244kDWiruhXWRpMvvlVJo6mpyay" width="690" height="172" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e7a1f9d784dff2afeb3147dbba1cf95c991c66e_2_690x172.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e7a1f9d784dff2afeb3147dbba1cf95c991c66e_2_1035x258.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e7a1f9d784dff2afeb3147dbba1cf95c991c66e.png 2x" data-dominant-color="EDEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1288×322 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-07-31 03:54 UTC)

<p>You need to add observers to all slice composite nodes if you want to get notified when a different volume gets visualized in any of the slice viewers.</p>
<p>Why do you need to continuously monitor when the user changed the displayed volume? It is usually not necessary.</p>

---

## Post #9 by @Tesla2687 (2020-07-31 06:32 UTC)

<p>Hello lassoan,</p>
<p>Thank you for your quickly reply. I can’t really understand how to implement what you said. Could you give me an example code?</p>
<p>I would like to process the current show volume and display the processed volume in “Slice4” and “Yellow” View Simultaneously, please see the picture below. So I need to know the current show volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb3d4436dfb741f8346cefb8c27ab180c51a6bc.jpeg" data-download-href="/uploads/short-url/fNjNQk9qtaChFTjUDy5diid6vEM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb3d4436dfb741f8346cefb8c27ab180c51a6bc_2_690x357.jpeg" alt="image" data-base62-sha1="fNjNQk9qtaChFTjUDy5diid6vEM" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb3d4436dfb741f8346cefb8c27ab180c51a6bc_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6eb3d4436dfb741f8346cefb8c27ab180c51a6bc_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb3d4436dfb741f8346cefb8c27ab180c51a6bc.jpeg 2x" data-dominant-color="2C2C2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1261×653 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2020-07-31 13:58 UTC)

<p>Do you have questions about how to set which volume is visible in which slice? Or you are unsure about how to detect when user selects a different volume for display in a slice view?</p>
<p>What is your overall goal?  What is the workflow you are trying to implement?</p>

---

## Post #11 by @Tesla2687 (2020-08-01 01:48 UTC)

<p>Hello lassoan,</p>
<p>1、Do you have questions about how to set which volume is visible in which slice?<br>
I don’t have this question. I know How to do this actually.</p>
<p>2、Or you are unsure about how to detect when user selects a different volume for display in a slice view?<br>
Yes, I would like to observe the change event of volume in “Subject hierarchy”.</p>
<p>3、What is your overall goal? What is the workflow you are trying to implement?<br>
I would like to observe the modify-event of the current volume, and process the volume, and put the processed volume in “Slice4” and “Yellow” view.</p>
<p>Thank you very much</p>

---

## Post #12 by @lassoan (2020-08-01 04:23 UTC)

<p>Instead of trying to figure out what volume the user looks at, I would recommend to add an input and output volume node selector (as it is done in all other modules). If you want to a simplified user interface, then I would recommend to allow the user to select input volume only in your module (not using slicer view controllers, not using Data module, etc.).</p>

---

## Post #13 by @Tesla2687 (2020-08-01 12:45 UTC)

<p>Hello lassoan,</p>
<p>I would like to make the User Interface looks friendly and concisely. So I don’t want to use input volume simply.</p>
<p>Thanks~</p>

---

## Post #14 by @lassoan (2020-08-01 13:42 UTC)

<p>My suggestion for a simplified GUI would be to not let the user switch between modules or access slice view controllers, but your module would select a volume to display (or if you have multiple volumes loaded, the user would select the current volume in your module).</p>
<p>If you described your workflow in more detail then we can give more specific advice.</p>

---

## Post #15 by @Tesla2687 (2020-08-04 03:10 UTC)

<p>Thank you very much for your help. <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/cpinter">@cpinter</a>. I have found a method to implement my idea.<br>
please check the code below.</p>
<pre><code>#Observe the change of the current volume
lastVolumeNodeID=''
def toDoSomethingInCurrentVolume(caller=None,event=None):
    global lastVolumeNodeID
    layoutManager = slicer.app.layoutManager()
    redCompsiteNode=layoutManager.sliceWidget("Red").sliceLogic().GetSliceCompositeNode()
    redVolumeID = redCompsiteNode.GetBackgroundVolumeID()
    if lastVolumeNodeID==redVolumeID:
        return 
    elif :
        redBackgroundVolumeNode=slicer.mrmlScene.GetNodeByID(redVolumeID)
        process(redBackgroundVolumeNode)
    
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
shNode.AddObserver(shNode.SubjectHierarchyItemModifiedEvent,toDoSomethingInCurrentVolume)</code></pre>

---

## Post #16 by @lassoan (2020-08-04 12:18 UTC)

<p>Thanks for sharing the solution that worked for you.</p>

---
