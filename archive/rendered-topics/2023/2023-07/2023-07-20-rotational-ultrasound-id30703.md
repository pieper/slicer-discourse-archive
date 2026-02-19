---
topic_id: 30703
title: "Rotational Ultrasound"
date: 2023-07-20
url: https://discourse.slicer.org/t/30703
---

# Rotational Ultrasound

**Topic ID**: 30703
**Date**: 2023-07-20
**URL**: https://discourse.slicer.org/t/rotational-ultrasound/30703

---

## Post #1 by @shabopbop (2023-07-20 12:57 UTC)

<p>Hey all, I am pretty new to 3D slicer, so I apologize if someone has answered my question before. Essentially, I have taken a rotational ultrasound around a fixed point and I am trying to recreated a 3D model based on this alone. Does anyone know it is possible for 3D slicer can produce a model from something like this? My issue is that the program view my rotational scan as a horizontal scan (through one dimensional plane). I feel like if I could make 3D slicer fixate potentially on a pixel that I know the ultrasound rotates around and spit out a model as if it was reading the base of a cone… maybe it could work? Regardless, does anyone have any ideas/extensions/anything that could be of help? Also my ability to code things is pretty poor… ='(</p>
<p>Thank you in advance!</p>

---

## Post #2 by @lassoan (2023-07-20 14:17 UTC)

<p>SlicerIGT extension’s Volume reconstruction module is developed for this purpose. See for example this demo:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="hIxr9OKBvQ8" data-video-title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=hIxr9OKBvQ8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/hIxr9OKBvQ8/maxresdefault.jpg" title="Reconstruct 3D or 4D cardiac volumes from sparse 2D frame set" width="" height="">
  </a>
</div>

<p>If your ultasound image sequence does not contain position and orientation information for each frame (which is usually the case) then you can use <a href="https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598/10">this script</a> to add that information and reconstruct the volume.</p>
<p>The script assumes that the ultrasound image sequence is loaded as a 3D volume (each time point is a frame of the volume), so you may either need to load the ultrasound image with enabling <code>Advanced</code> option in DICOM module and choose the <code>Scalar Volume</code> reader; or modify the script sothat it uses a volume sequence as input (the script will be somewhat simpler, as you don’t need to create a new sequence, just modify volumes in the sequence).</p>

---

## Post #3 by @shabopbop (2023-07-21 05:34 UTC)

<p>Thank you for your help! I am still running into some issues. I don’t exactly know if it is because I am using a stack of png files instead of dicom, or if I am not utilizing the right combination of extensions, or if it is something else entirely. But, I am getting this error back when I try to implement the script you linked:</p>
<p>Mixed Content: The page at ‘<a href="https://extensions.slicer.org/catalog/All/31382/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>’ was loaded over HTTPS, but requested an insecure image ‘<a href="http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png" rel="noopener nofollow ugc">http://www.slicer.org/slicerWiki/images/b/bc/BaselineFollowupSCANRegisteredCMFreg2.png</a>’. This content should also be served over HTTPS.</p>
<p>Sometimes, it has caused slicer to crash entirely.</p>

---

## Post #4 by @lassoan (2023-07-21 11:52 UTC)

<p>The <code>Mixed Content:...</code> messages are just warnings that the extension icons are stored on a non-https server. You can ignore them.</p>
<p>Starting from pngs should not be a problem at all. Then the <a href="https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598/10">script</a> should be usable as is. Use the latest Slicer Stable Release and if you encounter any issues then let me know. Provide enough details that allows me to reproduce what you do.</p>

---

## Post #5 by @shabopbop (2023-07-21 16:17 UTC)

