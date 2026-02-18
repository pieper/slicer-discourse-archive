# New extension: RawImageGuess - for loading of images from unrecognized file format

**Topic ID**: 9219
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219

---

## Post #1 by @lassoan (2019-11-19 17:16 UTC)

<p>There are proprietary image file formats the 3D Slicer does not recognize and so refuses to load. <a class="mention" href="/u/nagy.attila">@nagy.attila</a> in collaboration with Slicer core developers created an extension that can be used to load data from files that use an unknown format.</p>
<p><a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a> offers a number of parameters (image header size, dimensions, pixel type, etc.) that users can adjust and see the resulting image in real-time. This makes it possible to guess the image format in a couple of minutes.</p>
<p>See a demo video that shows how to guess format of a Samsung .mvl 3D ultrasound image:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ajpOQEAyWkA" data-video-title="How to load a file of unknown format into 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ajpOQEAyWkA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ajpOQEAyWkA/maxresdefault.jpg" title="How to load a file of unknown format into 3D Slicer" width="" height="">
  </a>
</div>

<p>The extension is available in the extension manager for latest Slicer Preview Release.</p>

---

## Post #2 by @Rodrigo_Visconti (2019-11-23 16:22 UTC)

<p>It works for GE ultrasound images?</p>

---

## Post #3 by @nagy.attila (2019-11-25 09:32 UTC)

<p>The extension should be able to handle any non-compressed raw data.</p>
<p>I have no experience with US images but can’t you export it in a format that Slicer recognizes?</p>

---

## Post #4 by @lassoan (2019-11-25 16:27 UTC)

<p>You can also load a few types of GE ultrasound images by using <a href="https://github.com/SlicerHeart/SlicerHeart#ge">SlicerHeart extension</a>.</p>

---

## Post #5 by @Pieter (2020-04-24 15:59 UTC)

<p>Hi<br>
I am using Version 4.10.2 and looking for this extension but I am not finding it as per the pic.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3316e9a53bf73272464c10aac9572a233bc0dbf.png" data-download-href="/uploads/short-url/u8iExH7zAChxDLBMgP546qFPfu7.png?dl=1" title="No RawImageGuess file" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3316e9a53bf73272464c10aac9572a233bc0dbf_2_690x175.png" alt="No RawImageGuess file" data-base62-sha1="u8iExH7zAChxDLBMgP546qFPfu7" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3316e9a53bf73272464c10aac9572a233bc0dbf_2_690x175.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3316e9a53bf73272464c10aac9572a233bc0dbf_2_1035x262.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3316e9a53bf73272464c10aac9572a233bc0dbf_2_1380x350.png 2x" data-dominant-color="FEFEFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">No RawImageGuess file</span><span class="informations">1914×487 32.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please can you assist as I would like to access the extension.</p>

---

## Post #6 by @lassoan (2020-04-24 16:07 UTC)

<p>RawImaeGuess module was released after Slicer 4.10.2. You need to use a recent Slicer Preview Release to access it.</p>

---

## Post #7 by @Pieter (2020-04-24 16:14 UTC)

<p>Thank you, I am installing it now.</p>

---

## Post #8 by @Pieter (2020-04-24 17:18 UTC)

<p>Hi there,</p>
<p>I have installed the new version and I tried to load the image, I just have a problem that on lower left it does not want to allow me to select Update, its just above the button to Generate NRRD Image Header.</p>
<p>What could be the issue?</p>
<p>I Also note that at the Output volume mine states Create New Volume and with yours it states Volume…</p>
<p>Please can you assist?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c.png" data-download-href="/uploads/short-url/AhuERdQVmDFXKVbBNi9ki1dzR9i.png?dl=1" title="Update and Generate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_690x246.png" alt="Update and Generate" data-base62-sha1="AhuERdQVmDFXKVbBNi9ki1dzR9i" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_690x246.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_1035x369.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_1380x492.png 2x" data-dominant-color="717076"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Update and Generate</span><span class="informations">1928×690 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Pieter (2020-04-24 17:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c.png" data-download-href="/uploads/short-url/AhuERdQVmDFXKVbBNi9ki1dzR9i.png?dl=1" title="Update and Generate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_690x246.png" alt="Update and Generate" data-base62-sha1="AhuERdQVmDFXKVbBNi9ki1dzR9i" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_690x246.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_1035x369.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe488617654750250c3e863190de1723e06b7e2c_2_1380x492.png 2x" data-dominant-color="717076"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Update and Generate</span><span class="informations">1928×690 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2020-04-24 18:51 UTC)

