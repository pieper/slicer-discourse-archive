# SlicerMorph Photogrammetry photo masking issue

**Topic ID**: 43369
**Date**: 2025-06-16
**URL**: https://discourse.slicer.org/t/slicermorph-photogrammetry-photo-masking-issue/43369

---

## Post #1 by @chz31 (2025-06-16 14:43 UTC)

<p>I am trying the Slicer Photogrammetry with a student. The photos were taken by a cell phone at a single perspective. However, the masking behaved very weirdly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afd06b5c8377fec1004145e3a472dc928739e458.png" data-download-href="/uploads/short-url/p5k5OxbjFQ3Ko1oLsHKLcS51Hrq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd06b5c8377fec1004145e3a472dc928739e458_2_345x102.png" alt="image" data-base62-sha1="p5k5OxbjFQ3Ko1oLsHKLcS51Hrq" width="345" height="102" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd06b5c8377fec1004145e3a472dc928739e458_2_345x102.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd06b5c8377fec1004145e3a472dc928739e458_2_517x153.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afd06b5c8377fec1004145e3a472dc928739e458_2_690x204.png 2x" data-dominant-color="0C0C0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">970×288 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fe9b4f76ea1395f809fd95ca2f816c7568ac95d.jpeg" data-download-href="/uploads/short-url/4yjw0GTixx97vDjzJpzRv44Ahlz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fe9b4f76ea1395f809fd95ca2f816c7568ac95d_2_345x238.jpeg" alt="image" data-base62-sha1="4yjw0GTixx97vDjzJpzRv44Ahlz" width="345" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fe9b4f76ea1395f809fd95ca2f816c7568ac95d_2_345x238.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fe9b4f76ea1395f809fd95ca2f816c7568ac95d_2_517x357.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fe9b4f76ea1395f809fd95ca2f816c7568ac95d_2_690x476.jpeg 2x" data-dominant-color="878787"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1202×830 88.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m also not very sure about the orientations. The photos were rotated horizontally in Slicer, and the output masks were also horizontal. The original photos were still vertical.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/344b4e51b1759ffa0844a97e5eeeaeca02fbbdad.png" data-download-href="/uploads/short-url/7sCaA6whTDPFTHglOZ38Tei6nyB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/344b4e51b1759ffa0844a97e5eeeaeca02fbbdad_2_517x247.png" alt="image" data-base62-sha1="7sCaA6whTDPFTHglOZ38Tei6nyB" width="517" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/344b4e51b1759ffa0844a97e5eeeaeca02fbbdad_2_517x247.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/344b4e51b1759ffa0844a97e5eeeaeca02fbbdad_2_775x370.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/344b4e51b1759ffa0844a97e5eeeaeca02fbbdad_2_1034x494.png 2x" data-dominant-color="8E8E8E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1479×708 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Perhaps due to the masking issue, the reconstruction failed at the very beginning.</p>
<p>Is there anyway to add an option to run ODM reconstruction without masking first?</p>
<p>Here are the photos:<a href="https://drive.google.com/drive/folders/1DsulCWvb-vO0o-L24PHcvSTrpUDQWgDW?usp=drive_link" class="inline-onebox" rel="noopener nofollow ugc">photos - Google Drive</a></p>
<p>Thanks!</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/oothomas">@oothomas</a></p>

---

## Post #2 by @muratmaga (2025-06-16 15:02 UTC)

<p>Yes, if that’s the masking result you got, photogrammetry isn’t likely to work on it. I have never seen patterns like that. Are you using the ROI tool to specify what to keep and then fine tune with points? Are there any errors in the console log?</p>

---

## Post #3 by @muratmaga (2025-06-16 15:07 UTC)

<p>Even if you can mask I suspect you are not going to get very good results, since your model shape very uniform and doesn’t have a lot of features. The most important step of photogrammetry is feature extracting and matching. This will actually will help by using something that has more texture than what you have.</p>
<p>For SlicerMorph Photogrammetry, accurate masking is considered crucial because it improves the reconstruction as well as speeds up the process and we have spent a lot of time trying to integrate SAM to achieve that. If you want to skip the masking and upload your photos as is, the best is probably would be launching the ODM on your own (without using the extension).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4739f77dd8a10c4ffe2af2e0fdf0120caa05af17.png" alt="image" data-base62-sha1="aa65NSvooSArZrtTFEDXpbTHJEX" width="123" height="84"></p>

---

## Post #4 by @chz31 (2025-06-16 15:09 UTC)

<p>I see. I think this model should be fine for regular photogrammetry. I will ask the student to take photos with some background to see if it works. If not, using WebODM might be an option.</p>

---

## Post #5 by @pieper (2025-06-16 15:10 UTC)

<p>Also I wonder if the phone is embedding some rotation info in the jpeg header about if the phone was in landscape or portrait mode when the photo was taken and that needs to be taken into account.</p>

---

## Post #6 by @muratmaga (2025-06-16 15:22 UTC)

<aside class="quote no-group" data-username="chz31" data-post="4" data-topic="43369">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>I will ask the student to take photos with some background to see if it works</p>
</blockquote>
</aside>
<p>Are you saying these were already masked and you tried to remask?</p>

---

## Post #7 by @chz31 (2025-06-16 15:24 UTC)