<p>I will try to outline what I have done so far so I can hopefully provide more insight to what I am doing. So, I upload my ultrasound .png’s into 3D Slicer with the ‘Add Data’ widget, and once loaded, I open the Python Console in the Slicer program and paste the script you posted in these responses. I have the extensions downloaded and enabled as well (SlicerIGSIO and SlicerIGT).</p>
<p>If I past the script alone without adding my images, it provides an attribute error (assuming because there is no image to obtain data from). And when I post the script after adding my images, my slicer program usually crashes. A couple times it gave an attribute error as well, to which I tried using DICOM files but my DICOM files aren’t compatible with Slicer at the moment.</p>
<p>I am sorry if this isn’t too helpful =( I can post images of what I am doing as well if that would be helpful in any way.</p>

---

## Post #6 by @lassoan (2023-07-21 17:07 UTC)

<p>Does the application actually crash or just hangs (does not respond while performing computations)? If it actually crashes then most likely you run out of memory due to non-optimal reconstruction parameters.</p>
<p>You can run the code in smaller chunks to see what line does not succeed and if you get any error messages. If you get any error message then it is not enough to tell us that you got some error messages, but copy here the complete message. Maybe also attach a few screenshots (that allows us to see what kind of images you work with, what Slicer version you are using, what operating system, etc. and we might notice something unusual that could help us determine what needs to be done).</p>
<p>It could also help if you could share your data set (upload somewhere and post the link). You can use Crop volume module to cut off patient information from the images (if they are burned into the image corner).</p>

---

## Post #7 by @shabopbop (2023-07-21 20:22 UTC)

<p>Yeah, the application crashes fully where it is forcefully shut down and I have to reopen the application. I am using Slicer version 5.2.2 on windows 10. I am posting screenshots below, but my work flow is that we have a video recording of the US, I extracted all the frames from the video and made those frames into png files. Then I uploaded the files into slicer. Eventually, my images will be cropped in a way so that only the tissue will be present and none of the UI portions of the ultrasound program that was also recorded.</p>
<p>I ran the code in smaller chunks/ individual lines without any errors until I input line 79 (slicer.modules.volumereconstruction.logic().ReconstructVolumeFromSequence(volumeReconstructionNode)) where it crashes the program. I also notice that I am receiving notification that my scalar component is 0, which I do not know if this is something I need to worry about.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f4b130c4cd87dc7eeaaff281f5cc7141dff6221.png" data-download-href="/uploads/short-url/2bi0vDBJCKTRLC5ts6S8WeMYNHj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4b130c4cd87dc7eeaaff281f5cc7141dff6221_2_690x388.png" alt="image" data-base62-sha1="2bi0vDBJCKTRLC5ts6S8WeMYNHj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4b130c4cd87dc7eeaaff281f5cc7141dff6221_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4b130c4cd87dc7eeaaff281f5cc7141dff6221_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f4b130c4cd87dc7eeaaff281f5cc7141dff6221_2_1380x776.png 2x" data-dominant-color="303038"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aefd9623a8a8ae48a645344d242fbad63c9d55e6.png" data-download-href="/uploads/short-url/oY2nXhnRUhEXRMWYUfd0SqdyZca.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefd9623a8a8ae48a645344d242fbad63c9d55e6_2_690x388.png" alt="image" data-base62-sha1="oY2nXhnRUhEXRMWYUfd0SqdyZca" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefd9623a8a8ae48a645344d242fbad63c9d55e6_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefd9623a8a8ae48a645344d242fbad63c9d55e6_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aefd9623a8a8ae48a645344d242fbad63c9d55e6_2_1380x776.png 2x" data-dominant-color="2D2D33"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2023-07-22 12:09 UTC)

<aside class="quote no-group" data-username="shabopbop" data-post="7" data-topic="30703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shabopbop/48/66886_2.png" class="avatar"> shabopbop:</div>
<blockquote>
<p>I am receiving notification that my scalar component is 0</p>
</blockquote>
</aside>
<p>This can be the root cause of the error. Please provide the exact message.</p>
<p>Ankther possibility is that your run out of memory. This can happen because you do not crop your image and the full screen screenshot can be very large.</p>
<pre><code>outputSpacingMm = imageSpacingMm * 10.0
</code></pre>
<p>You can also crop the image inside Slicer by modifying extent after setting it:</p>
<pre><code class="lang-auto">extent = inputFrameVolume.GetExtent()
extent[0] = 5
extent[1] = 510
extent[2] = 50
extent[3] = 400
</code></pre>
<p>It seems that you want to rotate around the horizontal axis, so you need to set the rotation axis to:</p>
<pre><code>rotationAxis = [1, 0, 0]
</code></pre>

---

## Post #9 by @shabopbop (2023-07-22 22:13 UTC)

<p>So this is the output that I was referring to:</p>
<pre><code class="lang-auto"># Convert RGB/RGBA volume to grayscale volume
if inputFrameVolume.GetNumberOfScalarComponents() &gt; 1:
    componentToExtract = 0
    print(f"Using scalar component {componentToExtract} of the image")
    extract = vtk.vtkImageExtractComponents()
    extract.SetInputData(inputFrameVolume)
    extract.SetComponents(componentToExtract)
    extract.Update()
    inputFrameVolume = extract.GetOutput()
Using scalar component 0 of the image
</code></pre>
<p>I will also try to crop the images before hand</p>
<p>Slicer finally didn’t crash on me! So here is the error from that line before:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.modules.volumereconstruction.logic().ReconstructVolumeFromSequence(volumeReconstructionNode)

[Qt] int __cdecl ctkVTKAbstractView::resumeRender(void) Cannot resume rendering, pause render count is already 0!
</code></pre>

---

## Post #10 by @lassoan (2023-07-24 11:42 UTC)

<blockquote>
<p>Using scalar component 0 of the image</p>
</blockquote>
<p>This is not an error but a message that our script prints.</p>
<blockquote>
<p>[Qt] int __cdecl ctkVTKAbstractView::resumeRender(void) Cannot resume rendering, pause render count is already 0!</p>
</blockquote>
<p>This is a false alarm that is fixed in recent Slicer Preview Releases. You can ignore this message.</p>

---

## Post #11 by @shabopbop (2023-07-24 19:49 UTC)

<p>I started using the preview release and the script is working! I am getting closer to the image I am looking for and it is now rotation along the x axis. However I am stumped on how to align the axis along the center of the ultrasound image I want. It seems to be rotating along the bottom edge of the frame rather than the center (which makes a rainbow shape rather than a conical one).</p>
<p>I do want to thank you so much for the help thus far, there is absolutely no way I could have made it to this point without your help! <img src="https://emoji.discourse-cdn.com/twitter/face_holding_back_tears.png?v=12" title=":face_holding_back_tears:" class="emoji" alt=":face_holding_back_tears:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ab979afc7320a73d012ca52d4c835a3b842a3f3.png" data-download-href="/uploads/short-url/3OpNbulHc2qx5ZhEj2xkKXrixpx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab979afc7320a73d012ca52d4c835a3b842a3f3_2_690x388.png" alt="image" data-base62-sha1="3OpNbulHc2qx5ZhEj2xkKXrixpx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab979afc7320a73d012ca52d4c835a3b842a3f3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab979afc7320a73d012ca52d4c835a3b842a3f3_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1ab979afc7320a73d012ca52d4c835a3b842a3f3_2_1380x776.png 2x" data-dominant-color="3D4041"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 348 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2023-07-25 12:13 UTC)

