# How can I subscribe to monitor individual extensions on Slicer dashboard?

**Topic ID**: 2261
**Date**: 2018-03-07
**URL**: https://discourse.slicer.org/t/how-can-i-subscribe-to-monitor-individual-extensions-on-slicer-dashboard/2261

---

## Post #1 by @fedorov (2018-03-07 15:57 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a href="https://github.com/QIICR/dcmqi/issues/335#issuecomment-369654159">mentioned</a></p>
<blockquote>
<p>The good news is that CDash support email notification and now support specifying more than one repository.</p>
</blockquote>
<p>Can someone help me figure out how to do this? My guess was that this should be configured in project subscription, but I don’t see how this can be done. There are no labels to select from.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25a332369c55f06fc2a43cd67469c65531872008.png" data-download-href="/uploads/short-url/5mXjnobeLRqTJCiCg7wlIvoFWdy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25a332369c55f06fc2a43cd67469c65531872008_2_644x500.png" alt="image" data-base62-sha1="5mXjnobeLRqTJCiCg7wlIvoFWdy" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25a332369c55f06fc2a43cd67469c65531872008_2_644x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25a332369c55f06fc2a43cd67469c65531872008_2_966x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25a332369c55f06fc2a43cd67469c65531872008.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×888 87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2018-03-07 17:10 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a> ,</p>
<p>When using <code>ctest</code> and <code>CDash</code> to build a single project, this work our of the box.</p>
<p>The challenge here is that we conveniently centralize the configure/build/test of more than hundred of projects.</p>
<p>You will find below comments and idea I came up with while looking at the current system</p>
<h3>in a nutshell</h3>
<p>… the extension build system is doing the following:</p>
<ol>
<li>Discover and parse all extension description files</li>
<li>Sort extension topologically based on dependency information</li>
<li>Add one external project per extension with associated dependency information  (this allow to support parallel build): This is used to download the source code and build the project.</li>
</ol>
<p>The external project is added <a href="https://github.com/Slicer/Slicer/blob/34cd89b97998bc0d23eaebcebc3b28bb5d6c689a/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtensions.cmake#L255-L263">here</a>.</p>
<h3>way forward</h3>
<p>The idea is to have for every extension build, repository <em>information</em> send along the configure/build/test restults. This should allow to associate together new configure/build/test error or warning with a given revision of the code.</p>
<p>To support this, I think we need to:</p>
<ol>
<li>keep around the extension source directory between successive builds</li>
<li>ensure that the command <a href="https://cmake.org/cmake/help/latest/command/ctest_update.html">ctest_update</a> is called.</li>
</ol>
<h3>Do we need to keep extension source checkout around between build ?</h3>
<p>Say differently, how does CTest/CDash find out the <em>diff</em> associated with two consecutive configure/build/test ?</p>
<p><strong>Note 1:</strong>  the <em>diff</em> is important to know as it allows to find out the list of authors who potentially introduced warnings/errors/failures/… and later notify them.</p>
<p><strong>Note 2:</strong> the extension sources are checked out cleanly every night, we are currently not keep source trees around. The only source tree we currently keep around it the one associated with the <a href="https://github.com/Slicer/ExtensionsIndex/">ExtensionsIndex</a></p>
<p>The answer to this question will help us move forward and decide what are the steps.</p>
<h4>case 1: if the answer is no</h4>
<p>This means that CDash can compute the <em>diff</em> on its his own by only using the build name and repository name.</p>
<p>In that case, it may be as simple as adding the <code>ctest_update</code> call between these two calls:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/34cd89b97998bc0d23eaebcebc3b28bb5d6c689a/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L133-L134" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/34cd89b97998bc0d23eaebcebc3b28bb5d6c689a/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L133-L134" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/34cd89b97998bc0d23eaebcebc3b28bb5d6c689a/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L133-L134</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="133" style="counter-reset: li-counter 132 ;">
<li>ctest_start(${CTEST_MODEL} TRACK ${track} ${EXTENSION_SOURCE_DIR} ${EXTENSION_SUPERBUILD_BINARY_DIR})</li>
<li>ctest_read_custom_files(${EXTENSION_SUPERBUILD_BINARY_DIR} ${EXTENSION_SUPERBUILD_BINARY_DIR}/${EXTENSION_BUILD_SUBDIRECTORY})</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><strong>intuition:</strong> I doubt this is the case, I will confirm this with the CDash development team.</p>
<h3>case 2: if the answer is yes</h3>
<p>This means that the <em>diff</em> is generated locally by using the call to <code>ctest_update</code></p>
<p>In that case, I think more changes would be involved:</p>
<p>We need to:</p>
<ol>
<li>update the system to keep <code>extension source checkouts</code> outside of the <code>extension index build tree</code>
</li>
<li>use <code>ctest_update</code> to update the checkout instead of teaching ExternalProject how to do it. The code used to setup the download command is <a href="https://github.com/Slicer/Slicer/blob/34cd89b97998bc0d23eaebcebc3b28bb5d6c689a/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtensions.cmake#L132-L213">here</a>
</li>
</ol>
<p>Setting either <a href="https://cmake.org/cmake/help/latest/variable/CTEST_GIT_UPDATE_OPTIONS.html#variable:CTEST_GIT_UPDATE_OPTIONS">CTEST_GIT_UPDATE_OPTIONS</a> or  <a href="https://cmake.org/cmake/help/latest/variable/CTEST_GIT_UPDATE_CUSTOM.html#variable:CTEST_GIT_UPDATE_CUSTOM">CTEST_GIT_UPDATE_CUSTOM</a>  should help checking a specific branch or commit.</p>
<p>i also suggest we transition all remaining extensions from <strong>svn</strong> to <strong>git</strong>, and only support <strong>git</strong>. That would help simplify the system.</p>

