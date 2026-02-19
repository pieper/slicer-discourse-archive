---
topic_id: 811
title: "Add Slicer Nightly To Homebrew Macos"
date: 2017-08-02
url: https://discourse.slicer.org/t/811
---

# Add Slicer Nightly to Homebrew (macOS)

**Topic ID**: 811
**Date**: 2017-08-02
**URL**: https://discourse.slicer.org/t/add-slicer-nightly-to-homebrew-macos/811

---

## Post #1 by @Fernando (2017-08-02 19:43 UTC)

<p>Hi all,</p>
<p>I am doing a fresh install of my OS and realized how powerful <code>brew</code> is. I checked whether I could install Slicer with it and discovered that only the <a href="https://github.com/caskroom/homebrew-cask/blob/d6da1a7be2ca37a53950ac7904ffb66b7facffef/Casks/slicer.rb" rel="nofollow noopener">stable version is available</a>:</p>
<pre><code class="lang-auto">brew cask install slicer
</code></pre>
<p>I thought it would be convenient to be able to install the nightly build, so I took the liberty to submit a <a href="https://github.com/caskroom/homebrew-versions/pull/4225" rel="nofollow noopener">PR</a> to <a href="https://github.com/caskroom/homebrew-versions" rel="nofollow noopener">homebrew-versions</a>. I hope you’re ok with that. If it’s accepted, one could install the official nightly version on macOS by doing:</p>
<pre><code class="lang-auto">brew cask install slicer-nightly
</code></pre>
<p>This is the comitted <code>cask</code>:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/fepegar/homebrew-versions/blob/c4a9537fdfa72081507ce4d56bed3c08c644844f/Casks/slicer-nightly.rb" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/fepegar/homebrew-versions/blob/c4a9537fdfa72081507ce4d56bed3c08c644844f/Casks/slicer-nightly.rb" target="_blank" rel="nofollow noopener">fepegar/homebrew-versions/blob/c4a9537fdfa72081507ce4d56bed3c08c644844f/Casks/slicer-nightly.rb</a></h4>
<pre><code class="lang-rb">cask 'slicer-nightly' do
  version '4.7.0.26186,672116'
  sha256 '41d50f7531bef1b759101f97ca1295d2f332133e8e06419e8d285d89552ee6d7'

  # slicer.kitware.com/midas3 was verified as official when first introduced to the cask
  url "http://slicer.kitware.com/midas3/download?bitstream=#{version.after_comma}"
  name '3D Slicer Nightly'
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
<p>It would need to be <a href="https://github.com/caskroom/homebrew-cask/blob/master/CONTRIBUTING.md#updating-a-cask" rel="nofollow noopener">updated</a> often. I can do it for some time, but I guess the right thing would be that someone from the core set a periodic <a href="https://github.com/vitorgalvao/tiny-scripts/blob/master/cask-repair" rel="nofollow noopener">script</a> to update it everyday. It needs just the version (like <code>4.7.0.26186,672116</code>) and an URL as parameters.</p>
<p>Please let me know what you think.</p>
<p>Best,<br>
Fernando</p>

---

## Post #2 by @jcfr (2017-08-02 20:01 UTC)

<p>Hi <a class="mention" href="/u/fernando">@Fernando</a></p>
<p>Thanks for working on this <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=5" title=":+1:" class="emoji" alt=":+1:"></p>
<p>As I have no experience with brew, do you have an example command line invocation of <a href="https://github.com/vitorgalvao/tiny-scripts/blob/master/cask-repair">cask-repair</a> ?</p>
<p>Would the following work:</p>
<pre><code class="lang-auto">curl -L https://raw.githubusercontent.com/vitorgalvao/tiny-scripts/master/cask-repair -o cash-repair.sh &amp;&amp; \
chmod u+x cash-repair.sh &amp;&amp; \ 
./cash-repair.sh --fail-on-error --cask-url XXX --cask-version 4.7.0.26186,672116  slicer
</code></pre>
<p>What should the parameter for <code>cask-url</code> and <code>cask-version</code> ?</p>

---

## Post #3 by @Fernando (2017-08-02 20:30 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>I learnt about all this stuff yesterday. I think something like that would work (replacing <code>slicer</code> by <code>slicer-nightly</code>). My idea is, once my PR is accepted, I can try those lines, make the necessary modifications, and once it seems like it’s working I’ll confirm the procedure in this thread.</p>
<p>Btw, the script doesn’t need to manually downloaded. It can be installed using <code>brew</code>:</p>
<pre><code class="lang-bash">brew install vitorgalvao/tiny-scripts/cask-repair
cask-repair --fail-on-error --cask-url XXX --cask-version 4.7.0.26186,672116 slicer-nightly
</code></pre>
<p>I’m not sure if the URL can be given as a function of the version, as in the cask code.</p>

