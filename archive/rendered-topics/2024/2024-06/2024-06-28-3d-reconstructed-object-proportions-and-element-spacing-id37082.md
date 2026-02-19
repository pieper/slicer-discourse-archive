---
topic_id: 37082
title: "3D Reconstructed Object Proportions And Element Spacing"
date: 2024-06-28
url: https://discourse.slicer.org/t/37082
---

# 3D Reconstructed Object Proportions and Element Spacing

**Topic ID**: 37082
**Date**: 2024-06-28
**URL**: https://discourse.slicer.org/t/3d-reconstructed-object-proportions-and-element-spacing/37082

---

## Post #1 by @Viktor_Sokolov (2024-06-28 10:19 UTC)

<p>Hello everybody! I have encountered a problem with volume proportions after 3D reconstruction. I acquire images via a Telemed US Probe and track positions using a robot arm. I scan a handmade phantom with a small 3D printed pyramid inside. The element spacing of Telemed US Probe is (0.2, 0.2, 0.2). When I load .mhd file into 3D Slicer with ElementSpacing = 0.2 0.2 0.2, I get very strange result of 3D reconstruction.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bdf886c0b6905f3ab888618635399ba7fdb0e3a.jpeg" data-download-href="/uploads/short-url/foi0osRLFEKRtpA4FNdmF0sTJtU.jpeg?dl=1" title="problem_with_3d_rec" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bdf886c0b6905f3ab888618635399ba7fdb0e3a.jpeg" alt="problem_with_3d_rec" data-base62-sha1="foi0osRLFEKRtpA4FNdmF0sTJtU" width="640" height="500" data-dominant-color="8F8FC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem_with_3d_rec</span><span class="informations">642×501 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I load the same.mhd file and change ElementSpacing to 1 1 1, the 3D reconstruction works, but I get a very squeezed pyramid.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2621cf841b18c7ae56dd8cb4af166b64f0d7c9.jpeg" data-download-href="/uploads/short-url/m8vHJYrAs8UmJDxxeBb8K8Zgwit.jpeg?dl=1" title="squeezed_3d_rec" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2621cf841b18c7ae56dd8cb4af166b64f0d7c9_2_690x436.jpeg" alt="squeezed_3d_rec" data-base62-sha1="m8vHJYrAs8UmJDxxeBb8K8Zgwit" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2621cf841b18c7ae56dd8cb4af166b64f0d7c9_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2621cf841b18c7ae56dd8cb4af166b64f0d7c9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2621cf841b18c7ae56dd8cb4af166b64f0d7c9.jpeg 2x" data-dominant-color="9E9AC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">squeezed_3d_rec</span><span class="informations">834×528 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
3D Reconstruction module also has similiar parameter called output spacing, but changing it doesn’t solve the problem.<br>
P.S. My US probe is uncalibrated, but I hope at least to get the correct proportions without calibration.</p>

---

## Post #2 by @ungi (2024-06-29 14:49 UTC)

<p>Hi, it’s difficult to comment without seeing your complete transform hierarchy. Image sequences in Slicer are usually stored without any transformation or spacing, so the units are pixels. Ultrasound tracking calibration in your case would be something like Image-to-RobotEnd. This trasnform will have a scaling of 0.2, converting from pixels to mm. It would also position and rotate the image relative to the most distal part (RobotEnd) of the robot.</p>

---

## Post #3 by @Viktor_Sokolov (2024-07-04 12:17 UTC)

<p>Thank you for response, I still has not been able to solve the problem.  My TELEMED probe aquries images with 0.2 spacing. I have tried to do 3D reconstruction in two ways, with different Element Spacings.</p>
<ol>
<li>
<p>I load .mhd sequence file with the Element Spacing = 0.2 0.2 0.2 into 3D Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9afa6829e27d391a892fd6d67d33f20af25c6e4e.jpeg" alt="spacing02" data-base62-sha1="m701x4ZwYwWiJgwrJT8Y9tKjZim" width="405" height="32"><br>
I get the following 2d view  where the US frame fills only a small part of the window:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85e234d43e5f7c6bee12cef86e321469e94a70c6.jpeg" alt="0_2_2D_view" data-base62-sha1="j6o9cId0dsrIrOquJbvLO5Ctgb4" width="676" height="444"><br>
The region of interest has <strong>correct proprotions</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ea0ec44879caa60996fbca1c5f18f6e567ec841.jpeg" alt="ROI_correct" data-base62-sha1="4mX6bWqlEnZ1i9jemPNpjgz367v" width="554" height="452"><br>
But after running 3D reconstruction, the volume isn’t rendered properly for some reason:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17180a6f381714220c11744f384bbd5dca9ac51f.jpeg" alt="wrong_3d_rec" data-base62-sha1="3iiujmYK37sJCGc9XCIo0BIlNRd" width="553" height="447"></p>
</li>
<li>
<p>When I load .mhd file with Element Spacing = 1 1 1:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8139dc085986bdceff8fd55528713a9bb593f95f.jpeg" alt="spacing1" data-base62-sha1="irbyxuyzd25vGPQ4U9zIYAsdvFt" width="318" height="29"><br>
The US frame fills up all the space of the 2D Red window.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8707d3585d772116b346e7f03002ca13c878a6fe.jpeg" alt="1_2D_view" data-base62-sha1="jgxdVMSeQNNE2kpLJQff0N8Eb4W" width="674" height="443"><br>
But the region of interest is squeezed and 3D reconstruction works (see the result in my first post), however; the volume has <strong>incorrect proprotions</strong>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bae7d4455e8224d57418efa92f97e4a81744d02d.jpeg" data-download-href="/uploads/short-url/qFrv4L9uJwWnSDfdiMFoFbCIrg1.jpeg?dl=1" title="ROI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bae7d4455e8224d57418efa92f97e4a81744d02d_2_690x431.jpeg" alt="ROI" data-base62-sha1="qFrv4L9uJwWnSDfdiMFoFbCIrg1" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bae7d4455e8224d57418efa92f97e4a81744d02d_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bae7d4455e8224d57418efa92f97e4a81744d02d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bae7d4455e8224d57418efa92f97e4a81744d02d.jpeg 2x" data-dominant-color="776A87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ROI</span><span class="informations">837×523 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>My transforamtion hierarchy looks like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8ca221e51f8c5a49cf94ddd2974c4bb5de5740f.jpeg" alt="Transform_Hierarchy" data-base62-sha1="uVOcx6Nom8RKZ57WXLWQ6q7l83J" width="564" height="124"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f1b867929f81a227198d75c4e6e63bf649570a.jpeg" alt="Transform" data-base62-sha1="uwDAfiwpxxfkcuKptD7VPjfri3g" width="565" height="220"></p>

