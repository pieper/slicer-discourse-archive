# Cannot perform Aruco marker tracking

**Topic ID**: 30578
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/cannot-perform-aruco-marker-tracking/30578

---

## Post #1 by @MasatoshiOBA (2023-07-13 11:30 UTC)

<p>I would like to try optical marker tracking which presented in this slides <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day2_Plus.pptx" rel="noopener nofollow ugc">https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day2_Plus.pptx</a>.</p>
<p>Using USB webcam, and Aruco marker, I would like to perform optical marker tracking demo like youtube video.</p><div class="youtube-onebox lazy-video-container" data-video-id="MOqh6wgOOYs" data-video-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=MOqh6wgOOYs" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/MOqh6wgOOYs/maxresdefault.jpg" title="Webcam-based tracking in 3D Slicer/SlicerIGT" width="" height="">
  </a>
</div>

<p>I basically follow the instructions written in the pptx. When I launched Plus server using configulation file attatched below (which was editted as same as the pptx said.), and connect the Plus server via OpenIGTLinkIF, nothing is shown in Scene. The slide <span class="hashtag-raw">#55</span> and <span class="hashtag-raw">#56</span> said that I should find those transform nodes "Scene &gt; IGTLConnector &gt; IN &gt; Marker0ToTracker, Marker1ToTracker, Marker0ToMarker1 " .</p>
<p>I seemed to stack around slide <span class="hashtag-raw">#56</span>.</p>
<p>Do you have any solution for this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37a648cf0849ebc028753029c7ca9e25d3808698.jpeg" data-download-href="/uploads/short-url/7WiwsDjbWYQ0kAemfJDl6fODiu4.jpeg?dl=1" title="capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a648cf0849ebc028753029c7ca9e25d3808698_2_690x388.jpeg" alt="capture" data-base62-sha1="7WiwsDjbWYQ0kAemfJDl6fODiu4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a648cf0849ebc028753029c7ca9e25d3808698_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a648cf0849ebc028753029c7ca9e25d3808698_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37a648cf0849ebc028753029c7ca9e25d3808698_2_1380x776.jpeg 2x" data-dominant-color="8E8FA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture</span><span class="informations">1920×1080 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

  
    
    
      
        
      
      
        
      
    
    
      
        
        
      
      
        
      
      
        
          
          
        
      
    
    
      
        
      
    
  
<p><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</p>
<p><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</p>

---

## Post #2 by @Sunderlandkyl (2023-07-13 13:50 UTC)

<p>The transforms won’t appear in OpenIGTLinkIF until you show them to the camera.</p>
<p>Make sure to try a couple of different PortUsImageOrientation, MF/UF/UN/UF, depending on your camera, this may need to be adjusted.</p>
<p>Could you attach the Plus log and config file?</p>

---

## Post #3 by @MasatoshiOBA (2023-07-14 10:37 UTC)

