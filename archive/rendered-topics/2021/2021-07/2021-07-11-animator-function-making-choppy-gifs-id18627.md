# Animator function making choppy gifs

**Topic ID**: 18627
**Date**: 2021-07-11
**URL**: https://discourse.slicer.org/t/animator-function-making-choppy-gifs/18627

---

## Post #1 by @bcolbert (2021-07-11 13:07 UTC)

<p>I am using the animator function to create a 5-10 second gif. The gifs all end up being very choppy regardless of what size they are. Any suggestions? Looking to create a gif to put in a presentation.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b658860a430521ce6696a9ad51006e5566cf9ab.gif" alt="Animation4" data-base62-sha1="6bU3Ym6n1B8Xkf2GZaTg6AeMSef" width="320" height="240" class="animated"></p>

---

## Post #2 by @pieper (2021-07-11 14:35 UTC)

<p>Does it look correct when it’s rendering?  Do other file formats behave differently?</p>

---

## Post #3 by @bcolbert (2021-07-11 19:08 UTC)

<p>It looks fine in the animator mode and when I change format to mpeg-4 it looks fine. Seems to only occur when making a gif.</p>

---

## Post #4 by @pieper (2021-07-11 21:19 UTC)

<p>The Ainimator uses the ScreenCapture module under the hood by creating a sequence.  If you go to that module you can select the sequence and play with the output options and also the ffmpeg command line options.  Or you can choose to save the frames to a directory and encode with a different gif tool.  You can google around and find lots of advice.  Perhaps the images are too high-res for a gif.  Let us know what you find out.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html</a></p>

---

## Post #5 by @lassoan (2021-07-12 03:26 UTC)

<p>Animated GIF is very bad for storing video: it only supports fixed 256-color palette, which results in very low quality images; file sizes can be 10-100x larger than with video compression; hardware-accelerated decoders are not available, etc. GIF format was designed more than 30 years ago and it is amazing that people still find it useful today, but it is really time to move on.</p>
<p>If you compress your video with h.264 encoder and store it in an mp4 file then you can replay it everywhere (you don’t need to worry that your video will not play on another computer like it was often the case 10 years ago). You might also consider h.265 codec (slightly better compression) or AV1 (no licensing hassles), but they are not as universally supported as h.264.</p>

---
