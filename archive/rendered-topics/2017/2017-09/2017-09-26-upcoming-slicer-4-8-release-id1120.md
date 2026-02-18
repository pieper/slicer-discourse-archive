# Upcoming Slicer 4.8 release

**Topic ID**: 1120
**Date**: 2017-09-26
**URL**: https://discourse.slicer.org/t/upcoming-slicer-4-8-release/1120

---

## Post #1 by @jcfr (2017-09-26 13:30 UTC)

<p>Hi Slicers,</p>
<p><strong>Update</strong>: We are currently addressing outstanding issues and cleaning up the issue tracker, once completed (in the two weeks timeframe), we will cut the 4.8 release.</p>
<p>If there are any outstanding issues you would like to see addressed for the release, report them on  <a href="https://issues.slicer.org/">https://issues.slicer.org/</a> and reply to this topic. We would also be happy to review patches.</p>
<p><strong>Extensions</strong>: We will also do a final call (by email) to extension maintainers so that we integrate PRs or fix their extensions. Without any response, we will either remove the extension from extension index or transfer the GitHub project into the Slicer organization so that it can be maintained by the community. See <a href="https://discourse.slicer.org/t/slicer-extensions-action-required-by-maintainers/1003">Slicer extensions: Action required by maintainers</a></p>
<p><strong>Next steps</strong> Following the 4.8 release, we will transition to Qt5 and VTK8 and start working on Slicer 5.0. Transition to python 3 is also planned.</p>
<p>Thanks,<br>
Jc</p>

---

## Post #2 by @pieper (2017-10-03 14:55 UTC)

<p>After discussion today we are thinking we will be able to release on Oct 18!</p>

---

## Post #3 by @bpaniagua (2017-10-03 15:22 UTC)

<p>Hurray! Very glad to hear this!</p>

---

## Post #4 by @jcfr (2017-10-18 00:21 UTC)

<p>Hi Slicers,</p>
<p>The release is imminent !</p>
<p>Here is a google document where I started to aggregate the ChangeLog for the announcements. I basically went through the ~1000 commit since Slicer 4.6 and grouped them into categories by omitting and/or rephrasing some.</p>
<p>See <a href="https://docs.google.com/document/d/1w1yhhEU55fHDzEBSlzP1I1V9jWag_UCiO_4VPXcyHGQ/edit#">https://docs.google.com/document/d/1w1yhhEU55fHDzEBSlzP1I1V9jWag_UCiO_4VPXcyHGQ/edit#</a></p>
<h3>Action items</h3>
<p>Your help would be appreciated to populate the <strong>New Extensions</strong>, <strong>Improved Extensions</strong> and <strong>New trainings / tutorials</strong> sections.</p>
<p>You are also welcome to help organize the remaining of the document.</p>
<p>Once the document is complete, I will update the wiki.</p>
<h3>After the release</h3>
<p>Note that, these bullet points will then be added to a <code>CHANGES.md</code>. And following the release, we will incrementally keep track of the changes.</p>
<p>An interesting resource related to ChangeLog. See <a href="http://keepachangelog.com/en/1.0.0/">keepachangelog.com/en/1.0.0/</a></p>

---

## Post #5 by @jcfr (2017-10-18 15:17 UTC)

