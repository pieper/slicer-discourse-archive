---
topic_id: 24416
title: "New Feature Automatic Update Of Extensions"
date: 2022-07-20
url: https://discourse.slicer.org/t/24416
---

# New feature: Automatic update of extensions

**Topic ID**: 24416
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/new-feature-automatic-update-of-extensions/24416

---

## Post #1 by @lassoan (2022-07-20 17:52 UTC)

<p>We have implemented some long-awaited improvements in the Extensions Manager in Slicer-5.0.3. Most importantly extensions can be updated automatically and bookmarks can be used for convenient reinstallation of a list of extensions across different Slicer versions, computers, or users.</p>
<p>See a half-minute demo video here and details below:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="0l2oTonCXFs" data-video-title="3D Slicer Extensions Manager redesigned" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=0l2oTonCXFs" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/0l2oTonCXFs/maxresdefault.jpg" title="3D Slicer Extensions Manager redesigned" width="690" height="388">
  </a>
</div>

<h3><a name="p-81058-new-features-1" class="anchor" href="#p-81058-new-features-1" aria-label="Heading link"></a>New features</h3>
<ul>
<li><strong>Extension update check and installation:</strong> Makes it easy for users to keep installed extensions up-to-date.
<ul>
<li>User can check for available updates and install those updates manually (by a single click) or enable automatic updates.</li>
<li>If extension updates are available (but automatic installation of updates is disabled) then a notification marker is displayed over the Extensions Manager toolbar icon and the user can install updates by</li>
</ul>
</li>
<li><strong>Bookmarked (favorite) extensions:</strong> Users can bookmark their frequently used extensions for easier installation.
<ul>
<li>Bookmarked extensions are shared between all installed Slicer versions, which makes it easy to reinstall the same extensions on different Slicer versions.</li>
<li>List of bookmarks can be edited as simple text. This makes it easy to transfer favorite extensions between computers or install a set of extensions at training events.</li>
</ul>
</li>
</ul>
<h3><a name="p-81058-usability-improvements-2" class="anchor" href="#p-81058-usability-improvements-2" aria-label="Heading link"></a>Usability improvements</h3>
<ul>
<li>Multiple extension package files can be installed at once.</li>
<li>The “manage” and “restore” tabs are merged into a single tab where user can install/uninstall/update/restore.</li>
<li>Dependent extensions are installed automatically by default, to simplify extension installation.<br>
Manual installation (user confirmation) can be enabled in extensions settings.</li>
<li>All dependent extensions (even indirect dependencies) are determined at once before asking the user to install them, saving several extra clicks for some extensions.</li>
<li>More extension metadata is displayed. Extension version and update time (when the package was built) is displayed for the installed extension and for the latest available updates (if any).</li>
</ul>
<h3><a name="p-81058-performance-and-stability-improvements-3" class="anchor" href="#p-81058-performance-and-stability-improvements-3" aria-label="Heading link"></a>Performance and stability improvements</h3>
<ul>
<li>Extensions Manager is displayed immediately. The user does not need to wait for any downloads.<br>
Previously, hundreds of requests were submitted to query all necessary extension<br>
metadata, which caused slowdowns and crashes. Now all metadata can be downloaded in<br>
batch (in 4 requests), very robustly, in 1-2 seconds, and cached in a json file<br>
(such as Slicer 5.0.3\NA-MIC\Extensions-30893\ExtensionsMetadataFromServer.json)<br>
All data is reloaded immediately from cache or downloaded asynchronously.</li>
<li>Extensions server website can be opened in the default web browser. This makes it easier to<br>
download extensions for offline installation from file or when firewall or proxy settings prevent<br>
the extensions manager from working.</li>
<li>Bookmarked extensions can be installed without the “Install Extensions” tab, which may be useful in cases where firewalls or proxy servers prevent access to the Extensions Catalog website.</li>
<li>Close/restart button is not enabled until batch processing (install all/update all extension) are completed.</li>
<li>Fixed display of icons of many extensions: icons that were hosted on servers with 301-redirect are now displayed correctly.</li>
</ul>

---
