# Rotation matrix from the Transform Module

**Topic ID**: 7103
**Date**: 2019-06-10
**URL**: https://discourse.slicer.org/t/rotation-matrix-from-the-transform-module/7103

---

## Post #1 by @Mary7291 (2019-06-10 10:40 UTC)

<p>Operating system: windows 7<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
Hello,<br>
I create a needle model to insert it to a specific region in my 3D model in slicer. This way, the position of the needle tip and the orientation of the needle is important. The desired pose of the needle is obtained by the translation and rotation part of the transform module (the needle model is defined as the transformed i.e the active transform is applied to it.)<br>
The problem is that:<br>
First: if i save the txt.file of the linear transform and load it in matlab, it can be undestood that the rotation part is not really the rotation matrix i.e the inverse and the traspose are not equal.<br>
(I convert the matrix from the LPS to RAS and the one that i load in matlab is exactly the same as seen in slicer)<br>
Second: The result is not the same as i use the invert in slicer in comparison to the inverse of the matrix from matlab.</p>
<p>I would be appreciated if anyone could help me…</p>

---

## Post #2 by @lassoan (2019-06-10 13:25 UTC)

<p>See this topic for explanation and solution: <a href="https://discourse.slicer.org/t/saving-linear-transformation-matrix/1192/7" class="inline-onebox">Saving Linear Transformation Matrix</a></p>

---

## Post #3 by @Mary7291 (2019-06-10 14:33 UTC)

<p>Thanks Mr. Lasso.<br>
Actually i saw the topic and i use it for the conversion to have the same rotation matrix in matlab. But i don’t want to use the Matlab bridge extension. I need to know which euler-angles the Slicer rotation matrix is based on?</p>

---

## Post #4 by @lassoan (2019-06-10 14:55 UTC)

<aside class="quote no-group" data-username="Mary7291" data-post="3" data-topic="7103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/48db29/48.png" class="avatar"> Mary7291:</div>
<blockquote>
<p>i don’t want to use the Matlab bridge extension</p>
</blockquote>
</aside>
<p>You don’t need to use the entire extension but just use the few lines of code that inverts axes and the matrix.</p>
<aside class="quote no-group" data-username="Mary7291" data-post="3" data-topic="7103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/48db29/48.png" class="avatar"> Mary7291:</div>
<blockquote>
<p>I need to know which euler-angles the Slicer rotation matrix is based on?</p>
</blockquote>
</aside>
<p>Euler angles are not well suited for representing arbitrary orientations (suffers from gimbal lock and there are multiple parametrizations for the same orientation). I would recommend using orientation matrix or quaternion representation.</p>

---

## Post #5 by @Mary7291 (2019-06-15 07:47 UTC)

<p>Thanks,<br>
Actually, i’m working on a robotic project and i should define the orientation of my tool.<br>
this way i want to know how the transformation module creates the rotation part based on the degrees which can be defined by the users?</p>

---

## Post #6 by @lassoan (2019-06-15 15:12 UTC)

<p>Slicer stores transformation as a <a href="https://modernrobotics.northwestern.edu/nu-gm-book-resource/3-3-1-homogeneous-transformation-matrices/" rel="nofollow noopener">4x4 homogeneous transformation matrix</a>, you can use this to compute robot joint coordinates from this matrix (<a href="http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/16311/www/current/lecture/Kinematics_final.pdf" rel="nofollow noopener">inverse kinematics</a>).</p>

---

## Post #7 by @Mary7291 (2019-06-15 15:33 UTC)

<p>Thanks,<br>
I think that i misunderstood your previous request.<br>
i found that the slicer works on Quaternions based on the Euler angles defined by users.</p>
<p>In Matlab, This could be obtained by converting the transformation matrix of slicer to the Quaternion definition and then find the Euler angles of the related Quaternion.<br>
Thanks a lot from your guidance…</p>

---

## Post #8 by @Mary7291 (2019-06-25 09:50 UTC)

