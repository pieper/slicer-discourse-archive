---
topic_id: 40883
title: "Windows Font Scaling Issue On Laptop Screens"
date: 2024-12-28
url: https://discourse.slicer.org/t/40883
---

# Windows font scaling issue on laptop screens

**Topic ID**: 40883
**Date**: 2024-12-28
**URL**: https://discourse.slicer.org/t/windows-font-scaling-issue-on-laptop-screens/40883

---

## Post #1 by @muratmaga (2024-12-28 11:53 UTC)

<p>During our latest SlicerMorph short course, students used their laptops most of which were 14" screen and typical 1920x1080 resolution.</p>
<p>In certain situations (often when Slicer application window is maximized), when user switches between modules, the layout gets messed up and often ends up in a unrecoverable state.  (For example in the 4up view, the yellow slice and/or 3D view may end up stretching beyond visible screen). Trying different layouts, switching to a module to minimize the width of the module panel has not effect. Not even closing and restarting the application window seems to help.</p>
<p>In almost all cases, the remedy is to go the windows display settings and reduce the font scaling. In 5-6 cases I have observed through out the week, default font scaling was 175% and in all cases, bringing it down to 100% and then increasing the menu font sizes inside the Slicer help resolved the issue.</p>
<p>I was too busy to make a screen recording of the issue, hopefully my verbal description is helpful. 5-6 cases in 28 attendees for a week seemed like a quite high incidence to chalk it up to chance. We have used the preview r33154 during the course.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2024-12-28 23:42 UTC)

<p>Thanks for reporting, this is useful feedback. Widget layout issues cannot always be resolved, especially when font size is set to larger than default, but there are several approaches to address this.</p>
<ol>
<li>Fixing problematic widgets</li>
</ol>
<p>There are specific widgets with sizing policies that cannot accommodate larger text/smaller screen. Could you give a list of modules/widgets that caused most of the trouble? We could try to redesign them.</p>
<ol start="2">
<li>User education</li>
</ol>
<p>For the remaining, less frequently occurring issues, user education (better documentation, notes in tutorials) could work.</p>
<p>Application scaling and font size can be set in Windows per application: when you right-click on SlicerApp-real.exe application icon in the task bar, choose “Properties”, and then in “Compatibility” section you get lots of options in “Change high DPI settings”.</p>
<p>You can also edit options in Slicer: font size in application settings, and various <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#runtime-environment-variables">scaling environment variables</a>.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="40883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In certain situations (often when Slicer application window is maximized), when user switches between modules, the layout gets messed up and often ends up in a unrecoverable state</p>
</blockquote>
</aside>
<p>Application window size has a hard limit when the application is maximized. Therefore, when sizing policies and the chosen font size caused irresolvable conflict, the behavior can be quite unpredictable. To get back to a reasonable behavior, you can un-maximize the window and maximize it again.</p>

---

## Post #3 by @muratmaga (2024-12-28 23:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="40883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are specific widgets with sizing policies that cannot accommodate larger text/smaller screen. Could you give a list of modules/widgets that caused most of the trouble? We could try to redesign them.</p>
</blockquote>
</aside>
<p>Unfortunately, I don’t know which modules triggered these problems.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="40883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Application scaling and font size can be set in Windows per application: when you right-click on SlicerApp-real.exe application icon in the task bar, choose “Properties”, and then in “Compatibility” section you get lots of options in “Change high DPI settings”.</p>
</blockquote>
</aside>
<p>I didn’t know this was possible. Application specific scaling makes more sense, as sometimes reducing the scaling to 100-125% made the windows UI difficult to use. Can we add this to slicer documentation? Do we have troubleshoot section in <a href="http://slicer.readthedocs.io" rel="noopener nofollow ugc">slicer.readthedocs.io</a>?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="40883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To get back to a reasonable behavior, you can un-maximize the window and maximize it again.</p>
</blockquote>
</aside>
<p>This did not recover the layout (i.e, in 4up view layout yellow 3D views stayed extended outside of the display).</p>

---