---

## Post #3 by @fedorov (2018-03-07 21:38 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> thank you for this thorough analysis. But, in a nutshell, this basically means we cannot monitor status of the individual extensions at the moment.</p>
<p>I am fully aware about the extremely limited resources, and unfortunately I have no resources to contribute to solving this issue. So I guess we will wait for better times to revisit this…</p>

---

## Post #4 by @jcfr (2018-03-07 21:39 UTC)

<p>I will follow up shortly, I have meeting with the CDash core developer in few minutes.</p>

---

## Post #5 by @fedorov (2018-03-07 21:53 UTC)

<p>So, as I was thinking about this, conceptually at least, this looks like a very manageable problem to solve (“this” == automatic notification about failing extensions based on the dashboard status).</p>
<p>A while ago, when I ran into this, I wrote <a href="https://github.com/fedorov/CDashWrangler">this script</a> to parse the dashboard HTML. I would not be surprised if this is broken by now, but I am also confident this can be done for the current incarnation of the the dashboard.</p>
<p>If we forget about the peculiarities of CDash/current system, isn’t it as simple as having a cron job running that kind of script and sending emails? Am I missing something?</p>
<p>What if we have the following setup:</p>
<ol>
<li>upon successful completion of all builds on the dashboard, some webhook is called to initiate a CI build (I think this webhook is the only piece missing).</li>
<li>CI script downloads the dashboard HTML page, parses it, and figures out the status of all extensions.</li>
<li>For projects hosted on GitHub we can <a href="https://developer.github.com/v3/repos/#list-contributors">automatically get the list of contributors</a>, and send them automatic notifications if dashboard problems with their extension are identified.</li>
<li>To keep things simple, we could hard-code the list of extensions for which we would send notifications to not bother with the subscribe/unsubscribe functionality.</li>
</ol>

---

## Post #6 by @ihnorton (2018-03-07 22:21 UTC)

<p>Instead of parsing html, you could use the <a href="https://www.paraview.org/Wiki/CDash:API">API</a>.</p>
<p>e.g.: <a href="http://slicer.cdash.org/api/v1/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=radiomics">http://slicer.cdash.org/api/v1/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=radiomics</a> (for corresponding <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercombine=or&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=radiomics">html page</a>)</p>

---

## Post #7 by @lassoan (2018-03-08 02:05 UTC)

<p>CDash almost does everything that we need and would offer more then the proposed custom scraping/query-based solution (can take into account repository modifications, has convenient web GUI for notification configuration, etc).</p>
<p>Setting up a notification system once may be less work than improving CDash, but in the long term it would probably cost more time to continuously maintain and support a custom system.</p>

---

## Post #8 by @fedorov (2018-03-08 03:58 UTC)

