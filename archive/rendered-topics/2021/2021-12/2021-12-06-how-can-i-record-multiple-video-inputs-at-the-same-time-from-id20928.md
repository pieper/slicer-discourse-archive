---
topic_id: 20928
title: "How Can I Record Multiple Video Inputs At The Same Time From"
date: 2021-12-06
url: https://discourse.slicer.org/t/20928
---

# How can I record multiple video inputs at the same time from Slicer?

**Topic ID**: 20928
**Date**: 2021-12-06
**URL**: https://discourse.slicer.org/t/how-can-i-record-multiple-video-inputs-at-the-same-time-from-slicer/20928

---

## Post #1 by @lb123 (2021-12-06 14:36 UTC)

<p>Hi,</p>
<p>I’m broadcasting 2 acquired videos through OpenIGTLink from Plus Server to Slicer 4.13.0.<br>
The videos consist in live data coming from 2 epiphan frame grabbers.</p>
<p>I can correctly see both the live videos on Slicer.</p>
<p>I would like to record <strong>both them</strong> from Slicer.</p>
<p>I tried to record adding a CaptureDevice in the plus server configuration file:</p>
<pre><code>&lt;Device
  Id="CaptureDevice"
  Type="VirtualCapture"
  BaseFilename="RecordingTest.igs.mha"
  EnableCapturingOnStart="FALSE" &gt;
  &lt;InputChannels&gt;
    &lt;InputChannel Id="VideoStream1" /&gt;
&lt;InputChannel Id="VideoStream2" /&gt;
  &lt;/InputChannels&gt;
&lt;/Device&gt;
</code></pre>
<p>Then I tried to start a recording from Slicer using the recording button of Plus Remote (IGT module) but only the VideoStream1 is recorded.</p>
<p>Can you please tell me what I am doing wrong?</p>

---

## Post #2 by @Sunderlandkyl (2021-12-06 16:06 UTC)

<p>Each VirtualCapture device can only record a single video stream, you’ll need to have one for each.</p>

---

## Post #3 by @lb123 (2021-12-06 16:26 UTC)

<p>Thank you for your reply. So I should add a second VirtualCaputure device like shown below, right?</p>
<pre><code class="lang-auto">&lt;Device
  Id="CaptureDevice1"
  Type="VirtualCapture"
  BaseFilename="RecordingTest1.igs.mha"
  EnableCapturingOnStart="FALSE" &gt;
  &lt;InputChannels&gt;
    &lt;InputChannel Id="VideoStream1" /&gt;
  &lt;/InputChannels&gt;
&lt;/Device&gt;

&lt;Device
  Id="CaptureDevice2"
  Type="VirtualCapture"
  BaseFilename="RecordingTest2.igs.mha"
  EnableCapturingOnStart="FALSE" &gt;
  &lt;InputChannels&gt;
    &lt;InputChannel Id="VideoStream2" /&gt;
  &lt;/InputChannels&gt;
&lt;/Device&gt;
</code></pre>
<p>But then how is it possible to run 2 recordings at the same time?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0c8e9febc8448edca7e347d0fb8736bb7433a3e.png" data-download-href="/uploads/short-url/pdUurZ7UyB4fJDc13ct0QlE60Y6.png?dl=1" title="ddd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0c8e9febc8448edca7e347d0fb8736bb7433a3e_2_363x500.png" alt="ddd" data-base62-sha1="pdUurZ7UyB4fJDc13ct0QlE60Y6" width="363" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0c8e9febc8448edca7e347d0fb8736bb7433a3e_2_363x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0c8e9febc8448edca7e347d0fb8736bb7433a3e_2_544x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0c8e9febc8448edca7e347d0fb8736bb7433a3e.png 2x" data-dominant-color="EEF0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ddd</span><span class="informations">575×790 32.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see from the attached image it is possibile to select just one capture device at a time</p>
<p>Is it possible to do it just coding or is there the possibility to do it from the Slicer GUI?</p>
<p>Maybe the most immediate way is just to set EnableCapturingOnStart=“TRUE”, right?</p>
<p>Also, is it possible to reduce the size of .mha files? Huge files are generated (several GB for a few seconds of recording).</p>

---

## Post #4 by @Sunderlandkyl (2021-12-06 17:53 UTC)

<p>There doesn’t seem to be a way to do this from the GUI currently.</p>
<p>EnableCapturingOnStart=“TRUE” will work if you’re ok with recording everything once the server is started.</p>
<p>You can also start recording from python like this:</p>
<ul>
<li>Start:</li>
</ul>
<pre><code class="lang-auto">startCommand = slicer.vtkSlicerOpenIGTLinkCommand()
startCommand.SetName("StartRecording")
startCommand.SetCommandContent('&lt;Command Name="StartRecording" CaptureDeviceId="CaptureDevice" OutputFilename="Recording.igs.mha" EnableCompression="False"&gt;&lt;/Command&gt;')
igtlConnectorNode.SendCommand(startCommand)
</code></pre>
<ul>
<li>Stop</li>
</ul>
<pre><code class="lang-auto">stopCommand = slicer.vtkSlicerOpenIGTLinkCommand()
stopCommand.SetName("StopRecording")
stopCommand.SetCommandContent('&lt;Command Name="StopRecording" CaptureDeviceId="CaptureDevice"&gt;&lt;/Command&gt;')
igtlConnectorNode.SendCommand(stopCommand)
</code></pre>

