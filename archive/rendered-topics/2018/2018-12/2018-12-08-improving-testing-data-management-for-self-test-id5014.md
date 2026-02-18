# Improving testing data management for "self-test"

**Topic ID**: 5014
**Date**: 2018-12-08
**URL**: https://discourse.slicer.org/t/improving-testing-data-management-for-self-test/5014

---

## Post #1 by @jcfr (2018-12-08 07:48 UTC)

<p>We recently <strong>improved the time required to run python self-tests</strong> from 2x to 10x depending on the case, see <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27617" rel="nofollow noopener">here</a> for more details.</p>
<p>I  suggest to leverage and improve the SampleData logic to:</p>
<ul>
<li>cache downloaded test data in a persistent directory that wouldn’t be cleared before each daily build starts.</li>
<li>ensure up-to-date data are always downloaded and be resilient to incomplete file download</li>
</ul>
<h3>Plan of action</h3>
<p>The plan is the following:</p>
<ol>
<li>Update <code>SampleDataLogic</code> and <code>SampleDataSource</code> to support Scene file type. Currently expectation seems to be that only files are downloaded.</li>
<li>Update all tests to use <code>SampleDataSource</code>, <code>SampleDataLogic</code>
</li>
<li>Improve SampleData download logic to accept checksums. Re-download will be re-done if the checksum of the file into the cache does not match the expected one.
<ul>
<li>This will help with testing, currently after aborting a test while it’s downloading (basically the first things happening when running a test), an invalid file may exist in the cache.</li>
</ul>
</li>
<li>Add a new property named <code>cacheDirectory</code>, if this property is set and a checksum is associated with a file:
<ul>
<li>the file will be downloaded into the <code>cacheDirectory</code>, renamed after the provided checksum and copied into the cache directory associated with the current scene</li>
<li>Also, in case an environment variable named <code>SLICER_SAMPLEDATA_CACHE_DIRECTORY</code> is set, it will be used to initialize this property.</li>
<li>By default, this new env. variable will be initialized with the same value already set to <code>ExternalData_OBJECT_STORES</code> env. variable. This variable is specified to Slicer and used to initialize where data downloaded using CMake ExternalData module are stored. That way, the cache used by regular CTest test and the one for the self-test will be downloaded in the same location saving time when re-running tests every day.</li>
</ul>
</li>
</ol>
<h3>What is ExternalData ?</h3>
<p>Read at <a href="https://blog.kitware.com/cmake-externaldata-using-large-files-with-distributed-version-control/" rel="nofollow noopener">https://blog.kitware.com/cmake-externaldata-using-large-files-with-distributed-version-control/</a> or look at the corresponding reference  documentation <a href="https://cmake.org/cmake/help/latest/module/ExternalData.html" rel="nofollow noopener">https://cmake.org/cmake/help/latest/module/ExternalData.html</a></p>
<h3>What is a self-test ?</h3>
<p>In a nutshell, a self-test has the following features:<br>
Important features include:</p>
<ul>
<li>Tests are available as part of the binary distributions of slicer, so users can confirm correct behavior on their systems</li>
<li>The same tests are run as part of the nightly test process and submitted to <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" rel="nofollow noopener">the slicer dashboard</a>.</li>
<li>Developers can efficiently develop the tests by reloading python scripts without needing to exit slicer.</li>
</ul>
<p>You may read more details on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/SelfTestModule" rel="nofollow noopener">wiki</a></p>

---

## Post #2 by @lassoan (2018-12-08 20:49 UTC)

<p>These would be great improvements.</p>
<p>It would be nice if we could improve the existing remote data management infrastructure (vtkCacheManager, vtkDataIOManager, vtkDataTransfer, vtkHTTPHandler, tkMRMLRemoteIOLogic) instead of building a new infrastructure. If we find that the current remote data management infrastructure is not useful or relevant anymore then probably we should remove it completely.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Do you remember what were the main remote data management use cases and if they are still relevant? It seems that Slicer could download data from remote servers using URLs stored in the scene, but I have never seen a scene like that.</p>

---

