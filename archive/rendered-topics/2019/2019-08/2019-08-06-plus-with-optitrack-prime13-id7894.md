# PLUS with Optitrack Prime13

**Topic ID**: 7894
**Date**: 2019-08-06
**URL**: https://discourse.slicer.org/t/plus-with-optitrack-prime13/7894

---

## Post #1 by @BGWH (2019-08-06 13:22 UTC)

<p>Dear all,</p>
<p>I tried to use SliceIGT and PLUS (PlusApp-2.9.0.20190802-Win64) in combination with Optitrack Prime 13 cameras (Motive version 2.0.0). To design the configuration file I have followed this guide:<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html" class="onebox" target="_blank" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html</a></p>
<p>So I have stored a .xml config file as well as two RigidBodyFiles.</p>
<p>According to the log files, the server started successfully, still two warning and one error occured:</p>
<p>|INFO|025.010000|SERVER&gt; Server status: Starting servers.<br>
|WARNING|025.011000|SERVER&gt; Buffer item is not in the buffer (Uid: 0)!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusTimestampedCircularBuffer.cxx(176)<br>
|WARNING|025.045000|SERVER&gt; Unable to get timestamp from OptiTrackReferenceToTracker tool tracker buffer for time: 0| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1293)<br>
|ERROR|025.046000|SERVER&gt; Failed to get tracker buffer item UID from time: 1.137856| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1325)<br>
|INFO|025.075000|SERVER&gt; Plus OpenIGTLink server listening on IPs: 169.254.62.161, 169.254.75.70, 169.254.44.54, 192.168.132.1, 192.168.47.1, 192.168.5.37, 169.254.35.96, 192.168.56.1, 127.0.0.1, 169.254.119.51 – port 18944<br>
|INFO|025.076000|SERVER&gt; Server status: Server(s) are running.</p>
<p>When connecting to the server in Slicer 3D (v4.10.2) the following warning appears:<br>
|WARNING|181.934000|SERVER&gt; Buffer item is not in the buffer (Uid: 1)!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusTimestampedCircularBuffer.cxx(182)<br>
|WARNING|181.936000|SERVER&gt; Unable to get timestamp from default tool tracker buffer| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1158)</p>
<p>Furthermore, in IGT/PlusRemote I cannot select a ‘Capture device ID’ and a ‘Reconstructor device ID’ in the dropdown list (it is empty).</p>
<p>Does anyone know these warnings/errors? And does anyone know if PLUS is compatible with the Optitrack Prime13 or just with Duo/Trio?</p>
<p>Best,<br>
Bernhard</p>

---

## Post #2 by @lassoan (2019-08-06 13:40 UTC)

<p>Yes, Plus toolkit supports all Optitrack cameras. Since most likely the issue is in the Plus configuration file, let’s continue the discussion here: <a href="https://github.com/PlusToolkit/PlusLib/issues/580" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib/issues/580</a></p>

---

## Post #3 by @BGWH (2019-08-07 12:00 UTC)

<p>Thanks, this issue is fixed.</p>

---
