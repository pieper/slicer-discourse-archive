# Unable to input channel Id in Slicer->IGT->Plus Remote

**Topic ID**: 5799
**Date**: 2019-02-16
**URL**: https://discourse.slicer.org/t/unable-to-input-channel-id-in-slicer-igt-plus-remote/5799

---

## Post #1 by @zoez (2019-02-16 03:45 UTC)

<p>Operating system: windows 10<br>
Slicer version:Slicer4.10.0<br>
Expected behavior:record mha file from image streamed via openigtlink<br>
Actual behavior:does not allow inputing channel id for image</p>
<p>Hello,</p>
<p>I streamed images from PLUS to Slicer and tried to record the image stream as a .mha file. However, I was not able to set the <strong>capture device id</strong> in IGT-&gt;Plus Remote (please see images below). Although the input widget is not grayed out, it does not allow me to type in or choose a capture device id.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7f5eff9202ee126bcb2abad2af5b21e6403b9cd.png" data-download-href="/uploads/short-url/nXQEFG5Q7sGU4rEsMaKkejn1jch.png?dl=1" title="SlicerRecordMha" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7f5eff9202ee126bcb2abad2af5b21e6403b9cd_2_690x416.png" alt="SlicerRecordMha" data-base62-sha1="nXQEFG5Q7sGU4rEsMaKkejn1jch" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7f5eff9202ee126bcb2abad2af5b21e6403b9cd_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7f5eff9202ee126bcb2abad2af5b21e6403b9cd_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7f5eff9202ee126bcb2abad2af5b21e6403b9cd_2_1380x832.png 2x" data-dominant-color="767676"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerRecordMha</span><span class="informations">1920×1160 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I believe that this is causing problems when saving mha files because the following errors were loged in PLUS:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2755083412c2f11d865397577fbbf61c4d1c6980.png" data-download-href="/uploads/short-url/5BWNHAH1z3Tu9vnKyKPDeoXRXY4.png?dl=1" title="FailedToRecordToMha" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2755083412c2f11d865397577fbbf61c4d1c6980.png" alt="FailedToRecordToMha" data-base62-sha1="5BWNHAH1z3Tu9vnKyKPDeoXRXY4" width="690" height="65" data-dominant-color="1F1B18"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">FailedToRecordToMha</span><span class="informations">1895×181 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone have suggestions on how to fix this?</p>
<p>Thanks,<br>
Zoe</p>

---

## Post #2 by @lassoan (2019-02-17 17:30 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you have a look at this? Thanks!</p>

---

## Post #3 by @Sunderlandkyl (2019-02-19 15:54 UTC)

<p>Can you provide a link to your config file?</p>

---

## Post #4 by @zoez (2019-02-19 18:56 UTC)

<p>Here’s the config file I’m using.</p>
<pre><code class="lang-auto">&lt;PlusConfiguration version="2.1"&gt;

	&lt;DataCollection StartupDelaySec="1.0" &gt;
		&lt;DeviceSet
		   Name="PlusServer: Clarius ultrasound device"
		   Description="Broadcasting acquired video through OpenIGTLink"/&gt;
		&lt;Device Id="VideoDevice"
				  Type="Clarius"
				  IpAddress = "192.168.0.101"
				  TcpPort = "5828"
				  ImageSourceId = "Video"&gt;
			&lt;DataSources&gt;
				&lt;DataSource Type="Video" Id="Video" PortName="B" PortUsImageOrientation="UN"/&gt;
			&lt;/DataSources&gt;
			&lt;OutputChannels&gt;
				&lt;OutputChannel Id="VideoStream" VideoDataSourceId="Video" /&gt;
			&lt;/OutputChannels&gt;
		&lt;/Device&gt;
		&lt;Device
		  Id="CaptureDevice"
		  Type="VirtualCapture"
		  BaseFilename="RecordingTest.mha"
		  EnableCapturingOnStart="TRUE"
		  RequestedFrameRate="30"
		  EnableCapturing="TRUE" &gt;
			&lt;InputChannels&gt;
				&lt;InputChannel Id="VideoStream" /&gt;
			&lt;/InputChannels&gt;
		&lt;/Device&gt;
	&lt;/DataCollection&gt;

	&lt;CoordinateDefinitions&gt;
		&lt;Transform From="Image" To="Reference"
		  Matrix="
        0.2 0.0 0.0 0.0
        0.0 0.2 0.0 0.0
        0.0 0.0 0.2 0.0
        0 0 0 1" /&gt;
	&lt;/CoordinateDefinitions&gt;

	&lt;PlusOpenIGTLinkServer
	  MaxNumberOfIgtlMessagesToSend="1"
	  MaxTimeSpentWithProcessingMs="50"
	  ListeningPort="18944"
	  SendValidTransformsOnly="false"
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

---

## Post #5 by @Sunderlandkyl (2019-02-19 19:21 UTC)

<p>Can you start PlusServer.exe with log level debug, connect using Slicer, then try to start recording with Plus remote?</p>
<p>Once you’ve done that, can you add a link to the log from Plus?</p>

---

## Post #6 by @zoez (2019-02-19 22:49 UTC)

<p>Hi,<br>
Here’s a screenshot of the relevant part of the log. The complete log can be found <a href="https://github.com/zoez526/slicer_debug/blob/master/ClariusSlicerLog.txt" rel="noopener nofollow ugc">here</a>.The log file is relatively long, but you can find the relevant error logs by searching for “error”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f90defe88799c262aa2cf6d4598bca8fddb316ae.png" data-download-href="/uploads/short-url/zxeKwgMsYrzbU043ETi5CZDteiO.png?dl=1" title="ErrorDownloadingMhaLogVerbose%3D4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f90defe88799c262aa2cf6d4598bca8fddb316ae.png" alt="ErrorDownloadingMhaLogVerbose%3D4" data-base62-sha1="zxeKwgMsYrzbU043ETi5CZDteiO" width="690" height="191" data-dominant-color="211F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ErrorDownloadingMhaLogVerbose%3D4</span><span class="informations">1900×527 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,<br>
Zoe</p>

