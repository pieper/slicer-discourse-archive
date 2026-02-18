# 3D Image not seen

**Topic ID**: 11880
**Date**: 2020-06-05
**URL**: https://discourse.slicer.org/t/3d-image-not-seen/11880

---

## Post #1 by @kavitha (2020-06-05 16:19 UTC)

<p>Hi,<br>
I am new to Slicer and trying to run a NVIDIAA spleen model on 3D Slicer. But, I am not able to see the 3D image of the model. Can you please guide me on what the problem is  ?<br>
Thanks in advance for your help<br>
Screenshot attached.<br>
Kavitha<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b90819dd19194429588062c56bc4b59f01ebfc93.png" data-download-href="/uploads/short-url/qoRGGfiBtMWdcOCf1MBB18dayEr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b90819dd19194429588062c56bc4b59f01ebfc93_2_690x315.png" alt="image" data-base62-sha1="qoRGGfiBtMWdcOCf1MBB18dayEr" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b90819dd19194429588062c56bc4b59f01ebfc93_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b90819dd19194429588062c56bc4b59f01ebfc93_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b90819dd19194429588062c56bc4b59f01ebfc93.png 2x" data-dominant-color="C3C4C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1355×620 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-06-05 16:32 UTC)

<p>Does it work well with the example data sets as described <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin">here</a>?</p>

---

## Post #3 by @kavitha (2020-06-08 08:22 UTC)

<p>Hi,<br>
For a sample dataset, we are able to see the 3D Brain Image , but there are no annotation models under segment from boundary points .  Please advise on how it has to be fixed.</p>
<p>Thanks<br>
Kavitha<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c06879d73cb407bd827a82beb7f93da5e613d80.png" data-download-href="/uploads/short-url/1InIBZPY8cwWwXiF7udHWrDUVX2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c06879d73cb407bd827a82beb7f93da5e613d80_2_690x259.png" alt="image" data-base62-sha1="1InIBZPY8cwWwXiF7udHWrDUVX2" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c06879d73cb407bd827a82beb7f93da5e613d80_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c06879d73cb407bd827a82beb7f93da5e613d80_2_1035x388.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c06879d73cb407bd827a82beb7f93da5e613d80.png 2x" data-dominant-color="BEBDC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1347×506 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-06-08 14:39 UTC)

<p>The error message tells that you could not connect to the remote server. Does the link work from a web browser? Do you connect to the server using a web proxy or VPN?</p>

---

## Post #5 by @kavitha (2020-06-08 19:23 UTC)

<p>Hi,</p>
<p>The message was the initial message when the server was not working. The server is accessible from the web too. After that ,it was fetching the models in 0.4 seconds.</p>
<p>Thanks<br>
Kavitha</p>

---

## Post #6 by @lassoan (2020-06-08 20:49 UTC)

<p>Does the module work with the default server (as described <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#boundary-point-based-segmentation-of-brain-tumor-mri">here</a>)?</p>
<p>If yes, then the issue is either with the server or the models (e.g., you have models incompatible with the server version or they are not DExtr3D models). You can add logs into the code (it is a Python script, any changes take effect immediately after restart Slicer) or <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">attach a debugger</a> to narrow it down. If you cannot figure out what the issue is then submit an issue <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues">here</a>.</p>

---

## Post #7 by @kavitha (2020-06-09 13:06 UTC)

<p>Hi,<br>
We are trying to do a sample model from NVIDIA Clara. We are not creating our own model. So, we cannot change or add logs in the code. We ran the model on our cloud instance with NVIDIA clara train. We are trying to see them in 3D Slicer. Should we have a sample data already in 3D Slicer or will the NVIDIA  images be downloaded from the server.<br>
We also get this error message when we load the models from the server.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8b5e6c62c16decca16f77d432786e70f069f832.png" data-download-href="/uploads/short-url/xcEuHEE6X3P8FZK6T7vlLHSuMpk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8b5e6c62c16decca16f77d432786e70f069f832_2_690x381.png" alt="image" data-base62-sha1="xcEuHEE6X3P8FZK6T7vlLHSuMpk" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8b5e6c62c16decca16f77d432786e70f069f832_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8b5e6c62c16decca16f77d432786e70f069f832.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8b5e6c62c16decca16f77d432786e70f069f832.png 2x" data-dominant-color="D7D6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">818×452 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-06-09 13:17 UTC)

<aside class="quote no-group" data-username="kavitha" data-post="7" data-topic="11880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/edb3f5/48.png" class="avatar"> kavitha:</div>
<blockquote>
<p>We are trying to do a sample model from NVIDIA Clara. We are not creating our own model.</p>
</blockquote>
</aside>
<p>There are several different kinds of models for several different versions of NVidia Clara. Can you select a model in “Segment from boundary points” section? If not then it seems that among the models that you installed, there is no DExtr3D model, it does not match your server version, or maybe it has not been installed correctly. Of course software bugs are always possible, so if you are confident that you have installed the right model then you can submit a bug report.</p>
<aside class="quote no-group" data-username="kavitha" data-post="7" data-topic="11880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/edb3f5/48.png" class="avatar"> kavitha:</div>
<blockquote>
<p>Should we have a sample data already in 3D Slicer or will the NVIDIA images be downloaded from the server</p>
</blockquote>
</aside>
<p>You don’t need to upload images to the Clara server manually. It is uploaded automatically when you run the segmentation. You get the correct confirmation popup of the image transfer so that seems to be good.</p>
<p>Does segmentation work with the default segmentation server and MRBrainTumor1 example data set?</p>

