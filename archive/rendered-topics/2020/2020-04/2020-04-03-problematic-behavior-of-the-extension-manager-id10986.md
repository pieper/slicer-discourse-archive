---
topic_id: 10986
title: "Problematic Behavior Of The Extension Manager"
date: 2020-04-03
url: https://discourse.slicer.org/t/10986
---

# Problematic behavior of the extension manager

**Topic ID**: 10986
**Date**: 2020-04-03
**URL**: https://discourse.slicer.org/t/problematic-behavior-of-the-extension-manager/10986

---

## Post #1 by @rkikinis (2020-04-03 23:06 UTC)

<p>Operating system: Mac OS 10.15.4<br>
Slicer version: Slicer-4.11.0-2020-04-01-macosx-amd64<br>
Actual behavior:<br>
Something is broken/bizarre with the extension manager. I need to click twice for the window to appear and the history tab is empty. After I install some extensions, i do not get a prompt to restart. When I close the extension manager and exit slicer, then the extension manager window pops up on its own and prompts for a restart.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d162ea6292e6072eecaad3132530918d0bc73ca7.png" data-download-href="/uploads/short-url/tSjIrWLDB7Y513JAbsTCb5p2Aab.png?dl=1" title="Screen Shot 2020-04-03 at 7.05.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d162ea6292e6072eecaad3132530918d0bc73ca7_2_690x210.png" alt="Screen Shot 2020-04-03 at 7.05.41 PM" data-base62-sha1="tSjIrWLDB7Y513JAbsTCb5p2Aab" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d162ea6292e6072eecaad3132530918d0bc73ca7_2_690x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d162ea6292e6072eecaad3132530918d0bc73ca7_2_1035x315.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d162ea6292e6072eecaad3132530918d0bc73ca7_2_1380x420.png 2x" data-dominant-color="586067"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-03 at 7.05.41 PM</span><span class="informations">1486×454 52.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-04 20:37 UTC)

<p>These issues are certainly annoying. I’ve submitted a bug report on the issue tracker to discuss it there and make sure it is included in the Slicer5 roadmap.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4806" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4806" target="_blank">Extension manager is slow</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-04-04" data-time="20:35:02" data-timezone="UTC">08:35PM - 04 Apr 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">From @rkikinis:
Operating system: Mac OS 10.15.4
Slicer version: Slicer-4.11.0-2020-04-01-macosx-amd64
Actual behavior:
Something is broken/bizarre with the extension manager. I need to click twice for...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">priority:medium</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mikebind (2020-05-28 23:04 UTC)

<p>Just want to add that I get the same thing on Windows when I install a new Slicer Nightly.  It takes two clicks to open the extension manager, then it loads with nothing in it, then it transiently shows several error messages like: <code>{1e8be032-811c-4583-b51d-7da23cafc52d}: 5: Operation canceled</code>.  It shows nothing listed in extensions to restore or manage, and the “install” tab initially shows nothing, then eventually shows the list of categories.  Clicking on a category launches another interminable wait.  Minutes later, there is something in the list of extensions to restore, although today it is telling me that none of those extensions are usable in the current nightly preview (2020-05-27 on Windows), which means I can’t really use this version and will need to go back to an earlier version.</p>
<p>Is there a way to tell whether a particular extension is supported in a release? I looked at the CDash dashboard, but I couldn’t make sense of it. I regularly use SlicerJupyter, SegmentEditorExtraEffects, and SlicerOpenCV, and the current nightly’s extension manager is telling me that none of these are compatible.</p>

---

## Post #4 by @mikebind (2020-05-28 23:14 UTC)

<p>It’s now been about 30min, and this is still what the Extension manager shows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94e6c82704a96d40f5dcd0fea95d5f71f65ae0b6.png" data-download-href="/uploads/short-url/lff726gkiFw8zw8bkFkgw2jIYWG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94e6c82704a96d40f5dcd0fea95d5f71f65ae0b6_2_690x385.png" alt="image" data-base62-sha1="lff726gkiFw8zw8bkFkgw2jIYWG" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94e6c82704a96d40f5dcd0fea95d5f71f65ae0b6_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94e6c82704a96d40f5dcd0fea95d5f71f65ae0b6_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94e6c82704a96d40f5dcd0fea95d5f71f65ae0b6_2_1380x770.png 2x" data-dominant-color="F9FBFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1749×976 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>EDIT: Now it has finally become responsive again, and it has decided that the Extensions I care about ARE compatible and I can install them. This is a frustrating process for users, and the sluggishness and inconsistency of this makes me reluctant to update frequently.</p>

---

## Post #5 by @lassoan (2020-05-29 00:29 UTC)

<p>I find this really frustrating, too. This unreliability is very harmful because most likely newcomers immediately give up on the entire software when they encounter this.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> What is the current state of migrating the extension manager to a new backend? How much work is still needed? What can we do to make it happen?</p>

---

## Post #6 by @jamesobutler (2020-05-29 01:18 UTC)

