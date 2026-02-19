---
topic_id: 19974
title: "Logo Area Cannot Be Reclaimed"
date: 2021-10-03
url: https://discourse.slicer.org/t/19974
---

# Logo area cannot be reclaimed

**Topic ID**: 19974
**Date**: 2021-10-03
**URL**: https://discourse.slicer.org/t/logo-area-cannot-be-reclaimed/19974

---

## Post #1 by @muratmaga (2021-10-03 05:21 UTC)

<p>We generally hide the slicer logo in the module panel to increase usable vertical space using the example int he script repo.</p>
<p>In the new preview version, logo is hidden, but the space is not reclaimed.<br>
Preview version<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d885e960c52f2db89f3622b1d79b9b164f125e5.png" alt="image" data-base62-sha1="6uNEHj0CjgnJ0qxcJmwjrtKqWCp" width="494" height="422"><br>
Stable version<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61943aea27d46908788b1ea1c789a9bc07a21f78.png" alt="image" data-base62-sha1="dVdTz7FqhvI6tYorC9RrYI5N3DO" width="523" height="242"></p>
<p>Would it be possible to bring back the old behavior?</p>

---

## Post #2 by @jamesobutler (2021-10-03 11:42 UTC)

<p>I honestly think you need to remove the following code from the SlicerMorph extension that is hiding the Slicer logo.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/67c622c4ab15f0a1dee2bb00dffde8dbcd5a91be/MorphPreferences/Resources/SlicerMorphRC.py#L60-L63">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/67c622c4ab15f0a1dee2bb00dffde8dbcd5a91be/MorphPreferences/Resources/SlicerMorphRC.py#L60-L63" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/67c622c4ab15f0a1dee2bb00dffde8dbcd5a91be/MorphPreferences/Resources/SlicerMorphRC.py#L60-L63" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/67c622c4ab15f0a1dee2bb00dffde8dbcd5a91be/MorphPreferences/Resources/SlicerMorphRC.py#L60-L63</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="60" style="counter-reset: li-counter 59 ;">
          <li>#
</li>
          <li>#hide SLicer logo in module tab
</li>
          <li>#
</li>
          <li>slicer.util.findChild(slicer.util.mainWindow(), 'LogoLabel').visible = False
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Removing of the logo for all users was discussed in a recent PR, but <a class="mention" href="/u/rkikinis">@rkikinis</a> had strong opinions on maintaining its visibility. See:</p>
<blockquote>
<p>The logo is a critical element of the branding of 3D Slicer. Having a recognizable brand helps with recognition in the user and and developer communities and with our fund raising. Visibility of the logo is very important to help prevent dilution of the brand.</p>
</blockquote>
<blockquote>
<p>I feel very strongly that maintaining the visibility and prominence of the Slicer logo at the top of the module panel is very important. I am strongly opposed to removing it and making it invisible. While we would gain a little space for engineering purposes, we would loose a lot in conveying that this is the 3D Slicer app.</p>
</blockquote>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5820#issuecomment-907882126">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5820#issuecomment-907882126" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
        to
        <a href="https://github.com/Slicer/Slicer/pull/5820#issuecomment-907882126" target="_blank" rel="noopener nofollow ugc">ENH: Move module panel logo into DataProbe collapsible area</a>
      </h4>



    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:hide-logo-left-panel</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hi all -