<p>Sorry, it looks like a minor bug snuck into the module, which can only be seen when you start the module the first time, so we missed it. It is fixed now, so in tomorrow’s Slicer Preview Release it will work well.</p>
<p>You don’t need to wait for the fix, though, just restart Slicer after you set the input file. Next time when you start Slicer the Update button will be enabled. The output volume is created automatically when you first click the Update button.</p>

---

## Post #11 by @Pieter (2020-04-25 12:22 UTC)

<p>Hi there,</p>
<p>Thank you, it took some time but I found the logic in the method. I could isolate the fetus and get it mostly in 1 frame.</p>
<p>I then opened in Volume rendering to get to the facial features but could not see much.</p>
<p>I then opened in Segment Editor, I added a segment in color green, I selected Threshold as I wanted to get the correct contrast to see the face or body or anything but I think I am missing something.</p>
<p>The goal is to see the fetus in 3D but I am not getting that image after I have isolated.</p>
<p>Please can you advise <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e50a9ded7e2522b2791e7de366f98d4db53da40.jpeg" data-download-href="/uploads/short-url/6BIMDFy134KFn7idxyI63BTWklq.jpeg?dl=1" title="Segmnt Editor.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e50a9ded7e2522b2791e7de366f98d4db53da40_2_690x375.jpeg" alt="Segmnt Editor.PNG" data-base62-sha1="6BIMDFy134KFn7idxyI63BTWklq" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e50a9ded7e2522b2791e7de366f98d4db53da40_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e50a9ded7e2522b2791e7de366f98d4db53da40_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e50a9ded7e2522b2791e7de366f98d4db53da40_2_1380x750.jpeg 2x" data-dominant-color="737779"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segmnt Editor.PNG</span><span class="informations">1909×1039 551 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Pieter (2020-04-25 12:51 UTC)

<p>I got the threshold to display data but I cannot get the face…</p>
<p>Maybe the slices are done wrong or something…</p>
<p>Can I ask if you would be ok with it to get the face for me if I send you the file?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a129c495c0f77f6e8ae2c278b67e341e5f9690a.jpeg" data-download-href="/uploads/short-url/8hJz62egry8rKJDpXOCJtOxr7Sy.jpeg?dl=1" title="View.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a129c495c0f77f6e8ae2c278b67e341e5f9690a_2_690x365.jpeg" alt="View.PNG" data-base62-sha1="8hJz62egry8rKJDpXOCJtOxr7Sy" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a129c495c0f77f6e8ae2c278b67e341e5f9690a_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a129c495c0f77f6e8ae2c278b67e341e5f9690a_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a129c495c0f77f6e8ae2c278b67e341e5f9690a_2_1380x730.jpeg 2x" data-dominant-color="6C6F71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">View.PNG</span><span class="informations">1886×998 478 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2020-04-25 14:22 UTC)

<p>You did get the X size right but the Y is not correct yet. As you move the frame slider, the image should not move up/down.</p>

---

## Post #14 by @finetjul (2020-06-23 15:49 UTC)

<p>This is great, thanks ! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I have a feature request if I may, I would suggest to add support for multiple RAW 2D files that make up a 3D volume. Thanks.</p>

---

## Post #15 by @lassoan (2020-06-23 15:55 UTC)

<p>That could be a nice addition. I’m not sure anyone would have time right now to implement this, but you could add it as a feature request here: <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess/issues">https://github.com/acetylsalicyl/SlicerRawImageGuess/issues</a></p>

---

## Post #16 by @Pieter (2020-07-13 19:06 UTC)

