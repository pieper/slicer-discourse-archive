---
topic_id: 933
title: "Slicer Installation On Mac Using Homebrew"
date: 2017-08-23
url: https://discourse.slicer.org/t/933
---

# Slicer installation on Mac using homebrew

**Topic ID**: 933
**Date**: 2017-08-23
**URL**: https://discourse.slicer.org/t/slicer-installation-on-mac-using-homebrew/933

---

## Post #1 by @Fernando (2017-08-23 19:48 UTC)

<p>It works fine for me using <code>brew</code>:</p>
<pre><code class="lang-auto">brew cask install https://raw.githubusercontent.com/fepegar/homebrew-versions/cask_repair_update-slicer-nightly/Casks/slicer-nightly.rb
</code></pre>
<p>Note: once the <a href="https://github.com/caskroom/homebrew-versions/pull/4318" rel="nofollow noopener">PR</a> is accepted, the line will just be:</p>
<pre><code class="lang-auto">brew cask install slicer-nightly
</code></pre>

---

## Post #2 by @fedorov (2017-08-23 20:01 UTC)

<p>This is great progress <a class="mention" href="/u/fernando">@Fernando</a>, but I am pretty sure brew approach is still not going to work for 100% of Mac users. It won’t replace the package.</p>

---

## Post #3 by @Fernando (2017-08-23 20:04 UTC)

<aside class="quote no-group quote-post-not-found" data-username="fedorov" data-post="4" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/4">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>I am pretty sure brew approach is still not going to work for 100% of Mac users. It won’t replace the package.</p>
</blockquote>
</aside>
<p>Why? What do you mean? What is exactly <em>the package</em>? Have you read the Lab about it?<br>
<a href="https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask</a></p>
<p>It’d be nice to get some feedback <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @fedorov (2017-08-23 20:25 UTC)

<aside class="quote no-group quote-modified" data-username="Fernando" data-post="5" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/5">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>Why? What do you mean?</p>
</blockquote>
</aside>
<p>Sorry for not being specific. I was just thinking about some of the Slicer users I know who are MDs. I am not sure they would appreciate using terminal and learning about brew and casks. I can’t imagine them running the steps you listed in “Steps to upgrade Slicer app (for users)” on the page lab page you referenced.</p>
<aside class="quote no-group quote-modified" data-username="Fernando" data-post="5" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/5">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>What is exactly the package?</p>
</blockquote>
</aside>
<p>For the users like above, <em>the package</em> is the dmg file that they download from the Slicer web page.</p>

---

## Post #5 by @lassoan (2017-08-23 20:45 UTC)

<p>I’m not a mac user, but this seems to be a very nice option for developers who use homebrew for installing applications.</p>
<p>Do you know if we can track number of downloads/installations/updates done through homebrew? If not, then we need to implement a more robust mechanism to measure application usage (e.g., check for updates at application startup and count these checks on the server side).</p>

---

## Post #6 by @fedorov (2017-08-23 20:47 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="7" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/7">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>this seems to be a very nice option for developers who use homebrew for installing applications</p>
</blockquote>
</aside>
<p>I completely agree. It is very nice to have this feature, I am glad <a class="mention" href="/u/fernando">@Fernando</a> is working on this, and I appreciate it! All I am saying is that it will not replace the downloadable dmg packages for Mac for all of the Slicer users on Mac.</p>

---

