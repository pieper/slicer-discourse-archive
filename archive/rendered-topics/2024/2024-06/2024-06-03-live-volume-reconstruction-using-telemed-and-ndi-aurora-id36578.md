---
topic_id: 36578
title: "Live Volume Reconstruction Using Telemed And Ndi Aurora"
date: 2024-06-03
url: https://discourse.slicer.org/t/36578
---

# Live volume reconstruction using Telemed and NDI Aurora

**Topic ID**: 36578
**Date**: 2024-06-03
**URL**: https://discourse.slicer.org/t/live-volume-reconstruction-using-telemed-and-ndi-aurora/36578

---

## Post #1 by @valerie (2024-06-03 19:09 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930<br>
Plus version: 2.9.0.20240320-Telemed-Win64<br>
Expected behavior: Image slice from Telemed moves as tracked by the NDI Aurora. Scout scan projects movement and live reconstruction creates volume.<br>
Actual behavior: Image slice from Telemed is not moving based on NDI Aurora tracker. Scout scan is not working, and live reconstruction does not work due to scout scan.</p>
<p>Hi, I am trying to perform live reconstruction of the kidney using Telemed to visualize images and NDI Aurora to track movement of probe. I successfully connected the devices to the Plus server using the configuration file provided below. I combined each device’s respective configuration into one file and followed the steps in this <a href="https://youtu.be/2vXeJxYFou4?si=d6KAe1T-cbZ707wK" rel="noopener nofollow ugc">video</a>. However, each time I get to the Scout scan and live reconstruction part, it does not work. Based on documentation, tutorials, and videos, the image slice projected by Telemed should move based on the movement of the probe tracked by the NDI Aurora. From my impression, the scout scanning and live reconstruction occurs based on the movement of the probe. The video uses a different method than the SlicerIGT tutorials. The video uses the Plus Remote module to set up the server and rearranges the transform data hierarchy. I assume that I need the Image_Image transform in my hierarchy but my list only contains Image_Reference. Also, when I click on the view in the 3D volume section, the image slice takes up the whole outlined volume box and the volume box disappears. I have included some screenshots as reference. I have trying to achieve the same results as this <a href="https://youtu.be/lfZeXabDjMg?si=xNzoaOaWt0ax2OpN" rel="noopener nofollow ugc">video</a>, but with the Telemed and NDI Aurora. I looked at forums to find similar questions and tried to troubleshoot it, but I cannot figure it out. I’m not sure if my configuration files are incorrect or missing a part or if I am missing a step when setting up the live reconstruction in 3D Slicer. Please provide advice and solutions to this problem.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/928d17525556f9867a48dab40cd163d8dd4b9825.png" alt="image (1)" data-base62-sha1="kUrZOmExvG6aH8lBhA3lITo0kUB" width="576" height="266"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b5c144b5116698b7acfd6e9dd928fd691f38d15.png" data-download-href="/uploads/short-url/6bzOegTlT4Wr0QlY5XFQyLWhrox.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5c144b5116698b7acfd6e9dd928fd691f38d15_2_690x218.png" alt="image" data-base62-sha1="6bzOegTlT4Wr0QlY5XFQyLWhrox" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5c144b5116698b7acfd6e9dd928fd691f38d15_2_690x218.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5c144b5116698b7acfd6e9dd928fd691f38d15_2_1035x327.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b5c144b5116698b7acfd6e9dd928fd691f38d15_2_1380x436.png 2x" data-dominant-color="4E4D63"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3262×1034 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/eced31dcfc7f2a186f3e4ad35851b78c4e6b061f.png" data-download-href="/uploads/short-url/xNWRYbeN2Y3JZIqp1dNSZtofVzp.png?dl=1" title="PlusDeviceSet_Server_NDIAurora_and_Telemed_Configuration_File" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/eced31dcfc7f2a186f3e4ad35851b78c4e6b061f_2_242x500.png" alt="PlusDeviceSet_Server_NDIAurora_and_Telemed_Configuration_File" data-base62-sha1="xNWRYbeN2Y3JZIqp1dNSZtofVzp" width="242" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/eced31dcfc7f2a186f3e4ad35851b78c4e6b061f_2_242x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/eced31dcfc7f2a186f3e4ad35851b78c4e6b061f_2_363x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/eced31dcfc7f2a186f3e4ad35851b78c4e6b061f_2_484x1000.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PlusDeviceSet_Server_NDIAurora_and_Telemed_Configuration_File</span><span class="informations">868×1787 33.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2024-06-03 20:05 UTC)

