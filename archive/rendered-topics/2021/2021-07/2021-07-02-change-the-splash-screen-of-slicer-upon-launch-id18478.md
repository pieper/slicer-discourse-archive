# Change the splash screen of Slicer upon launch

**Topic ID**: 18478
**Date**: 2021-07-02
**URL**: https://discourse.slicer.org/t/change-the-splash-screen-of-slicer-upon-launch/18478

---

## Post #1 by @seanchoi0519 (2021-07-02 07:49 UTC)

<p>I’ve fiddled around with editing the filepath in SlicerApp.arc as well as slicerlaunchersettings.ini to no avail. Could someone please help me? I have a custom .png file I’d like to change to.</p>

---

## Post #2 by @lassoan (2021-07-03 19:58 UTC)

<p>The first splash screen is displayed by the launcher and it is stored in a separate file (Slicer-SplashScreen.png) that you can easily replace. However, the second splash screen is displayed by SlicerApp-real.exe and it is embedded as a binary resource in the application that you can only replace if you build a <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">Slicer Custom Application</a>.</p>
<p>As a workaround, you can hide the splashscreen by launching the application like this:</p>
<pre><code>Slicer.exe --no-splash</code></pre>

---

## Post #3 by @seanchoi0519 (2021-07-05 12:58 UTC)

<p>Hello Prof Andras</p>
<p>I tried replacing the Slicer-SplashScreen.png file however it does not seem to do anything. Just so we’re on the same page, are you talking about the Slicer-SplashScreen.png located in the /images folder?</p>

---

## Post #4 by @seanchoi0519 (2021-07-05 12:59 UTC)

<p>If possible, I’d like to not use the terminal if possible as the reason I am replacing the splash screen is to make it available to my wider audience (research participants). Would there be absolutely no other way to change the second splash screen without having to start my project from scratch with the Slicer Custom Application?</p>

---

## Post #5 by @lassoan (2021-07-09 06:05 UTC)

<p>You can edit the <code>bin\SlicerLauncherSettings.ini</code> file so that no splashscreen is displayed:</p>
<pre><code class="lang-auto">[General]
launcherNoSplashScreen=true
...

[Application]
arguments=--no-splash
...
</code></pre>

---

## Post #6 by @seanchoi0519 (2021-07-14 14:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="18478">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>arguments=--no-splash</code></p>
</blockquote>
</aside>
<p>this does not seem to do anything <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2021-07-14 15:05 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="6" data-topic="18478">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>this does not seem to do anything</p>
</blockquote>
</aside>
<p>Well, it does what I described above. I don’t know what to say, so I just show a video proof of how the splash screens are shown, then changing one option hides one, and setting another option hides the second:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa3f742a9561b8543726b9d192f671f12eebb6c0.mp4">
  </div><p></p>
<p>Just repeat what is shown in the video on your computer and it will work for you, too.</p>

---
