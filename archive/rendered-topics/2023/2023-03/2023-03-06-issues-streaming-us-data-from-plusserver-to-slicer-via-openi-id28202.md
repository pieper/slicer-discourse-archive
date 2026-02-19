---
topic_id: 28202
title: "Issues Streaming Us Data From Plusserver To Slicer Via Openi"
date: 2023-03-06
url: https://discourse.slicer.org/t/28202
---

# Issues streaming US data from PlusServer to Slicer via OpenIGTLink

**Topic ID**: 28202
**Date**: 2023-03-06
**URL**: https://discourse.slicer.org/t/issues-streaming-us-data-from-plusserver-to-slicer-via-openigtlink/28202

---

## Post #1 by @vipulraikar (2023-03-06 22:03 UTC)

<p>Hi All,</p>
<p>OS: Win10<br>
Slicer: 5.2.2 + Associated extensions SlicerIGT, OpenIGTLink</p>
<p>We are currently trying to stream data from an ultrasound scanner to slicer via PlusServer. Sofar, we have integrated the scanner into pluslib as a device and are able to render 2D and 3D images in fCal. This step confirms that the integration within pluslib is successful. (See image below)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8298f19b979b535bb700ea5e0173871026e9cde1.jpeg" data-download-href="/uploads/short-url/iDjKBwm2R7wDqOwqW0f9iy47VpD.jpeg?dl=1" title="Screenshot 2023-03-06 at 4.41.58 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8298f19b979b535bb700ea5e0173871026e9cde1_2_690x431.jpeg" alt="Screenshot 2023-03-06 at 4.41.58 PM" data-base62-sha1="iDjKBwm2R7wDqOwqW0f9iy47VpD" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8298f19b979b535bb700ea5e0173871026e9cde1_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8298f19b979b535bb700ea5e0173871026e9cde1_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8298f19b979b535bb700ea5e0173871026e9cde1_2_1380x862.jpeg 2x" data-dominant-color="5C5B5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-06 at 4.41.58 PM</span><span class="informations">1920×1200 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when connecting to Slicer via PlusServer and OpenIGTLink, we never see an image being streamed in as a node (see image below). If you notice the pannel to the left, we only ever see the the status ‘node’ but no image node.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57a63a8996eafc64078c084d533ef651e20c81dc.jpeg" data-download-href="/uploads/short-url/cvnGmcrBYzn7WnDATcO2zYHsA56.jpeg?dl=1" title="Screenshot 2023-03-06 at 4.53.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57a63a8996eafc64078c084d533ef651e20c81dc_2_690x406.jpeg" alt="Screenshot 2023-03-06 at 4.53.51 PM" data-base62-sha1="cvnGmcrBYzn7WnDATcO2zYHsA56" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57a63a8996eafc64078c084d533ef651e20c81dc_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57a63a8996eafc64078c084d533ef651e20c81dc_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57a63a8996eafc64078c084d533ef651e20c81dc_2_1380x812.jpeg 2x" data-dominant-color="242528"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-06 at 4.53.51 PM</span><span class="informations">2352×1384 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, attached is the simple config file that, based on the documentation, should allow us to stream images into slicer. Any help would be appraciated. No obvious errors in the logs.</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.0"&gt;
  &lt;DataCollection StartupDelaySec="6.0"&gt;
   &lt;DeviceSet Name="PlusServer: UltrasoundStreaming" Description="Broadcasting 2D/3D US scans through OpenIGTLink" /&gt;
    &lt;Device Id="VideoDevice" Type="USStreamerDevice" IPAddress="10.228.91.93" Port=""&gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="MF" BufferSize="100"/&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
  &lt;/DataCollection&gt;

  &lt;CoordinateDefinitions&gt;

    &lt;Transform From="Image" To="Reference"
      Matrix="
        1	0	0	0
        0	1	0	0
        0	0	1	0
        0	0	0	1"
       Date="2011.12.06 17:57:00"/&gt;

  &lt;/CoordinateDefinitions&gt;

  &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18945"
    SendValidTransformsOnly="true"
    OutputChannelId="VideoStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="IMAGE"/&gt;
      &lt;/MessageTypes&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Reference"/&gt;
      &lt;/ImageNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
&lt;/PlusConfiguration&gt;
</code></pre>

---

## Post #2 by @Sunderlandkyl (2023-03-07 17:10 UTC)

<p>It would be helpful if you could include the PlusServer log.</p>

---

## Post #3 by @vipulraikar (2023-03-07 21:09 UTC)

<p>Hi Kyle, you can find the log in the following gist. I have redacted parts of it since its mostly just printing out framecount.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/vipulraikar/ddbdc677f96c382921d8e7ee58dffb4b">
  <header class="source">

      <a href="https://gist.github.com/vipulraikar/ddbdc677f96c382921d8e7ee58dffb4b" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/vipulraikar/ddbdc677f96c382921d8e7ee58dffb4b" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/vipulraikar/ddbdc677f96c382921d8e7ee58dffb4b</a></h4>

  <h5>Plus_server_log.txt</h5>
  <pre><code class="Text">time|level|timeoffset|message|location