## Post #7 by @Fernando (2017-08-23 20:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/fedorov">@fedorov</a>, thanks a lot for your opinions!</p>
<aside class="quote no-group quote-post-not-found" data-username="fedorov" data-post="8" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/8">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>All I am saying is that it will not replace the downloadable dmg packages for Mac for all of the Slicer users on Mac.</p>
</blockquote>
</aside>
<p>Andrey, I didn’t propose it as a replacement of the package but as an alternative for the process of installing and upgrading. I think most users (like the MDs) will be doing it the traditional way, but I also think that developers will appreciate this approach. Also, it’s very easy to <a href="https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask#Update" rel="noopener nofollow ugc">maintain</a> by the Kitware machines. I think <a class="mention" href="/u/jcfr">@jcfr</a> can confirm this.</p>
<p>Also, the package <em>is</em> downloaded and automatically mounted, installed and unmounted by <code>brew</code>.</p>
<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="7" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/7">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>Do you know if we can track number of downloads/installations/updates done through homebrew?</p>
</blockquote>
</aside>
<p>Andras, according to <a class="mention" href="/u/pieper">@pieper</a>, <a href="https://discourse.slicer.org/t/add-slicer-nightly-to-homebrew-macos/811/10">they’ll be tracked as usual</a> because the packages are still <a href="https://github.com/caskroom/homebrew-versions/blob/master/Casks/slicer-nightly.rb#L6" rel="noopener nofollow ugc">downloaded from midas</a>.</p>

---

## Post #8 by @Fernando (2017-08-23 20:56 UTC)

<p>BTW Linux users might also be able to brew Slicer, I can work on it if needed: <a href="http://linuxbrew.sh/" rel="nofollow noopener">http://linuxbrew.sh/</a></p>

---

## Post #9 by @jcfr (2017-08-23 20:59 UTC)

<aside class="quote no-group quote-post-not-found" data-username="Fernando" data-post="9" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/9">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>as an alternative for the process of installing and upgrading.</p>
</blockquote>
</aside>
<p>It will be complementary.</p>
<p>Similarly to a potential <code>sudo apt-get install slicer</code> and alike …</p>
<aside class="quote no-group quote-post-not-found" data-username="Fernando" data-post="9" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/9">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>they’ll be tracked as usual because the packages are still downloaded from midas.</p>
</blockquote>
</aside>
<p>Indeed, in that particular case, see</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Homebrew/homebrew-cask-versions/blob/a875838c82cac4f2e3a930444beb7f6397efdf5f/Casks/slicer-nightly.rb#L6">
  <header class="source">

      <a href="https://github.com/Homebrew/homebrew-cask-versions/blob/a875838c82cac4f2e3a930444beb7f6397efdf5f/Casks/slicer-nightly.rb#L6" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Homebrew/homebrew-cask-versions/blob/a875838c82cac4f2e3a930444beb7f6397efdf5f/Casks/slicer-nightly.rb#L6" target="_blank" rel="noopener">Homebrew/homebrew-cask-versions/blob/a875838c82cac4f2e3a930444beb7f6397efdf5f/Casks/slicer-nightly.rb#L6</a></h4>



    <pre class="onebox"><code class="lang-rb">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>cask 'slicer-nightly' do</li>
          <li>  version '4.7.0.26296,679359'</li>
          <li>  sha256 '20c254f36ccd753c969523c75aa5962525411e9777857589d7944b718241e32a'</li>
          <li></li>
          <li>  # slicer.kitware.com/midas3 was verified as official when first introduced to the cask</li>
          <li class="selected">  url "http://slicer.kitware.com/midas3/download?bitstream=#{version.after_comma}"</li>
          <li>  name '3D Slicer Nightly'</li>
          <li>  homepage 'https://www.slicer.org/'</li>
          <li></li>
          <li>  app 'Slicer.app'</li>
          <li>end</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group quote-post-not-found" data-username="Fernando" data-post="9" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/9">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>Also, it’s very easy to maintain by the Kitware machines. I think <a class="mention" href="/u/jcfr">@jcfr</a> can confirm this.</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @pieper (2017-08-23 21:16 UTC)

<p>I like the idea of linuxbrew!   Unfortunately there doesn’t seem to be a windowsbrew but of course there are <a href="https://laracasts.com/discuss/channels/laravel/homebrew-install-on-windows-os">some alternatives</a>.</p>
<p>Also I suppose if we wanted to we could make a wrapper application (maybe with Qt or with <a href="https://electron.atom.io/">electron</a> or similar) that provided a consistent user installation experience across platforms.</p>

---