---

## Post #4 by @jcfr (2017-08-02 20:48 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>like it’s working I’ll confirm the procedure in this thread.</p>
</blockquote>
</aside>
<p>Sounds like a plan. Thanks <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>doesn’t need to manually downloaded. It can be installed using brew</p>
</blockquote>
</aside>
<p>Thanks for the the note. (For the record, I naively downloaded the script on linux … but realized soon enough brew executable was required)</p>
<aside class="quote no-group" data-username="Fernando" data-post="3" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>URL can be given as a function of the version</p>
</blockquote>
</aside>
<p>I have no idea. Keep us posted of your findings <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @Fernando (2017-08-03 10:18 UTC)

<p>This is the line for today (10 am UTC):</p>
<pre><code class="lang-bash">cask-repair --cask-version 4.7.0.26187,673138 slicer-nightly
</code></pre>
<p>The tool is clever enough to figure out the URL from the version and it automatically computes the SHA256. Also it created this <a href="https://github.com/caskroom/homebrew-versions/pull/4232" rel="nofollow noopener">pull request</a>. Not bad.</p>
<p>Before running that line I had to go through the classic process of <a href="https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/" rel="nofollow noopener">adding an ssh key to my computer and GitHub</a>.</p>
<p>So one can now officially download and install 3D Slicer (and nightly) with <code>brew</code>. Shall we write something in the Announcements category? The wiki?</p>
<p>Do you think the above line could be run after each macOS build?</p>

---

## Post #6 by @pieper (2017-08-03 12:08 UTC)

<p>This is cool Fernando <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=5" title=":ok_hand:" class="emoji" alt=":ok_hand:"></p>
<p>But what is the right install line?</p>
<p>I updated brew and but I get this:</p>
<pre><code class="lang-auto">$ brew cask install slicer-nightly
Error: Cask 'slicer-nightly' is unavailable: No Cask with this name exists.
Error: Install incomplete.
</code></pre>
<p>The same line works for regular slicer.</p>

---

## Post #7 by @Fernando (2017-08-03 12:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But what is the right install line?</p>
</blockquote>
</aside>
<p>I think you need to tell <code>brew</code> to look also in <a href="https://github.com/caskroom/homebrew-versions" rel="noopener nofollow ugc"><code>homebrew-versions</code></a>. So, to configure:</p>
<ol>
<li>Install <code>homebrew</code> (I think this will install <code>cask</code> too)</li>
</ol>
<pre><code class="lang-auto">/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
</code></pre>
<ol start="2">
<li>Install <code>homebrew-versions</code>:</li>
</ol>
<pre><code class="lang-auto">brew tap caskroom/versions
</code></pre>
<p>To install the first time:</p>
<pre><code class="lang-auto">brew cask install slicer-nightly
</code></pre>
<p>If you want to easily upgrade, you can install <a href="https://github.com/buo/homebrew-cask-upgrade" rel="noopener nofollow ugc"><code>cask-upgrade</code></a>:</p>
<pre><code class="lang-auto">brew tap buo/cask-upgrade
</code></pre>
<p>And each time you want to upgrade:</p>
<pre><code class="lang-auto">brew update
brew cu slicer-nightly
</code></pre>
<p>I think that these are more or less the steps that can be in the wiki / announcements.</p>

---

## Post #8 by @pieper (2017-08-03 13:32 UTC)

<p>Nice!  Yes, step 2, adding the caskroom/versions is what I needed.</p>

---

## Post #9 by @fedorov (2017-08-03 13:37 UTC)

<p>Just curious - does Homebrew provide any statistics about package installs?</p>

---

## Post #10 by @pieper (2017-08-03 13:55 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="811" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Just curious - does Homebrew provide any statistics about package installs?</p>
</blockquote>
</aside>
<p>The homebrew script downloads from midas, so our regular statistics will be updated by these installs.</p>

---

## Post #11 by @hjmjohnson (2017-08-04 20:55 UTC)

<p>Installing QT 4.8.7 with homebrew on mac 10.12:</p>
<ul>
<li>brew tap cartr/qt4</li>
<li>brew tap-pin cartr/qt4</li>
<li>brew install qt@4</li>
<li>brew install qt-webkit@2.3</li>
</ul>
<p>It would be nice to add these instructions to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Mac_2" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Mac_2</a></p>
<p>Hans</p>

---

## Post #12 by @pieper (2017-08-04 23:40 UTC)

<p>Thanks <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> - added:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Mac_with_Homebrew" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt#Mac_with_Homebrew</a></p>

---

## Post #13 by @Fernando (2017-08-05 12:44 UTC)

