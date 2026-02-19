---
topic_id: 26410
title: "Confused Trying To Use Bullseye In Slicerigt Viewpoint Modul"
date: 2022-11-23
url: https://discourse.slicer.org/t/26410
---

# Confused trying to use Bullseye in SlicerIGT Viewpoint module to locate and point a camera view

**Topic ID**: 26410
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/confused-trying-to-use-bullseye-in-slicerigt-viewpoint-module-to-locate-and-point-a-camera-view/26410

---

## Post #1 by @mikebind (2022-11-23 18:23 UTC)

<p>Hello, I am trying to have a 3D view camera in Slicer follow the position and orientation of a tracked tool using SlicerIGT.  By following the tutorials I have successfully tracked a tool and gone through the pivot and spin calibrations and can see the tracked tool and registered object moving through 3D space in correct relation to each other in the 3D Slicer views. I now want to set up the second 3D view camera to be looking out from the tip of the tool (like a laryngoscope camera).</p>
<p>I think this is what the “Bullseye” mode of the Viewpoint module of SlicerIGT should do, but I think I am maybe not using it correctly.  I created a linear transform node, placed it as the parent transform node of the camera, and chose it as the “Camera positioning transform”.  I wasn’t sure whether to have the parent transform of that camera transform be the “ToolTipToTool” transform or the “ToolToReference” transform, so I have tried both.  I chose 6DOF and did not change the zoom or translation settings and left “Parallel projection” unchecked. I clicked “Enable Bullseye View Mode”, and the camera view did successfully move around with the tool, but the location and orientation of the view was not what I wanted.  Instead of looking outward towards in the direction the tool pointed, the camera looked backwards along the shaft of the tool.  When I tried some simple modifications to the camera parent transform (like changing signs of the ones on the diagonal) I got changes in view orientation, but also undesired changes in camera position.</p>
<p>I’m sure all I need is a transform that points the camera in the direction I want in the location I want relative to the tool, and then the parent tracked transforms will move things around as I would like, but I’m having trouble figuring out how to get this set up properly.  I’m also not sure whether I need to (in addition to having the proper parent transform on the camera) adjust the camera FocalPoint or ViewUp direction, or whether these will basically just be part of the parent transform.   It seems like the Bullseye View Mode is probably designed to set the camera up more or less in the way I want, but I’m not sure what I am doing wrong in using it, and I can’t find any documentation which would help me sort through it.  Specifically, I want to know:</p>
<ul>
<li>what should the transform hierarchy look like?</li>
<li>which transform in that hierarchy should be chosen as the “camera positioning transform” in the Viewpoint module?</li>
<li>what should happen when I enable Bullseye View Mode?</li>
<li>what should happen when I disable it again? (in my experiments so far, disabling seems to have no effect, the camera continues to move with the tracked tool (because the tracked transform is still above the camera in the transform hierarchy))</li>
<li>do I need to do anything to change or reset the FocalPoint or ViewUp direction on the camera before or after using Bullseye Mode?</li>
</ul>
<p>Also, if these questions would be better asked somewhere else, please let me know and I will ask there.</p>

---

## Post #2 by @lassoan (2022-11-27 03:02 UTC)

<p>Thr Viewpoint module was implemented for exactly this purpose.</p>
<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="26410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>created a linear transform node, placed it as the parent transform node of the camera</p>
</blockquote>
</aside>
<p>Do not place the camera under a transform. Viewpoint module takes care of setting up the camera and putting the camera under a transform will probably interfere with it.</p>
<blockquote>
<p>what should the transform hierarchy look like?</p>
</blockquote>
<p>The Viewpoint module does not require any additional transform. You just need the tooltip to world transform hierarchy.</p>
<blockquote>
<p>which transform in that hierarchy should be chosen as the “camera positioning transform” in the Viewpoint module?</p>
</blockquote>
<p>ToolTipToX (usually ToolTipToTool, which is under ToolToReference, which is under ReferenceToRas).</p>
<blockquote>
<p>what should happen when I enable Bullseye View Mode?</p>
</blockquote>
<p>The camera works as an endoscopic camera mounted on the tool.</p>
<blockquote>
<p>what should happen when I disable it again?</p>
</blockquote>
<p>The camera stops moving.</p>
<blockquote>
<p>do I need to do anything to change or reset the FocalPoint or ViewUp direction on the camera before or after using Bullseye Mode</p>
</blockquote>
<p>You can slightly adjust the camera, but usually not needed.</p>

---

## Post #3 by @mikebind (2022-11-28 16:01 UTC)

<p>Thank you!  I thought it was probably something simple I was missing!</p>

---

## Post #4 by @mikebind (2022-12-01 16:11 UTC)