## Post #11 by @fedorov (2017-08-23 21:16 UTC)

<aside class="quote no-group quote-post-not-found" data-username="Fernando" data-post="9" data-topic="932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"><a href="https://discourse.slicer.org/t/unable-to-open-slicer-package-on-mac/932/9">Unable to open Slicer package on Mac</a></div>
<blockquote>
<p>Andrey, I didn’t propose it as a replacement of the package but as an alternative for the process of installing and upgrading. I think most users (like the MDs) will be doing it the traditional way, but I also think that developers will appreciate this approach.</p>
</blockquote>
</aside>
<p>I completely agree with you.</p>

---

## Post #12 by @fedorov (2017-08-23 21:42 UTC)

<p>For completeness, this discussion could be considered a follow up on <a href="https://discourse.slicer.org/t/add-slicer-nightly-to-homebrew-macos/811">Add Slicer Nightly to Homebrew (macOS)</a></p>

---

## Post #13 by @Fernando (2017-08-23 22:12 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I like the idea of linuxbrew!   Unfortunately there doesn’t seem to be a windowsbrew but of course there are some alternatives.</p>
</blockquote>
</aside>
<p>Looks good, I’ll explore those too.</p>

---

## Post #14 by @jcfr (2017-08-23 22:42 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="13" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>there doesn’t seem to be a windowsbrew</p>
</blockquote>
</aside>
<p>That would be <a href="https://chocolatey.org/">https://chocolatey.org/</a></p>

---

## Post #15 by @Fernando (2017-08-24 01:06 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I like the idea of linuxbrew!</p>
</blockquote>
</aside>
<p>I have been checking. Unfortunately there’s only <code>brew</code> and no <code>brew cask</code>, so only command-line tools can be installed with Linuxbrew.</p>
<aside class="quote no-group" data-username="jcfr" data-post="14" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That would be <a href="https://chocolatey.org/" rel="noopener nofollow ugc">https://chocolatey.org/</a></p>
</blockquote>
</aside>
<p>I have also taken a look at <code>choco</code>. I tried creating a package for Slicer, but I finally gave up. It’s way more complicated than <code>brew</code>.</p>

---

## Post #16 by @Fernando (2017-09-06 11:58 UTC)

<p>Hi all,</p>
<p>FYI and to follow up, I’ve kept updating the cask:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/Homebrew/homebrew-cask-versions/commits/3502f8019d86b0e3284ee0e170eac48c8a49266e/Casks/slicer-nightly.rb" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/1503512?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/Homebrew/homebrew-cask-versions/commits/3502f8019d86b0e3284ee0e170eac48c8a49266e/Casks/slicer-nightly.rb" target="_blank" rel="nofollow noopener">Homebrew/homebrew-cask-versions</a></h3>

<p>🔢 Alternate versions of Casks. Contribute to Homebrew/homebrew-cask-versions development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The Lab in the Slicer wiki is also updated with explanations and instructions:<br>
<a href="https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask</a></p>

---

## Post #17 by @jcfr (2017-09-06 12:47 UTC)

<p>Thanks for the update.</p>
<p>Homebrew and caskrepair have just been installed on <code>factory.kitware</code>. Summary <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory/HomeBrewInstall">here</a></p>
<p>We now need an automated way to generate the following command:</p>
<pre><code class="lang-auto">cask-repair --cask-version 4.7.0.26273,676538 --fail-on-error --blind-submit slicer-nightly
</code></pre>
<p>While <code>4.7.0</code> and <code>26273</code> respectively correspond to the major.minor.patch version and the SVN revision (and I should be able to write a small script getting that info from either <a href="http://slicer.kitware.com">slicer.kitware.com</a>  or <a href="http://download.slicer.org">download.slicer.org</a>). What is the value <code>676538</code> ?</p>

---

## Post #18 by @Fernando (2017-09-06 12:50 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>. I don’t know what it means, hoped you could answer. It’s the number at the end of the download URL, e.g. <a href="http://download.slicer.org/bitstream/684799" rel="nofollow noopener">http://download.slicer.org/bitstream/684799</a></p>