I checked with [Ron](https://en.wikipedia.org/wiki/Ron_Kikinis), who<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5820" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> many know is the person who really made Slicer happen as the original visionary, active promoter, dedicated user and tester, and long time PI on many grants that have and continue to fund the use and support of Slicer.  He asked me to pass this on:

&gt; The logo is a critical element of the branding of 3D Slicer. Having a recognizable brand helps with recognition in the user and and developer communities and with our fund raising. Visibility of the logo is very important to help prevent dilution of the brand.

&gt; I feel very strongly that maintaining the visibility and prominence of the Slicer logo at the top of the module panel is very important. I am strongly opposed to removing it and making it invisible. While we would gain a little space for engineering purposes, we would loose a lot in conveying that this is the 3D Slicer app.

So let's see what we can do to keep the logo visible.  Perhaps it could be made into a button the brings up the Data module as a popup; that could be very handy for quickly navigating the app, changing visibility, etc without losing context of the current module.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Under that philosophy about the logo usage, SlicerMorph developers shouldn’t be hiding the logo automatically for anyone who happens to download Slicer and then install the SlicerMorph extension. The logo should be prominently displayed. It also helps so that it is included in screenshots of the UI in tutorials that may be made using SlicerMorph modules.</p>
<p>It is one thing for one user to manually decide to hide the logo, but it is another thing for a developer to automatically hide the logo for all of its users after they install the SlicerMorph extension, especially the large SlicerMorph user base. Until you create a Slicer Custom App, as an extension you should continue to maintain Slicer design and not do custom app type actions.</p>

---

## Post #3 by @muratmaga (2021-10-03 15:17 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I honestly think you need to remove the following code from the SlicerMorph extension that is hiding the Slicer logo.</p>
</blockquote>
</aside>
<p>As documented <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/MorphPreferences">here</a>, SlicerMorph preferences are opt-in. It is up to the user to apply or not.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Removing of the logo for all users was discussed in a recent PR, but <a class="mention" href="/u/rkikinis">@rkikinis</a> had strong opinions on maintaining its visibility. See:</p>
</blockquote>
</aside>
<p>I respectfully disagree. We already have a very prominent splash screen that displays the logo. Having a static logo display inside the UI is not useful (at best ignored by the user, at worst takes important space). I cannot think of any other major program that embedded a static logo inside a functional space. If they are present, they are minimalist and unobtrusive at the menubars, edges of windows etc…</p>
<p>I completely agree that Slicer logo is important for the branding and distinction. I simply do not agree that particular spot is the best way to do that. Even the reduced width of that logo takes as much vertical space as a toolbar, which are functional.</p>
<p>Instead, what I would argue is that we need a very simple way of making an elegant looking (not too intrusive) visual that says something along the line “Created using 3D Slicer” (with  the logo  preferably) so that people who are sharing their screen captures on the social media can easily add to that, if they choose to do so.</p>

---

## Post #4 by @jamesobutler (2021-10-03 15:39 UTC)

<p>Maybe you and <a class="mention" href="/u/rkikinis">@rkikinis</a> and <a class="mention" href="/u/pieper">@pieper</a> (who knows the historical decisions of these things) can discuss to figure out a solution.</p>
<p>Not sure of what Slicer Extension policies are applied after an extension has been approved into the Slicer extensions index. <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a>, in general, are extensions allowed to modify Slicer core design and other core module behavior? Or are extensions only allowed to “extend” functionality? What should be done to prevent extensions from modifying core design and behavior? Hypothetically, would it be approved for an extension to redefine what a Slicer core keyboard shortcut does or redefine where the Slicer module panel is located? Just providing examples of how an extension may modify Slicer core.</p>

---

## Post #5 by @lassoan (2021-10-03 16:56 UTC)

<p>We reworked the module panel in recent Slicer Preview Release so that now in Slicer-4.13 the module panel header and footer (with the Data probe collapsed) has the same size as in Slicer-4.13 with the application logo hidden!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4df61ecff42b65ac3a688b130dc018bebbcae205.png" data-download-href="/uploads/short-url/b7G4GR9DcVkGj30R7wy958C2p2l.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4df61ecff42b65ac3a688b130dc018bebbcae205_2_690x395.png" alt="image" data-base62-sha1="b7G4GR9DcVkGj30R7wy958C2p2l" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4df61ecff42b65ac3a688b130dc018bebbcae205_2_690x395.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4df61ecff42b65ac3a688b130dc018bebbcae205_2_1035x592.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4df61ecff42b65ac3a688b130dc018bebbcae205_2_1380x790.png 2x" data-dominant-color="6A6A6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2761×1583 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By completely removing the application logo, 35 pixels could be gained (a single line of text), which would be rarely justified. I agree with <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that with this new Slicer version, it should not be necessary for SlicerMorph to hide the application logo anymore.</p>
<p>I’ve added more arguments to customize the application logo, which allow making that module panel header arbitrarily small, but a smaller header may be hard to hit with the mouse (and so it would be hard to move the docking window), so most likely it would only be used by custom applications. Example:</p>
<pre data-code-wrap="python"><code class="lang-python">setApplicationLogoVisible(scaleFactor=0.5)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886e4f431351dbe5f5fa2903c211e597d8922e0a.png" data-download-href="/uploads/short-url/jsVgWmbc3iqOLY6TCCcyywVw6oi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886e4f431351dbe5f5fa2903c211e597d8922e0a.png" alt="image" data-base62-sha1="jsVgWmbc3iqOLY6TCCcyywVw6oi" width="690" height="347" data-dominant-color="444242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×420 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="19974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>in general, are extensions allowed to modify Slicer core design and other core module behavior? Or are extensions only allowed to “extend” functionality? What should be done to prevent extensions from modifying core design and behavior? Hypothetically,</p>
</blockquote>
</aside>
<p>We would certainly need to step in if extensions started to override look and behavior of Slicer core, because it would make Slicer user experience inconsistent. It would also mean that Slicer core does not work well, so we would need to improve it.</p>
<p>I consider SlicerMorph customizations as quick, temporary changes to allow trying new ideas before they are mature enough to be implemented in Slicer core.</p>

---

## Post #6 by @muratmaga (2021-10-03 17:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="19974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>setApplicationLogoVisible(scaleFactor=0.5)</code></p>
</blockquote>
</aside>
<p>Where is this setting applied? In Slicer.ini?<br>
I am getting this error when typed in python terminal:</p>
<pre><code class="lang-auto">&gt; setApplicationLogoVisible(scaleFactor=0.5)
&gt; Traceback (most recent call last):
&gt;   File "&lt;console&gt;", line 1, in &lt;module&gt;
&gt; TypeError: setApplicationLogoVisible() got an unexpected keyword argument 'scaleFactor'
</code></pre>

---

## Post #7 by @lassoan (2021-10-03 17:44 UTC)

<p>I’ve added <code>scaleFactor</code> parameter today so it will be available in the Slicer Preview Release tomorrow. The default size should be good, though.</p>

---

## Post #8 by @muratmaga (2021-10-03 18:42 UTC)

<p>Thanks.<br>
I agree that new design is more space efficient than the previous one. Our issue is most of our users are on the stable (and we need the stable so that they can get SlicerMorph updates without having to reinstall slicer). Once there is a stable based on 4.13, I am ok to remove the customization to hide the logo from SlicerMorph.</p>
<p>However, I standby with the criticisms of inline SLicer logo that;</p>
<ol>
<li>Within the main application window is not doing much branding, in fact it is sort of an in your face and it is not clear what is its purpose. People using the Slicer daily will not even notice it. They already now they are using Slicer.</li>
<li>It is taking important vertical space, still as much as the height of a toolbar.</li>
<li>We need better branding tools (my suggestion on created by 3D Slicer or something along those lines) to facilitate brand recognition in social media, where nowadays how things are propagating.</li>
</ol>

---

## Post #9 by @lassoan (2021-10-03 19:46 UTC)

<p>We discussed these exact points many times over the years, most recently before the latest changes <a href="https://github.com/Slicer/Slicer/pull/5820">here</a>. Read the comments in the pull request to see all the other points that have been taken into account when we chose the current design over all the other evaluated options.</p>
<p>In short: You cannot simply remove the title bar of a dockable widget (without losing essential functionality). Making it slightly smaller would not make a big difference in usability. Making the title bar gradually smaller as the widget is being scrolled up (as it is done in the Slicer website) was not trivial to implement and again would just make a very small difference. We could not find any other good use of this small space (we tried to move the module selector toolbar widgets there but there was not enough space).</p>

---

## Post #10 by @lassoan (2021-10-04 03:36 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="19974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We need better branding tools (my suggestion on created by 3D Slicer or something along those lines) to facilitate brand recognition in social media, where nowadays how things are propagating</p>
</blockquote>
</aside>
<p>Can you elaborate on this? There is already an option to add Slicer logo to screen capture output, but I would find enabling it by default would be too aggressive. Would you make it easier to share screenshots/images/models directly to twitter/youtube?</p>

---

## Post #11 by @muratmaga (2021-10-04 04:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="19974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is already an option to add Slicer logo to screen capture output,</p>
</blockquote>
</aside>
<p>You mean the watermark feature in the screen capture module? THat’s the only one I am aware of and it is too buried. If there is another one, I dont think I know where it lives.</p>
<p>I am not sure how other people does their images for tweets, but I usually use the OS screen capture functionality, as it is far easier than using screen capture or snapshot and saving it to disk and then bringing it to twitter.</p>
<p>Perhaps adding a version of it to 3D window controls would be a bit more easy. Maybe under the … or the eye icons. Like a ruler that can be turned on/off</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93b4d2add2220f46d9f7c40a38cd92feefc4d84e.png" alt="" data-base62-sha1="l4FBaKDUt6W9X0am3bcvZS00Z5A" role="presentation" width="270" height="161"><br>
Another idea for less intrusive branding is the 3D axis: Can’t we make a 3D rendering of the Slicer icon and use it in the origin of the 3D axes, with a small caps 3D Slicer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c088b845385a8b20c5b4b7115c62642a87d07b5.png" alt="image" data-base62-sha1="1Is2iZcQDQkxPllEnWXXD0ubkDH" width="152" height="150"></p>

---

## Post #12 by @hherhold (2021-10-04 11:08 UTC)

<p>I like the branded axis idea a lot - I also just use the OS screen grab hot keys about 95% of the time, which often contains the axis.</p>

---