<h3>Update <span class="hashtag">#1</span>
</h3>
<ul>
<li>Release packages for <code>macOS</code> and <code>Windows</code> have being generated</li>
<li>The failure on <code>Linux</code> was an issue in the dashboard script, now fixed in <a href="https://github.com/Slicer/DashboardScripts/commit/6caeb06c8e60b9770639cfacc2de737fb9c064f4">Slicer/DashboardScripts@6caeb06c</a>.
<ul>
<li>CDash entry removed and build restarted using updated dashboard scripts.</li>
</ul>
</li>
<li>Wiki pages have been versioned.</li>
</ul>
<p>Stay tuned !</p>
<h3>Notes</h3>
<ul>
<li>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess">Release process checklist</a> updated to account for new option <code>Slicer_RELEASE_TYPE</code>
</li>
<li>Update of dashboard script now automated. See <a href="https://github.com/Slicer/DashboardScripts#rename-and-update-release-scripts">https://github.com/Slicer/DashboardScripts#rename-and-update-release-scripts</a>
</li>
</ul>
<h4>Analysis of the Linux failure</h4>
<p>As indicated above, there was an error in the dashboard script. While creating the release scripts, I used the <em>wrong</em> one as a template and it was missing:</p>
<pre><code class="lang-auto"># This will ensure compiler paths specified using the cache variable are used
# consistently.
set(ENV{CC} "/dev/null")
set(ENV{CXX} "/dev/null")

[...]

