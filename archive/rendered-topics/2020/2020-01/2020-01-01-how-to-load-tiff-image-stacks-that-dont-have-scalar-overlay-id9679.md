---
topic_id: 9679
title: "How To Load Tiff Image Stacks That Dont Have Scalar Overlay"
date: 2020-01-01
url: https://discourse.slicer.org/t/9679
---

# How to load TIFF image stacks that don't have scalar overlay already associated?

**Topic ID**: 9679
**Date**: 2020-01-01
**URL**: https://discourse.slicer.org/t/how-to-load-tiff-image-stacks-that-dont-have-scalar-overlay-already-associated/9679

---

## Post #1 by @carterrt (2020-01-01 19:43 UTC)

<p>I have a few TIFF image stacks that when I load into Slicer seem to only have a volume data set and no scalar overlay data associated with them and therefore load in an illogical way. When I load different TIFF image stacks that seem to “come with” a scalar overlay meaning that it appears in data loading box, they load fine. All these data sets (with and without scalar overlay data) load fine in Dragonfly, leading me to suspect there is a way to load image stacks that don’t have scalar overlay data in Dragonfly but I don’t know how. I would prefer to use Slicer for all these data sets if possible.</p>

---

## Post #2 by @muratmaga (2020-01-01 22:50 UTC)

<p>I am not sure what you mean by ‘load in an illogical way’. You do not need a scalar overlay for an image stack to be imported as scalar volume.</p>
<p>Just drag and drop one of the tiff files, uncheck the option ‘single file’ and then you should be able to read your image stack as a scalar volume (not overlay). If this is a RBG stack, then you may have to use the vector2scalar module to convert them as a scalar.</p>
<p>If you can tell us more about these stacks, better yet share one we can probably help more. I do not know anything about Dragonfly.</p>

---

## Post #3 by @carterrt (2020-01-02 15:54 UTC)

<p>Thanks of getting back to me. Dragging and dropping didn’t work and I tried the vector to scalar module but I must be doing something wrong because I cant get the Input Vector Volume drop down to work. Whats the best way to share a data set with you?</p>

---

## Post #4 by @pieper (2020-01-02 16:19 UTC)

<aside class="quote no-group" data-username="carterrt" data-post="3" data-topic="9679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/6bbea6/48.png" class="avatar"> carterrt:</div>
<blockquote>
<p>Whats the best way to share a data set with you?</p>
</blockquote>
</aside>
<p>Yes, it will hep to look at an example. You can use dropbox, google drive, or microsoft onedrive, whatever is easiest for you to share.</p>

---

## Post #5 by @carterrt (2020-01-02 20:09 UTC)

<p>here is a link to a folder with one of the TIFF image stacks that I having trouble loading.</p>
<p><a href="https://etsu365-my.sharepoint.com/:f:/g/personal/carterrt_etsu_edu/EgIeFFyiG5NBt8RTzhuv7q4B305lbCX6bRLhpGcuQog6Gg?e=jwefGw" class="onebox" target="_blank" rel="nofollow noopener">https://etsu365-my.sharepoint.com/:f:/g/personal/carterrt_etsu_edu/EgIeFFyiG5NBt8RTzhuv7q4B305lbCX6bRLhpGcuQog6Gg?e=jwefGw</a></p>

---

## Post #6 by @muratmaga (2020-01-02 20:38 UTC)

<p>Thanks, downloading right now. Next time packaging them into single zip file would be preferable.</p>

---

## Post #7 by @pieper (2020-01-02 20:51 UTC)

<p>Once I downloaded it seems to load up just fine.  I selected one file, turned on the load options and unchecked “Single file”.  Then in the Volumes module I set the slice spacing to 0.015 to match the in plane spacing.  The image quality looks great.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aea615eb9d85fab2f2e3b6b02e432703f85aa15d.jpeg" data-download-href="/uploads/short-url/oV0UPGxdOaCOSKOUVVw0hnMvM97.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aea615eb9d85fab2f2e3b6b02e432703f85aa15d_2_689x470.jpeg" alt="image" data-base62-sha1="oV0UPGxdOaCOSKOUVVw0hnMvM97" width="689" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aea615eb9d85fab2f2e3b6b02e432703f85aa15d_2_689x470.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aea615eb9d85fab2f2e3b6b02e432703f85aa15d_2_1033x705.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aea615eb9d85fab2f2e3b6b02e432703f85aa15d.jpeg 2x" data-dominant-color="55535D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1268×864 400 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @muratmaga (2020-01-02 20:54 UTC)

