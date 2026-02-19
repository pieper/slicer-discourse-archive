---
topic_id: 39938
title: "Bug And Spatial Calibration In Fcal"
date: 2024-10-30
url: https://discourse.slicer.org/t/39938
---

# BUG and spatial calibration in fCal

**Topic ID**: 39938
**Date**: 2024-10-30
**URL**: https://discourse.slicer.org/t/bug-and-spatial-calibration-in-fcal/39938

---

## Post #1 by @jonortegav (2024-10-30 15:47 UTC)

<p>Hi,</p>
<p>I’m experiencing an issue where fCal unexpectedly closes whenever I attempt to use the Spatial Calibration toolbox. I’m not sure why this is happening, and I haven’t been able to identify any specific error messages leading up to the crash.</p>
<p>Moreover, I have not the opportunity to perform the spatial calibration because it says that “Phantom registration is not available”</p>
<p>Here’s a summary of my setup and the image showing the error:</p>
<p>fCal Version: PlusApp-2.9.0.20240906-Clarius-Win64<br>
Operating System: Windows 11</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d27e48528b19355caa53f3e0b9781b7ec914ba8.png" data-download-href="/uploads/short-url/8J0AUpxJt4nTgaEpWeDCfKMvUnK.png?dl=1" title="Captura de pantalla 2024-10-30 155739" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d27e48528b19355caa53f3e0b9781b7ec914ba8.png" alt="Captura de pantalla 2024-10-30 155739" data-base62-sha1="8J0AUpxJt4nTgaEpWeDCfKMvUnK" width="377" height="282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-10-30 155739</span><span class="informations">377×282 6.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is my XML config file</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1" PlusRevision="Plus-2.9.0.d463ee5d - Win64"&gt;
  &lt;DataCollection StartupDelaySec="2"&gt;
    &lt;DeviceSet Name="PlusServer: (Jon) XML file after doing Temporal Calibration" Description="XML file created after temporal calibration between NDI Polaris tracker and Clarius ultrasound device temporal calibration " /&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="PolarisTracker"
      ToolReferenceFrame="Tracker"
      SerialPort="5"
      CheckDSR="true"
      LocalTimeOffsetSec="0.103834"&gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Tool" RomFile="NdiToolDefinitions/8700339.rom" BufferSize="150"&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              01000000
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700339
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              34801403
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              01000000
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700339
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              34801403
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              01000000
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700339
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              34801403
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
        &lt;/DataSource&gt;
        &lt;DataSource Type="Tool" Id="Stylus" RomFile="NdiToolDefinitions/8700340.rom" BufferSize="150"&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              02000001
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700340
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              34802401
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              02000001
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700340
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              34802401
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              02000001
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700340
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              34802401
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
        &lt;/DataSource&gt;
        &lt;DataSource Type="Tool" Id="Reference" RomFile="NdiToolDefinitions/8700449.rom" BufferSize="150"&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              01000000
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700449
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              3532DC02
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              01000000
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700449
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              3532DC02
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
          &lt;CustomProperties&gt;
            &lt;Manufacturer&gt;
              NDI
            &lt;/Manufacturer&gt;
            &lt;NdiIdentity&gt;
              01000000
            &lt;/NdiIdentity&gt;
            &lt;PartNumber&gt;
              8700449
            &lt;/PartNumber&gt;
            &lt;Revision&gt;
              000
            &lt;/Revision&gt;
            &lt;SerialNumber&gt;
              3532DC02
            &lt;/SerialNumber&gt;
          &lt;/CustomProperties&gt;
        &lt;/DataSource&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream"&gt;
          &lt;DataSource Id="Tool" /&gt;
          &lt;DataSource Id="Stylus" /&gt;
          &lt;DataSource Id="Reference" /&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
      &lt;Parameters /&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="VideoDevice"
      Type="Clarius"
      IpAddress="192.168.1.1"
      TcpPort="5828"
      FrameWidth="640"
      FrameHeight="480"
      ImuEnabled="TRUE"
      ImuOutputFileName="ImuOutput.csv"
      WriteImagesToDisk="FALSE"&gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Video" Id="Video" PortName="B" PortUsImageOrientation="UN" BufferSize="150" /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
      &lt;/OutputChannels&gt;
      &lt;Parameters /&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="CaptureDevice_NDIPolaris"
      Type="VirtualCapture"
      BaseFilename="NDIRecording.igs.nrrd"
      EnableFileCompression="TRUE"
      RequestedFrameRate="20"
      EnableCapturing="FALSE"
      AdquisitionRate="20"
      EnableCaptureOnStart="FALSE"&gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
      &lt;/InputChannels&gt;
      &lt;Parameters /&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="CaptureDevice_Clarius"
      Type="VirtualCapture"
      BaseFilename="ClariusRecording.igs.mha"
      EnableCapturing="FALSE"
      AdquisitionRate="20"
      RequestedFrameRate="20"
      EnableFileCompression="FALSE"
      EnableCaptureOnStart="FALSE"&gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="VideoStream" /&gt;
      &lt;/InputChannels&gt;
      &lt;Parameters /&gt;
    &lt;/Device&gt;
    &lt;Device Id="TrackedVideoDevice" Type="VirtualMixer"&gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
        &lt;InputChannel Id="VideoStream" /&gt;
      &lt;/InputChannels&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackedVideoStream" /&gt;
      &lt;/OutputChannels&gt;
      &lt;Parameters /&gt;
    &lt;/Device&gt;
  &lt;/DataCollection&gt;
  &lt;CoordinateDefinitions&gt;
    &lt;Transform From="Image" To="Reference"
      Matrix="
        0.2	0	0	0
        0	0.2	0	0
        0	0	0.2	0
        0	0	0	1"
       Date="2024.10.16 08:58:47" /&gt;
    &lt;Transform From="Image" To="TransducerOriginPixel"
      Matrix="
        1	0	0	-410
        0	1	0	5
        0	0	1	0
        0	0	0	1"
       Date="2011.12.06 17:57:00" /&gt;
    &lt;Transform From="StylusTip" To="Stylus"
      Matrix="
        0.993277	0	-0.115758	-18.3409
        -0.000238798	-0.999998	-0.00204904	-0.324654
        -0.115758	0.00206291	-0.993275	-157.376
        0	0	0	1"
       Error="0.296001" Date="102824_165712" /&gt;
    &lt;Transform From="Phantom" To="Reference"
      Matrix="
        -0.0128807	-0.998959	-0.0437555	-0.0547717
        -0.999908	0.0130579	-0.00376595	-27.2892
        0.00433338	0.043703	-0.999035	230.147
        0	0	0	1"
       Error="1.35234" Date="103024_133300" /&gt;
  &lt;/CoordinateDefinitions&gt;
  &lt;Rendering WorldCoordinateFrame="Reference" DisplayedImageOrientation="MF"&gt;
    &lt;DisplayableObject Type="Model" ObjectCoordinateFrame="TransducerOrigin" Id="ProbeModel" File="Probe_L14-5_38.stl"
      ModelToObjectTransform="
        -1	0	0	29.7
        0	-1	0	1.5
        0	0	1	-14
        0	0	0	1" /&gt;
    &lt;DisplayableObject Type="Model" ObjectCoordinateFrame="Reference" Id="Volume" /&gt;
    &lt;DisplayableObject Type="Model" ObjectCoordinateFrame="StylusTip" Id="StylusModel" File="Stylus_Example.stl" /&gt;
    &lt;DisplayableObject
      Id="PhantomModel"
      Type="Model"
      ObjectCoordinateFrame="Phantom"
      Opacity="0.6"
      File="fCal_2.0.stl"
      ModelToObjectTransform="
        1	0	0	-35
        0	1	0	-10
        0	0	1	-5
        0	0	0	1" /&gt;
    &lt;DisplayableObject Type="Image" ObjectCoordinateFrame="Image" Id="LiveImage" /&gt;
  &lt;/Rendering&gt;
  &lt;PlusOpenIGTLinkServer MaxNumberOfIgtlMessagesToSend="1" MaxTimeSpentWithProcessingMs="50" ListeningPort="18944" SendValidTransformsOnly="true" OutputChannelId="TrackerStream"&gt;
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
  &lt;PlusOpenIGTLinkServer MaxNumberOfIgtlMessagesToSend="1" MaxTimeSpentWithProcessingMs="50" ListeningPort="54474" SendValidTransformsOnly="false" OutputChannelId="VideoStream"&gt;
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
  &lt;PhantomDefinition&gt;
    &lt;Description Name="fCAL" Type="Multi-N" Version="2.0" WiringVersion="2.0" Institution="Queen's University PerkLab" /&gt;
    &lt;Geometry&gt;
      &lt;Pattern Type="NWire"&gt;
        &lt;Wire Name="7:G1_g1" EndPointFront="30.0 0.0 20.0" EndPointBack="30.0 40.0 20.0" /&gt;
        &lt;Wire Name="8:L1_h1" EndPointFront="55.0 0.0 20.0" EndPointBack="35.0 40.0 20.0" /&gt;
        &lt;Wire Name="9:M1_m1" EndPointFront="60.0 0.0 20.0" EndPointBack="60.0 40.0 20.0" /&gt;
      &lt;/Pattern&gt;
      &lt;Pattern Type="NWire"&gt;
        &lt;Wire Name="4:G3_g3" EndPointFront="30.0 0.0 10.0" EndPointBack="30.0 40.0 10.0" /&gt;
        &lt;Wire Name="5:H3_l3" EndPointFront="35.0 0.0 10.0" EndPointBack="55.0 40.0 10.0" /&gt;
        &lt;Wire Name="6:M3_m3" EndPointFront="60.0 0.0 10.0" EndPointBack="60.0 40.0 10.0" /&gt;
      &lt;/Pattern&gt;
      &lt;Pattern Type="NWire"&gt;
        &lt;Wire Name="1:H5_h5" EndPointFront="35.0 0.0 0.0" EndPointBack="35.0 40.0 0.0" /&gt;
        &lt;Wire Name="2:L5_i5" EndPointFront="55.0 0.0 0.0" EndPointBack="40.0 40.0 0.0" /&gt;
        &lt;Wire Name="3:M5_m5" EndPointFront="60.0 0.0 0.0" EndPointBack="60.0 40.0 0.0" /&gt;
      &lt;/Pattern&gt;
      &lt;Landmarks&gt;
        &lt;Landmark Name="#1" Position="104.3 5.0 20.0" /&gt;
        &lt;Landmark Name="#2" Position="104.3 45.0 20.0" /&gt;
        &lt;Landmark Name="#3" Position="104.3 45.0 0.0" /&gt;
        &lt;Landmark Name="#4" Position="104.3 -5.0 0.0" /&gt;
        &lt;Landmark Name="#5" Position="-34.3 45.0 15.0" /&gt;
        &lt;Landmark Name="#6" Position="-34.3 -5.0 20.0" /&gt;
        &lt;Landmark Name="#7" Position="-34.3 -5.0 0.0" /&gt;
        &lt;Landmark Name="#8" Position="-34.3 45.0 0.0" /&gt;
      &lt;/Landmarks&gt;
      &lt;Planes&gt;
        &lt;Plane Name="Superior" BasePoint="5.5 3.0 35.0" EndPoint1="135.0 3.0 35.0" EndPoint2="135.0 55.0 35.0" /&gt;
        &lt;Plane Name="Inferior" BasePoint="5.5 55.0 0.0" EndPoint1="135.0 55.0 0.0" EndPoint2="135.0 5.5 0.0" /&gt;
        &lt;Plane Name="Outside Unmarked" BasePoint="140.0 5.0 30.0" EndPoint1="140.0 50.0 30.0" EndPoint2="140.0 50.0 5.0" /&gt;
        &lt;Plane Name="Inside Unmarked" BasePoint="125.0 40.0 30.0" EndPoint1="125.0 20.0 10.0" EndPoint2="125.0 40.0 10.0" /&gt;
        &lt;Plane Name="Outside Marked" BasePoint="0.0 40.0 30.0" EndPoint1="0.0 40.0 5.5" EndPoint2="0.0 15.5 5.5" /&gt;
        &lt;Plane Name="Outside Posterior" BasePoint="130.0 0.0 30.0" EndPoint1="20.0 0.0 30.0" EndPoint2="20.0 0.0 15.0" /&gt;
        &lt;Plane Name="Inside Posterior" BasePoint="110.0 10.0 30.0" EndPoint1="40.0 10.0 30.0" EndPoint2="30.0 10.0 10.0" /&gt;
        &lt;Plane Name="Outside Anterior" BasePoint="130.0 60.0 30.0" EndPoint1="20.0 60.0 30.0" EndPoint2="20.0 60.0 5.0" /&gt;
      &lt;/Planes&gt;
      &lt;References&gt;
        &lt;Reference Name="#1" Position="104.3 5.0 20.0" /&gt;
        &lt;Reference Name="#2" Position="104.3 45.0 20.0" /&gt;
        &lt;Reference Name="#3" Position="104.3 45.0 0.0" /&gt;
        &lt;Reference Name="#4" Position="104.3 -5.0 0.0" /&gt;
        &lt;Reference Name="#5" Position="-34.3 45.0 15.0" /&gt;
        &lt;Reference Name="#6" Position="-34.3 -5.0 20.0" /&gt;
        &lt;Reference Name="#7" Position="-34.3 -5.0 0.0" /&gt;
        &lt;Reference Name="#8" Position="-34.3 45.0 0.0" /&gt;
      &lt;/References&gt;
    &lt;/Geometry&gt;
  &lt;/PhantomDefinition&gt;
  &lt;VolumeReconstruction
    OutputSpacing="0.5 0.5 0.5"
    ClipRectangleOrigin="0 0"
    ClipRectangleSize="820 616"
    Interpolation="LINEAR"
    Optimization="FULL"
    CompoundingMode="MEAN"
    FillHoles="OFF" /&gt;
    
    &lt;fCal
    PhantomModelId="PhantomModel"
    ReconstructedVolumeId="Volume"
    TransducerModelId="ProbeModel"
    StylusModelId="StylusModel"
    ImageDisplayableObjectId="LiveImage"
    NumberOfCalibrationImagesToAcquire="200"
    NumberOfValidationImagesToAcquire="100"
    NumberOfStylusCalibrationPointsToAcquire="200"
    RecordingIntervalMs="100"
    MaxTimeSpentWithProcessingMs="70"
    ImageCoordinateFrame="Image"
    ProbeCoordinateFrame="Probe"
    ReferenceCoordinateFrame="Reference"
    TransducerOriginCoordinateFrame="TransducerOrigin"
    TransducerOriginPixelCoordinateFrame="TransducerOriginPixel"
    TemporalCalibrationDurationSec="10"
    FixedChannelId="VideoStream"
    FixedSourceId="Video"
    MovingChannelId="TrackerStream"
    MovingSourceId="ProbeToTracker"
    DefaultSelectedChannelId="TrackedVideoStream"
    FreeHandStartupDelaySec="3" /&gt;

    &lt;Segmentation
    ApproximateSpacingMmPerPixel="0.078"
    MorphologicalOpeningCircleRadiusMm="0.27"
    MorphologicalOpeningBarSizeMm="2"
    MaxLinePairDistanceErrorPercent="10"
    AngleToleranceDegrees="10"
    MaxAngleDifferenceDegrees="10"
    MinThetaDegrees="-70"
    MaxThetaDegrees="70"
    MaxLineShiftMm="10"
    ThresholdImagePercent="10"
    CollinearPointsMaxDistanceFromLineMm="0.6"
    UseOriginalImageIntensityForDotIntensityScore="FALSE"
    NumberOfMaximumFiducialPointCandidates="20"
    ClipRectangleOrigin="27 27"
    ClipRectangleSize="766 562" /&gt;
  


