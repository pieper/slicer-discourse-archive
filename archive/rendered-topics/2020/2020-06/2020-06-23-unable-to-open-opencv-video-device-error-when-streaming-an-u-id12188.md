# "Unable to open OpenCV video device" error when streaming an URL using PLUS Toolkit

**Topic ID**: 12188
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/unable-to-open-opencv-video-device-error-when-streaming-an-url-using-plus-toolkit/12188

---

## Post #1 by @xlucia (2020-06-23 21:59 UTC)

<p>Hello!</p>
<ol>
<li>I am trying to stream an URL using the following PLUS config file (I want to send the video from the streaming to SlicerIGT):</li>
</ol>

  
    
   	
      
        
      
      
        
      
    
  
<p><br>
<br>
<br>
<br>
<br>
<br>
<video><br>
<br>
</video><br>
<br>
<br>
</p>

<p>When I lauch the server, I get the following error:</p>
<p>|ERROR|5539.549000|SERVER&gt; Unable to open OpenCV video device.| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(193)<br>
|ERROR|5539.582000|SERVER&gt; VideoDevice: Cannot connect to data source, ConnectInternal failed| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1147)<br>
|ERROR|5539.583000|SERVER&gt; Unable to connect device: VideoDevice.| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(353)<br>
|ERROR|5539.584000|SERVER&gt; Datacollector failed to connect to devices| in :\D\PSNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(106)</p>
<p>I have tried to stream using VLC media player and it worked with that URL, so I don’t know why it does not work with PLUS.</p>
<ol start="2">
<li>I have also tried to select a file from my computer so that ‘VideoURL’ in the config file is the path to my file (I just modified that line from the config file), which is an .mkv file. It did not display any error but reproduced the video very fast and apparently not taking into account the specified acquisition rate.</li>
</ol>
<p>Which option is better? What am I missing?</p>
<p>Thanks in advance!</p>

---