<p>Nice progress.</p>
<aside class="quote no-group" data-username="shabopbop" data-post="11" data-topic="30703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shabopbop/48/66886_2.png" class="avatar"> shabopbop:</div>
<blockquote>
<p>I am stumped on how to align the axis along the center of the ultrasound image</p>
</blockquote>
</aside>
<p>The center of rotation position is specified here:</p>
<pre><code>centerOfRotationIJK = [(extent[0]+extent[1])/2.0, extent[2], 0]
</code></pre>
<p><code>extent[2]</code> means the top of the image along the J axis. You can replace it by <code>(extent[2]+extent[3])/2.0 </code> if you want to rotate around the J axis center.</p>

---

## Post #13 by @shabopbop (2023-09-13 00:47 UTC)

<p>Hello,</p>
<p>Just wanted to give you an update/reaffirm that what you sent over worked for me! And it works pretty well too, so I am attaching an image of what I am making a model of. It is supposed to be they human eye with different layers out lined (retina, sclera, tumor tissue in this example below).</p>
<p>A couple things I did notice while working on it. After the image manipulation, the resolution of the resulting images did decrease a fair amount. I was just curious, but is this unavoidable?</p>
<p>Also, I saved these models as a mrml file. But when I try to open the model in Slicer, my program crashes soon after it tries to load the model. Do you have any potential reason why or if this can be fixed? I don’t think there are any error codes after the crash that I can find at least. I would post the file here so you had an example, but it seems like I can’t do so.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1f66cf3cb0692c0d935bf7f85e174081d80a480.jpeg" data-download-href="/uploads/short-url/rFS7cFtbIfgkstxYrTwkb6cuVjO.jpeg?dl=1" title="tumor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1f66cf3cb0692c0d935bf7f85e174081d80a480_2_690x339.jpeg" alt="tumor" data-base62-sha1="rFS7cFtbIfgkstxYrTwkb6cuVjO" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1f66cf3cb0692c0d935bf7f85e174081d80a480_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1f66cf3cb0692c0d935bf7f85e174081d80a480_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1f66cf3cb0692c0d935bf7f85e174081d80a480_2_1380x678.jpeg 2x" data-dominant-color="5E6076"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tumor</span><span class="informations">1829×900 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @pieper (2023-09-13 18:17 UTC)

