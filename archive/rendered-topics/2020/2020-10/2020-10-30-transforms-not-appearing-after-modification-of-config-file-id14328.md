---
topic_id: 14328
title: "Transforms Not Appearing After Modification Of Config File"
date: 2020-10-30
url: https://discourse.slicer.org/t/14328
---

# Transforms not appearing after modification of config file

**Topic ID**: 14328
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/transforms-not-appearing-after-modification-of-config-file/14328

---

## Post #1 by @Ada_123 (2020-10-30 13:34 UTC)

<p>Hello,<br>
I would be very grateful if someone could have a look at the config file. We wanted to add on one more tool (Biopsy Needle) after the modification of the config file. Previous tools transforms appear but Biopsy Needle transforms (BiopsyNeedleToReference and BiopsyNeedleToTrackerNot). I am attaching the print screen and the config file. Thank you!</p>
<pre><code class="lang-xml"> &lt;PlusConfiguration version="2.7"&gt;

  &lt;DataCollection StartupDelaySec="1.0"&gt;
    &lt;DeviceSet
      Name="PlusServer: OptiTrack (Profile file Stylus and TrajectoryGuide and BiopsyNeedle)"
      Description="Broadcasting tracking data through OpenIGTLink."
    /&gt;
    &lt;Device
      Id="TrackerDevice"
      Type="OptiTrack"
      ToolReferenceFrame="Tracker" 
      Profile="Slicer tracking test1 (GL).motive"
      AttachToRunningMotive="TRUE"
      MotiveDataDescriptionsUpdateTimeSec="1.0" &gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Stylus" RigidBodyFile="Stylus.motive" /&gt;
        &lt;DataSource Type="Tool" Id="Reference" RigidBodyFile="Reference.motive" /&gt;
		&lt;DataSource Type="Tool" Id="TrajectoryGuide" RigidBodyFile="TrajectoryGuide.motive" /&gt;
		&lt;DataSource Type="Tool" Id="BiopsyNeedle" RigidBodyFile="BiopsyNeedle.motive" /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream"&gt;
        &lt;DataSource Type="Tool" Id="Stylus" /&gt;
        &lt;DataSource Type="Tool" Id="Reference" /&gt;
		&lt;DataSource Type="Tool" Id="TrajectoryGuide" /&gt;
		&lt;DataSource Type="Tool" Id="BiopsyNeedle" /&gt;
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
        &lt;Transform Name="StylusToTracker" /&gt;
        &lt;Transform Name="ReferenceToTracker" /&gt;
		&lt;Transform Name="TrajectoryGuideToReference" /&gt;
        &lt;Transform Name="TrajectoryGuideToTracker" /&gt;
		&lt;Transform Name="BiopsyNeedleToReference" /&gt;
        &lt;Transform Name="BiopsyNeedleToTracker" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
  
&lt;/PlusConfiguration&gt;
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73785db652ac6907d452cacc85eca336c642abc.jpeg" data-download-href="/uploads/short-url/q8OkJ5Qc1SJAtkNRhA14UAS3bQM.jpeg?dl=1" title="Screenshot (215)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_690x388.jpeg" alt="Screenshot (215)" data-base62-sha1="q8OkJ5Qc1SJAtkNRhA14UAS3bQM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_1380x776.jpeg 2x" data-dominant-color="81858A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (215)</span><span class="informations">1920×1080 431 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73785db652ac6907d452cacc85eca336c642abc.jpeg" data-download-href="/uploads/short-url/q8OkJ5Qc1SJAtkNRhA14UAS3bQM.jpeg?dl=1" title="Screenshot (215)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_690x388.jpeg" alt="Screenshot (215)" data-base62-sha1="q8OkJ5Qc1SJAtkNRhA14UAS3bQM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b73785db652ac6907d452cacc85eca336c642abc_2_1380x776.jpeg 2x" data-dominant-color="81858A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (215)</span><span class="informations">1920×1080 431 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