<p>It makes sense to me, because sometimes my iphone photos just rotated when I imported them into my computer. I feel the output masking may not match the photos, which led to failure.</p>
<p>For example, for some reason, I got a very good masking results, but the task still failed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a0fd2b6ca98d7cd51707cd9fc7f6dc47ef88c01.jpeg" data-download-href="/uploads/short-url/jHlN5wNYhxXrXfAfyPe3kOrRa6t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0fd2b6ca98d7cd51707cd9fc7f6dc47ef88c01_2_517x313.jpeg" alt="image" data-base62-sha1="jHlN5wNYhxXrXfAfyPe3kOrRa6t" width="517" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0fd2b6ca98d7cd51707cd9fc7f6dc47ef88c01_2_517x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0fd2b6ca98d7cd51707cd9fc7f6dc47ef88c01_2_775x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0fd2b6ca98d7cd51707cd9fc7f6dc47ef88c01_2_1034x626.jpeg 2x" data-dominant-color="B0B0B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1525×926 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will try rotating photos in Slicer, or try with a regular camera and also added some background to it.</p>

---

## Post #8 by @muratmaga (2025-06-16 15:33 UTC)

<p>These images looked already processed. So I don’t know how well SAM works on such cases.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43cb9a9972cc2c5aff4b38029f41b3c57b2f496.jpeg" data-download-href="/uploads/short-url/yQCBzyG51xsRktjZexsjFzfDCJ0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43cb9a9972cc2c5aff4b38029f41b3c57b2f496_2_462x500.jpeg" alt="image" data-base62-sha1="yQCBzyG51xsRktjZexsjFzfDCJ0" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43cb9a9972cc2c5aff4b38029f41b3c57b2f496_2_462x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43cb9a9972cc2c5aff4b38029f41b3c57b2f496_2_693x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f43cb9a9972cc2c5aff4b38029f41b3c57b2f496_2_924x1000.jpeg 2x" data-dominant-color="333128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1033×1116 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Try on the original ones.</p>
<p>As for your second set of masks, yes, looks like there is some kind of a rotation. The masks should inherit the image information from the photographs, but we never worked with cellphone photos. I will ask <a class="mention" href="/u/oothomas">@oothomas</a> to take a look. If you can provide the originals as saved by the camera (prior to any processing) would be great.</p>

---

## Post #9 by @chz31 (2025-06-16 15:39 UTC)

<p>I found this interesting thread for similar rotation issue: <a href="https://discussions.apple.com/thread/251323176?answerId=252561528022&amp;sortBy=rank#252561528022:~:text=May%201%2C%202020%209,with%20the%20orientation%20tags" rel="noopener nofollow ugc">https://discussions.apple.com/thread/251323176?answerId=252561528022&amp;sortBy=rank#252561528022:~:text=May%201%2C%202020%209,with%20the%20orientation%20tags</a>.</p>
<p>I will ask the student about how the pictures were taken. I feel adding some background might be helpful for masking as well.</p>

---

## Post #10 by @pieper (2025-06-16 15:48 UTC)

<p>It would be cool to be able to use a cellphone camera if you can figure out how to account for the orientation tags.</p>
<p>Also I think Murat’s point about the surface of the object needing to have more texture for feature masking makes sense.  Maybe try a different toy for testing.</p>

---

## Post #11 by @oothomas (2025-06-16 17:15 UTC)

<p>Hi Chi,</p>
<p>Regarding the first images you shared with the masking issue; I’ve run into this before when the bounding box isn’t tight enough around the objects to be masked. Were you using the include/exclude options at all?</p>

---

## Post #12 by @muratmaga (2025-06-16 17:28 UTC)

<p>I think currently the issue is even when the mask is good, they seem to be rotated with respect to the original image, which might indicate some kind of a portrait/landscape flip in the image headers that we are missing out. but I think we will need the original photos from the phone as well to track where the difference is coming from.</p>

---

## Post #13 by @chz31 (2025-06-16 20:06 UTC)

<p>Thanks, <a class="mention" href="/u/oothomas">@oothomas</a>. Yes, I did a big ROI box since the object was not in a stable position. I did not try placing ROI for a single object. I’ll wait for the original photos then give it a try.</p>

---

## Post #14 by @muratmaga (2025-06-16 20:16 UTC)

<p>Since the same ROI is used for all images, setting a very large ROI to accommodate everything gives less than ideal result. If you don’t have too many pictures, you can try to set the ROI manually per photo, which is obviously a bit tedious.</p>
<p>Alternatively, there is ClusterPhotos which sort of tries re-organizes your photos into sets with similar orientation to deal with subject moving in the picture frame. You can also give that a try…</p>

---

## Post #15 by @chz31 (2025-06-16 23:47 UTC)

<p>With the help of ChatGPT, yes, iphone would add a transpose flag when the photos are taken in portrait mode. Slicer is not a photo-editing app, so it’ll read raw images without EXIF data and display it in landscape orientation.</p>
<p>This is a simple script using Pillow to transpose the image to counter the flag:</p>
<pre><code class="lang-auto">from PIL import Image, ImageOps
img = Image.open("/home/zhang/Downloads/Test_Out/All Images/IMG_5653.jpg")
exif = img.info.get('exif') 
img_corrected = ImageOps.exif_transpose(img)
img_corrected.save("/home/zhang/Downloads/Test_Out/IMG_5653_corrected.jpg", exif=exif)
</code></pre>
<p>Now the image displayed correctly in Slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbe2a72b07ed8f0d84943cca0cc8796ab8ad23a8.jpeg" data-download-href="/uploads/short-url/t5EwKQdxTbTsrDMB6ZolyAa8QsM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe2a72b07ed8f0d84943cca0cc8796ab8ad23a8_2_689x292.jpeg" alt="image" data-base62-sha1="t5EwKQdxTbTsrDMB6ZolyAa8QsM" width="689" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe2a72b07ed8f0d84943cca0cc8796ab8ad23a8_2_689x292.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe2a72b07ed8f0d84943cca0cc8796ab8ad23a8_2_1033x438.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbe2a72b07ed8f0d84943cca0cc8796ab8ad23a8.jpeg 2x" data-dominant-color="20211A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×569 55.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will try it soon to see these corrected photos work.</p>

---