<p>From the post at <a href="https://discourse.slicer.org/t/running-slicer-on-headless-server-installing-extensions-and-more/11689/12" class="inline-onebox">Running Slicer on headless server (Installing Extensions and more...)</a> it appears resources need to be allocated for it. Whether that is people scheduling or a monetary decision is unknown to me.</p>

---

## Post #7 by @Dominic_LaBella (2020-06-04 20:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1b46af53d011974172f1b5ef5fd2ab0333c357e.png" data-download-href="/uploads/short-url/n4vpNvFb2aJAb7N16khofljs4Jo.png?dl=1" title="2020-06-04 14_14_31-Clipboard" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b46af53d011974172f1b5ef5fd2ab0333c357e_2_690x371.png" alt="2020-06-04 14_14_31-Clipboard" data-base62-sha1="n4vpNvFb2aJAb7N16khofljs4Jo" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b46af53d011974172f1b5ef5fd2ab0333c357e_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b46af53d011974172f1b5ef5fd2ab0333c357e_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b46af53d011974172f1b5ef5fd2ab0333c357e_2_1380x742.png 2x" data-dominant-color="FEFEFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-06-04 14_14_31-Clipboard</span><span class="informations">1817×979 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is the extension manager up and running? (6-4-2020)<br>
I get a “Loading extensions” message that won’t go away.<br>
I have tried multiple wifis and the firewall is not blocking Slicer. I have tried multiple computers/windows 4.11.0 Slicer applications.</p>
<p>I am also unable to open the following website…<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/slicerappstore</a></p>
<p>Thanks!</p>

---

## Post #8 by @lassoan (2020-06-04 21:23 UTC)

<p>Sorry, this is a temporary issue that should resolve on its own, please try again in 30-60 minutes.</p>
<p>We are in the process of upgrading the software infrastructure to make the extension server work more reliably.</p>

---

## Post #9 by @muratmaga (2020-06-12 20:05 UTC)

<p>this behavior doesn’t seem to be resolved?</p>
<p>Even with the latest preview, I still need to click the extension manager to twice to open?</p>

---

## Post #10 by @lassoan (2020-06-12 20:16 UTC)

<p>Have you tried to click once and wait (up to several minutes)?</p>

---

## Post #11 by @dmarquette (2020-07-01 08:15 UTC)

<p>Operating system: macOS Catalina 10.15.5<br>
Slicer version: 4.11.0<br>
Expected behavior: open the extension manager successfully and have access to the catalog of available extensions</p>
<p>Actual behavior:<br>
When I click on the “Extension Manager” icon for the first time after launching Slicer, the following error message is always displayed. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60280f89ae206bedb75565f080e9fc9023656cc0.jpeg" data-download-href="/uploads/short-url/dIDFlcoNnmUsbM3OWPaSmI6dvdC.jpeg?dl=1" title="Error message (Extension Manager)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60280f89ae206bedb75565f080e9fc9023656cc0_2_690x431.jpeg" alt="Error message (Extension Manager)" data-base62-sha1="dIDFlcoNnmUsbM3OWPaSmI6dvdC" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60280f89ae206bedb75565f080e9fc9023656cc0_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60280f89ae206bedb75565f080e9fc9023656cc0_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60280f89ae206bedb75565f080e9fc9023656cc0_2_1380x862.jpeg 2x" data-dominant-color="DBDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error message (Extension Manager)</span><span class="informations">2880×1800 676 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After closing the error window by pressing the “annuler” (= cancel) button and clicking again on the “Extension Manager” icon, I can open the extension manager. The “Manage Extensions” and “Restore Extensions” tabs work fine, but the “Install Extensions” tab always remains blank with no loading symbol whatsoever. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/955b7d2cc603c69dac717b734f6d894c062615d4.png" data-download-href="/uploads/short-url/ljh9KEO0QE2zKdBmr5yqhW5GZ3C.png?dl=1" title="Extension manager" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955b7d2cc603c69dac717b734f6d894c062615d4_2_690x431.png" alt="Extension manager" data-base62-sha1="ljh9KEO0QE2zKdBmr5yqhW5GZ3C" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955b7d2cc603c69dac717b734f6d894c062615d4_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955b7d2cc603c69dac717b734f6d894c062615d4_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955b7d2cc603c69dac717b734f6d894c062615d4_2_1380x862.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Extension manager</span><span class="informations">2880×1800 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Has this problem been reported by other users?</p>
<p>In the meantime, I was able to install the Surface Wrap Solidify extension manually using the Extension Wizard and the extension GitHub.</p>
<p>Thanks for the help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @jamesobutler (2020-07-01 11:44 UTC)

<p>Yes, this issue has been reported and you can track the status at <a href="https://github.com/Slicer/Slicer/issues/5022" rel="nofollow noopener">https://github.com/Slicer/Slicer/issues/5022</a>. I will link your post there to provide additional info. Thank you!</p>

---