<p>Please don’t upload images of config files. It makes them difficult to search.</p>
<p>Your ImageToReference is a static transform, so the ultrasound image will never move. You’ll need to update your config file to use the correct names for the tools tracked by the Aurora.</p>
<p>With only one sensor you can perform the volume reconstruction in the “Tracker” coordinate system, provided that the object you’re scanning never moves, but it would be better to have both a reference sensor attached to the object and a sensor on the probe, and perform the reconstruction in the “Reference” coordinate system.</p>
<p>If you want to perform the volume reconstruction like it is done in the first video, you will need the latest stable or nightly version of Slicer.</p>

---

## Post #3 by @Sunderlandkyl (2024-06-03 20:11 UTC)

<p>You can find more info on commonly used coordinate systems in Plus here:</p>
<p><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html" class="onebox" target="_blank" rel="noopener nofollow ugc">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html</a></p>

---

## Post #4 by @valerie (2024-06-03 20:32 UTC)

<p>Hi Kyle,<br>
I appreciate your timely response. Sorry about the configuration file image. I didn’t know how to upload it since I could only upload image or video files and thought pasting it into the text would make the post too long. Is there a better way to share the file for next time?</p>

---

## Post #5 by @valerie (2024-06-03 20:33 UTC)

<p>Thank you for the resource! The sketch is very helpful and clarifies the problem. Is there a configuration file based on this coordinate system sketch?</p>

---

## Post #6 by @Sunderlandkyl (2024-06-03 20:41 UTC)

<p>In the future you can upload the config file somewhere else and add a link or attach the config file text to the discourse post using:</p>
<pre><code class="lang-auto">[details="Config file"]
```
&lt;xml&gt;&lt;/xml&gt;
```
[/details]
</code></pre>
<p>Which creates:</p>
<details>
<summary>
Config file</summary>
<pre><code class="lang-auto">&lt;xml&gt;&lt;/xml&gt;
</code></pre>
</details>
<p>This config file uses Ultrasonix and Ascension devices, but the concept should be the same if you update the config file to use Telemed and Aurora.</p>

---

## Post #7 by @valerie (2024-06-04 16:41 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="6" data-topic="36578">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p><code>&lt;xml&gt;&lt;/xml&gt;</code></p>
</blockquote>
</aside>
<p>Is this the config file for Ultrasonix and Ascension? I cannot open it or view the config file you are referring to.</p>

---

## Post #8 by @Sunderlandkyl (2024-06-04 16:43 UTC)

<p>Sorry, forgot to add the link:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml">
  <header class="source">

      <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml" target="_blank" rel="noopener nofollow ugc">PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml</a></h4>


      <pre><code class="lang-xml"> &lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet
      Name="PlusServer: Ultrasonix US (C5-2/60 GPS probe) + Ascension3DG tracker (Probe, Reference, Stylus) - calibrated"
      Description="Broadcasting ultrasound images acquired from the Ultrasonix system through OpenIGTLink. Probe is spatially calibrated for any imaging depth. If PlusServer does not run on the Ultrasonix PC then update the IP attribute in the Device element with the Ultrasonix PC's IP address. Ascension3DG sensors should be plugged in to the Ascension3DG DriveBay mounted on Ultrasonix US in the following order from to leftmost slot (Transducer 1) to the right: 1 Probe, 2 Reference, 3 Stylus." /&gt;
    &lt;Device
      Id="TrackerDevice" 
      Type="Ascension3DG" 
      LocalTimeOffsetSec="0.0" 
      FilterAcWideNotch="1"
      ToolReferenceFrame="Tracker" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Probe" PortName="0"  /&gt;
        &lt;DataSource Type="Tool" Id="Reference" PortName="1"  /&gt;
        &lt;DataSource Type="Tool" Id="Stylus" PortName="2"  /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
          &lt;DataSource Id="Probe"/&gt;
</code></pre>



  This file has been truncated. <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @valerie (2024-06-04 20:22 UTC)