<p>Hello again,</p>
<p>I came to the problem again when using the transform module.<br>
when i save the transformation matrix even the translation part is changed. why is this happen? is there any way to obtain the same translation part (position) which can be seen in slicer software?<br>
Actually i need the position of the needle tip in RAS coordinate system.</p>
<p>here is the position (red square box) which i can be seen in slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06996a403f49d0f31102f84654e97f21ea14650e.jpeg" data-download-href="/uploads/short-url/WnypyDnWiU94uPT3A368ySAEPk.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06996a403f49d0f31102f84654e97f21ea14650e_2_690x368.jpeg" alt="PNG" data-base62-sha1="WnypyDnWiU94uPT3A368ySAEPk" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06996a403f49d0f31102f84654e97f21ea14650e_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06996a403f49d0f31102f84654e97f21ea14650e_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06996a403f49d0f31102f84654e97f21ea14650e.jpeg 2x" data-dominant-color="ABA9BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1365×728 295 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and here is the piece of matlab code to convert LPS to RAS for the data which have been saved as linear transform_3. it can be obviously seen that the position is totally changed while the other arrays in rows are the columns of the transform module in slicer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9410a237ebeae23cc45389f983c80445b960cd54.png" alt="slicer%20pose%20matlab" data-base62-sha1="l7QiN55sgI1AdlIW9JiqWwcfOw4" width="509" height="472"></p>
<p>I know that i ask a lot but i need to use this module correctly. and i am so grateful from your guidance, Mr. Lasso. <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #9 by @lassoan (2019-06-25 11:43 UTC)

<p>It seems that you don’t put the matrix elements into their correct location because the orientation part is transposed. If the orientation part is incorrect then the translation is computed incorrectly, too. Probably you need to swap the row and column indices.</p>
<p>Is the needle model origin at (0,0,0)? You can verify this by creating a “Coordinate system” model using “Create models” module in SlicerIGT and apply the same transform to it. Axes of the coordinate system model should intersect at the needle tip.</p>

---

## Post #10 by @Mary7291 (2019-06-25 12:28 UTC)

<p>The transposed Matrix was from the inverse in Matlab code. So the arrays are now at the correct locations.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3da3a7f70e508d4c769f3e8ffaf784064f79bc9.png" alt="M2" data-base62-sha1="pF31dsuUHuhw4Xvf9jCz8bCR7MR" width="471" height="472"><br>
I add a coordinate system to the of the needle by applying the same transform to both of the needle and coordinate system model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b25910c152a03caf8b21609d9ea771aa8d98e5.png" data-download-href="/uploads/short-url/lmhfBFIv3zo3m5416khwrxUBKlv.png?dl=1" title="S2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95b25910c152a03caf8b21609d9ea771aa8d98e5_2_690x367.png" alt="S2" data-base62-sha1="lmhfBFIv3zo3m5416khwrxUBKlv" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95b25910c152a03caf8b21609d9ea771aa8d98e5_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95b25910c152a03caf8b21609d9ea771aa8d98e5_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95b25910c152a03caf8b21609d9ea771aa8d98e5.png 2x" data-dominant-color="A09EAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">S2</span><span class="informations">1365×727 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But the problem is still exist…Is there any translational offset between the RAS and LPS coordinate systems? I mean that multiplying the matrix from the saved file to the diagonal matrix is just because of the rotational difference between the RAS and LPS and it doesn’t have any effect on the translation values…<br>
Another surprising is that the position is changed as changing the rotation part. I mean that if i changed the orientation of the needle and entering the same position in the Matrix, the position data will be different in saved file from the previous file, even they are entered the same in slicer but with different rotation part…</p>

---

## Post #11 by @lassoan (2019-06-26 03:04 UTC)

<p>As I wrote above, there is a mistake in how the B (<em>fromParent_LPS</em>)  matrix is constructed in your example above. The correct <em>fromParent_LPS</em> matrix looks something like this:</p>
<pre><code class="lang-auto">[[  -0.65   -0.44    0.62 -107.59]
 [   0.62    0.15    0.76 -227.31]
 [  -0.43    0.89    0.18  -88.75]
 [   0.      0.      0.      1.  ]]
