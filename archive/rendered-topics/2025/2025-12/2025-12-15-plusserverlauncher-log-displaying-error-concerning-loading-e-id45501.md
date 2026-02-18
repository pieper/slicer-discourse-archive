# PlusServerLauncher log displaying error concerning loading Echowave US settings

**Topic ID**: 45501
**Date**: 2025-12-15
**URL**: https://discourse.slicer.org/t/plusserverlauncher-log-displaying-error-concerning-loading-echowave-us-settings/45501

---

## Post #1 by @daandevlieger2-alt (2025-12-15 20:50 UTC)

<p>Hi everyone</p>
<p>We’re currently performing the 3D freehand ultrasound setup with 3D slicer (5.6.2), optitrack V120 trio (motive 3.1.0), echowowave 4.2.2 (Telemed Artus and LF11 probe) and PlusApp-2.9.0.20251014-Telemed-Win64 in our lab.</p>
<p>When launching the plus server, we’re able to succesfully connect all devices. However, when looking at the log we noticed an error when plus tries to read the ultrasound parameters:</p>
<p>|ERROR|341.926000|SERVER&gt; Invalid key request sent to vtkPlusParameters::IsSet – FrequencyMhz| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusParameters.cxx(150)</p>
<p>|ERROR|341.966000|SERVER&gt; Invalid key request sent to vtkPlusParameters::IsSet – GainPercent| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusParameters.cxx(150)</p>
<p>|ERROR|341.967000|SERVER&gt; Invalid key request sent to vtkPlusParameters::IsSet – DynRangeDb| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusParameters.cxx(150)</p>
<p>|ERROR|341.967000|SERVER&gt; Invalid key request sent to vtkPlusParameters::IsSet – PowerDb| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusParameters.cxx(150)</p>
<p>|ERROR|341.967000|SERVER&gt; Invalid key request sent to vtkPlusParameters::IsSet – FocusDepthPercent| in D:\a\PlusLib\PlusLib\build\PlusLib\src\PlusDataCollection\vtkPlusParameters.cxx(150)</p>
<p>In the code lines afterwards, it looks like it’s finding the corrsponding parameters:</p>
<p>|INFO|329.222000|SERVER&gt; Setting US parameter DepthMm=60</p>
<p>|INFO|341.967000|SERVER&gt; Setting US parameter FrequencyMhz=9</p>
<p>|INFO|341.968000|SERVER&gt; Setting US parameter DepthMm=60</p>
<p>|INFO|341.968000|SERVER&gt; Setting US parameter GainPercent=60</p>
<p>|INFO|341.968000|SERVER&gt; Setting US parameter DynRangeDb=78</p>
<p>|INFO|341.968000|SERVER&gt; Setting US parameter PowerDb=0</p>
<p>|INFO|341.968000|SERVER&gt; Setting US parameter FocusDepthPercent=60</p>
<p>All parameters do correspond with the ones set in echowave, except for the FocusDepthPercent. We set the focus at 20mm with a scanning depth of 60mm. I tried changing the parameter in echowave, running plus and echowave together and adding the FocusDepthPercent parameter in the xml file, but it never seems to be changing correctly in the log. For instance, when I disconnect en reconnect a couple of time without changing anything, this parameter does change (60, 40, 80, 66.667).</p>
<p>Can anyone explain me:</p>
<ul>
<li>Why the errors display in the log and how I can resolve them or does it even matter?</li>
<li>If echowave needs to be running while launching plus or not</li>
<li>If it’s correct that plus just read the last saved parameters from echowave</li>
<li>what is the parameter FocusDepthPercent really doing and why does it seem to change unexpectedly?</li>
</ul>
<p>Our xml file code:</p>

     
<pre><code class="lang-auto">&lt;!-- Optitrack Configuration --&gt;
&lt;Device Id="TrackerDevice" Type="OptiTrack" ToolReferenceFrame="Tracker" Calibration="N/A" Profile="motiveprofilefile.xml" ProjectFile="motiveprofilefile.xml" AttachToRunningMotive="TRUE" MotiveDataDescriptionsUpdateTimeSec="1.0" LocalTimeOffsetSec="0.2566"&gt; &lt;!-- change LocalTimeOffsetSec="0.2566" to value obtained in temporal calib, add (gpt) Calibration="N/A" to line --&gt;
  &lt;DataSources&gt;
    &lt;DataSource Type="Tool" Id="Stylus" BufferSize="150" /&gt;
    &lt;DataSource Type="Tool" Id="Probe" BufferSize="150" /&gt;
  &lt;/DataSources&gt;
  &lt;OutputChannels&gt;
    &lt;OutputChannel Id="TrackerStream"&gt;
      &lt;DataSource Type="Tool" Id="Stylus" /&gt; &lt;!-- everyting with stylus can be deleted for accuistion file --&gt;
      &lt;DataSource Type="Tool" Id="Probe" /&gt;
    &lt;/OutputChannel&gt;
  &lt;/OutputChannels&gt;
&lt;/Device&gt;

&lt;!-- Telemed Configuration --&gt;
&lt;Device Id="VideoDevice" Type="TelemedVideo" DepthMm="60"&gt; &lt;!-- added depth setting to this line --&gt;
  &lt;DataSources&gt;
    &lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="UN" /&gt;
  &lt;/DataSources&gt;
  &lt;OutputChannels&gt;
    &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
  &lt;/OutputChannels&gt;
&lt;/Device&gt;

&lt;!-- Caputre Decvice Configuration --&gt;
&lt;Device Id="CaptureDevice" Type="VirtualCapture" BaseFilename="RecordingTest.igs.mha" EnableCapturingOnStart="FALSE"&gt;
  &lt;InputChannels&gt;
    &lt;InputChannel Id="VideoStream" /&gt;
  &lt;/InputChannels&gt;
&lt;/Device&gt;

&lt;!-- Video and Optitrack Mixer --&gt;
&lt;Device Id="TrackedVideoDevice" Type="VirtualMixer"&gt;
  &lt;InputChannels&gt;
    &lt;InputChannel Id="TrackerStream" /&gt;
    &lt;InputChannel Id="VideoStream" /&gt;
  &lt;/InputChannels&gt;
  &lt;OutputChannels&gt;
    &lt;OutputChannel Id="TrackedVideoStream" /&gt;
  &lt;/OutputChannels&gt;
&lt;/Device&gt;
</code></pre>



    
      
        
        
      
      
        
        
        
      
      
        
      
    
  



<p>Thank you in advance!</p>

---
