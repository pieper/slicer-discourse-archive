# Hardware connection issue

**Topic ID**: 6217
**Date**: 2019-03-20
**URL**: https://discourse.slicer.org/t/hardware-connection-issue/6217

---

## Post #1 by @lRaulMN7 (2019-03-20 11:54 UTC)

<p>Hello!.</p>
<p>I’m using a video reader to collect the live time images from an ultrasound machine.</p>
<p>I managed to collect that video data and stream it to a rtmp URL.</p>
<p>Now I guess I have to connect this URL with PlusToolkit, right? Or PlusToolkit is already able to detect the images captured by the video reader?</p>
<p>My idea is to send the frames from the streaming to SlicerIGT and then show those images in 3DSlicer.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2019-03-20 12:15 UTC)

<p>Try the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpenCVVideo.html" rel="nofollow noopener">OpenCV video device</a> in Plus, it may be able to receive an rtmp stream. You can then follow <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a> to set up receiving and visualization in Slicer.</p>

---

## Post #3 by @lRaulMN7 (2019-03-21 08:51 UTC)

<p>Hi Andras! Thanks for your reply.</p>
<p>When I use that configuration file, it says that OpenCVVideo is not a supported Device.</p>
<pre><code>|ERROR|008.246000|SERVER&gt; Unknown device type: OpenCVVideo. Supported devices: 3dConnexion, AuroraTracker, ChRobotics, Epiphan, FakeTracker, GenericSerialDevice, ICCapturing, ImageProcessor, Microchip, MmfVideo, NDITracker, NoiseVideo, OpenIGTLinkTracker, OpenIGTLinkVideo, OpticalMarkerTracker, PhidgetSpatial, PolarisTracker, SavedDataSource, UsSimulator, VFWVideo, VirtualBufferedCapture, VirtualCapture, VirtualDiscCapture, VirtualMixer, VirtualSwitcher, VirtualVolumeReconstructor| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDeviceFactory.cxx(386)
|ERROR|008.264000|SERVER&gt; No devices created. Please verify configuration file and any error produced.| in :\D\PSNP64b\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(134)
|INFO|008.264000| Server process terminated.| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(453)
|INFO|008.265000| Disconnect request successful| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(307)
|ERROR|008.265000| Failed to start server process| in E:\D\PSNP64b\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(219)
</code></pre>
<p>I’m using the last version of Plus Toolkit.</p>

---

## Post #4 by @lRaulMN7 (2019-03-21 09:11 UTC)

<p>It seems I have to do a proper installation of Plus Toolkit, <a href="https://github.com/PlusToolkit/PlusLib/issues/363" rel="nofollow noopener">https://github.com/PlusToolkit/PlusLib/issues/363</a></p>
<p>I just downloaded a part of it. I’m following this instructions now <a href="https://github.com/PlusToolkit/PlusBuild/blob/master/Docs/BuildInstructionsWindows.md" rel="nofollow noopener">https://github.com/PlusToolkit/PlusBuild/blob/master/Docs/BuildInstructionsWindows.md</a></p>

---

## Post #5 by @Sunderlandkyl (2019-03-21 18:25 UTC)

<p>I’m going to enable OpenCV video device in the Plus nightly build and see how much it increases the package size.<br>
If it is not too much, then we can enable it in the downloadable releases.</p>

---

## Post #6 by @lRaulMN7 (2019-03-22 08:06 UTC)

<p>That would be amazing! Yesterday I had a few issues trying to set up the PlusBuild (long build process, some errors after build, etc…)</p>
<p>Tell me if you do this update ^^</p>

---

## Post #7 by @Sunderlandkyl (2019-03-22 15:30 UTC)

<p>OpenCV was already included in package for ArUco marker tracking, so the additional size of the OpenCVVideo device was negligible.</p>
<p>The device should be included in the nightly packages starting tomorrow.</p>

---

## Post #8 by @lRaulMN7 (2019-03-25 11:10 UTC)

