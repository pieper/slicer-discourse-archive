# Splash Screen Showing Version Number

**Topic ID**: 804
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/splash-screen-showing-version-number/804

---

## Post #1 by @moselhy (2017-08-01 17:05 UTC)

<p>I think it would be nice if the splash screen displayed the version number in the top-right corner. Like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603ae3c6a636497b7c03f6ba5d4257d451e1d063.jpeg" data-download-href="/uploads/short-url/dJi0ufJf9gA4O6mxfiFKV2HJIe7.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/603ae3c6a636497b7c03f6ba5d4257d451e1d063_2_690x456.jpg" alt="image" data-base62-sha1="dJi0ufJf9gA4O6mxfiFKV2HJIe7" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/603ae3c6a636497b7c03f6ba5d4257d451e1d063_2_690x456.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603ae3c6a636497b7c03f6ba5d4257d451e1d063.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603ae3c6a636497b7c03f6ba5d4257d451e1d063.jpeg 2x" data-dominant-color="E7E6E6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×478 61.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am having a hard time implementing a static message (version number), because the <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Main.cxx#L89" rel="noopener nofollow ugc">showMessage() function</a> is made for dynamic messages only.</p>

---

## Post #2 by @jcfr (2017-08-01 17:21 UTC)

<p>Hi,</p>
<p>To provide some more context, the splashscreen is displayed at two different times:</p>
<ul>
<li>by the <a href="https://github.com/commontk/AppLauncher">application launcher</a> while the application is loaded.</li>
<li>by the Slicer application itself while the modules are loaded</li>
</ul>
<p>If you would like the version info to be visible through the entire loading time, both steps should probably be considered.</p>
<p>A simple solution (but not so elegant) would be to regenerate a new splashscreen daily. The cons of this approach is that it would bloat the Slicer history …</p>
<p>A more complete solution would be to teach both Slicer and the launcher to display version on top of the splashscreen</p>

---

## Post #3 by @moselhy (2017-08-01 17:24 UTC)

<blockquote>
<p>A more complete solution would be to teach both Slicer and the launcher to display version on top of the splashscreen</p>
</blockquote>
<p>Would it be efficient to connect the version display function to the messageChanged signal of the splash screen? If not, is there a better way?</p>

---

## Post #4 by @jcfr (2017-08-01 17:42 UTC)

<aside class="quote no-group" data-username="moselhy" data-post="3" data-topic="804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moselhy/48/501_2.png" class="avatar"> moselhy:</div>
<blockquote>
<p>If not, is there a better way?</p>
</blockquote>
</aside>
<p>I do not think connecting to <code>messageChanged</code> will be helpful. A possible approach would be subclass <code>QSplashScreen</code> into <code>ctkSplashScreen</code> by adding a method like <code>showCornerMessage(const QString&amp; msg, Qt::Corner corner)</code>.</p>
<p>The <code>ctkSplashScreen</code> class could be added to <a href="https://github.com/commontk/CTK">CTK</a> and then reused in both Slicer and the launcher.</p>
<p>You could look at <code>QSplashScreen::drawContents(QPainter *painter)</code> to understand how the Qt API works.</p>

---

## Post #5 by @lassoan (2017-08-01 17:54 UTC)

<p>Do you really need to show versin info in the splash screen? We already have an about dialog that shows detailed version information and version is always visible in the title bar as well. Splash screen is only shown for a couple of seconds and you cannot copy-paste from it, so I think overall the about box is more useful.</p>

---

## Post #6 by @moselhy (2017-08-01 18:04 UTC)

<p>It would be convenient for me because I have a button to terminate the Slicer process, which I could easily click if I find that I am loading the incorrect version of Slicer. It could be useful for other users having a similar setup to me.</p>

---

## Post #7 by @lassoan (2017-08-01 18:24 UTC)

<p>I see. This use case makes sense but it is very narrow and I would not encourage anyone to to forcefully terminate an application (in unfortunate cases it might corrupt settings files etc).</p>

---
