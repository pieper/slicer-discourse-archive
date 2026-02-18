# Drawing Circle on CT Image

**Topic ID**: 20387
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/drawing-circle-on-ct-image/20387

---

## Post #1 by @ckbow (2021-10-27 14:12 UTC)

<p>Is it possible to draw a circle (markup) on a CT image? I initially tried using the Closed Curve Markup, but I do not know how to make or adjust it into a circle. I need to be able to align the perimeter of the circle with the cortices of the bone, while having a visible midpoint to determine the bone’s midline (as shown).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f3fbd42a344f53a092a9a8fd8bcca857eedd8cb.jpeg" data-download-href="/uploads/short-url/kreQ1sLa4CpgjYR2Yh866pkSieL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f3fbd42a344f53a092a9a8fd8bcca857eedd8cb.jpeg" alt="image" data-base62-sha1="kreQ1sLa4CpgjYR2Yh866pkSieL" width="489" height="500" data-dominant-color="6E6C6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">515×526 58.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-10-27 16:24 UTC)

<p>In Slicer we focus on 3D operations and don’t have much support for drawing 2D shapes like circles.  Instead you could use a 3D fiducial (point with radius) to fit the 3D shape of the bone.  Then you could use a 3D line for the bone axis.  See the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">Markups module</a>.</p>

---

## Post #3 by @lassoan (2021-10-28 12:55 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Instead you could use a 3D fiducial (point with radius) to fit the 3D shape of the bone.</p>
</blockquote>
</aside>
<p>You can also use 2 points of a markups fiducial node to specify a circle by copy-pasting a few lines of code to into the Python console as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">this example</a>.</p>
<p>I’ve created a modified script that allows you to place 2 circles by specifying 6 points on the circumference: <a href="https://gist.github.com/lassoan/99514fb5edf98e1e3dda926253dc9742" class="inline-onebox">Compute bone axis in 3D Slicer by specifying two circles. · GitHub</a></p>
<p>You can use this by placing one fiducial list containing 6 points then copy-pasting into the Python console:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="1DG3y1TqWvw" data-video-title="Custom interactive measurement using Python scripting" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=1DG3y1TqWvw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/1DG3y1TqWvw/maxresdefault.jpg" title="Custom interactive measurement using Python scripting" width="" height="">
  </a>
</div>


---

## Post #4 by @ckbow (2021-10-29 16:25 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Instead you could use a 3D fiducial (point with radius) to fit the 3D shape of the bone.</p>
</blockquote>
</aside>
<p>With this approach, I have managed to get a circular region of interest. However, I am not able to get a separate circle when I run the code again with a new set of fiducial points.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve created a modified script that allows you to place 2 circles by specifying 6 points on the circumference</p>
</blockquote>
</aside>
<p>With this approach, I am running into a similar issue. I am able to get the first set of two circles, but I am not able to get the second set of two circles on a different bone. (I need two circles to define each bone axis, as well as two bone axes to measure joint flexion angle).</p>

---

## Post #5 by @lassoan (2021-10-29 16:34 UTC)

<aside class="quote no-group" data-username="ckbow" data-post="4" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/49beb7/48.png" class="avatar"> ckbow:</div>
<blockquote>
<p>With this approach, I am running into a similar issue. I am able to get the first set of two circles, but I am not able to get the second set of two circles on a different bone. (I need two circles to define each bone axis, as well as two bone axes to measure joint flexion angle).</p>
</blockquote>
</aside>
<p>Yes, sure, based on the workflow you want to implement you need to tune the script.</p>
<p>For example, you can add a keyboard shortcut to call a function that adds measurement results to a table node and clears the fiducial points so that you can place the points again. This is a quick solution if you are the only person who performs these measurements.</p>
<p>You can also write a Slicer Python scripted module that observes markups fiducial lists that the module adds to the scene and add the model nodes as needed. See the <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/BafflePlanner">Baffle Planner module in SlicerHeart extension</a> as an example. This requires more work than just crafting a python script in the Python console, but it is worth it if you want to create user-friendly tool that other people can use, too.</p>
<p>The most sophisticated level is to create a custom widget representation, which renders the fiducial list as two circles and a line. This should be quite simple to do in C++ (you can define a new markup type by deriving from an existing type and override anything in it), but we have not made the classes customizable in Python yet.</p>

---

## Post #6 by @reynvw (2022-11-17 14:34 UTC)

<p>Hi,</p>
<p>I have come across this section because I need to use a circle as well in 2D (with a central point, because I want to be able to calculate the radius) and your first suggestion works perfectly for that. However, I have problems removing the circle from my image, if I remove the control points the circle stays and I can not move it anymore. Is there any solution for that?</p>
<p>Also, is there an option to view the radius of the created circle? That way I don’t have to go and measure it for every circle I make.</p>
<p>Thanks a lot,<br>
from a medical student</p>

---

## Post #7 by @chir.set (2022-11-17 15:10 UTC)

<p>If you can build Slicer, you may build <a href="https://github.com/chir-set/ExtraMarkups" rel="noopener nofollow ugc">this</a> extension. It has a custom markups that will do what you want.  (It’s somehow funny because it is this very opening post that prompted me to write this extension). If you can’t build software, it’s not the right tool for you.</p>

