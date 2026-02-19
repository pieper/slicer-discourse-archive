---
topic_id: 13935
title: "Slicer And Video Projector Issue"
date: 2020-10-08
url: https://discourse.slicer.org/t/13935
---

# Slicer and video projector issue

**Topic ID**: 13935
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/slicer-and-video-projector-issue/13935

---

## Post #1 by @PaoloZaffino (2020-10-08 14:12 UTC)

<p>Hi all,<br>
maybe it is not a proper “slicer related” question/issue, but maybe you can help me.</p>
<p>I connected my laptop (arch Linux/gnome) to a video projector to show something in Slicer.<br>
In order to make the Slicer windows more visible, I edited the resolution of the video projector.</p>
<p>Now, the problem is that if I connect the laptop on a second screen I see Slicer zoomed, even if it is not the video projector!<br>
The even stranger thing is that this happens only with my office second monitor…on my home screen this does not happen!</p>
<p>I tried to use another Slicer nightly version but nothing changes.<br>
Any tips for fixing the problem?</p>
<p>Thanks a lot!<br>
Paolo</p>

---

## Post #2 by @lassoan (2020-10-08 18:25 UTC)

<p>Can you post a screenshot of how Slicer is zoomed in? Are the fonts larger, too, or just the application window does not fit on the screen?</p>
<p>How is it with latest Slicer Stable Release?</p>
<p>You can also adjust these environment variables to customize application scaling: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html#runtime-environment-variables">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html#runtime-environment-variables</a></p>

---

## Post #3 by @lassoan (2020-10-10 02:55 UTC)

<p>Does erasing Slicer.ini fix the issue?</p>
<p>Other users reported issues with automatic restoring of window position after disconnecting a screen. We could try to apply additional checks for window restore (see <a href="https://bugreports.qt.io/browse/QTBUG-77385">here</a>), which may help.</p>
<p>We could also check if a specific key is held down during startup (e.g., Shift key is depressed, using <code>QGuiApplication::queryKeyboardModifiers()</code>), and if yes, then do not restore previously saved window position. Would we want this? (<a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/jcfr">@jcfr</a>)</p>

---

## Post #4 by @pieper (2020-10-10 12:56 UTC)

<p>Holding shift during startup to bypass previous settings sounds harmless in general and maybe super useful on special occasions.</p>

---

## Post #5 by @lassoan (2020-10-10 14:30 UTC)

<p>Would you bypass all settings or just skip restoring the window position?</p>

---

## Post #6 by @pieper (2020-10-10 14:39 UTC)

<p>It seems there could be other settings that would break things at startup, so a general way to bypass would be handy.  But maybe the window position issue is so common it deserves a dedicated solution?  I don’t know because this does not happen for me.</p>
<p>Actually wouldn’t running with the <code>--disable-settings --keep-temporary-settings</code> options fix the problem?</p>
<p>From <code>Slicer --help</code></p>
<pre><code class="lang-auto">  --disable-settings                            Start application ignoring user settings and using new temporary settings.
  --keep-temporary-settings                     Indicate whether temporary settings should be maintained.
</code></pre>

---

## Post #7 by @lassoan (2020-10-10 14:52 UTC)

<p>Yes, disable+keep settings does the same, but finding the Slicer executable, starting a terminal at that location, and copy-pasting a command there is too hard for many users.</p>
<p>Maybe we could add a shortcut that would launch Slicer with these options (not too hard to set it up in the Windows installer but I don’t know if it is available on Mac and Linux).</p>
<p>We could also provide a “Slicer maintanance tool” (maybe as a separate download), which would allow cleaning up Slicer.ini and version-specific Slicer-NNN.ini files, cleaning up Slicer installations, find/view logs, etc.</p>

---

## Post #8 by @PaoloZaffino (2020-10-10 15:04 UTC)

<p>Thanks for the tips.<br>
The screen is in my office (at home with a different second screen it is ok), so I’ll be able to run the tests in the next days.<br>
I’ll update you asap!</p>
<p>Paolo</p>

---

## Post #9 by @pieper (2020-10-10 15:23 UTC)

<p>Yes, a diagnostic tool / mode would make sense.  It’s easy to bundle a shell script with linux.  For mac we’d probably need a second app - instructions to open the terminal would probably be easier.</p>

---

## Post #10 by @PaoloZaffino (2020-10-20 11:16 UTC)

<p>Hi all,<br>
I ran the test, the options suggested didn’t fix the problem.</p>
<p>I attach a screenshot.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb3715983a419f4de01acf22e5635f43249ed8b4.png" data-download-href="/uploads/short-url/qIbiT6AGjSkExeUOA8Qjtohe1yk.png?dl=1" title="Slicer_screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb3715983a419f4de01acf22e5635f43249ed8b4_2_690x430.png" alt="Slicer_screenshot" data-base62-sha1="qIbiT6AGjSkExeUOA8Qjtohe1yk" width="690" height="430" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb3715983a419f4de01acf22e5635f43249ed8b4_2_690x430.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb3715983a419f4de01acf22e5635f43249ed8b4_2_1035x645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb3715983a419f4de01acf22e5635f43249ed8b4_2_1380x860.png 2x" data-dominant-color="C0BFC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_screenshot</span><span class="informations">1678×1046 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you.</p>
<p>Paolo</p>

---
