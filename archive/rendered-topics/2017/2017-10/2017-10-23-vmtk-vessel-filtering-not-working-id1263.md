# VMTK vessel filtering not working

**Topic ID**: 1263
**Date**: 2017-10-23
**URL**: https://discourse.slicer.org/t/vmtk-vessel-filtering-not-working/1263

---

## Post #1 by @Keno_Mentor (2017-10-23 01:36 UTC)

<p>Operating system: macOS<br>
Slicer version: 4.5<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello again,</p>
<p>Trying to use the VMTK module which I recently downloaded.  When I select the vessel filtering option I get a “failure to load VMTK libraries” error message.  The other options seem to work fine.</p>
<p>Any ideas?</p>
<p>Keno</p>

---

## Post #2 by @pieper (2017-10-23 14:20 UTC)

<p>Version 4.5 is very old.  Please try with the latest release 4.8.</p>

---

## Post #3 by @Keno_Mentor (2017-10-24 10:08 UTC)

<p>Thanks for the reply Steve.</p>
<p>I’ve tried with 4.8 and the latest 4.9 version - same behavior.</p>
<p>When I use the Segmentation module, the options load but the ‘Start’ button<br>
is disabled.  I add all the details I can as well as seeding the vascular<br>
tree on the image but it remains greyed out…</p>
<p>Does the Mac version generally have more problems than the windows version?</p>

---

## Post #4 by @lassoan (2017-10-24 13:07 UTC)

<p>Could you please copy here a screenshot (make sure no patient name and ID is displayed in slice views) and check if there are any error messages printed in the Python console (Ctrl+3)?</p>

---

## Post #5 by @pieper (2017-10-24 13:22 UTC)

<p>I just tried the vmtk extension on mac with Slicer 4.8 and confirmed it isn’t working.</p>
<p>There’s an issue with the python library:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import vtkvmtkSegmentationPython as vtkvmtkSegmentation
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ImportError: dlopen(/Applications/Slicer-4.8.0.app/Contents/Extensions-26489/SlicerVMTK/lib/Slicer-4.8/qt-loadable-modules/Python/vtkvmtkSegmentationPython.so, 2): Library not loaded: libvtkvmtkSegmentationPythonD.dylib
  Referenced from: /Applications/Slicer-4.8.0.app/Contents/Extensions-26489/SlicerVMTK/lib/Slicer-4.8/qt-loadable-modules/Python/vtkvmtkSegmentationPython.so
  Reason: image not found
</code></pre>

---

## Post #6 by @lassoan (2017-10-24 13:24 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you have a look? I think this worked before (but maybe just on Windows and Linux).</p>

---

## Post #7 by @Keno_Mentor (2017-10-24 13:26 UTC)