<p><strong>Thank you for your reply!</strong></p>
<p><strong>I’m using Windows 10 (64bit) PC with USB webcam.</strong><br>
<strong>Slicer 5.2.2</strong><br>
<strong>PlusApp-2.9.0.20230704-Win64</strong></p>
<p><strong>My config file is below</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80e52d59f582078e7d867371175a29b94a4a9589.jpeg" data-download-href="/uploads/short-url/iog7OmzCniJiwm1aNHw5jlCj1FL.jpeg?dl=1" title="capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e52d59f582078e7d867371175a29b94a4a9589_2_690x377.jpeg" alt="capture3" data-base62-sha1="iog7OmzCniJiwm1aNHw5jlCj1FL" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e52d59f582078e7d867371175a29b94a4a9589_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e52d59f582078e7d867371175a29b94a4a9589_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80e52d59f582078e7d867371175a29b94a4a9589_2_1380x754.jpeg 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture3</span><span class="informations">1893×1035 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1073508255e5df89ab220b6f1036d751bec11d5b.jpeg" data-download-href="/uploads/short-url/2lwHnzjJ7hwq9LSI0S95B8ptHlN.jpeg?dl=1" title="capture4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1073508255e5df89ab220b6f1036d751bec11d5b_2_690x368.jpeg" alt="capture4" data-base62-sha1="2lwHnzjJ7hwq9LSI0S95B8ptHlN" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1073508255e5df89ab220b6f1036d751bec11d5b_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1073508255e5df89ab220b6f1036d751bec11d5b_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1073508255e5df89ab220b6f1036d751bec11d5b_2_1380x736.jpeg 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture4</span><span class="informations">1900×1016 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>And the log file which was obtained immediately after launching Plus server using the config file above.</strong></p>
<p>time|level|timeoffset|message|location<br>
071423_192354.498|INFO|000.001000|&gt; Software version: Plus-2.9.0.5a7cefc6 - Win64| in vtkPlusLogger(52)<br>
071423_192354.500|INFO|000.002000| Logging at level 3 (INFO) to file: C:/Users/MasatoshiOba/PlusApp-2.9.0.20230704-Win64/data/071423_192354_PlusLog.txt| in E:\D\PTNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(81)<br>
071423_192354.500|INFO|000.003000| Selected US image orientation: UN| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataSource.cxx(300)<br>
071423_192354.501|INFO|000.004000| Server status: Reading configuration.| in E:\D\PTNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(92)<br>
071423_192354.501|INFO|000.004000| Server status: Connecting to devices.| in E:\D\PTNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(103)<br>
071423_192354.628|INFO|000.130000| Use aruco camera calibration file located at: C:/Users/MasatoshiOba/PlusApp-2.9.0.20230704-Win64/config/OpticalMarkerTracker/realsense_gen2_calibration.yml| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(233)<br>
071423_192355.634|INFO|001.137000| Server status: Starting servers.| in E:\D\PTNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(116)<br>
071423_192355.634|WARNING|001.137000| Buffer item is not in the buffer (Uid: 0)!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusTimestampedCircularBuffer.cxx(176)<br>
071423_192355.634|WARNING|001.137000| Unable to get timestamp from Marker0ToTracker tool tracker buffer for time: 0| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1295)<br>
071423_192355.634|WARNING|001.137000| Buffer item is not in the buffer (Uid: 0)!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusTimestampedCircularBuffer.cxx(176)<br>
071423_192355.635|WARNING|001.138000| Unable to get timestamp from Marker1ToTracker tool tracker buffer for time: 0| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1295)<br>
071423_192355.635|ERROR|001.138000| Failed to get most recent timestamp from all the tracker tools| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1312)<br>
071423_192355.638|INFO|001.141000| Plus OpenIGTLink server listening on IPs: 192.168.17.88, 169.254.14.106, 169.254.63.16, 127.0.0.1, 172.23.112.1, 172.18.224.1 – port 18944| in E:\D\PTNP64b\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServerWin32.cxx(81)<br>
071423_192355.692|INFO|001.195000| Plus OpenIGTLink server listening on IPs: 192.168.17.88, 169.254.14.106, 169.254.63.16, 127.0.0.1, 172.23.112.1, 172.18.224.1 – port 18945| in E:\D\PTNP64b\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServerWin32.cxx(81)<br>
071423_192355.735|INFO|001.238000| Server status: Server(s) are running.| in E:\D\PTNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(147)<br>
071423_192355.735|INFO|001.238000| Press Ctrl-C to quit.| in E:\D\PTNP64b\PlusLib\src\PlusServer\Tools\PlusServer.cxx(148)</p>
<p><strong>The message window of Plus server saying</strong></p>
<p>Connection successful!</p>
<p>Tracking of printed ArUco markers using a simple camera. Marker positions and image data are broadcasted through OpenIGTLink (on port 18944 and 18945, respectively). To use a different camera, change CaptureDeviceId attribute (to 0, 1, 2, …).</p>
<p>Plus OpenIGTLink server listening on IPs: 192.168.17.88, 169.254.14.106, 169.254.63.16, 127.0.0.1, 172.23.112.1, 172.18.224.1 – port 18944<br>
Plus OpenIGTLink server listening on IPs: 192.168.17.88, 169.254.14.106, 169.254.63.16, 127.0.0.1, 172.23.112.1, 172.18.224.1 – port 18945</p>
<p><strong>Then I switched to OpenIGTLinkIF module, and change the port number from 18944 to 18945.</strong><br>
<strong>After that, I turned the “Active” checkbox on. I showed Aruco marker printed from the slide to my webcam, however, I couldn’t find translation node ("marker0totracker or "marker1totracker) in"I/O configulation window.</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf6ff752ed02df11a8f80b2435ec0ddd8ede1ba.jpeg" data-download-href="/uploads/short-url/dgp7iPDrWkYxXZD2Z3fT2fVUylI.jpeg?dl=1" title="capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf6ff752ed02df11a8f80b2435ec0ddd8ede1ba_2_690x388.jpeg" alt="capture2" data-base62-sha1="dgp7iPDrWkYxXZD2Z3fT2fVUylI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf6ff752ed02df11a8f80b2435ec0ddd8ede1ba_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf6ff752ed02df11a8f80b2435ec0ddd8ede1ba_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf6ff752ed02df11a8f80b2435ec0ddd8ede1ba_2_1380x776.jpeg 2x" data-dominant-color="BABBC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture2</span><span class="informations">1920×1080 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>the Plus log file in this situation is</strong></p>
<p>071423_193351.080|ERROR|009.708000| Pose estimation failed. Tool Marker0ToTracker with marker 0.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.082|ERROR|009.709000| Pose estimation failed. Tool Marker1ToTracker with marker 1.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.115|ERROR|009.742000| Pose estimation failed. Tool Marker0ToTracker with marker 0.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.115|ERROR|009.742000| Pose estimation failed. Tool Marker1ToTracker with marker 1.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.151|ERROR|009.778000| Pose estimation failed. Tool Marker0ToTracker with marker 0.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.151|ERROR|009.778000| Pose estimation failed. Tool Marker1ToTracker with marker 1.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.184|ERROR|009.812000| Pose estimation failed. Tool Marker1ToTracker with marker 1.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.215|ERROR|009.843000| Pose estimation failed. Tool Marker1ToTracker with marker 1.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)<br>
071423_193351.253|ERROR|009.880000| Pose estimation failed. Tool Marker1ToTracker with marker 1.| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpticalMarkerTracking\vtkPlusOpticalMarkerTracker.cxx(416)</p>
<p><strong>I appriciate your support.</strong></p>