---

## Post #4 by @ungi (2024-07-04 12:37 UTC)

<p>Could you please check if ImageToReference is changing over time when you move the sequence browser time slider, and if the values of the ImageToReference matrix make sense? You can see the matrix in the Transforms module if you select ImageToReference. The first three columns should have a norm of 0.2, and they should be orthogonal. Also check that Image does not have any extra transform in it. You can check that if you go to Volumes module and select Image (h_l_man_pyr-Image), and expand the section called “Volume Information”. The third value of dimensions should be 1, spacing should be 1 everywhere, origin should be (0,0,0), and the IJK to RAS matrix should be the identity.</p>
<p>If you check all these and they all look correct, then something might be wrong with the recorded data or the ImageToProbe calibration (should be part of ImageToReference). If you are recording data with PLUS, could you attach or copy the contents of your PLUS config file here?</p>

---

## Post #5 by @Viktor_Sokolov (2024-07-09 08:16 UTC)

<p>I checked all the points you mentioned; everything seems to be fine. I think the problem is with maths, as I generate the transformations manually in my Python code instead of obtaining them from PLUS. You mentioned that the first three columns of the transformation matrix should have a norm of 0.2. Have I understood correctly that the transformation matrix should look like in the equation below?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bf9448eee95e1952bfd26a9f691721111a50734.png" alt="65e94de4fa1683747a2dc0eb066b7974" data-base62-sha1="fpb8SgugaZ0cFdtzpP5nZYpgKhe" width="430" height="229"><br>
And the content of my PLUS config:</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;
&lt;DataCollection StartupDelaySec="1.0"&gt;
&lt;DeviceSet Name="PlusServer: Telemed ultrasound device (CUSTOM)" Description="Broadcasting acquired video through OpenIGTLink"/&gt;
&lt;!-- SELF-CLOSING TAG, THIS IS WHAT USER SEE IN PlusLucher from drop-down menu --&gt;
&lt;Device Id="VideoDevice" Type="TelemedVideo"&gt;
&lt;!--   AcquisitionRate="15" FrameSize="1920 1080" VideoFormat="YUY2" CaptureDeviceId="0" --&gt;
&lt;DataSources&gt;
&lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="UN"/&gt;
&lt;!-- &lt;DataSource Type="Video" Id="Video" PortUsImageOrientation="US_IMG_ORIENT_MF" ImageType="BRIGHTNESS"/&gt;  --&gt;
&lt;!-- ImageType="RGB_COLOR"  --&gt;
&lt;/DataSources&gt;
&lt;OutputChannels&gt;
&lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video"/&gt;
&lt;/OutputChannels&gt;
&lt;/Device&gt;
&lt;Device Id="CaptureDevice" Type="VirtualCapture" BaseFilename="RecordingTest.igs.mha" EnableCapturingOnStart="FALSE"&gt;
&lt;InputChannels&gt;
&lt;InputChannel Id="VideoStream"/&gt;
&lt;/InputChannels&gt;
&lt;/Device&gt;
&lt;/DataCollection&gt;
&lt;CoordinateDefinitions&gt;
&lt;Transform From="Image" To="Reference" Matrix=" 0.5 0 0 0 0 0.5 0 0 0 0 0.5 0 0 0 0 1"/&gt;
&lt;/CoordinateDefinitions&gt;
&lt;PlusOpenIGTLinkServer MaxNumberOfIgtlMessagesToSend="1" MaxTimeSpentWithProcessingMs="50" ListeningPort="18944" SendValidTransformsOnly="true" OutputChannelId="VideoStream"&gt;
&lt;DefaultClientInfo&gt;
&lt;MessageTypes&gt;
&lt;Message Type="IMAGE"/&gt;
&lt;/MessageTypes&gt;
&lt;ImageNames&gt;
&lt;Image Name="Image" EmbeddedTransformToFrame="Reference"/&gt;
&lt;/ImageNames&gt;
&lt;/DefaultClientInfo&gt;
&lt;/PlusOpenIGTLinkServer&gt;
&lt;/PlusConfiguration&gt;
</code></pre>