<p>Hi again. Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> for updating the nighty package.</p>
<p>I still have problems with the configuration in 3d Slicer. I’ll try to give all the possible information so maybe someone can help me out.</p>
<p>I’m currently streaming the ultrasound image in rtmp://192.168.146.30/live/1234. This works because I tried this URL in VLC and I can see the broadcast.</p>
<p>Now, I prepared this xml file for the plus server.</p>
<pre><code>&lt;PlusConfiguration version="2.1"&gt;
  &lt;DataCollection StartupDelaySec="1.0" &gt;
    &lt;DeviceSet
      Name="PlusServer: OpenCV device capturing an RTMP stream"
      Description="Broadcasting acquired video through OpenIGTLink"
    /&gt;
   &lt;Device
      Id="VideoDevice"
      Type="OpenCVVideo" 
      RequestedCaptureApi="CAP_FFMPEG"
      VideoURL="rtmp://192.168.146.30/live/1234"&gt;
      &lt;DataSources&gt;
        &lt;DataSource Type="Video" Id="Video" ImageType="RGB_COLOR" PortUsImageOrientation="MF"  /&gt;
      &lt;/DataSources&gt;
      &lt;OutputChannels&gt;
        &lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
      &lt;/OutputChannels&gt;
    &lt;/Device&gt;
  &lt;/DataCollection&gt;
  &lt;CoordinateDefinitions&gt;
    &lt;Transform From="Image" To="Reference"
      Matrix="
        1 0 0 0
        0 1 0 0
        0 0 1 0
        0 0 0 1" /&gt;
  &lt;/CoordinateDefinitions&gt;
  &lt;PlusOpenIGTLinkServer
    MaxNumberOfIgtlMessagesToSend="1"
    MaxTimeSpentWithProcessingMs="50"
    ListeningPort="18944"
    SendValidTransformsOnly="true"
    OutputChannelId="VideoStream" &gt;
    &lt;DefaultClientInfo&gt;
      &lt;MessageTypes&gt;
        &lt;Message Type="IMAGE" /&gt;
      &lt;/MessageTypes&gt;
      &lt;ImageNames&gt;
        &lt;Image Name="Image" EmbeddedTransformToFrame="Reference" /&gt;
      &lt;/ImageNames&gt;
    &lt;/DefaultClientInfo&gt;
  &lt;/PlusOpenIGTLinkServer&gt;
