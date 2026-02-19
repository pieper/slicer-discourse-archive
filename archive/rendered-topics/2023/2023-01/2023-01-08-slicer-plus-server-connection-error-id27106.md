---
topic_id: 27106
title: "Slicer Plus Server Connection Error"
date: 2023-01-08
url: https://discourse.slicer.org/t/27106
---

# Slicer + Plus Server Connection Error

**Topic ID**: 27106
**Date**: 2023-01-08
**URL**: https://discourse.slicer.org/t/slicer-plus-server-connection-error/27106

---

## Post #1 by @Kush_Hari (2023-01-08 03:26 UTC)

<p>Hi,<br>
I am attempting to obtain the appropriate transforms for a configuration of NDI markers. I am using the Polaris Vega VT camera, and the Plus Remote module on Slicer. When I launch the Plus server individually, the connection works. But once I launch the Plus Remote module and link the server, I get the following error.</p>
<p>Failed to create IMAGE message - unable to pack image message</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebe3fc42c1867efb98b2dc8755dd0191e31e619f.jpeg" data-download-href="/uploads/short-url/xEMF2LbFo6CT2aS4jTv6V51293x.jpeg?dl=1" title="IMG_3034" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe3fc42c1867efb98b2dc8755dd0191e31e619f_2_666x500.jpeg" alt="IMG_3034" data-base62-sha1="xEMF2LbFo6CT2aS4jTv6V51293x" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe3fc42c1867efb98b2dc8755dd0191e31e619f_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe3fc42c1867efb98b2dc8755dd0191e31e619f_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe3fc42c1867efb98b2dc8755dd0191e31e619f_2_1332x1000.jpeg 2x" data-dominant-color="979391"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_3034</span><span class="informations">1920×1440 731 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @ungi (2023-01-09 02:54 UTC)

<p>Hi, it’s interesting that IMAGE message occurs in your log. If you are only using a position tracker and no imaging device (e.g. ultrasound), then PLUS should not try to create an IMAGE message. Do you want to post the contents of your PLUS config file here?</p>

---

## Post #3 by @Kush_Hari (2023-01-09 21:11 UTC)

<p>Yeah, the contents are attached in the below file.</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet
      Name="PlusServer: NDI Vega tracker with passive markers"
      Description="Broadcasting tool tracking data through OpenIGTLink
For NDI Vega: Tool (8700339), Stylus (8700340), Reference (8700449)" /&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="NDITracker"
      NetworkHostname="P9-13119"
      NetworkPort="8765"
      ToolReferenceFrame="Reference" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Stylus" RomFile="NdiToolDefinitions/8700340.rom"  /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
          &lt;DataSource Id="Stylus"/&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;


    &lt;Device
      Id="TrackedVideoDevice"
      Type="VirtualMixer" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
      &lt;/InputChannels&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackedVideoStream"/&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
  &lt;/DataCollection&gt;

  &lt;CoordinateDefinitions&gt;
    &lt;Transform From="Image" To="Reference"
      Matrix="
        1	0	0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1"
       Error="0.554951" Date="012617_105449" /&gt;
    &lt;Transform From="StylusTip" To="Stylus"
      Matrix="
        1	0	0.000203823	0.0180449
        3.31529e-09	-1	-1.62655e-05	-0.00144002
        0.000203823	1.62655e-05	-1	-88.5321
        0	0	0	1"
       Error="0.554951" Date="012617_105449" /&gt;
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
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;
      &lt;/ImageNames&gt;
      &lt;TransformNames&gt;
        &lt;Transform Name="StylusTipToReference" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

&lt;/PlusConfiguration&gt;
</code></pre>

---

## Post #4 by @ning_w (2024-08-08 12:20 UTC)

