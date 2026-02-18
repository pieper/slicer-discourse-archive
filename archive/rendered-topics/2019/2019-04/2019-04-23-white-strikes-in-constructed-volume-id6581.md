# White strikes in constructed volume

**Topic ID**: 6581
**Date**: 2019-04-23
**URL**: https://discourse.slicer.org/t/white-strikes-in-constructed-volume/6581

---

## Post #1 by @zoez (2019-04-23 21:25 UTC)

<p>Hello,</p>
<p>I have generated a volume by running VolumeReconstructor.exe with a saved mha file. However, the resulted volume has many white strikes in them, and these white strikes are not present in the original mha file. I’m wondering if you have any suggestions on how to resolve this?</p>
<p>I’m suspecting that the problem might be caused by each pixel in the images having 4 bytes. Does the VolumeReconstructor algorithm support images with 4 color channels?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8855cb9fc7becdfa25edb14ae2abf11a98582975.png" data-download-href="/uploads/short-url/js4KBTb4koI7EygU9AH3rvLIwsZ.png?dl=1" title="Screenshot%20(8)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8855cb9fc7becdfa25edb14ae2abf11a98582975_2_690x431.png" alt="Screenshot%20(8)" data-base62-sha1="js4KBTb4koI7EygU9AH3rvLIwsZ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8855cb9fc7becdfa25edb14ae2abf11a98582975_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8855cb9fc7becdfa25edb14ae2abf11a98582975_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8855cb9fc7becdfa25edb14ae2abf11a98582975_2_1380x862.png 2x" data-dominant-color="9B9BA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20(8)</span><span class="informations">1920×1200 494 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,<br>
Zoe</p>

---

## Post #2 by @zoez (2019-04-23 21:27 UTC)

<p>Here’s a screenshot of the original image in slicer: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e227335a1fd658fb52992dbea4b19093cd2155c3.png" data-download-href="/uploads/short-url/wgDTvaOl9t2gRNq3EfO4fbFzwH1.png?dl=1" title="Screenshot%20(9)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e227335a1fd658fb52992dbea4b19093cd2155c3_2_690x431.png" alt="Screenshot%20(9)" data-base62-sha1="wgDTvaOl9t2gRNq3EfO4fbFzwH1" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e227335a1fd658fb52992dbea4b19093cd2155c3_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e227335a1fd658fb52992dbea4b19093cd2155c3_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e227335a1fd658fb52992dbea4b19093cd2155c3_2_1380x862.png 2x" data-dominant-color="929298"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20(9)</span><span class="informations">1920×1200 324 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Sunderlandkyl (2019-04-24 12:42 UTC)

<p>VolumeReconstructor.exe should be able to handle color images by converting them to grayscale.</p>
<p>I’ll take a look. Could you upload your config file and Plus log somewhere?</p>

---

## Post #4 by @zoez (2019-04-24 21:54 UTC)

<p>Hello Kyle,</p>
<p>Please find the config file, the original mha recording and PlusLog file <a href="https://drive.google.com/drive/folders/1WaFab3bI45xS3dGyNIaYxu-9WeGgr3YO?usp=sharing" rel="nofollow noopener">here</a>.</p>
<p>Thanks,<br>
Zoe</p>

---

## Post #5 by @zoez (2019-04-29 19:30 UTC)

<p>Hello Kyle,</p>
<p>I tried converting the images to grayscale before feeding into the VolumeReconstructor app and it worked.</p>
<p>Thanks.<br>
Zoe</p>

---
