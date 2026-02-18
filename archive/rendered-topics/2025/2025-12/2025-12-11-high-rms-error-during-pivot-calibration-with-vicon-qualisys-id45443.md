# High RMS error during pivot calibration with Vicon/Qualisys

**Topic ID**: 45443
**Date**: 2025-12-11
**URL**: https://discourse.slicer.org/t/high-rms-error-during-pivot-calibration-with-vicon-qualisys/45443

---

## Post #1 by @AurelieS (2025-12-11 12:37 UTC)

<p>Dear Slicer team,</p>
<p>We succeeded in integrating live Qualisys and VICON data into Slicer using IGT (I will go back to you for this code and integration).</p>
<p>However during the pivot calibration of the stylus using the Qualisys system (we have no issue using VICON data), we obtain a very high RMS error (about 33 in mean, we can go down to 8-9 at the minimum).</p>
<p>It is the first time that we have such data, we used Slicer and pivot with Vicon, Optitrack, NDI and the RMS was always less than 1.</p>
<p>What could explain such value ?</p>
<p>Thanks in advance,</p>
<p>Best regards,</p>
<p>Aurélie Sarcher</p>

---

## Post #2 by @cpinter (2025-12-11 12:43 UTC)

<p>What do you see when moving the stylus (or needle or whatever you want to pivot-calibrate) without the calibration? Is the motion smooth, or are there jumps? How does the motion look like during pivot calibration?</p>

---

## Post #3 by @AurelieS (2025-12-11 12:56 UTC)

<p>Thank you for your quick answer.</p>
<p>The movement is very smooth and we made sure that we tracked with 100% quality the rigidbody on top of the stylus.</p>
<p>We are proof testing the Qualisys code and I wonder if this is not a pb of construction of the coordinate matrix that I sent into 3D Slicer.</p>
<p>For now I do that in my Qualisys code :</p>
<p><code>rotationMatrix = np.array([</code><br>
<code>[rotation.matrix[0], rotation.matrix[1], rotation.matrix[2], position.x],</code><br>
<code>[rotation.matrix[3], rotation.matrix[4], rotation.matrix[5], position.y],</code><br>
<code>[rotation.matrix[6], rotation.matrix[7], rotation.matrix[8], position.z],</code><br>
<code>[0, 0, 0, 1]</code><br>
<code>], dtype=float)</code></p>
<p>But I think I need to check the data and be sure that QTM does not send data in columns :</p>
<p><code>R = rotation.matrix</code><br>
<code>rotationMatrix = np.array([</code><br>
<code>[R[0], R[3], R[6], position.x],</code><br>
<code>[R[1], R[4], R[7], position.y],</code><br>
<code>[R[2], R[5], R[8], position.z],</code><br>
<code>[0,    0,    0,    1],</code><br>
<code>])</code></p>
<p>or even maybe transposed.</p>
<p>I just wanted to be sure that this pb could not come from anything else ?</p>
<p>Best regards,</p>
<p>Aurélie</p>

---

## Post #4 by @cpinter (2025-12-11 13:05 UTC)

<p>Interesting, so you are constructing the pose matrix yourself? Do you have a new PLUS device for aquiring the data? Or how do you do the acquisition?</p>
<p>Based on what you write, the positions seem fine, because the motion seems smooth. If you’re not sure how to construct the rotation matrix, maybe assume certain poses with the stylus and verify what the 9 elements in the rotation elements vector are? Knowing that the three columns of the rotation matrix are the three axis vectors allow you to compare the changes after each rotation (horizontal vs vertical for example).</p>

---

## Post #5 by @AurelieS (2025-12-11 13:14 UTC)

<p>Yes we are constructing the pose matrix since we run our own <strong>OpenIGTLink server</strong> using Python that streams motion-capture transforms on <strong>port 18946</strong>.<br>
These transforms come from either <strong>Vicon</strong> or <strong>Qualisys</strong>, depending on the setup.</p>
<p>We then use <strong>PlusServer</strong>, which connects to our OpenIGTLink server as a client.<br>
PlusServer reads the incoming transforms on <strong>port 18946</strong>, synchronizes them with the ultrasound video stream, and then re-publishes the combined (video + tracking) data to <strong>3D Slicer</strong> via OpenIGTLink on <strong>port 18944</strong>. Interestingly the delay is comparable to direct integration using Optitrack and PlusServer for example.</p>
<p>Since it was pretty straightforward using Vicon I did not really think about Qualisys but yes I need to test everything because something in the constructed matrix seems wrong.</p>
<p>Thanks a lot, I will keep you updated.</p>

---

## Post #6 by @AurelieS (2025-12-16 10:57 UTC)

<p>Hello !</p>
<p>I confirm that the issue came from the fact that QTM sends data in columns, and not in lines ! so our transform matrices were wrong, Slicer and IGT have nothing to do with our issue <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I adjusted the code and now the pivot calibration works fine with an RMS &lt;1.</p>
<p>We will shortly share our code for Qualisys and Vicon integration.</p>
<p>Best regards,</p>
<p>Aurélie</p>

---

## Post #7 by @cpinter (2025-12-16 12:01 UTC)

<p>Excellent, thanks for confirming!</p>
<p>It makes sense that the transform is sent per column, because that’s how the vectors make sense one after the other.</p>
<p>Looking forward to seeing the shared core for integration. Thanks for all the work!</p>

---