&lt;vtkTemporalCalibrationAlgo ClipRectangleOrigin="27 27" ClipRectangleSize="766 562" /&gt;

&lt;vtkPlusPivotCalibrationAlgo
ObjectMarkerCoordinateFrame="Stylus"
ReferenceCoordinateFrame="Reference"
ObjectPivotPointCoordinateFrame="StylusTip" /&gt;

&lt;vtkPlusPhantomLandmarkRegistrationAlgo
  PhantomCoordinateFrame="Phantom"
  ReferenceCoordinateFrame="Reference"
  StylusTipCoordinateFrame="StylusTip" 
  DetectionTimeSec="1.0"
  StylusTipMaximumDisplacementThresholdMm="1.8" /&gt;

&lt;vtkPhantomLinearObjectRegistrationAlgo
  PhantomCoordinateFrame="Phantom"
  ReferenceCoordinateFrame="Reference"
  StylusTipCoordinateFrame="StylusTip" /&gt;

&lt;vtkPlusProbeCalibrationAlgo
  ImageCoordinateFrame="Image"
  ProbeCoordinateFrame="Probe"
  PhantomCoordinateFrame="Phantom"
  ReferenceCoordinateFrame="Reference" /&gt;

  &lt;fCal&gt;
    &lt;ImageCoordinateFrame&gt;
      Image
    &lt;/ImageCoordinateFrame&gt;
    &lt;WorldCoordinateFrame&gt;
      Reference
    &lt;/WorldCoordinateFrame&gt;
    &lt;PhantomModelId&gt;
      PhantomModel
    &lt;/PhantomModelId&gt;
    &lt;ReconstructedVolumeId&gt;
      Volume
    &lt;/ReconstructedVolumeId&gt;
    &lt;TransducerModelId&gt;
      ProbeModel
    &lt;/TransducerModelId&gt;
    &lt;StylusModelId&gt;
      StylusModel
    &lt;/StylusModelId&gt;
  &lt;/fCal&gt;
  
