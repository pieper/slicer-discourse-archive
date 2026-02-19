---
topic_id: 155
title: "Extensions Download Fails"
date: 2017-04-20
url: https://discourse.slicer.org/t/155
---

# Extensions Download fails?

**Topic ID**: 155
**Date**: 2017-04-20
**URL**: https://discourse.slicer.org/t/extensions-download-fails/155

---

## Post #1 by @fedorov (2017-04-20 20:15 UTC)

<p>Question asked by Matias Montroull on slicer-user list:</p>
<p>Hi,</p>
<p>I’m trying to download an extension using the extension manager but I get an error saying the download failed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f280c0873aca2a6ccb2b136d5fb71783df35f9.png" data-download-href="/uploads/short-url/8nyJcW9HtSb9nFEsuFLUaDNN0d.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00f280c0873aca2a6ccb2b136d5fb71783df35f9.png" alt="image" data-base62-sha1="8nyJcW9HtSb9nFEsuFLUaDNN0d" width="690" height="482" data-dominant-color="FCFCF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×585 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-394-when-i-go-to-httpslicerkitwarecommidas3slicerappstore-i-cant-see-any-extension-to-download-it-comes-up-with-no-extensions-found-am-i-in-the-right-page-pasted1-1" class="anchor" href="#p-394-when-i-go-to-httpslicerkitwarecommidas3slicerappstore-i-cant-see-any-extension-to-download-it-comes-up-with-no-extensions-found-am-i-in-the-right-page-pasted1-1" aria-label="Heading link"></a>When I go to <a href="http://slicer.kitware.com/midas3/slicerappstore" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a> I can’t see ANY extension to download, it comes up with: No Extensions Found.<br>
Am I in the right page?<br>
pasted1</h2>
<p>Matias</p>

---

## Post #2 by @fedorov (2017-04-20 20:17 UTC)

<p>Matias,</p>
<p>We are not building extensions for 32 bit platforms, and it appears from your screenshot that is what you are looking at.</p>
<p>Let us know if you have troubles downloading extensions for 64 bit platforms.</p>
<p>AF</p>

---

## Post #3 by @hina-shah (2017-04-20 20:24 UTC)

