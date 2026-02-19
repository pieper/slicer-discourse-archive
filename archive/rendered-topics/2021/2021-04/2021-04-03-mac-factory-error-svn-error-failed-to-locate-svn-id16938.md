---
topic_id: 16938
title: "Mac Factory Error Svn Error Failed To Locate Svn"
date: 2021-04-03
url: https://discourse.slicer.org/t/16938
---

# Mac factory error - "svn: error: Failed to locate 'svn'."

**Topic ID**: 16938
**Date**: 2021-04-03
**URL**: https://discourse.slicer.org/t/mac-factory-error-svn-error-failed-to-locate-svn/16938

---

## Post #1 by @fedorov (2021-04-03 21:58 UTC)

<p>There is an error for the dcmqi extension on the mac factory here: <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2194606" class="inline-onebox">CDash</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562da42d48028072c6e0122d0373160ee77e4e7e.png" data-download-href="/uploads/short-url/cimQBJKvo4oOTdXeAwlu7U3R4Oa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562da42d48028072c6e0122d0373160ee77e4e7e_2_690x258.png" alt="image" data-base62-sha1="cimQBJKvo4oOTdXeAwlu7U3R4Oa" width="690" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562da42d48028072c6e0122d0373160ee77e4e7e_2_690x258.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562da42d48028072c6e0122d0373160ee77e4e7e_2_1035x387.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562da42d48028072c6e0122d0373160ee77e4e7e_2_1380x516.png 2x" data-dominant-color="E8E9EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1656×620 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have a Slicer build on my mac, and I also don’t have svn, but extension build does not fail the same way. Here’s what I get when building locally:</p>
<pre><code class="lang-plaintext">-- Setting default for EXTENSION_STATUS ........:
-- Found Git: /usr/bin/git
-- Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE)
-- Checking if using built-in JsonCpp
-- Checking if using built-in JsonCpp - no
</code></pre>
<p>I then installed svn using brew, and, again, I have no problem with configuring and building the extension:</p>
<pre><code class="lang-plaintext">-- Setting default for EXTENSION_STATUS ........:
-- Found Git: /usr/bin/git
-- Found Subversion: /usr/local/bin/svn (found version "1.14.1")
-- Checking if using built-in JsonCpp
-- Checking if using built-in JsonCpp - no
</code></pre>
<p>Is there an issue with how svn is installed on the mac factory? Does anyone know more about this error?</p>

---

## Post #2 by @jamesobutler (2021-04-03 22:05 UTC)

<p>May want to check out <a href="https://github.com/Slicer/Slicer/pull/5562" class="inline-onebox" rel="noopener nofollow ugc">Simplify build system removing extension build svn support by jcfr · Pull Request #5562 · Slicer/Slicer · GitHub</a> which removes some svn support. Ultimate solution might simply be to remove the old svn support.</p>

---

## Post #3 by @fedorov (2021-04-03 22:23 UTC)

<p>Thanks, although I am not sure this is related. I still think there is something not right with the svn installation on the factory. From the factory error, it seems that there is svn installed, but it does not produce the expected output when run with <code>--version</code>.</p>
<p>If I only knew where svn should be removed in my superbuild! I do not consciously use it my extension, it is inherited somewhere in cmake, and I can’t trace it down.</p>

---

## Post #4 by @lassoan (2021-04-03 23:09 UTC)

<p>SVN is not installed on that factory machine (it is not the one that build the extensions, it just runs tests).</p>
<p>We debated if we should install SVN on that factory machine or remove SVN support from the build scripts. We chose the latter because nobody uses SVN anymore (none of the 150+ extensions), and removing it allow some simplification in the build scripts.</p>

---

## Post #5 by @fedorov (2021-04-04 01:13 UTC)

<p>Is there any guidance on what should be done in extensions to adapt to that change?</p>

---

## Post #6 by @lassoan (2021-04-04 01:18 UTC)

<p>No action needed from extension developers. The extensions are successfully built by <code>factory-south-macos.kitware</code>. For now, just ignore the “SVN not found” error on <code>computron-macos-tests.kitware</code>.</p>

---

## Post #7 by @fedorov (2021-04-04 01:22 UTC)

<p>I checked again, and those are build errors, not failing tests, see <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2021-03-29" class="inline-onebox">CDash</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7ddf71c3b5aed5595eef0901f232da8f280c1417.png" data-download-href="/uploads/short-url/hXwpuGGBuA19rt5YTZYM4Arw2IT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7ddf71c3b5aed5595eef0901f232da8f280c1417_2_690x35.png" alt="image" data-base62-sha1="hXwpuGGBuA19rt5YTZYM4Arw2IT" width="690" height="35" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7ddf71c3b5aed5595eef0901f232da8f280c1417_2_690x35.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7ddf71c3b5aed5595eef0901f232da8f280c1417_2_1035x52.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7ddf71c3b5aed5595eef0901f232da8f280c1417_2_1380x70.png 2x" data-dominant-color="D9D4CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2094×108 20.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3e244bb4c494f27fbd86117ceb33846cf69719.gif" alt="2021-04-03_21-21-03" data-base62-sha1="t8OxBULgFCPeiOGKDwKQr1sB43n" width="690" height="339" class="animated"></p>

---

## Post #8 by @fedorov (2021-04-04 01:24 UTC)

<p>I see, I misunderstood your earlier statement. I will ignore anything coming from <code>computron-macos-tests.kitware</code>. Thank you.</p>

---

## Post #9 by @Sam_Horvath (2021-04-05 14:33 UTC)

<p>Once the SVN issue is sorted, computron-macos-tests.kitware will the be authoritative report for test results for mac.</p>
<p>Background:</p>
<p>I have been working on getting the testing infrastructure cleaned up for Slicer and extensions.  Tasks for this include:</p>
<ul>
<li>Re-enabling linux testing [done]</li>
<li>Moving mac testing to a separate factory (in progress, and the cause of the current issue)
<ul>
<li>Reason:  The mac GUI tests can be pretty fragile, and error / info dialogs that might pop up hold up the entire testing process.  While I work on preventing these issues from happening, the tests have been moved so that the build and package process is not interrupted.</li>
</ul>
</li>
<li>Fixing windows tests so that we capture the console output
<ul>
<li>Console output is not captured because we are using a non-console launcher for the factory packages.  We are planning to create a separate testing launcher w/ console to allow capture of console output.</li>
</ul>
</li>
</ul>

---
