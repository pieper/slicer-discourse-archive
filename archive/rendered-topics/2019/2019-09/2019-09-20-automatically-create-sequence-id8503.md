---
topic_id: 8503
title: "Automatically Create Sequence"
date: 2019-09-20
url: https://discourse.slicer.org/t/8503
---

# Automatically create sequence

**Topic ID**: 8503
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/automatically-create-sequence/8503

---

## Post #1 by @rbahegne (2019-09-20 09:55 UTC)

<p>Hello, I’ve installed the sequence extension and its work fine.</p>
<p>Currently i’m working on a module to receive via a specific siemens API, MRI images (dicom format) and displaying them in real time.</p>
<p><strong>1) First question :</strong></p>
<p>I’m displaying data on a node, so setting it as a proxy node works fine, but i would like to automate it so that when the first data arrive a new sequence is created and the proxy node is setted. (The node is create as the first data arrives).</p>
<p>I found in the sequence browser logic source code promising function, but i did not manage to access it from my own module, and i’m not sure it’s the right way to do it. What do you recommend ?</p>
<p><strong>2) Second question :</strong></p>
<p>I’ve also tried building multivolume wich works quite fine but need a few more processing for the data. I’ve tried both solutions (multi and sequence) and they seems to give equal result  (for displaying) for 10 images/sec (I display volume (ie do a “SetAndObserveImageData”) only when full, so roughtly two by second). But when i tried with a higher image rate like 20 images/sec the slicer app freeze or crash.</p>
<p>-Is it to be expected ? I’m not sure how the render is done in slicer, so i’m not sure how much stress i put on the app.<br>
-Doing a  SetAndObserveImageData on the volume or multivolume node is the right way for this ? I saw that streamNode exist but didn’t find much doc on it.<br>
-Should I use a timer to do a display at a fixed rate, not matter the rate of images received?</p>
<p>That a lot of questions, thank you for your assistance.</p>

---

## Post #2 by @Sam_Horvath (2019-09-20 13:39 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="1" data-topic="8503">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>I found in the sequence browser logic source code promising function, but i did not manage to access it from my own module, and i’m not sure it’s the right way to do it. What do you recommend ?</p>
</blockquote>
</aside>
<p>Can you share a code snippet of what you tried in your own module, and any resulting error(s)?</p>

---

## Post #3 by @rbahegne (2019-09-20 13:50 UTC)

<p>I did something like this after including vtkSlicerSequenceBrowserLogic.h :</p>
<blockquote>
<p>qSlicerAbstractCoreModule* SequenceBrowserModule =<br>
qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module(“SequenceBrowser”);<br>
if (!SequenceBrowserModule)<br>
{<br>
qCritical() &lt;&lt; “SequenceBrowserModule module is not found”;<br>
return;<br>
}<br>
vtkSlicerSequenceBrowserLogic* SequenceBrowserLogic =<br>
vtkSlicerSequenceBrowserLogic::SafeDownCast(SequenceBrowserModule-&gt;logic());<br>
if (!SequenceBrowserLogic)<br>
{<br>
qCritical() &lt;&lt; “SequenceBrowserModule logic is not found”;<br>
return;<br>
}</p>
<p>SequenceBrowserLogic-&gt;“AnyFunction”</p>
</blockquote>
<p>Compilation said i could not access to logic. Maybe it’s just a cmake problem, my project have 3 subdirectory : mine (SiCo) , sequences and sequenceBrowser.</p>

---

## Post #4 by @Sam_Horvath (2019-09-20 14:06 UTC)

<p>So i think that this part is a CMake issue.  In order to use the logic of another loadable modules, you need to link them in the CMake.  See <a href="https://github.com/Slicer/Slicer/blob/659f1c0b8f75e8c3358e9bddd3e04cc6ee179375/Modules/Loadable/CropVolume/Logic/CMakeLists.txt#L20" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/659f1c0b8f75e8c3358e9bddd3e04cc6ee179375/Modules/Loadable/CropVolume/Logic/CMakeLists.txt#L20</a>  for an example.</p>

---

## Post #5 by @cpinter (2019-09-20 14:59 UTC)

<p>Here’s an example for how to use a module logic class from another module logic class:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L53" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L53" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/master/DicomRtImportExport/Logic/vtkSlicerDicomRtImportExportModuleLogic.cxx#L53</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="43" style="counter-reset: li-counter 42 ;">
<li>// SubjectHierarchy includes
</li>
<li>#include "vtkMRMLSubjectHierarchyConstants.h"
</li>
<li>#include "vtkMRMLSubjectHierarchyNode.h"
</li>
<li>#include "vtkSlicerSubjectHierarchyModuleLogic.h"
</li>
<li>
</li>
<li>// SlicerRT includes
</li>
<li>#include "vtkSlicerRtCommon.h"
</li>
<li>#include "PlmCommon.h"
</li>
<li>#include "vtkMRMLIsodoseNode.h"
</li>
<li>#include "vtkMRMLPlanarImageNode.h"
</li>
<li class="selected">#include "vtkSlicerIsodoseModuleLogic.h"
</li>
<li>#include "vtkSlicerPlanarImageModuleLogic.h"
</li>
<li>#include "vtkSlicerBeamsModuleLogic.h"
</li>
<li>#include "vtkMRMLRTPlanNode.h"
</li>
<li>#include "vtkMRMLRTBeamNode.h"
</li>
<li>
</li>
<li>// Segmentations includes
</li>
<li>#include "vtkMRMLSegmentationNode.h"
</li>
<li>#include "vtkMRMLSegmentationDisplayNode.h"
</li>
<li>#include "vtkMRMLSegmentationStorageNode.h"
</li>
<li>#include "vtkSlicerSegmentationsModuleLogic.h"
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Just search for this class name. You will find that the instance is set from the module class at setup time.</p>

