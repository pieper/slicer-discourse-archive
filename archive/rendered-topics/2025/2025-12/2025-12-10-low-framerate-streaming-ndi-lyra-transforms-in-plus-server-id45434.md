---
topic_id: 45434
title: "Low Framerate Streaming Ndi Lyra Transforms In Plus Server"
date: 2025-12-10
url: https://discourse.slicer.org/t/45434
---

# Low Framerate streaming NDI Lyra Transforms in Plus Server

**Topic ID**: 45434
**Date**: 2025-12-10
**URL**: https://discourse.slicer.org/t/low-framerate-streaming-ndi-lyra-transforms-in-plus-server/45434

---

## Post #1 by @damparm (2025-12-10 12:30 UTC)

<p>Hello</p>
<p>My project is to track Telemed ultrasound using a recently purchased NDI Polaris Lyra tracker.</p>
<p>So far PlusServer connects well with Telemed and the tracker, Images are moving in my Slicer scene. But the refreshment rate is very low (3 - 4 Hz) compared to Lyra acquisition rate (10 - 120 Hz).</p>
<p>My config is Windows 11 / Slicer 5.6.2 / PlusApp-2.8.0.20191105-Telemed-Win32</p>
<p>Firmware of the Lyra is 008.010.017</p>
<p>What I’ve tried to speed up refreshment rate :</p>
<ul>
<li>Set up only Telemed in config XML : images refresh at 30 Hz- 40 Hz indicating NDI cause the latency</li>
<li>Set up only NDI Lyra in config XML with 4  tools (passive) transforms : rate decrease to 3 Hz in Slicer</li>
<li>Set up only 1 tool in config XML : same</li>
<li>Tried PlusApp-2.9.0.20251125-Telemed-Win64 : same</li>
</ul>
<p>My last config file looks like this :</p>
<pre><code class="lang-auto">&lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet 
      Name="TEST FRAMERATE NDI ONLY REF ONLY" 
      Description="TEST FRAMERATE NDI ONLY REF ONLY" /&gt;
	 
    &lt;Device
      Id="TrackerDevice"
      Type="NDITracker"
	  NetworkHostname="PB-00525.local"
      ToolReferenceFrame="Tracker" 
	  AcquisitionRate="60"
	  TrackingFrequencyNumber="0"&gt;
      &lt;DataSources&gt;
		&lt;DataSource Type="Tool" Id="Reference" RomFile="PHToolDefinitions/Reference.rom"/&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream" &gt;
		  &lt;DataSource Id="Reference"/&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
    &lt;/DataCollection&gt;

   &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18944"
    SendValidTransformsOnly="false"
    OutputChannelId="TrackerStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt; 
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt; 
		&lt;Transform Name="ReferenceToTracker" /&gt;
	  &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;

</code></pre>
<p>I’ve played with Parameters like AcquisitionRate , TrackingFrequencyNumber , MaxNumberOfIgtlMessagesToSend , SendValidTransformsOnly but still same result in Slicer.</p>
<p>Reading this post : <a href="https://github.com/PlusToolkit/PlusLib/issues/1110" class="inline-onebox" rel="noopener nofollow ugc">Polaris Vega Device - CRC Error upon Averaging Feature Activation on the Device · Issue #1110 · PlusToolkit/PlusLib · GitHub</a> , I have checked that the camera does not average frames (NDI is configured with Data Averaging Depth set to 1)</p>
<p>Any hints ?</p>
<p>Thanks a lot !</p>

---

## Post #2 by @cpinter (2025-12-11 13:38 UTC)

<p>I don’t see any issue with the config file, but I also don’t have much experience (at least from the last decade) with PLUS performance issues. The only thing that occurs to me is trying with <code>SendValidTransformsOnly=”TRUE”</code>?</p>
<p>By the way 5.6.2 is more than a year and a half old. Generally, before trying to help, we tend to ask people to use at least the latest stable version. It is currently 5.10. I find it unlikely that it will make a difference, but better be safe. Can you please try?</p>

---

## Post #3 by @damparm (2025-12-11 16:19 UTC)

<p>Hi Csaba,</p>
<p>Thanks for your reply !</p>
<p>I think I have found the problem which was not related to Plus but to Slicer : I displayed way too large STL models in my transfoms causing Slicer to overload and then decrease IGT client refreshment rate. So I reduced the size of STL files (10 fold) and displayed only required models in the scene.  Now framerate for both Ultrasound and Tranforms is about 30 Hz !!</p>
<p>I will follow your advice to install Slicer 5.10. If you have any other suggestions to optimize resources within Slicer let me know… (In particular, I have seen that Resclice driver and 2D vidibility of models  are quite costly reducing framerate from 60 Hz to about 40 Hz)</p>

---
