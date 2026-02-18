# Slow application start if recently used file is on unavailable network

**Topic ID**: 25970
**Date**: 2022-10-29
**URL**: https://discourse.slicer.org/t/slow-application-start-if-recently-used-file-is-on-unavailable-network/25970

---

## Post #1 by @jamesobutler (2022-10-29 20:33 UTC)

<p>Maybe this is what I noticed today where it was hanging at initialization and would finally load modules after a noticeable delay. This happening on launch of the application (not just first startup). I use a multi monitor setup with my HP laptop and so maybe had Slicer last up on a multiple monitor, but this hang I observed today was without any external displays connected.</p>

---

## Post #2 by @lassoan (2022-10-29 20:55 UTC)

<p>Delayed startup is most likely a different issue than not starting at all. Delay may be due to Windows malware checks.</p>
<p>Are subsequent startups faster? Is startup slow again after restarting Windows?</p>

---

## Post #3 by @jamesobutler (2022-10-29 21:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are subsequent startups faster? Is startup slow again after restarting Windows?</p>
</blockquote>
</aside>
<p>Subsequent startups where equally slow and restarting Windows didn’t help.</p>
<p>It was only once I deleted the following file that it was fast to start again:<br>
“C:\Users\butlej30383\AppData\Roaming\NA-MIC\Slicer.ini”</p>
<p>I haven’t yet narrowed down the specific setting that might be causing the issue.</p>

---

## Post #4 by @lassoan (2022-10-30 01:43 UTC)

<p>It might have been an an extension that did some time-consuming operations at startup.</p>

---

## Post #5 by @jamesobutler (2022-10-30 05:23 UTC)

<p>Apologies if I have discovered a separate issue from what the “Slicer doesn’t load” original author was posting about.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I didn’t have any extensions installed so I continued debugging. I was able to narrow it down to a setting specifying a recent file that is unavailable because it was on a local file share at work that I don’t have access to at home.</p>
<p>Slicer was hanging at the splash screen showing “Initializing user interface…” where it took 45 seconds for it to finally begin loading modules as seen on the splash screen. Once I removed the following key (see below) from the <code>RecentlyLoadedFiles</code> section, the startup of Slicer was back to being fast. I couldn’t even see “Initializing user interface…” at the splash screen because it was so fast.</p>
<p>Is Slicer doing checks on the recent files to determine if they are still present and in this case that request to the local file share (that isn’t connected anymore) takes a long time and only reaches a timeout after 45 seconds for that request?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/291df806e97fcf5080568ec67e54dcb4b2f0afa3.png" data-download-href="/uploads/short-url/5RJMCIl6OA6AqEIQw9L9KeTKsRt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291df806e97fcf5080568ec67e54dcb4b2f0afa3_2_690x110.png" alt="image" data-base62-sha1="5RJMCIl6OA6AqEIQw9L9KeTKsRt" width="690" height="110" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291df806e97fcf5080568ec67e54dcb4b2f0afa3_2_690x110.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291df806e97fcf5080568ec67e54dcb4b2f0afa3_2_1035x165.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/291df806e97fcf5080568ec67e54dcb4b2f0afa3_2_1380x220.png 2x" data-dominant-color="D4D5D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1559×249 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><code>RecentFiles\1\file=@Variant(\0\0\0\b\0\0\0\n\0\0\0\x14\0s\0i\0n\0g\0l\0\x65\0\x46\0i\0l\0\x65\0\0\0\x1\x1\0\0\0\b\0s\0h\0o\0w\0\0\0\x1\x1\0\0\0\xe\0n\0o\0\x64\0\x65\0I\0\x44\0s\0\0\0\v\0\0\0\x1\0\0\0\x30\0v\0t\0k\0M\0R\0M\0L\0S\0\x63\0\x61\0l\0\x61\0r\0V\0o\0l\0u\0m\0\x65\0N\0o\0\x64\0\x65\0\x31\0\0\0\b\0n\0\x61\0m\0\x65\0\0\0\n\0\0\0\x1a\0U\0n\0\x66\0u\0s\0\x65\0\x64\0V\0o\0l\0u\0m\0\x65\0\0\0\x10\0l\0\x61\0\x62\0\x65\0l\0m\0\x61\0p\0\0\0\x1\0\0\0\0\x10\0\x66\0i\0l\0\x65\0T\0y\0p\0\x65\0\0\0\n\0\0\0\x14\0V\0o\0l\0u\0m\0\x65\0\x46\0i\0l\0\x65\0\0\0\x10\0\x66\0i\0l\0\x65\0N\0\x61\0m\0\x65\0\0\0\n\0\0\x1n\0/\0/\0\x31\0\x39\0\x32\0.\0\x31\0\x36\0\x38\0.\0\x31\0.\0\x36\0\x39\0/\0G\0\x65\0n\0\x65\0r\0\x61\0l\0_\0I\0m\0\x61\0g\0\x65\0s\0/\0R\0&amp;\0\x44\0 \0\x44\0\x61\0t\0\x61\0/\0Q\0\x41\0 \0\x61\0n\0\x64\0 \0Q\0\x43\0/\0Q\0\x43\0 \0\x44\0\x61\0t\0\x61\0 \0R\0\x65\0p\0o\0s\0i\0t\0o\0r\0y\0/\0S\0V\0L\0\x31\0\x32\0/\0\x30\0\x39\0\x32\0\x32\0\x32\0\x32\0/\0Q\0u\0\x61\0l\0i\0t\0y\0\x43\0o\0n\0t\0r\0o\0l\0/\0\x32\0\x30\0\x32\0\x32\0_\0\x30\0\x37\0_\0\x30\0\x39\0/\0U\0l\0t\0r\0\x61\0s\0o\0u\0n\0\x64\0 \0S\0t\0r\0\x65\0\x61\0m\0 \0T\0\x65\0s\0t\0s\0/\0\x42\0-\0M\0o\0\x64\0\x65\0_\0\x32\0\x44\0 \0S\0\x63\0\x61\0n\0_\0\x32\0\x30\0\x32\0\x32\0_\0\x30\0\x37\0_\0\x30\0\x39\0-\0\x32\0\x30\0_\0\x31\0\x34\0_\0\x30\0\x37\0/\0U\0n\0\x66\0u\0s\0\x65\0\x64\0V\0o\0l\0u\0m\0\x65\0.\0m\0h\0\x64\0\0\0$\0\x64\0i\0s\0\x63\0\x61\0r\0\x64\0O\0r\0i\0\x65\0n\0t\0\x61\0t\0i\0o\0n\0\0\0\x1\0\0\0\0\x16\0\x63\0o\0l\0o\0r\0N\0o\0\x64\0\x65\0I\0\x44\0\0\0\n\0\0\0\x32\0v\0t\0k\0M\0R\0M\0L\0\x43\0o\0l\0o\0r\0T\0\x61\0\x62\0l\0\x65\0N\0o\0\x64\0\x65\0G\0r\0\x65\0y\0\0\0\f\0\x63\0\x65\0n\0t\0\x65\0r\0\0\0\x1\0)</code></p>

