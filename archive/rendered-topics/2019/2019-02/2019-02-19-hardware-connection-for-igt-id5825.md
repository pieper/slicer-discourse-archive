---
topic_id: 5825
title: "Hardware Connection For Igt"
date: 2019-02-19
url: https://discourse.slicer.org/t/5825
---

# Hardware connection for IGT

**Topic ID**: 5825
**Date**: 2019-02-19
**URL**: https://discourse.slicer.org/t/hardware-connection-for-igt/5825

---

## Post #1 by @Felix_Navarro_Guirad (2019-02-19 09:47 UTC)

<p>Dear communuty,</p>
<p>We are trying to connect our ultrasound device and brachy stepper to Slicer using the PLUS server.</p>
<p>Do any of you have used a BK US device (via OEM interface or video capture) or a brachy stepper as tracker device?</p>
<p>I cannot connect with my devices and I don’t know why (I can provide the xml configuration files).</p>

---

## Post #2 by @Sunderlandkyl (2019-02-19 13:58 UTC)

<p>Can you post an issue, including your config file + log file to the Plus GitHub page?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PlusToolkit/PlusLib/issues/new">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PlusToolkit/PlusLib/issues/new" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/337b7cc06184984e148c075df20ef009e0e6ecaa.png" class="thumbnail onebox-avatar" width="500" height="500" data-dominant-color="E1E1E1">

<h3><a href="https://github.com/PlusToolkit/PlusLib/issues/new" target="_blank" rel="noopener nofollow ugc">Build software better, together</a></h3>

  <p>GitHub is where people build software. More than 100 million people use GitHub to discover, fork, and contribute to over 330 million projects.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Felix_Navarro_Guirad (2019-02-20 09:59 UTC)