---

## Post #4 by @MasatoshiOBA (2023-07-14 11:24 UTC)

<p>I think I could solved this by my self after the latest reply…</p>
<p>When I created two scene, one is listening port 18944, another is listening 18945,<br>
pointer model apperead and which seemed to move with the marker moving in front of the Webcam.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2e1dd16f2dcdfd246d35bc37a7451ca7f7079fc.jpeg" data-download-href="/uploads/short-url/neVgayDfYEVxNY7BaeiMggONGYQ.jpeg?dl=1" title="capture5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e1dd16f2dcdfd246d35bc37a7451ca7f7079fc_2_690x378.jpeg" alt="capture5" data-base62-sha1="neVgayDfYEVxNY7BaeiMggONGYQ" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e1dd16f2dcdfd246d35bc37a7451ca7f7079fc_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e1dd16f2dcdfd246d35bc37a7451ca7f7079fc_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2e1dd16f2dcdfd246d35bc37a7451ca7f7079fc_2_1380x756.jpeg 2x" data-dominant-color="9596A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture5</span><span class="informations">1903×1043 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is little bit lagged, even with low pass filter provided by transform processor module. But it’s fine.</p>
<p>I am still wondering I solved this or not. But your kind reply encourage me to face this.</p>

---

## Post #5 by @Sunderlandkyl (2023-07-14 16:14 UTC)

<p>Yeah I think you’ve solved it. The config file has 2 OpenIGTLink connections. The one on 18944 is transmitting the marker transforms, and the one on 18945 is transmitting the webcam image.</p>

---

## Post #6 by @ngansir (2024-02-17 06:44 UTC)

<p>Hi, I am new to 3D Slicer, can show the step how to make the Aruco Marker tracking work as the Video exactly? I have followed the tutorial and made webcam function, created the needle model, however the tracking position and direction is not I expected.</p>
<p><a href="https://www.youtube.com/watch?v=MOqh6wgOOYs" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=MOqh6wgOOYs</a></p>

---