<p>Indeed, but in absence of a perfect solution, there is no notifications mechanism for years now, and it happens again and again (at least for me!) that extensions get broken and that remains unnoticed.</p>
<p>The good part is that the solution I proposed, in its most simple implementation using a locally running cron job, has 0 dependencies and is easy to implement with minimum resources (unless I am missing something, which may well be). I will update this thread when I get around to do it.</p>

---

## Post #9 by @fedorov (2018-03-08 03:59 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="6" data-topic="2261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Instead of parsing html, you could use the API.</p>
</blockquote>
</aside>
<p>Yes, JC mentioned that in the past as well, but I had troubles locating documentation. I agree, I should search again.</p>

---

## Post #10 by @vkt1414 (2023-11-02 10:26 UTC)

<p>thanks to <a class="mention" href="/u/fedorov">@fedorov</a> and <a class="mention" href="/u/ihnorton">@ihnorton</a>, we have now set up simple GitHub actions to check the status of the extension’s build.</p>
<p><a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser/pull/16" rel="noopener nofollow ugc">A github actions workflow to notify if building the extension fails by vkt1414 · Pull Request #16 · ImagingDataCommons/SlicerIDCBrowser</a></p>

---

## Post #11 by @fedorov (2023-11-02 12:52 UTC)

<p>Thank you <a class="mention" href="/u/vkt1414">@vkt1414</a> - this addresses the immediate problem for me! Most definitely, the proper way to address this would be via some kind of a notification or status reporting mechanism from CDash, but clearly it is either not easy, not a priority, or both.</p>
<p>We should go ahead and implement this for all of the extensions we maintain! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @vkt1414 (2023-11-02 13:06 UTC)

<p>Great. Github actions is turning out to be an excellent tool to do all the chores.<br>
any other extensions to keep track of, than below?<br>
DCMQI<br>
QuantitativeReporting<br>
QIICR SDT<br>
SlicerMRunner (mhub)<br>
mpReview</p>

---

## Post #13 by @pieper (2023-11-02 13:54 UTC)

<p><a class="mention" href="/u/vkt1414">@vkt1414</a> can you provide some more documentation about this feature?  Specifically where does it post the results and how do people set it up for their own extensions?</p>

---

## Post #14 by @vkt1414 (2023-11-02 14:31 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> !</p>
<p>Absolutely!</p>
<p>I wrote a simple GitHub actions script that runs a python script that calls the cdash API to get the build info. It extracts the error counts from all categories (configuration, compilation, and test). If the sum of errors is greater than zero, I simply triggered an exit code 1 to fail the GitHub actions, and it should then send a notification.</p>
<p>To adapt this workflow to any extension, copy the .github/ folder to any repo, and then just need to modify the variable ‘slicerExtensionName’ in the get_build_status.py, and that’s it. Happy to submit a pull request if you would like me to submit one for any extension!</p>
<p><a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser/tree/main/.github" rel="noopener nofollow ugc">SlicerIDCBrowser/.github at main · ImagingDataCommons/SlicerIDCBrowser</a></p>
<p>We are not posting the results anywhere, the script just prints the counts of errors to the console.</p>
<p>One big picture idea I had was, if we want to implement for all extensions as part of slicer, we can use an action like this <a href="https://github.com/marketplace/actions/send-email" rel="noopener nofollow ugc">Send email · Actions · GitHub Marketplace</a> to send notifications to only developers of the extension, as I believe we can get contributors email addresses from github api. We will need to setup some official slicer email address I guess. Just my two cents.</p>

---

## Post #15 by @jcfr (2023-11-02 14:47 UTC)

<p>This is a great idea <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<p>What do you think of generalizing this to all extensions ?</p>
<p>Possible workflow:</p>
<ul>
<li>When errors (or warnings) are reported for a specific extension, have an issue titled <code>ExtensionName [Preview]</code> or <code>ExtensionName [Stable X.Y]</code> created in the <a href="https://github.com/Slicer/ExtensionsIndex">Slicer/ExtensionsIndex</a> GitHub project.</li>
<li>In the issue description, include a comment to notify code owners associated with this extension</li>
<li>If an issue for a given extension already exists, it could be closed if there are no more errors.</li>
</ul>
<p>Some pointers:</p>
<ul>
<li>add a workflow to <a href="https://github.com/Slicer/ExtensionsIndex/">https://github.com/Slicer/ExtensionsIndex/</a></li>
<li>add a <a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners">CODEOWNERS</a> file   to the <code>ExtensionsIndex</code> associating each <code>.s4ext</code> with relevant developers</li>
<li>issue automatically created would be opened by the <code>slicerbot</code> GitHub user</li>
</ul>
<p>Related actions:</p>
<ul>
<li><a href="https://github.com/marketplace/actions/codeowners-action">https://github.com/marketplace/actions/codeowners-action</a></li>
</ul>

