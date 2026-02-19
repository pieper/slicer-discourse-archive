---
topic_id: 17653
title: "Slicermorph Animator Yellow Highlight On Gif Images"
date: 2021-05-17
url: https://discourse.slicer.org/t/17653
---

# SlicerMorph Animator yellow highlight on gif images

**Topic ID**: 17653
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/slicermorph-animator-yellow-highlight-on-gif-images/17653

---

## Post #1 by @tsehrhardt (2021-05-17 15:48 UTC)

<p>I am getting this yellow highlighting when I make a gif in SlicerMorph Animator–it does not appear when I save an mp4 and I don’t see it in the Preview window.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13e16490843f07de591f9de48b7aa7f2231d57c5.jpeg" data-download-href="/uploads/short-url/2PRYntISG3WlkgmdmskP1oSClz7.jpeg?dl=1" title="2021-05-17_11-42-59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13e16490843f07de591f9de48b7aa7f2231d57c5_2_674x499.jpeg" alt="2021-05-17_11-42-59" data-base62-sha1="2PRYntISG3WlkgmdmskP1oSClz7" width="674" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13e16490843f07de591f9de48b7aa7f2231d57c5_2_674x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13e16490843f07de591f9de48b7aa7f2231d57c5_2_1011x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13e16490843f07de591f9de48b7aa7f2231d57c5.jpeg 2x" data-dominant-color="EAE7E4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-05-17_11-42-59</span><span class="informations">1343×995 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-05-17 15:58 UTC)

<p>I can confirm that this happens on my end too, and does not happen when I choose the gif output on screen capture. I opened a <a href="https://github.com/SlicerMorph/SlicerMorph/issues/160">bug</a> for <a class="mention" href="/u/pieper">@pieper</a> to take a quick look.</p>

---

## Post #3 by @pieper (2021-05-17 16:22 UTC)

