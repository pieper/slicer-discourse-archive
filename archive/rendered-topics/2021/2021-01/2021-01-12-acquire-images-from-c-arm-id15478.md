---
topic_id: 15478
title: "Acquire Images From C Arm"
date: 2021-01-12
url: https://discourse.slicer.org/t/15478
---

# Acquire images from C-arm

**Topic ID**: 15478
**Date**: 2021-01-12
**URL**: https://discourse.slicer.org/t/acquire-images-from-c-arm/15478

---

## Post #1 by @drvarunagarwal (2021-01-12 18:24 UTC)

<p>Thanks a lot</p>
<p>For guidance always</p>
<p>Also can u please tell me one more query.</p>
<p>Can I get a C arm output directly into slicer everytime I take a shot so I can clear up image on the fly?</p>
<p>The c arm gives output via video out either BNC or s-video.</p>
<p>Please advise</p>
<p>Many thanks</p>
<p>Best Regards,<br>
Dr. Varun Agarwal</p>

---

## Post #2 by @lassoan (2021-01-12 18:42 UTC)

<p>You can connect Slicer to a C-arm in several ways.</p>
<ol>
<li>Capture video output</li>
</ol>
<p>You can connect a framegrabber to your computer and capture images from the C-arm’s video output. Analog output, such as S-video will be somewhat noisy and it may be lower resolution than the native resolution of the fluoro.</p>
<p>You don’t have direct access to the C-arm’s pose, so you either need to attach an <a href="http://perk.cs.queensu.ca/sites/perk.cs.queensu.ca/files/Wolff2013b.pdf">accelerometer</a> or have a special marker object (such as <a href="https://jhu.pure.elsevier.com/en/publications/ftrac-a-robust-fluoroscope-tracking-fiducial-3">FTRAC</a>) in the field of view. For us, accelerometers (in IMU/MARG sensors) were more accurate and much easier to work with overall, the only disadvantage is that they only provide orientation, and not position. You can also use optical trackers, surface scanners, etc. to get relative pose between C-arm and patient. Running OCR on the acquired image may work, too, but it is very specific to the C-arm software and may be quite fragile.</p>
<p>You can connect to various types of framegrabbers, accelerometers, optical trackers, surface scanners using Plus toolkit, which can send the data in real-time to Slicer.</p>
<ol start="2">
<li>Automated DICOM push</li>
</ol>
<p>You can set up your C-arm to automatically push acquired image sequences or snapshot to a DICOM C-store storage server. If you enable DICOM C-store SCP in Slicer and set it as destination server for auto-push in your C-arm then Slicer receives all acquired images within a few seconds and it shows up in the DICOM database from where you can load it into the scene.</p>
<p>The advantage is that you can get much higher image quality than via analog video and metadata in the DICOM header, such as the C-arm angle, SID, SOD, etc.</p>

---

## Post #3 by @drvarunagarwal (2021-01-12 18:51 UTC)

<p>Why would I need an accelerometer for pose on the c arm for the analog solution u described?</p>
<p>I am not clear on that part.</p>
<p>Please clarify many thanks</p>
<p>Best Regards,<br>
Dr. Varun Agarwal</p>

---

## Post #4 by @lassoan (2021-01-12 18:55 UTC)

<p>There are many reasons why you would want to know the C-arm pose, such as showing surgical plan in the same orientation as the fluoro view, maybe even overlaying the plan over the fluoro, helping users to align the C-arm with the planned tool trajectory, do cone-beam volume reconstruction, etc. If you get the image via analog video output then you don’t get the angle information.</p>

---

## Post #5 by @drvarunagarwal (2021-01-13 03:47 UTC)

<p>I see that</p>
<p>But there is an inherent bias and error in MARG sensor.<br>
Would it be a suitable solution for tasks you describe?</p>

---

## Post #6 by @lassoan (2021-01-13 03:57 UTC)

<p>According to our <a href="http://perk.cs.queensu.ca/sites/perk.cs.queensu.ca/files/Wolff2013b.pdf">experiments on a mobile C-arm</a>, you can get better accuracy with a MARG sensor than with built-in sensors. However, getting accurate C-arm angles is not enough, because you also need to perform camera calibration, distortion correction (if an image intensifier is used and not a flat panel detector), deal with bending (sagging) and of the C-arm, etc.</p>
<p>Displaying a surgical plan in the same orientation as the current C-arm orientation does not require high accuracy, so that is very easily doable.</p>
<p>However, doing something like patient/tool registration form a few views with 1-2mm accuracy is more challenging, and cone-beam volume reconstruction with submillimeter accuracy on a mobile C-arm would be an extremely difficult task.</p>