---

## Post #6 by @ungi (2024-07-18 14:10 UTC)

<p>In the PLUS config file, we never define ImageToReference. Image is rigidly linked to an ultrasound probe. But Reference is typically fixed to the patient. ImageToReference represents the motion of the image relative to the patient. It is always changing, so you cannot create a constant for it in the config file. That section is for constant transforms like ImageToProbe (because the ultrasound image is not moving relative to the ultrasound probe).</p>
<p>You say that you generate transforms in your Python code, you are not getting it from PLUS. I’m not sure I understand how is that possible. But in that case you just send the Image from PLUS without any transforms. Does your Python code obtains the tracking transforms directly from a tracker?</p>

---

## Post #7 by @Viktor_Sokolov (2024-07-19 15:55 UTC)

<p>The PLUS config file that I use is from an official example on the website; for some reason, it does have an ImageToReference transform. However, as you said, it shouldn’t affect me in any way since I use only raw frames from the PLUS app and positions I receive from the joint encoders of my robot. After that, I generate transform matrices in Python code and embed them into the .mhd sequence file header. In my particular experiment where I scan in a linear manner, I assume the rotation matrix to be identity and change only the translation vector. If I understood you correctly, for preserving proportions, I should use an identity matrix multiplied by the element spacing - 0.2?</p>

---

## Post #8 by @ungi (2024-07-20 21:29 UTC)

<p>That ImageToReference was for convnience of display for a different image type. Honestly, it shouldn’t have been there in the first place, or at least named something else. You need to remove it, and send the Image in the Image coordinate system, because sending an ImageToReference in the Slicer scene will conflict with a tracking method. You can just send the Image in the Image coordinate system from PLUS. Untransformed.<br>
I’m still not sure how you will get the tracking data for each frame.</p>

---

## Post #9 by @Viktor_Sokolov (2024-07-22 08:48 UTC)

<p><a href="https://discourse.slicer.org/u/ungi">ungi</a><a href="https://discourse.slicer.org/u/ungi">Tamas Ungi</a> thank you for the help! I multiplied rotation matrix by element spacing and managed to get the correct proportions.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8734ff2fc8336c1dda1ec17d0919d27648730fbb.jpeg" alt="1" data-base62-sha1="ji60e91vKRoaS8fv3dgR3gbHPKP" width="443" height="392"></p>
<blockquote>
<p>I’m still not sure how you will get the tracking data for each frame</p>
</blockquote>
<p>I just insert in my Python code the z-coordinates of my robot’s end-effector, obtained from joint encoders and inverse kinematics, into the translation vector of the 4x4 transformation matrix.</p>

---

## Post #10 by @lassoan (2024-07-22 22:04 UTC)

<p><code>ElementSpacing</code>, <code>Offset</code>, <code>TransformMatrix</code> are not used in sequence files, as they cannot vary for each frame.</p>
<p>You need to come up with a list of coordinate systems for your system, such as <code>RobotBase</code>, <code>RobotEndEffector</code>, <code>Probe</code>, <code>Image</code>, and <code>Reference</code>. Then make sure the <code>ImageToReference</code> transform is defined for each time point. The <code>ImageToReference</code> is defined if there is a chain of transforms between the <code>Image</code> and <code>Reference</code> coordinate systems. You can achieve this by specifying the following transforms:</p>
<ul>
<li>If you want to use <code>RobotBase</code> coordinate system as your <code>Reference</code> coordinate system then you can put an identity<br>
<code>&lt;Transform From="RobotBase" To="Reference" Matrix="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/&gt;</code> transform into <code>CoordinateDefinitions</code>. If the robot base is mounted to the patient bed then you may want to specify orientation that is aligned with patient anatomical axis directions. You may set this transform using landmark registration after the patient is positioned (e.g., by touching anatomical landmarks on the patient).</li>
<li>The probe calibration matrix, which tells the image pixel spacing and position and orientation of the image relative to a coordinate system that you define on the ultrasound probe goes into <code>CoordinateDefinitions</code>, too.</li>
<li><code>RobotEndEffector</code> to <code>Probe</code> transform describes how the robot end effector grabs the ultrasound imaging probe (and you need to recompute each time you reposition the probe in the end effector). It goes into <code>CoordinateDefinitions</code>.</li>
<li>You compute <code>RobotBase</code> to <code>RobotEndEffector</code> from your robot kinematics model and joint encoders. It goes into the <code>Seq_FrameNNNN_RobotEndEffectorToRobotBaseTransform</code> fields in the sequence file header.</li>
</ul>

---