<p>Hi there, hope you are doing well.</p>
<p>I have been trying my best to get this image of my child of 23 weeks. I just cannot get the 3D image to display the face. I tried to scale the vectors but I am doing something wrong. I recorded the x y z and will attach the file. Could you please please have a look and see if you can get the correct image and inform me what I am doing wrong, its really important to me.<br>
Please tell me if possible if I can send you the .mlv file via we transfer or any other method.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dae4d4baf914247b2314f5968097807dcb7c524a.jpeg" data-download-href="/uploads/short-url/veqm71LhQqLB9tb6J9CtEEgmN74.jpeg?dl=1" title="Pic 1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dae4d4baf914247b2314f5968097807dcb7c524a_2_690x369.jpeg" alt="Pic 1.PNG" data-base62-sha1="veqm71LhQqLB9tb6J9CtEEgmN74" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dae4d4baf914247b2314f5968097807dcb7c524a_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dae4d4baf914247b2314f5968097807dcb7c524a_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dae4d4baf914247b2314f5968097807dcb7c524a_2_1380x738.jpeg 2x" data-dominant-color="91979E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic 1.PNG</span><span class="informations">1912×1024 505 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ec0f7a8781256cc34917f09fa99c4e8d26c064.jpeg" data-download-href="/uploads/short-url/x5G3hhKhUsYo7F56ZsZdCyhE6rO.jpeg?dl=1" title="Pic 2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ec0f7a8781256cc34917f09fa99c4e8d26c064_2_690x370.jpeg" alt="Pic 2.PNG" data-base62-sha1="x5G3hhKhUsYo7F56ZsZdCyhE6rO" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ec0f7a8781256cc34917f09fa99c4e8d26c064_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ec0f7a8781256cc34917f09fa99c4e8d26c064_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ec0f7a8781256cc34917f09fa99c4e8d26c064_2_1380x740.jpeg 2x" data-dominant-color="9499A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pic 2.PNG</span><span class="informations">1922×1031 457 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @lassoan (2020-07-13 19:15 UTC)

<p>To see the face, you need to remove the regions that occlude it (see red marking):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12f7cb739ff3f697424e3ff47eab08eb600babd3.jpeg" data-download-href="/uploads/short-url/2HNuw9q4m0tZpHI8V6ewMMvEJLd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/12f7cb739ff3f697424e3ff47eab08eb600babd3_2_690x215.jpeg" alt="image" data-base62-sha1="2HNuw9q4m0tZpHI8V6ewMMvEJLd" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/12f7cb739ff3f697424e3ff47eab08eb600babd3_2_690x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12f7cb739ff3f697424e3ff47eab08eb600babd3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12f7cb739ff3f697424e3ff47eab08eb600babd3.jpeg 2x" data-dominant-color="555953"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">766×239 79.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You may want to apply anisotropic filtering on the image before segmentation to reduce noise in the image.</p>
<p>If you want to create a 3D-printable model then I would recommend to remove the volume rendering display.</p>

---

## Post #18 by @Pieter (2020-07-14 06:36 UTC)

<p>Thank you I will do what you have recommended.</p>
<p>Just for clarity, on the button Display ROI what does it mean (ROI) ?</p>
<p>The X Y Z Spacing means the the size of the model I think, so if the fetus is 31 CM from Cranium to Coccyx then how do I calibrate correctly or at least very close?</p>

---

## Post #19 by @lassoan (2020-07-14 14:04 UTC)

<p>ROI = region of interest. It is an Annotation ROI node, which acts as a clipping box.</p>
<p>You can estimate the relative XYZ spacing by looking at the image and adjust the values to that there is no obvious distortion. Then do a linear measurement of a known length and multiply all the spacing values by the ratio of the expected and measured length.</p>

---

## Post #20 by @Otilio_Dominguez (2021-01-05 20:07 UTC)

<p>Hi Pieter, I’m having trouble to get the software to display the .mvl data with the extension RawImage, could you tell us about this “Logic method” of yours? I’m trying to 3d print my baby’s ultrasound. I’d appreciate it.</p>

---

## Post #21 by @lassoan (2021-01-05 22:01 UTC)

<p>Have you tried to follow the video tutorial?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ajpOQEAyWkA" data-video-title="How to load a file of unknown format into 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ajpOQEAyWkA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ajpOQEAyWkA/maxresdefault.jpg" title="How to load a file of unknown format into 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #22 by @isiloon (2021-05-23 18:11 UTC)

<p>Hello Andras, I’m glad that you are aware about mvl files and lack of softwares using them. I tried the raw image guess extension it’s really hard to get it right. I don’t know whether my source is right or not, can you check my file if it can be used with the extension and converted to stl or another filetype for use in meshmixer etc?<br>
<a href="https://drive.google.com/drive/folders/1RJqdjDETbZNwtA4AHr8mRolyjc1lDEDG?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1RJqdjDETbZNwtA4AHr8mRolyjc1lDEDG?usp=sharing</a></p>
<p>And the second question is once I determine the exact values of header size, xyz positions, spacings etc, does same values work for every mlv file obtained from the same samsung machine or I have to retune the values again for every render?</p>
<p>Thanks in advance, I read every post of yours about mvl files, apreciate your efforts to help people</p>

---
