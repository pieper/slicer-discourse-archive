---
topic_id: 33876
title: "Temporal Calibration In 3D Slicer"
date: 2024-01-19
url: https://discourse.slicer.org/t/33876
---

# Temporal calibration in 3D slicer

**Topic ID**: 33876
**Date**: 2024-01-19
**URL**: https://discourse.slicer.org/t/temporal-calibration-in-3d-slicer/33876

---

## Post #1 by @MReza (2024-01-19 17:00 UTC)

<p>Hello,<br>
I’m wondering if it’s possible to perform temporal calibration in 3D Slicer as well. According to the Slicer IGT tutorial, temporal calibration seems to require the use of fCal. However, using fCal for temporal calibration also involves pivot calibration. I appreciate any guidance you can provide on this matter.<br>
Thank you.</p>

---

## Post #2 by @ungi (2024-01-21 20:02 UTC)

<p>While there is no dedicated module for temporal calibration, I find it relatively easy to do it with existing modules. Just record the data streams from two devices using maximum frame rate in the Sequences module of Slicer. While recording the data streams, do sudden direction changes with both tools at the same time. While replaying the recording frame-by-frame, you can observe the timestamps and note for yourself how much delay is there between the direction changes of the two tools. If you repeat the measurement 5-10 times, you will get a quite accurate estimation of both the delay and the variability in delay.</p>

---

## Post #3 by @jonortegav (2024-10-16 06:13 UTC)

<p>Hello <a class="mention" href="/u/ungi">@ungi</a>,</p>
<p>Once you estimate the delay between the data stream of the devices, what do you need to do with that information if you want to follow the ultrasound spatial calibration following the SlicerIGT tutorial available in:</p>
<p><a href="https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018%213712&amp;authkey=!ACNGX3PqH0BLg74" class="onebox" target="_blank" rel="noopener nofollow ugc">https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3712&amp;authkey=!ACNGX3PqH0BLg74</a></p>
<p>I have already perform the temporal calibration using Clarius C3 HD3 ultrasound and NDI Polaris Spectra tracker but i don’t know how to use the delay measured in the temporal calibration for a correct spatial calibration.</p>
<p>Any guidance will be appreciated,</p>
<p>Thank you</p>

---

## Post #4 by @jonortegav (2024-10-16 07:37 UTC)

<p>PD: The temporal calibration has been done using fCal application and after performing the temporal calibration the device set configuration has been saved in XML format (see figure)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7365800612444251a70939e4e309223044eddeb2.png" alt="image" data-base62-sha1="gsQn49gonQTxrPDOoIc0KqdyeHg" width="387" height="437"></p>

---

## Post #5 by @cpinter (2024-10-16 08:47 UTC)

<p>I think this page explains it all<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/AlgorithmTemporalCalibration.html" class="onebox" target="_blank" rel="noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/AlgorithmTemporalCalibration.html</a></p>
<p>You need to add that number as parameter <code>TemporalCalibrationDurationSec</code>.</p>

---

## Post #6 by @jonortegav (2024-10-16 08:57 UTC)