set(ADDITIONAL_CMAKECACHE_OPTION "
  CMAKE_C_COMPILER:FILEPATH=/usr/bin/gcc-4.6
  CMAKE_CXX_COMPILER:FILEPATH=/usr/bin/g++-4.6
  [...]
  ")
</code></pre>
<p>which led the linux build to use the older compiler <code>g++ 4.4</code> (available in the PATH) on that platform.</p>
<p>Instead , the script should explicitly use <code>g++ 4.6</code></p>
<p>See here for the list of available compilers on that build machine: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory-south-ubuntu.kitware">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#factory-south-ubuntu.kitware</a></p>

---

## Post #6 by @jcfr (2017-10-18 20:33 UTC)

<h3>Update <span class="hashtag">#2</span>
</h3>
<ul>
<li>Slicer package generated on all platforms - <strong>done</strong>
</li>
<li>Create release branches - <strong>done</strong>
</li>
<li>Update <a href="https://www.slicer.org/wiki/Release_Details#Slicer_4.8">Release_Details</a> wiki page  -<strong>done</strong>
</li>
<li>Update Mantis - <strong>done</strong>
</li>
<li>Update CDash - <strong>done</strong>
</li>
<li>Update Slicer wiki - <strong>done</strong>
</li>
</ul>
<p>Remaining:</p>
<ul>
<li>Clean-up older nightly packages</li>
<li>Manually sign packages</li>
<li>Tag release packages</li>
<li>Version NA-MIC data tree</li>
<li>Update ExtensionsIndex</li>
<li>Update external website</li>
</ul>

---

## Post #7 by @jcfr (2017-10-18 22:46 UTC)

<h3>Update <span class="hashtag">#3</span>
</h3>
<ul>
<li>Slicer package generated on all platforms - <strong>done</strong>
</li>
<li>Create release branches - <strong>done</strong>
</li>
<li>Update <a href="https://www.slicer.org/wiki/Release_Details#Slicer_4.8">Release_Details</a> wiki page  -<strong>done</strong>
</li>
<li>Update Mantis - <strong>done</strong>
</li>
<li>Update CDash - <strong>done</strong>
</li>
<li>Update Slicer wiki - <strong>done</strong>
</li>
<li>Version NA-MIC data tree - <strong>done</strong>  (associated release script was also tweaked - See <a href="https://github.com/Slicer/Slicer/pull/822">Slicer/Slicer#822</a>)</li>
<li>Update ExtensionsIndex - <strong>done</strong>
</li>
</ul>
<p>Doing:</p>
<ul>
<li>Tweaking ChangeLog - <strong>do not hesitate to help review, improve wording and add (or remove) content</strong> - <a href="https://docs.google.com/document/d/1w1yhhEU55fHDzEBSlzP1I1V9jWag_UCiO_4VPXcyHGQ/edit?ts=59e7c872#heading=h.ykslj6qjg0f">https://docs.google.com/document/d/1w1yhhEU55fHDzEBSlzP1I1V9jWag_UCiO_4VPXcyHGQ/edit?ts=59e7c872#heading=h.ykslj6qjg0f</a>
</li>
</ul>
<p>Remaining:</p>
<ul>
<li>Clean-up older nightly packages</li>
<li>Manually sign packages</li>
<li>Tag release packages</li>
<li>Update external website</li>
</ul>

---

## Post #8 by @jcfr (2017-10-19 07:54 UTC)

<h3><a name="p-5125-update-4-1" class="anchor" href="#p-5125-update-4-1" aria-label="Heading link"></a>Update <span class="hashtag-raw">#4</span></h3>
<p>Here it is:</p>
<p><a href="http://download.slicer.org/#installers"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2af3110fa387b6fc99321559b7a80e93974d10.png" alt="8" data-base62-sha1="zYMlaift3fvRQ4YOIFDY0NbYQ2k" width="690" height="125"></a></p>
<p>Remarks:</p>
<ul>
<li>
<p>We will formally announce the release, update social media, etc … <strong>after</strong> the announcements page and change log are fully updated.</p>
</li>
<li>
<p>Also anticipating a faster release cycle, the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess">ReleaseProcess</a> document has been cleaned up and improved.</p>
</li>
</ul>
<p>Doing:</p>
<ul>
<li>Tweaking <a href="https://docs.google.com/document/d/1w1yhhEU55fHDzEBSlzP1I1V9jWag_UCiO_4VPXcyHGQ/edit?ts=59e7c872#heading=h.ykslj6qjg0f">ChangeLog</a> : 75% complete</li>
</ul>
<p>Remaining:</p>
<ul>
<li>Define Slicer highlights to include in Announcements</li>
<li>Update list of <em>New and/or updated tutorials</em></li>
<li>Clean-up older nightly packages</li>
</ul>
<p>Completed:</p>
<ul>
<li>Slicer package generated on all platforms - <strong>done</strong></li>
<li>Create release branches - <strong>done</strong></li>
<li>Update <a href="https://www.slicer.org/wiki/Release_Details#Slicer_4.8">Release_Details</a> wiki page  -<strong>done</strong></li>
<li>Update Mantis - <strong>done</strong></li>
<li>Update CDash - <strong>done</strong></li>
<li>Update Slicer wiki - <strong>done</strong></li>
<li>Version NA-MIC data tree - <strong>done</strong></li>
<li>Update ExtensionsIndex - <strong>done</strong></li>
<li>Manually sign packages - <strong>done</strong></li>
<li>Tag release packages - <strong>done</strong></li>
<li>Update external website - (<a href="https://en.wikipedia.org/wiki/3DSlicer">wikipedia</a>: <strong>done</strong> , <a href="https://www.nitrc.org/projects/slicer/">nitrc</a>: <strong>to be done</strong>)</li>
</ul>

---

## Post #9 by @Fernando (2017-10-25 21:04 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I’ve updated the cask for the stable version:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/caskroom/homebrew-cask/blob/108ce53f6da821e5146afbca7fc707f02fc213e8/Casks/slicer.rb" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/caskroom/homebrew-cask/blob/108ce53f6da821e5146afbca7fc707f02fc213e8/Casks/slicer.rb" target="_blank" rel="nofollow noopener">caskroom/homebrew-cask/blob/108ce53f6da821e5146afbca7fc707f02fc213e8/Casks/slicer.rb</a></h4>
<pre><code class="lang-rb">cask 'slicer' do
  version '4.8.0.26489,700005'
  sha256 '9a13ef5084b1aee1fd56891c7c61cd5d8f093f17168fe996f067548cf4e825c8'

  # slicer.kitware.com/midas3 was verified as official when first introduced to the cask
  url "https://slicer.kitware.com/midas3/download?bitstream=#{version.after_comma}"
  appcast 'https://github.com/Slicer/Slicer/releases.atom',
          checkpoint: '51525b99e07c45a2001ee17dbd400a25060d465255498344d9e132931787b91d'
  name '3D Slicer'
  homepage 'https://www.slicer.org/'

  app 'Slicer.app'
end
</code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<h3>How to install Slicer 4.8 on macOS using brew ?</h3>
<p>So macOS users can do this to install Slicer 4.8:</p>
<pre><code class="lang-auto"># Install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install Slicer
brew cask install slicer
</code></pre>

---

## Post #10 by @jcfr (2017-10-26 21:39 UTC)

<h3>Final and last update <span class="hashtag">#5</span>
</h3>
<p>Hi Slicers,</p>
<p>Thanks everyone</p>
<ul>
<li>
<p><a href="https://discourse.slicer.org/t/slicer-4-8-summary-highlights-and-changelog/1292">Slicer 4.8: Summary, Highlights and Changelog</a> have been published in the <code>Annoucement/Release Notes</code> category.</p>
</li>
<li>
<p><a href="https://slicer.org">https://slicer.org</a> landing page as well as the <a href="https://www.slicer.org/wiki/Documentation/4.8/Announcements">Announcements</a> page have been updated.</p>
</li>
<li>
<p>In addition of the regular package available on <a href="http://download.slicer.org">http://download.slicer.org</a>, thanks to <a class="mention" href="/u/fernando">@Fernando</a> you can also <a href="https://discourse.slicer.org/t/upcoming-slicer-4-8-release/1120/9?u=jcfr">install Slicer 4.8 using brew</a></p>
</li>
</ul>
<p>Completed:</p>
<ul>
<li>Slicer package generated on all platforms - <strong>done</strong>
</li>
<li>Create release branches - <strong>done</strong>
</li>
<li>Update <a href="https://www.slicer.org/wiki/Release_Details#Slicer_4.8">Release_Details</a> wiki page  -<strong>done</strong>
</li>
<li>Update Mantis - <strong>done</strong>
</li>
<li>Update CDash - <strong>done</strong>
</li>
<li>Update Slicer wiki - <strong>done</strong>
</li>
<li>Version NA-MIC data tree - <strong>done</strong>
</li>
<li>Update ExtensionsIndex - <strong>done</strong>
</li>
<li>Manually sign packages - <strong>done</strong>
</li>
<li>Tag release packages - <strong>done</strong>
</li>
<li>Update external website - (<a href="https://en.wikipedia.org/wiki/3DSlicer">wikipedia</a>: <strong>done</strong> )</li>
<li>Update external website - ( <a href="https://www.nitrc.org/projects/slicer/">nitrc</a>: <strong>done</strong> - Thanks <a class="mention" href="/u/pieper">@pieper</a> - See <a href="https://www.nitrc.org/forum/forum.php?forum_id=7945">here</a> )</li>
<li>Tweaking <a href="https://docs.google.com/document/d/1w1yhhEU55fHDzEBSlzP1I1V9jWag_UCiO_4VPXcyHGQ/edit?ts=59e7c872#heading=h.ykslj6qjg0f">ChangeLog</a> <strong>done</strong>
</li>
<li>
<s>Update list of</s> <em>New and/or updated tutorials</em>  - <strong>done</strong> (Existing page was cleaned up and is referenced from the <a href="https://discourse.slicer.org/t/slicer-4-8-summary-highlights-and-changelog/1292">release notes</a>)</li>
<li>Define Slicer highlights to include in Announcements  -<strong>done</strong>
</li>
<li>Update Acknowledgments  -<strong>done</strong>
</li>
<li>Update <a href="http://slicer.org">slicer.org</a> - <strong>done</strong>
</li>
<li>Publish blog - <strong>done</strong> - See <a href="https://blog.kitware.com/3d-slicer-4-8-gets-released-with-improved-dicom-support-and-segmentation-capabilities/">here</a>
</li>
<li>Update macOS cask - <strong>done</strong> - Thanks <a class="mention" href="/u/fernando">@Fernando</a>
</li>
</ul>
<p>Remaining:</p>
<ul>
<li>Clean-up older nightly packages</li>
</ul>

---

## Post #11 by @pieper (2017-10-26 22:21 UTC)

<p>Nice! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I added a news item on nitrc with a pointer to the blog post.</p>

---
