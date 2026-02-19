---
topic_id: 6093
title: "Opgenigtlinkif How To Use Bindmessages"
date: 2019-03-10
url: https://discourse.slicer.org/t/6093
---

# OpgenIGTLinkIF: How to use BindMessages

**Topic ID**: 6093
**Date**: 2019-03-10
**URL**: https://discourse.slicer.org/t/opgenigtlinkif-how-to-use-bindmessages/6093

---

## Post #1 by @mcfly3001 (2019-03-10 19:58 UTC)

<p>Hi everyone,</p>
<p>I am trying to receive some data via OpenIGTLink with additional data added. For example I can already receive a vtkMRMLScalarVolumeNode but in this node I cannot include information about the patient (e.g. UID). In the overview page of OpenIGTLinkIF I found some information that BindMessages could solve the problem (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/OpenIGTLinkIF" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/OpenIGTLinkIF</a>).<br>
Unfortunately I have not found further information on how to use it and in the source files of the project I also hardly found any hints. Are BindMessages support via the Python-Interface at all?<br>
Anyone has a small example on how to use them?</p>
<p>Thanks!</p>

---

## Post #2 by @Sunderlandkyl (2019-03-10 23:18 UTC)

<p>The BindMessages are in the “Ideas” section. They have not been implemented.</p>
<p>The page is also out of date. The current source code is contained here: <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink</a>.</p>
<p>I can easily implement a mechanism to set node attributes from igtl message metadata if that would suit your purpose?</p>

---

## Post #3 by @lassoan (2019-03-10 23:40 UTC)

<p>Could you write a bit more about your use case? There can be many solutions and we would need to know what your preferences and constraints are. What kind of images do you send? How often? How often do metadata change?</p>
<p>You can already send patient metadata in a STRING message when you start a procedure. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>’s proposal of saving metadata as node attribute would be useful in general and may help in your case, too.</p>

---

## Post #4 by @mcfly3001 (2019-03-10 23:51 UTC)

<p>Hi,</p>
<p>Thanks for your reply. I almost thought that there is currently no such feature. But now I know for sure and can stop searching, thanks.</p>
<p>I am not sure whether your suggestion would help us in this case. We have a server running on another machine which processes data and then sends results (e.g. segmentation image) to our client. On client side we need to identify to which volume series the result belongs to. The server could send a message (Text) before or after the actual result for communicating the corresponding UID. But since the server is multi-threaded, results for different datasets could potentially arrive randomly.</p>
<p>Adding such info into somewhere in the metadata of the ogtl::ImageMessage is not possible, is it? Or is this what you are suggesting?</p>
<p>Thanks!</p>

---

## Post #5 by @mcfly3001 (2019-03-10 23:57 UTC)

<p>Hi again,</p>
<p>the use case I have just described partially in my last reply. Maybe you are right and it will be sufficient to send such data only if the currently processed patient is changing. On both machines we received new volume data via dicom nodes which shall be processed on the fly. Our client allows to load and view the data in Slicer, the server does some post-processing based on the volume and sends the results. We need to make sure that each result is assigned to the correct acquisition. But we can assume that new acquisitions are not made too often. So probably we simply send it once.</p>
<p>Thanks again for your replies!</p>
<p>Andreas</p>

---

## Post #6 by @lassoan (2019-03-13 23:27 UTC)

<p>You can identify volumes in Slicer based on the “device name” OpenIGTLink message field. This field is used as volume node name when Slicer receives the message. You can use any string, such as a randomly generated ID or by concatenation patient/study/series IDs. OpenIGTLink 2 has a limit of 20 characters but I think OpenIGTLink 3 has a mechanism to use longer device name.</p>

---

## Post #7 by @pfrwilson (2023-07-20 19:11 UTC)

<p>Hi All,</p>
<p>I am wondering if the solution of allowing node attributes to be sent as image metadata has been implemented?</p>
<p>My use case is that I have an AI inference listening to a pyigtl server. The AI model needs to know not just the pixel values of the image but other metadata from the image as well - specifically it needs to know the physical height and width of the image so it can select the appropriate ROIs to make predictions.</p>
<p>I think allowing node attributes to go through the OpenIGTLink as image metadata would be a good solution. My current workaround is to send text messages with serialized attribute dictionaries through the interface, but it is not the cleanest.</p>
<p>Paul</p>

---

## Post #8 by @lassoan (2023-07-20 22:32 UTC)

<aside class="quote no-group" data-username="pfrwilson" data-post="7" data-topic="6093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pfrwilson/48/66902_2.png" class="avatar"> pfrwilson:</div>
<blockquote>
<p>specifically it needs to know the physical height and width of the image</p>
</blockquote>
</aside>
<p>Physical height and width is already included in the basic IMAGE message (without that Slicer could not correctly display an image). Note that to define the image geometry, specifying spacing is not sufficient, but you also need to specify origin, spacing, axis directions.</p>
<p>You can also add any additional metadata to any message (in the <code>metadata</code> property of the message object in pyigtl) and I believe all metadata fields appear as MRML node attributes in Slicer.</p>

---

## Post #9 by @pfrwilson (2023-07-24 20:52 UTC)

<p>Hi Andras,</p>
<p>Thanks for your help!</p>
<p>“Physical height and width is already included in the basic IMAGE message (without that Slicer could not correctly display an image). Note that to define the image geometry, specifying spacing is not sufficient, but you also need to specify origin, spacing, axis directions.”</p>
<p>I did notice that the ijk to world matrix is included in the image message. However, I have not been using the ijk to world matrices in my slicer module but instead i’ve been using a transform to put the image into the correct coordinate system. I think Tamas told me it would be better to use a transform rather than touch the ijk to world matrices. Therefore the image message that OpenIGTLinkIF is sending to my python process is not getting the info about the image geometry that it needs. I guess I could send the transform that it is observing as another message to pyigtl.</p>
<p>“You can also add any additional metadata to any message (in the <code>metadata</code> property of the message object in pyigtl) and I believe all metadata fields appear as MRML node attributes in Slicer.”</p>
<p>This is a useful feature, but in my case I need to send metadata attributes from OpenIGTLinkIF to pyigtl, rather than the other way around.</p>
<p>Paul</p>

---

## Post #10 by @lassoan (2023-07-24 21:01 UTC)

<aside class="quote no-group" data-username="pfrwilson" data-post="9" data-topic="6093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pfrwilson/48/66902_2.png" class="avatar"> pfrwilson:</div>
<blockquote>
<p>I have not been using the ijk to world matrices in my slicer module but instead i’ve been using a transform to put the image into the correct coordinate system</p>
</blockquote>
</aside>
<p>It is more flexible if you send the image in the IJK coordinate system and the IJKTo?Transform and other transforms in separate messages. This flexibility is useful if you build a complex surgical guidance system with live images, various tracked tools, etc.</p>
<p>If all you need to send is an image in physical space then embedding origin, spacing, axis directions in the IMAGE message may be simpler.</p>
<aside class="quote no-group" data-username="pfrwilson" data-post="9" data-topic="6093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pfrwilson/48/66902_2.png" class="avatar"> pfrwilson:</div>
<blockquote>
<p>This is a useful feature, but in my case I need to send metadata attributes from OpenIGTLinkIF to pyigtl, rather than the other way around.</p>
</blockquote>
</aside>
<p>Slicer only sends a few selected MRML node attributes as OpenIGTLink message metadata (e.g., transform status). It wouldn’t be hard to generalize this (e.g., allow specifying a list of MRML node attribute names that would be included as metadata).</p>

---

## Post #11 by @pfrwilson (2023-07-24 21:07 UTC)

<p>Sounds good, I’ll use one of those two options. Do you have any examples of programs that use OpenIGTLinkIF for communicating with an AI server? Also, do you have any examples of Scripted modules that access the OpenIGTLinkIF logic to programatically set up connections?</p>
<p>Thanks again,</p>
<p>Paul</p>

---

## Post #12 by @lassoan (2023-07-25 01:42 UTC)

<aside class="quote no-group" data-username="pfrwilson" data-post="11" data-topic="6093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pfrwilson/48/66902_2.png" class="avatar"> pfrwilson:</div>
<blockquote>
<p>Do you have any examples of programs that use OpenIGTLinkIF for communicating with an AI server?</p>
</blockquote>
</aside>
<p>You can find examples at <a href="https://github.com/SlicerIGT/aigt" class="inline-onebox">GitHub - SlicerIGT/aigt: Deep learning software modules for image-guided medical procedures</a> Maybe <a class="mention" href="/u/ungi">@ungi</a> can make more specific recommendations.</p>
<aside class="quote no-group" data-username="pfrwilson" data-post="11" data-topic="6093">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pfrwilson/48/66902_2.png" class="avatar"> pfrwilson:</div>
<blockquote>
<p>Also, do you have any examples of Scripted modules that access the OpenIGTLinkIF logic to programatically set up connections?</p>
</blockquote>
</aside>
<p>All you need to do is to create a <code>vtkMRMLIGTLConnectorNode</code> and set its properties. You can find examples for this in the AIGT repository, too.</p>

---

## Post #13 by @ungi (2023-07-25 12:48 UTC)

<p>There are some specific examples. These are very new and subject to change once we organize them better. Running segmentation on an AI “server”: <a href="https://github.com/SlicerIGT/aigt/blob/master/UltrasoundSegmentation/RealtimeInferenceOverOpenIGTLink.py" rel="noopener nofollow ugc">aigt/UltrasoundSegmentation/RealtimeInferenceOverOpenIGTLink.py at master · SlicerIGT/aigt (github.com)</a></p>
<p>And look at files that start as “RealTime…” here: <a href="https://github.com/SlicerIGT/aigt/tree/Ultrasound-object-detection/UltrasoundObjectDetection" rel="noopener nofollow ugc">aigt/UltrasoundObjectDetection at Ultrasound-object-detection · SlicerIGT/aigt (github.com)</a></p>

---