<p>i have already read that page but i haven’t noticed anything related to how to use the temporal calibration done in fCal in 3D slicer.</p>
<p>this is my config XML file. I think I defined the parameter you mentioned “TemporalCalibrationDurationSec”</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;
  &lt;DataCollection StartupDelaySec="2.0" &gt;
    &lt;DeviceSet 
      Name="PlusServer: (Jon) Temporal Calibration with NDI Polaris tracker and Clarius ultrasound device" 
      Description="No description" /&gt;
    
    &lt;!-- NDI Polaris Tracker Device --&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="PolarisTracker"
      ToolReferenceFrame="Tracker" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Tool" RomFile="NdiToolDefinitions/8700339.rom"/&gt;
        &lt;DataSource Type="Tool" Id="Stylus" RomFile="NdiToolDefinitions/8700340.rom"/&gt;
        &lt;DataSource Type="Tool" Id="Reference" RomFile="NdiToolDefinitions/8700449.rom"/&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
          &lt;DataSource Id="Tool"/&gt;
          &lt;DataSource Id="Stylus"/&gt;
          &lt;DataSource Id="Reference"/&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;

    &lt;!-- Clarius Ultrasound Device --&gt;
    &lt;Device Id="VideoDevice"
      Type="Clarius"
      IpAddress = "192.168.1.1"
      TcpPort = "5828"
      FrameWidth = "640"
      FrameHeight = "480"
      ImuEnabled = "TRUE"
      ImuOutputFileName = "ImuOutput.csv"
      WriteImagesToDisk = "FALSE"&gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Video" Id="Video" PortName="B" PortUsImageOrientation="UN"/&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;


    &lt;!-- Virtual Capture Device for NDI Polaris --&gt;
    &lt;Device
      Id="CaptureDevice_NDIPolaris"
      Type="VirtualCapture"
      BaseFilename="NDIRecording.igs.nrrd"
      EnableFileCompression="TRUE"
      RequestedFrameRate="20"
      EnableCapturing="TRUE"
      AdquisitionRate="20" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
      &lt;/InputChannels&gt;
    &lt;/Device&gt;

    &lt;!-- Virtual Capture Device for Clarius Ultrasound --&gt;
    &lt;Device
      Id="CaptureDevice_Clarius"
      Type="VirtualCapture"
      BaseFilename= "ClariusRecording.igs.mha"
      EnableCapturing="TRUE"
      AdquisitionRate="20"
      RequestedFrameRate="20"&gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="VideoStream" /&gt;
      &lt;/InputChannels&gt;
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

  &lt;/DataCollection&gt;
  
  &lt;CoordinateDefinitions&gt;

    &lt;!-- NDI Polaris Stylus coordinate transformation --&gt;
    &lt;Transform From="StylusTip" To="Stylus"
      Matrix="
        1	0	0.000203823	0.0180449
        3.31529e-09	-1	-1.62655e-05	-0.00144002
        0.000203823	1.62655e-05	-1	-88.5321
        0	0	0	1"
       Error="0.554951" Date="012617_105449" /&gt;

    &lt;!-- Clarius Ultrasound Image coordinate transformation --&gt;
    &lt;Transform From="Image" To="Reference"
      Matrix="
      0.2 0.0 0.0 0.0
      0.0 0.2 0.0 0.0
      0.0 0.0 0.2 0.0
      0 0 0 1" /&gt;

    &lt;Transform From="Image" To="TransducerOriginPixel"
    Matrix="1 0 0 -410
            0 1 0 5
            0 0 1 0
            0 0 0 1"
    Date="2011.12.06 17:57:00" Error="0.0" /&gt;
  &lt;/CoordinateDefinitions&gt;

  &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="64010"
    SendValidTransformsOnly="false"
    OutputChannelId="VideoStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="IMAGE" /&gt;
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;
      &lt;/ImageNames&gt;
      &lt;TransformNames&gt;
        &lt;Transform Name="ImageToReference" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

    &lt;!-- NDI Polaris PlusOpenIGTLinkServer config --&gt;
    &lt;PlusOpenIGTLinkServer 
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18944"
    SendValidTransformsOnly="true"
    OutputChannelId="TrackerStream"&gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt;
        &lt;Transform Name="StylusTipToReference" /&gt;
        &lt;Transform Name="ToolToReference" /&gt;
        &lt;Transform Name="ToolToTracker" /&gt;
        &lt;Transform Name="StylusToTracker" /&gt;
        &lt;Transform Name="ReferenceToTracker" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

  &lt;fCal
  NumberOfCalibrationImagesToAcquire="200"
  NumberOfValidationImagesToAcquire="100"
  NumberOfStylusCalibrationPointsToAcquire="200"
  RecordingIntervalMs="100"
  MaxTimeSpentWithProcessingMs="70"
  TemporalCalibrationDurationSec="10"
  FixedChannelId="VideoStream" 
  FixedSourceId="Video"
  MovingChannelId="TrackerStream"
  MovingSourceId="ReferenceToTracker"
  DefaultSelectedChannelId="TrackedVideoStream" 
  FreeHandStartupDelaySec="3" /&gt;

  &lt;vtkTemporalCalibrationAlgo
  ClipRectangleOrigin="27 27" 
  ClipRectangleSize="766 562" /&gt;

&lt;/PlusConfiguration&gt;
</code></pre>

---

## Post #7 by @cpinter (2024-10-16 09:07 UTC)

<p>I may be wrong and that parameter is to determine the length of the recording that is used for temporal calibration. Need to see the code at this point.</p>

---

## Post #8 by @cpinter (2024-10-16 09:13 UTC)

<p>Taking another look I think it is this parameter of each device that you need to set after finding out the temporal lag of the devices<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed71596ccef7d195d70cef8eee74320b87b57129.png" data-download-href="/uploads/short-url/xSw0DxHwkACdg2bFCZKxCFUC5ol.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed71596ccef7d195d70cef8eee74320b87b57129.png" alt="image" data-base62-sha1="xSw0DxHwkACdg2bFCZKxCFUC5ol" width="557" height="500" data-dominant-color="F2F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">688×617 21.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>See also here:<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html" class="onebox" target="_blank" rel="noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html</a></p>
<p>" <strong>LocalTimeOffsetSec</strong> . This value allows for compensating time lag of the data acquisition of the device. The value is typically determined by temporal calibration. Global time (common for all devices in the process) is computed from the device’s local time (timestamps provided by the device) as: GlobalTime = LocalTime + LocalTimeOffset. Therefore, if local time is the time when the process receives the data from a device and it takes 0.5 sec for the device to acquire data and send to the process then the LocalTimeOffsetSec value will be -0.5. Optional. Default value is 0 sec."</p>

---