<p>These things (reduced resolution and crashing on reload) sound like bugs or maybe something related to your workflow that can be worked around.  Either way, it would be great if you could find a way to reproduce them with sharable data so they can be tracked down and fixed.</p>

---

## Post #15 by @shabopbop (2023-09-13 18:37 UTC)

<p>I don’t know if I can reproduce the bugs in a way that can be shared. However, I may be able to send my mrml files through this avenue that I am trying. I will see if this works.</p>
<p>If not, I can share my png files and outline the steps I do to produce the 3d model and see if anyone in the community can find the bugs/ workflow issues.</p>
<p><a href="https://drive.google.com/file/d/1NEn1O6xGfqHAq0UF11mWpWd759FLGMKH/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="" height="">tumor.mrml</a><br>
<a href="https://drive.google.com/file/d/1nFwM3gioJY--x8kFipls-S7inBsAXNWs/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://ssl.gstatic.com/docs/doclist/images/icon_10_generic_list.png" width="" height="">tumor.seq.mrb</a></p>

---

## Post #16 by @shabopbop (2023-09-13 23:18 UTC)

<p>I was able to load a different file onto 3d slicer, I didn’t have to use the mrml/seq.mrb files like I initially thought! (used the nrrd file instead). The resolution decreasing issue still stands but I can work with what I have now. Thanks to all who have helped!</p>

---

## Post #17 by @lassoan (2023-09-18 13:27 UTC)

<aside class="quote no-group" data-username="shabopbop" data-post="13" data-topic="30703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shabopbop/48/66886_2.png" class="avatar"> shabopbop:</div>
<blockquote>
<p>After the image manipulation, the resolution of the resulting images did decrease a fair amount</p>
</blockquote>
</aside>
<p>You can choose any resolution that is sufficient for your purpose and your computer can still handle, by adjusting <code>outputSpacingMm</code>. If you decrease the spacing a lot then you may need to enable hole filling (because the slices you paste become thinner).</p>

---

## Post #18 by @nunno (2024-01-16 04:14 UTC)

<p>Hello Andras.</p>
<p>This is Josh. I am currently working on the same project as shabopbop, and we are encountering a issue that we are not sure how to resolve.</p>
<p>There are two parts.</p>
<ol>
<li>When the flipper.py converts images from ijk to xyz dimension, certain region shows a misaligned center of axis rotation.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0767399db595ca57a4c3873d9375aad45a746d92.jpeg" data-download-href="/uploads/short-url/13uv3JbdVXW6qC6PLszCtA5iGH0.jpeg?dl=1" title="Screenshot 2023-11-10 at 2.19.35 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0767399db595ca57a4c3873d9375aad45a746d92_2_690x368.jpeg" alt="Screenshot 2023-11-10 at 2.19.35 AM" data-base62-sha1="13uv3JbdVXW6qC6PLszCtA5iGH0" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0767399db595ca57a4c3873d9375aad45a746d92_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0767399db595ca57a4c3873d9375aad45a746d92_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0767399db595ca57a4c3873d9375aad45a746d92_2_1380x736.jpeg 2x" data-dominant-color="504F55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-10 at 2.19.35 AM</span><span class="informations">2032×1084 330 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>this shift is a result of flipping along a false axis (yellow) and it needs to be fixed to flip along the true axis (red).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0accfb01e5f87e5ea799dbadec8dbbe083d9e8.png" data-download-href="/uploads/short-url/404vAOl17dgKVlnWmx9eeOAHZs4.png?dl=1" title="Screenshot 2023-11-10 at 2.27.18 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0accfb01e5f87e5ea799dbadec8dbbe083d9e8_2_690x333.png" alt="Screenshot 2023-11-10 at 2.27.18 AM" data-base62-sha1="404vAOl17dgKVlnWmx9eeOAHZs4" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c0accfb01e5f87e5ea799dbadec8dbbe083d9e8_2_690x333.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0accfb01e5f87e5ea799dbadec8dbbe083d9e8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0accfb01e5f87e5ea799dbadec8dbbe083d9e8.png 2x" data-dominant-color="423A38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-10 at 2.27.18 AM</span><span class="informations">757×366 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have identified that the value “2.12” from below determines the location of the axis.</p>
<p><span class="hashtag-raw">#Set</span> up frame geometry and rotation<br>
<span class="hashtag-raw">#centerOfRotationIJK</span> = [(extent[0]+extent[1])/2.0, extent[2], 0]<br>
<strong>centerOfRotationIJK = [(newExtent[0]+newExtent[1])/2.0, newExtent[2]+newExtent[3]/2.12, 0]</strong><br>
rotationAxis = [1, 0, 0]<br>
rotationDegreesPerFrame = 180.0/numberOfFrames</p>
<p>Here’s my question.<br>
Is it possible to automate estimation for this value for each image before executing the image flip to fix the misalignment?</p>
<ol start="2">
<li>When annotating the segments, I noticed that anatomical structures before the image flip is much clearer compared to post flip. Is it possible to edit the flip code such that we can annotate the structure first on the ijk images, then flip the annotation along with the pixels?</li>
</ol>

