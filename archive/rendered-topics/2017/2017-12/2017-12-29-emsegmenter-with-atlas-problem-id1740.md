# EMSegmenter with Atlas problem

**Topic ID**: 1740
**Date**: 2017-12-29
**URL**: https://discourse.slicer.org/t/emsegmenter-with-atlas-problem/1740

---

## Post #1 by @NaglisR (2017-12-29 15:30 UTC)

<p>Hi, everyone,</p>
<p>I am trying to use the EMSegmenter with Atlas module and run in to this screen:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3108b612e027474789b5e9db48faf8fa28a16fc.png" data-download-href="/uploads/short-url/yGfteZMb1nRIEAike9lgcHEzGCo.png?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3108b612e027474789b5e9db48faf8fa28a16fc_2_406x500.png" alt="slicer" data-base62-sha1="yGfteZMb1nRIEAike9lgcHEzGCo" width="406" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3108b612e027474789b5e9db48faf8fa28a16fc_2_406x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3108b612e027474789b5e9db48faf8fa28a16fc_2_609x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3108b612e027474789b5e9db48faf8fa28a16fc.png 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">711×875 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Don’t seem to be moving anywhere from this point as there are no options for input. Am I doing something wrong here?</p>

---

## Post #2 by @pieper (2018-01-07 16:14 UTC)

<p>Thanks for pointing this out - I was able to replicate the issue and the fix was pretty easy.</p>
<p>With this fix I could segment the MRHead sample data on my local build.  Tomorrow’s Slicer Nightly will include the fix.</p>
<p><a href="https://github.com/Slicer/Slicer/commit/0297723d5ac517584472e1da1324c9894f49b3a6" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/commit/0297723d5ac517584472e1da1324c9894f49b3a6</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d96cfdf4c44dcd4b1369a35143fa157ab836132d.png" alt="image" data-base62-sha1="v1r7M3w01weNoMf9eFxwLTvjqHz" width="497" height="371"></p>

---
