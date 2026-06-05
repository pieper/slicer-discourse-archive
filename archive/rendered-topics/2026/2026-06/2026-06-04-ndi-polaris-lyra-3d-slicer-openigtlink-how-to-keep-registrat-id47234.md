---
topic_id: 47234
title: "NDI Polaris Lyra + 3D Slicer OpenIGTLink: How to Keep Registration Valid After Moving the Phantom?"
date: 2026-06-04
url: https://discourse.slicer.org/t/47234
last_bumped: 2026-06-04T20:32:13.052Z
---

# NDI Polaris Lyra + 3D Slicer OpenIGTLink: How to Keep Registration Valid After Moving the Phantom?

**Topic ID**: 47234
**Date**: 2026-06-04
**URL**: https://discourse.slicer.org/t/ndi-polaris-lyra-3d-slicer-openigtlink-how-to-keep-registration-valid-after-moving-the-phantom/47234

---

## Post #1 by @AdamDomafoldi (2026-06-04 12:55 UTC)

<p>Hello,</p>
<p>I have been experimenting with the NDI Polaris Lyra and Slicer OpenIGTLink. I have read all the documentation and, after numerous attempts, I think I have some parts working, but I would like to ask for help.</p>
<h3><a name="p-134145-what-i-want-to-achieve-1" class="anchor" href="#p-134145-what-i-want-to-achieve-1" aria-label="Heading link"></a>What I want to achieve</h3>
<p>I have a phantom skull with an NDI passive marker tool attached to it. I also have a passive stylus tool. My goal is to be able to move the patient’s head (or phantom skull) while maintaining the calibration, so that I do not need to recalibrate every time the head moves. The tracking should remain consistent relative to the stylus tip.</p>
<h3><a name="p-134145-my-workflow-2" class="anchor" href="#p-134145-my-workflow-2" aria-label="Heading link"></a>My workflow</h3>
<p>The NDI Polaris Lyra is connected to the network, and I use the Plus application to stream both the stylus and reference tool passive markers.</p>
<p>In 3D Slicer, I have the following transforms:</p>
<ul>
<li>
<p><code>ToolToTracker</code></p>
</li>
<li>
<p><code>StylusToTracker</code></p>
</li>
</ul>
<p>My first step is to calculate <code>StylusToReference</code>. I use the Transform Processor module to compute a full transform:</p>
<ul>
<li>
<p><strong>From:</strong> <code>ToolToTracker</code></p>
</li>
<li>
<p><strong>To:</strong> <code>StylusToTracker</code></p>
</li>
<li>
<p><strong>Output:</strong> <code>StylusToReference</code></p>
</li>
</ul>
<p>Once I have <code>StylusToReference</code>, I create a <code>Skull_StylusTipToStylus</code> transform and place a needle model under it.</p>
<p>For the fiducial registration workflow, I create the following transforms:</p>
<ul>
<li>
<p><code>ReferenceToInitial</code></p>
</li>
<li>
<p><code>InitialToRAS</code></p>
</li>
</ul>
<p>The final hierarchy is shown below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/248b56760c79e521aa67d4bb8d831b707d123971.png" data-download-href="/uploads/short-url/5dhIyxV4fdmtCuoIrfJtLjUR4I1.png?dl=1" title="hieralchy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/248b56760c79e521aa67d4bb8d831b707d123971.png" alt="hieralchy" data-base62-sha1="5dhIyxV4fdmtCuoIrfJtLjUR4I1" width="562" height="242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hieralchy</span><span class="informations">562×242 4.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-134145-registration-workflow-3" class="anchor" href="#p-134145-registration-workflow-3" aria-label="Heading link"></a>Registration workflow</h3>
<p>The next step is fiducial registration. I create a <code>ReferencePoints</code> point list that I populate using <code>Skull_StylusTipToStylus</code>, and an <code>InitialPoints</code> point list that I place on my skull STL model.</p>
<p>After registration, the tip of the virtual needle is very close to the corresponding point on my real-life printed phantom.</p>
<p>To improve accuracy, I then perform surface registration. I create an <code>InitialSurfacePoints</code> point list, collect approximately 40 points on the phantom surface, and register them to the skull model using the <code>InitialToRAS</code> transform.</p>
<p>After surface registration, the stylus appears even more accurate.</p>
<h3><a name="p-134145-my-question-4" class="anchor" href="#p-134145-my-question-4" aria-label="Heading link"></a>My question</h3>
<p>When I move the patient’s head (or phantom skull), the tracking no longer follows correctly. Shouldn’t <code>StylusToReference</code> be continuously updated through <code>ToolToTracker</code>?</p>
<p>Perhaps I am misunderstanding how the transform hierarchy should work. Should I enable automatic fiducial registration instead of using manual registration?</p>
<p>Any guidance on whether my workflow is correct, or what I may be missing, would be greatly appreciated.</p>
<p>Thank you very much in advance.</p>

---

## Post #2 by @ungi (2026-06-04 18:35 UTC)

<p>Hi, it’s best to send StylusToReference directly from PLUS. You can add that transform to the OpenIGTLink part of the PLUS config file and PLUS will calculate it automatically if Reference and Stylus are available as tracked tools.</p>
<p>I’m not sure what you mean by ToolToTracker. Shouldn’t that be ReferenceToTracker? Anyway, if you call your reference “Tool” then StylusToTool should work just as well as StylusToReference.</p>
<p>Alternatively, you can invert and concatenate transforms in Slicer too, but that is less efficient, and a bit inconvenient.</p>
<p>I hope this helps.</p>

---

## Post #3 by @AdamDomafoldi (2026-06-04 20:32 UTC)

<p>Hi Tamás,</p>
<p>I tried it, but perhaps my configuration is not correct because no transformation appears in SlicerIGT.</p>
<p>Do you have any documentation or tutorial that I could use?</p>
<p>I am using the Tool as Reference. It is the same passive marker, but a bit longer.</p>
<p>My plus configuration:</p>
<pre data-code-wrap="xml"><code class="lang-xml">&lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0" &gt;
  &lt;DeviceSet 
      Name="PlusServer: NDI Polaris tracker with passive markers" 
      Description="Broadcasting tool tracking data through OpenIGTLink
For NDI Polaris passive marker starting kit: Tool (8700339), Stylus (8700340)" /&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="NDITracker"
      ToolReferenceFrame="Tracker" 
      NetworkHostname="192.168.1.115"
      NetworkPort="8765" &gt;
      &lt;DataSources&gt;
  	&lt;DataSource Type="Tool" Id="Tool" RomFile="NdiToolDefinitions/8700339.rom"  /&gt;
        &lt;DataSource Type="Tool" Id="Stylus" RomFile="NdiToolDefinitions/8700340.rom"  /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
          &lt;DataSource Id="Tool"/&gt;
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

    &lt;Transform From="Tool" To="Reference"
    Matrix="
      1 0 0 0
      0 1 0 0
      0 0 1 0
      0 0 0 1" /&gt;
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
        &lt;Transform Name="ToolToReference" /&gt;
        &lt;Transform Name="StylusToReference" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

&lt;/PlusConfiguration&gt;

</code></pre>

---