<p>HI Matias,</p>
<p>You will also need a correct revision number to see the list of extensions. (as seen on <a href="http://download.slicer.org">download.slicer.org</a>: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db09f756578ea8a25c34d49438ae20cac891380c.png" data-download-href="/uploads/short-url/vfHUWrEyMwOhucgrZSqV7QA3Qug.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db09f756578ea8a25c34d49438ae20cac891380c_2_690x221.png" alt="image" data-base62-sha1="vfHUWrEyMwOhucgrZSqV7QA3Qug" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db09f756578ea8a25c34d49438ae20cac891380c_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db09f756578ea8a25c34d49438ae20cac891380c_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db09f756578ea8a25c34d49438ae20cac891380c_2_1380x442.png 2x" data-dominant-color="F8F9F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1884×606 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.</p>
<p>Are you trying to populate the extensions list in an installed version of slicer or a built one? If you’re trying to get extensions on a built version of slicer you need to get the git-hash for the nightly revision number: <code>git svn find-rev r25938</code> (for example), and then checkout the branch with that hash.</p>
<p>Hope this helps!<br>
Hina</p>

---

## Post #4 by @pieper (2017-04-20 20:35 UTC)

<p>Unfortunately the default app store link never shows anything because you<br>
need to switch to 64bit and specify a revision number.</p>
<p>Here are links to see extensions for the 4.6.2 builds on Mac and Windows:</p>
<p><a href="http://slicer.kitware.com/midas3/slicerappstore?layout=empty&amp;os=macosx&amp;arch=amd64&amp;revision=25516" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerappstore?layout=empty&amp;os=macosx&amp;arch=amd64&amp;revision=25516</a></p>
<p><a href="http://slicer.kitware.com/midas3/slicerappstore?layout=empty&amp;os=win&amp;arch=amd64&amp;revision=25516" class="onebox" target="_blank">http://slicer.kitware.com/midas3/slicerappstore?layout=empty&amp;os=win&amp;arch=amd64&amp;revision=25516</a></p>
<p>If you see these, but the download fails inside slicer then the issue may<br>
lie elsewhere.  Did you look in the error log?</p>

---

## Post #5 by @Matias_Montroull (2017-04-20 20:55 UTC)

<p>Hi Fedorov, I changed to 64 bits and still I can’t see anything…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/512f5c39c94a005c742340d8fa1f5f7ed4411932.png" data-download-href="/uploads/short-url/bAc8VuuhhuuvBZi5i0VMloWYCn8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/512f5c39c94a005c742340d8fa1f5f7ed4411932.png" alt="image" data-base62-sha1="bAc8VuuhhuuvBZi5i0VMloWYCn8" width="690" height="390" data-dominant-color="FBFBF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×544 15.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Matias_Montroull (2017-04-20 20:56 UTC)

<p>Thanks, I’m trying to populate in an installed version of Slicer in a Windows 64 bits machine,</p>

---

## Post #7 by @Matias_Montroull (2017-04-20 20:58 UTC)

<p>Thanks Pieper, I went to the links you shared and was able to download the extension and install it. Now, I’m curious why it wouldn’t let me install in the Slicer app itself…</p>
<p>This is in the error log:<br>
“Failed downloading: <a href="http://slicer.kitware.com/midas3/download?items=259272" rel="nofollow noopener">http://slicer.kitware.com/midas3/download?items=259272</a>”</p>

---

## Post #8 by @fedorov (2017-04-20 21:00 UTC)

<p><a class="mention" href="/u/matias_montroull">@Matias_Montroull</a>, following the link you included, it looks like a problem on the server</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f829770c4b6972161f4ad8e8920b8791f416f3.png" data-download-href="/uploads/short-url/ZEy3SKEDUo16d5OzSvFiZUpdHZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06f829770c4b6972161f4ad8e8920b8791f416f3_2_690x230.png" alt="image" data-base62-sha1="ZEy3SKEDUo16d5OzSvFiZUpdHZ" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06f829770c4b6972161f4ad8e8920b8791f416f3_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f829770c4b6972161f4ad8e8920b8791f416f3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f829770c4b6972161f4ad8e8920b8791f416f3.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×284 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think <a class="mention" href="/u/jcfr">@jcfr</a> is the only person who can answer what is happening.</p>

---

## Post #9 by @jcfr (2017-04-21 15:53 UTC)

<aside class="quote no-group quote-modified" data-username="Matias_Montroull" data-post="7" data-topic="155" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c6cbf5/48.png" class="avatar"> Matias_Montroull:</div>
<blockquote>
<p>Thanks Pieper, I went to the links you shared and was able to download the extension and install it. Now, I’m curious why it wouldn’t let me install in the Slicer app itself..</p>
<p>This is in the error log:<br>
"Failed downloading: <a href="http://slicer.kitware.com/midas3/download?items=259272">http://slicer.kitware.com/midas3/download?items=259272</a></p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/matias_montroull">@Matias_Montroull</a>,</p>
<h3><a name="p-435-short-version-1" class="anchor" href="#p-435-short-version-1" aria-label="Heading link"></a>Short version:</h3>
<p>Install Slicer 4.6.2 , extensions are expected to be available.</p>
<h3><a name="p-435-long-version-2" class="anchor" href="#p-435-long-version-2" aria-label="Heading link"></a>Long version</h3>
<p>The link you provided corresponds to extension <code>25441-win-amd64-SkullStripper-git280121d-2015-01-12.zip</code> which is associated with Slicer r25441 and corresponds to Slicer 4.6.0. This can be seen using these links:</p>
<ul>
<li><a href="http://slicer.kitware.com/midas3/item/259272">http://slicer.kitware.com/midas3/item/259272</a></li>
<li><a href="https://www.slicer.org/wiki/Release_Details" class="inline-onebox">Release Details - Slicer Wiki</a></li>
</ul>
<p>I would suggest to download the latest “stable” version <code>4.6.2</code> here: <a href="http://download.slicer.org">http://download.slicer.org</a>  (which is associated with <code>r25516</code>)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08b9f4ea8aba85a1b3cb57595284da3b5dd8054e.png" data-download-href="/uploads/short-url/1fcegKxVaeT8wacCVY1vkR7vnvo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08b9f4ea8aba85a1b3cb57595284da3b5dd8054e_2_690x261.png" alt="image" data-base62-sha1="1fcegKxVaeT8wacCVY1vkR7vnvo" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08b9f4ea8aba85a1b3cb57595284da3b5dd8054e_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08b9f4ea8aba85a1b3cb57595284da3b5dd8054e_2_1035x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08b9f4ea8aba85a1b3cb57595284da3b5dd8054e.png 2x" data-dominant-color="F7F9F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1056×400 19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-435-slicer-appstore-from-the-web-3" class="anchor" href="#p-435-slicer-appstore-from-the-web-3" aria-label="Heading link"></a>Slicer AppStore from the web</h3>
<p>Using this link: <a href="http://slicer.kitware.com/midas3/slicerappstore" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a>  will allow to enter revision number and also select the expected platform and arch.</p>
<p>(Note that the <code>layout=empty&amp;</code> is not present in this link)</p>

---

## Post #10 by @JohnK (2017-11-28 00:48 UTC)

<p>Hi, I am using 3DSlicer version 4.9.0 on Windows 7-64bit</p>
<ul>
<li>In Install Extensions tab I get an access error:<br>
“you must be authenticed to acces this URL…”<br>
(I registered and logged into kitware with my own account to be sure)</li>
</ul>
<p>-Went to <a href="http://slicer.kitware.com/midas3/item/261265" rel="nofollow noopener">http://slicer.kitware.com/midas3/item/261265</a><br>
to manually download the DMRI plugin<br>
now I get the same error posted earlier:</p>
<p><strong>An error occurred</strong><br>
<strong>The system has encountered the following error:</strong><br>
<strong>Unable to find file on the disk</strong><br>
<strong>In /projects/src/Midas3/core/controllers/components/DownloadBitstreamComponent.php, line: 45</strong><br>
etc.</p>
<p>Should I revert to an older version or what might be my problem? Thanks,<br>
John</p>

---

## Post #11 by @lassoan (2017-11-28 01:20 UTC)

<aside class="quote no-group" data-username="JohnK" data-post="10" data-topic="155">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/59ef9b/48.png" class="avatar"> JohnK:</div>
<blockquote>
<p>3DSlicer version 4.9.0</p>
</blockquote>
</aside>
<p>Extension packages for nightly versions may be cleaned up to conserve disk space. Download the latest nightly build of Slicer (as of now, 26654) - the extension package is available for this build (<a href="http://slicer.kitware.com/midas3/slicerappstore/extension/view?extensionId=197038&amp;layout=layout" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a>).</p>
<p>Slicer app store does not require you to log in for downloading packages. The error that you got (“you must be authenticed to acces this URL…”) is most likely is a message from your hospital/corporate firewall.</p>

---

## Post #12 by @JohnK (2017-11-28 18:24 UTC)

<p>Yes, the new version (26654) will work with the manual install plugin (no dialog box to let you know it is done though). FYI, there is a windows console window present (I assume this is now default or a debugging component?). Now always on exit of 3D slicer I get a memory leak error the log is:</p>
<pre><code class="lang-auto">Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkSlicerTractographyInteractiveSeedingLogic

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkSlicerFiberBundleLogic

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkMRMLFiberBundleNode

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkMRMLFiberBundleLineDisplayNode

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkPolyDataColorLinesByOrientation

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkPolyDataTensorToColor

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkMRMLFiberBundleTubeDisplayNode

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkPolyDataTensorToColor

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkPolyDataColorLinesByOrientation

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkMRMLFiberBundleGlyphDisplayNode

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkMRMLFiberBundleStorageNode

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkMRMLTractographyInteractiveSeedingNode

Generic Warning: In C:\D\N\Slicer-0-build\VTKv9\Common\Core\vtkDebugLeaks.cxx, line 281
Deleting unknown object: vtkTractographyDisplayMRMLDMObjectFactory
</code></pre>

---

## Post #13 by @ihnorton (2017-11-28 19:04 UTC)

<p>Thanks for the report. I’ll take a look at the leak warnings.</p>

---