&lt;/PlusConfiguration&gt;
</code></pre>
<p>(if you prefer in image format)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f903b84ddd6f87a861803efc285993a27a8cea1.jpeg" data-download-href="/uploads/short-url/94j629UHoTi9tHlRghddEPkJjXj.jpeg?dl=1" title="code1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f903b84ddd6f87a861803efc285993a27a8cea1_2_103x500.jpeg" alt="code1" data-base62-sha1="94j629UHoTi9tHlRghddEPkJjXj" width="103" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f903b84ddd6f87a861803efc285993a27a8cea1_2_103x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f903b84ddd6f87a861803efc285993a27a8cea1_2_154x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f903b84ddd6f87a861803efc285993a27a8cea1_2_206x1000.jpeg 2x" data-dominant-color="252526"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">code1</span><span class="informations">1920×9236 632 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jonortegav (2024-10-31 08:39 UTC)

<p>full log:</p>
<pre><code class="lang-auto">|INFO|000.066000| Toolbox changed to Configuration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|054.484000| Connect to devices| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QConfigurationToolbox.cxx(158)
|INFO|054.527000| TrackerDevice: Local time offset: 103.834ms| in E:\D\PTNPCb\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1098)
|INFO|054.531000| Selected US image orientation: UN| in E:\D\PTNPCb\PlusLib\src\PlusDataCollection\vtkPlusDataSource.cxx(300)
|INFO|061.576000| ImageToProbe transform is absent, spatial calibration needs to be performed or imported.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QCapturingToolbox.cxx(214)
|INFO|061.578000| Sampling rate changed to 10 (matching requested frame rate is 30)| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QCapturingToolbox.cxx(593)
|INFO|061.582000| Sampling rate changed to 10 (matching requested frame rate is 20)| in E:\D\PTNPCb\PlusApp\fCal\PlusCaptureControlWidget.cxx(244)
|INFO|061.585000| Sampling rate changed to 10 (matching requested frame rate is 20)| in E:\D\PTNPCb\PlusApp\fCal\PlusCaptureControlWidget.cxx(244)
|INFO|061.585000| ImageToProbe transform is absent, spatial calibration needs to be performed or imported.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QCapturingToolbox.cxx(214)
|INFO|061.585000| Sampling rate changed to 10 (matching requested frame rate is 30)| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QCapturingToolbox.cxx(593)
|INFO|061.585000| Toolbox changed to Capturing| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|068.083000| Toolbox changed to Stylus calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|ERROR|071.572000| Unable to find required vtkPlusPhantomLinearObjectRegistrationAlgo element in device set configuration| in E:\D\PTNPCb\PlusLib\src\PlusCalibration\vtkPhantomLinearObjectRegistrationAlgo\vtkPlusPhantomLinearObjectRegistrationAlgo.cxx(321)
|WARNING|071.588000| Phantom plane definitions not found in XML tree. Perform Landmark Registration instead!| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(161)
|INFO|071.595000| Toolbox changed to Phantom registration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|071.595000| Less than 3 landmarks! Try again| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(1142)
|ERROR|071.597000| Unable to find required vtkPlusPhantomLinearObjectRegistrationAlgo element in device set configuration| in E:\D\PTNPCb\PlusLib\src\PlusCalibration\vtkPhantomLinearObjectRegistrationAlgo\vtkPlusPhantomLinearObjectRegistrationAlgo.cxx(321)
|WARNING|071.597000| Phantom plane definitions not found in XML tree. Perform Landmark Registration instead!| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(161)
|INFO|071.599000| Toolbox changed to Phantom registration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|071.599000| Less than 3 landmarks! Try again| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(1142)
|ERROR|071.601000| Unable to find required vtkPlusPhantomLinearObjectRegistrationAlgo element in device set configuration| in E:\D\PTNPCb\PlusLib\src\PlusCalibration\vtkPhantomLinearObjectRegistrationAlgo\vtkPlusPhantomLinearObjectRegistrationAlgo.cxx(321)
|WARNING|071.601000| Phantom plane definitions not found in XML tree. Perform Landmark Registration instead!| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(161)
|INFO|071.604000| Toolbox changed to Phantom registration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|071.604000| Less than 3 landmarks! Try again| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(1142)
|ERROR|071.606000| Unable to find required vtkPlusPhantomLinearObjectRegistrationAlgo element in device set configuration| in E:\D\PTNPCb\PlusLib\src\PlusCalibration\vtkPhantomLinearObjectRegistrationAlgo\vtkPlusPhantomLinearObjectRegistrationAlgo.cxx(321)
|WARNING|071.606000| Phantom plane definitions not found in XML tree. Perform Landmark Registration instead!| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(161)
|INFO|071.607000| Toolbox changed to Phantom registration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|077.868000| Less than 3 landmarks! Try again| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QPhantomRegistrationToolbox.cxx(1142)
|INFO|077.874000| Toolbox changed to Temporal calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|077.877000| Toolbox changed to Temporal calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|077.879000| Toolbox changed to Temporal calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|077.882000| Toolbox changed to Temporal calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|080.865000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.866000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.866000| Toolbox changed to Spatial calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|080.867000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.868000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.868000| Toolbox changed to Spatial calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|080.868000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.869000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.869000| Toolbox changed to Spatial calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
|INFO|080.870000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.870000| Phantom registration is not available: transform between Probe and Reference coordinate frames is missing. Either phantom registration has not performed yet or the ProbeCoordinateFrame, ReferenceCoordinateFrame, or PhantomCoordinateFrame attributes in the device set configuration file are not set correctly.| in E:\D\PTNPCb\PlusApp\fCal\Toolboxes\QSpatialCalibrationToolbox.cxx(290)
|INFO|080.871000| Toolbox changed to Spatial calibration| in E:\D\PTNPCb\PlusApp\fCal\fCalMainWindow.cxx(330)
</code></pre>
<p>Please any guidance in this topic would be appreciated !</p>
<p>Thanks</p>