---

## Post #7 by @drvarunagarwal (2021-01-14 17:08 UTC)

<p>If we want to track C arm position so that after moving it away from the surgical scene the technician can easily bring it back to same spot. We would have to use an optical tracking system. Simple MARG sensor would be insufficient.</p>
<p>Also for this purpose would we have to put a tracker on the patient?</p>
<p>If we don’t want to put a tracker on the patient then would we have to fix the position of the camera?</p>
<p>Please advise.</p>
<p>Thanks</p>
<p>Best Regards,<br>
Dr. Varun Agarwal</p>

---

## Post #8 by @lassoan (2021-01-14 19:49 UTC)

<aside class="quote no-group" data-username="drvarunagarwal" data-post="7" data-topic="15478">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"> drvarunagarwal:</div>
<blockquote>
<p>We would have to use an optical tracking system</p>
</blockquote>
</aside>
<p>Optical trackers are somewhat impractical to use with C-arms, as the detector/image intensifier where you can place the marker on is about 60-80 cam away from the isocenter. It is just hard to position the tracking camera to have tool, patient, and C-arm markers in the field of view, without occlusion. With a single-camera tracker, such as NDI Polaris, it was quite a struggle, even in phantom experiments. It is also not generally feasible to track the X-ray generator, so you may still need to do sophisticated modeling of the C-arm to compensate for bending of the C-arm.</p>
<p>If you want to do optical tracking then probably you need a multi-camera setup (e.g., 4 Optitrack Prime cameras) to cover the large field and be quite robust against occlusions.</p>
<p>In selected applications, attaching tracker camera or surface scanner to the C-arm may work, too.</p>
<p>What clinical application do you have in mind? Pedicle screw insertion?</p>

---

## Post #9 by @drvarunagarwal (2021-01-14 23:53 UTC)

<p>Please see the attached link</p>
<p><a href="https://youtu.be/gCUYk5VZ1DI" rel="noopener nofollow ugc">https://youtu.be/gCUYk5VZ1DI</a></p>
<p>This is what I meant by c arm tracking.<br>
To easily reposition the c arm rather than tool tracking.</p>
<p>For tool tracking patient reference frame is must.<br>
For the kind of c arm tracking shown in video is patient tracker required?<br>
Also can this be solely achieved with MARG sensors?</p>
<p>Best Regards,<br>
Dr. Varun Agarwal</p>

---

## Post #10 by @lassoan (2021-01-15 04:05 UTC)

<aside class="quote no-group" data-username="drvarunagarwal" data-post="9" data-topic="15478">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"> drvarunagarwal:</div>
<blockquote>
<p>This is what I meant by c arm tracking.<br>
To easily reposition the c arm rather than tool tracking.</p>
</blockquote>
</aside>
<p>This feature has been implemented several times by various research groups and small companies over the last 1-2 decades. It is somewhat useful but it does not justify all the inconveniences of adding a tracker. It is also interesting to note that it is trivial to implement this feature for floor/ceiling-mounted C-arms (which already have encoders in the C-arm and patient table), this feature is not commonly used in these systems either.</p>
<p>If you already track the C-arm for some reason (for example, you track the patient and tools) and you can manage to keep the C-arm in the field of view then it may make sense to use it for helping with the positioning. You can also replace the clumsy high-accuracy optical tracker with inside-out tracking (MARG sensor for angle; camera or surface scanner looking at the patient and/or the ceiling for translation tracking) However, since positioning is still done using manually (most mobile C-arms are not motorized), it is not a huge improvement overall.</p>
<p>I keep hearing from companies the importance of dose reduction, but it is rarely a concern for patients and physicians I talked to are generally not concerned by the radiation. They often seem to accept higher exposure if it allows them to save time or make things more convenient.</p>

---

## Post #11 by @drvarunagarwal (2021-01-15 07:26 UTC)

<p>camera or surface scanner looking at the patient and/or the ceiling for translation tracking)</p>
<p>By the above u mean the same optical tracking camera? Or some other (like machine vision kinds) camera? Hope u can share some example or paper.</p>
<p>Many thanks</p>
<p>Best Regards,<br>
Dr. Varun Agarwal</p>

---

## Post #13 by @lassoan (2023-07-04 15:51 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-acquire-x-ray-images-from-c-arm/30393">How to acquire X-ray images from C-arm?</a></p>

---
