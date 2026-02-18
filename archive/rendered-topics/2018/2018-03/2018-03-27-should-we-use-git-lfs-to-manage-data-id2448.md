# Should we use Git LFS to manage data?

**Topic ID**: 2448
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/should-we-use-git-lfs-to-manage-data/2448

---

## Post #1 by @Lorensen (2018-03-27 21:38 UTC)

<p>You might consider git lfs (large file system) for the large files. I<br>
use in the VTKExamples for some of the very large datasets.</p>
<p>Bill</p>

---

## Post #2 by @jcfr (2018-03-28 00:08 UTC)

<p>Thanks for the suggestion Bill.</p>
<p>To manage the data, I think we will standardize on the approach already used by ITK. See <a href="https://itk.org/ITKExamples/Documentation/Contribute/UploadBinaryData.html">https://itk.org/ITKExamples/Documentation/Contribute/UploadBinaryData.html</a></p>

---

## Post #3 by @Lorensen (2018-03-28 01:00 UTC)

<p>Lfs maybe lower maintenance and less Kitware resources. Remember Midas?</p>
<p>I expect that GitHub has more resources and it is part of their core.</p>
<p>Also when you transition to GitHub, try to avoid any Kitware Slicer mods. Don’t fall into the Gerrit trap by adding local mods.</p>

---

## Post #4 by @lassoan (2018-03-28 02:18 UTC)

<p>Do you know how does git-lfs work with private and public forks? Also, can anybody contribute new data sets or update them using pull requests?</p>

---

## Post #5 by @jcfr (2018-03-28 03:29 UTC)