<p>I would say this is probably an artifact of the limited color space for gif images (only 256 distinct colors per-frame (see <a href="https://en.wikipedia.org/wiki/GIF">this description</a>).  I’m not sure we have a lot of control over that.  Perhaps using a different background color would help.</p>

---

## Post #4 by @muratmaga (2021-05-17 16:27 UTC)

<p>But doesn’t happen when the same scene is captured with animated gif option in Screen Capture.</p>

---

## Post #5 by @tsehrhardt (2021-05-17 16:33 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="17653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Perhaps using a different background color would help.</p>
</blockquote>
</aside>
<p>Yes it does not appear with black or light blue backgrounds.</p>

---

## Post #6 by @pieper (2021-05-17 17:21 UTC)

<p>The Animator uses the ScreenCaptureLogic class, so the arguments to ffmpeg will be the same, but probably the screensize influences the way the colors are selected.  Since it can only have 256 unique colors the overall number of pixels in a frame will make a big difference and probably the algorithm isn’t very good at picking a good set of colors.  You could check this by trying different target sizes.</p>
<p>Depending on your use case, apng might be a good format to use.  We could add that to ScreenCapture/Animator.</p>
<aside class="onebox wikipedia">
  <header class="source">

      <a href="https://en.wikipedia.org/wiki/APNG" target="_blank" rel="noopener">en.wikipedia.org</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:100/100;"><img src="//upload.wikimedia.org/wikipedia/commons/1/14/Animated_PNG_example_bouncing_beach_ball.png" class="thumbnail" width="100" height="100"></div>

<h3><a href="https://en.wikipedia.org/wiki/APNG" target="_blank" rel="noopener">APNG</a></h3>

<p>Animated Portable Network Graphics (APNG) is a file format which extends the Portable Network Graphics (PNG) specification to permit animated images that work similarly to animated GIF files, while supporting 24-bit images and 8-bit transparency not available for GIFs. It also retains backward compatibility with non-animated PNG files.
 The first frame of an APNG file is stored as a normal PNG stream, so most standard PNG decoders are able to display the first frame of an APNG file. The frame spe...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @muratmaga (2021-05-17 17:51 UTC)

<p>This might be good. Particularly if we can save this directly (without ffmpeg). On linux ffmpeg doesn’t get automatically installed like windows or mac, so that’s an issue.</p>

---

## Post #8 by @pieper (2021-05-17 18:00 UTC)

<p>It looks like this package could be pip_installed into Slicer and avoid ffmpeg altogether.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="16" height="16">

      <a href="https://pypi.org/project/apng/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.90915068.jpg" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://pypi.org/project/apng/" target="_blank" rel="noopener">apng</a></h3>

  <p>A Python module to deal with APNG file.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The files will be bigger and may not be as widely supported, but the quality will be better.</p>

---

## Post #9 by @lassoan (2021-05-17 18:09 UTC)

<p>The artifact that you see is indeed what <a class="mention" href="/u/pieper">@pieper</a> suggested above - due to gif using only 256 colors. In the ScreenCapture module’s GIF export option we apply a palette optimization step (<code>-filter_complex palettegen,[v]paletteuse</code>) and there are many other optimization and preprocessing options in ffmpeg that you can use to improve the output image quality.</p>
<p>However, nowadays I would avoid using gifs. You can achieve 10-100x smaller image size and much better image quality with mp4. A few years ago, mp4 was not usable at many places, but nowadays it is quite universally supported (e.g, you can include it in discourse posts, github issues, …).</p>

---

## Post #10 by @tsehrhardt (2021-05-17 18:28 UTC)

<p>As Murat pointed out, the yellow artifact doesn’t show up when generating a gif with the Screen Capture module, just with Animator.</p>
<p>I mostly use gifs in presentations, but I can work with mp4.</p>

---

## Post #11 by @muratmaga (2021-05-17 18:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="17653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ol start="4">
<li>A few years ago, mp4 was not usable at many places, but nowadays it is quite universally supported (e.g, you can include it in discourse posts, github issues, …).</li>
</ol>
</blockquote>
</aside>
<p>Except the support in powerpoint is hit and miss (e.g., in presentations where you are not running the slide deck from your own computer). Unfortunately support APNG Is even worse than mp4 in powerpoint, so that’s not a total solution either.</p>
<p>Having reliable gif output would be useful.</p>

---

## Post #12 by @pieper (2021-05-17 18:39 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="10" data-topic="17653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>As Murat pointed out, the yellow artifact doesn’t show up when generating a gif with the Screen Capture module, just with Animator.</p>
</blockquote>
</aside>
<p>Right, but did you investigate the image size issue?  If you make the Animator gif output smaller it should have a different selection of colors.</p>

---

## Post #13 by @muratmaga (2021-05-17 18:48 UTC)

<p>I did try with a quick one (120x160), still happened.</p>

---

## Post #14 by @lassoan (2021-05-17 18:53 UTC)

<p>A .mp4 file can contain video stream with a wide range of compression methods. If you use a basic H.264 compression then I don’t think you will have replay issues anywhere.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="17653" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I did try with a quick one (120x160), still happened.</p>
</blockquote>
</aside>
<p>Check the command-line that is used for running ffmpeg. It should include the palette optimization step (<code>-filter_complex palettegen,[v]paletteuse</code>). You may also check if the issue is related to background color or transparent background. You can experiment with ffmpeg gif encoding options and various preprocessing filters outside of Slicer.</p>

---

## Post #15 by @tsehrhardt (2021-05-17 19:17 UTC)

<p>I turned OFF the palette optimization under Screen Capture and got the yellow artifact, so maybe the palette optimization is not being used in Animator.</p>

---

## Post #16 by @pieper (2021-05-17 20:40 UTC)

<p>Thanks for testing - the animator passes these arguments, but I guess the ScreenCapture settings are not being used with it.</p>
<p><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L732-L737">https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py#L732-L737</a></p>
<p>I believe Murat is experimenting with a fix to add the flags as we speak, but in the mean time after exporting from the Animator you will have a Sequence that can be selected in ScreenCapture for output using the options available there.</p>

---

## Post #17 by @muratmaga (2021-05-17 21:35 UTC)

<aside class="quote no-group" data-username="pieper" data-post="16" data-topic="17653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>but in the mean time after exporting from the Animator you will have a Sequence that can be selected in ScreenCapture for output using the options available there.</p>
</blockquote>
</aside>
<p>Yes, see this for more information using Screen Capture for exporting <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_2/SlicerAnimator/SlicerAnimator.md#saving-output" class="inline-onebox">Spr_2021/Day_2/SlicerAnimator/SlicerAnimator.md at main · SlicerMorph/Spr_2021 · GitHub</a></p>

---

## Post #18 by @pieper (2021-05-17 22:58 UTC)

<p>Thanks for the report and all the help debugging <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>This should be fixed with this PR:</p>
<aside class="onebox githubpullrequest">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/pull/161" target="_blank" rel="noopener">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerMorph/SlicerMorph/pull/161" target="_blank" rel="noopener">fix(animator): use ScreenCapture encoding options</a>
    </h4>

    <div class="branches">
      <code>SlicerMorph:master</code> ← <code>pieper:160-fix-animator-gif</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-17" data-time="22:56:51" data-timezone="UTC">10:56PM - 17 May 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 11 additions and 11 deletions">
        <a href="https://github.com/SlicerMorph/SlicerMorph/pull/161/files" target="_blank" rel="noopener">
          <span class="added">+11</span>
          <span class="removed">-11</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Before the Animator exposed a custom subset of encoding
options, but these were<span class="show-more-container"><a href="https://github.com/SlicerMorph/SlicerMorph/pull/161" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> not optimal for gif.

Now we use the ScreenCaptureLogic to replicate the same
list of options so there is only one place where encoding
options are stored.

Fixes #160</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
