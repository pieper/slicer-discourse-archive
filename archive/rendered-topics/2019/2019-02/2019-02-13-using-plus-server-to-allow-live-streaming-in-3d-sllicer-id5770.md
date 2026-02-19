---
topic_id: 5770
title: "Using Plus Server To Allow Live Streaming In 3D Sllicer"
date: 2019-02-13
url: https://discourse.slicer.org/t/5770
---

# Using Plus Server to allow live streaming in 3D sllicer

**Topic ID**: 5770
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/using-plus-server-to-allow-live-streaming-in-3d-sllicer/5770

---

## Post #1 by @dsikka (2019-02-13 22:38 UTC)

<p>We’re trying to get live streaming in 3D slicer using Plus Server but we’re having a bit of trouble. We tried to follow the instructions under <code>Show live images in 3D Slicer</code> on this link: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ProcedureStreamingToSlicer.html" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ProcedureStreamingToSlicer.html</a> but were not able to get live streaming. Essentially, we launch Slicer without anything else, load an Image Reference mentioned in the link above and then follow the steps.</p>
<p>We’re currently using the Plus Server Launcher and in the instructions it refers to an Image Reference. We used the <code>Image_Image.nrrd</code>file. We’re not sure if we’re missing a step or doing something incorrectly?</p>

---

## Post #2 by @Sunderlandkyl (2019-02-13 23:03 UTC)

<p>That document is a bit out of date.<br>
In Slicer 4.10+, you need to download the SlicerOpenIGTLink extension to get access to OpenIGTLinkIF.</p>
<p>What config file are you using in Plus?</p>

---

## Post #3 by @dsikka (2019-02-14 01:02 UTC)

<p>We are using the OpenIGTLinkIF module in order to set up our connection however, the steps we followed in how we used it were based on the link above.</p>
<p>The config file we’re using within Plus Server is the following xml: <code>PlusDeviceSet_Server_OpticalMarkerTracker_Mmf</code>. Should we be using another one?</p>

---

## Post #4 by @Sunderlandkyl (2019-02-14 01:21 UTC)

<p>With that config file, you need to create two connectors.</p>
<ol>
<li>Port 18944 – Transmits transforms for Optical markers</li>
<li>Port 18945 – Transmits webcam as image called “Image_Image”</li>
</ol>
<p>If you encounter other issues with Plus, could you submit an issue on the Plus github page and attach the Plus log file?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PlusToolkit/PlusLib/issues/new">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PlusToolkit/PlusLib/issues/new" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/337b7cc06184984e148c075df20ef009e0e6ecaa.png" class="thumbnail onebox-avatar" width="500" height="500" data-dominant-color="E1E1E1">

<h3><a href="https://github.com/PlusToolkit/PlusLib/issues/new" target="_blank" rel="noopener nofollow ugc">Build software better, together</a></h3>

  <p>GitHub is where people build software. More than 100 million people use GitHub to discover, fork, and contribute to over 330 million projects.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @LWRwada (2024-05-02 08:44 UTC)

<p>Hi, Sunderlandkyl!<br>
I always tried the function of “PlusServer: Video for Windows video capture device”. But when I connect the US device, I found the directions of that figure on 3D Slicer and on US device are upside-down. For the better presentation of US imaging data, I tried the “Transform” on Slicer, but it didn’t work <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_tear.png?v=12" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20"><br>
So, could u offer me some solutions?</p>

---

## Post #6 by @Sunderlandkyl (2024-05-02 13:29 UTC)

<p>You can update “PortUsImageOrientation” to quickly flip the image.<br>
See possible orientations here: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/UltrasoundImageOrientation.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Ultrasound image orientation</a></p>

---

## Post #7 by @LWRwada (2024-05-06 08:27 UTC)

<p>Thanks, Kyle! And sorry for the late reply.<br>
But actually, I only have the Cannon US device (which was not included in the list of supported devices). So, I just assumed the US probe as the video capture tool for testing the function of "PlusServer: Video for Windows video capture device”. Then, the images showed upside-down.<br>
Then, I also tried the method you told me, the fCal. It doesn’t work. But I found the “Volume Reslice Driver” can flip the image, which may not show the actual orientation ( I guess?).</p>
<p>Sorry, one more question. The most attractive points of PLUS toolkit are the function of volume reconstruction and the flexible application of different devices. And now we have the Cannon US device and the robotic arm. Both of them were not included in the supported devices. I was wondering if that is possible to utilize PLUS toolkit to help me to realize the volume reconstruction in real-time under the assistance of robotic arm. Thank you for your time and consideration again!</p>

---

## Post #8 by @Sunderlandkyl (2024-05-06 16:02 UTC)

<p>Are you tracking the ultrasound or sending the transforms from the robotic arm to Plus or Slicer? If the ultrasound is tracked in some way, then you should be able to do live volume reconstruction with the current setup.</p>

---

## Post #9 by @LWRwada (2024-05-11 08:31 UTC)

<p>Sorry for the late reply. Actually, we just bond the US probe and robotic arm together, which means the spatial data of US probe can be obtained by the robotic arm.<br>
And, I will try to follow the setup to do the live volume reconstruction. Thank you so much~~~</p>

---