<blockquote>
<p>Remember Midas?</p>
</blockquote>
<p>So far, it has been working reasonably well. Associated with the Midas instance currently used to handle the Slicer data and packages, there is more than 350k items stored in the database. (<em>this a side topic, but they have been working on the new iteration of this infrastructure now called <a href="https://github.com/girder/slicer_package_manager#readme">Slicer package manager</a> that is built on top of <a href="http://girder.readthedocs.io">Girder</a>- more on this in a different post</em>)</p>
<p>Also thanks to the CMake <a href="https://cmake.org/cmake/help/latest/module/ExternalData.html">ExternalData</a> module, it is very easy to specify multiple data source, a global cache, and also granular download.</p>
<p>The multiple data source support allows to have redundancy of the data hosting and not rely on only one provider. For, example here are the <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/48e0febb8a4f7af4cb82397360133b596021f67b/CMake/ITKExternalData.cmake#L32-L49">data source configured for ITK</a>, with the option of easily providing your own list.</p>
<blockquote>
<p>I expect that GitHub has more resources and it is part of their core.</p>
</blockquote>
<p>Also, for the ITK releases, it is for example possible to leverage <a href="https://github.com/InsightSoftwareConsortium/ITKTestingData">GitHub to serve</a> the testing data leveraging GitHub pages feature.</p>
<p>Here are some more info I gathered while <a href="https://github.com/jcfr/bazel-large-files-with-girder#what-are-the-advantages-over-git-lfs-">investigating LFS last year</a>:</p>
<ul>
<li>
<p>it is all or nothing. No incremental download</p>
</li>
<li>
<p>it is does <a href="https://github.com/git-lfs/git-lfs/issues/1002">not support parallel download</a> at clone time. That, it is possible to workaround this <a href="https://github.com/git-lfs/git-lfs/wiki/Tutorial#pulling-and-cloning">setting an env variable</a> (or using the <code>--skip-smudge</code> option) to disable dowbload, and then run <code>git lfs pull</code> explicitly.</p>
</li>
<li>
<p>it requires an other tool to install. That said, it seems quite easy now by running</p>
</li>
<li>
<p>no central cache or way to share data between repo. (This has been an <a href="https://github.com/git-lfs/git-lfs/issues/766">issue</a> since 2015, was added to the git-lfs <a href="https://github.com/git-lfs/git-lfs/pull/1438">roadmap in 2016</a>, but it is <a href="https://github.com/git-lfs/git-lfs/blob/master/ROADMAP.md">still pending</a>.</p>
</li>
</ul>
<blockquote>
<p>it is all or nothing</p>
</blockquote>
<p><em>Here is a comment from a colleague that could mitigate this</em>:</p>
<p>For example, it is possible not to install git-lfs globally but rather do a local install after the repo is cloned if the data is needed at all.</p>
<p>This for example lets you have 1 repo with data present across several builds. The other builds point to this directory for their data rather than their own source dirs.  I imagine you could use the trick of never installing git-lfs globally (i.e., nothing in ~/.gitconfig) to prevent a global smudge and instead ask git-lfs during the build to smudge only certain files.</p>
<p>In addition, there is support for adding a default match exclusion<br>
(following <code>.gitignore</code> semantics) like this:</p>
<pre><code>git config -f .lfsconfig lfs.fetchexclude '*'
</code></pre>
<p>and then use similar logic that is in the <code>ExternalData</code> module to do<br>
manual <code>git lfs fetch &amp;&amp; git lfs checkout</code> commands to fetch data<br>
on-demand at build time.</p>
<h3><a name="p-9992-question-1" class="anchor" href="#p-9992-question-1" aria-label="Heading link"></a>question</h3>
<p>It would be great to hear feedback of someone using it on a day-to-day basis.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a> Since you have been though the process of implementing this for ITK, it would be great to hear your comments. If you would have to do it again, what would you choose ?</p>
<h3><a name="p-9992-itk-manual-references-2" class="anchor" href="#p-9992-itk-manual-references-2" aria-label="Heading link"></a>ITK manual references</h3>
<ul>
<li><a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/UploadBinaryData.md">https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/UploadBinaryData.md</a></li>
<li><a href="https://itk.org/ITKExamples/Documentation/Contribute/UploadBinaryData.html" class="inline-onebox">Upload Binary Data — v5.4.0</a></li>
</ul>

---

## Post #6 by @fedorov (2018-03-28 13:46 UTC)

<p>When I considered using git-lfs for another project some time ago, one of the key concerns was that it was not possible to download the data directly from the GitHub web site (or any other web site). The only way to get to it was to install git-lfs client, which I considered to be a huge deterrent for a non tech-savvy user. See the issue and communication with GitHub support summarized here: <a href="https://github.com/isaacs/github/issues/712">https://github.com/isaacs/github/issues/712</a>.</p>
<p>There were also other issues related to usability and possibly bugs in git-lfs implementation that I encountered at the time, but the lack of download without extra software was the deciding factor against git-lfs for me.</p>

---

## Post #7 by @thewtex (2018-03-28 13:47 UTC)

<p>CMake <code>ExternalData</code> has two important advantages:</p>
<ol>
<li>Simplicity</li>
<li>Lack of a dependence on a single point of failure</li>
</ol>
<p><code>git lfs</code> is similar to <code>git submodule</code> – it is an other set of commands that a developer must learn, and it requires learning and keeping another model and state associated with the source code repository tree in your head. If you already know git submodules or git lfs, then they are nice. However, they are both a big barrier to entry for new contributors, many of which whom are just struggling to understand Git.</p>
<p>With ExternalData, a developer can just upload the binary in a simple web page interface, and download a file that contains its hash. In the past, this was more difficult because the Midas web interface was clunky and slow. Now, Girder is faster and the UI is much improved. And, <a class="mention" href="/u/zachmullen">@zachmullen</a> is working on making it even better. Or, it would be possible to create a simple web app to do this…</p>
<p>With ExternalData, multiple simple, redundant data stores are possible, including</p>
<ul>
<li><strong>A local cache</strong></li>
<li><strong>An archive that can be stored and distributed with a release</strong></li>
<li>GitHub pages</li>
<li>A Midas server</li>
<li>A Girder server</li>
<li>An Apache server</li>
<li>An Azure blob store</li>
<li>Cloud provider X’s blob storage service</li>
</ul>
<p>For ITK, we have used the first seven options throughout the project’s lifetime. If one of the resources is not available, the system tries a different resource. This means you are rarely, if ever, disabled when you are offline, have a poor connection, or the LFS server is offline.</p>
<p>Also, CMake ExternalData requires no other dependencies if you are already using CMake.</p>

---

## Post #8 by @Lorensen (2018-03-28 14:00 UTC)

<p>I had no trouble install a client. I think any approach will require<br>
some setup. That said, my comments were only meant to start a<br>
discussion. I am no expert on this subject. For my small project<br>
<a href="https://lorensen.github.io/VTKExamples/site/" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/</a> it works. A more<br>
sophisticated approach is probably required for Slicer…</p>
<p>Bill</p>

---

## Post #9 by @ihnorton (2018-03-28 14:07 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="2448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>it is all or nothing. No incremental download</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="2448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>When I considered using git-lfs for another project some time ago, one of the key concerns was that it was not possible to download the data directly from the GitHub web site</p>
</blockquote>
</aside>
<p>I was also looking at git-lfs recently, and this seems to have changed:</p>
<p><a href="https://github.com/SlicerDMRI/DMRITestData/blob/master/Tractography/fiber_ply_export_test.vtk?raw=true" class="onebox" target="_blank" rel="noopener">https://github.com/SlicerDMRI/DMRITestData/blob/master/Tractography/fiber_ply_export_test.vtk?raw=true</a></p>
<p>from:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerDMRI/DMRITestData">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerDMRI/DMRITestData" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/9dfe33574d4d08ced5a12aff2fcea17f09489ef2a5b8374e4141b2a179569632/SlicerDMRI/DMRITestData" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerDMRI/DMRITestData" target="_blank" rel="noopener">GitHub - SlicerDMRI/DMRITestData</a></h3>

  <p>Contribute to SlicerDMRI/DMRITestData development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>So, this would allow git-lfs to be used for <em>data management</em>, but not necessarily for runtime usage – clients would still download from a hash.</p>
<p>However, my personal opinion on git-lfs is a bit low right now because it broke all git pushes when I enabled it on a repo, due to <a href="https://github.com/git-lfs/git-lfs/issues/2291">this bug</a> (can’t use github tokens with macOS credential helper). Uninstalling was easy and restored ability to push, but figuring out that I needed to do so took some time. Credential helper support should be a relatively simple fix, so somewhat concerning that it has not been fixed promptly.</p>
<p>I like the idea of reducing dependence on bespoke projects, but given that (1) on the client side, we are just pulling from raw URLs no matter what and (2) girder implements the S3 API (proprietary, but more-or-less a standard at this point), girder is only a soft dependency. We could move the data to any storage that implements S3-style buckets.</p>
<p>(to that end, it would be good to eventually put the data URLs and hashes in separate files rather that inline in cmake files – but not a priority)</p>

---

## Post #10 by @fedorov (2018-03-28 14:22 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="9" data-topic="2448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>this seems to have changed</p>
</blockquote>
</aside>
<p>It’s nice to see that individual files can be downloaded, but the issue remains that when the whole repository is downloaded as ZIP, it only contains git-lfs pointers to the data.</p>

---

## Post #11 by @fedorov (2018-10-24 15:27 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="2448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>It’s nice to see that individual files can be downloaded, but the issue remains that when the whole repository is downloaded as ZIP, it only contains git-lfs pointers to the data.</p>
</blockquote>
</aside>
<p>I was looking into this again, and as of today at least, if I download the whole directory as ZIP, individual files are downloaded, and not just links.</p>

---

## Post #12 by @fedorov (2018-11-01 19:51 UTC)

<p>Someone alerted me to this issue again, and I realized was checking this using a repository that contains git-lfs managed content side by side with a large file directly stored in the repo. I downloaded the whole repo as zip, and concluded the behavior changed because I saw that large file.</p>
<p>It remains the case that git-lfs managed content is NOT included when the repository containing that content is downloaded as ZIP.</p>
<p>I apologize for my sloppiness.</p>

---

## Post #13 by @lassoan (2018-11-02 16:19 UTC)

<p>I’ve tested git-lfs and have mixed results.</p>
<p>Good:</p>
<ul>
<li>easy to set up, just install git-lfs and specify what files should be stored using git-lfs (you can specify folders and/or file extensions)</li>
<li>works nicely and transparently when used on systems where git-lfs is installed</li>
<li>git-lfs files show up on Github’s web interface as regular files (e.g., you see the actual file content instead of pointer information)</li>
</ul>
<p>Bad:</p>
<ul>
<li>Github’s web interface always uploads files as regular files</li>
<li>If someone commits files who has not installed git-lfs, those files will be committed as regular files</li>
<li>Regular files can be converted to git-lfs files (there is an officially supported script for that), but it rewrites git history</li>
<li>Users reported various esoteric issues that were hard to understand and fix (see <a href="https://github.com/git-lfs/git-lfs/issues/1939">1</a>, <a href="https://github.com/git-lfs/git-lfs/issues/1544">2</a>, <a href="https://github.com/git-lfs/git-lfs/issues/2839">3</a>), even when users were careful and experienced. It is scary to think about how wrong things can go when we accept pull request from a larger community.</li>
</ul>

---

## Post #14 by @fedorov (2018-11-02 16:43 UTC)

<p>In addition to the “Bad” above, it should not be forgotten that git-lfs (if we use GitHub hosting, and if we don’t, the idea of consolidating things in one place goes away) requires the user to buy “data packs”. Included is only “1 GB of free storage and 1 GB a month of free bandwidth” (see <a href="https://help.github.com/articles/about-storage-and-bandwidth-usage/">https://help.github.com/articles/about-storage-and-bandwidth-usage/</a>). Also, “Purchasing data packs for Git LFS is independent of any other paid plan on GitHub”, which to me means that the free entry level plan that any academic user can get does not give you any “data packs”. If we keep data on git-lfs, I imagine we would be checking it out quite frequently with nightly testing and users downloading sample data, so this fee alone might be a complete stopper.</p>

---

## Post #16 by @kayarre (2021-11-13 01:29 UTC)

<p>I know this is an old thread but  has there been any more learning gather in this realm?<br>
Is there something out there at this point that is something in-between a full blown <code>girder</code> implementation and git-lfs approach? i.e. is there a “deploy a girder instance” equivalent to the “create a repo in github” out there in the wild yet?</p>
<p>it seems like git-lfs has the lowest bar to entry from a developer standpoint for smaller projects?</p>

---