030623_165044.108|INFO|000.006000|&gt; Software version: Plus-2.9.0.d12ebea0 (debug build) - Win64 (debug build)| in vtkPlusLogger(52)
030623_165044.108|INFO|000.006000| Logging at level 4 (DEBUG) to file: C:/PlusLibBuildFolder/bin/Debug/Output/030623_165044_PlusLog.txt| in C:\PlusLibBuildFolder\PlusLib\src\PlusServer\Tools\PlusServer.cxx(81)
030623_165044.109|DEBUG|000.007000| Device set configuration is read from file: a.xml| in C:\PlusLibBuildFolder\PlusLib\src\PlusCommon\vtkPlusConfig.cxx(249)
030623_165044.109|DEBUG|000.007000| Device set configuration file contents: 
 &lt;PlusConfiguration version="2.0"&gt;
   &lt;DataCollection StartupDelaySec="6.0"&gt;
     &lt;DeviceSet Name="PlusServer: UltrasoundStreaming" Description="Broadcasting 2D/3D US scans through OpenIGTLink" /&gt;
     &lt;Device Id="VideoDevice" Type="USStreamerDevice" IPAddress="10.228.91.93"&gt;
       &lt;DataSources&gt;</code></pre>
    This file has been truncated. <a href="https://gist.github.com/vipulraikar/ddbdc677f96c382921d8e7ee58dffb4b" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Sunderlandkyl (2023-03-07 21:26 UTC)

<p>I assume that the redaction removed the “Received new client connection” message from the log. Otherwise I don’t see anything suspicious in the log.</p>
<p>Can you also share your Slicer log?</p>

---

## Post #5 by @vipulraikar (2023-03-07 21:49 UTC)

<p>Yes, the “Received new client connection (client 1 at 127.0.0.1:18944). Number of connected clients: 1|” is present.</p>
<p>Slicer log created just now</p>
<pre><code class="lang-auto">[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Session start time .......: 2023-03-07 16:37:10
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Slicer version ...........: 5.2.2 (revision 31382 / fb46bd1) win-amd64 - installed release
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19044, Code Page 65001) - 64-bit
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Memory ...................: 32571 MB physical, 40763 MB virtual
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - CPU ......................: GenuineIntel , 12 cores, 12 logical processors
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Application path .........: C:/Users/320022720/AppData/Local/NA-MIC/Slicer 5.2.2/bin
[DEBUG][Qt] 07.03.2023 16:37:10 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-31382/SlicerIGSIO/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerIGT/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerIGT/lib/Slicer-5.2/qt-scripted-modules, NA-MIC/Extensions-31382/SlicerOpenIGTLink/lib/Slicer-5.2/qt-loadable-modules, NA-MIC/Extensions-31382/SlicerOpenIGTLink/lib/Slicer-5.2/qt-scripted-modules
[DEBUG][Python] 07.03.2023 16:37:21 [Python] (C:\Users\v\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 07.03.2023 16:37:24 [Python] (C:\Users\v\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 07.03.2023 16:37:24 [Python] (C:\Users\v\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 07.03.2023 16:37:25 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 07.03.2023 16:37:34 [] (unknown:0) - Switch to module:  "OpenIGTLinkIF"
[INFO][VTK] 07.03.2023 16:37:39 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:38:05 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:38:39 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:38:46 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:38:56 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:39:12 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1389) - Disconnected: localhost:18944
[INFO][VTK] 07.03.2023 16:40:31 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:40:46 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1389) - Disconnected: localhost:18944
[INFO][VTK] 07.03.2023 16:40:47 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:40:53 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1389) - Disconnected: localhost:18944
[INFO][VTK] 07.03.2023 16:46:50 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1365) - Connected: localhost:18944
[INFO][VTK] 07.03.2023 16:47:00 [vtkMRMLIGTLConnectorNode (000001D3A609E100)] (D:\D\S\S-0-E-b\SlicerOpenIGTLink\OpenIGTLinkIF\MRML\vtkMRMLIGTLConnectorNode.cxx:1389) - Disconnected: localhost:18944

</code></pre>

---

## Post #6 by @Sunderlandkyl (2023-03-10 20:02 UTC)

<p>I don’t see anything out of place in either log. Try disabling SendValidTransformsOnly.</p>
<p>You may need to set your tool status in the device code.</p>

---

## Post #7 by @vipulraikar (2023-03-12 17:57 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> ,</p>
<p>So it turns out, the framecounter was not updating correctly (error on my part). This is my hypothesis. Since it was always sending frame ‘0’, no new images were timestamped and hence it was failing to send ‘new’ frames so to speak. When I tried temporal calibration, it would not generate any results. Looking at the errors I noticed messages that said that the acquisition was too fast. Tried saving recodrings, which also had same issue (recording can’t keep up). So debugging/stepping throught the temporal caibration code showed a stack of recoded frames as null with similar time stamps. This helped me trace it back to a bug on my part.</p>
<p>Thanks again for taking the time!</p>
<p>Best,<br>
Vipul</p>

---