<p>Yep, works just fine. Here is a visual of load data dialog box. I just replaced the filename (which was too long, with hagfish), and unchecked the Single File option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ab2a29dde853b16b3d68a054aafdf1f52838d5c.png" data-download-href="/uploads/short-url/fdTkPPxrLV3Mwdu42L4cRLVT4te.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab2a29dde853b16b3d68a054aafdf1f52838d5c_2_690x157.png" alt="image" data-base62-sha1="fdTkPPxrLV3Mwdu42L4cRLVT4te" width="690" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab2a29dde853b16b3d68a054aafdf1f52838d5c_2_690x157.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab2a29dde853b16b3d68a054aafdf1f52838d5c_2_1035x235.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ab2a29dde853b16b3d68a054aafdf1f52838d5c_2_1380x314.png 2x" data-dominant-color="F4F5EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2010×458 32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @carterrt (2020-01-03 16:11 UTC)

<p>Still struggling. Here’s what I did. selected Load Data &gt; Choose File(s) to Add and selected one TIFF from the stack as shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/919827d538e4138638f72960beddd9115556ba6c.png" data-download-href="/uploads/short-url/kLZdXczPEblWepwNSh8qN1ww4hu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919827d538e4138638f72960beddd9115556ba6c_2_690x388.png" alt="image" data-base62-sha1="kLZdXczPEblWepwNSh8qN1ww4hu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919827d538e4138638f72960beddd9115556ba6c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919827d538e4138638f72960beddd9115556ba6c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/919827d538e4138638f72960beddd9115556ba6c_2_1380x776.png 2x" data-dominant-color="A7A9B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then unchecked single file and changed volume name to hagfish as shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d2e13bf7a992235d8cee423e9281db9fd2fb4bf.png" data-download-href="/uploads/short-url/mqtGkdrSxhXrm2JW2tOkXSyJ3Fd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2e13bf7a992235d8cee423e9281db9fd2fb4bf_2_690x388.png" alt="image" data-base62-sha1="mqtGkdrSxhXrm2JW2tOkXSyJ3Fd" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2e13bf7a992235d8cee423e9281db9fd2fb4bf_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2e13bf7a992235d8cee423e9281db9fd2fb4bf_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d2e13bf7a992235d8cee423e9281db9fd2fb4bf_2_1380x776.png 2x" data-dominant-color="EBEDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Loads like this…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ff04601bb0b6b46353653af4157dafa8fb1f1fc.jpeg" data-download-href="/uploads/short-url/2gZWCNX2xFugaonEUq2LR3xjJPm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ff04601bb0b6b46353653af4157dafa8fb1f1fc_2_690x388.jpeg" alt="image" data-base62-sha1="2gZWCNX2xFugaonEUq2LR3xjJPm" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ff04601bb0b6b46353653af4157dafa8fb1f1fc_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ff04601bb0b6b46353653af4157dafa8fb1f1fc_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ff04601bb0b6b46353653af4157dafa8fb1f1fc_2_1380x776.jpeg 2x" data-dominant-color="858598"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @carterrt (2020-01-03 16:14 UTC)

<p>Sorry that second screen capture should have looked like this…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bcaab9132c9fe28a288822448ac66cd202ab6a9.png" data-download-href="/uploads/short-url/d61FsoIMNZDKZhrTSUCj3fz8JDP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcaab9132c9fe28a288822448ac66cd202ab6a9_2_690x388.png" alt="image" data-base62-sha1="d61FsoIMNZDKZhrTSUCj3fz8JDP" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcaab9132c9fe28a288822448ac66cd202ab6a9_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcaab9132c9fe28a288822448ac66cd202ab6a9_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcaab9132c9fe28a288822448ac66cd202ab6a9_2_1380x776.png 2x" data-dominant-color="9C9DAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @muratmaga (2020-01-03 17:16 UTC)

<p>Go to volumes module and check your data</p>
<ol>
<li>Does volume dimensions make sense?</li>
<li>Is the slice spacing across three axes correct?</li>
</ol>
<p>If the image stack loaded correctly, I suspect you are suffering from <span class="hashtag">#2</span>.</p>

---

## Post #12 by @carterrt (2020-01-03 17:40 UTC)

<p>OK, finally got it. Thanks for your patience!</p>

---

## Post #13 by @muratmaga (2020-01-03 17:43 UTC)

<p>Tiff is not a suitable format to retain image geometry. Make sure to save your volume as nrrd file so that you don’t encounter the same issue when you reload your data.</p>

---