---

## Post #9 by @kavitha (2020-06-09 13:44 UTC)

<p>Under segment from boundary points, the model is empty for the example data set of MRBrainTumor1.  Also, even for our server also, it is empty.  Are we missing something here.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d33e54cd6d54916131258a27ce335d905560a261.png" alt="image" data-base62-sha1="u8Ki0bThgpmvozYzVq6TVJywXOp" width="627" height="190">  ?</p>

---

## Post #10 by @lassoan (2020-06-10 00:35 UTC)

<p>If you set an empty string in Nvidia AIAA server and click the refresh icon (fetch models) then in “Segment from boundary points (DExtr3D)” section you can select a model from the list.</p>
<p>I see that you enabled filtering by segment name (yellow funnel icon next to the model selector). If you enable this then only those models will be shown that contain the currently segment’s name in their model description. Probably you need to disable this filtering (just click on the button).</p>

---

## Post #11 by @kavitha (2020-06-10 08:43 UTC)

<p>I kept the Nvidia AIAA server empty, refreshed and then used “Segment from boundary points” and selected the brain tumour annotation model as in the example link. But,on clicking Start , I get the error message.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01d6e6769a1a98b8429f0b6a8c0f63aa32a63299.png" data-download-href="/uploads/short-url/ggTKf3WLwVZqLVYZC4dvzF1tQB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d6e6769a1a98b8429f0b6a8c0f63aa32a63299_2_690x250.png" alt="image" data-base62-sha1="ggTKf3WLwVZqLVYZC4dvzF1tQB" width="690" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d6e6769a1a98b8429f0b6a8c0f63aa32a63299_2_690x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01d6e6769a1a98b8429f0b6a8c0f63aa32a63299_2_1035x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01d6e6769a1a98b8429f0b6a8c0f63aa32a63299.png 2x" data-dominant-color="D3D2D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1251×455 97.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the error message in details<br>
Traceback (most recent call last):<br>
File “C:/Users/User/AppData/Roaming/NA-MIC/Extensions-29057/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 361, in createAiaaSessionIfNotExists<br>
in_file, session_id = self.logic.createSession(inputVolume)<br>
File “C:/Users/User/AppData/Roaming/NA-MIC/Extensions-29057/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1008, in createSession<br>
response = aiaaClient.create_session(in_file)<br>
File “C:\Users\User\AppData\Roaming\NA-MIC\Extensions-29057\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 107, in create_session<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, response))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 404; Response: b'\n404 Not Found\n</p><h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n'’)<p></p>

---

## Post #12 by @lassoan (2020-06-10 12:49 UTC)

<p>Do these link work in your web browser?</p>
<ul>
<li><a href="http://skull.cs.queensu.ca:8123">http://skull.cs.queensu.ca:8123</a></li>
<li><a href="http://skull.cs.queensu.ca:8123/v1/models">http://skull.cs.queensu.ca:8123/v1/models</a></li>
</ul>
<p>Do they work when you use them as server address?</p>

---

## Post #13 by @kavitha (2020-06-10 13:44 UTC)

<p>Hi,</p>
<p>The links that you sent worked in our web browser. When we use them as server address, we get the same error message for this server address too</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/User/AppData/Roaming/NA-MIC/Extensions-29057/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 361, in createAiaaSessionIfNotExists<br>
in_file, session_id = self.logic.createSession(inputVolume)<br>
File “C:/Users/User/AppData/Roaming/NA-MIC/Extensions-29057/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1008, in createSession<br>
response = aiaaClient.create_session(in_file)<br>
File “C:\Users\User\AppData\Roaming\NA-MIC\Extensions-29057\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 107, in create_session<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, response))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 404; Response: b'\n404 Not Found\n</p><h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n'’)<p></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd0a64bb141b3d78436c1f41df352e94e53fa534.png" data-download-href="/uploads/short-url/A6v4dcBSVIXibojuDus0wEs7O3G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd0a64bb141b3d78436c1f41df352e94e53fa534_2_690x239.png" alt="image" data-base62-sha1="A6v4dcBSVIXibojuDus0wEs7O3G" width="690" height="239" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd0a64bb141b3d78436c1f41df352e94e53fa534_2_690x239.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd0a64bb141b3d78436c1f41df352e94e53fa534_2_1035x358.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd0a64bb141b3d78436c1f41df352e94e53fa534.png 2x" data-dominant-color="C9C8CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1278×444 97.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @lassoan (2020-06-10 14:26 UTC)

<p>It may be a network issue then. Are you on a corporate or hospital network? Do you use a proxy to connect to the internet?</p>

---

## Post #15 by @kavitha (2020-06-10 15:40 UTC)

<p>Hi,</p>
<p>I am working from my personal computer. There is no proxy. Is there any specific specifications for 3D Slicer on a Windows computer</p>
<p>Thanks</p>
<p>Kavitha</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23a8d201efa0a2f0176ba5b9aed6ae01a1173452.gif" alt="blocked.gif" data-base62-sha1="55spfY9VCmI7im715wnOljFpRIK" width="100" height="50"></p>

---

## Post #16 by @lassoan (2020-06-10 16:29 UTC)

<p>Maybe the issue is that you place all the landmarks in a single plane. Could you try placing them in at least two planes (so that you have points along each side of the region of interest, as shown in the tutorial and demo video)?</p>

---
