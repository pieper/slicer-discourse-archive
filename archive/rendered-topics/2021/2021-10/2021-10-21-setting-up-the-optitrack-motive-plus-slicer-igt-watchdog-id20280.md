# Setting up the Optitrack Motive => PLUS => Slicer IGT Watchdog

**Topic ID**: 20280
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/setting-up-the-optitrack-motive-plus-slicer-igt-watchdog/20280

---

## Post #1 by @pll_llq (2021-10-21 08:33 UTC)

<p>Hi everyone <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20">,<br>
We’re using Optitrack DUO for to track tools in our setup. The PLUS server is set up to attach to a running motive and send only valid transforms to Slicer.<br>
We see a problem that on the Slicer side that it continues to receive the last known transform of the tool even if the tool is out of the tracker camera’s sight.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99860466fef8a31b2b17700ba733fae2dc2c1dc1.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99860466fef8a31b2b17700ba733fae2dc2c1dc1.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99860466fef8a31b2b17700ba733fae2dc2c1dc1.mp4</a>
    </source></video>
  </div><p></p>
<p>As showed in the video - in Motive itself when the tool is out of sight the icon dims, so I assume that the Motive knows that the tool is not visible. In Slicer the transform update stops only when I turn PLUS server off completely.</p>
<p>I guess there is either some setting on the Motive side that should be toggled to prevent these transforms from being sent or some additional setting for the PLUS server configuration. Has anyone had similar issues or can advice on how to establish this <code>MotiveToSlicer</code> connection correctly?</p>

---

## Post #2 by @Sunderlandkyl (2021-10-21 14:51 UTC)

<p>In the config file, you can add "SendValidTransformsOnly=“TRUE” to the PlusOpenIGTLinkServer element, which should stop them from being sent.</p>
<pre><code class="lang-auto">&lt;PlusOpenIGTLinkServer
  ...
  SendValidTransformsOnly="TRUE"
  ...
</code></pre>

---

## Post #3 by @pll_llq (2021-10-21 14:55 UTC)

<p>Thanks for the input. We see this behaviour when the <code>SendValidTransformsOnly</code> is <code>"TRUE"</code>. (in the video on the right side there is a text editor open with the config that we’re using. line 38). If the tool is lost we continue to receive the transform update that shows the last known tool position.</p>
<p>We saw that Motive and PLUS send invalid transforms only if the tool is not registered in Motive. We did try switching the <code>SendValidTransformsOnly</code> to “not TRUE” earlier today and validated this.</p>

---

## Post #4 by @Sunderlandkyl (2021-10-21 15:20 UTC)

<p>I found this issue in PlusLib that is still open:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/PlusToolkit/PlusLib/issues/436">
  <header class="source">

      <a href="https://github.com/PlusToolkit/PlusLib/issues/436" target="_blank" rel="noopener nofollow ugc">github.com/PlusToolkit/PlusLib</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PlusToolkit/PlusLib/issues/436" target="_blank" rel="noopener nofollow ugc">PLUS still sends valid transforms when object is not tracked in Motive</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-11-06" data-time="16:22:52" data-timezone="UTC">04:22PM - 06 Nov 18 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/zacbaum" target="_blank" rel="noopener nofollow ugc">
          <img alt="zacbaum" src="https://avatars.githubusercontent.com/u/7175543?v=4" class="onebox-avatar-inline" width="20" height="20">
          zacbaum
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a tool is no longer visible by OptiTrack cameras in Motive (in at least v2.<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">0.2), PLUS still sends transforms of the last known location of the object in the transform (ie. watchdog does not know that the tool is hidden or not currently tracked).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And this PR that I think was meant to address the issue: <a href="https://github.com/PlusToolkit/PlusLib/pull/699" class="inline-onebox" rel="noopener nofollow ugc">Otitrack valid tracking status by hgueziri · Pull Request #699 · PlusToolkit/PlusLib · GitHub</a></p>
<p>I can’t make it out in the video, what version of Plus are you using?</p>

---

## Post #5 by @pll_llq (2021-10-21 15:28 UTC)

<p>Thanks for pointing that out <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a><br>
Plus App version is 2.8.0.20191105-Win64 (latest stable)<br>
I didn’t get from the discussion if it was fixed in 2020?</p>

---

## Post #6 by @Sunderlandkyl (2021-10-21 15:30 UTC)

<p>Yes, the PR changed the transform to be invalid if it was out of view, so it should have the correct behavior in the latest nightly version. Let me know if it works in the nightly.</p>

---

## Post #7 by @pll_llq (2021-10-22 13:05 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> ,</p>
<p>At first we’ve tried using the latest PLUS with the same config file and it failed to work with Motive. We’ve tried it with versions 2.1.1, 2.1.2, 2.2.0 and 2.3.0.</p>
<p>Previously we were using the combination of PLUS - Motive mentioned in the docs <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOptiTrack.html" rel="noopener nofollow ugc">here</a> (latest stable with 2.1.1).</p>
<p>I’ve uploaded the log file to <a href="https://gist.github.com/piiq/deb5607b2ffd9a5c74b4087802d11f55" rel="noopener nofollow ugc">this gist</a></p>
<p>After some poking around the logs, source code and the configs I have managed to launch the server by providing the <code>Calibration</code> parameter to the <code>Device</code> section of the configuration file like this:</p>
<pre><code class="lang-auto">Profile="MotiveProfile.motive"
Calibration="MotiveProfile.motive"
</code></pre>
<p>I suspect that the Calibration parameter became mandatory in <a href="https://github.com/PlusToolkit/PlusLib/commit/d49e0cf58ab69a9742548e58c2acaa2326d2c452#diff-b835af89861c2db0a123645070ed5fb24fa9af6f1e2f2213362c0d4d5951525b" rel="noopener nofollow ugc">this commit</a>.</p>
<p>I can’t yet test the setup but I’ll update you on the results.</p>

---

## Post #8 by @pll_llq (2021-10-25 12:55 UTC)

<p>Thanks, the latest nightly 2.9 works</p>

---
