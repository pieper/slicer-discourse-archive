# Elastix registration fails: Too many samples map outside moving image buffer

**Topic ID**: 15798
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/elastix-registration-fails-too-many-samples-map-outside-moving-image-buffer/15798

---

## Post #1 by @DAT_Minh (2021-02-02 15:50 UTC)

<p>Dear Andras <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
I’m segmenting temporal bone using ABL Temporal Bone Segmentation. I stuck at step 2: Rigid registration. When I apply Rigid registration, the process stopped at 14% and it said: “command ‘elastix’ returned non-zero exit status 1”. I’ve installed SlicerElastix, Slicer version 4.11.20200930. Thanks in advance<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba38fdd57c2d745680abf78370781d94dd775175.png" data-download-href="/uploads/short-url/qzoUCLS55DKz85yi9QQYNB88l13.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba38fdd57c2d745680abf78370781d94dd775175.png" alt="image" data-base62-sha1="qzoUCLS55DKz85yi9QQYNB88l13" width="499" height="500" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">597×598 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Best,<br>
Dat</p>

---

## Post #2 by @lassoan (2021-02-02 16:41 UTC)

<p>Do you see any details about the error in the application log?</p>

---

## Post #3 by @DAT_Minh (2021-02-02 23:01 UTC)

<p>Here it is <a class="mention" href="/u/lassoan">@lassoan</a>. Lots of thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cf569154e0b0a3e77edc440e92eb25421ed4d96.png" data-download-href="/uploads/short-url/8Hgr8K3AMj8FpMeeTlphfOSkY7Q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cf569154e0b0a3e77edc440e92eb25421ed4d96_2_690x223.png" alt="image" data-base62-sha1="8Hgr8K3AMj8FpMeeTlphfOSkY7Q" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cf569154e0b0a3e77edc440e92eb25421ed4d96_2_690x223.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cf569154e0b0a3e77edc440e92eb25421ed4d96_2_1035x334.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cf569154e0b0a3e77edc440e92eb25421ed4d96_2_1380x446.png 2x" data-dominant-color="E7EBF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1894×613 25.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @DAT_Minh (2021-02-02 23:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/357d9bada86947674dc938fd9a8e4292fe7ce9c0.png" data-download-href="/uploads/short-url/7Dcq2OpN5dC2GVjK6HMMb0Wlboc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/357d9bada86947674dc938fd9a8e4292fe7ce9c0_2_690x128.png" alt="image" data-base62-sha1="7Dcq2OpN5dC2GVjK6HMMb0Wlboc" width="690" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/357d9bada86947674dc938fd9a8e4292fe7ce9c0_2_690x128.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/357d9bada86947674dc938fd9a8e4292fe7ce9c0_2_1035x192.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/357d9bada86947674dc938fd9a8e4292fe7ce9c0_2_1380x256.png 2x" data-dominant-color="ECECF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1885×351 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e2a104df9fe637a40dc98c77fc94d6454d0d0a3.png" data-download-href="/uploads/short-url/i06hvdU1fqiF8pbWg5StrLJhKpR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e2a104df9fe637a40dc98c77fc94d6454d0d0a3_2_690x65.png" alt="image" data-base62-sha1="i06hvdU1fqiF8pbWg5StrLJhKpR" width="690" height="65" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e2a104df9fe637a40dc98c77fc94d6454d0d0a3_2_690x65.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e2a104df9fe637a40dc98c77fc94d6454d0d0a3_2_1035x97.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e2a104df9fe637a40dc98c77fc94d6454d0d0a3_2_1380x130.png 2x" data-dominant-color="F5F5FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1893×180 8.83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b88580d6baf45707cfc4549c941537e233715cfb.png" data-download-href="/uploads/short-url/qklSO99oJNeORaTRKpe2gO9QJn5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b88580d6baf45707cfc4549c941537e233715cfb_2_690x110.png" alt="image" data-base62-sha1="qklSO99oJNeORaTRKpe2gO9QJn5" width="690" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b88580d6baf45707cfc4549c941537e233715cfb_2_690x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b88580d6baf45707cfc4549c941537e233715cfb_2_1035x165.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b88580d6baf45707cfc4549c941537e233715cfb_2_1380x220.png 2x" data-dominant-color="EDEDF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1893×302 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-02-02 23:10 UTC)

