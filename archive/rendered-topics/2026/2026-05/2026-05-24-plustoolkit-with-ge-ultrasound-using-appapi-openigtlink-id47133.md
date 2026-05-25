---
topic_id: 47133
title: "Plustoolkit With Ge Ultrasound Using Appapi Openigtlink"
date: 2026-05-24
url: https://discourse.slicer.org/t/47133
---

# PlusToolkit with GE Ultrasound using AppAPI + OpenIGTLink

**Topic ID**: 47133
**Date**: 2026-05-24
**URL**: https://discourse.slicer.org/t/plustoolkit-with-ge-ultrasound-using-appapi-openigtlink/47133

---

## Post #1 by @nicxo99 (2026-05-24 08:34 UTC)

<p>Hello!</p>
<p>I am trying to connect a GE ultrasound machine to the Plus framework for free-hand calibration (fCal). I am using Slicer to check that the data is valid. I wrote a small program in C++ that sends image data using OpenIGTLink. The image data is originally captured using GE AppAPI interface. Using this program, I am successfully able to stream directly to Slicer using the OpenIGTLinkIF module:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">bool StreamLink::sendImage(const cv::Mat&amp; frame, uint64_t timestamp_ms)
{
    if (socket_.IsNull())
        return false;

    cv::Mat img = frame.clone();

    // Convert BGR -&gt; RGB
    int channels = img.channels();
    if (channels == 3)
    {
        cv::cvtColor(img, img, cv::COLOR_BGR2RGB);
    }

    //----------------------------------
    // IMAGE SETUP
    //----------------------------------

    int size[3] = { img.cols, img.rows, 1 };

    auto imageMsg = igtl::ImageMessage::New();

    imageMsg-&gt;SetHeaderVersion(IGTL_HEADER_VERSION_1);

    imageMsg-&gt;SetDimensions(size);

    int svsize[3] = { img.cols, img.rows, 1 };
    int svoffset[3] = { 0, 0, 0 };

    imageMsg-&gt;SetSubVolume(svsize, svoffset);

    float spacing[3] = { 1.0f, 1.0f, 1.0f };
    imageMsg-&gt;SetSpacing(spacing);

    imageMsg-&gt;SetNumComponents(channels);
    imageMsg-&gt;SetScalarType(igtl::ImageMessage::TYPE_UINT8);

    igtl::Matrix4x4 matrix;
    igtl::IdentityMatrix(matrix);

    matrix[1][1] = -1;
    matrix[1][3] = img.rows - 1;

    imageMsg-&gt;SetMatrix(matrix);

    //----------------------------------
    // Coordinate system
    //----------------------------------

    imageMsg-&gt;SetCoordinateSystem(igtl::ImageMessage::COORDINATE_LPS);

    //----------------------------------
    // Device name
    //----------------------------------

    imageMsg-&gt;SetDeviceName("Video");

    //----------------------------------
    // Allocate image buffer
    //----------------------------------

    imageMsg-&gt;AllocateScalars();

    memcpy(
        imageMsg-&gt;GetScalarPointer(),
        img.data,
        img.total() * img.elemSize()
    );

    //----------------------------------
    // Timestamp
    //----------------------------------

    igtl::TimeStamp::Pointer ts = igtl::TimeStamp::New();

    uint64_t sec = timestamp_ms / 1000;
    uint64_t nsec = (timestamp_ms % 1000) * 1000000;

    ts-&gt;SetTime(sec, nsec);
    imageMsg-&gt;SetTimeStamp(ts);

    static uint32_t frameNumber = 0;
    frameNumber++;
    imageMsg-&gt;SetMetaDataElement("FrameNumber", frameNumber);

    //----------------------------------
    // Pack + send
    //----------------------------------

    imageMsg-&gt;Pack();

    int sent = socket_-&gt;Send(
        imageMsg-&gt;GetPackPointer(),
        imageMsg-&gt;GetPackSize()
    );

    //std::cout &lt;&lt; "Sent frame "
    //    &lt;&lt; img.cols &lt;&lt; "x" &lt;&lt; img.rows
    //    &lt;&lt; " channels=" &lt;&lt; channels
    //    &lt;&lt; " bytes=" &lt;&lt; imageMsg-&gt;GetPackSize()
    //    &lt;&lt; std::endl;

    return sent &gt; 0;
}
</code></pre>
<p>However, when integrating it with the Plus framework I can connect to my OpenIGTLink server, but I am no longer able to receive the data in Slicer. I am using this config file in the PlusToolkit:</p>
<pre data-code-wrap="xml"><code class="lang-xml">&lt;PlusConfiguration version="2.9"&gt;

  &lt;DataCollection StartupDelaySec="1.0"&gt;
    &lt;DeviceSet
      Name="fCal: GE ultrasound + Atracsys"
      Description="Broadcasting ultrasound data from GE HealthCare + tracking data from Atracsys spryTrack180, fusionTrack250 or fusionTrack500 through OpenIGTLink."
    /&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="AtracsysTracker"
      MaxMissingFiducials="1"
      MaxMeanRegistrationErrorMm="1.0"
      ToolReferenceFrame="Tracker" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Stylus" TrackingType="PASSIVE" GeometryFile="AtracsysTools/geometry420.ini" GeometryId="420" /&gt;
        &lt;DataSource Type="Tool" Id="Probe" TrackingType="PASSIVE" GeometryFile="AtracsysTools/geometry505.ini" GeometryId="505" /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream"&gt;
        &lt;DataSource Type="Tool" Id="Stylus" /&gt;
        &lt;DataSource Type="Tool" Id="Probe" /&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
	
	&lt;!-- ========================= --&gt;
    &lt;!-- ULTRASOUND (FROM C++ IGTL SERVER) --&gt;
    &lt;!-- ========================= --&gt;
    &lt;Device
      Id="VideoDevice"
      Type="OpenIGTLinkVideo"
	  MessageType="IMAGE"
      ServerAddress="127.0.0.1"
      ServerPort="18945"
      Active="true"
	  IgtlMessageCrcCheckEnabled="false"
      LocalTimeOffsetSec="0"
	  ReceiveTimeoutSec="5"
	  ReconnectOnReceiveTimeout="true"&gt;

      &lt;DataSources&gt;
        &lt;DataSource Id="Video" Type="Video" PortUsImageOrientation="MF" /&gt;
      &lt;/DataSources&gt;

      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream"
                       VideoDataSourceId="Video"/&gt;
      &lt;/OutputChannels&gt;

    &lt;/Device&gt;

    &lt;!-- ========================= --&gt;
    &lt;!-- FUSION (TRACKED VIDEO) --&gt;
    &lt;!-- ========================= --&gt;
    &lt;Device
      Id="TrackedVideoDevice"
      Type="VirtualMixer"
	  ToolReferenceFrame="Tracker" &gt;

      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream"/&gt;
        &lt;InputChannel Id="VideoStream"/&gt;
      &lt;/InputChannels&gt;

      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackedVideoStream"/&gt;
      &lt;/OutputChannels&gt;

    &lt;/Device&gt;

  &lt;/DataCollection&gt;

  &lt;!-- ========================= --&gt;
  &lt;!-- OPENIGTLINK SERVER (TO SLICER) --&gt;
  &lt;!-- ========================= --&gt;
  &lt;PlusOpenIGTLinkServer
    ListeningPort="18944"
    OutputChannelId="TrackedVideoStream"
    SendValidTransformsOnly="TRUE"&gt;

    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="IMAGE"/&gt;
        &lt;Message Type="TRANSFORM"/&gt;
      &lt;/MessageTypes&gt;
    &lt;/DefaultClientInfo&gt;

    &lt;TransformNames&gt;
      &lt;Transform Name="StylusToTracker"/&gt;
      &lt;Transform Name="ProbeToTracker"/&gt;
    &lt;/TransformNames&gt;
	
	&lt;ImageNames&gt;
        &lt;Image Name="Video" EmbeddedTransformToFrame="Probe" /&gt;
      &lt;/ImageNames&gt;

  &lt;/PlusOpenIGTLinkServer&gt;
  