&lt;/PlusConfiguration&gt;
</code></pre>
<p>I did a little change to the .xml <a class="mention" href="/u/lassoan">@lassoan</a> suggested, I had to change the parameter StreamURL to VideoURL, because I was getting errors and the PLUS Server logs suggested me that.</p>
<p>When I Launch the server, I get 0 errors. However, I don’t know if Plus Server is reading correctly the images yet (In the logs I have several python debug lines, I’ll trace down them now, but maybe this is not the issue)</p>
<pre><code>032519_104702.717|TRACE|045.826000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in     E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.750|TRACE|045.860000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.785|TRACE|045.894000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.818|TRACE|045.927000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.829|INFO|045.939000| Received new client connection (client 1 at 192.168.146.30:18944). Number of connected clients: 1| in E:\D\PTNP64b\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(277)
032519_104702.851|TRACE|045.960000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.884|TRACE|045.994000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.919|TRACE|046.028000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.936|INFO|046.045000| OpenIGTLink broadcasting started. No data was available between 0-41.0331sec, therefore no data were broadcasted during this time period.| in E:\D\PTNP64b\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(428)
032519_104702.936|TRACE|046.045000| vtkPlusDevice::GetTrackedFrameList(41.1331, 1)| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(717)
032519_104702.936|TRACE|046.045000| Unable to get latest timestamp from video buffer!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1273)
032519_104702.936|TRACE|046.045000| Unable to get most recent timestamp!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(754)
032519_104702.936|TRACE|046.045000| Number of added frames: 1 out of 1| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(935)
032519_104702.946|TRACE|046.055000| Failed to get tracked frame list from data collector (last recorded timestamp: 46.042243| in E:\D\PTNP64b\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(433)
032519_104702.953|TRACE|046.062000| vtkPlusOpenCVCaptureVideoSource::InternalUpdate| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\OpenCVVideo\vtkPlusOpenCVCaptureVideoSource.cxx(275)
032519_104702.983|TRACE|046.092000| vtkPlusDevice::GetTrackedFrameList(46.0422, 1)| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(717)
032519_104702.983|TRACE|046.092000| Unable to get latest timestamp from video buffer!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(1273)
032519_104702.983|TRACE|046.092000| Unable to get most recent timestamp!| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(754)
032519_104702.983|TRACE|046.093000| Number of added frames: 1 out of 1| in E:\D\PTNP64b\PlusLib\src\PlusDataCollection\vtkPlusChannel.cxx(935)
</code></pre>
<p>That is just a part of the logs when I connect the client from the 3D slicer. In Slicer, first I’m setting the IGTLink, following the tutorial steps:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39789ff220668adee2f62a75c6feef2034056d97.png" data-download-href="/uploads/short-url/8cpEv1D3FeBujvAaJ0IKvn2P54z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39789ff220668adee2f62a75c6feef2034056d97_2_567x499.png" alt="image" data-base62-sha1="8cpEv1D3FeBujvAaJ0IKvn2P54z" width="567" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39789ff220668adee2f62a75c6feef2034056d97_2_567x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39789ff220668adee2f62a75c6feef2034056d97_2_850x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39789ff220668adee2f62a75c6feef2034056d97.png 2x" data-dominant-color="F2F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">901×794 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After that, I press the box “Active”. Then I go to the Plus Remote Module. Here is where I start getting lost because Slicer is asking me to set a Configuration file to “Launch Server”? Why would I Launch another Server when the plus one is already running? 3DSlicer should play a client role, right? I guess I have a misconception about this…</p>
<p>Anyways I set the IP and the port, and for the configuration file, I’m using the Plus Server one. Then I click connect and I open the log, but when I click “Launch server”, nothings happens.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3363578d792a0af57bc9661bb475a952bd837087.png" data-download-href="/uploads/short-url/7kBbNkh8guh51Im0LQpz1xQTnkH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3363578d792a0af57bc9661bb475a952bd837087_2_555x500.png" alt="image" data-base62-sha1="7kBbNkh8guh51Im0LQpz1xQTnkH" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3363578d792a0af57bc9661bb475a952bd837087_2_555x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3363578d792a0af57bc9661bb475a952bd837087_2_832x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3363578d792a0af57bc9661bb475a952bd837087.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">900×810 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you guys know what I might be missing here? D: Also, I saw the Capture device ID field, but I’m not able to write in it.</p>

---

## Post #9 by @Sunderlandkyl (2019-03-25 14:08 UTC)

<p>Once you click “Active” then your images should already start appearing in 3D Slicer as a volume called “Image_Reference”.</p>
<p>You don’t need to use the “Plus server launcher remote control” section in PlusRemote. It is an interface that can be used to start and stop PlusServer instances remotely.</p>

---

## Post #10 by @lRaulMN7 (2019-03-26 08:45 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> you were right, I don’t need Plus Remote method for this. Sorry.</p>
<p>However, I’m not able to see the images in real time properly. I managed to take some snapshots by using the method “UltrasoundSnapshots”. When I click “Add Snapshot”, I can see the last frame of my stream.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a93fd3fea1d86f9f1502471e2ddbb4dc3728efb.png" data-download-href="/uploads/short-url/3N7tKacFGV1Sj3KhKhiYZj8fW0H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a93fd3fea1d86f9f1502471e2ddbb4dc3728efb_2_690x168.png" alt="image" data-base62-sha1="3N7tKacFGV1Sj3KhKhiYZj8fW0H" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a93fd3fea1d86f9f1502471e2ddbb4dc3728efb_2_690x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a93fd3fea1d86f9f1502471e2ddbb4dc3728efb_2_1035x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a93fd3fea1d86f9f1502471e2ddbb4dc3728efb_2_1380x336.png 2x" data-dominant-color="CCCEE6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1625×398 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I don’t find the way to see the whole streaming.</p>
<p>If I enter the method Wizards&gt;“Compare Volumes” and I press “Lightbox Target Volume” I can see the streaming, but in 9 boxes and exiting the working space…</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gyazo.com/e9feaec62cef754f218a0cd963a6a8bb">
  <header class="source">
      <img src="https://assets2.gyazo.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://gyazo.com/e9feaec62cef754f218a0cd963a6a8bb" target="_blank" rel="noopener nofollow ugc">Gyazo</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/256;"><img src="https://thumb.gyazo.com/thumb/800_w/eyJhbGciOiJIUzI1NiJ9.eyJpbWciOiJfNDQwNjg2ZThmOWIzNjBkNTcxMmM3YWI1OGJhNmE3ZmEifQ.8loHVr3QdT6CcOQjsJlrXwmhrkC-9p1AZ07rFXYjCoo-gif.jpg" class="thumbnail" width="" height=""></div>

<h3><a href="https://gyazo.com/e9feaec62cef754f218a0cd963a6a8bb" target="_blank" rel="noopener nofollow ugc">Gyazo Screen Video</a></h3>

  <p>Gyazo is the easiest way to record screenshots &amp; videos you can share instantly. Save time with async visual communication that's effortless and engaging.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I guess the Image_Reference is a vector of 1 frame and each time I collect a new frame, I’m updating it?</p>

---

## Post #11 by @lRaulMN7 (2019-03-26 10:42 UTC)

<p>Ok, it was as easy as Data &gt; Image_Reference &gt; Show , then link the different views and toggle 3D view.</p>
<p>Finally!</p>

---

## Post #12 by @lassoan (2019-03-27 13:56 UTC)

<p>I’m glad you could figure it out. You can find step-by-step instructions for setting up Slicer scenes for image guidance in <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a>.</p>

---