<p>Thank you very much for your reply.</p>
<p>I’m going to attach screenshots of the config files since the software of the modifies the content.</p>
<p>This is the xml file that I have used to test the connection with the CIVCO EXII brachy stepper:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72cf97decff2b95846bc07be3ba8c51cff095e59.png" data-download-href="/uploads/short-url/gnFchvOvVIEP8nqXXZryjxyBeeB.png?dl=1" title="CIVCO_STEPPER" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72cf97decff2b95846bc07be3ba8c51cff095e59.png" alt="CIVCO_STEPPER" data-base62-sha1="gnFchvOvVIEP8nqXXZryjxyBeeB" width="335" height="499" data-dominant-color="F2F3F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CIVCO_STEPPER</span><span class="informations">582×868 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the xml file that I have used to test the connection with the BK flex focus TRUS via OEM port:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29e27697d43904bcd992606cbb4e636d22f0e002.png" data-download-href="/uploads/short-url/5YwLPVqlqrxHovRLZvcQj75Bn2y.png?dl=1" title="TRUS_FlexFocus" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29e27697d43904bcd992606cbb4e636d22f0e002.png" alt="TRUS_FlexFocus" data-base62-sha1="5YwLPVqlqrxHovRLZvcQj75Bn2y" width="393" height="500" data-dominant-color="F3F5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TRUS_FlexFocus</span><span class="informations">582×740 18.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regarding the CIVCO stepper: I have verified that the baud rate is 9600 and that the virtual COM port is the number 5, nevertheless it seems that no answer is received. Do you have any information about the remaining configuration parameters of the COM port?</p>
<p>Regarding the TRUS device: I’m using Flex Focus inestead of Pro Focus. I’m supposed to deactivate the crc check and the acknowledge of the communications but I have not received support form the manufacturer about how to do this. When I try to connect the server says “unexpected response”. Do you know how to do this or could you recommend a frame grabber?<br>
This is the complete log of the connection trial:</p>
<blockquote>
<p>Blockquote:<br>
|DEBUG|266.132000| Application configuration file ‘C:/Users/BEBIG Variseed/PlusApp-2.6.0.20180310-Win32/bin/PlusConfig.xml’ saved| in E:\D\PSNPb\PlusLib\src\PlusCommon\vtkPlusConfig.cxx(502)<br>
|INFO|266.133000| Connect using configuration file: C:\Users\BEBIG Variseed\Desktop\Pruebas registro US-RM\BkOEM.xml| in E:\D\PSNPb\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(314)<br>
|INFO|266.134000| Server process command line: “C:/Users/BEBIG Variseed/PlusApp-2.6.0.20180310-Win32/bin/PlusServer.exe” --config-file=“C:\Users\BEBIG Variseed\Desktop\Pruebas registro US-RM\BkOEM.xml” --verbose=5| in E:\D\PSNPb\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(205)<br>
|INFO|266.770000| Server process started successfully| in E:\D\PSNPb\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(213)<br>
|INFO|272.763000|SERVER&gt; Software version: Plus-2.6.0.63ba551d - Win32| in tkPlusLogger(188)<br>
|DEBUG|272.763000|SERVER&gt; Device set configuration is read from file: C:\Users\BEBIG Variseed\Desktop\Pruebas registro US-RM\BkOEM.xml| in :\D\PSNPb\PlusLib\src\PlusServer\Tools\PlusServer.cxx(104)<br>
|INFO|272.764000|SERVER&gt; Server status: Reading configuration.| in :\D\PSNPb\PlusLib\src\PlusServer\Tools\PlusServer.cxx(109)<br>
|DEBUG|272.764000|SERVER&gt; StartupDelaySec: 1.000000| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(89)<br>
|DEBUG|272.764000|SERVER&gt; AveragedItemsForFiltering is not defined in source element “Video”. Using default value: 20| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDataSource.cxx(378)<br>
|INFO|272.765000|SERVER&gt; VideoDevice: Local time offset: 0ms| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1105)<br>
|DEBUG|272.765000|SERVER&gt; vtkPlusTransformRepository::ReadConfiguration: no CoordinateDefinitions element was found| in :\D\PSNPb\PlusLib\src\PlusCommon\vtkPlusTransformRepository.cxx(626)<br>
|DEBUG|272.765000|SERVER&gt; BK scanner OEM port: 7915| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(170)<br>
|DEBUG|272.766000|SERVER&gt; Connected to BK scanner| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(188)<br>
|DEBUG|272.766000|SERVER&gt; No saved data source devices were found that use original timestamps, so synchronization of loop times is not performed| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(652)<br>
|DEBUG|272.767000|SERVER&gt; VideoDevice: vtkPlusDevice::StartRecording| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDevice.cxx(1240)<br>
|DEBUG|272.767000|SERVER&gt; Process message from BK: DATA:US_WIN_SIZE 600,580;| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|DEBUG|272.768000|SERVER&gt; Initializing Plus OpenIGTLink server…| in :\D\PSNPb\PlusLib\src\PlusServer\Tools\PlusServer.cxx(154)<br>
|DEBUG|272.768000|SERVER&gt; Data sent by default: IGTL version: 1Message types: IMAGE. Transforms: (none). Strings: (none). Images: Image (EmbeddedTransformToFrame: Tracker)| in :\D\PSNPb\PlusLib\src\PlusServer\vtkPlusOpenIGTLinkServer.cxx(170)<br>
|INFO|272.768000|SERVER&gt; Press Ctrl-C to quit.| in :\D\PSNPb\PlusLib\src\PlusServer\Tools\PlusServer.cxx(171)<br>
|INFO|272.769000|SERVER&gt; Plus OpenIGTLink server listening on IPs: 169.254.94.70, 169.254.115.33, 169.254.17.247, 169.254.45.154, 127.0.0.1 – port 18944| in :\d\psnpb\pluslib\src\plusserver\vtkPlusOpenIGTLinkServerWin32.cxx(81)<br>
|DEBUG|272.769000|SERVER&gt; Ultrasound geometry. StartLineX_m: 0.00933471 StartLineY_m: -0.00658264 StartLineAngle_rad: 0.342409 StartDepth_m: -1.32635e-005 StopLineX_m: -0.00933471 StopLineY_m: -0.00658264 StopLineAngle_rad: 2.79918 StopDepth_m: 0.0766017| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(746)<br>
|DEBUG|272.770000|SERVER&gt; Process message from BK: DATA:B_GEOMETRY_PIXEL:A 212,270,811,849;| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|DEBUG|272.770000|SERVER&gt; Ultrasound geometry. tissueLeft_m: -0.0429663 tissueTop_m: 0.0765787 tissueRight_m: 0.0429663 tissueBottom_m: -0.00648955| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(826)<br>
|DEBUG|272.771000|SERVER&gt; Process message from BK: DATA:B_GAIN:A 50;| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|DEBUG|272.771000|SERVER&gt; Acknowledge message received| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(513)<br>
|DEBUG|272.772000|SERVER&gt; Process message from BK: SDATA:US_WIN_SIZE 600,580;| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|DEBUG|272.772000|SERVER&gt; Ultrasound geometry. StartLineX_m: 0.00933471 StartLineY_m: -0.00658264 StartLineAngle_rad: 0.342409 StartDepth_m: -1.32635e-005 StopLineX_m: -0.00933471 StopLineY_m: -0.00658264 StopLineAngle_rad: 2.79918 StopDepth_m: 0.0766017| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(746)<br>
|DEBUG|272.773000|SERVER&gt; Process message from BK: SDATA:B_GEOMETRY_PIXEL:A 212,270,811,849;| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|DEBUG|272.773000|SERVER&gt; Ultrasound geometry. tissueLeft_m: -0.0429663 tissueTop_m: 0.0765787 tissueRight_m: 0.0429663 tissueBottom_m: -0.00648955| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(826)<br>
|DEBUG|272.774000|SERVER&gt; Process message from BK: SDATA:B_GAIN:A 50;| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|DEBUG|272.774000|SERVER&gt; uncompressedPixelBufferSize = 265087| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(571)<br>
|DEBUG|272.774000|SERVER&gt; Process message from BK: DATA:CAPTURE_IMAGE <span class="hashtag-raw">#6265087</span>?PNG | in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(451)<br>
|WARNING|272.792000|SERVER&gt; Received unknown message from BK: ERROR:INTERFACE| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(517)<br>
|WARNING|272.824000|SERVER&gt; Unspecified charactes received. Adding these to image.| in :\D\PSNPb\PlusLib\src\PlusDataCollection\BkProFocus\vtkPlusBkProFocusOemVideoSource.cxx(618)</p>
</blockquote>
<p>Thank you very much.</p>

---

## Post #4 by @Sunderlandkyl (2019-02-21 14:23 UTC)

<p>I’m not familiar with the details of the BK devices, and I can’t test the connection since we don’t have a device here.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> are you able to help, or do you know someone who can?</p>

---

## Post #5 by @Felix_Navarro_Guirad (2019-02-22 10:12 UTC)

<p>Thank you very much for your answer,</p>
<p>In order to provide a workaround, could you recommend a frame grabber or video capture device?</p>

---

## Post #6 by @MARKRONSON (2020-01-01 06:34 UTC)

<p>Thank you so much for the response. I wasn’t aware about this.</p>

---
