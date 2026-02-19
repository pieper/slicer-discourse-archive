---
topic_id: 14928
title: "Failing To Download Extension With Slicer 4 11 Stable"
date: 2020-12-07
url: https://discourse.slicer.org/t/14928
---

# Failing to download extension with Slicer-4.11 stable

**Topic ID**: 14928
**Date**: 2020-12-07
**URL**: https://discourse.slicer.org/t/failing-to-download-extension-with-slicer-4-11-stable/14928

---

## Post #1 by @tbillah (2020-12-07 15:55 UTC)

<p>Hi all,</p>
<p>Is this a familar error?</p>
<blockquote>
<p>A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the <code>SameSite</code> attrute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with <code>SaSite=None</code> and <code>Secure</code>. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and semore details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus.com/feate/5633521622188032" rel="noopener nofollow ugc">https://www.chromestatus.com/feate/5633521622188032</a>.<br>
“Retrieving extension metadata [ extensionId: 405920]”<br>
“Downloading extension [ itemId: 548487]”<br>
“Archive /tmp/29402-linux-amd64-SlicerDMRI-git366d232-2020-10-21.tar.gz.IwhwIr doesn’t contain any files !”<br>
Uncaught SyntaxError: missing ) after argument list</p>
</blockquote>

---

## Post #2 by @Sam_Horvath (2020-12-07 16:13 UTC)

<p>The extension server is down, we are looking into it:</p>
<aside class="quote" data-post="1" data-topic="14914">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extension-service-is-down/14914">Extension service is down</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It looks like midas is half-broken.  The metadata can be retrieved but the downloaded files are empty. 
Can someone reboot it? 
"Retrieving extension metadata [ extensionId: 405842]"
"Downloading extension [ itemId: 548410]"
"Archive /tmp/29402-linux-amd64-WindowLevelEffect-git39baeae-2016-07-22.tar.gz.mFmokN doesn't contain any files !"
Uncaught SyntaxError: missing ) after argument list
  </blockquote>
</aside>


---

## Post #3 by @tbillah (2020-12-07 16:14 UTC)

<p>Glad to know that something is not broken at my end <img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=9" title=":innocent:" class="emoji" alt=":innocent:"></p>

---

## Post #4 by @tbillah (2020-12-07 18:49 UTC)

<p>Sam, can you give a heads up once it is fixed?</p>

---

## Post #5 by @jcfr (2020-12-08 13:25 UTC)

<p>Problem has been addressed and packages should be available. For more details, see <a href="https://discourse.slicer.org/t/extension-service-is-down/14914/4" class="inline-onebox">Extension service is down</a></p>

---
