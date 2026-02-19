---
topic_id: 20467
title: "Slicermarkupstomodel Failing Because Of Unauthenticated Git"
date: 2021-11-02
url: https://discourse.slicer.org/t/20467
---

# Slicermarkupstomodel failing because of unauthenticated git protocol on port 9418 is no longer supported

**Topic ID**: 20467
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/slicermarkupstomodel-failing-because-of-unauthenticated-git-protocol-on-port-9418-is-no-longer-supported/20467

---

## Post #1 by @Shazam_L (2021-11-02 19:21 UTC)

<p>Hello to whoever wants to help,</p>
<p>I was building and got this error in the title. I was wondering how to solve this.</p>
<p>Thanks,</p>
<p>Shazam L</p>

---

## Post #2 by @Shazam_L (2021-11-02 19:51 UTC)

<p>Some where ‘git://github.com/SlicerIGT/SlicerMarkupsToModel.git’ is cloned however, I am unable to change <code>git://</code> to <code>https://</code> to setup the correct protocol. Github changed its protocols.</p>

---

## Post #3 by @lassoan (2021-11-02 20:02 UTC)

<p>Thanks for reporting, see the discussion in this topic:</p>
<aside class="quote" data-post="1" data-topic="20460">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/build-failure-on-mac-using-git-protocol/20460">Build failure on Mac using git:// protocol</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I haven’t built from scratch (clean) in a while, so apologies if this was mentioned elsewhere (didn’t see it in a quick search). 
It looks like as of Nov 2, the “brownout” of the git:// protocol is beginning. Cloning of DCMTK using this protocol during the build fails, but the solution is just to un-check Slicer_USE_GIT_PROTOCOL in CMake. Should this be the default now, as git:// protocol is truly going away?
  </blockquote>
</aside>


---
