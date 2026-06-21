---
topic_id: 47389
title: "Stable Release 5.1 Cannot be Opened Because Developer is Unverified"
date: 2026-06-19
url: https://discourse.slicer.org/t/47389
last_bumped: 2026-06-20T15:18:10.490Z
---

# Stable Release 5.1 Cannot be Opened Because Developer is Unverified

**Topic ID**: 47389
**Date**: 2026-06-19
**URL**: https://discourse.slicer.org/t/stable-release-5-1-cannot-be-opened-because-developer-is-unverified/47389

---

## Post #1 by @JHegg (2026-06-19 12:32 UTC)

<p>Hello,</p>
<p>I recently downloaded the latest stable version of slicer for MacOS and updated from a prior version. However, I get the “Cannot be opened because the developer cannot be verified error”.</p>
<p>I am aware that the preview version is known to have this issue, but I couldn’t find a support post of this happening with the stable version. Is this related to it being an update? (I dragged the icon into the Applications folder and I replaced the old one). I’m certain I downloaded the stable version, I downloaded it once and my IT person downloaded it again and we got the same result both times.</p>
<p>IT is reluctant to bypass the verification and use “open anyway” in settings. Is there a reason I’m getting this error, or things I could try to get the verification to read?</p>
<p>Thanks in advance,</p>
<p>Jens</p>
<p>The prior threads on this error are linked below:</p>
<aside class="quote" data-post="1" data-topic="12930">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/unsigned-application-issue-on-mac/12930">Unsigned application issue on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Posting on behalf of a user. He apparently installed the latest mac preview, but got this error message after trying to start Slicer. 

“Slicer” cannot be opened because the developer cannot be verified. macOS cannot verify that this app is free from malware 

What is the proper way to override this?
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="46687">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sathishbalachandran/48/82192_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/slicer-is-so-buggy-and-keeps-showing-error-on-macbook-air-m5/46687">Slicer is so buggy and keeps showing error on macbook air M5</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hello Slicer Support Team, 
I am a Radiation Oncologist (MD, DNB) attempting to use 3D Slicer for my daily clinical cases (1-2 cases/day). I recently moved from an old, basic Windows laptop to a new MacBook Air M5, but the experience has been very difficult and I am unable to use the software. 
The primary issues I am facing: 


Security/Verification Issues: Upon installation, macOS could not verify the software. I had to manually go into my system settings and select “Open Anyway” just to get t…
  </blockquote>
</aside>


---

## Post #2 by @pieper (2026-06-20 15:18 UTC)

<p>Yes, thanks for posting here.  This is a known issue we recently became aware of and it’s being tracked here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9207">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9207" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9207" target="_blank" rel="noopener">Request signed and notarized macOS builds</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-06-03" data-time="20:10:18" data-timezone="UTC">08:10PM - 03 Jun 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/uurazzle" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/6226458?v=4" class="onebox-avatar-inline" width="20" height="20">
          uurazzle
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Title: Request: Sign and notarize the macOS application for improved Gatekeeper <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">and deployment compatibility

Hello Slicer maintainers,

First, thank you for the continued work on Slicer and for making such an important tool available as open source. I am opening this issue as a request to consider signing and notarizing the macOS application builds distributed by the project.

At present, the macOS application appears to be unsigned and/or not notarized by Apple. This creates friction for end users and for organizations that manage Macs at scale, because macOS Gatekeeper treats unsigned or non-notarized software differently from software signed with a Developer ID certificate and submitted to Apple’s notarization service.

Apple’s documentation for distributing macOS apps outside the Mac App Store recommends signing apps with a Developer ID certificate and notes that users gain additional assurance when the Developer ID-signed app is also notarized by Apple:

https://help.apple.com/xcode/mac/current/en.lproj/dev033e997ca.html

Apple’s notarization documentation is here:

https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution

Apple also documents that hardened runtime is required for notarization:

https://developer.apple.com/documentation/security/hardened_runtime

This has a practical impact beyond the first-launch warning. Many managed macOS environments rely on automation tools such as Installomator and AutoPkg to download, validate, package, and deploy third-party applications. When a macOS app is not signed and notarized, it can limit or complicate use with these workflows because administrators cannot rely on normal Gatekeeper trust checks, Developer ID identity validation, or standard deployment verification patterns.

Examples of affected open source Mac admin tooling:

* Installomator: https://github.com/Installomator/Installomator
* AutoPkg: https://github.com/autopkg/autopkg

For institutional, lab, classroom, and managed-device deployments, having a signed and notarized Slicer.app would make the software easier to deploy safely and consistently. It would also reduce user confusion, help avoid security exceptions, and make it easier for Mac administrators to support Slicer in environments with stricter endpoint security policies.

Would the project consider adding Developer ID signing and Apple notarization to the macOS release process?

Possible acceptance criteria could include:

* macOS `.app`, `.dmg`, and/or `.pkg` release artifacts are signed with a valid Developer ID certificate.
* Release artifacts are submitted to Apple’s notary service.
* The notarization ticket is stapled where appropriate.
* The release process includes verification steps such as `codesign --verify`, `spctl --assess`, and notarization status checks.
* The project documentation notes that macOS builds are signed and notarized.

I appreciate that signing and notarization can add complexity to open source release pipelines, especially around certificate management and CI/CD secrets. Even so, this would be a significant improvement for Mac users and for organizations deploying Slicer at scale.

Thank you for considering this request.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>There are also workarounds described there.</p>

---