---

## Post #8 by @reynvw (2022-11-17 15:42 UTC)

<p>I don’t know almost anything about coding or building software so I am not sure. The provided code is actually already perfectly what I need, it’s just annoying sometimes that the yellow circle stays in all my 2D planes when I don’t need it anymore.</p>
<p>Thanks for your reply though!</p>

---

## Post #9 by @muratmaga (2022-11-17 17:34 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="20387" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>If you can build Slicer, you may build <a href="https://github.com/chir-set/ExtraMarkups">this </a> extension. It has a custom markups that will do what you want. (It’s somehow funny because it is this very opening post that prompted me to write this extension). If you can’t build software, it’s not the right tool for you.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/chir.set">@chir.set</a> This looks useful, particularly the label one. Is there a reason why you are not making this part of the extension catalog (like the surface markup add on is)?</p>

---

## Post #10 by @chir.set (2022-11-17 17:48 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is there a reason why you are not making this part of the extension catalog</p>
</blockquote>
</aside>
<ol>
<li>
<p>It did not trigger much interest on previous evaluation requests.</p>
</li>
<li>
<p>Bureaucracy is significant when submitting an extension. We have to interact with robots and it’s not an easy one. But it’s not a hard blocker as such.</p>
</li>
</ol>

---

## Post #11 by @lassoan (2022-11-17 19:20 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="10" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It did not trigger much interest on previous evaluation requests</p>
</blockquote>
</aside>
<p>It seems that there is some interest, so you may reconsider now.</p>
<aside class="quote no-group" data-username="chir.set" data-post="10" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Bureaucracy is significant when submitting an extension. We have to interact with robots and it’s not an easy one. But it’s not a hard blocker as such.</p>
</blockquote>
</aside>
<p>This is the checklist you need to complete:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md" target="_blank" rel="noopener">Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md</a></h4>


      <pre><code class="lang-md">&lt;!--
Thank you for contributing to 3D Slicer!
- To add a new extension with this pull request: Please keep content of "New extension" section and put an 'x' in the brackets for each todo item to indicate that you have accomplished that prerequisite.
- To update an existing extension with this pull request: Please delete all text in this template and just describe which extension is updated and optionally tell us in a sentence what has been changed. To make extension updates easier in the future you may consider replacing specific git hash in your s4ext file by a branch name (for example: `main` for Slicer Preview Releases; `(majorVersion).(minorVersion)` such as `4.10` for Slicer Stable Releases).
--&gt;

# New extension

&lt;!-- To make sure users can find your extension, understand what it is intended for and how to use it, please complete the checklist below. You do not need to complete all the item by the time you submit the pull request, but most likely the changes will only be merged if all the tasks are done. See more information about the submission process here: https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html --&gt;

- [ ] Extension has a reasonable name (not too general, not too narrow, suggests what the extension is for)
- [ ] Repository name is Slicer+ExtensionName
- [ ] Repository is associated with `3d-slicer-extension` GitHub topic so that it is listed [here](https://github.com/topics/3d-slicer-extension). To edit topics, click the settings icon in the right side of "About" section header and enter `3d-slicer-extension` in "Topics" and click "Save changes". To learn more about topics, read https://help.github.com/en/articles/about-topics
- [ ] Extension description summarizes in 1-2 sentences what the extension is usable (should be understandable for non-experts)
- [ ] Any known related patents must be mentioned in the extension description.
- [ ] LICENSE.txt is present in the repository root. MIT  (https://choosealicense.com/licenses/mit/) or Apache (https://choosealicense.com/licenses/apache-2.0/) license is recommended. If source code license is more restrictive for users than MIT, BSD, Apache, or 3D Slicer license then the name of the used license must be mentioned in the extension description.
- [ ] Extension URL and revision (scmurl, scmrevision) is correct, consider using a branch name (main, release, ...) instead of a specific git hash to avoid re-submitting pull request whenever the extension is updated
- [ ] Extension icon URL is correct (do not use the icon's webpage but the raw data download URL that you get from the download button - it should look something like this: https://raw.githubusercontent.com/user/repo/main/SomeIcon.png)
- [ ] Screenshot URLs (screenshoturls) are correct, contains at least one
- [ ] Homepage URL points to valid webpage containing the following:
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/.github/PULL_REQUEST_TEMPLATE.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As I see, you can check out almost all the boxes, so it should not be a lot of extra work.</p>
<p>Slicer extensions submission process is not very automated, so dealing with robots should not be a big issue. Usually the main challenge is availability of reviewers, but we do our best.</p>

---

## Post #12 by @chir.set (2022-11-17 19:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we do our best</p>
</blockquote>
</aside>
<p>I don’t have any doubt about that.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>so you may reconsider now</p>
</blockquote>
</aside>
<p>I’ll start preparing the work for the extension catalog ASAP.</p>

---

## Post #13 by @chir.set (2022-11-20 18:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="20387">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>making this part of the extension catalog</p>
</blockquote>
</aside>
<p>The PR is <a href="https://github.com/Slicer/ExtensionsIndex/pull/1897" rel="noopener nofollow ugc">here</a> in the extension index. I don’t know how it is further processed, wait and see.</p>

---
