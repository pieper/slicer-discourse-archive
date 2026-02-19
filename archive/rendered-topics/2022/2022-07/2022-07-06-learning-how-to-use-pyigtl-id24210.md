---
topic_id: 24210
title: "Learning How To Use Pyigtl"
date: 2022-07-06
url: https://discourse.slicer.org/t/24210
---

# Learning how to use pyigtl

**Topic ID**: 24210
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/learning-how-to-use-pyigtl/24210

---

## Post #1 by @Elvis_Chen (2022-07-06 16:59 UTC)

<p>Operating system: 10<br>
Slicer version: n/a<br>
Expected behavior: receiving an imaged with embedded transform<br>
Actual behavior: received “None”</p>
<p>hi all,</p>
<p>I am trying to create a python program that receives tracked images from PlusLib via pyigtl. I am trying to understand how to use pyigtl effectively and am seeking your help in understanding it.</p>
<p>First, I downloaded the latest stable version of  <a href="http://perk-software.cs.queensu.ca/plus/packages/stable/" rel="noopener nofollow ugc">Plus Toolkit</a>. Using a simple webcam as a tracker, I launched the Plus Server Launched and used “PlusServer: Optical Marker Tracker using MMF video”. Using the following code, I am able to receive tracking transform of an Aruco Marker:</p>
<pre><code class="lang-auto">import pyigtl
tclient = pyigtl.OpenIGTLinkClient("127.0.0.1", 18944)
tmessage = tclient.wait_for_message("Marker0ToTracker", timeout=5)
print(tmessage)
</code></pre>
<p>However, modifying the above to acquire the tracked image always returns with a message of “None”:</p>
<pre><code class="lang-auto">import pyigtl
client = pyigtl.OpenIGTLinkClient("127.0.0.1", 18945)
message = client.wait_for_message("Image", timeout=5)
print(message)
</code></pre>
<p>suggesting that the tracked image is not being received. Please note that the image is transmitted via a different port than the transforms themselves.</p>
<p>can anyone suggest a reason why the tracked images are not been received?</p>
<p>for complete reference, the plus server XML is listed below:</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.4"&gt;
  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet
      Name="PlusServer: Optical marker tracker using MMF video"
      Description="Tracking of printed ArUco markers using a simple camera. Marker positions and image data are broadcasted through OpenIGTLink (on port 18944 and 18945, respectively). To use a different camera, change CaptureDeviceId attribute (to 0, 1, 2, ...)." /&gt;
    &lt;Device
      Id="VideoDevice"
      Type="MmfVideo"
      FrameSize="640 480"
      VideoFormat="YUY2"
      CaptureDeviceId="1" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="MF" ImageType="RGB_COLOR" /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="OpticalMarkerTracker"
      CameraCalibrationFile="OpticalMarkerTracker/realsense_gen2_calibration.yml"
      ToolReferenceFrame="Tracker"
      TrackingMethod="OPTICAL"
      MarkerDictionary="ARUCO_MIP_36h12"&gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Marker0" MarkerId="0" MarkerSizeMm="80" /&gt;
        &lt;DataSource Type="Tool" Id="Marker1" MarkerId="1" MarkerSizeMm="80" /&gt;
        &lt;DataSource Type="Tool" Id="Marker2" MarkerId="2" MarkerSizeMm="50" /&gt;
        &lt;DataSource Type="Tool" Id="Marker3" MarkerId="3" MarkerSizeMm="50" /&gt;
        &lt;DataSource Type="Tool" Id="Marker4" MarkerId="4" MarkerSizeMm="50" /&gt;
        &lt;DataSource Type="Tool" Id="Marker5" MarkerId="5" MarkerSizeMm="30" /&gt;
        &lt;DataSource Type="Tool" Id="Marker6" MarkerId="6" MarkerSizeMm="30" /&gt;
        &lt;DataSource Type="Tool" Id="Marker7" MarkerId="7" MarkerSizeMm="30" /&gt;
        &lt;DataSource Type="Tool" Id="Marker8" MarkerId="8" MarkerSizeMm="30" /&gt;
      &lt;/DataSources&gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="VideoStream"  /&gt;
      &lt;/InputChannels&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
          &lt;DataSource Id="Marker0"/&gt;
          &lt;DataSource Id="Marker1"/&gt;
          &lt;DataSource Id="Marker2"/&gt;
          &lt;DataSource Id="Marker3"/&gt;
          &lt;DataSource Id="Marker4"/&gt;
          &lt;DataSource Id="Marker5"/&gt;
          &lt;DataSource Id="Marker6"/&gt;
          &lt;DataSource Id="Marker7"/&gt;
          &lt;DataSource Id="Marker8"/&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="CaptureDevice"
      Type="VirtualCapture"
      BaseFilename="RecordingTest.igs.mha"
      EnableCapturingOnStart="FALSE" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
      &lt;/InputChannels&gt;
    &lt;/Device&gt;
  &lt;/DataCollection&gt;
  
  &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18944"
    SendValidTransformsOnly="true"
    OutputChannelId="TrackerStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt;
        &lt;Transform Name="Marker0ToTracker" /&gt;
        &lt;Transform Name="Marker1ToTracker" /&gt;
        &lt;Transform Name="Marker2ToTracker" /&gt;
        &lt;Transform Name="Marker3ToTracker" /&gt;
        &lt;Transform Name="Marker4ToTracker" /&gt;
        &lt;Transform Name="Marker5ToTracker" /&gt;
        &lt;Transform Name="Marker6ToTracker" /&gt;
        &lt;Transform Name="Marker7ToTracker" /&gt;
        &lt;Transform Name="Marker8ToTracker" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

  &lt;PlusOpenIGTLinkServer 
    MaxNumberOfIgtlMessagesToSend="1" 
    MaxTimeSpentWithProcessingMs="50" 
    ListeningPort="18945" 
    SendValidTransformsOnly="true" 
    OutputChannelId="VideoStream" &gt; 
    &lt;DefaultClientInfo&gt; 
      &lt;MessageTypes&gt; 
        &lt;Message Type="IMAGE" /&gt;
      &lt;/MessageTypes&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Image" /&gt;
      &lt;/ImageNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

&lt;/PlusConfiguration&gt;

</code></pre>

---

## Post #2 by @lassoan (2022-07-06 18:30 UTC)

<p>Can Slicer receive a continuous stream of images from this server?</p>
<p>If yes, then the issue is in pyigtl. Since it is a pure native Python package, you can debug it very easily in any Python IDE. Please step through the code using a debugger and let us know where things go wrong.</p>

---

## Post #3 by @Elvis_Chen (2022-07-06 19:07 UTC)

<aside class="quote no-group" data-username="Elvis_Chen" data-post="1" data-topic="24210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elvis_chen/48/15908_2.png" class="avatar"> Elvis_Chen:</div>
<blockquote>
<pre><code class="lang-auto">import pyigtl
tclient = pyigtl.OpenIGTLinkClient("127.0.0.1", 18944)
tmessage = tclient.wait_for_message("Marker0ToTracker", timeout=5)
print(tmessage)
</code></pre>
</blockquote>
</aside>
<p>hi Andras,</p>
<p>thanks for the hint. Indeed it works in Slicer. The mistake I made was that I should be querying “Image_Image” instead of just “Image” in the code above.  Now it works just fine.</p>
<p>regards,</p>

---
