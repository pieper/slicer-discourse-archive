# New extension: Fully automatic whole-body CT segmentation in 2 minutes using TotalSegmentator

**Topic ID**: 26710
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710

---

## Post #1 by @lassoan (2022-12-13 13:32 UTC)

<p>The <strong><a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator AI model is now available as an extension for 3D Slicer</a></strong> version 5.2 and above (see installation instructions <a href="https://github.com/lassoan/SlicerTotalSegmentator#setup">here</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1.jpeg" data-download-href="/uploads/short-url/uNEukuqDrXUWbSpuiA6BDwYo6Ln.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1_2_690x377.jpeg" alt="image" data-base62-sha1="uNEukuqDrXUWbSpuiA6BDwYo6Ln" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1_2_1380x754.jpeg 2x" data-dominant-color="413C38"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1050 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>A large number of AI segmentation models have been developed over the past few years, but <a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a> stands out in several aspects:</p>
<ul>
<li>
<strong>it can segment many structures</strong>: 104 anatomical structures (all abdominal organs, bones, larger vessels, muscles)</li>
<li>
<strong>it is very robust</strong>: it can segment any whole-body, abdominal, chest CT images, regardless of image resolution and field of view</li>
<li>
<strong>fast</strong>: computation time at full resolution is 1-2 minutes on a CUDA-capable GPU; and about 1-minute at low-resolution mode on CPU</li>
</ul>
<p>While it is not perfect (there can be a couple of few-millimeter segmentation errors), the segmentation is accurate enough for most purposes - 3D visualization, quantification, specifying region of interest for segmentation, registration, or further analysis.</p>
<p>TotalSegmentator extension can be installed by a few clicks in the extensions manager. It does not require a GPU, it can segment a whole-body CT in about a minute using just the CPU, but a CUDA-capable GPU is recommended for full-resolution segmentation (which takes 1-2 minutes on GPU but it would take 40-50 minutes on CPU).</p>
<p>Demo and tutorial video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="osvMB5SKcVQ" data-video-title="Automatic whole-body CT segmentation in 2 minutes using 3D Slicer and TotalSegmentator" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=osvMB5SKcVQ" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/osvMB5SKcVQ/maxresdefault.jpg" title="Automatic whole-body CT segmentation in 2 minutes using 3D Slicer and TotalSegmentator" width="" height="">
  </a>
</div>

<p>The <a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator segmentation engine</a> used in this extension was created at the department of Research and Analysis at University Hospital Basel using the <a href="https://github.com/MIC-DKFZ/nnUNet">nnU-Net framework</a> developed at DKFZ. If you use this tool then please cite: <code>Wasserthal J., Meyer M., Breit H., Cyriac J., Yang S., Segeroth M. TotalSegmentator: robust segmentation of 104 anatomical structures in CT images, 2022. https://arxiv.org/abs/2208.05868.  arXiv: 2208.05868</code></p>

---

## Post #2 by @lassoan (2022-12-13 19:59 UTC)

<p>11 posts were split to a new topic: <a href="/t/totalsegmentator-error-at-first-run-command-pip-install-git-https-github-com-wasserth-totalsegmentator-git-no-deps-returned-non-zero-exit-status/26715">TotalSegmentator error at first run: “Command ‘pip’, ‘install’, ‘git+https://github.com/wasserth/TotalSegmentator.git’, ‘–no-deps’ returned non-zero exit status”</a></p>

---

## Post #3 by @lassoan (2022-12-14 19:27 UTC)

<p>4 posts were split to a new topic: <a href="/t/totalsegmentator-for-only-segmenting-the-spine/26734">TotalSegmentator for only segmenting the spine</a></p>

---

## Post #6 by @philippepellerin (2022-12-14 16:56 UTC)

<p>Dear Andras, as I have said in an other post where you replied to a question, you have done an incredible job and I received it as my prefered X’mas gift.<br>
Thanks again and season greeting.</p>

---

## Post #8 by @lassoan (2022-12-14 19:28 UTC)

<p>3 posts were split to a new topic: <a href="/t/offline-installation-of-totalsegmentator/26735">Offline installation of TotalSegmentator</a></p>

---

## Post #9 by @Juicy (2022-12-14 21:36 UTC)

<p>Wow, this is really amazing! Excellent work. As Pellerin said, great Xmas present!!</p>

---

## Post #10 by @spalte (2022-12-16 14:46 UTC)

<p>Wow that is awesome!</p>

---

## Post #11 by @volkodavmyx (2022-12-16 17:02 UTC)

<p>Hmm. Does the module require any special CUDA drivers, or it must work on standard Game-ready Nvidia drivers?</p>
<p>I tried module, and it ignored my 2080ti. <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_tear.png?v=12" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @lassoan (2022-12-16 19:47 UTC)

<p>You must use <a href="https://pytorch.org/get-started/locally/">one of the CUDA versions listed on pytorch website as “Compute platform” for your system</a>, which is currently CUDA 11.6 or 11.7 for Windows and Linux. All other CUDA versions are ignored. Gaming cards (GeForce RTX) are fine. See <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/README.md#tutorial">documentation</a> for some more details.</p>

---

## Post #13 by @Esteban_Barreiro (2022-12-17 23:21 UTC)

<p>This is extremely beautifull!!! Cant wait to try it out! Im amazed!!! &lt;3</p>

---

## Post #14 by @lassoan (2022-12-19 03:52 UTC)

<p>3 posts were split to a new topic: <a href="/t/use-totalsegmentator-with-atlasess/26814">Use TotalSegmentator with atlasess</a></p>

---

## Post #15 by @sandigeeup (2022-12-19 15:30 UTC)

<p>Hei, thank you so much,  this looks amazing, but not able to find it in extensions manager. Using 5.0.3 ?</p>

---

## Post #16 by @rbumm (2022-12-19 16:09 UTC)

<p>Please use the extension from Slicer 5.2.1 stable, it is not compatible with previous Slicer versions.</p>

---

## Post #17 by @sandigeeup (2022-12-19 16:56 UTC)

<aside class="quote no-group" data-username="sandigeeup" data-post="17" data-topic="26710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sandigeeup/48/13722_2.png" class="avatar"> sandigeeup:</div>
<blockquote>
<p>just having a play with some canine data sets <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>haha, let us know if it works! <img src="https://emoji.discourse-cdn.com/twitter/dog2.png?v=12" title=":dog2:" class="emoji" alt=":dog2:" loading="lazy" width="20" height="20"></p>

---

## Post #18 by @sandigeeup (2022-12-19 18:09 UTC)

<p>Needs a little refining for canine data sets <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fb15b0a5b4f90aa0c443963f501b4cbb4e323c9.jpeg" alt="Picture1" data-base62-sha1="6NUqh2MYe4j6uHFh7IxylqotFY5" width="586" height="350"></p>
<p>. What is the lights extension, I have tried to find that but can’t?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43146a7208c71d8bbac5ef571340062722af0544.jpeg" alt="Picture4" data-base62-sha1="9zpJkDxpZmRRpLthKEtsvrIdwNK" width="586" height="350"></p>

---

## Post #19 by @rbumm (2022-12-19 18:37 UTC)

<aside class="quote no-group" data-username="sandigeeup" data-post="18" data-topic="26710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sandigeeup/48/13722_2.png" class="avatar"> sandigeeup:</div>
<blockquote>
<p>What is the lights extension</p>
</blockquote>
</aside>
<p>The “Lights” module is in the “Sandbox” extension.</p>

---

## Post #20 by @Chop1n (2022-12-21 12:04 UTC)

<p>Hi,</p>
<p>I’ve been following and using Slicer for a while. Today I’m giving a try to this magnific new tool. It really works well with the Sample data, but I get a wrong segmentation when working with my own DICOM file.</p>
<p>I add the file, then open TotalSegmentator with the configs you can see there. What can be happening? Thanks again for you huge contribution for this field.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18b34b3cedc05d2bf6c4ed9b6dacb118313254cf.jpeg" data-download-href="/uploads/short-url/3wvAS0QCLPqwscBIuI5QMzJYyIf.jpeg?dl=1" title="TotalSegmentator - CMF Wrong segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b34b3cedc05d2bf6c4ed9b6dacb118313254cf_2_690x354.jpeg" alt="TotalSegmentator - CMF Wrong segmentation" data-base62-sha1="3wvAS0QCLPqwscBIuI5QMzJYyIf" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b34b3cedc05d2bf6c4ed9b6dacb118313254cf_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b34b3cedc05d2bf6c4ed9b6dacb118313254cf_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18b34b3cedc05d2bf6c4ed9b6dacb118313254cf_2_1380x708.jpeg 2x" data-dominant-color="9E9EAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TotalSegmentator - CMF Wrong segmentation</span><span class="informations">1918×985 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #21 by @pieper (2022-12-21 12:36 UTC)

<p>That result looks reasonable.  There’s a big segment called ‘face’ at the front of the head.  My understanding is that this can be used to remove features that might otherwise identify the individual subject.  Removing these features makes it easier to share 3D data.</p>

---

## Post #22 by @Chop1n (2022-12-21 19:55 UTC)

<p>Thanks for your reply, Pieper!</p>
<p>I guess that CMF structures can’t be segmented due to data protection on the training process. I’m right?<br>
After reading your comment I have loaded different body CT scans and the result was good.</p>
<p>Hats off to the development team.</p>

---

## Post #23 by @pieper (2022-12-21 20:06 UTC)

<p>Right now there are no CMF-specific substructures included in the TotalSegmentator model.  There are dedicated models in development to subdivide the head into relevant anatomical regions.  Some of that work will be discussed during the upcoming <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/">Project Week</a>.</p>

---

## Post #24 by @abertelsen (2022-12-22 10:25 UTC)

<p>Truly amazing! Thanks for sharing this!</p>

---

## Post #25 by @lassoan (2022-12-28 13:18 UTC)

<p>6 posts were split to a new topic: <a href="/t/error-while-installing-pytorch/26956">Error while installing pytorch</a></p>

---

## Post #26 by @R.Boellaard (2022-12-28 13:30 UTC)

<p>After installing the totalsegmentor and trying to run it by pressing apply, i got a message that pytorch will be installed in several minutes. However, after one hour it is still not proceeding. Does anyone have a suggestion what might go wrong?</p>

---

## Post #27 by @Anish_Raj (2022-12-28 13:39 UTC)

<p>It works for some of my CT data, for other i get this error:<br>
Traceback (most recent call last):<br>
File “E:\apps\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “E:/apps/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 258, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “E:/apps/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 715, in process<br>
self.logProcessOutput(proc)<br>
File “E:/apps/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 624, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘E:/apps/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘E:\apps\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/ar38/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_14+33+20.804/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/ar38/AppData/Local/Temp/Slicer/__SlicerTemp__2022-12-28_14+33+20.804/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Do you know what is the reason for this? Thanks in advance</p>

---

## Post #28 by @Aoz (2022-12-28 16:01 UTC)

<p>Hi!<br>
Amazing work, thanks for sharing such a powerful tool.<br>
Any plan to add the shoulder rotator cuff muscles one day?</p>

---

## Post #29 by @rbumm (2022-12-28 16:05 UTC)

<p>This is could indicate GPU memory issues on a big dataset. Please check the content of the console output window for additional information.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c74edab685a6979581383246f2572b4b06809f91.png" alt="image" data-base62-sha1="sr9XB9U9C5QLwQczKtQ4zaTna93" width="532" height="224"></p>
<p>What is your GPU memory size?</p>

---

## Post #30 by @Anish_Raj (2022-12-28 16:12 UTC)

<p>I have a 4gb gpu. Surprising thing is it works for a bigger file. Any suggestions?</p>

---

## Post #31 by @pieper (2022-12-28 16:18 UTC)

<aside class="quote no-group" data-username="Aoz" data-post="28" data-topic="26710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/d9b06d/48.png" class="avatar"> Aoz:</div>
<blockquote>
<p>Any plan to add the shoulder rotator cuff muscles one day?</p>
</blockquote>
</aside>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> pointed out, this is a Slicer wrapper around <a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a>, which itself uses <a href="https://github.com/MIC-DKFZ/nnUNet">nnUNet</a>, both of which are fairly new and being actively developed.  So we can hope for continued improvement (higher resolution, more segments, etc).  Both projects are open source, so it’s also possible to contribute directly to them to build momentum, or even just congratulate the developers directly.</p>
<p>Note that we also work with the MONAI Label application, which is also very powerful and can be used to train new segments using the Slicer extension.  These are exciting times as automatic segmentation is (finally) evolving rapidly into useful tools.</p>

---

## Post #32 by @rbumm (2022-12-28 16:19 UTC)

<p>We know that the creators are working on including subcutaneous fat, the sternum bone, costovertebral connectors, and vessels. You may ask about specific structures in the <a href="https://github.com/wasserth/TotalSegmentator/issues/1">TotalSegmentator GitHub Usage Issue</a> and you could even train the software yourself or provide ground truth data to the creators because all training data are disclosed.</p>

---

## Post #33 by @rbumm (2022-12-28 16:27 UTC)

<p>4 GB GPU memory is on the very low side of system requirements. See <a href="https://github.com/wasserth/TotalSegmentator#resource-requirements">more details here</a>.<br>
So more GPU memory and RAM should help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #34 by @lassoan (2022-12-28 17:28 UTC)

<aside class="quote no-group" data-username="Anish_Raj" data-post="30" data-topic="26710" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anish_raj/48/13980_2.png" class="avatar"> Anish_Raj:</div>
<blockquote>
<p>I have a 4gb gpu. Surprising thing is it works for a bigger file. Any suggestions?</p>
</blockquote>
</aside>
<p>Minimum GPU memory requirement is 7GB.below that the segmentation may randomly fail on some data sets. For predictable outcomes, you need to <a href="https://github.com/lassoan/SlicerTotalSegmentator#segmentation-fails-while-predicting">switch to using CPU</a> or upgrade your GPU.</p>
<aside class="quote no-group" data-username="Aoz" data-post="28" data-topic="26710">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/d9b06d/48.png" class="avatar"> Aoz:</div>
<blockquote>
<p>rotator cuff muscles</p>
</blockquote>
</aside>
<p>Rotator cuff muscle injuries are so common that I’m sure there is enough interest in adding I to the TotalSegmentator model. If you segment this muscle on the TotalSegmentator datasets (they are all publicly available) and send them to Jakob Wassrthal (main developer of the TotalSegmentator model) then he will add it to the model.</p>
<p>Segmentation of a muscle in 2000 images may seem like a big effort, but if the muscle is well visible in CTs then it could be a very doable. You can use TotalSegmentator to segment each image then extract the relevant ROI based on the segmentation results (e.g., bounding box defined by a couple of segments). After that you can use MONAILabel to segment the muscle in each extracted image region. MONAILabel allows you to segment with adaptive learning, which means that you only need to segment a few dozen images from scratch, for the remaining you can get an automatic segmentation result that you just need to verify and fix up as needed. The automatic segmentation result will improve continuously with each completed case, so you should be able to finish the segmentation fairly quickly.</p>

---

## Post #35 by @Atena90 (2022-12-29 15:11 UTC)

<p>Awesome,<br>
I am wondering if I can have chest wall and para spinal muscles segmentation by TotalSegmentator?</p>

---

## Post #36 by @lassoan (2022-12-29 15:53 UTC)

<p>Similar/nearby structures around the chest wall and para spinal muscles are already segmented. Can you derive sufficient information from those? What is your clinical application?</p>
<p>In general the same answers apply to segmentation of any additional structure as given for the rotator cuff muscle question above, i.e., you need to segment a number of cases with manual/semi-automatic/adaptive learning tools and then that can be used to extend TotalSegmentator.</p>

---

## Post #37 by @Atena90 (2022-12-29 16:06 UTC)

<p>Thank you for replying.<br>
I found paraspinal muscles segmentations.<br>
I`ll try for the rest of muscles what you explained for Rotator Cuff.</p>

---

## Post #38 by @LipTeck_Chew (2023-01-06 06:04 UTC)

<p>Hi Lassoan,</p>
<p>Very impressive work! Are you able to add option to smooth all the contours generated via fast option? Hoping this can reduce the jaggies?</p>
<p>Thanks,<br>
LipTeck</p>

---

## Post #39 by @lassoan (2023-01-06 06:12 UTC)

<p>Yes, you can apply smoothing in Segment Editor. However, that would not make the segmentation more accurate, so I would not recommend doing it (unless you just want to improve the look of the segmentation). If you want better image quality but you don’t have a GPU then you can get the full quality segmentation in 30-40 minutes on the CPU. It is fully automatic, so you just start it and it runs in the background.</p>

---

## Post #40 by @lassoan (2023-01-09 14:10 UTC)

<p>7 posts were split to a new topic: <a href="/t/totalsegmentator-failed-to-compute-results-file-not-found/27129">TotalSegmentator failed to compute results - file not found</a></p>

---

## Post #44 by @lassoan (2023-01-09 14:18 UTC)

<p>A post was merged into an existing topic: <a href="/t/totalsegmentator-failed-to-compute-results-file-not-found/27129/9">TotalSegmentator failed to compute results - file not found</a></p>

---

## Post #47 by @lassoan (2023-04-05 20:00 UTC)

<p>3 posts were split to a new topic: <a href="/t/convert-totalsegmentator-results-to-rt-structure-set/28767">Convert TotalSegmentator results to RT structure set</a></p>

---

## Post #50 by @lassoan (2023-04-05 20:01 UTC)

<p>2 posts were split to a new topic: <a href="/t/totalsegmentator-results-computed-in-fast-mode-are-rough/28768">TotalSegmentator results computed in fast mode are rough</a></p>

---

## Post #52 by @Xavier_Tre (2023-01-30 04:24 UTC)

<p>Hello, I have problems to install totalsegmentator, already I have read the document several times where, and I have made several attempts to install it without results. Can someone explain to me how to install it? a tutorial video?</p>

---

## Post #53 by @lassoan (2023-01-30 07:55 UTC)

<p>Please describe what you did, what you expected to happen, and what happened instead. Include screenshots and copy here all messages displayed in the log window of the TotalSegmentator module.</p>

---

## Post #54 by @lassoan (2023-02-06 14:53 UTC)

<p>5 posts were split to a new topic: <a href="/t/segment-the-body-surface-using-stotalsegmentator/27666">Segment the body surface using sTotalSegmentator</a></p>

---

## Post #55 by @lassoan (2023-02-15 03:30 UTC)

<p>A post was split to a new topic: <a href="/t/export-totalsegmentator-results-to-dicom/27815">Export TotalSegmentator results to DICOM</a></p>

---

## Post #56 by @zhang_ming (2023-02-20 12:18 UTC)

<p>Will this plugin use our local weights to compute(refined or trained by my local dataset), and  the weights uploaded to googledrive for users to download</p>

---

## Post #57 by @lassoan (2023-04-05 19:58 UTC)

<p>2 posts were split to a new topic: <a href="/t/totalsegmentator-indicates-that-gtx-1060-gpu-has-not-enough-memory/28766">TotalSegmentator indicates that GTX 1060 GPU has not enough memory</a></p>

---

## Post #60 by @lassoan (2023-04-05 19:56 UTC)

<p>2 posts were split to a new topic: <a href="/t/can-totalsegmentator-capture-deformities-such-as-can-totalsegmentator-heterotopic-ossification/28765">Can TotalSegmentator capture deformities such as Can TotalSegmentator heterotopic ossification?</a></p>

---

## Post #62 by @lassoan (2023-08-09 17:42 UTC)

<p>A post was split to a new topic: <a href="/t/run-totalsegmentator-on-multivolume/31073">Run TotalSegmentator on MultiVolume</a></p>

---

## Post #63 by @Julius_W (2023-10-12 13:00 UTC)

<p>Congratulation for implementing TotalSegmentator to Slicer. I use Slicer to segment bones of the lower extremities and wondered, if you are planning on implementing the v2.0 of TotalSegmentator as well? I would greatly appreciate this work as the segmentation of the lower extremity is enabled in this version.</p>
<p>Thank you very much<br>
Julius</p>

---

## Post #64 by @rbumm (2023-10-12 15:44 UTC)

<p>Yes, it is planned to implement TotalSegmentator v2 as soon as possible.</p>

---

## Post #65 by @lassoan (2023-10-13 16:54 UTC)

<p>We have a functional prototype in this <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/38">pull request</a> of TotalSegmentator v2 in Slicer. We need to tune a few small things before we release it, probably in a week or so. If you don’t want to wait for that then you can get the updated TotalSegmentator.py and .ui files from github and overwrite the files in your Slicer installation folder.</p>

---

## Post #66 by @Julius_W (2023-10-17 11:17 UTC)

<p>That’s great thank you!</p>

---

## Post #67 by @lassoan (2024-01-12 04:44 UTC)

<p>A post was split to a new topic: <a href="/t/segmenting-fractured-bones/33746">Segmenting fractured bones</a></p>

---

## Post #68 by @Luca1 (2024-01-18 16:29 UTC)

<p>Is there any chance to use “total segmentator” with cone beam CT acquired with angiography systems in the body (liver)? Thanks</p>

---

## Post #69 by @lassoan (2024-01-18 16:44 UTC)

<p>Yes, it works on CBCT images as well. However, if the image quality is very bad (which is not uncommon, especially for low-dose acquisitions) then the accuracy will suffer.</p>

---

## Post #70 by @Tobias (2024-02-11 20:23 UTC)

<p>Hi,<br>
I am trying to make it run and when I look in pytorch utils it said torch version 1.8.1<br>
However, when i run the totalsegmentator it says that it needs to install a higher version of torch (1.12.1) and restart. And then it restarts but nothing happens.<br>
Does anyone have any idea what I am doing wrong?</p>

---

## Post #71 by @lassoan (2024-02-12 03:03 UTC)

<p>You have some old pytorch 1.x version in your pip cache that gets installed by default.</p>
<p>You can go to Pytorch Utils module, uninstall this old version, restart Slicer, go to Pytorch Utils module again, and before you click to install Pytorch, write <code>&gt;=2</code> in the version requirement textbox.</p>
<p>These uninstall and install steps should be performed automatically if you use the latest Slicer Stable Release or latest Slicer Preview Release.</p>

---

## Post #72 by @Sandra_Garcia (2024-06-19 08:58 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> I have a quick question.</p>
<p>I am interested in conducting an experimental campaign on the functionality of TotalSegmentator. For this purpose, I want to modify some parameters and compare the results obtained. I have tried to make modifications from within the program, but regarding segmentation, it is practically impossible to change anything. Therefore, I wanted to ask if there are parameters in the program’s code that can be modified to obtain different results from the same data set. For example, changing the resolution, edge detection, or something like that. If you have any ideas on how I can achieve this, I would greatly appreciate it. It doesn’t have to be something complex, just to be able to compare various results. Thank you in advance for your response.</p>
<p>Using CT images.</p>
<p>Thank you in advance for your response</p>

---

## Post #74 by @lassoan (2024-06-19 11:47 UTC)

<p>The result is anyways resampled in the end to the input image resolution, so if you want to change that then you can resample the input image before running TotalSegmentator.</p>
<p>This will not change things fundamentally, as the internal segmentation model had fixed resolution. You would need to retrain the entire model on higher-resolution data to get finer details.</p>

---

## Post #75 by @carl (2025-01-07 07:59 UTC)

<p>Hi,<br>
has anyone tried this with situs inversus or situs ambiguus patients?<br>
i will give that a try on a mac studio. No idea if the M4 is supported.</p>

---

## Post #76 by @lassoan (2025-01-07 17:06 UTC)

<p>The model may work perfectly on these anatomical variations (it can even segment some structures in various animal images). Please try it and let us know.</p>
<p>All AI segmentation tools should work on macOS, they are just slower than on systems that have a discrete GPU (TotalSegmentator may take 5-10 minutes instead of 30 seconds).</p>

---

## Post #77 by @lassoan (2025-05-03 14:38 UTC)

<p>A post was split to a new topic: <a href="/t/what-modalities-and-protocols-totalsegmentator-works-with/42779">What modalities and protocols TotalSegmentator works with?</a></p>

---