---

## Post #7 by @Sunderlandkyl (2019-02-21 13:59 UTC)

<p>It looks like the query for capture devices is being received by Plus, but the response is not being received in Slicer.</p>
<p>Thanks, I’ll keep looking into it.</p>

---

## Post #8 by @Sunderlandkyl (2019-02-21 16:23 UTC)

<p>I think I’ve solved the issue.<br>
There was a bug in the way that command responses were handled in Plus-2.6.</p>
<p>I’ve added a fix so that Plus-2.6 should work with the latest PlusRemote starting tomorrow morning with the next nightly build.<br>
Alternatively, you could also start using the nightly release (Plus-2.7).</p>

---

## Post #9 by @zoez (2019-02-23 22:48 UTC)

<p>Hello Kyle,</p>
<p>Thanks for the fix! I’m able to save .mha files from slicer now!</p>
<p>However, when the saved mha files are reloaded, the dimensions seem to be different from the original image.</p>
<p>The Image dimensions when saving: (640 * 480 * <strong>1</strong>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d9dd880292612152845e7b126faa67134e89d97.png" data-download-href="/uploads/short-url/fDIe58E9aXtXeqLD6taiPGeoHCn.png?dl=1" title="RecordingImageInfo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d9dd880292612152845e7b126faa67134e89d97_2_555x500.png" alt="RecordingImageInfo" data-base62-sha1="fDIe58E9aXtXeqLD6taiPGeoHCn" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d9dd880292612152845e7b126faa67134e89d97_2_555x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d9dd880292612152845e7b126faa67134e89d97_2_832x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d9dd880292612152845e7b126faa67134e89d97_2_1110x1000.png 2x" data-dominant-color="797978"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RecordingImageInfo</span><span class="informations">1246×1122 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Reloaded from mha: (<strong>4</strong> * 640 * 480)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dabab1950c9afeebfe1627e1a3dbfebf97e0759.png" data-download-href="/uploads/short-url/6w1hBpbmpd127aC9fbFNMJZEoeB.png?dl=1" title="ReloadedImageInfo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dabab1950c9afeebfe1627e1a3dbfebf97e0759_2_547x499.png" alt="ReloadedImageInfo" data-base62-sha1="6w1hBpbmpd127aC9fbFNMJZEoeB" width="547" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dabab1950c9afeebfe1627e1a3dbfebf97e0759_2_547x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dabab1950c9afeebfe1627e1a3dbfebf97e0759_2_820x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dabab1950c9afeebfe1627e1a3dbfebf97e0759_2_1094x998.png 2x" data-dominant-color="737271"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ReloadedImageInfo</span><span class="informations">1236×1128 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,<br>
Zoe</p>

---

## Post #10 by @Sunderlandkyl (2019-03-01 14:50 UTC)

<p>Could you send me the mha that you recorded?</p>
<p>For now, you should be able to replay the mha correctly using Plus (<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceSavedDataSource.html" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceSavedDataSource.html</a>).</p>

---

## Post #11 by @zoez (2019-03-01 18:26 UTC)

<p>Hello Kyle,</p>
<p>I didn’t find a way to add an attachment to this post. Please download the zipped mha file here: <a href="https://github.com/zoez526/slicer_debug/blob/master/MhaRecording.7z" rel="noopener nofollow ugc">https://github.com/zoez526/slicer_debug/blob/master/MhaRecording.7z</a></p>
<p>Also, I realized that if I open the mha file in visual studio and change the DimSize to be 1 640 480, the image will show up normally. However, the image will show up in the sagittal plane instead of axial plane.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b5294f47dcf5e2ffc16e802253b3e4743d3ec5f.png" data-download-href="/uploads/short-url/ma2WcttTbvFzmMwZzK9nfhltlqT.png?dl=1" title="MhaRecording" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b5294f47dcf5e2ffc16e802253b3e4743d3ec5f.png" alt="MhaRecording" data-base62-sha1="ma2WcttTbvFzmMwZzK9nfhltlqT" width="638" height="500" data-dominant-color="EDEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MhaRecording</span><span class="informations">970×760 37.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks,<br>
Zoe</p>

---

## Post #12 by @jamesobutler (2019-03-01 22:45 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> The issue of the frames showing up as a grid in one view due to weird DimSize line in the header. Any chance this is related to the issue described in <a href="https://github.com/SlicerRt/Sequences/issues/64" rel="nofollow noopener">SlicerRt/Sequences #64Viewing sequences without transforms problems</a>?</p>

---

## Post #13 by @Sunderlandkyl (2019-03-02 01:19 UTC)

<p>Yes, I think that it’s likely the same issue.</p>

---

## Post #14 by @zoez (2019-03-07 17:51 UTC)

<p>I’m wondering if you will be working on this issue soon?</p>

---

## Post #15 by @Sunderlandkyl (2019-03-08 15:10 UTC)

<p>Support for reading .igs.* files has been moved to the SlicerIGSIO extension.</p>
<p>The IGSIO library was recently created from Plus to allow access to reusable components between different applications. One of these components was sequence file IO.</p>
<p>If you install the SlicerIGSIO extension, you should be able to load the files as IGSIO sequence.<br>
I’ve tested it on the file that you provided, and it works well.</p>
<p>It’s included in the latest nightly, and will be included in the stable once it’s built.</p>

---
