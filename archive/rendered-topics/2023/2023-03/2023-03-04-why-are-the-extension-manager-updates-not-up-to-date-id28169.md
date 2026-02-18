# Why are the extension manager updates not up-to-date?

**Topic ID**: 28169
**Date**: 2023-03-04
**URL**: https://discourse.slicer.org/t/why-are-the-extension-manager-updates-not-up-to-date/28169

---

## Post #1 by @rbumm (2023-03-04 16:36 UTC)

<p>After an update on a 3D Slicer cloud server with the extension manager, the Lung CT Analyzer extension is dated 20.2.2023 - a gap of one and a half weeks with many commits.<br>
How can I force an update?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ef302d2cd3d63e95d3887dca98678f581d9184.png" data-download-href="/uploads/short-url/bYw5tJitdthpbFk3GUO5Cloxwd6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53ef302d2cd3d63e95d3887dca98678f581d9184_2_690x260.png" alt="image" data-base62-sha1="bYw5tJitdthpbFk3GUO5Cloxwd6" width="690" height="260" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53ef302d2cd3d63e95d3887dca98678f581d9184_2_690x260.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ef302d2cd3d63e95d3887dca98678f581d9184.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ef302d2cd3d63e95d3887dca98678f581d9184.png 2x" data-dominant-color="E9EAF3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×267 26.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-03-04 17:17 UTC)

<p>Probably you need to install 5.2.2.  We only update extensions for the current release and preview versions.</p>

---

## Post #3 by @jamesobutler (2023-03-04 18:44 UTC)

<p>Maybe this is another place worthy of an update notification <a class="mention" href="/u/lassoan">@lassoan</a> ? It would equally be applied to each Slicer Preview build where entering the extensions manager days after the release would detail that these aren’t the latest versions of the extensions.</p>

---

## Post #4 by @lassoan (2023-03-04 19:27 UTC)

<p>We display a notification that the application is not up-to-date. This also means that none of the applications are up-to-date, but users are not explicitly told, so they are not aware of this. I’m not sure where should we display this information. Any suggestions are welcome.</p>

---

## Post #5 by @pieper (2023-03-04 20:03 UTC)

<p>How about a notice on the extension window that extensions are no longer being updated for the version currently in use?  That would be the time the user would need to know this information.</p>

---

## Post #6 by @lassoan (2023-03-05 05:44 UTC)

<p>This sounds good there is some space in the extensions manager next to the Restart/Close buttons:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d91f15d0e9de65e4842b67ef82923dc0b240b8a.jpeg" data-download-href="/uploads/short-url/1W2T49Tw5KTOYb68vyAuuSMNzfA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d91f15d0e9de65e4842b67ef82923dc0b240b8a_2_690x429.jpeg" alt="image" data-base62-sha1="1W2T49Tw5KTOYb68vyAuuSMNzfA" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d91f15d0e9de65e4842b67ef82923dc0b240b8a_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d91f15d0e9de65e4842b67ef82923dc0b240b8a_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d91f15d0e9de65e4842b67ef82923dc0b240b8a_2_1380x858.jpeg 2x" data-dominant-color="CED4D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1734×1079 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What would be the text?</p>
<blockquote>
<p>Update the application to receive extension updates.</p>
</blockquote>
<p>or</p>
<blockquote>
<p>This application version no longer receives extension updates.</p>
</blockquote>
<p>or</p>
<blockquote>
<p>A new application version is available. This version no longer receives extension updates.</p>
</blockquote>
<p>(there is no space for a lot of text)</p>

---

## Post #7 by @jamesobutler (2023-03-05 13:33 UTC)

<p>The first option is probably succinct enough. Or slightly modify to “…receive the latest extension updates.”</p>
<p>The “Check for updates” button at the top of the window should be disabled/hidden in this case to make it clear that this functionality is now unavailable for this version? Or I guess you could update to the last version of the extension for the given application version? I could imagine being confused that pressing “Check for updates” could get an update even though the text at the bottom of the window says the application doesn’t receive updates. The user could receive an extension update that is newer from what they already have installed but it is no longer guaranteed to be the latest version of the extension.</p>

---

## Post #8 by @pieper (2023-03-05 16:07 UTC)

<p>I know we like to avoid warning dialogs, but to me it would make sense that if you open the extension manager you would get a message like: “Extensions are not updated for the Slicer version you are using.  Please update to the latest release or preview build to install updated extensions.”  This could have a “don’t show again” option.</p>

---

## Post #9 by @rbumm (2023-03-05 16:22 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="28169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Extensions are not updated for the Slicer version you are using. Please update to the latest release or preview build to install updated extensions.</p>
</blockquote>
</aside>
<p>Thumbs up for this message box …</p>

---

## Post #10 by @muratmaga (2023-03-05 18:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="28169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Update the application to receive extension updates.</p>
</blockquote>
</aside>
<p>“Please update Slicer to the latest stable version to receive extension update.”</p>
<p>I really would like us to emphasize the distinction in stable version (as this feature is only available for stable releases).</p>
<p>I also like Steve’s suggestion of more intrusive popup box that is hard to avoid. i think if we do it once (as opposed to every time extension manager is brought forward) it will be ok.</p>

---

## Post #11 by @jamesobutler (2023-03-05 18:44 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="28169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>as this feature is only available for stable releases</p>
</blockquote>
</aside>
<p>Not quite. The <code>main</code> branch can go several days without a new commit. Extensions are still built each day so you can get multiple days of updated extensions for an individual preview release revision.</p>

---

## Post #12 by @muratmaga (2023-03-05 19:03 UTC)

<p>The point is though, you cannot update an extension installed in a preview version. The message does not make it clear which version of slicer to upgrade. As a user of 5.2.1 you can also intrepret this to get the latest and brightest in the preview version, and you won’t be getting any extension updates after you install the program.</p>

---

## Post #13 by @jamesobutler (2023-03-05 19:10 UTC)

<p>You can update an extension installed in a preview release.</p>
<p>For example Slicer 5.3.0 revision 31618 was built last night along with other extensions such as SlicerMorph. If you install that version of Slicer and SlicerMorph today, then if Slicer has no new commit pushed today, but if SlicerMorph has a commit pushed today, then tomorrow there would be an available extension update for SlicerMorph for Slicer 5.3.0 revision 31618.</p>
<p>A preview build version only becomes obsolete once there is a new commit pushed to the <code>main</code> branch.</p>

---

## Post #14 by @muratmaga (2023-03-05 19:12 UTC)

<p>But what if Slicer pushed a commit before we did? What you are describing is a corner case. We can’t rely on that to update extensions in a preview version.</p>

---

## Post #15 by @jamesobutler (2023-03-05 19:15 UTC)

<p>If Slicer pushes any commit today, then yes the preview build becomes obsolete. However at times over the weekend and especially during holidays there are often no new commits pushed to the <code>main</code> branch, however updated extensions will constantly be provided on a nightly basis.</p>

---

## Post #16 by @muratmaga (2023-03-05 19:18 UTC)

<p>Again the point is that continuous and reliable updates to extension is a feature that is only available in stable release. That’s what I am trying to communicate.</p>

---

## Post #17 by @jamesobutler (2023-03-05 19:20 UTC)

<p>Ok that is fine. Just pointing out that extensions can be updated when using a Slicer Preview release if that preview release is &gt;1 days old and is the latest preview release.</p>

---

## Post #18 by @rbumm (2023-03-06 06:18 UTC)

<p>It would be great if a new Slicer stable version could automatically detect. which extensions were installed previously in stable on that computer, and install all of them in one go.</p>

---
