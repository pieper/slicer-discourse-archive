---
topic_id: 15410
title: "Slicer Is Now Fully Portable"
date: 2021-01-08
url: https://discourse.slicer.org/t/15410
---

# Slicer is now fully portable

**Topic ID**: 15410
**Date**: 2021-01-08
**URL**: https://discourse.slicer.org/t/slicer-is-now-fully-portable/15410

---

## Post #1 by @lassoan (2021-01-08 19:15 UTC)

<p>Slicer can now be run from a portable drive (external drive, USB stick), along with all extensions, Python packages, settings, DICOM database, etc. - without installation. This can be used for easy distribution of Slicer to users, for example to be used as a free DICOM viewer for a folder full of DICOM files, or handing out preconfigured Slicer instance for a training course (see <a href="https://discourse.slicer.org/t/portable-installation-of-slicer-with-extension-on-usb/8582">this related request</a>). Since cache directory can be made local, too, the cache can be prepopulated with sample data sets, therefore the application does not need to access the internet for downloading them.</p>
<p>The feature is available in latest Slicer Preview Release. <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Updated documentation</a> describes the exact rules how the application finds local and common settings. Implementation details are available <a href="https://github.com/Slicer/Slicer/pull/5029">here</a>.</p>
<h2>Example: How to set up Slicer as a portable viewer for a folder of DICOM files</h2>
<p>By default, common settings (such as view settings, DICOM database folder location, various module preferences) are still taken from the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">user profile folder</a> by default:</p>
<p><strong>x:\myfolder\Slicer 4.13.0-2021-01-05&gt;Slicer.exe --settings-path | more</strong><br>
<em>c:/Users/andra/AppData/Roaming/NA-MIC/Slicer.ini</em></p>
<p>But if Slicer.ini file is copied to the Slicer home folder (including the organization subfolder NA-MIC) then Slicer will use this local settings file instead:</p>
<p><strong>x:\myfolder\Slicer 4.13.0-2021-01-05&gt;copy C:\Users\andra\AppData\Roaming\NA-MIC\Slicer.ini NA-MIC\Slicer.ini</strong><br>
<em>1 file(s) copied.</em><br>
<strong>x:\myfolder\Slicer 4.13.0-2021-01-05&gt;Slicer.exe --settings-path | more</strong><br>
<em>x:\myfolder\Slicer 4.13.0-2021-01-05/NA-MIC/Slicer.ini</em></p>
<p>After this local settings file is created, all changes in settings are recorded in this file. All paths that are specified relative to the application home folder will be kept as relative folders.</p>
<p>To change DICOM database to a local folder (that is portable along with the application), go to DICOM module, click “Database location”, a choose a folder that you created within the application home folder (for example, <code>x:\myfolder\Slicer 4.13.0-2021-01-05/dicomdb</code>). This change will be stored in the local Slicer.ini file, with a relative path:</p>
<pre><code>[General]
DatabaseDirectory_0.6.3=dicomdb
</code></pre>
<p>Similarly, other absolute paths in Slicer.ini and Slicer-NNN.ini can be changed to relative paths (they will be resolved using the current application home folder as a basis).</p>
<p>After this, add DICOM images to the local DICOM database using DICOM module -&gt; “Import DICOM files” button. Make sure to set “Import Directory Mode” -&gt; Copy.</p>

---

## Post #2 by @muratmaga (2021-01-08 19:57 UTC)

<p>This awesome. Thank you to all folks involved in making it happen.</p>
<p>I do have a small suggestion: Would it be possible to incorporate his into the installer mechanism? For example, installer may ask the user if they intended this is as portable installation and copy all the necessary files and paths automatically? It will be fairly useful in windows envirornment where most users are not even aware of AppData folder (as it is hidden by default)</p>

---

## Post #3 by @lassoan (2021-01-08 21:10 UTC)

<p>I would not complicate the installation process with any questions or decisions. It would complicate the installation process and would make user support harder for us (when we help a user we don’t know what installation options he chose). Also, there are dozens of settings to customize when you create a portable Slicer, so it would not be practical to implement all these as part of the installer.</p>
<p>Instead, you can create an extension that creates a portable version of the current Slicer instance. You could choose what directories you want to make portable, if you want to move or clone images in the DICOM database, etc. It could recreate the same setup for all operating systems (the extension could download Slicer core and extensions for all other operating systems and set up everything consistently).</p>

---

## Post #4 by @pieper (2021-01-08 21:18 UTC)

<p>I agree doing this after install time is better, then you could easily change it again later.</p>
<p>But wouldn’t this be better as part of the core instead of an extension?  Seems like a pretty broadly applicable functionality.</p>

