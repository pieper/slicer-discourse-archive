---
topic_id: 1233
title: "Vtkmrmlfiberbundlenode Transmission Via Openigtlinkif"
date: 2017-10-17
url: https://discourse.slicer.org/t/1233
---

# vtkMRMLFiberBundleNode Transmission via OpenIGTLinkIF

**Topic ID**: 1233
**Date**: 2017-10-17
**URL**: https://discourse.slicer.org/t/vtkmrmlfiberbundlenode-transmission-via-openigtlinkif/1233

---

## Post #1 by @leochan2009 (2017-10-17 00:37 UTC)

<p>Dear Slicer Developers,</p>
<p>I am trying to extend OpenIGTLinkIF module to transmit the tractography.<br>
The tracts are vtkMRMLFiberBundleNode data, which is a derived class from vtkMRMLModelNode.<br>
The OpenIGTLinkIF module is able to transmit vtkMRMLModelNode.<br>
To make it work on vtkMRMLFiberBundleNode, i need to include the vtkMRMLFiberBundleNode.h file.<br>
Unfortunately the vtkMRMLFiberBundleNode is defined in SlicerDMRI extension.<br>
I could include the SlicerDMRI library, but then OpenIGTLinkIF module will depend on SlicerDMRI.</p>
<p>Do you think it might be possible to merge the mrmlNode define in the following link into Slicer trunk?<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/Loadable/TractographyDisplay/MRML" rel="nofollow noopener">SlicerDMRI mrmlNodes</a></p>
<p>Thanks in advance!</p>
<p>Best,<br>
Longquan</p>

---

## Post #2 by @lassoan (2017-10-17 01:08 UTC)

<p>IGTL converters for special nodes should be specified in the extension where those special nodes are defined (in SlicerDMRI).</p>
<p>For example, these design options could be used for handling vktMRMLFiberBundleNode conversion without introducing dependencies between extensions:</p>
<ul>
<li>Option A: Add a new OpenIGTLink device type (FIBERBUNDLE) which would encode its content the same way as a POLYDATA. You may even decide to only include those POLYDATA fields which make sense for fiber bundles.</li>
<li>Option B: introducing a new “confidence” parameter in the IGTL converters. (similarly to file IO and DICOM plugins)</li>
</ul>

---

## Post #3 by @leochan2009 (2017-10-17 01:15 UTC)

<p>Thanks Andras,</p>
<p>I will take a look into the IO and DICOM plugins for more information!<br>
Best,<br>
Longquan</p>

---

## Post #4 by @lassoan (2017-10-17 01:28 UTC)

<p>Fiber bundles are not really models. The design of using vtkMRMLModelNode as a base class of vtkMRMLFiberBundle node is not clean at all (requires many workarounds throughout Slicer code to make it work), but considering that it allowed relatively simple implementation, it somewhat makes sense.</p>
<p>However, it would be better if this questionable design choice would not be further propagated to OpenIGTLink as well. It would be much cleaner to have a new OpenIGTLink device (message) type for this distinct data type.</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> What do you think?</p>

---

## Post #5 by @ihnorton (2017-10-17 14:36 UTC)

<p>I don’t think depending on vtkMRMLFiberBundleNode.h would be very helpful. It should be sufficient to work with <code>vtkMRMLModelNode::GetPolyData</code> output, but dispatch to custom encoding when <code>IsA("vtkMRMLFiberBundleNode")</code>. The polydata will have all the points and cells to identify streamlines. If you need the secondary data (e.g. tensors or measurements along the tracts) those are stored as named arrays.</p>
<p>That said, I’m a bit curious what is the use-case; who needs this? There are already several other ways to get these nodes out to external software: CLIs, Steve’s MRML server setup, DICOM server (and probably others). Plain streamlines are pretty simple, but beyond that there’s a lot of complexity which has already been extensively considered in <a href="http://dicom.nema.org/Dicom/News/June2015/docs/sups/sup181.pdf">DICOM</a> so I would suggest carefully considering whether it makes sense to recapitulate that specification.</p>

---

## Post #6 by @ihnorton (2017-10-17 15:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="1233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> What do you think?</p>
</blockquote>
</aside>
<p>I agree with your assessment of the design.</p>
<p>As far as OpenIGTLink, looking at the <a href="https://github.com/openigtlink/OpenIGTLink/tree/master/Documents/Protocol">protocol</a>, I think all the necessary data <em>could</em> be represented in the existing message types (POLYDATA for lines, NDARRAY for tensors and everything else). Whether it’s worth doing an ad-hoc naming scheme with existing message types or adding a tractography message type to the spec  depends on the application and the desired direction of OpenIGTLink.</p>

---

## Post #7 by @leochan2009 (2017-10-17 15:51 UTC)

<p>Thanks both.<br>
I totally agree that it really depends on the application and desired direction of OpenIGTLink.<br>
The issue is the mismatch between the OpenIGTLink message type and the mrml node.<br>
All mrmlNode can be represented in exsiting message types, but several different nodes could be represented in one message type(such as vtkMRMLFiberBundleNode and vtkMRMLModelNode are both represented in igtlPolyDataMessage type). Once the client receive the igtlPolyDataMessage, it needs additional steps to decide which node to choose to represent/visualize the data.<br>
A tractography message derived from igtlPolyDataMessage could be a solution.<br>
I will discuss with Junichi regarding this question.</p>

---

## Post #8 by @ihnorton (2017-10-17 16:11 UTC)

<p>Just to add: for receiving I think you can still avoid the dependency by using <code>vtkMRMLScene::CreateNodeByClass("vtkMRMLFiberBundleNode")</code> to create the node if SlicerDMRI is installed, then <code>SetPolyData</code> after deserialization.</p>
<p>(if SlicerDMRI is not installed then fall back to <code>vtkMRMLModelNode</code> and likewise <code>SetPD</code> – the streamlines should display fine as lines, but won’t have measurement-coloring or extended glyphing options provided by the FiberBundleDisplayNode* classes)</p>
<aside class="quote no-group" data-username="leochan2009" data-post="7" data-topic="1233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leochan2009/48/519_2.png" class="avatar"> leochan2009:</div>
<blockquote>
<p>Once the client receive the igtlPolyDataMessage, it needs additional steps to decide which node to choose to represent/visualize the data.</p>
</blockquote>
</aside>
<p>Right, that question is either a protocol change or application-specific interpretation of certain naming convention when deciding how to deserialize. (and FWIW, making that choice shouldn’t involve SlicerDMRI headers as far as I can understand)</p>

---

## Post #9 by @leochan2009 (2017-10-17 16:46 UTC)

<p>Hi Isaiah,</p>
<p>Thanks a lot for your adding!</p>

---

## Post #10 by @leochan2009 (2017-10-17 23:13 UTC)

<p>Hi Andras, Hi lsaiah,</p>
<p>Thanks for your kind suggestions,<br>
I just make some commits in OpenIGTLinkIF module.<br>
Once these commits are integrated, 3D slicer will be able to transmit fiberbundle data between machines <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>
<p>Best,<br>
Longquan</p>

---