<p>Hello, can we use your .xml file in our laboratory equipment Polaris Vega ST? I tried to load your file in Plus, but it kept giving me an error. As a beginner, I really hope to get help. Thank you very much.<br>
The following is the error reported by pkus:<br>
|INFO|000.032000| Software version: Plus-2.8.0.62873a16 - Win64| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(122)<br>
|INFO|000.032000| Logging at level 3 to file: D:/PlusServer/install/PlusApp-2.8.0.20191105-Win64/data/080824_194208_PlusLog.txt| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(123)<br>
|INFO|000.379000| Supported devices: - 3dConnexion (ver: Plus-2.8.0) - AuroraTracker (ver: NDICAPI-1.7) - BkProFocusOem (ver: Plus-2.8.0) - ChRobotics (ver: Plus-2.8.0) - Epiphan (ver: Plus-2.8.0) - FakeTracker (ver: Plus-2.8.0) - GenericSerialDevice (ver: Plus-2.8.0) - ICCapturing (ver: The Imaging Source UDSHL-3.4) - ImageProcessor (ver: Plus-2.8.0) - IntelRealSense (ver: Plus-2.8.0) - Microchip (ver: Plus-2.8.0) - MmfVideo (ver: Plus-2.8.0) - NDITracker (ver: NDICAPI-1.7) - NoiseVideo (ver: Plus-2.8.0) - OpenCVVideo (ver: Plus-2.8.0) - OpenIGTLinkTracker (ver: OpenIGTLink v3.1.0) - OpenIGTLinkVideo (ver: OpenIGTLink v3.1.0) - OptiTrack (ver: Plus-2.8.0) - OpticalMarkerTracker (ver: Plus-2.8.0) - PhidgetSpatial (ver: Plus-2.8.0) - PolarisTracker (ver: NDICAPI-1.7) - SavedDataSource (ver: Plus-2.8.0) - UsSimulator (ver: Plus-2.8.0) - VFWVideo (ver: Plus-2.8.0) - VirtualBufferedCapture (ver: Plus-2.8.0) - VirtualCapture (ver: Plus-2.8.0) - VirtualDiscCapture (ver: Plus-2.8.0) - VirtualMixer (ver: Plus-2.8.0) - VirtualSwitcher (ver: Plus-2.8.0) - VirtualTextRecognizer (ver: Plus-2.8.0) - VirtualVolumeReconstructor (ver: Plus-2.8.0) - WitMotionTracker (ver: Plus-2.8.0) | in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(127)<br>
|INFO|000.382000| Server host name: PC-20221110SWJT| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(158)<br>
|INFO|000.387000| Server IP addresses: 169.254.216.10, 169.254.189.249, 192.168.2.94, 127.0.0.1| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(178)<br>
|INFO|000.387000| Start remote control server at port: 18904| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(187)<br>
|INFO|153.504000| Connect using configuration file: D:\PlusServer\install\PlusApp-2.8.0.20191105-Win64\config\PlusDeviceSet_Server_NDIVega.xml| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(639)<br>
|INFO|153.505000| Server process command line: “D:/PlusServer/install/PlusApp-2.8.0.20191105-Win64/bin/PlusServer.exe” --config-file=“PlusDeviceSet_Server_NDIVega.xml” --verbose=3| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(320)<br>
|INFO|154.167000| Server process started successfully| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(329)<br>
|ERROR|244.895000|SERVER&gt; Unable to open OpenCV video device.| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(193)<br>
|ERROR|244.908000|SERVER&gt; VideoDevice: Cannot connect to data source, ConnectInternal failed| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1147)<br>
|ERROR|244.908000|SERVER&gt; Unable to connect device: VideoDevice.| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(353)<br>
|ERROR|244.998000|SERVER&gt; Host not capable of given communications parameters| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\NDICAPITracking\vtkPlusNDITracker.cxx(429)<br>
|ERROR|244.998000|SERVER&gt; Datacollector failed to connect to devices| in :\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(106)<br>
|INFO|245.070000|SERVER&gt; warning: Error opening file (/build/opencv/modules/videoio/src/cap_ffmpeg_impl.hpp:808)<br>
|INFO|245.071000|SERVER&gt; warning: rtsp://192.168.0.30/video (/build/opencv/modules/videoio/src/cap_ffmpeg_impl.hpp:809)<br>
|ERROR|245.078000| Server stopped unexpectedly. Return code: 1| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(864)<br>
|INFO|245.079000| Disconnect request successful| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(632)</p>

---