<p>So, shall we discuss:</p>
<ol>
<li>Cron script to update the cask after each mac build</li>
<li>Add the info to the wiki</li>
<li>Announce this in the forum</li>
</ol>

---

## Post #14 by @Fernando (2017-08-10 22:18 UTC)

<p>Just updated the cask:</p>
<pre><code class="lang-auto">cask-repair --cask-version 4.7.0.26221,675049 slicer-nightly
</code></pre>

---

## Post #15 by @Fernando (2017-08-15 18:34 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="13" data-topic="811" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>So, shall we discuss:</p>
<ol>
<li>Cron script to update the cask after each mac build</li>
<li>Add the info to the wiki</li>
<li>Announce this in the forum</li>
</ol>
</blockquote>
</aside>
<p>Hi all,</p>
<p>I’m still not sure whether you think it’s useful to add this info to the wiki and/or the forum. Could you please give me some feedback?</p>
<p>I’ve kept updating the cask and it works very well. It’s nice to update Slicer with just one command.</p>
<p>Thanks</p>

---

## Post #16 by @jcfr (2017-08-15 18:46 UTC)

<p>Hi Fernando,</p>
<p>Thanks for the reminder. I have been busy upgrading the infrastructure to work with Qt5 and VTK8 and didn’t have a chance to look further into this.</p>
<p>To move forward, it would be ideal to share few scripts consolidating all valuable information shared here.</p>
<p>For example:</p>
<ul>
<li>script 1: <code>slicer-homebrew-setuptenv.sh</code>  # This would allow to install the required homebrew environment</li>
<li>script 2: <code>slicer-homebrew-update.sh</code>      # This script allowing to download the latest package, repackage and publish the PR for the cask, etc …</li>
</ul>
<p>Last, since we all agree moving forward with this make sense <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"> (Thanks <a class="mention" href="/u/fernando">@Fernando</a> for your patience and help), could you add the content of these scripts as well as few additional info on this wiki page:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Labs/HomebrewCask</a></p>
<p>After we have the draft scripts ready and tested for few days, we will find them a home (e.g <code>Slicer/Utilities/Scripts</code>).</p>

---

## Post #17 by @Fernando (2017-08-15 19:34 UTC)

<p>Alright! Those scripts would be run by you, right? I mean, we’re talking first about what you guys need to do to keep the cask updated and then we can publish the info needed by the users?</p>

---

## Post #18 by @jcfr (2017-08-15 19:50 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="17" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>Those scripts would be run by you, right?</p>
</blockquote>
</aside>
<p>The script will be run automatically on a nightly basis from the macOS machine hosted at Kitware that is already generating the MacOSX installer.</p>
<aside class="quote no-group" data-username="Fernando" data-post="17" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>what you guys need to do to keep the cask updated</p>
</blockquote>
</aside>
<p>Hopefully, running the scripts (with one or two arguments) is all that is needed.</p>
<aside class="quote no-group" data-username="Fernando" data-post="17" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>then we can publish the info needed by the users?</p>
</blockquote>
</aside>
<p>The info (on the wiki to begin) will be high level documentation describing what is homebrew, when and how the cask are generated/updated/…</p>
<p>In this case, the users are Slicer maintainers or anyone who would like to run the scripts of their own</p>

---

## Post #19 by @Fernando (2017-08-15 19:53 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="18" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>the macOS machine hosted at Kitware</p>
</blockquote>
</aside>
<p>Sure, that is what I meant by “you” <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="jcfr" data-post="18" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>In this case, the users are Slicer maintainers</p>
</blockquote>
</aside>
<p>Ok, but we’re doing this so that the end users can upgrade Slicer easily, right? Shall we write the instructions to the wiki page?</p>

---

## Post #20 by @jcfr (2017-08-15 21:39 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="19" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>we’re doing this so that the end users can upgrade Slicer easily, right? Shall we write the instructions to the wiki page?</p>
</blockquote>
</aside>
<p>Indeed.</p>
<p>Instructions would be great. That said, they should be fairly minimum as all the steps would be captured in the scripts.</p>
<p>Ideally, running the setupenv script, and then running the update script should be the only things needed</p>

---

## Post #21 by @Fernando (2017-08-15 21:47 UTC)

<p>I think I’m missing something. In my head there are actually four scripts:</p>
<ul>
<li>
<p>Slicer maintainers</p>
<ol>
<li>Setup = install brew + install cask-upgrade</li>
<li>Update = send PR with new version</li>
</ol>
</li>
<li>
<p>Slicer users</p>
<ol>
<li>Setup = install brew and other stuff + Slicer Nightly</li>
<li>Update = download and install nightly version of Slicer</li>
</ol>
</li>
</ul>
<p>I’m working of the maintainers part, I don’t know if the users side should be also added to the wiki.</p>