<p>I downloaded the latest stable version of Slicer and modified the given config file for the NDI Aurora and Telemed but I still cannot get the slice to move. I included the modified config file and an image of my setup (currently testing on gel sample instead of phantom model). Also, initially, I did see ProbetoTracker and ReferencetoTracker in my hierarchy list but the only thing listed is the Image_Reference. I’m assuming it has something to do with the transform matrix in the coordinate definitions section. Should I have used the matrix given in the default Telemed config file?</p>
<details>
<summary>
Config file</summary>
<pre><code class="lang-auto"> &lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet
      Name="PlusServer: Telemed US + NDI Aurora tracker (Probe, Reference)"
      Description="Broadcasting ultrasound images acquired from the Ultrasonix system through OpenIGTLink. Probe is spatially calibrated for any imaging depth. If PlusServer does not run on the Ultrasonix PC then update the IP attribute in the Device element with the Ultrasonix PC's IP address. Ascension3DG sensors should be plugged in to the Ascension3DG DriveBay mounted on Ultrasonix US in the following order from to leftmost slot (Transducer 1) to the right: 1 Probe, 2 Reference, 3 Stylus." /&gt;
    &lt;Device
      Id="TrackerDevice" 
      Type="AuroraTracker" 
      SerialPort="3" 
      BaudRate="9600"
      AcquisitionRate="50"
      LocalTimeOffsetSec="0.0"
      FilterAcWideNotch="1"
      ToolReferenceFrame="Tracker" &gt;
      &lt;DataSources&gt;
        &lt;DataSource 
			Type="Tool" 
			Id="Probe" 
			RomFile="DDRO-080-061-01_GENERIC (4).rom"
			PortName="0" 
		/&gt; &lt;!-- PortName relates to physical port 1 --&gt;
		&lt;DataSource 
			Type="Tool" 
			Id="Reference" 
			RomFile="DDRO-080-051-01_GENERIC.rom"
			PortName="1" 
		/&gt; &lt;!-- PortName relates to physical port 2 --&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
          &lt;DataSource Id="Probe"/&gt;
          &lt;DataSource Id="Reference"/&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="VideoDevice"
      Type="TelemedVideo" 
      AcquisitionRate="30" 
      LocalTimeOffsetSec="-0.2976"
      IP="127.0.0.1"
      AutoClipEnabled="TRUE"
      ImageToTransducerTransformName="ImageToTransducer" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="UN"  /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video"/&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;Device 
      Id="TrackedVideoDevice" 
      Type="VirtualMixer" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
        &lt;InputChannel Id="VideoStream" /&gt;
      &lt;/InputChannels&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackedVideoStream"/&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="CaptureDevice"
      Type="VirtualCapture"
      BaseFilename="Recording.igs.mhd"
      EnableCapturingOnStart="FALSE"
      RequestedFrameRate="15" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackedVideoStream" /&gt;
      &lt;/InputChannels&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="VolumeReconstructorDevice"
      Type="VirtualVolumeReconstructor"
      OutputVolDeviceName="Volume_Reference"
      EnableReconstruction="FALSE" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackedVideoStream" /&gt;
      &lt;/InputChannels&gt;
      &lt;VolumeReconstruction
        ImageCoordinateFrame="Image" ReferenceCoordinateFrame="Reference"
        CompoundingMode="MEAN" Interpolation="LINEAR"
        Optimization="FULL" NumberOfThreads="2"
        ClipRectangleOrigin="0 0" ClipRectangleSize="820 616" PixelRejectionThreshold="1"
        OutputSpacing="0.5 0.5 0.5"
        FillHoles="ON" &gt;
        &lt;HoleFilling&gt;
          &lt;HoleFillingElement Type="GAUSSIAN" Size="5" Stdev="0.6667" MinimumKnownVoxelsRatio="0.50001" /&gt;
          &lt;HoleFillingElement Type="STICK" StickLengthLimit="9" NumberOfSticksToUse="1" /&gt;
        &lt;/HoleFilling&gt;
      &lt;/VolumeReconstruction&gt;
    &lt;/Device&gt;
  &lt;/DataCollection&gt;

  &lt;CoordinateDefinitions&gt;
    &lt;!-- transform matrix provided by Telemed default config file --&gt;
    &lt;Transform From="Image" To="Reference"
      Matrix="
        0.2 0.0 0.0 0.0
        0.0 0.2 0.0 0.0
        0.0 0.0 0.2 0.0
        0 0 0 1" /&gt;
  &lt;/CoordinateDefinitions&gt;
  
  &lt;PlusOpenIGTLinkServer 
    MaxNumberOfIgtlMessagesToSend="1" 
    MaxTimeSpentWithProcessingMs="50" 
    ListeningPort="18944" 
    SendValidTransformsOnly="true" 
    OutputChannelId="TrackedVideoStream" &gt; 
    &lt;DefaultClientInfo&gt; 
      &lt;MessageTypes&gt; 
        &lt;Message Type="IMAGE" /&gt;
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt; 
        &lt;Transform Name="ProbeToReference" /&gt;
        &lt;Transform Name="ReferenceToTracker" /&gt;
      &lt;/TransformNames&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;
      &lt;/ImageNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

&lt;/PlusConfiguration&gt;
</code></pre>
</details>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d920295448823865837a383887676cd4777a4a3.png" data-download-href="/uploads/short-url/1W3207Ub8v1CyvQ2zloSI0X8yzN.png?dl=1" title="Labelled_setup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d920295448823865837a383887676cd4777a4a3_2_577x500.png" alt="Labelled_setup" data-base62-sha1="1W3207Ub8v1CyvQ2zloSI0X8yzN" width="577" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d920295448823865837a383887676cd4777a4a3_2_577x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d920295448823865837a383887676cd4777a4a3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d920295448823865837a383887676cd4777a4a3.png 2x" data-dominant-color="969283"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Labelled_setup</span><span class="informations">606×525 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @LeidyMoraV (2024-06-04 20:34 UTC)