<p>The messages are not visible in these screenshots. Instead of posting pictures, could you copy here the log message text (in menu: Help / Report a bug)? Thank you.</p>

---

## Post #6 by @DAT_Minh (2021-02-05 12:53 UTC)

<p>Dear Andras. Here is the message log. It’s too long. I’ve deleted some parts. Please take a look at it. Thank you very much.</p>
<p>“ABLTemporalBoneSegmentationModule”<br>
[INFO][Python] 05.02.2021 19:34:26 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) - Stopping condition: Error in metric.</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Stopping condition: Error in metric.</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Stopping condition: Error in metric.</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) - Settings of AdaptiveStochasticGradientDescent in resolution 0:</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Settings of AdaptiveStochasticGradientDescent in resolution 0:</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) - Description: itk::ERROR: itk::ERROR: AdvancedMattesMutualInformationMetric(000002BF54164290): Too many samples map outside moving image buffer: 188 / 1117</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Description: itk::ERROR: itk::ERROR: AdvancedMattesMutualInformationMetric(000002BF54164290): Too many samples map outside moving image buffer: 188 / 1117</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Description: itk::ERROR: itk::ERROR: AdvancedMattesMutualInformationMetric(000002BF54164290): Too many samples map outside moving image buffer: 188 / 1117</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) - Error occurred during actual registration.</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Error occurred during actual registration.</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Error occurred during actual registration.</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) -</p>
<p>[INFO][Python] 05.02.2021 19:34:27 [Python] (C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py:392) - Errors occurred!</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Errors occurred!</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Errors occurred!</p>
<p>[INFO][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Error: Command ‘elastix’ returned non-zero exit status 1.</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - File “C:/Users/USER/AppData/Roaming/NA-MIC/Extensions-29402/ABLTemporalBoneSegmentation/lib/Slicer-4.11/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py”, line 635, in process_transform</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - output = function()</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - File “C:/Users/USER/AppData/Roaming/NA-MIC/Extensions-29402/ABLTemporalBoneSegmentation/lib/Slicer-4.11/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py”, line 812, in transform</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - log_callback=self.update_rigid_progress)</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - File “C:/Users/USER/AppData/Roaming/NA-MIC/Extensions-29402/ABLTemporalBoneSegmentation/lib/Slicer-4.11/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py”, line 1318, in apply_elastix_rigid_registration</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - movingVolumeMaskNode=mask_node</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - File “C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py”, line 807, in registerVolumes</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - self.logProcessOutput(ep)</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - File “C:\Users\USER\AppData\Roaming\NA-MIC\Extensions-29402\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Elastix.py”, line 728, in logProcessOutput</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - raise subprocess.CalledProcessError(return_code, “elastix”)</p>
<p>[CRITICAL][Stream] 05.02.2021 19:34:27 [] (unknown:0) - subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 1.</p>

---

## Post #7 by @lassoan (2021-02-05 15:35 UTC)

<aside class="quote no-group" data-username="DAT_Minh" data-post="6" data-topic="15798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dat_minh/48/9097_2.png" class="avatar"> DAT_Minh:</div>
<blockquote>
<p>Too many samples map outside moving image buffer: 188 / 1117</p>
</blockquote>
</aside>
<p>This is probably the most common image registration error and it means that the two volumes are too far from each other, so it is not possible to compute the similarity metric. This usually happens when the input images in their initial position do not sufficiently overlap (but rarely it can happen when the registration completely diverges).</p>
<p>One solution is to use an initialization step that automatically pre-aligns the input volumes. I think the default preset contains such a step (it uses center of gravity to align the position, maybe also moments to align the orientation), which works well if the two input volumes are cropped to approximately to the same region.</p>
<p>If automatic initialization fails then you can pre-align manually, using a very quick fiducial registration using 3-5 points.</p>

---

## Post #8 by @DAT_Minh (2021-02-06 11:29 UTC)

