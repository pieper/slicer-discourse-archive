# Plus Server error when connecting NDI Aurora tracker to Slicer

**Topic ID**: 27729
**Date**: 2023-02-09
**URL**: https://discourse.slicer.org/t/plus-server-error-when-connecting-ndi-aurora-tracker-to-slicer/27729

---

## Post #1 by @sm-philips (2023-02-09 19:18 UTC)

<p>Hi,</p>
<p>I have been trying to connect a NDI Aurora tracker to Slicer. Initially I just want to visualize the points coming in from the tracker in 3D space. I have couple of issues I am running into.</p>
<ol>
<li>The Plus Server launched and the connection was successful. But the indicator did not turn green. Upon inspection of the log file (attached), I found the error:<code> |ERROR|008.162000| Unable to start data sending. OutputChannelId not found: TrackerStream| in E:\D\PSNP64b\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(328)</code>
</li>
</ol>
<p>The OutputChanneld used in the config file was taken from example config files. I did not find documentation to what OutputChannelIds can be used.</p>
<ol start="2">
<li>In OpenIGTLinkIF, after adding a connector and changing status to Active, Status changes to ON. But in I/O configuration I do not see a visualize option for IN. Also I do not see any transforms. Could anyone advice on what I might be doing wrong? I am following the instruction to visualize tracked tools <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ProcedureStreamingToSlicer.html" rel="noopener nofollow ugc">here</a>
</li>
</ol>
<p>I am guessing 2 might be related to the error in 1. But cannot figure out where things are going wrong.</p>
<p>Config File:</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;
  &lt;DataCollection StartupDelaySec="1.0"&gt;
    &lt;DeviceSet 
      Name="PlusServer: NDI Aurora"
      Description="Broadcasting tool tracking data through OpenIGTLink
      Tracking a single EM pointer and an optical pointer and reference." /&gt;
    &lt;Device
      Id="EmTracker" 
      Type="AuroraTracker"
      SerialPort="3"
      BaudRate="115200"
      AcquisitionRate="20"
      LocalTimeOffsetSec="0.0"
      ToolReferenceFrame="EmTracker" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Pointer" PortName="0" /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="EmTrackerStream"&gt;
          &lt;DataSource Id="Pointer" /&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    
  &lt;/DataCollection&gt;
  &lt;PlusOpenIGTLinkServer 
    MaxNumberOfIgtlMessagesToSend="1" 
    MaxTimeSpentWithProcessingMs="50" 
    ListeningPort="18944" 
    SendValidTransformsOnly="TRUE" 
    OutputChannelId="TrackerStream" &gt; 
    &lt;DefaultClientInfo&gt; 
      &lt;MessageTypes&gt; 
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt; 
        &lt;Transform Name="StylusToReference" /&gt;
        &lt;!-- &lt;Transform Name="ReferenceToOpticalTracker" /&gt;
        &lt;Transform Name="StylusToOpticalTracker" /&gt;
        &lt;Transform Name="PointerToEmTracker" /&gt;         --&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
  
&lt;/PlusConfiguration&gt;
</code></pre>

---

## Post #2 by @Sunderlandkyl (2023-02-09 19:53 UTC)

<p>The output channel in the AuroraTracker device is EmTrackerStream, not TrackerStream.</p>
<p>So in PlusOpenIGTLinkServer:</p>
<pre><code class="lang-auto">OutputChannelId="TrackerStream"
</code></pre>
<p>should be</p>
<pre><code class="lang-auto">OutputChannelId="EmTrackerStream"
</code></pre>

---