<p>Thanks for the guidance.  I have now tried using the Bullseye mode exactly as you suggest, and the results are as follows:  The camera moves as if it were located at the tool tip, as desired, but it looks backwards up the shaft of the tool rather than forwards out from the tip of the tool. This is after performing the pivot and spin calibrations on the tool, doing fiducial point registration as outlined in <a href="https://1drv.ms/p/s!AhiABcbe1DBygcAwmU7_GDzj4iGxWg" rel="noopener nofollow ugc">tutorial U-12</a> and verifying that the spatial relationships in Slicer between the tracked tool (just the default ball and stick model) and the imported surface model with fiducials (representing the physical object) correspond to their relative locations and orientations in physical space (just saying that the calibration and registration seems to have worked well).  The ball end of the stick represents the tool tip, correct?  I would be happy to share an mrb file if that would be helpful, but I don’t know if it would be useful or not without the live tracking.</p>

---

## Post #5 by @lassoan (2022-12-04 06:12 UTC)

<p>You can record live tracking data using Sequences module and then you have everything in one file that you can replay using Sequences module. See <a href="https://onedrive.live.com/redir?resid=7230D4DEC6058018!3128&amp;authkey=!AMy-wgNHStEKsPU&amp;ithint=file%2cpptx">U-11 SlicerIGT Tutorial</a>.</p>
<p>Use the needle model that is generated by <code>Create Models</code> module in SlicerIGT extension. The pointer model that OpenIGTLinkIF module creates may use a different direction for the third axis of the StylusTip coordinate system. You can easily swap the z axis direction in the Pivot calibration module.</p>

---

## Post #6 by @brennachampion (2023-02-09 22:26 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> Were you ever able to get this to work? I am having the same problem and although I can switch the z axis using the Pivot Calibration module that only switches the body of the needle, never the way the camera is facing. If you were able to figure this out I’d be interested to learn how you did it. Thanks!</p>

---

## Post #7 by @mikebind (2023-02-10 20:35 UTC)

<p>I will let you know if I get it working.  I’m only at the location where this equipment is intermittently, and have not gotten back to this aspect of this project yet.  Hopefully within the next week or so I’ll be able to give this a try.</p>

---

## Post #8 by @thymallus (2023-10-05 12:18 UTC)

<p>Hello,</p>
<p>What is the best way to receive the ToolTipToTool-transformation matrix from a Medtronic StealthStation (S7) (electromagnetical tracking) via  PlusServer and openIGTlink?</p>
<p>The “XToTool”-transformation obviously already delivers the “XToToolTip” Transformation. Is it possible to to write the configfile in a way that it delivers the ToolTipToTool-transformation-matrix?</p>
<p>Thank you!</p>

---

## Post #9 by @mikebind (2023-10-05 17:34 UTC)

<p>You can incorporate transformation matrices from calibrations in a <code>&lt;CoordinateDefinitions&gt;</code> section of your configuration file.  Here is an example  of what that section could look like, with two supplied matrices, one from a fiducial calibration connecting a fixed sensor to an image volume space, and one which is just used to swap coordinate axis directions to align the coordinate axes of a needle model with the sensor directions.</p>
<pre><code class="lang-auto">    &lt;Transform From="HeadSensor" To="July9Scan"
      Matrix="
        0.0737387	0.997278	-0.000223394	-3.23661
        0.850112	-0.0629744	-0.522823	89.2261
        -0.521414	0.0383624	-0.852441	-129.196
        0	0	0	1"
       Error="0.9" Date="2023.07.11" /&gt;
    &lt;Transform From="NeedleTip" To="StylusSensor"
      Matrix="
        0	0	1	0
        1	0	0	0
        0	1	0	0
        0	0	0	1"
       Error="0" Date="2023.05.02" /&gt;
  &lt;/CoordinateDefinitions&gt;
</code></pre>
<p>To get these transformations (or concatenated transformations which use these) sent to Slicer, you also need to include appropriately named <code>&lt;Transform&gt;</code> elements to the <code>&lt;PlusOpenIGTLinkServer&gt;</code> section.  For example, this is what mine looks like:</p>
<pre><code class="lang-auto">  &lt;PlusOpenIGTLinkServer MaxNumberOfIgtlMessagesToSend="1" MaxTimeSpentWithProcessingMs="50" ListeningPort="18944" SendValidTransformsOnly="true" OutputChannelId="EmTrackerStream"&gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="TRANSFORM" /&gt;
      &lt;/MessageTypes&gt;
      &lt;TransformNames&gt;
        &lt;Transform Name="StylusSensorToEmTracker" /&gt;
        &lt;Transform Name="EmTrackerToHeadSensor" /&gt;
        &lt;Transform Name="NeedleTipToStylusSensor" /&gt;
        &lt;Transform Name="HeadSensorToJuly9Scan" /&gt;
      &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
</code></pre>
<p>I’m not sure if this addresses what you are asking about.  I am working with an electromagnetic rather than optical tracker, but I assume the system is generally similar and hope that some of the above is helpful.</p>

---

## Post #10 by @thymallus (2023-10-11 12:31 UTC)

<p>As a workaround one can define an additional matrix, which is basically a copy of the NeedleTipToStylusSensor, BUT the sign of the z-axis (+/-) is changed. Then take the minimum front/back-translation in the viewpoint-module (-0.01).</p>
<p>Does anyone have a more satisfieing solution?</p>

---