<p>Hi Andras,</p>
<p>Images below: before scrolling down the module window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/0b2cafd0f26779115a4e024d5492b1d6214f7e4d.png" data-download-href="/uploads/short-url/1AQZzILaS628kVqHCE2GMD07kS1.png?dl=1" title="Screen Shot 2017-10-24 at 2.23.36 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0b2cafd0f26779115a4e024d5492b1d6214f7e4d_2_690x420.png" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0b2cafd0f26779115a4e024d5492b1d6214f7e4d_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0b2cafd0f26779115a4e024d5492b1d6214f7e4d_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0b2cafd0f26779115a4e024d5492b1d6214f7e4d_2_1380x840.png 2x" data-dominant-color="ADACB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2017-10-24 at 2.23.36 PM.png</span><span class="informations">2548×1552 785 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After scrolling down to the start button</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/25582c4bd2eca05679f6ba73db15238fe1511b27.png" data-download-href="/uploads/short-url/5kmzJ824gXD4lus1yybRVo8pzJZ.png?dl=1" title="Screen Shot 2017-10-24 at 2.23.18 PM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/25582c4bd2eca05679f6ba73db15238fe1511b27_2_690x416.png" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/25582c4bd2eca05679f6ba73db15238fe1511b27_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/25582c4bd2eca05679f6ba73db15238fe1511b27_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/25582c4bd2eca05679f6ba73db15238fe1511b27_2_1380x832.png 2x" data-dominant-color="ACACB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2017-10-24 at 2.23.18 PM.png</span><span class="informations">2552×1540 785 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2017-10-25 01:56 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> confirmed this is a building/packaging error on MacOS. We are working on releasing a new stable version, so most likely we cannot fix this issue in the next 2 weeks. You can track its status by watching this issue: <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/11">https://github.com/vmtk/SlicerExtension-VMTK/issues/11</a></p>
<p>Until the problem is fixed, you can run a Windows version of Slicer (using Parallels) or try to use VMTK directly, using command-line tools (see <a href="http://www.vmtk.org/">http://www.vmtk.org/</a>).</p>

---

## Post #9 by @Keno_Mentor (2017-10-25 05:36 UTC)

<p>Thanks for the update Andras. I’ll try the windows or linux version</p>

---

## Post #10 by @Fernando (2017-11-17 19:46 UTC)

<p>This is still not working, I just had the same issue.</p>

---

## Post #11 by @lassoan (2017-11-18 07:10 UTC)

<p>Latest nightly works for me on both Windows and Linux. Haven’t tested Mac.</p>

---

## Post #12 by @Fernando (2017-11-18 17:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="1263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Haven’t tested Mac.</p>
</blockquote>
</aside>
<p>Seems to be ok with latest build on Mac too.</p>

---

## Post #13 by @MBJS (2017-12-04 21:19 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> - VMTK doesn’t appear in the Extension Manager in Slicer 4.9 Nightly 4/Dec/17 on MacOS X 10.13.</p>
<p>Am I missing something obvious?</p>

---

## Post #14 by @Fernando (2017-12-05 11:11 UTC)

<aside class="quote no-group" data-username="MBJS" data-post="13" data-topic="1263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/f14d63/48.png" class="avatar"> MBJS:</div>
<blockquote>
<p>Am I missing something obvious?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/mbjs">@MBJS</a> I’m not sure what you mean. I can see VMTK on the Extensions Manager (on macOS 10.12.6).</p>

---

## Post #15 by @MBJS (2017-12-05 11:29 UTC)

<p>That’s interesting.<br>
When I search in Slicer 4.8.0, VMTK is in the Extension Manager.<br>
When I search in Slicer 4.9 Nightly, it does not appear there.</p>

---

## Post #16 by @cpinter (2017-12-05 14:06 UTC)

<p>Sometimes nightly build fails for certain extensions, so the nightlies are not always perfect. Unfortunately in this case it seems that VMTK build fails consistently:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;display=project&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a><br>
This was the last successful build, on November 19:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-11-19&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-11-19&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a></p>
<p>The logs show a linking error when trying to find vtkCommonExecutionModelPython.</p>

---

## Post #17 by @MBJS (2017-12-05 18:33 UTC)

<p>Awesome! Thanks for hunting the down <a class="mention" href="/u/cpinter">@cpinter</a>! Much appreciated</p>

---

## Post #18 by @lassoan (2017-12-05 19:30 UTC)

<p>The culprit is this commit in VMTK: <a href="https://github.com/vmtk/vmtk/commit/58c882900cacb66a1f6e5bd26f248b937a362ee8">https://github.com/vmtk/vmtk/commit/58c882900cacb66a1f6e5bd26f248b937a362ee8</a></p>
<p>I update the git hash in VMTK extension to use the last working version until we fix the VMTK master. So, VMTK should be available in the nightly build again from tomorrow.</p>

---

## Post #19 by @MBJS (2017-12-06 09:46 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> ! I’ll wait for the next mac nightly build.<br>
Just downloaded the 4/12/17 Nightly, and its still to show up.</p>

---

## Post #20 by @lassoan (2017-12-06 15:19 UTC)

<p>Probably you’ve tried it too early in the morning (US time). It should be available now on Windows and Linux.</p>

---

## Post #21 by @lassoan (2017-12-06 15:50 UTC)

<p>Build on Mac is broken - the issue is tracked here: <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/11">https://github.com/vmtk/SlicerExtension-VMTK/issues/11</a></p>

---

## Post #22 by @avarghes23 (2018-11-26 20:07 UTC)

<p>Hi all,</p>
<p>Was this issue ever resolved? I’m trying to follow along with this tutorial (<a href="https://www.youtube.com/watch?v=DJ2032yo5Co" rel="nofollow noopener">https://www.youtube.com/watch?v=DJ2032yo5Co</a>) but whenever I try to use Vesselness Filtering within VMTK I get the same error as OP. I found the GitHub VMTK extension files. Do I need to just drag those under the Extensions subfolder of 3D Slicer (after doing “Show Package Contents” in Finder)?</p>
<p>Also, if this extension is still confirmed not working for Mac, is there an alternate workflow to achieve the same result?</p>

---

## Post #23 by @cpinter (2018-11-26 21:13 UTC)

<p>Mac build has been failing as far as the CDash history goes. Linux build was fixed by <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-08-18&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=VMTK" rel="nofollow noopener">this</a> nightly, but unfortunately Mac build kept failing.</p>
<p>You can’t just point to the source code to try it, binaries need to be built from source. A Slicer developer who uses Mac will need to look into the issue to fix it.</p>
<p>(To the devs: even if we can’t get the factory to build it, maybe we could get a build that we can upload to midas for the stable so that it can be installed by the users?)</p>

---

## Post #24 by @mschumaker (2018-11-30 15:34 UTC)

<p>I’ve ultimately given up on using Slicer-VMTK, in part because of these ongoing issues, but I would be very interested to see a resolution to this.</p>

---

## Post #25 by @lucie.macron (2019-07-12 08:59 UTC)

<p>Hi,</p>
<p>I’m having the same issue using Slicer 4.10.2 on macOS.<br>
Has this issue been resolved ?</p>
<p>Thanks,</p>

---

## Post #26 by @lassoan (2019-07-12 13:46 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> you fixed VMTK builds in the past, could you please have a look at it again? Maybe the issue is that .so files are not placed into the correct location - see <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1641848" rel="nofollow noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1641848</a></p>

---

## Post #27 by @jcfr (2019-07-13 02:58 UTC)

<p>I identified the problem and this should be fixed by <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/17" rel="nofollow noopener">https://github.com/vmtk/SlicerExtension-VMTK/pull/17</a></p>

---

## Post #28 by @Ritu_Karela (2019-08-05 10:58 UTC)

<p>Can anyone help me with vesselness filtering? my issue is that when I preview one fiducial point for arteries it looks okay but when I click on apply button it selects some part of skull as well with arteries. I am trying to extract arteries from CT Angiography. Any suggestions? I am not sure what I am doing wrong.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b2e6f9891fd791cbdfa247f46f4553db1aff8b5.png" data-download-href="/uploads/short-url/fiazPdQgtwWpwQ2tHysYRd1qoTz.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b2e6f9891fd791cbdfa247f46f4553db1aff8b5_2_620x500.png" alt="Capture" data-base62-sha1="fiazPdQgtwWpwQ2tHysYRd1qoTz" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b2e6f9891fd791cbdfa247f46f4553db1aff8b5_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b2e6f9891fd791cbdfa247f46f4553db1aff8b5_2_930x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b2e6f9891fd791cbdfa247f46f4553db1aff8b5_2_1240x1000.png 2x" data-dominant-color="828180"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1254×1010 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #29 by @lassoan (2019-08-05 14:08 UTC)

<p>Vesselness filtering enhances visibility and contrast of vessels but usually does not perfectly extracts vessels from the entire image.</p>
<p>You may use vesselness image as master volume in Segment Editor to touch up results. For example, you can use Thresholding effect to do an initial extraction and clean it up by Scissors and Islands effects.</p>

---

## Post #30 by @Ritu_Karela (2019-08-06 05:37 UTC)

<p>Thank you Andras for the quick reply. Can you direct me to any tutorial link through which I can extract arteries from DICOM images?</p>

---

## Post #31 by @lassoan (2019-08-06 16:21 UTC)

<p>See segmentation tutorials here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>

---

## Post #32 by @Ritu_Karela (2019-08-06 16:36 UTC)

<p>I have gone through all these tutorials already. But still I am unable to segment the arteries. Whenever I extract them from DICOM using thresholding and islands effect it comes with some part of skull as well. Is there any other way of extracting arteries other than thresholding?<br>
Thank you in advance.</p>

---

## Post #33 by @lassoan (2019-08-06 17:00 UTC)

<p>Maybe you’ve missed the segmentation recipes. This one is relevant for what you would like to achieve: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/" rel="nofollow noopener">https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/</a></p>

---

## Post #34 by @Ritu_Karela (2019-08-07 10:22 UTC)

<p>Thank you for the link Andras but it doesn’t solve my problem completely. I am attaching some pictures here. Actually grow from seeds effect is not able to extract all arteries. It is extracting only the once that I have painted and it is very difficult to paint each and everything. It was successful with Aorta because it was a single structure. Could you suggest something more?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be81957205097721863cf5954a14e0e59a36f00d.png" data-download-href="/uploads/short-url/rbilMwOLw9wOKZmWi7MJN70fLsx.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81957205097721863cf5954a14e0e59a36f00d_2_690x362.png" alt="Capture" data-base62-sha1="rbilMwOLw9wOKZmWi7MJN70fLsx" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81957205097721863cf5954a14e0e59a36f00d_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81957205097721863cf5954a14e0e59a36f00d_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be81957205097721863cf5954a14e0e59a36f00d_2_1380x724.png 2x" data-dominant-color="757478"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1918×1009 454 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #35 by @lassoan (2019-08-10 17:49 UTC)

<p>You can start with simple thresholding, choosing threshold value so low that all vessels that you are interested are included. Then use that for masking and use Grow from seeds. This should allow very clear <em>separation</em> of bone from vessels.</p>
<p>However, if image is noisy and/or low-resolution, contrast filling is uneven, etc. then it may be hard to choose a threshold value that includes small vessels and you may need to do more manual work, e.g., with Paint effect or Draw tubes effect, with thresholding (Maskin settings / editable intensity range).</p>
<p>Do you have a baseline image without contrast? If yes, then you can subtract the background (with automatic motion compensation), which may help in segmenting smaller vessels and automatically remove bone.</p>

---

## Post #36 by @Ritu_Karela (2019-08-12 04:02 UTC)

<p>I can you the .nrrd file of brain angio. Will you try this please? I have actually tried everything and still not able to do this.</p>

---

## Post #37 by @Ritu_Karela (2019-08-12 07:18 UTC)

<p>Also I tried “subtract scalar volume” effect but my output volume still has bone data. So when I do thresholding it selects bone as well.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cc828366ec7b25d64913069ef6ee4e2be246f92.jpeg" data-download-href="/uploads/short-url/fwkoST6JO9cybsROZogjC3bBp8m.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc828366ec7b25d64913069ef6ee4e2be246f92_2_690x361.jpeg" alt="PNG" data-base62-sha1="fwkoST6JO9cybsROZogjC3bBp8m" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc828366ec7b25d64913069ef6ee4e2be246f92_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc828366ec7b25d64913069ef6ee4e2be246f92_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6cc828366ec7b25d64913069ef6ee4e2be246f92_2_1380x722.jpeg 2x" data-dominant-color="8C8C94"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1920×1007 451 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #38 by @Ritu_Karela (2019-08-12 07:23 UTC)

<p>Link to my nrrd files:<br>
<a href="https://drive.google.com/drive/folders/1fTDOh9KjKuQAt14sYgIJdUjfDDJm-EAl?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/1fTDOh9KjKuQAt14sYgIJdUjfDDJm-EAl?usp=sharing</a></p>

---

## Post #39 by @chir.set (2019-08-12 09:53 UTC)

<p>Slicer does not have a dedicated tool for vessel extraction, even with contrast enhancement. VMTK does not help any better, at least in my experience.</p>
<p>You will find such tools with dedicated software made by CT OEMs. That’s what I see with radiologists in my health institution. They do every vessel segmentation nearly automatically, refining with mouse clicks on the vessels.</p>
<p>Slicer aims to be a more generic tool. The developer team does not have enough financial resources to target specific tasks by medical discipline in my view. I think you should accept that your aim cannot be reached.</p>
<p>For your specific problem, the image below shows the best I could get using Level Tracing/Flood Filling/Grow from seeds. As you can see, the arterial isolation extent is quite limited. The skull base is always merged with the internal carotid arteries in close contact to the bone. If the latter is segmented at the same time, it could have been isolated from the arteries at the skull base. But this implies a lot of painting before the final segmentation. This is not feasible in practice.</p>
<p>In general, contrast enhanced arteries are quite readily segmented when there is no intimate contact with bones and when they are of surgical diameters (fortunately!). Otherwise, distal arteries isolation remains a challenge.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/871f3fac67e1bd6cd97d35c004df6a23ff8153ed.png" alt="Screenshot_20190812_113141" data-base62-sha1="jhlpkDo8jSusX38xQTfCh4B8ROJ" width="624" height="429"></p>

---

## Post #40 by @lassoan (2019-08-12 14:02 UTC)

<aside class="quote no-group" data-username="Ritu_Karela" data-post="37" data-topic="1263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ritu_karela/48/4324_2.png" class="avatar"> Ritu_Karela:</div>
<blockquote>
<p>Also I tried “subtract scalar volume” effect but my output volume still has bone data. So when I do thresholding it selects bone as well.</p>
</blockquote>
</aside>
<p>Usually, you need to register (spatially align) the two volumes before subtraction. You can use Elastix extension for this.</p>
<p>Subtraction without registration:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc66317ac08a5049e7d5d9519bfada3b9b3be402.jpeg" data-download-href="/uploads/short-url/A0PgMm6PmPrxhAB2eiczBWSbr8u.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc66317ac08a5049e7d5d9519bfada3b9b3be402_2_690x338.jpeg" alt="image" data-base62-sha1="A0PgMm6PmPrxhAB2eiczBWSbr8u" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc66317ac08a5049e7d5d9519bfada3b9b3be402_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc66317ac08a5049e7d5d9519bfada3b9b3be402_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc66317ac08a5049e7d5d9519bfada3b9b3be402.jpeg 2x" data-dominant-color="6E6D6B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1230×603 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Subtraction after registration:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa8196e30027bcccc751fa095a3ebb3026d02c1.jpeg" data-download-href="/uploads/short-url/AtDUbbarHKA8LXfqIF8AOn8lIn7.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa8196e30027bcccc751fa095a3ebb3026d02c1_2_506x500.jpeg" alt="image" data-base62-sha1="AtDUbbarHKA8LXfqIF8AOn8lIn7" width="506" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa8196e30027bcccc751fa095a3ebb3026d02c1_2_506x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa8196e30027bcccc751fa095a3ebb3026d02c1_2_759x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa8196e30027bcccc751fa095a3ebb3026d02c1_2_1012x1000.jpeg 2x" data-dominant-color="7B7C99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1227×1212 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="chir.set" data-post="39" data-topic="1263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Slicer does not have a dedicated tool for vessel extraction, even with contrast enhancement. VMTK does not help any better, at least in my experience.</p>
<p>You will find such tools with dedicated software made by CT OEMs.</p>
</blockquote>
</aside>
<p>For some reason, in recent years there have not been significant (funded) interest for developing/maintaining open-source vessel analysis tools. Maybe this is, as you say, because commercial tools already fulfill all the clinical and research needs. It is also possible that there are still unmet needs but there have not been research groups who could allocate grant funding for this.</p>

---

## Post #41 by @Ritu_Karela (2019-08-13 04:00 UTC)

<p>Andras this looks great! Could you please explain how did you do that?</p>

---

## Post #42 by @lassoan (2019-08-13 15:22 UTC)

<p>I’ve described all the steps in this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/" rel="nofollow noopener">segmentation recipe</a>. Example of segmentation:</p>
<p>                    <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/image-010.gif" target="_blank" class="onebox" rel="nofollow noopener">
            <img src="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/image-010.gif" width="491" height="500">
          </a>

</p>
<p>The only “manual” steps needed were choosing a few parameter values, so the whole workflow could be easily made fully automated - requiring only a single click and some optional parameter adjustments from the user.</p>

---
