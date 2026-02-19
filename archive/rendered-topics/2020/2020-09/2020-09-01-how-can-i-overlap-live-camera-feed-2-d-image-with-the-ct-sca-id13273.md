---
topic_id: 13273
title: "How Can I Overlap Live Camera Feed 2 D Image With The Ct Sca"
date: 2020-09-01
url: https://discourse.slicer.org/t/13273
---

# How can I overlap live camera feed (2-D image) with the CT scan model for an Augmented Reality feel?

**Topic ID**: 13273
**Date**: 2020-09-01
**URL**: https://discourse.slicer.org/t/how-can-i-overlap-live-camera-feed-2-d-image-with-the-ct-scan-model-for-an-augmented-reality-feel/13273

---

## Post #1 by @rak_shrma (2020-09-01 06:26 UTC)

<p>We want to overlay the live camera feed with the CT scan model. The method to calculate the transformation matrix for accurate positioning has been worked out. However, we are struggling with the integration of both 2-D camera feed image and CT scan volume in the same window. Any help will be hugely appreciated.</p>

---

## Post #2 by @lassoan (2020-09-04 02:44 UTC)

<p>You can acquire camera image using <a href="https://plustoolkit.github.io/">Plus toolkit</a>, display the live image in 3D via a slice view, and set up renderer camera parameters to match the optical camera parameters. You can access the camera as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras">here</a>.</p>

---

## Post #3 by @szhang (2020-10-08 20:59 UTC)

<p>Sorry it still seems foreign to me, but to step back a little,</p>
<ol>
<li>What config is needed on <a href="https://plustoolkit.github.io/" rel="noopener nofollow ugc">Plus toolkit</a> if e.g. to broadcast the webcam view?<br>
I tried “PlusServer: Video for Windows video capture device” on PlusApp-2.8.0, it showed “Connection successful!”, but the red light constantly spit out error messages of</li>
</ol>
<blockquote>
<p>SERVER&gt; AddFrameToBuffer: video compression mode MJPG(0x47504a4d): can’t grab| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\VideoForWindows\vtkPlusWin32VideoSource2.cxx(519)</p>
</blockquote>
<ol start="2">
<li>How to <em>display the live image in 3D via a slice view</em>?</li>
</ol>
<p>Thank you!!</p>

---

## Post #4 by @lassoan (2020-10-08 22:36 UTC)

<p>It seems that your webcam only supports mjpg encoding, while Plus only supports uncompressed encodings only. Video for Windows interface is about 30 years old. It is a miracle that Windows still supports it at all.</p>
<p>I would recommend to connect to your webcam using Plus toolkit’s Microsoft Media Foundation or OpenCV imaging interfaces.</p>

---

## Post #5 by @szhang (2020-10-10 11:17 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>!<br>
I did get some local help and managed to modify the config file of “PlusServer:Video for Windows video capture device” based on “PlusServer: Optical marker tracker using MMF video” (since it is webcam based), basically to set up device properly like below</p>
<pre><code> &lt;Device
  Id="VideoDevice" Type="MmfVideo"
  FrameSize="640 480"
  VideoFormat="YUY2"
  CaptureDeviceId="0" 
  &lt;DataSources&gt;
    &lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="MF" ImageType="RGB_COLOR" /&gt;
  &lt;/DataSources&gt;
  &lt;OutputChannels&gt;
    &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
</code></pre>
<p>Once the server is launched on Plus, adding an IGTLConnector using OpenIGTLink module on Slicer will do the job of displaying the cam video in a view window.</p>
<p>This is probably one of many ways to make it work.</p>

---