---

## Post #19 by @jcfr (2017-09-06 13:24 UTC)

<p>Great. That was the missing information. It corresponds to the database identifier allowing to retrieve the item.</p>
<p>For example, given the latest nightly, here are two ways to download the package:</p>
<ul>
<li>by bitstreamId: <code>http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;id=684799</code>
</li>
<li>by checksum: <code>http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=5010fdd6d2a960e87280b4e867dd99ad</code>
</li>
</ul>
<p>All of that said, here is the command that will be executed every morning:</p>
<pre><code class="lang-auto">$ curl --progress-bar "http://download.slicer.org/find?os=macosx&amp;stability=any" -o /tmp/latest &amp;&amp; \
version=$(cat /tmp/latest | python -c 'import sys, json; print(json.load(sys.stdin)["version"])') &amp;&amp; \
revision=$(cat /tmp/latest | python -c 'import sys, json; print(json.load(sys.stdin)["revision"])') &amp;&amp; \
bitstream_id=$(cat /tmp/latest | python -c 'import sys, json; print(json.load(sys.stdin)["download_url"])' | cut -d"/" -f3) &amp;&amp; \
echo "cask-repair --cask-version $version.$revision,$bitstream_id --fail-on-error --blind-submit slicer-nightly"

######################################################################## 100.0%
cask-repair --cask-version 4.7.0.26338,684799 --fail-on-error --blind-submit slicer-nightly



</code></pre>

---

## Post #20 by @Fernando (2017-09-06 17:40 UTC)

<p>Great, I’ll stop updating the cask. Will the script be run immediately after binaries are ready to be downloaded?</p>

---

## Post #21 by @jcfr (2017-09-06 17:43 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="20" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Will the script be run immediately after binaries are ready to be downloaded?</p>
</blockquote>
</aside>
<p>Since the script will run from a different machine, at first I will have it run at 8am EST. Is that too late ? Would you prefer to have the package as soon as it is available ?</p>

---

## Post #22 by @Fernando (2017-09-06 17:54 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="21" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Would you prefer to have the package as soon as it is available ?</p>
</blockquote>
</aside>
<p>That would be optimal, but I don’t think it’s critical.</p>
<p>I was planning to cron a script that constantly (like every half hour) whether the latest version corresponds to the current cask and repair it if needed. I guess something like that would do the trick.</p>

---

