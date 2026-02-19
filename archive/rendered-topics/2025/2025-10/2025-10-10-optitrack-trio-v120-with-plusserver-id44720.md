---
topic_id: 44720
title: "Optitrack Trio V120 With Plusserver"
date: 2025-10-10
url: https://discourse.slicer.org/t/44720
---

# Optitrack Trio V120 with PlusServer

**Topic ID**: 44720
**Date**: 2025-10-10
**URL**: https://discourse.slicer.org/t/optitrack-trio-v120-with-plusserver/44720

---

## Post #1 by @max_05ge (2025-10-10 12:23 UTC)

<p>Hello,</p>
<p>Unfortunately, I can’t launch PlusServer with Optitrack.<br>
First, here are the logs I get with PlusServer:<br>
"<br>
time|level|timeoffset|message|location<br>
101025_110628.500|INFO|000.003000|&gt; Software version: Plus-2.9.0.9d59465a - Win64| in vtkPlusLogger(52)<br>
101025_110628.503|INFO|000.006000|  Software version: Plus-2.9.0.9d59465a - Win64| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(126)<br>
101025_110628.503|INFO|000.006000| Logging at level 3 to file: C:/Users/maxam/PlusApp-2.9.0.20231006-Telemed-Win64/data/101025_110628_PlusLog.txt| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(127)<br>
101025_110629.315|INFO|000.818000| Supported devices:</p>
<ul>
<li>3dConnexion (ver: Plus-2.9.0)</li>
<li>AuroraTracker (ver: NDICAPI-1.7)</li>
<li>BkProFocusOem (ver: Plus-2.9.0)</li>
<li>ChRobotics (ver: Plus-2.9.0)</li>
<li>Epiphan (ver: Plus-2.9.0)</li>
<li>FakeTracker (ver: Plus-2.9.0)</li>
<li>GenericSerialDevice (ver: Plus-2.9.0)</li>
<li>ICCapturing (ver: The Imaging Source UDSHL-3.5)</li>
<li>ImageProcessor (ver: Plus-2.9.0)</li>
<li>IntelRealSense (ver: Plus-2.9.0)</li>
<li>Microchip (ver: Plus-2.9.0)</li>
<li>MmfVideo (ver: Plus-2.9.0)</li>
<li>NDITracker (ver: NDICAPI-1.7)</li>
<li>NoiseVideo (ver: Plus-2.9.0)</li>
<li>OpenCVVideo (ver: Plus-2.9.0)</li>
<li>OpenIGTLinkTracker (ver: OpenIGTLink v3.1.0)</li>
<li>OpenIGTLinkVideo (ver: OpenIGTLink v3.1.0)</li>
<li>OptiTrack (ver: Plus-2.9.0)</li>
<li>OpticalMarkerTracker (ver: Plus-2.9.0)</li>
<li>PhidgetSpatial (ver: Plus-2.9.0)</li>
<li>PolarisTracker (ver: NDICAPI-1.7)</li>
<li>SavedDataSource (ver: Plus-2.9.0)</li>
<li>TelemedVideo (ver: Telemed version unknown| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(131)<br>
101025_110629.340|INFO|000.843000| Server host name: LAPTOP-VO4GMB9P| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(162)<br>
101025_110629.373|INFO|000.876000| Server IP addresses: 172.30.48.1, 192.168.135.211, 127.0.0.1| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(182)<br>
101025_110629.375|INFO|000.877000| Start remote control server at port: 18904| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(191)<br>
101025_110631.980|INFO|003.482000| Connect using configuration file: C:\Users\maxam\PlusApp-2.9.0.20231006-Telemed-Win64\config\PlusDeviceSet_Server_OptiTrack_Profile.xml| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(646)<br>
101025_110631.980|INFO|003.483000| Server process command line: “C:/Users/maxam/PlusApp-2.9.0.20231006-Telemed-Win64/bin/PlusServer.exe” --config-file=“PlusDeviceSet_Server_OptiTrack_Profile.xml” --verbose=3| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(327)<br>
101025_110632.570|INFO|004.073000| Server process started successfully| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(336)<br>
101025_110635.316|INFO|006.819000|SERVER&gt; Software version: Plus-2.9.0.9d59465a - Win64<br>
101025_110635.317|INFO|006.820000|SERVER&gt; Logging at level 3 (INFO) to file: C:/Users/maxam/PlusApp-2.9.0.20231006-Telemed-Win64/data/101025_110632_PlusLog.txt<br>
101025_110635.319|INFO|006.821000|SERVER&gt; Server status: Reading configuration.<br>
101025_110635.320|INFO|006.823000|SERVER&gt; Server status: Connecting to devices.<br>
101025_110635.322|INFO|006.825000|SERVER&gt; Starting NatNet server [IP:127.0.0.1]…<br>
101025_110635.323|INFO|006.826000|SERVER&gt; Starting NatNet server [IP:127.0.0.1]…<br>
101025_110635.323|INFO|006.826000|SERVER&gt; ---------------------------------MOTIVE SETTINGS--------------------------------<br>
101025_110635.325|INFO|006.828000|SERVER&gt; Connected cameras:<br>
101025_110635.334|INFO|006.837000|SERVER&gt; 0: V120:Trio 331578b<br>
101025_110635.335|INFO|006.838000|SERVER&gt; 1: V120:Trio 331578a<br>
101025_110635.335|INFO|006.838000|SERVER&gt; 2: V120:Trio 331578c<br>
101025_110635.336|INFO|006.839000|SERVER&gt; Using Motive profile located at:<br>
101025_110635.336|INFO|006.839000|SERVER&gt; C:/Users/maxam/PlusApp-2.9.0.20231006-Telemed-Win64/config/motiveprofilefile_Maxamed.motive<br>
101025_110635.337|INFO|006.840000|SERVER&gt; Using Motive calibration located at:<br>
101025_110635.338|INFO|006.841000|SERVER&gt; C:/Users/maxam/PlusApp-2.9.0.20231006-Telemed-Win64/config/None<br>
101025_110635.338|INFO|006.841000|SERVER&gt; Tracked rigid bodies:<br>
101025_110635.339|INFO|006.842000|SERVER&gt; Stylus<br>
101025_110635.339|INFO|006.842000|SERVER&gt; Probe<br>
101025_110635.340|INFO|006.843000|SERVER&gt; --------------------------------------------------------------------------------<br>
101025_110636.334|INFO|007.837000|SERVER&gt; Server status: Starting servers.<br>
101025_110636.337|WARNING|007.840000|SERVER&gt;  Buffer item is not in the buffer (Uid: 0)!| in E:\D\PTNPTe64b\PlusLib\src\PlusDataCollection\vtkPlusTimestampedCircularBuffer.cxx(176)<br>
101025_110636.366|WARNING|007.869000|SERVER&gt;  Unable to get timestamp from ProbeToTracker tool tracker buffer for time: 0| in E:\D\PTNPTe64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1295)<br>
101025_110636.367|WARNING|007.870000|SERVER&gt;  Buffer item is not in the buffer (Uid: 0)!| in E:\D\PTNPTe64b\PlusLib\src\PlusDataCollection\vtkPlusTimestampedCircularBuffer.cxx(176)<br>
101025_110636.368|WARNING|007.871000|SERVER&gt;  Unable to get timestamp from StylusToTracker tool tracker buffer for time: 0| in E:\D\PTNPTe64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1295)<br>
101025_110636.368|ERROR|007.871000|SERVER&gt;  Failed to get most recent timestamp from all the tracker tools| in E:\D\PTNPTe64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1312)<br>
101025_110636.401|INFO|007.904000|SERVER&gt; Plus OpenIGTLink server listening on IPs: 169.254.221.243, 172.30.48.1, 169.254.225.90, 169.254.111.91, 192.168.135.211, 169.254.161.53, 127.0.0.1 – port 18944<br>
101025_110636.404|INFO|007.907000|SERVER&gt; Server status: Server(s) are running.<br>
101025_110636.406|INFO|007.909000|SERVER&gt; Press Ctrl-C to quit.<br>
101025_110652.056|INFO|023.559000| Server process stop request sent successfully| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(519)<br>
101025_110654.699|INFO|026.202000| Server process stopped successfully| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(538)<br>
101025_110654.701|INFO|026.204000| Disconnect request successful| in E:\D\PTNPTe64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(639)</li>
</ul>
<p>"</p>
<p>Here is my PlusDeviceSet_Server_OptiTrack_Profile.xml file:<br>
”<br>
</p>
  
