---
topic_id: 18461
title: "Connect Plus To The Polaris Vicra"
date: 2021-07-01
url: https://discourse.slicer.org/t/18461
---

# Connect Plus to the Polaris vicra

**Topic ID**: 18461
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/connect-plus-to-the-polaris-vicra/18461

---

## Post #1 by @Matteo_Boles (2021-07-01 16:07 UTC)

<p>Hello,<br>
I am trying to connect the Polaris Vicra to 3D slicer to be able to read the position of the tip of an instrument, but every time I try to connect the Polaris Vicra with Plus I got the following errors:</p>
<pre><code class="lang-auto">|WARNING|2784.624000|SERVER&gt; vtkPlusChannel::GetTrackedFrameListSampled: Frames in the buffer are not available any more at time: 0.672000. Skipping 0.113000 seconds from the recording to catch up. Increase the buffer size or decrease the acquisition rate to avoid this situation.| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1089)

|ERROR|2784.825000|SERVER&gt; Unable to retrieve number of scalar components.| in :\D\PSNPb\PlusLib\src\PlusCommon\IO\vtkPlusNrrdSequenceIO.cxx(585)

|ERROR|2784.841000|SERVER&gt; Unable to prepare header| in :\D\PSNPb\PlusLib\src\PlusDataCollection\VirtualDevices\vtkPlusVirtualCapture.cxx(614)
</code></pre>
<p>I also attach my config file:</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet 
      Name="PlusServer: NDI Polaris tracker with passive markers" 
      Description="Broadcasting tool tracking data through OpenIGTLink
For NDI Polaris passive marker starting kit: Reference (8700339), Stylus (8700340)" /&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="PolarisTracker"
      ToolReferenceFrame="Tracker" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Reference" RomFile="NdiToolDefinitions/8700339.rom"  /&gt;
        &lt;DataSource Type="Tool" Id="Stylus" RomFile="NdiToolDefinitions/8700340.rom"  /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
		  &lt;DataSource Id="Reference"/&gt;
          &lt;DataSource Id="Stylus"/&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;Device
      Id="CaptureDevice"
      Type="VirtualCapture"
      BaseFilename="RecordingTest.igs.nrrd"
      EnableFileCompression="TRUE"
      EnableCapturingOnStart="TRUE" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
      &lt;/InputChannels&gt;
    &lt;/Device&gt;    
  &lt;/DataCollection&gt;

  &lt;CoordinateDefinitions&gt;
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
    OutputChannelId="TrackerStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt;
        &lt;Transform Name="StylusToReference" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

&lt;/PlusConfiguration&gt;
</code></pre>
<p>Hope anybody can help!</p>

---

## Post #3 by @lassoan (2021-07-01 16:21 UTC)

<p>You can remove the capture device for now (you’ll still be able to record at the client side) and see if you still get errors.</p>

---

## Post #4 by @Matteo_Boles (2021-07-01 16:38 UTC)

<p>Now the error is gone but when I go to 3D slicer nothing happen.<br>
These are the steps that I did in 3D slicer:</p>
<ol>
<li>I created a tranform and named it “StylusToReference” as in the config file</li>
<li>I created a needle model that I put as a child of the “StylusToReference” transform</li>
<li>I followed the tutorial and I set up OpenIGTLinkIF module as it was described</li>
</ol>
<p>Now if I am not wrong, when I move the probe seen by the polaris vicra I should also see the needle model move in 3D slicer, right? or I am missing something?</p>

---

## Post #5 by @Matteo_Boles (2021-07-02 07:22 UTC)

<p>I installed:<br>
PlusApp-2.8.0.20190617-Win32.exe and I have 3D slicer 4.11<br>
Are they ok?</p>

---

## Post #6 by @lassoan (2021-07-02 18:32 UTC)

<p>Please use the latest Slicer Preview Release and latest Plus Toolkit release.</p>

---

## Post #7 by @YingyiFang (2021-11-07 11:19 UTC)

<p>Excuse me,I am also conducting a similar experiment,and I have the same problem with you.May I ask if your problem has been solved?If so,could you please reply me how to solve this problem?Thanks so much!!</p>

---

## Post #8 by @lassoan (2021-11-08 02:42 UTC)

<p>See the post that was mark as solution (remove the capture device section from the file).</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/adamrankin">@adamrankin</a> If latest Plus version cannot record a tracking-data-only stream then it is a regression that should be fixed. Not urgent, but at least a bug report should be filed.</p>

---

## Post #9 by @Sunderlandkyl (2021-11-08 16:30 UTC)

<p>Just tested recording a tracking-data-only data stream (from a data replay device) in the latest release, and it recorded fine.</p>

---