## Post #23 by @jcfr (2017-09-06 18:27 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="22" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>I was planning to cron a script that constantly (like every half hour) whether the latest version corresponds to the current cask and repair it if needed. I guess something like that would do the trick.</p>
</blockquote>
</aside>
<p>We still need to have a more robust error checking, but the bulk of it is here:</p>
<pre><code class="lang-auto"># Get revision associated with the last successful caskrepair
last_revision=$(curl -# "https://raw.githubusercontent.com/caskroom/homebrew-versions/master/Casks/slicer-nightly.rb" | grep -e "^\s*version" | cut -d"," -f1 | cut -d"." -f4)

[[ -z $last_revision ]] &amp;&amp; echo "Failed to extract revision from slicer-nightly.rb" &amp;&amp; exit 1

# Get revision associated with the last macosx package
package_info=$(curl --progress-bar "http://download.slicer.org/find?os=macosx&amp;stability=any")

version=$(echo $package_info | python -c 'import sys, json; print(json.load(sys.stdin)["version"])') &amp;&amp; \
revision=$(echo $package_info | python -c 'import sys, json; print(json.load(sys.stdin)["revision"])') &amp;&amp; \
bitstream_id=$(echo $package_info | python -c 'import sys, json; print(json.load(sys.stdin)["download_url"])' | cut -d"/" -f3)

[[ -z $revision ]] &amp;&amp; echo "Failed to extract revision from Slicer package info" &amp;&amp; exit 1

# If both revision match, we are all set
if [[ $last_revision ==  $revision ]]; then
  exit 0
fi

cask-repair --cask-version $version.$revision,$bitstream_id --fail-on-error --blind-submit slicer-nightly
</code></pre>

---

## Post #24 by @Fernando (2017-09-06 18:45 UTC)

<p>Yes, that looks good. However, I think we also need to check whether a PR has already been sent with a call to <code>cask-repair</code>. Otherwise it will continue to create PRs until the first is accepted. What about keeping a local copy with info about the last repair?</p>
<pre><code class="lang-auto"># Get revision associated with the last requested update
revision_path="/tmp/slicer-version.txt"
last_requested_revision=`cat $revision_path`

[[ -z $last_requested_revision ]] &amp;&amp; echo "Failed to extract revision from $revision_path" &amp;&amp; exit 1

# Get revision associated with the last macosx package
package_info=$(curl --progress-bar "http://download.slicer.org/find?os=macosx&amp;stability=any")

version=$(echo $package_info | python -c 'import sys, json; print(json.load(sys.stdin)["version"])') &amp;&amp; \
revision=$(echo $package_info | python -c 'import sys, json; print(json.load(sys.stdin)["revision"])') &amp;&amp; \
bitstream_id=$(echo $package_info | python -c 'import sys, json; print(json.load(sys.stdin)["download_url"])' | cut -d"/" -f3)

[[ -z $revision ]] &amp;&amp; echo "Failed to extract revision from Slicer package info" &amp;&amp; exit 1

# If both revision match, we are all set
if [[ $last_requested_revision ==  $revision ]]; then
  exit 0
fi

cask-repair --cask-version $version.$revision,$bitstream_id --fail-on-error --blind-submit slicer-nightly

echo $revision &gt; $revision_path
</code></pre>
<p>P.S.: sometimes the bitstream ID changes and not the revision number. Why is that?</p>

---

## Post #25 by @jcfr (2017-09-06 20:03 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="24" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>What about keeping a local copy with info about the last repair?</p>
</blockquote>
</aside>
<p>Yeahh. That was I did first … but wanted to have something with no state stored in local file. That will definitively work.</p>
<blockquote>
<p>will continue to create PRs until the first is accepted.</p>
</blockquote>
<p>Makes sense</p>
<blockquote>
<p>sometimes the bitstream ID changes and not the revision number. Why is that?</p>
</blockquote>
<p>If between Day 1 and Day 2 there is no commit done, we still build the package and upload it. Then, you will have the same revision but different id.</p>

---

## Post #26 by @lassoan (2017-09-06 22:46 UTC)

<p>I would recommend to not update the package immediately when the core installer is ready because by that time extensions are not available yet. Something like 8am Eastern time should work.</p>

---

## Post #27 by @Fernando (2017-09-28 10:11 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="24" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>However, I think we also need to check whether a PR has already been sent with a call to cask-repair. Otherwise it will continue to create PRs until the first is accepted.</p>
</blockquote>
</aside>
<p>Actually, a PR won’t be created if there’s also one pending, the command will just fail. So I guess the script can be safely run daily without the local copy of the last submitted version.</p>

---

## Post #28 by @Fernando (2018-06-19 12:39 UTC)

<p>I keep updating the cask from time to time, but still think it could be done automatically every day: <a href="https://discourse.slicer.org/t/slicer-installation-on-mac-using-homebrew/933/24?u=fernando">Slicer installation on Mac using homebrew</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think?</p>

---

## Post #29 by @Fernando (2019-06-24 15:20 UTC)

<p>I might be the only person in the world updating Slicer with brew, but in case someone else is interested, I  just submitted a PR so that the cask for the nightly version doesn’t need to be updated every day: <a href="https://github.com/Homebrew/homebrew-cask-versions/pull/7538" rel="nofollow noopener">https://github.com/Homebrew/homebrew-cask-versions/pull/7538</a></p>

---

## Post #30 by @Alex_Vergara (2019-06-25 06:55 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="29" data-topic="933">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>I might be the only person in the world updating Slicer with brew</p>
</blockquote>
</aside>
<p>You are not the only one</p>

---

## Post #31 by @Fernando (2019-08-01 14:19 UTC)

<p>FYI Slicer nightly <code>slicer-nightly</code> can be installed by running:</p>
<pre><code class="lang-auto">brew cask install slicer-nightly
</code></pre>
<p>and upgraded:</p>
<pre><code class="lang-auto">brew cask upgrade slicer-nightly
</code></pre>

---

## Post #32 by @Alex_Vergara (2019-08-22 07:13 UTC)

<p>In the last upgrade I have obtained:</p>
<pre><code class="lang-bash">==&gt; Installing Cask slicer-nightly
==&gt; Purging files for version latest of Cask slicer-nightly
Error: No such file or directory @ rb_sysopen - /usr/local/Caskroom/slicer-nightly/.metadata/latest.upgrading/20190806090848.651/Casks/slicer-nightly.rb
Follow the instructions here:
  https://github.com/Homebrew/homebrew-cask#reporting-bugs
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:1393:in `initialize'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:1393:in `open'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:1393:in `copy_file'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:487:in `copy_file'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:404:in `block in cp'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:1572:in `block in fu_each_src_dest'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:1586:in `fu_each_src_dest0'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:1570:in `fu_each_src_dest'
/System/Library/Frameworks/Ruby.framework/Versions/2.3/usr/lib/ruby/2.3.0/fileutils.rb:403:in `cp'
/usr/local/Homebrew/Library/Homebrew/cask/installer.rb:388:in `save_caskfile'
/usr/local/Homebrew/Library/Homebrew/cask/installer.rb:78:in `stage'
/usr/local/Homebrew/Library/Homebrew/cask/installer.rb:99:in `install'
/usr/local/Homebrew/Library/Homebrew/cask/installer.rb:126:in `reinstall'
/usr/local/Homebrew/Library/Homebrew/cask/cmd/reinstall.rb:13:in `block in run'
/usr/local/Homebrew/Library/Homebrew/cask/cmd/reinstall.rb:7:in `each'
/usr/local/Homebrew/Library/Homebrew/cask/cmd/reinstall.rb:7:in `run'
/usr/local/Homebrew/Library/Homebrew/cask/cmd/abstract_command.rb:36:in `run'
/usr/local/Homebrew/Library/Homebrew/cask/cmd.rb:93:in `run_command'
/usr/local/Homebrew/Library/Homebrew/cask/cmd.rb:159:in `run'
/usr/local/Homebrew/Library/Homebrew/cask/cmd.rb:124:in `run'
/usr/local/Homebrew/Library/Homebrew/cmd/cask.rb:9:in `cask'
/usr/local/Homebrew/Library/Homebrew/brew.rb:102:in `&lt;main&gt;'
</code></pre>
<p>Now slicer nightly is broken, it used to work really fine until last week!</p>

---

## Post #33 by @Fernando (2019-08-24 11:02 UTC)

<p>Hi Alex,</p>
<p>It works for me. If you still have problems, you can create an issue on the <a href="https://github.com/homebrew/homebrew-cask" rel="nofollow noopener"><code>homebrew-cask</code> repo</a>.</p>

---

## Post #34 by @Fernando (2020-10-09 17:55 UTC)

<p>PR to update the cask submitted: <a href="https://github.com/Homebrew/homebrew-cask/pull/90632" rel="noopener nofollow ugc">https://github.com/Homebrew/homebrew-cask/pull/90632</a></p>

---

## Post #35 by @Fernando (2020-10-12 22:40 UTC)

<p>PR to update the name of the cask for the <s>nightly</s> preview version: <a href="https://github.com/Homebrew/homebrew-cask-versions/pull/9751" rel="noopener nofollow ugc">https://github.com/Homebrew/homebrew-cask-versions/pull/9751</a></p>
<p>Documentation updated: <a href="https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask</a></p>

---
