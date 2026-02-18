# Live image transfer via TCP/IP

**Topic ID**: 4866
**Date**: 2018-11-26
**URL**: https://discourse.slicer.org/t/live-image-transfer-via-tcp-ip/4866

---

## Post #1 by @shellyverde (2018-11-26 02:22 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8</p>
<p>Hi,</p>
<p>I need to connect a device with Slicer through TCP/IP socket connection. The device runs in real time and the data from the device need to be sent to Slicer in every certain milliseconds. Meanwhile commands will send to the device through Slicer. Could you please suggest how to implement the TCP/IP communication? Can I use OpenIGTLink? If yes, could I find any documents or examples? Shall I implement the socket connection using Qt Socket, Qt TCPServer, etc.? Or any other way?<br>
Any suggestion is highly appreciated!</p>
<p>-Shelly</p>

---

## Post #2 by @lassoan (2018-11-26 05:07 UTC)

<p>OpenIGTLink is a very simple TCP/IP protocol that is already well supported in Slicer. I would highly recommend using it, as it is not easy to implement stable and efficient multi-threaded communication in an frontend application. You can find OpenIGTLink implementations for most common programming languages (C++, Python, Java, MATLAB, etc.).</p>

---

## Post #3 by @shellyverde (2018-11-27 03:45 UTC)

<p>Thanks! Will try it.<br>
-Shelly</p>

---

## Post #4 by @slicer365 (2023-07-22 16:25 UTC)

<p>Sorry to disturb you ,Mr Lasso！<br>
I wrote a server script in python to get the coordinates sent from slicer, but what I got was bytes, how to convert it into a string? Decode is still error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20caeca9ca1d0750fcbfab1ea63cd0fab3e58007.png" data-download-href="/uploads/short-url/4G62EcHH6qBg7hCJffIRGqqNBHN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20caeca9ca1d0750fcbfab1ea63cd0fab3e58007_2_517x373.png" alt="image" data-base62-sha1="4G62EcHH6qBg7hCJffIRGqqNBHN" width="517" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20caeca9ca1d0750fcbfab1ea63cd0fab3e58007_2_517x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20caeca9ca1d0750fcbfab1ea63cd0fab3e58007_2_775x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20caeca9ca1d0750fcbfab1ea63cd0fab3e58007_2_1034x746.png 2x" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1170×845 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2023-07-22 16:38 UTC)

<p>There is no need to develop a Python script for this, because sending/receiveing transforms, markups, images, etc. to/from Slicer via TCP/IP (using OpenIGTLink protocol) is already implemented in <a href="https://pypi.org/project/pyigtl/">pyigtl</a> Python package.</p>

---

## Post #6 by @slicer365 (2023-07-22 17:09 UTC)

<p>Thank you!<br>
If I need to get the coordinates sent by slicer in real time, or when the coordinates in slicer change, it will trigger the sending coordinates, how should I write this script?</p>
<p>Is this right？<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b13286c6a2117fe20c7e9c7bbf5fa0352a80a0f5.png" data-download-href="/uploads/short-url/phyLpChkhYIFNc5d3L6w0IOx3yl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b13286c6a2117fe20c7e9c7bbf5fa0352a80a0f5.png" alt="image" data-base62-sha1="phyLpChkhYIFNc5d3L6w0IOx3yl" width="517" height="207" data-dominant-color="272728"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×338 8.35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and If I want send a transfrom from Unity Scene to slicer by IGT，how should I define the transform.</p>

---

## Post #7 by @lassoan (2023-07-22 22:22 UTC)

<p>Yes, Slicer sends the updated transform, image, markup, etc. automatically when there is a change. You can set it up in OpenIGTLinkIF module.</p>
<p>If you want to use Unity then I would recommend to start from an existing project, there are a couple of them that show the Slicer scene, allows moving nodes by grabbing and moving them physically, reslice images, etc. Search for augmented reality and HoloLens in this forum for more information.</p>

---

## Post #8 by @slicer365 (2023-07-23 01:57 UTC)

<p>Thank you!<br>
In addition，I used the example script, it runs normally.</p>
<p>How can I receive the position message in slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50a8a06c38719a483aa67f73a810177490810b3c.png" data-download-href="/uploads/short-url/bvxtFCFoclRRrnQeG0NC2bHPmUs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50a8a06c38719a483aa67f73a810177490810b3c.png" alt="image" data-base62-sha1="bvxtFCFoclRRrnQeG0NC2bHPmUs" width="690" height="394" data-dominant-color="272829"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1143×653 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is no message in the slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf8e7f88523280ce315a21731e05661e7834d99b.png" data-download-href="/uploads/short-url/rkAuRu9lCjzFkB1secmeEZzLeOL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf8e7f88523280ce315a21731e05661e7834d99b_2_690x266.png" alt="image" data-base62-sha1="rkAuRu9lCjzFkB1secmeEZzLeOL" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf8e7f88523280ce315a21731e05661e7834d99b_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf8e7f88523280ce315a21731e05661e7834d99b_2_1035x399.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf8e7f88523280ce315a21731e05661e7834d99b_2_1380x532.png 2x" data-dominant-color="D8DCF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2079×802 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2023-07-23 04:42 UTC)

<p>It did not make sense to add the POSITION message to Slicer, as it just barely smaller than a TRANSFORM message and way more limited. I would recommend to use the TRANSFORM message instead.</p>

---

## Post #10 by @slicer365 (2023-07-24 16:34 UTC)

<p>Dear Mr Lasso，</p>
<p>I want to receive the image from slicer through Python and display it. My code is like this. I can get the message, but how can I filter out the array and display it as a picture?</p>
<p>Thank you ！</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f938d69c90166e3e630c98586f2ece63a789caf0.jpeg" data-download-href="/uploads/short-url/zyIFgVFx9w80uLaonQKfW2EuFsQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f938d69c90166e3e630c98586f2ece63a789caf0_2_673x500.jpeg" alt="image" data-base62-sha1="zyIFgVFx9w80uLaonQKfW2EuFsQ" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f938d69c90166e3e630c98586f2ece63a789caf0_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f938d69c90166e3e630c98586f2ece63a789caf0_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f938d69c90166e3e630c98586f2ece63a789caf0.jpeg 2x" data-dominant-color="535457"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1162×863 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2023-07-24 16:38 UTC)

<p>It seems that you are considering reimplementing some image visualization, which should not be necessary. What is your overall goal?</p>

---

## Post #12 by @slicer365 (2023-07-24 16:43 UTC)

<p>I want to transfer the image in slicer to other software in real time.<br>
For example, I develop a mobile phone software based on TCP, and then I can operate it on my computer and transmit the image to my phone in real time or Hololens device.</p>

---

## Post #13 by @lassoan (2023-07-24 17:45 UTC)

<p>For HoloLens there are already full-feature open-source augmented reality applications that you can use as is, or customize/extend to match your needs. See for example:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/1d0157a7a50a0c35b3956925b10394a13952db3dd75d7fe4dfb4a0d270d3a27b/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning" target="_blank" rel="noopener">GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning: GitHub...</a></h3>

  <p>GitHub repository for the IJCARS paper: "Real-Time open-source integration between Microsoft HoloLens 2 and 3D Slicer" - GitHub - BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlann...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