<p>Dear Andras. I used two methods of alignment shown in the yellow circle in the pictures attached. None of them work.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d690204f9d3556bbb3034e8bfa12cf63a99fdee1.jpeg" data-download-href="/uploads/short-url/uC6XZIbX4jN0SFg0dqgbpGPuY93.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d690204f9d3556bbb3034e8bfa12cf63a99fdee1_2_262x500.jpeg" alt="image" data-base62-sha1="uC6XZIbX4jN0SFg0dqgbpGPuY93" width="262" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d690204f9d3556bbb3034e8bfa12cf63a99fdee1_2_262x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d690204f9d3556bbb3034e8bfa12cf63a99fdee1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d690204f9d3556bbb3034e8bfa12cf63a99fdee1.jpeg 2x" data-dominant-color="565452"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">388×738 71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c47748a0d78a0a49ca1e65c5a78498e1e15c48c7.jpeg" alt="image" data-base62-sha1="s219cjHQyX10BuSH4vqnqsVfWWX" width="624" height="379"><br>
What do you mean by pre-align manually? Thank you.</p>

---

## Post #9 by @lassoan (2021-02-06 14:01 UTC)

<p>Zooming in/out the slice view (“Adjust the field of view…” button) does not change the images or their alignments. It has no effect on registration.</p>
<p>What you may need to do is to transform the image with manual or semi-automatic registration methods before running the automatic method; crop the images to the same region (not just zoom in the view but actually crop, using Crop volume module). See details <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">here</a>.</p>

---

## Post #10 by @DAT_Minh (2021-02-06 14:59 UTC)

<p>Thank you very much. I will try again.</p>

---

## Post #11 by @DAT_Minh (2021-02-06 17:09 UTC)

<p>Dear Andras, I have a few questions:<br>
I tried to pre-align the Left temporal volume with Atlas_L volume. In the ABL temporal bone segmentation module, Atlas_L exist as a volume (picture):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ed2c4be7e9649e86db5b61041267e12fde74a0.jpeg" data-download-href="/uploads/short-url/4YYnf1jz4EfRst2KC0nSrJlsYFO.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22ed2c4be7e9649e86db5b61041267e12fde74a0_2_543x500.jpeg" alt="image.jpg" data-base62-sha1="4YYnf1jz4EfRst2KC0nSrJlsYFO" width="543" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22ed2c4be7e9649e86db5b61041267e12fde74a0_2_543x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ed2c4be7e9649e86db5b61041267e12fde74a0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ed2c4be7e9649e86db5b61041267e12fde74a0.jpeg 2x" data-dominant-color="A7A5A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">623×573 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I turned to Data module, Atlas_L module does not appear as a volume, but CochleaRegistrationMask_L. When I toggle off CochleaRegistrationMask_L volume, Atlas_L turns on and reverse.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a93068295f53c1e73a3cd36766f0392b5c814bf.jpeg" alt="image.jpg" data-base62-sha1="cVfYjIxAmDtwincgSE2Hg7kkTHV" width="562" height="214"><br>
The CochleaRegistrationMask_L volume appeared to be blanked</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e71a5065f42c78a7b33b21e0502cd7c4e1506a91.png" alt="image.png" data-base62-sha1="wYqFK50xeR79R5xH0goQqZEbUnn" width="562" height="194"></p>
<p>I tried to register Left temporal volume with CochleaRegistrationMask_L volume (the latter is supposed to be Atlas_L volume, however, Atlas_L didn’t appear as a volume in Data) using Landmarks registration, CochleaRegistrationMask_L volume is completely black.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1999b25f593e476f3683f6bd623f282f45502ef.jpeg" alt="image.jpg" data-base62-sha1="pl7BVpuoR7rDPFiBQRE3uq1oaQv" width="562" height="316"></p>
<p>So my question is: which volume to register with? Why the Atlas_L volume does not appear in Data module? Lots of thanks for your help.</p>

---

## Post #12 by @lassoan (2021-02-06 17:47 UTC)

<p>When the slice view is all black then it means that it shows a region that is outside the volume’s region. Landmark registration module is good for refining alignment when two volumes are already approximately aligned. You can use Fiducial Registration Wizard module to align volumes that are very far from each other.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> It would be great if you could update Landmark Registration module to allow independent point placement on the two volumes (this is particularly important for the first point, and if orientation is very different then for the first 3 points), because if the two volumes are at very different places then the current module is not usable by itself.</p>

