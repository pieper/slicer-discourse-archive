# Recommended approach to store tutorial materials

**Topic ID**: 9235
**Date**: 2019-11-20
**URL**: https://discourse.slicer.org/t/recommended-approach-to-store-tutorial-materials/9235

---

## Post #1 by @fedorov (2019-11-20 18:50 UTC)

<p>Today I discovered that a PDF linked from a documentation wiki page disappeared (wiki page: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer">https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer</a>, broken link: <a href="https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf">https://www.slicer.org/slicerWiki/images/8/8d/MultiVolumeExplorer_Meysam_SNR-April2013-v4.pdf</a>).</p>
<p>Are there any recommendations how attachments for various Slicer-related resources should be stored? How is this done with the on-going migration to ReadTheDocs?</p>
<p>I think it would be nice to agree on some recommendation for storing attachments going forward. I am reluctant to use Slicer wiki for this purpose.</p>

---

## Post #2 by @fedorov (2019-11-20 18:57 UTC)

<p>One idea to handle this - we could upload those to GitHub, and link from wiki pages corresponding to individual repositories. This way links would be maintained by GitHub. It is easy to upload files and associate them with GitHub repositories using the workaround below. I am thinking to use this approach going forward.</p>
<p>            <video title="2019-11-20_13-52-48.mp4" width="695" height="422" style="max-width:100%" poster="https://thumb.screencast.com/3/1807ad2f-12c9-4280-9bbd-9fee80fec916/thumb.gif" controls="">
              <source src="https://content.screencast.com/users/andrey.f/folders/Snagit/media/1807ad2f-12c9-4280-9bbd-9fee80fec916/2019-11-20_13-52-48.mp4">
            </source></video>
</p>

---

## Post #3 by @lassoan (2019-11-20 20:07 UTC)

<p>You can only upload certain files as issue attachments and it is hard to keep track of the files. However, we have several options:</p>
<ul>
<li>A. Upload files as release assets (as we do it for <a href="https://github.com/Slicer/SlicerTestingData/releases">Slicer test data</a>): unlimited file storage, you can drag-and-drop files to upload, can be used as CMake ExternalData server (need to use hash as file name), but no versioning, downloading many files at once is tedious, uploading requires repository write access</li>
<li>B. Upload files as source files in git repository (as we do it for <a href="https://github.com/PerkLab/PerkLabBootcamp/tree/master/Doc">PerkLab bootcamp training materials</a>): easy to upload files (click a button then drag-and-drop file), version-controlled, users without write access can request adding of new files, easy to download all files, but repository size can grow big if large frequently changing binary files are stored, maximum file size is 100MB (warning at 50MB), repository maximum size is 100GB (recommended 1GB, warning at 75GB).</li>
<li>C. Keep them in a shared OneDrive folder (as we do it for <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>): slides can be viewed/edited online, without downloading, no limit on file size, version history can be maintained, easy to upload/download in bulk, can sync with local folder, but write access to the folder cannot be shared easily (trusted people may get write access but the user community cannot propose changes easily; github account cannot be used for authentication), links<br>
are not guaranteed to be permanent, only for MS Office file formats</li>
<li>D. Similar to C but with Google Drive and Googe Docs instead of OneDrive and MS Office (I don’t know any actual usage of this model in Slicer’s ecosystem).</li>
<li>E. Create tutorials from scratch using markdown/javascript-based tools: all open-source and vendor-independent, but only suitable for simple text + non-annotated image content due to lack of sophisticated authoring tools (some tools appear then usually die off within a few years)</li>
</ul>
<p>For me it seems that the two most viable options are B (to promote wider contributions and independence from MS Office) and C (for maximum convenience of a small number of contributors), but I would be interested in hearing about other options.</p>

---

## Post #4 by @mholden8 (2019-11-20 21:44 UTC)

<p>As an example of option D, we did some tutorials with sample data for Perk Tutor (<a href="http://perktutor.github.io/Help.html" rel="nofollow noopener">http://perktutor.github.io/Help.html</a>)…</p>

---

## Post #5 by @fedorov (2019-11-20 22:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="9235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can only upload certain files as issue attachments</p>
</blockquote>
</aside>
<p>Indeed, but the list includes ZIP. Citing <a href="https://help.github.com/en/github/managing-your-work-on-github/file-attachments-on-issues-and-pull-requests:">https://help.github.com/en/github/managing-your-work-on-github/file-attachments-on-issues-and-pull-requests:</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/639544c6329e43888ec8128ffbc25dee72d52393.png" alt="image" data-base62-sha1="ecX4IPXw9wSWyQfrNCfQE8qiYDx" width="637" height="400"></p>
<p>I guess I am ok with B, as long as the repository for data is not the same as the code repository. C and D are less attractive, because those spaces may belong to the institutions, storage is limited and user may hit the quota, and it is impossible to control availability in the general case. I like the approach I demonstrated, because it is so quick and easy, the threshold is very low for non-developers, and often we deal with files that are not expected to be updated.</p>
<p>We used to have Midas, but it is gone, and I don’t know about Girder space for Slicer.</p>
<p>Should we set up a dedicated repository under the Slicer organization to keep this kind of content (PDFs and various tutorial materials)? Would sample images go to that repo too?</p>

---

## Post #6 by @pieper (2019-11-20 22:01 UTC)

<p><a class="mention" href="/u/freephile">@freephile</a> may be able to comment more.  He told me that some similar path issues are being addressed during the wiki transition.</p>

---

## Post #7 by @freephile (2019-11-26 15:16 UTC)

<p>A few comments about the slicer wiki…</p>
<p>The deprecated ‘slicerWiki’ url mentioned at the outset of this post is now <a href="https://discourse.equality-tech.com/t/add-rewrite-rules-to-nginx-to-replace-apache-rules/991/3" rel="nofollow noopener">working again</a> in the newly migrated wiki system (using rewrite rules).</p>
<p>The newly upgraded wiki is able to store file assets of virtually any type. We currently allow png, gif, jpg, jpeg, webp, csv, doc, docx, ico, ics, jar, json, kml, mm, mov, mp3, mpg, odc, odg, odp, odt, owl, pdf, ppt, pptx, psd, qt, svg, txt, vsd, wmv, xls, xlsx, xml, zip, flac, mkv, mp4, oga, ogg, ogv, wav, webm.</p>
<p>PDF files are handled by a special viewer; and they are indexed for search inclusion.</p>
<p>The wiki allows admins to ‘side load’ (from another URL) files up to 500MB in size; and upload 8MB files from your desktop. (8MB may be increased to suit your needs).</p>
<p>With the new editors (Visual Editor and Source Editor), you can drag and drop files to be uploaded as you edit pages… You don’t need to perform a separate step.</p>

---