</code></pre>
<p>The inverse operator is responsible for computing the “to parent” transform (displayed in Slicer) from the “from parent” transform (stored in the ITK transform). Do not remove it. The first formula that you used above was correct:</p>
<p><strong><em>toParent_RAS</em> =</strong><br>
= <em>LPS_to_RAS</em> * <em>toParent_LPS</em> * <em>RAS_to_LPS</em><br>
= <em>LPS_to_RAS</em> * inv(<em>fromParent_LPS</em>) * <em>RAS_to_LPS</em><br>
<strong>= diag(-1,-1,1,1) * inv(<em>fromParent_LPS</em>) * diag(-1,-1,1,1)</strong></p>
<p>toParent_RAS =&gt; shown in Slicer<br>
fromParent_LPS =&gt; saved in ITK transform</p>

---

## Post #12 by @Mary7291 (2019-06-26 13:26 UTC)

<p>Thanks a lot Mr. Lasso.<br>
By following your suggestion, now it is work…</p>

---

## Post #13 by @Zul_Abdullah (2022-06-28 09:29 UTC)

<p>Hi Mr Lassoan,<br>
Refering to Unity Code (OpenIGTLinkConnect.cs) taken from this Github (<a href="https://github.com/franklinwk/OpenIGTLink-Unity/tree/master/OpenIGTLink-Unity/Assets/Scripts" class="inline-onebox" rel="noopener nofollow ugc">OpenIGTLink-Unity/OpenIGTLink-Unity/Assets/Scripts at master · franklinwk/OpenIGTLink-Unity · GitHub</a>)</p>
<p>This is the Unity .cs code</p>
<p>// ##### #################################################<br>
Matrix4x4 matrix = new Matrix4x4();<br>
matrix.SetRow(0, new Vector4(m[0], m[3], m[6], m[9] / scaleMultiplier));<br>
matrix.SetRow(1, new Vector4(m[1], m[4], m[7], m[10] / scaleMultiplier));<br>
matrix.SetRow(2, new Vector4(m[2], m[5], m[8], m[11] / scaleMultiplier));<br>
matrix.SetRow(3, new Vector4(0.0f, 0.0f, 0.0f, 1.0f));</p>
<p>Matrix4x4 IJKToRAS = new Matrix4x4();<br>
IJKToRAS.SetRow(0, new Vector4(-1.0f, 0, 0, 0));<br>
IJKToRAS.SetRow(1, new Vector4(0, -1.0f, 0, 2));<br>
IJKToRAS.SetRow(2, new Vector4(0, 0, 1.0f, 0));<br>
IJKToRAS.SetRow(3, new Vector4(0.0f, 0.0f, 0.0f, 1.0f));</p>
<p>Matrix4x4 matrixRAS = matrix * IJKToRAS;</p>
<p>// ##### #################################################</p>
<p>comparing to the steps that you described above<br>
<strong><em>toParent_RAS</em> =</strong><br>
= <em>LPS_to_RAS</em> * <em>toParent_LPS</em> * <em>RAS_to_LPS</em><br>
= <em>LPS_to_RAS</em> * inv(<em>fromParent_LPS</em> ) * <em>RAS_to_LPS</em><br>
<strong>= diag(-1,-1,1,1) * inv(<em>fromParent_LPS</em>) * diag(-1,-1,1,1)</strong></p>
<p>It looks like the steps for conversion is not complete there.<br>
I am getting different values in Unity, compare to the value from NDI Track App.</p>
<p>And, the value I am getting from NDI Track App is the same for Slicer and Unity.<br>
Does it mean that I need to set the Needle origin in Slicer or can I set this in PLUS server setting? so that I get same values for Needle coordinates in NDI Track, Slicer and Unity?</p>
<p>FYI - The reference coordinate is correct and similar for all three - NDI Track, Slicer and Unity (if I am using the matrix and not the IJKToRAS)<br>
if I am multiplying them with IJKToRAS - none of the values are the same in all 3 Apps.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c27a30a199bc95135358b2deb9225d00acffc2ed.jpeg" data-download-href="/uploads/short-url/rKqq2IqpZWX5V2Ok13D4NO0O9qd.jpeg?dl=1" title="Reference_OK" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c27a30a199bc95135358b2deb9225d00acffc2ed_2_690x119.jpeg" alt="Reference_OK" data-base62-sha1="rKqq2IqpZWX5V2Ok13D4NO0O9qd" width="690" height="119" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c27a30a199bc95135358b2deb9225d00acffc2ed_2_690x119.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c27a30a199bc95135358b2deb9225d00acffc2ed_2_1035x178.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c27a30a199bc95135358b2deb9225d00acffc2ed.jpeg 2x" data-dominant-color="A5A8AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Reference_OK</span><span class="informations">1321×228 59.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #14 by @Zul_Abdullah (2022-06-28 11:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94f4195e23a30576f06e8e25c3024cef6abdc715.png" data-download-href="/uploads/short-url/lfHE1nDt7SQuv4y2MAJAbOlxoNf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94f4195e23a30576f06e8e25c3024cef6abdc715.png" alt="image" data-base62-sha1="lfHE1nDt7SQuv4y2MAJAbOlxoNf" width="690" height="376" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">717×391 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After StylusTip calibration in Slicer following this tutorials (<a href="https://andysbrainbook.readthedocs.io/en/latest/Slicer/Slicer_Short_Course/Slicer_05_Calibration.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer Tutorial #5: Receiving the Connection and Calibrating the Stylus — Andy's Brain Book 1.0 documentation</a> &amp; <a href="https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3128&amp;ithint=file%2cpptx&amp;authkey=!AMy-wgNHStEKsPU" rel="noopener nofollow ugc">https://onedrive.live.com/view.aspx?resid=7230D4DEC6058018!3128&amp;ithint=file%2Cpptx&amp;authkey=!AMy-wgNHStEKsPU</a> ) - I got this <em>scene</em>.mrml file that contains the matric for the StylusTip, and I need to apply them as a <strong>CoordinateDefinitions</strong> in PLUS Server.</p>
<p>What does the StylusTip matric value means and which represent the x,y,z, offset that I need to use in PLUS server?</p>
<p>Thanks.</p>

