# Import 3DUS Stradwin Files

**Topic ID**: 25480
**Date**: 2022-09-29
**URL**: https://discourse.slicer.org/t/import-3dus-stradwin-files/25480

---

## Post #1 by @PaulT95 (2022-09-29 05:11 UTC)

<p>Hi everyone,<br>
I have been collecting freehand 3DUS data using StradWin (<a href="http://mi.eng.cam.ac.uk/Main/StradWin" rel="noopener nofollow ugc">http://mi.eng.cam.ac.uk/Main/StradWin</a>) but I would like to perform the segmentation in 3D slicer, however, the file format of the recorded data is .sw (2D image slices) and .sxi (information about the acquisition and the orientation of the slices). I am trying now to figure out how can I merge/convert this information into a single file (nifti or NRRD) but I do not know how to combine properly the information.<br>
Has anyone already performed such a conversion?</p>
<p>Thank you for your help</p>

---

## Post #2 by @lassoan (2022-10-19 13:23 UTC)

<p>If you figure out a solution (e.g., how to export reconstructed volume in a standard file format) then it would be nice if you could share it with the community. Thank you!</p>

---

## Post #3 by @PaulT95 (2022-10-19 16:47 UTC)

<p>Unlucky, it is not perfect yet in terms of absolute length. So, before sharing something that I am not 100% that is correct about, I’d rather wait.</p>
<p>Paolo Tecchio</p>

---

## Post #4 by @lassoan (2022-10-19 17:00 UTC)

<p>You may also consider using 3D Slicer and SlicerIGT and related extensions. SlicerIGT offers much of the same feature set regarding ultrasound image acquisition and volume reconstruction, but it has much more features, they are free, restriction-free open-source software that you can customize and extend, it is actively maintained (while Stradwin development stopped several years ago), and it supports modern workflows (e.g., AI-based real-time processing and live volume reconstruction).</p>

---

## Post #5 by @PaulT95 (2022-10-19 19:16 UTC)

<p>Thank you for the information, I’ve started considering it. The only doubt is about the frame rate acquisition. Currently with Stradwin and Telemed+OptiTrack I can reach 130fps. Is it possible to use these two systems together as well in IGT slicer ?</p>
<p>Paolo Tecchio</p>

---

## Post #6 by @lassoan (2022-10-19 19:45 UTC)

<p>Do you really mean 130 fps? Typical ultrasound imaging frame rate is in the low tens. What probe and imaging settings allow you to have this high frame rate? What is the clinical application?</p>
<p>We typically aim for acquiring images at 15-30fps, as we move the probe on the patient skin slowly and we don’t want to collect and process much of the same images. At this speed we can do acquisition, recording, processing, volume reconstruction, 3D visualization in real-time on an stronger laptop or average desktop computer without issues. Depending on the computer, doing all these operations at higher frame rates may start to become challenging. For use cases that require high frames, we record on server-side (PlusServer has a remote control interface, so the application can start/stop recording), do real-time processing and visualization at the rate that the computer can keep up with, and do full-quality processing from the recorded data offline.</p>

---

## Post #7 by @PaulT95 (2022-10-20 07:58 UTC)

<p>Yes, in less than 10s I can have a full complete scan of a shank for example with a high-quality image. Mostly it depends on the computer (Alienware m51r2), as I looked for specific hardware that was also compatible with stradwin. However, my aim is to do the recording of muscle-tendon unit in controlled conditions (e.g. fixed-end contractions). The segmentation is will be post-process. But thanks for the information! Really helpful! In fact, I would like to try recording via 3D slicer to skip the problem of converting stradwin files in nifti.<br>
However, I read and quickly tried this morning IGT link and Plus server. I had no issue running Plus server and streaming to the 3D slicer the US data (artUs by Telemed). However, when I tried to connect to optitrack it didn’t work, despite it did connect for like a moment (attached the txt with the error). I saw from the web pages there is a version of Plus with optitrack and telemed configuration and to contact you for requesting this version.<br>
Can you please share it with me? That would be great! So also I can compare the performance with stradwin.</p>
<p>(Attachment Plus_Issue.txt is missing)</p>

---

## Post #8 by @PaulT95 (2022-10-20 12:30 UTC)

<p>Yes, in less than 10s I can have a full complete scan of a shank for example with a high-quality image. Mostly it depends on the computer (Alienware m51r2), as I looked for specific hardware that was also compatible with stradwin. However, my aim is to do the recording of muscle-tendon unit in controlled conditions (e.g. fixed-end contractions). The segmentation is will be post-process. But thanks for the information! Really helpful! In fact, I would like to try recording via 3D slicer to skip the problem of converting stradwin files in nifti.<br>
However, I read and quickly tried this morning IGT link and Plus server. I had no problem in streaming US data or connecting to optitrack. However I am not sure how to do the 3Dus. I saw from the web page there is a version of Plus with optitrack and telemed configuration and to contact you for requesting this version.<br>
Can you please share it with me? That would be great! So also I can compare the performance with stradwin</p>

---

## Post #9 by @lassoan (2022-10-20 14:55 UTC)

<aside class="quote no-group" data-username="PaulT95" data-post="8" data-topic="25480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pault95/48/16800_2.png" class="avatar"> PaulT95:</div>
<blockquote>
<p>in less than 10s I can have a full complete scan of a shank for example with a high-quality image.</p>
</blockquote>
</aside>
<p>That should be no problem. See this example of reconstructing vertebrae with AI segmentation and volume reconstruction, all working in real-time:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="l0BcW8c9CnI" data-video-title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" data-video-start-time="504" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI&amp;t=504" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l0BcW8c9CnI/maxresdefault.jpg" title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" width="" height="">
  </a>
</div>

<p>You can record the sequence and post-proces and reconstruct again later, but real-time 3D visualization is useful because it allows you to continuously monitor the quality of the scan.</p>
<p>There is also a simpler example here (no AI processing, just direct volume visualization, which may be suitable for images where the bone surface is well visible without any enhancement):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-video-start-time="161" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4&amp;t=161" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="PaulT95" data-post="8" data-topic="25480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pault95/48/16800_2.png" class="avatar"> PaulT95:</div>
<blockquote>
<p>I saw from the web page there is a version of Plus with optitrack and telemed configuration and to contact you for requesting this version.<br>
Can you please share it with me?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Can you help with this?</p>

---

## Post #10 by @Sunderlandkyl (2022-10-20 15:04 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="25480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="PaulT95" data-post="8" data-topic="25480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pault95/48/16800_2.png" class="avatar"> PaulT95:</div>
<blockquote>
<p>I saw from the web page there is a version of Plus with optitrack and telemed configuration and to contact you for requesting this version.<br>
Can you please share it with me?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Can you help with this?</p>
</blockquote>
</aside>
<p>The regular Plus Telemed package should have support for OptiTrack through Motive 1.10.3. If you would rather have a 64-bit version with Telemed and Motive 2.2.0, then I can get that for you.</p>

---

## Post #11 by @PaulT95 (2022-10-20 13:11 UTC)

<p>Okay thanks to both of you!!<br>
So, to calibrate and stream to 3D slicer, I have to create a configuration xml using the VirtualMixer to stream both Telemed US data and Optitrack data, correct?</p>

---

## Post #12 by @Sunderlandkyl (2022-10-20 15:14 UTC)

<p>Yes, exactly. This config file shows an example of using a VirtualMixer with Ascension and Ultrasonix: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceVirtualMixer.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Virtual Mixer</a>. You should be able to just replace the devices with the OptiTrack+Telemed.</p>
<p>Let me know if you have any questions.</p>

---

## Post #13 by @PaulT95 (2022-10-20 13:20 UTC)

<p>Okay perfect! So till now everything works fine! The main point now is all the parameters in the file like “PhantomDefinition”, "Segmentation, “Rendering”. I guess they mainly come from fCal. So do I have to perform a calibration using fCal to retrieve them?<br>
And then the data streamed by PLUS to 3Dslicer is already “2D ultrasound slices oriented in the 3D space” or the 3DSlicer is performing the operation?</p>

---

## Post #14 by @Sunderlandkyl (2022-10-20 15:33 UTC)

<p>Sorry, that config file was for fCal, this one is the same for streaming with Plus: <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml" class="inline-onebox" rel="noopener nofollow ugc">PlusLibData/PlusDeviceSet_Server_Ultrasonix_C5-2_Ascension3DG_calibrated.xml at master · PlusToolkit/PlusLibData · GitHub</a>.</p>
<p>To perform the calibration, you can use fCal, or you can use fiducial registration in 3D Slicer. See the “Tracked Ultrasound Calibration” tutorial here: <a href="https://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a>.</p>

---

## Post #15 by @lassoan (2022-10-20 16:23 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="10" data-topic="25480">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>The regular Plus Telemed package should have support for OptiTrack through Motive 1.10.3. If you would rather have a 64-bit version with Telemed and Motive 2.2.0, then I can get that for you.</p>
</blockquote>
</aside>
<p>If you have time, could you please update the <a href="https://plustoolkit.github.io/download">download page</a>? It says that 32-bit telemed+optitrack package is available on request, I guess that is just needed for the 64-bit package now.</p>

---

## Post #16 by @Sunderlandkyl (2022-10-20 16:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="25480">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you have time, could you please update the <a href="https://plustoolkit.github.io/download" rel="noopener nofollow ugc">download page</a>? It says that 32-bit telemed+optitrack package is available on request, I guess that is just needed for the 64-bit package now.</p>
</blockquote>
</aside>
<p>Sure, I’ve removed the mention to the 32-bit OptiTrack package.</p>

---