<pre><code>&lt;DeviceSet

  Name="PlusServer: OptiTrack (Profile only)"

  Description="Broadcasting tracking data through OpenIGTLink."

/&gt;



&lt;Device

  Id="TrackerDevice"

  Type="OptiTrack"

  ToolReferenceFrame="Tracker" 

  Profile= "motiveprofilefile_Maxamed.motive"

  Calibration="None"

  AttachToRunningMotive="FALSE"

  MotiveDataDescriptionsUpdateTimeSec="1.0" &gt;

  &lt;DataSources&gt;

    &lt;DataSource Type="Tool" Id="Stylus" /&gt;

    &lt;DataSource Type="Tool" Id="Probe"  /&gt;

  &lt;/DataSources&gt;

  &lt;OutputChannels&gt;

    &lt;OutputChannel Id="TrackerStream"&gt;

    &lt;DataSource Type="Tool" Id="Stylus" /&gt;

    &lt;DataSource Type="Tool" Id="Probe" /&gt;

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
</code></pre>
  
<p>&lt;PlusOpenIGTLinkServer</p>
<pre><code>MaxNumberOfIgtlMessagesToSend="1"

MaxTimeSpentWithProcessingMs="50"

ListeningPort="18944"

SendValidTransformsOnly="TRUE"

