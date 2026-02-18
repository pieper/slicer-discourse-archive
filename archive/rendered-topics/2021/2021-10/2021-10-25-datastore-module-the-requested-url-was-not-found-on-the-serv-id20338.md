# DataStore module: "The requested URL was not found on the server." error

**Topic ID**: 20338
**Date**: 2021-10-25
**URL**: https://discourse.slicer.org/t/datastore-module-the-requested-url-was-not-found-on-the-server-error/20338

---

## Post #1 by @DIV (2021-10-25 13:05 UTC)

<p>In version 4.11.20210226 I am getting an error in the DataStore in both</p>
<ul>
<li>Download Datasets<br>
and</li>
<li>Upload Datasets.</li>
</ul>
<p><strong># Not Found</strong><br>
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
<p>This is a newish installation, and to the best of my knowledge the URL set as the <strong>DataStore URL</strong>, <code>http://slicer.kitware.com/midas3</code>, is whatever the application shipped with as the default URL.</p>
<p>—DIV</p>

---

## Post #2 by @DIV (2021-10-25 13:08 UTC)

<p>Actually, the same issue is being experienced in the previous version of Slicer too, which I had previously used successfully for this with no error message.<br>
Maybe the URL is correct, but the site is just temporarily down?<br>
—DIV</p>

---

## Post #3 by @jamesobutler (2021-10-25 13:26 UTC)

<p>The servers were upgraded so the midas version doesn’t exist anymore. See this post about extensions and DataStore items.</p>
<aside class="quote quote-modified" data-post="1" data-topic="19256">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256">Downloading extensions for older releases</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Due to the recent transition to the updated Extension Manager and Data Store infrastructure, when using Slicer-4.11 (or older) version, users will need to manually download and install extensions from the new extension server, and download data sets from an alternative server instead of using the Data Store module. Rationale for the transition can be found <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444">here</a>.  We anticipate that this will be a temporary measure will the transition is finalized. 
Thank you for your patience!  Please do not hes…
  </blockquote>
</aside>


---

## Post #4 by @DIV (2021-10-25 13:54 UTC)

<p>Thanks, James.<br>
I did search the forums for DataStore &amp; URL, but didn’t make the connection to that post.</p>
<aside class="quote no-group" data-username="Sam_Horvath" data-post="1" data-topic="19256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"><a href="https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256/1">Downloading extensions for older releases</a></div>
<blockquote>
<h2>Download data sets that were previously hosted on the DataStore</h2>
<p>If you are looking for data previously accessible via the Data Store module (hosted on the DataStore server), it can be found <strong><a href="https://slicer-packages.kitware.com/#collection/6124ffb8342a877cb3b8afdd/folder/6125487e342a877cb3b8b6ed" rel="noopener nofollow ugc">here</a></strong></p>
</blockquote>
</aside>
<p>So I tried updating the <strong>DataStore URL</strong> to <code>https://slicer-packages.kitware.com/#collection/6124ffb8342a877cb3b8afdd/folder/6125487e342a877cb3b8b6ed</code>, and it seems to <em>more-or-less</em> work.<br>
The above URL ‘should’ directly take one to the DataStore folder, but in Slicer it opens up initially at the root.  After navigating through the directory structure in the Slicer interface, clicking to load one example (Robex Brain) I got an error message <code>Failed to load data store page</code> in the <strong>Data Store</strong> dialogue box.  But in the topmost dialogue box, <strong>Add data into the scene</strong>, there was no error, and the selected data appears to load successfully.</p>
<p>—DIV</p>

---

## Post #5 by @jamesobutler (2021-10-25 13:59 UTC)

<p>Yes it is not expected to work to just update the URL in Slicer Stable code (4.11.20210226). Currently no development is expected to backport the new server work to latest Slicer stable. Instead the latest Slicer Preview where there aren’t any issues will soon become the new Slicer stable.</p>

---

## Post #6 by @lassoan (2021-10-25 23:13 UTC)

<p>The Slicer DataStore server was developed at a time when open data repositories barely existed and self-hosting data was complicated and expensive. The world has changed and it does not make sense for the Slicer project to maintain a custom data hosting solution anymore.</p>
<p>All the old data sets are moved <a href="https://github.com/Slicer/SlicerDataStore/releases/tag/SHA256">here</a>, but there may be some that is not uploaded yet (see <a href="https://github.com/Slicer/Slicer/issues/5796">#5796</a> and <a href="https://github.com/Slicer/Slicer/issues/4602">#4602</a>).</p>

---
