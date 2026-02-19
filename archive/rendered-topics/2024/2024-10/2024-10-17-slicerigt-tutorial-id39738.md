---
topic_id: 39738
title: "Slicerigt Tutorial"
date: 2024-10-17
url: https://discourse.slicer.org/t/39738
---

# SlicerIGT tutorial

**Topic ID**: 39738
**Date**: 2024-10-17
**URL**: https://discourse.slicer.org/t/slicerigt-tutorial/39738

---

## Post #1 by @DanielGu (2024-10-17 03:28 UTC)

<p>Hi, I’m a very beginner of 3dslicer and slicerIGT,<br>
and I would like to connect my webcam to 3dslicer by using slicerigt</p>
<p><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</p>
<p>I’ve changed CaptureDeviceID, Framesize, Videoformat, also port, but still ‘connection failed’ message comes out.</p>
<p>How can I solve this?<br>
(I’ve prepared OpticalMarkerTracker/realsense_gen2_calibration.yml as well)<br>
is there any video lecture for this connection?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2c157dfbb65f8a812e7fd0aa2c936cc4c4d44a7.png" data-download-href="/uploads/short-url/u4qviv9tW5B7ntuOAQ2rSzTjMXB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2c157dfbb65f8a812e7fd0aa2c936cc4c4d44a7_2_690x408.png" alt="image" data-base62-sha1="u4qviv9tW5B7ntuOAQ2rSzTjMXB" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2c157dfbb65f8a812e7fd0aa2c936cc4c4d44a7_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2c157dfbb65f8a812e7fd0aa2c936cc4c4d44a7_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2c157dfbb65f8a812e7fd0aa2c936cc4c4d44a7_2_1380x816.png 2x" data-dominant-color="F8F5FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2880×1704 400 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2024-10-17 14:50 UTC)

<p>Can you attach a log file?</p>

---

## Post #3 by @DanielGu (2024-10-17 14:51 UTC)

<p>how can I find a log file from plustoolkit?</p>

---

## Post #4 by @Sunderlandkyl (2024-10-17 14:52 UTC)

<p>It will be in the data folder in your Plus install directory.</p>

---

## Post #5 by @DanielGu (2024-10-17 14:53 UTC)

<p>time|level|timeoffset|message|location<br>
101724_235305.665|INFO|000.001000| System start timestamp: 719845| in E:\D\PSNP64b\PlusLib\src\PlusCommon\vtkPlusAccurateTimer.cxx(51)<br>
101724_235305.667|INFO|000.003000| Software version: Plus-2.8.0.62873a16 - Win64| in vtkPlusLogger(188)<br>
101724_235305.667|INFO|000.003000| Logging at level 3 (INFO) to file: C:/Users/tjmds/PlusApp-2.8.0.20191105-Win64/data/101724_235305_PlusLog.txt| in E:\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(81)<br>
101724_235305.670|INFO|000.005000| Selected US image orientation: MF| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataSource.cxx(301)<br>
101724_235305.687|INFO|000.023000| Server status: Reading configuration.| in E:\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(92)<br>
101724_235305.687|INFO|000.023000| Server status: Connecting to devices.| in E:\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(103)<br>
101724_235305.720|WARNING|000.055000|&gt; Unable to init capture device with requested details: device ID: 0 (Camera Sensor OV02C10) stream 0, 1920x1080, 30Hz, MJPG| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(313)<br>
101724_235305.720|INFO|000.056000|&gt; Supported vide formats for Device Id 0 (Camera Sensor OV02C10)| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(680)<br>
101724_235305.720|INFO|000.056000|&gt;   Stream index 0 - Frame size: 1920x1080, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.720|INFO|000.056000|&gt;   Stream index 0 - Frame size: 1280x720, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.720|INFO|000.056000|&gt;   Stream index 0 - Frame size: 640x360, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.720|INFO|000.056000|&gt;   Stream index 0 - Frame size: 640x480, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.720|INFO|000.056000|&gt;   Stream index 0 - Frame size: 960x540, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.720|ERROR|000.056000|&gt; Unable to initialize capture device with default details: device ID: 0 (Camera Sensor OV02C10) stream 0, 640x480, 30Hz, YUY2| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(319)<br>
101724_235305.720|INFO|000.056000| Found capture devices:| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(692)<br>
101724_235305.721|INFO|000.057000|&gt;   0: Camera Sensor OV02C10| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(698)<br>
101724_235305.721|INFO|000.057000|&gt; Supported vide formats for Device Id 0 (Camera Sensor OV02C10)| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(680)<br>
101724_235305.721|INFO|000.057000|&gt;   Stream index 0 - Frame size: 1920x1080, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.721|INFO|000.057000|&gt;   Stream index 0 - Frame size: 1280x720, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.721|INFO|000.057000|&gt;   Stream index 0 - Frame size: 640x360, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.721|INFO|000.057000|&gt;   Stream index 0 - Frame size: 640x480, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.721|INFO|000.057000|&gt;   Stream index 0 - Frame size: 960x540, video format: NV12, frame rate: 30| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\MicrosoftMediaFoundation\vtkPlusMmfVideoSource.cxx(685)<br>
101724_235305.721|ERROR|000.057000| VideoDevice: Cannot connect to data source, ConnectInternal failed| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1147)<br>
101724_235305.721|ERROR|000.057000| Unable to connect device: VideoDevice.| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(353)<br>
101724_235305.723|INFO|000.058000| Use aruco camera calibration file located at: C:/Users/tjmds/PlusApp-2.8.0.20191105-Win64/config/OpticalMarkerTracker/realsense_gen2_calibration.yml| in E:\D\PSNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(236)<br>
101724_235305.723|ERROR|000.059000| Datacollector failed to connect to devices| in E:\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(106)</p>