---

## Post #13 by @DAT_Minh (2021-02-07 10:15 UTC)

<p>Dear Andras. Which volume to pre-align left temporal volume with (Atlas_L or CochleaRegistrationMask_L volume) before doing rigid registration in ABL temporal bone segmentation module? Does it mean that we have to register the input image twice in order the computer to understand?<br>
Atlas_L volume is not shown in Data. I can’t pre-register input volume with it<br>
I still can’t see the solution. Please help. Can you do an example. Thanks.</p>

---

## Post #14 by @bonniezyao (2022-08-30 18:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="15798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>fiducial</p>
</blockquote>
</aside>
<p>Hi.<br>
I have been using elastix via the command line package trying to register two stacks of images (mice brain serial imaging). I was able to use affine transform between my datasets. And I want to use a bspline transformation to obtain more precise registration with sub-regions. I encountered the same error message as this thread, even though the fixed image is the result from the affine transformation.<br>
I was wondering if I could do anything like the suggested manual alignment with the command line package, or should I use 3D slicer for this?</p>
<p>Thanks!<br>
Bonnie Zhiyi Yao</p>
<p>Command window:<br>
itk::ExceptionObject (0x556ff4159750)<br>
Location: “ElastixTemplate - Run()”<br>
File: /home/niels_dekker/dev/src/elastix/Common/CostFunctions/itkAdvancedImageToImageMetric.hxx<br>
Line: 1006<br>
Description: itk::ERROR: itk::ERROR: AdvancedMattesMutualInformationMetric(0x556ff411dd70): Too many samples map outside moving image buffer: 621 / 3000</p>
<p>Error occurred during actual registration.</p>

---

## Post #15 by @lassoan (2022-08-30 18:51 UTC)

<p>This error message means that the two input images do not overlap sufficiently enough. Make sure you harden the transform on the input images before starting the registration.</p>

---

## Post #16 by @bonniezyao (2022-08-30 20:41 UTC)

<p>That’s a feature only available in the 3D slicer software, and is not a command line option, correct? I think since I used the constructed images from the affine transformation, the original nodes information wouldn’t be involved?</p>
<p>Thanks for the speedy reply!</p>

---

## Post #17 by @bonniezyao (2022-08-30 21:08 UTC)

<p>Actually, I didn’t have the correct output files as the moving image. Problem solved! Thank you again!</p>

---

## Post #18 by @lassoan (2022-08-30 21:10 UTC)

<p>Hardening an affine transform on an image is a one-click operation in Slicer. It is also available via Python scripting (and since you can run Python commands via command line, the feature is available from the console, too).</p>

---

## Post #19 by @evan (2022-12-10 00:00 UTC)

<p>Thank you to everyone who contributed on this thread and for the work of <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>I will be using the following GitHub Issue to track the issue that <a class="mention" href="/u/dat_minh">@DAT_Minh</a> mentioned:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/8">
  <header class="source">

      <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/8" target="_blank" rel="noopener nofollow ugc">github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/8" target="_blank" rel="noopener nofollow ugc">Elastix compatibility "Too many samples map outside moving image buffer"</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-30" data-time="18:47:14" data-timezone="UTC">06:47PM - 30 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/young-oct" target="_blank" rel="noopener nofollow ugc">
          <img alt="young-oct" src="https://avatars.githubusercontent.com/u/61168470?v=4" class="onebox-avatar-inline" width="20" height="20">
          young-oct
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I was excited when I found out about this module, and thank you for all your wor<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">k. Currently I'm stuck at step 2 and I got the error message saying: 
"command elsatix return to non-zero exit status 1 error."

&lt;img width="1503" alt="Screenshot 2022-11-30 at 14 18 11" src="https://user-images.githubusercontent.com/61168470/204880516-399145d8-ca63-4acb-aed8-c750e1a850d9.png"&gt;

Any help is greatly appreciated. 
@ben-connors @jamesobutler @e-simpson</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