<p>Try changing:</p>
<aside class="quote no-group" data-username="valerie" data-post="9" data-topic="36578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ccd318/48.png" class="avatar"> valerie:</div>
<blockquote>
<p><code>&lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;</code></p>
</blockquote>
</aside>
<p>to:</p>
<p><code>&lt;Image Name="Image" EmbeddedTransformToFrame="Probe" /&gt;</code></p>
<p>And puting Image_Reference in the hierachy of ProbeToReferences, something like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9254c4db3b726ac54bcf3a5afb451a7af2f5f2f8.jpeg" alt="image" data-base62-sha1="kSvkioDzjPuQw0s6Y2e2CL19CRy" width="454" height="490"></p>

---

## Post #11 by @valerie (2024-06-04 20:43 UTC)

<p>Hi Leidy,</p>
<p>Thank you for your advice. Unfortunately, my problem still remains with the Transform hierarchy list. I do not see the other transforms. The only one that is being listed is Image_Probe. How do I get the other transforms to appear in the list like in the image you show?</p>
<p>Update: I have ReferenceToTracker in my list by opening OpenIGTLinkIF first and then viewing Data; previously, I was following the steps of the video and creating the Plus Remote Server and then viewing Data. However, I am missing Image_Reference and ProbeToReference in my list. Any way to solve this issue?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3936b52dd60bd2f5e5fc69fe1b2572eef2bc77a.png" alt="Screenshot 2024-06-04 170911" data-base62-sha1="ubGABWigEKjUp1uU0unhZoohBBU" width="531" height="203"></p>

---

## Post #12 by @valerie (2024-06-13 19:19 UTC)

<p>I am still having issues with reconstructing the volume in 3D Slicer. The image slice is now moving based on the position of the transducer. However, after I complete the Scout scan, there is a black square. I ended up following the steps in the <a href="https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018%213992&amp;authkey=!ADFvs6W6EnKJR44" rel="noopener nofollow ugc">SlicerIGT tutorial presentation</a> instead of following the <a href="https://youtu.be/2vXeJxYFou4?si=Zz4mrDYXCzc3wff3" rel="noopener nofollow ugc">video</a> in my original post (it wasn’t working as well and produced nothing). How do I fix this and achieve the desired reconstruction of the kidney? Any suggestions on how to visualize the reconstruction volume?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a613c311292b55c3a5b37c75cb584e588775a63.png" alt="List of transforms based on config file." data-base62-sha1="1tP6cnWHdwLFDlbB1Bp28dexAQ3" width="528" height="126"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/917c8278295d77cb33f99ce6d58bf44e935eef2c.png" data-download-href="/uploads/short-url/kL1ZCyxoft2wybH2gtVzqW0KGKg.png?dl=1" title="Black square from Scout scan and Live reconstruction. Floating image slice outside volume is tracked transducer." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/917c8278295d77cb33f99ce6d58bf44e935eef2c_2_589x500.png" alt="Black square from Scout scan and Live reconstruction. Floating image slice outside volume is tracked transducer." data-base62-sha1="kL1ZCyxoft2wybH2gtVzqW0KGKg" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/917c8278295d77cb33f99ce6d58bf44e935eef2c_2_589x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/917c8278295d77cb33f99ce6d58bf44e935eef2c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/917c8278295d77cb33f99ce6d58bf44e935eef2c.png 2x" data-dominant-color="8E8FC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Black square from Scout scan and Live reconstruction. Floating image slice outside volume is tracked transducer.</span><span class="informations">835×708 17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @LeidyMoraV (2024-06-17 14:26 UTC)

<p>Remember to turn on the visualization of the volume in the ‘Volume Rendering’ module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ebcd1daf96bf5b111eff8b8539d02e0d64a2a2c.png" data-download-href="/uploads/short-url/kmIlp83nyvIwrsOjKbXl8MxTNr6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ebcd1daf96bf5b111eff8b8539d02e0d64a2a2c_2_420x500.png" alt="image" data-base62-sha1="kmIlp83nyvIwrsOjKbXl8MxTNr6" width="420" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ebcd1daf96bf5b111eff8b8539d02e0d64a2a2c_2_420x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ebcd1daf96bf5b111eff8b8539d02e0d64a2a2c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ebcd1daf96bf5b111eff8b8539d02e0d64a2a2c.png 2x" data-dominant-color="F6F6F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">538×639 27.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