---

## Post #16 by @vkt1414 (2023-11-02 15:16 UTC)

<p>Sounds like a great idea! I have not used the CODEOWNERS file before but the only gripe I have is, that someone will have to maintain the CODEOWNERS file or you make it a requirement, whenever a new extension is added I guess.</p>
<p>I’ll be happy to work on this and report back!</p>

---

## Post #17 by @pieper (2023-11-02 15:30 UTC)

<p>Sounds great <a class="mention" href="/u/vkt1414">@vkt1414</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">   This should be really helpful.</p>

---

## Post #18 by @vkt1414 (2023-11-13 19:25 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/pieper">@pieper</a>, and <a class="mention" href="/u/fedorov">@fedorov</a>,</p>
<p>I’ve worked on this and summarized my progress in the attached figure.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10f76c2f9e8585a0c6dff905bcd7cff600003aad.png" data-download-href="/uploads/short-url/2q5JSAekEE5fBuzWmLDhdlJzxKJ.png?dl=1" title="Copy of Decision Tree Diagram by Slidesgo (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10f76c2f9e8585a0c6dff905bcd7cff600003aad_2_690x388.png" alt="Copy of Decision Tree Diagram by Slidesgo (2)" data-base62-sha1="2q5JSAekEE5fBuzWmLDhdlJzxKJ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10f76c2f9e8585a0c6dff905bcd7cff600003aad_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10f76c2f9e8585a0c6dff905bcd7cff600003aad.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10f76c2f9e8585a0c6dff905bcd7cff600003aad.png 2x" data-dominant-color="EDECEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Copy of Decision Tree Diagram by Slidesgo (2)</span><span class="informations">960×540 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve been conducting my experiments on a fork, without actually tagging anyone (for now). You can view the issues that GitHub actions bot has created/closed here <a href="https://github.com/vkt1414/ExtensionsIndex/issues" rel="noopener nofollow ugc">link</a>.</p>
<p>The GitHub Actions workflow I’ve been using can be found <a href="https://github.com/vkt1414/ExtensionsIndex/blob/main/.github/workflows/notify_code_owners.yaml" rel="noopener nofollow ugc">here</a>, and the CODEOWNERS file is located <a href="https://github.com/vkt1414/ExtensionsIndex/blob/main/CODEOWNERS" rel="noopener nofollow ugc">here</a>.</p>
<p>I would appreciate any feedback or suggestions for improvement. One area that could use refinement is the CODEOWNERS file. Currently, I check contributors and select the individual who merged the most recent pull request. If more people should be notified, we can edit the file to include them.</p>
<p>This workflow does not interfere if an extension already has a point of contact. However, it will automatically check for new extensions that do not have a CODEOWNER. If you wish to edit it, feel free to do so once I submit the PR. Whether you choose to commit the updated CODEOWNERS back to the repo when an extension lacks a CODEOWNER is entirely up to you. I can add another step to the workflow to accommodate this.</p>
<p>Another thing I would like to know is if there is a github issue for an extension already, I do not update it. Should we? I do not if some extensions are maintained anymore, so we will have a long thread if errors or warnings are not addressed promptly.</p>
<p>Please note that a limitation of this workflow is that non-GitHub repositories cannot be notified.</p>
<p>Looking forward to your feedback.</p>

---

## Post #19 by @fedorov (2023-11-13 19:59 UTC)

<p><a class="mention" href="/u/vkt1414">@vkt1414</a> I think this is excellent! Having all issues opened under ExtensionsIndex is very good from the user perspective, I think, since it helps with having a single point to check the status.</p>
<p>If we had a vote, I would definitely support adding this to ExtensionIndex - it’s such a huge improvement over what we have right now (which isn’t much!) in terms of helping developers monitor the dashboard, and informing users about the de facto status of the extensions based on nightly tests.</p>

---