---

## Post #5 by @lassoan (2021-01-08 21:27 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="15410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But wouldn’t this be better as part of the core instead of an extension? Seems like a pretty broadly applicable functionality.</p>
</blockquote>
</aside>
<p>It would be probably better to develop in a sandbox and then move it to the Slicer core if it is mature enough and we find that many users are interested in it.</p>

---

## Post #6 by @jamesobutler (2021-01-08 22:00 UTC)

<p>I’ve seen applications where their download page allows picking to download an installer or the portable version (packaged in a ZIP).</p>
<p>Here’s Visual Studio Code’s download page <a href="https://code.visualstudio.com/download:" rel="noopener nofollow ugc">https://code.visualstudio.com/download:</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a279ed47a204d0cd897dbc91ae39ac7c9941d4ba.png" alt="image" data-base62-sha1="nbkzNhmBgXIWEgOr6rTG5h1MgZ4" width="293" height="320"></p>

---

## Post #7 by @pieper (2021-01-08 22:01 UTC)

<p>Oh, that’s right - this relocatable version won’t even <em>need</em> an installer.  Sweet.</p>

---

## Post #8 by @lassoan (2021-01-08 22:08 UTC)

<p>Yes, every installed Slicer is relocatable now (there is no specific “portable” version of Slicer).</p>
<p>It could be nice to provide download link for zip packages in addition to installer/dmg (CMake can create it already), because users often think that they need to install Slicer or that they need to have admin rights, while in fact they don’t.</p>

---

## Post #9 by @jamesobutler (2021-01-08 22:12 UTC)

<p>Yeah I think it would be nice to set up download links just like Visual Studio Code there.</p>
<p>User Installer first for the majority use case. User’s don’t need admin rights which is helpful in an academic setting.</p>
<p>System Installer second for those wanting to install it for all their users of said computer. Instead of right-click run as admin, manually change path to Program Files, etc.</p>
<p>ZIP/Portable listed last for those lesser used cases, but still nice to have to move it anywhere such as on to a USB drive to shared.</p>

---

## Post #10 by @rbumm (2021-01-09 11:02 UTC)

<p>This is very very good news for a hospital setting, where users often do not have the admin privileges necessary to run Slicer and administrators do not like the idea of downloaded data sets and extensions.  Thanks for the realization! I would also support the idea of a zip download, as most portable applications come zipped …</p>

---

## Post #11 by @lassoan (2021-01-09 18:31 UTC)

<p>The current installer does not require administrative privileges. It is essentially a self-extracting zip file, with a few additional steps (creates start menu shortcuts, sets up file associations, and writes uninstall information). Have you run into troubles running the installer on locked-down hospital computers?</p>

---

## Post #12 by @lassoan (2021-03-24 13:26 UTC)

<p>A post was split to a new topic: <a href="/t/application-failed-to-start-on-windows-7/16749">Application failed to start on Windows 7</a></p>

---

## Post #13 by @dangerweenie (2024-05-16 22:41 UTC)

<p>I’ve followed the directions -</p>
<ul>
<li>moving silicer.ini from %APPDATA%/roaming/slicer/slicer.ini to %APPDATA/local/slicer5.6.2/slicer.ini</li>
</ul>
<p>then</p>
<pre><code class="lang-auto">./slicer.exe --settings-path | more
</code></pre>
<p>And it still returns the original path (it also recreates the slicer.ini in the original folder it was moved from.</p>
<p>Any advice? Is the slicer <code>home folder</code> not the same folder that slicer.exe lives in?</p>
<p>I’d like to be able to keep all the extensions and data in one place and relocate it to another HDD.</p>
<p>Thanks!</p>

---

## Post #14 by @lassoan (2024-05-17 01:18 UTC)

<p>Slicer.ini file was placed in the wrong folder, therefore it was not found and a new default one was created. The application home folder and location of the Slicer.ini file within it is described on the documentation page referred to in the first post.</p>
<p>Probably the easiest way to get the correct location is to run this command in Slicer’s Python console:</p>
<pre><code>slicer.app.revisionUserSettings().fileName()
</code></pre>
<p>It will print the filename of the revision-specific settings file, such as this:</p>
<pre><code>C:/Users/andra/AppData/Local/slicer.org/Slicer 5.7.0-2024-05-09/slicer.org/Slicer-32842.ini
</code></pre>
<p>You need to copy the <code>Slicer.ini</code> file into this same folder:</p>
<pre><code>C:/Users/andra/AppData/Local/slicer.org/Slicer 5.7.0-2024-05-09/slicer.org/Slicer.ini
</code></pre>

---