---

## Post #22 by @Fernando (2017-08-15 22:01 UTC)

<p>I created a first version of the page, feel free to edit!</p>

---

## Post #23 by @jcfr (2017-08-15 22:01 UTC)

<p>Thanks clarifying.</p>
<blockquote>
<p>I’m working of the maintainers part</p>
</blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>the users side should be also added to the wiki.</p>
</blockquote>
<p>We could probably add the info on <a href="http://download.slicer.org">download.slicer.org</a></p>

---

## Post #24 by @Fernando (2017-08-15 22:04 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="23" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>We could probably add the info on <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a></p>
</blockquote>
</aside>
<p>I hope you can figure out that part from the users steps I wrote on the wiki.</p>
<p>Thanks for the feedback and help <a class="mention" href="/u/jcfr">@jcfr</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #25 by @jcfr (2017-08-15 22:05 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="22" data-topic="811" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>I created a first version of the page, feel free to edit!</p>
</blockquote>
</aside>
<p>Well done. I will give a try tonight or tomorrow.</p>
<p>Is it possible to install homebrew in a specific folder  (e.g <code>/Volumes/Dashboards/Support/Homebrew</code>) so that it doesn’t “pollute” the PATH and does not install anything in folder like <code>/usr</code>, <code>/usr/lib</code>, … ?</p>

---

## Post #26 by @Fernando (2017-08-15 22:20 UTC)

<p><code>brew</code> doesn’t <code>sudo</code>, I think it installs stuff in its own libraries directory. There are some good answers for that here:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://docs.brew.sh/assets/img/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://docs.brew.sh/FAQ.html" target="_blank" rel="nofollow noopener">Homebrew Documentation</a>
  </header>
  <article class="onebox-body">
    <img src="https://docs.brew.sh/assets/img/homebrew-256x256.png" class="thumbnail onebox-avatar" width="256" height="256">

<h3><a href="https://docs.brew.sh/FAQ.html" target="_blank" rel="nofollow noopener">FAQ</a></h3>

<p>Documentation for the missing package manager for macOS.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I’m sorry I can’t help you much more about that topic, I’m still very new about this.</p>

---

## Post #27 by @fedorov (2017-08-23 21:43 UTC)

<p>For those interested, see related discussion in <a href="https://discourse.slicer.org/t/slicer-installation-on-mac-using-homebrew/933">Slicer installation on Mac using homebrew</a></p>

---

## Post #28 by @wmwf (2017-10-30 12:42 UTC)

<p>“jcfr” Seconded, can we install homebrew in a specific folder? This will very much help to keep things more organized.</p>
<p>Regards<br>
<a href="https://www.weber-financial.com" rel="nofollow noopener">wf</a></p>

---

## Post #29 by @Fernando (2017-10-30 12:57 UTC)

<aside class="quote no-group" data-username="wmwf" data-post="28" data-topic="811">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/aca169/48.png" class="avatar"> wmwf:</div>
<blockquote>
<p>can we install homebrew in a specific folder? This will very much help to keep things more organized.</p>
</blockquote>
</aside>
<p>Please see their comments about that on <a href="https://docs.brew.sh/Installation.html" class="inline-onebox" rel="noopener nofollow ugc">Installation — Homebrew Documentation</a></p>

---

## Post #30 by @KHATRINA (2018-12-20 18:09 UTC)

<p>Thanks for the the note. (For the record, I naively downloaded the script on linux … <a href="https://downloader.vip/itunes/" rel="nofollow noopener">iTunes</a> <a href="https://inro.in/mobdro/" rel="nofollow noopener">Mobdro</a><a href="https://inro.in/tutuapp/" rel="nofollow noopener">TutuApp</a>but realized soon enough brew executable was required)</p>
<p><img src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/40/25_1.png" alt width="20" height="20"> Fernando:</p>

---

## Post #31 by @Fernando (2018-12-20 19:23 UTC)

<p>I use this script to update Slicer automatically on Linux. You might find it interesting.</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/fepegar/f49c5062695562370a76222dada47e47" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/fepegar/f49c5062695562370a76222dada47e47" target="_blank" rel="nofollow noopener">https://gist.github.com/fepegar/f49c5062695562370a76222dada47e47</a></h4>
<h5>updateSlicer.py</h5>
<pre><code class="Python">#!/usr/bin/env python

import os
import re
import sys
from sys import platform as _platform
import glob
import time
import shutil
import urllib</code></pre>
This file has been truncated. <a href="https://gist.github.com/fepegar/f49c5062695562370a76222dada47e47" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