---

## Post #15 by @lassoan (2022-06-29 03:08 UTC)

<aside class="quote no-group" data-username="Zul_Abdullah" data-post="13" data-topic="7103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zul_abdullah/48/15815_2.png" class="avatar"> Zul_Abdullah:</div>
<blockquote>
<p>It looks like the steps for conversion is not complete there.</p>
</blockquote>
</aside>
<p>I cannot comment or investigate why the conversion was done like that in <code>OpenIGTLinkConnect.cs</code>. If you don’t think it is correct then feel free to modify it as you see fit and then you may consider submitting a pull request to that repository, but I’m not sure if that project is still active.</p>
<aside class="quote no-group" data-username="Zul_Abdullah" data-post="13" data-topic="7103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zul_abdullah/48/15815_2.png" class="avatar"> Zul_Abdullah:</div>
<blockquote>
<p>Does it mean that I need to set the Needle origin in Slicer or can I set this in PLUS server setting?</p>
</blockquote>
</aside>
<p>You cannot “set the Needle origin”. You specify coordinate systems (see <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationfCalCoordinateSystemDefinitions.html">coordinate systems specifications that we use in all Plus and SlicerIGT projects</a>), such as <code>Needle</code> and <code>NeedleTip</code> and then compute transform between them using various calibration tools. You can accept and use these conventions, but you are free to establish different conventions - they will work, too, as long as you are using them consistently.</p>
<aside class="quote no-group" data-username="Zul_Abdullah" data-post="13" data-topic="7103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zul_abdullah/48/15815_2.png" class="avatar"> Zul_Abdullah:</div>
<blockquote>
<p>if I am multiplying them with IJKToRAS - none of the values are the same in all 3 Apps.</p>
</blockquote>
</aside>
<p>IJKToRAS is for converting voxel (IJK) coordinates to anatomical (RAS) coordinates of an image volume. We don’t talk about images here at all. We do not have coordinates in IJK coordinate system here, so you cannot use the IJKToRAS matrix for anything that is discussed in this topic.</p>
<aside class="quote no-group" data-username="Zul_Abdullah" data-post="14" data-topic="7103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zul_abdullah/48/15815_2.png" class="avatar"> Zul_Abdullah:</div>
<blockquote>
<p>I got this <em>scene</em>.mrml file that contains the matric for the StylusTip, and I need to apply them as a <strong>CoordinateDefinitions</strong> in PLUS Server.</p>
</blockquote>
</aside>
<p>If you store a NeedleTip to Needle transform in the Plus configuration file (e.g., by performing pivot calibration in fCal; or performing pivot calibration in Slicer and then sending or copying the transform to Plus) then you can send the NeedleTipToReference transform to Slicer.</p>
<p>If you just store NeedleTip to Needle transform in the Slicer scene then you can use it by assembling a correct transform hierarchy.</p>

---

## Post #16 by @Zul_Abdullah (2022-07-01 09:04 UTC)

<p>Hi Mr Lassoan,</p>
<p>Thanks for the reply.<br>
It is a great help in getting us a useful result. Thank you.</p>
<p>Previously -<br>
a) Only Reference value for NDI, Slicer and Unity is the same<br>
b) All other sensors for both Slicer and Unity which share the same value contradicts with NDI.</p>
<p>The reason behind this is due to - PLUS setting that does not use Reference.<br>
So, with this new PLUS setting, all sensors refer back to Reference, and got all its value corrected to match the NDI.</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;

  &lt;DataCollection StartupDelaySec="1.0"&gt;
    &lt;DeviceSet 
      Name="NDI_to_Unity_PLUS"
      Description=""
    /&gt;
    &lt;Device
      Id="TrackerDevice" 
      Type="AuroraTracker"
      SerialPort="6"
      ToolReferenceFrame="Tracker" &gt;
     &lt;DataSources&gt;
        &lt;DataSource Type="Tool" Id="Probe" PortName="0" /&gt;
        &lt;DataSource Type="Tool" Id="Reference" PortName="1" /&gt;
        &lt;DataSource Type="Tool" Id="StylusSensor" PortName="2" /&gt;
       
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="TrackerStream"&gt;
          &lt;DataSource Id="Probe" /&gt;
          &lt;DataSource Id="Reference" /&gt;
          &lt;DataSource Id="StylusSensor" /&gt;
        &lt;/OutputChannel&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
	    
		&lt;Device
      Id="CaptureDevice"
      Type="VirtualCapture"
      BaseFilename="RecordingTest.igs.mha"
      EnableCapturingOnStart="FALSE" &gt;
      &lt;InputChannels&gt;
        &lt;InputChannel Id="TrackerStream" /&gt;
      &lt;/InputChannels&gt;
    &lt;/Device&gt;
	
  &lt;/DataCollection&gt;

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
        &lt;Transform Name="ProbeToReference" /&gt;
        &lt;Transform Name="ProbeToTrackerTransform" /&gt;
        &lt;Transform Name="ReferenceToTrackerTransform" /&gt;
        &lt;Transform Name="StylusToTrackerTransform" /&gt;
        &lt;/TransformNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
  
 &lt;CoordinateDefinitions&gt;
    &lt;Transform From="Stylus" To="StylusSensor"
      Matrix="
        1 0 0 0
        0 1  0  0
        0 0 1 0
        0 0 0 1"
       Error="0.554951" Date="012617_105449" /&gt;
  &lt;/CoordinateDefinitions&gt;
	
&lt;/PlusConfiguration&gt;
</code></pre>

---

## Post #17 by @Zul_Abdullah (2022-07-01 09:06 UTC)

<pre><code class="lang-auto">&lt;CoordinateDefinitions&gt;
    &lt;Transform From="Stylus" To="StylusSensor"
      Matrix="
        1 0 0 0
        0 1  0  0
        0 0 1 0
        0 0 0 1"
       Error="0.554951" Date="012617_105449" /&gt;
  &lt;/CoordinateDefinitions&gt;
</code></pre>
<p>This coordinate setting does nothing becauase after trying a few values - it does not offset the needle, so we leave it at Vector.Identity (no change)</p>
<p>However, the Needle tip does not require any offset in Unity. although we first thought that this could be around 8.8cm back from the tip.</p>

---
