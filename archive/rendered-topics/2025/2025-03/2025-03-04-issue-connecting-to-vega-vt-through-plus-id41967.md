# Issue connecting to Vega VT Through PLUS

**Topic ID**: 41967
**Date**: 2025-03-04
**URL**: https://discourse.slicer.org/t/issue-connecting-to-vega-vt-through-plus/41967

---

## Post #1 by @mariedemeyy (2025-03-04 20:48 UTC)

<p>Hi,</p>
<p>I am getting the following error when I try to connect to a Vega VT camera.</p>
<p>|INFO|2072.377000| Server process started successfully| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(329)</p>
<p>|ERROR|2072.388000|SERVER&gt; Device-&gt;host communication timeout| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\NDICAPITracking\vtkPlusNDITracker.cxx(967)</p>
<p>|ERROR|2072.413000|SERVER&gt; Failed to determine NDI port handle for tool APPLE02ToTracker| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\NDICAPITracking\vtkPlusNDITracker.cxx(657)</p>
<p>|ERROR|2072.414000|SERVER&gt; Failed to enable tool ports| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\NDICAPITracking\vtkPlusNDITracker.cxx(319)</p>
<p>|ERROR|2072.414000|SERVER&gt; TrackerDevice: Cannot connect to data source, ConnectInternal failed| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1147)</p>
<p>|ERROR|2072.415000|SERVER&gt; Unable to connect device: TrackerDevice.| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(353)</p>
<p>|ERROR|2072.415000|SERVER&gt; Datacollector failed to connect to devices| in :\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(106)</p>
<p>|ERROR|2072.486000| Server stopped unexpectedly. Return code: 1| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(864)</p>
<p>|INFO|2072.486000| Disconnect request successful| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(632)</p>
<p>I am able to connect to the camera through the NDI Toolbox Track. I am also able to ping the camera from the command line using ping 169.254.10.46. I can ping it with ping p9-25024.local. Here is the xml file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caec3ce78cdabfac3fc0f24406a6e9143965b374.png" data-download-href="/uploads/short-url/sX8Amb2z9ib6H3Fc3V6xDky0bmk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caec3ce78cdabfac3fc0f24406a6e9143965b374_2_554x500.png" alt="image" data-base62-sha1="sX8Amb2z9ib6H3Fc3V6xDky0bmk" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caec3ce78cdabfac3fc0f24406a6e9143965b374_2_554x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caec3ce78cdabfac3fc0f24406a6e9143965b374_2_831x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caec3ce78cdabfac3fc0f24406a6e9143965b374_2_1108x1000.png 2x" data-dominant-color="232324"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2211×1992 475 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b730bb2af18ac9e9242482d6eb979045733ce67.png" data-download-href="/uploads/short-url/mbauvXrx7d8Kq1Vu8Urj0oEm1RZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b730bb2af18ac9e9242482d6eb979045733ce67_2_690x261.png" alt="image" data-base62-sha1="mbauvXrx7d8Kq1Vu8Urj0oEm1RZ" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b730bb2af18ac9e9242482d6eb979045733ce67_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b730bb2af18ac9e9242482d6eb979045733ce67.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b730bb2af18ac9e9242482d6eb979045733ce67.png 2x" data-dominant-color="242527"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">912×345 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