---

## Post #5 by @lb123 (2021-12-06 17:57 UTC)

<p>Thank you a lot for your explanation!</p>
<p>Do you know if there is any way to decrease the size of the recordings?<br>
Huge files are generated (several GB for a few seconds of recording).</p>

---

## Post #6 by @Sunderlandkyl (2021-12-06 19:40 UTC)

<p>Couple of ways:</p>
<ul>
<li>Can you post the epiphan device config? If the image is in color, then it will increase the size of the files.</li>
<li>You can add "EnableCompression=“TRUE” to the command to use compression when saving.</li>
<li>In tomorrow’s nightly Plus build, you can change the file name extension from “.igs.mha” to “mkv”. Even if the video is color, this should reduce file size by saving as a Matroska file (using VP9 compression).</li>
</ul>
<p>Not sure if you are aware, but you can also record images and transforms in Slicer using the Sequences module. Let me know if you have any questions.</p>

---

## Post #7 by @lb123 (2021-12-16 16:32 UTC)

<p>Thank you, I tried to save to “mkv” and the size is really smaller now!</p>
<p>So, following your suggestions I recorded 2 videos in mkv format. But now I would like to replay them but I am facing some issues.</p>
<p>This is the configuration file I am using to replay the 2 videos:</p>
<pre><code class="lang-auto"> &lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet
      Name="test_multi_replay_mkv___"
      Description="Broadcasting acquired video through OpenIGTLink"
    /&gt;
	&lt;Device
		Id="VideoDevice"
		Type="SavedDataSource"
		SequenceFile="RecordingFristVideo21-12-16-10-20-46.mkv"
		UseData="IMAGE"
		UseOriginalTimestamps="TRUE"
		ToolReferenceFrame="Reference"
		RepeatEnabled="TRUE" &gt;
		&lt;DataSources&gt;
		&lt;DataSource Type="Video" Id="Video" BufferSize="100" /&gt;
		&lt;/DataSources&gt;
		&lt;OutputChannels&gt;
		&lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
		&lt;/OutputChannels&gt;
    &lt;/Device&gt;
	
	&lt;Device
		Id="VideoDevice2"
		Type="SavedDataSource"
		SequenceFile="RecordingSecondVideo21-12-16-10-20-46.mkv"
		UseData="IMAGE"
		UseOriginalTimestamps="TRUE"
		ToolReferenceFrame="Reference"
		RepeatEnabled="TRUE" &gt;
		&lt;DataSources&gt;
		&lt;DataSource Type="Video" Id="Video2" BufferSize="100" /&gt;
		&lt;/DataSources&gt;
		&lt;OutputChannels&gt;
		&lt;OutputChannel Id="VideoStream2" VideoDataSourceId="Video2" /&gt;
		&lt;/OutputChannels&gt;
    &lt;/Device&gt;
	
  &lt;/DataCollection&gt;

  &lt;CoordinateDefinitions&gt;
    &lt;Transform From="Image" To="Reference"
      Matrix="
        1 0.0 0.0 0.0
        0.0 1 0.0 0.0
        0.0 0.0 1 0.0
        0 0 0 1" /&gt;
		
	&lt;Transform From="Image2" To="Reference"
      Matrix="
        1 0.0 0.0 0.0
        0.0 1 0.0 0.0
        0.0 0.0 1 0.0
        0 0 0 1" /&gt;
  &lt;/CoordinateDefinitions&gt;

  &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18944"
    SendValidTransformsOnly="true"
    OutputChannelId="VideoStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="IMAGE" /&gt;
      &lt;/MessageTypes&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;
      &lt;/ImageNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
  
    &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18945"
    SendValidTransformsOnly="true"
    OutputChannelId="VideoStream2" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="IMAGE" /&gt;
      &lt;/MessageTypes&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image2" EmbeddedTransformToFrame="Reference" /&gt;
      &lt;/ImageNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

&lt;/PlusConfiguration&gt;

</code></pre>
<p>When I run the OpenIGTLink clients in Slicer as you can see in the screenshot below there isn’t any vector volume on the “IGTLConnector” but only on the “IGTLConnector_1”:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6fcf79fe1207626c9db63b00aa8c39b27bc1449.png" data-download-href="/uploads/short-url/uFS9PAioEaEeXPPjK9FEPDq8e7v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6fcf79fe1207626c9db63b00aa8c39b27bc1449.png" alt="image" data-base62-sha1="uFS9PAioEaEeXPPjK9FEPDq8e7v" width="482" height="499" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×686 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know I to solve this issue?</p>
<p>Thank you</p>