---

## Post #6 by @lassoan (2019-09-21 15:14 UTC)

<p>It may be simpler to just activate sequence recording (create a sequence browser node, set the input proxy node, and enable recording). Then, whenever you receive a new volume, you just update the proxy volume with it. The new volume will be automatically added to the sequence. You don’t need to call sequence module logic functions at all.</p>
<p>This is how we record live images and tool tracking information in all real-time navigation applications. See <a href="http://www.slicerigt.org" rel="nofollow noopener">www.slicerigt.org</a> for examples and tutorials.</p>

---

## Post #7 by @rbahegne (2019-09-23 07:52 UTC)

<blockquote>
<p>It may be simpler to just activate sequence recording (create a sequence browser node, set the input proxy node, and enable recording). Then, whenever you receive a new volume, you just update the proxy volume with it. The new volume will be automatically added to the sequence. You don’t need to call sequence module logic functions at all.</p>
</blockquote>
<p>I did try it and it work well, but the thing is that before the transmission begin there no nodes to set as proxy. The node where the data is displayed is automatically created as we received data. So during the transmission I need to set the proxy node and record, which is not really convenient, and doing this I miss the beginning of the transmission.</p>
<p>I really can’t create the node before receiving the transmission, because i can received an unknown amount of serie data and i need to create one node per serie data.</p>

---

## Post #8 by @lassoan (2019-09-23 11:45 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="7" data-topic="8503">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>The node where the data is displayed is automatically created as we received data.</p>
</blockquote>
</aside>
<p>Do you use OpenIGTLink? Which module creates the node automatically?</p>
<aside class="quote no-group" data-username="rbahegne" data-post="7" data-topic="8503">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>i can received an unknown amount of serie data</p>
</blockquote>
</aside>
<p>You only need to create one proxy node for an entire sequence.</p>
<p>We also have an OpenIGTLink implementation for receiving real-time images from Siemens MRI scanners and also control the scan plane position and orientation from Slicer. Probably it uses the same protocol that you do. If interested, contact <a class="mention" href="/u/tokjun">@tokjun</a>.</p>

---

## Post #9 by @rbahegne (2019-09-24 09:50 UTC)

<p>Thank you for your answer,</p>
<p>The module that create the node is the one i am currently developping. It is a little bit similar than OpenIGTLink but the communication with the MRI is via a specific API using http protocol to open a websocket connection.</p>
<p>Then i receive dicom images of module, phase and temperature. I sort them on the fly and display reconstructed volumes, tring to do it in real time.</p>
<p>I did manage to create sequence and record automatically. But i’m still working on second question : when the rate of display is high (something like displaying 2 volumes of 5 slices every 250 ms) the app crash or freeze. In the sequence solution i’m using regular vtkMRMLScalarVolumeNode updated by a SetAndObserveImageData .</p>
<p>I don’t know if it adapted to this kind of stream, i saw that a vtkMRMLStreamingVolumeNode exist, could you tell me if more adapted and if there is difficulties to use it ?</p>

---

## Post #10 by @lassoan (2019-09-24 13:05 UTC)

<aside class="quote no-group" data-username="rbahegne" data-post="9" data-topic="8503">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbahegne/48/4837_2.png" class="avatar"> rbahegne:</div>
<blockquote>
<p>I did manage to create sequence and record automatically. But i’m still working on second question : when the rate of display is high (something like displaying 2 volumes of 5 slices every 250 ms) the app crash or freeze</p>
</blockquote>
</aside>
<p>If processing takes too long time then response time of the application may get worse but crash should never happen. Crash indicates that there is a bug in your module. Do you receive the images on a different thread? Do you use mutexes to communicate with the main thread? I see two potential solutions:</p>
<ul>
<li>Option A: The simple one. Create a small standalone application that receives images from Siemens and sends it to Slicer through OpenIGTLink. You only need to link your small application to OpenIGTLink library. No need to use threading! Slicer’s OpenIGTLinkIF module can already receive images (and real-time tracking, sensor, etc. information) on a background thread and pass it to the main thread robustly and efficiently. This is how we usually implement real-time communication with hardware devices, which use proprietary communication protocol and not OpenIGTLink interface.</li>
<li>Option B: The complicated one. Create a loadable module, which communicates with the scanner on background threads. When you you received an image, put it in a thread-safe queue and signal the main thread that you have received new data. In the main thread, retrieve the dataset from the queue and set it in a node in the scene.</li>
</ul>
<p>vtkMRMLStreamingVolumeNode is only useful if you receive compressed data stream and you want to store the compressed stream while viewing the uncompressed images on screen.</p>
<p>What is the name and version of the protocol that you use with the Siemens scanner? As I wrote above, we may already have a working solution.</p>
<p><a class="mention" href="/u/tokjun">@tokjun</a> - can you give some information about the Siemens MRI real-time image receving/scan plane control interface that you developed?</p>

---

## Post #11 by @rbahegne (2019-09-24 13:26 UTC)

<p>Thank you for this detailed answer, the web socket communication is in separate tread. I may need a few more mutexes indeed.</p>
<p>The protocol used is SRC (Scanner Remote Toolkit), i read OpenIGTLInk Doc and I did’nt found anything about it. Also a possible issue is that i received images of Module, Phase and Temperature, in a mixed order, that’s the main reason i developped my own module, i need to sort them as i receive them.</p>
<p>I’ve contacted tokjun and i’m waiting an anwser.</p>

---