&lt;/PlusConfiguration&gt;
</code></pre>
<p>And I receive these errors in the log, which indicate that maybe something is wrong with my timestamps, I just don’t know what:</p>
<pre data-code-wrap="plaintext"><code class="lang-plaintext">052226_123756.913|INFO|011.913000| Received new client connection (client 1 at 127.0.0.1:18944). Number of connected clients: 1| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(298)
052226_123756.927|TRACE|011.927000| vtkPlusAtracsysTracker::InternalUpdate| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\Atracsys\vtkPlusAtracsysTracker.cxx(716)
052226_123756.927|INFO|011.927000| OpenIGTLink broadcasting started. No data was available between 0-5.514sec, therefore no data were broadcasted during this time period.| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(449)
052226_123756.927|TRACE|011.927000| vtkPlusDevice::GetTrackedFrameList(5.614, 50)| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(719)
052226_123756.927|TRACE|011.927000| Unable to get latest timestamp from video buffer!| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1275)
052226_123756.927|TRACE|011.927000| Failed to get video buffer item UID from time: 11.911000| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1427)
052226_123756.927|TRACE|011.927000| Failed to get video buffer timestamp from UID: 268| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1429)
052226_123756.927|TRACE|011.927000| Unable to get most recent timestamp!| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(756)
052226_123756.927|TRACE|011.927000| Number of added frames: 50 out of 50| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(937)
052226_123756.934|TRACE|011.935000| Failed to get tracked frame list from data collector (last recorded timestamp: 11.863000| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(454)
</code></pre>

---