## Post #3 by @pieper (2018-12-09 20:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="5014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you remember what were the main remote data management use cases and if they are still relevant? It seems that Slicer could download data from remote servers using URLs stored in the scene, but I have never seen a scene like that.</p>
</blockquote>
</aside>
<p>Yes, that was the goal and it did generally work but it didn’t turn out to be used (maybe we just never pushed it).  The use cases were to allow slicer to natively reference image archives in MRML.  I guess in the end people end up managing download tasks explicitly with server-specific interfaces (we have TCIA Browser, XNAT interface, DICOM Query/Retrieve) but we tend to use MRML only for local files.</p>
<p>+1 for the idea of unified caching infrastructure with checksums.</p>

---

## Post #4 by @lassoan (2018-12-10 00:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="5014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>unified caching infrastructure</p>
</blockquote>
</aside>
<p>Should that be high-level feature implemented in SampleData/Python or low-level feature implemented at MRML level in C++?</p>
<p>I tend to prefer the former option (remove networking from MRML and add it at higher level), as I don’t think network communication could be part of MRML (https, various authentication protocols, etc. would be too complicated to implement; simple anonymous public data download over http would be too limited). We could keep cache management (finding cached files, cleaning up old files, etc) in C++ and add checksum support.</p>

---

## Post #5 by @pieper (2018-12-10 13:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="5014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should that be high-level feature implemented in SampleData/Python or low-level feature implemented at MRML level in C++?</p>
</blockquote>
</aside>
<p>Good question - I definitely agree we should keep the networking details out of MRML.  Personally I like Jc’s focus on caching SampleData for SelfTests since it’s a concrete use case to optimize.  General Slicer use, like managing a locally cached subset from large case archives is a different problem.</p>

---

## Post #6 by @lassoan (2018-12-10 17:38 UTC)

<p>Currently, SampleData uses the same cache folder as vtkCacheManager and there is already some interference (vtkCacheManager deletes data downloaded by SampleData when cache limit is exceeded).</p>
<p>To allow SampleData module to work reliably, we would need to update the cache manager’s strategy of how to delete things and probably also add support for checksum computation. The rest could be implemented at higher level, in SampleData.</p>
<p>If we touch the cache manager, it would be a good opportunity to remove remote data support from MRML, as it would simplify things. I add a note to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer50" rel="nofollow noopener">Slicer5 roadmap</a>.</p>

---

## Post #7 by @jcfr (2018-12-14 20:19 UTC)

<p>“Fun” facts:</p>
<ul>
<li>On the windows factory, there was 1.3GB (+120k files) of <code>Slicer-*.log</code> and <code>Slicer-tmp*.log</code> files</li>
<li>“Slicer4minutes” test is failing because the file <code>slicer4minute.mrb</code> already exist in the tmp folder but is the wrong one (it was updated few days ago). Moving to a checksum based approach will avoid this.</li>
<li>There is a “Cache” panel in the Slicer settings with the maximum size cache but user is not notified when the cache is growing beyond the set limit.</li>
<li>Application tests (e.g self-test in python) are run sequentially because (1) temporary test folder are not unique per Slicer session and would clash and (2) for historical reason test involving rendering couldn’t run in parallel when executed on VM</li>
</ul>
<p>To move forward, the plan would be:</p>
<ul>
<li>make sure the Cache folder persist between machine restart (by default the cache folder will be outside of the tmp folder. Currently it is <code>/tmp/Slicer-&lt;username&gt;/RemoteIO</code>)</li>
<li>before using file from the cache, they will be copied into a temporary location. This applies to SampleData download, datastore download, tests, …</li>
<li>each Slicer start would be associated with a unique temporary folder (e.g Slicer-NNN or Slicer-test-NNN) and only the last X one would be kept.</li>
</ul>

---

## Post #8 by @lassoan (2018-12-14 20:26 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="5014">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>using file from the cache, they will be copied into a temporary location. This applies to SampleData download</p>
</blockquote>
</aside>
<p>We should be able to load data directly from cache. We don’t even know what files we need to copy to a temporary location (we often need multiple files to be able to load data, e.g., for nhdr+raw files, MRML scenes, DICOM data).</p>

---