---

## Post #6 by @lassoan (2022-10-30 12:12 UTC)

<p>Thank you for the investigation,this is a very interesting find. Network resources may take some time to become available, so it makes sense for the operating system to wait for them a bit.</p>
<p>Graying out unavailable files in the recent file list is a nice feature, but maybe we should replace it by an on-demand check, when the user selects an item. In case of failure, a popup could be displayed that has the option of removing the file from the list.</p>
<p>Could you submit an issue to the Slicer bugtracker about this? Thank you!</p>

---

## Post #7 by @jamesobutler (2022-10-30 15:26 UTC)

<p>Issue created:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6631">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6631" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6631" target="_blank" rel="noopener nofollow ugc">Slow application start if recently used file is on unavailable network</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-10-30" data-time="15:26:39" data-timezone="UTC">03:26PM - 30 Oct 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As originally discussed at https://discourse.slicer.org/t/slow-application-start<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">-if-recently-used-file-is-on-unavailable-network/25970/5.

While at work I opened a file in 3D Slicer that I had accessed from a local file share that is on our corporate network. When I went home and tried to start Slicer it was hanging at the "Initializing user interface..." step on the splash screen for 45 seconds before proceeding to load the Slicer modules. This was due to a setting for the recent files including the path to the local file share that I no longer had access to from my home network.

https://user-images.githubusercontent.com/15837524/198886694-549dc9ef-0bd9-4a79-81fd-a109248d2008.mp4

@lassoan has suggested maybe changing this to a runtime check rather than at startup. I also don't see a reason to wait 45 seconds trying to see if a file is still accessible from a file share location.

The specific code of interest is this section in `restoreGUIState`:
https://github.com/Slicer/Slicer/blob/9a56f644406357394f42004133c6ee13ae7e3ad3/Base/QTApp/qSlicerMainWindow.cxx#L1694-L1702

## Environment
- Slicer version: Slicer-5.1.0-2022-10-28, Slicer 5.0.3
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @fbordignon (2025-10-09 11:59 UTC)

<p>Hi guys, we are facing this issue right now. Our users are in a distributed filesystem environment that uses large files and scenes that cannot be saved locally. Most of the .mrml scenes are on network locations. Often times they move the mrml or delete them, and it takes 1m to timeout for each invalid path at the recent files list. One invalid network path takes the app launch time from 20s to 1m20s</p>
<p>Would it be a solution to have this check completely removed at startup and let the error happen when the user clicks to load a recent file that is not available?</p>
<p>Thanks in advance</p>

---

## Post #9 by @jamesobutler (2025-10-09 13:06 UTC)

<p>I would agree that the app should not check if the file still exists at startup when populating the recent files menu. It should just add the list of items and therefore will no longer show unavailable entries as disabled items in the menu. Upon clicking an item that is missing/unavailable the load event should fail. The item in the recent list should remain as-is and stay enabled as the file may be restored to its original location or the network connection may be restored to make it available.</p>

---

## Post #10 by @lassoan (2025-10-10 12:59 UTC)

<p>It is nice if it is visible that a file is unavailable, but I agree it is not worth delaying the application startup (or showing of the menu because of it), when the delay is long. We should do the check each time the most recently used file list is shown and disable the check for non-local files. But if these are not trivial to implement then it is simpler to just remove this check completely (it would be just a minor inconvenience for users, not happening very frequently).</p>

---

## Post #11 by @pieper (2025-10-11 03:08 UTC)

<p>Another option is to do this kind of operation asynchronously.</p>

---

## Post #12 by @lassoan (2025-10-11 03:17 UTC)

<blockquote>
<p>Another option is to do this kind of operation asynchronously.</p>
</blockquote>
<p>Yes, we cannot block the GUI each time the user open the most recently used files section, so if there is any check then it must be done in the background.</p>

---
