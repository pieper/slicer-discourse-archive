---
topic_id: 1464
title: "Why The Editor Module Is Missing"
date: 2017-11-15
url: https://discourse.slicer.org/t/1464
---

# Why the Editor module is missing?

**Topic ID**: 1464
**Date**: 2017-11-15
**URL**: https://discourse.slicer.org/t/why-the-editor-module-is-missing/1464

---

## Post #1 by @gildoringlorin (2017-11-15 11:56 UTC)

<p>Operating system:Windows 7 X64<br>
Slicer version:4.7.0<br>
Expected behavior:Editor module<br>
Actual behavior:Can’t find Editor module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14d6c8d6bb0c4e8007d7937d22991a02ee62f76.png" data-download-href="/uploads/short-url/yqEWW7tC6FjxYebc5OKf1riZ0EK.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f14d6c8d6bb0c4e8007d7937d22991a02ee62f76_2_690x388.png" alt="无标题" data-base62-sha1="yqEWW7tC6FjxYebc5OKf1riZ0EK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f14d6c8d6bb0c4e8007d7937d22991a02ee62f76_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f14d6c8d6bb0c4e8007d7937d22991a02ee62f76_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f14d6c8d6bb0c4e8007d7937d22991a02ee62f76_2_1380x776.png 2x" data-dominant-color="59585A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">1920×1080 339 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce458c17d2cce8d8b2d510bc348c1f921e5733c.png" data-download-href="/uploads/short-url/mnVIo5pYbrAEN6Q705pqOs1arkU.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ce458c17d2cce8d8b2d510bc348c1f921e5733c_2_690x414.png" alt="无标题" data-base62-sha1="mnVIo5pYbrAEN6Q705pqOs1arkU" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ce458c17d2cce8d8b2d510bc348c1f921e5733c_2_690x414.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce458c17d2cce8d8b2d510bc348c1f921e5733c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce458c17d2cce8d8b2d510bc348c1f921e5733c.png 2x" data-dominant-color="A6A6AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">1022×614 59.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>as the image shows.I start 3D Slicer with debug mode using VS2013, but I can’t a module named ‘Editor’ which exists in 3D Slicer installation version.<br>
I tried several version in Github and none of them has Editor module.What problem is it?</p>

---

## Post #2 by @pieper (2017-11-15 12:39 UTC)

<p>Thanks for sending the screenshot - in the terminal where you started Slicer there’s a python error saying that numpy cannot be imported and that’s why the Editor didn’t load.</p>
<p>You’ll need to go back and debug the build process to make numpy work since a lot of Slicer code depends on it.  Building numpy, especially on windows, can be tricky, but if you describe your steps and post build logs hopefully someone here can help.</p>

---

## Post #3 by @lassoan (2017-11-15 12:45 UTC)

<p>Also, for developers who build Slicer, it is recommended to use the latest master version (now 4.9) but at the very minimum the latest stable (now 4.8).</p>

---

## Post #4 by @gildoringlorin (2017-11-17 10:59 UTC)

<p>thanks for replying!<br>
indeed I didn’t build numpy,because it makes building unsuccessful.<br>
can you tell me where to find build logs?</p>

---

## Post #5 by @cpinter (2017-11-17 13:31 UTC)

<p>On Windows the build logs are in [SuperbuildDir]\x64[Configuration] for example S4R\x64\Release</p>

---

## Post #6 by @gildoringlorin (2017-11-18 12:27 UTC)

<p>thanks a lot,I’ve solved the problem:grinning:</p>

---

## Post #7 by @cpinter (2017-11-18 13:06 UTC)

<p>Can you describe your solution in case somebody else has the same problem? Thanks!</p>

---

## Post #8 by @gildoringlorin (2017-11-22 13:44 UTC)

<p>when use CMake to generate the project, make sure the ‘Slicer_USE_NUMPY’ is selected.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32ef61ff2b83c28665f01440b020941808951193.png" data-download-href="/uploads/short-url/7gAKqpngnHZnnpoK1sVQPUTH3zR.png?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32ef61ff2b83c28665f01440b020941808951193.png" alt="无标题" data-base62-sha1="7gAKqpngnHZnnpoK1sVQPUTH3zR" width="514" height="500" data-dominant-color="E4E5E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">658×639 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the later compile in VS2013 maybe fail many times.I just compile over and over until it succeed…<img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2017-11-22 14:10 UTC)

<aside class="quote no-group" data-username="gildoringlorin" data-post="8" data-topic="1464">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gildoringlorin/48/931_2.png" class="avatar"> gildoringlorin:</div>
<blockquote>
<p>I just compile over and over until it succeed</p>
</blockquote>
</aside>
<p>If you need multiple attempts for the build succeed then most likely something interferes with the build process. It might be a too aggressive firewall disrupting network communication, antivirus software preventing/delaying file access, etc.</p>

---

## Post #10 by @gildoringlorin (2017-11-25 23:09 UTC)

<p>maybe you are right, I didn’t close the firewall.<img src="https://emoji.discourse-cdn.com/twitter/grimacing.png?v=5" title=":grimacing:" class="emoji" alt=":grimacing:"></p>

---