---

## Post #3 by @jonortegav (2024-11-04 07:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> any update on this? I am kind of desperate because I don’t find the solution to my problem <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>If desired, you can checked the video I recorded showing my problem on: <a href="https://github.com/PlusToolkit/PlusLib/issues/1210" class="inline-onebox" rel="noopener nofollow ugc">BUG: fCal Unexpectedly Closes When Using Spatial Calibration Toolbox · Issue #1210 · PlusToolkit/PlusLib · GitHub</a></p>
<p>I would really appreciate your help !</p>
<p>Thanks</p>

---

## Post #4 by @jonortegav (2024-11-05 08:34 UTC)

<p>I have been able to fix it making this changes that you can compare it with the already uploaded config file:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/503d720d7ef068e39293c787c7b294c7bd538abe.png" data-download-href="/uploads/short-url/brPQkxeawUyOiTIzxQS8nSJvKhg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/503d720d7ef068e39293c787c7b294c7bd538abe.png" alt="image" data-base62-sha1="brPQkxeawUyOiTIzxQS8nSJvKhg" width="401" height="500" data-dominant-color="262728"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×915 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fe9dad78b7dacd95e67e3082b839e8af3e8e62.png" data-download-href="/uploads/short-url/v6t7DztFS3onsrNnYhP2Ea2Ggzo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fe9dad78b7dacd95e67e3082b839e8af3e8e62.png" alt="image" data-base62-sha1="v6t7DztFS3onsrNnYhP2Ea2Ggzo" width="493" height="500" data-dominant-color="242628"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">709×719 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>These changes have been done since I am using the “Tool” NDI marker which is specified in the device part of the config file (check screeshot):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e57761c8168b4975eb7981ad8ddc26bc69cac416.png" data-download-href="/uploads/short-url/wJX79BjMfDNacuKm9lNBnBFxOK2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e57761c8168b4975eb7981ad8ddc26bc69cac416.png" alt="image" data-base62-sha1="wJX79BjMfDNacuKm9lNBnBFxOK2" width="690" height="418" data-dominant-color="252526"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">751×455 24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