OutputChannelId="TrackerStream" &gt;

&lt;DefaultClientInfo&gt;

  &lt;MessageTypes&gt;

    &lt;Message Type="TRANSFORM" /&gt;

  &lt;/MessageTypes&gt;

  &lt;TransformNames&gt;

    &lt;Transform Name="StylusToTracker" /&gt;

    &lt;Transform Name="ProbeToTracker" /&gt;

  &lt;/TransformNames&gt;

&lt;/DefaultClientInfo&gt;
</code></pre>
  

<p>”</p>
<p>I have Plus Applications version 2.9.0.2023-10-06 (Telemed-Win64)<br>
I have Motive version 2.1.2</p>
<p>I’ve tried changing the AttachToRunningMotive parameter to TRUE and running Motive alongside it, but it doesn’t change anything.</p>
<p>I also saw that here:</p>
<p>you could add</p>
<pre><code class="lang-auto">&lt;DataSources&gt;
&lt;DataSource Type="Tool" Id="Stylus" BufferSize="150" /&gt;
&lt;DataSource Type="Tool" Id="Probe" BufferSize="150" /&gt;
</code></pre>
<p>But nothing works. Even if I change the BufferSize value, it doesn’t work either.</p>
<p>The ultimate goal will be to use OptiTrack + TeleMed. I can get TeleMed to work, and I get the video stream. However, I can’t get OptiTrack to work, and I don’t know why.</p>
<p>I can also attach my motiveprofilefile_Maxamed.motive file if needed.</p>

---

## Post #2 by @max_05ge (2025-10-12 16:43 UTC)

<p>Hello,</p>
<p>I’ve solved my issue. If anyone encounters the same problem, I can share my configuration files.</p>
<p>Best regards.</p>

---

## Post #3 by @lassoan (2025-10-14 02:44 UTC)

<p>Thanks for the update. There is no need to share the config file, but if you can describe in 1-2 sentences what was unclear, unexpected, or not well documented then that would be helpful. We could then improve our documentation, tutorials, or examples accordingly.</p>

---