---

## Post #8 by @J.vd.Zee (2024-03-19 08:05 UTC)

<p>Hi!<br>
Can I re-open this topic?<br>
I would like to make multiple streams of the same videodevice, but each with a different crop. I’m now struggling with cropping each individual stream.<br>
<strong>Expected behaviour:</strong><br>
Cropping each videostream with the specific crop.</p>
<p><strong>Observerd behavior</strong><br>
Cropping each videostream with the first cropping settings.</p>
<p>Can someone help me out?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57d5794f52e56ec14e512660f1ee8fdcd09bc777.png" data-download-href="/uploads/short-url/cx0U92Pn6qCos4BLvqYOwnKqbWf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57d5794f52e56ec14e512660f1ee8fdcd09bc777.png" alt="image" data-base62-sha1="cx0U92Pn6qCos4BLvqYOwnKqbWf" width="690" height="356" data-dominant-color="FBF8FD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1421×734 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Sunderlandkyl (2024-03-19 15:00 UTC)

<p>I’m not sure if the MmfVideo device will work with multiple data sources, but a couple of things:</p>
<ul>
<li>You should only include one “DataSources” element. Both “DataSource” should be in the same one.</li>
<li>Same deal with “OutputChannels” and “OutputChannel”.</li>
<li>A channel can only include a single image stream, so you would need to separate the two. (VideoStream1, VideoStream2). Probably using more descriptive names for each stream.</li>
</ul>

---

## Post #10 by @J.vd.Zee (2024-03-19 15:14 UTC)

<p>Hi Kyle,</p>
<p>Thank you for your prompt reply!</p>
<p>I tried your adjustments (see the photo). However, it is not working. Do you have other possible adjustments?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fefabccd7d42b9995052e5e450a660a9bdf62a18.png" data-download-href="/uploads/short-url/AnEtLD5ssEmjkw4sK9bxNi0hwj6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fefabccd7d42b9995052e5e450a660a9bdf62a18_2_690x379.png" alt="image" data-base62-sha1="AnEtLD5ssEmjkw4sK9bxNi0hwj6" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fefabccd7d42b9995052e5e450a660a9bdf62a18_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fefabccd7d42b9995052e5e450a660a9bdf62a18_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fefabccd7d42b9995052e5e450a660a9bdf62a18_2_1380x758.png 2x" data-dominant-color="FCFAFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1241 371 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Sunderlandkyl (2024-03-19 15:17 UTC)

<p>You will need to provide more information. It what way is it not working?</p>

---

## Post #12 by @J.vd.Zee (2024-03-20 15:17 UTC)

<p>In my previous post, I included the tips you mentioned.<br>
However, the Plus gives an error after launching:</p>
<p>|WARNING|61724.344000|SERVER&gt; vtkPlusMmfVideoSource is expecting one output channel and there are 2 channels. First output channel will be used.</p>
<p>Is it possible to create different VideoDevices for each videostream (same capture device) and specific crop?</p>

---

## Post #13 by @Sunderlandkyl (2024-03-20 16:38 UTC)

<p>Ok, thanks! Since it looks the device doesn’t currently support multiple output channels, then it is probably not currently possible. I’ll look into what is required to support it.</p>

---

## Post #14 by @Sunderlandkyl (2024-03-20 16:54 UTC)

<p>I’ve updated the vtkPlusMmfVideoSource device. The nightly release tomorrow should be able to support multiple video data sources at the same time, with different crop regions.</p>

---

## Post #15 by @J.vd.Zee (2024-03-22 10:11 UTC)

<p>Hi Kyle!</p>
<p>Thanks for updating.<br>
However, the new update is not working yet. I added my configuration file in the attachments. I made two VideoDevices for each videostream, same capture device and specific crop. Can you help me out?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d2df8908c737afb6473a389a6df8eaf03bfd421.png" data-download-href="/uploads/short-url/6rFYFjbDJOQPnM7ggj7S4nUP841.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2df8908c737afb6473a389a6df8eaf03bfd421_2_421x500.png" alt="image" data-base62-sha1="6rFYFjbDJOQPnM7ggj7S4nUP841" width="421" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2df8908c737afb6473a389a6df8eaf03bfd421_2_421x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2df8908c737afb6473a389a6df8eaf03bfd421_2_631x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2df8908c737afb6473a389a6df8eaf03bfd421_2_842x1000.png 2x" data-dominant-color="FCFAFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1495×1773 460 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @Sunderlandkyl (2024-03-22 13:35 UTC)

<p>The config file should have only 1 Device that has 2 Data sources and 2 Output channels.</p>

---

## Post #17 by @J.vd.Zee (2024-03-25 11:59 UTC)

<p>It worked!<br>
Thanks for helping me out <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---