---

## Post #6 by @Sunderlandkyl (2024-10-17 16:05 UTC)

<p>The log file lists the supported video streams configurations from your camera.</p>
<p>The only video format from the camera seems to be NV12, which is not currently a supported format in Plus.</p>

---

## Post #7 by @MReza (2024-10-17 16:06 UTC)

<p>Hello,</p>
<p>I don’t understand the log file, but I would recommend that you first test your webcam using a configuration file specifically for the webcam without including the markers. If you can successfully connect to the Plus server and see the camera in 3D Slicer, then you can go back to your main configuration file.</p>
<p>Remember, when you run the main configuration file, if your webcam doesn’t see even one of the markers, you will receive an error indicating that it is not successfully connected. I have attached a configuration file for you to check your webcam first.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9eca5ec9227c07f1ab1a3cf77724cf05220f0cf.png" data-download-href="/uploads/short-url/zEVUcnntCxiQf9W0rThnQHKX1zF.png?dl=1" title="qq" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9eca5ec9227c07f1ab1a3cf77724cf05220f0cf.png" alt="qq" data-base62-sha1="zEVUcnntCxiQf9W0rThnQHKX1zF" width="608" height="500" data-dominant-color="FCF9FD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">qq</span><span class="informations">898×738 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @DanielGu (2024-10-18 06:42 UTC)

<p>Thanks to your advice, the connection issue has been resolved, and I can confirm that the status in OpenIGTlinkIF is ‘on’!(I’ve set Videoformat from YUY2 to NV12 and solved → Perhaps Plus support NV12 currently?)</p>
<p>What I want to do next is to align the object and the marker, as shown in this video: <a href="https://youtu.be/MOqh6wgOOYs?si=hZqHskpL6N3Ah9ey" rel="noopener nofollow ugc">Aligning Object and Marker</a>. What steps should I follow next?</p>

---

## Post #9 by @Sunderlandkyl (2024-10-18 14:26 UTC)

<p>Interesting, I didn’t think that NV12 would work.</p>
<p>You can load the OpticalMarkerTracker_Scene.mrb from the “config” folder in your Plus install.</p>

---

## Post #10 by @DanielGu (2024-10-18 15:00 UTC)

<p>Can I get more detail of it?<br>
in the config\OpticalMarkerTracker folder, I already have OpticalMarkerTracker_Scene.mrb file</p>
<p>How can I turn on Camera from the scene in the 3d slicer?<br>
Also how to align my marker with stl file?<br>
So many questions haha</p>
<p>I hope you can dedicate some time to check my status remotely. How did you study, Where and what did you study? Can you spare some time? If so, I will do my best to accommodate the time you suggest.</p>

---

## Post #11 by @Sunderlandkyl (2024-10-18 15:15 UTC)

<p>In the Marker coordinate system, the origin of the marker is at the center of the marker, and the XY axis lie perpendicular with the marker plane. Transforming a square on the XY plane using the MarkerNToTracker transform should be positioned correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bcbb4f7700835845a57646de47465962f2d8039.png" data-download-href="/uploads/short-url/8wYBRPxHTAvXlyQXFMYBuxBtkrn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bcbb4f7700835845a57646de47465962f2d8039.png" alt="image" data-base62-sha1="8wYBRPxHTAvXlyQXFMYBuxBtkrn" width="234" height="282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">234×282 6.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For more complex models, you will have to perform a stylus calibration and then a landmark registration.</p>
<p>Have you worked through the tutorials from <a href="http://www.slicerigt.org" rel="noopener nofollow ugc">www.slicerigt.org</a>?<br>
<a href="https://onedrive.live.com/?authkey=%21AGQkSCZOwjVYXw8&amp;id=7230D4DEC6058018%212937&amp;cid=7230D4DEC6058018" rel="noopener nofollow ugc">SlicerIGT Tutorials</a></p>
<p>They should help walk you through the process of stylus calibration and landmark registration using Slicer and Plus.</p>

---