---

## Post #19 by @nunno (2024-01-17 16:19 UTC)

<p>Hello.</p>
<p>This is a follow up to the resolved thread “Rotational Ultrasound”</p>
<aside class="quote quote-modified" data-post="18" data-topic="30703">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/eada6e/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotational-ultrasound/30703/18">Rotational Ultrasound</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello Andras. 
This is Josh. I am currently working on the same project as shabopbop, and we are encountering a issue that we are not sure how to resolve. 
There are two parts. 

When the flipper.py converts images from ijk to xyz dimension, certain region shows a misaligned center of axis rotation.

 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0767399db595ca57a4c3873d9375aad45a746d92.jpeg" data-download-href="/uploads/short-url/13uv3JbdVXW6qC6PLszCtA5iGH0.jpeg?dl=1" title="Screenshot 2023-11-10 at 2.19.35 AM" rel="noopener nofollow ugc">[Screenshot 2023-11-10 at 2.19.35 AM]</a> 
this shift is a result of flipping along a false axis (yellow) and it needs to be fixed to flip along the true axis (red). 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c0accfb01e5f87e5ea799dbadec8dbbe083d9e8.png" data-download-href="/uploads/short-url/404vAOl17dgKVlnWmx9eeOAHZs4.png?dl=1" title="Screenshot 2023-11-10 at 2.27.18 AM" rel="noopener nofollow ugc">[Screenshot 2023-11-10 at 2.27.18…</a>
  </blockquote>
</aside>

<p>Can someone help me with this?</p>
<p>Thank you.</p>
<p>Josh</p>

---

## Post #20 by @lassoan (2024-01-17 17:20 UTC)

<aside class="quote no-group" data-username="nunno" data-post="18" data-topic="30703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/eada6e/48.png" class="avatar"> nunno:</div>
<blockquote>
<p>Is it possible to automate estimation for this value for each image before executing the image flip to fix the misalignment?</p>
</blockquote>
</aside>
<p>It seems that it could be quite easily annotated, for example by computing the center of gravity of the non-zero voxels in the purple region.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0ce2b1960906e4828def19a10cbad0c6fe503009.jpeg" data-download-href="/uploads/short-url/1PZpXhBesltJM573EIt85vEykEV.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0ce2b1960906e4828def19a10cbad0c6fe503009_2_690x331.jpeg" alt="image" data-base62-sha1="1PZpXhBesltJM573EIt85vEykEV" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0ce2b1960906e4828def19a10cbad0c6fe503009_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0ce2b1960906e4828def19a10cbad0c6fe503009_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0ce2b1960906e4828def19a10cbad0c6fe503009_2_1380x662.jpeg 2x" data-dominant-color="413A38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1707×819 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="nunno" data-post="18" data-topic="30703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/eada6e/48.png" class="avatar"> nunno:</div>
<blockquote>
<p>When annotating the segments, I noticed that anatomical structures before the image flip is much clearer compared to post flip. Is it possible to edit the flip code such that we can annotate the structure first on the ijk images, then flip the annotation along with the pixels?</p>
</blockquote>
</aside>
<p>Yes, you can segment the 2D slices (before 3D reconstruction), export the segmentation to a labelmap image, and then reconstruct a 3D volume from this labelmap image the same way as you do from the ultrasound image.</p>

---
