# Building Slicer behind a firewall

**Topic ID**: 385
**Date**: 2017-05-25
**URL**: https://discourse.slicer.org/t/building-slicer-behind-a-firewall/385

---

## Post #1 by @muratmaga (2017-05-25 16:08 UTC)

<p>Hi,<br>
I am trying to build Slicer from the source. I have a centos 7.3 VM at home, and instructions things worked out well until the point it ran out of space during the superbuild of ITK.<br>
Right now I am repeating the tasks on my work computer, and I am getting this error at the git svn rebase step:</p>
<p>URL access forbidden for unknown reason: Unable to connect to a repository at URL ‘<a href="http://svn.slicer.org/Slicer4/trunk" rel="nofollow noopener">http://svn.slicer.org/Slicer4/trunk</a>’: Access to ‘<a href="http://svn.slicer.org/Slicer4/trunk" rel="nofollow noopener">http://svn.slicer.org/Slicer4/trunk</a>’ forbidden at /usr/share/perl5/vendor_perl/Git/SVN.pm line 717.</p>
<p>which likely related to the proxy and firewall settings at work (didn’t have the issue at home). Is there an alternative way to do this?</p>

---

## Post #2 by @pieper (2017-05-25 16:21 UTC)

<p>You can skip the svn steps - those are only needed for people with commit access to svn.  I’ll update the wiki to clarify.</p>
<p>If you do want to contribute fixes to the Slicer source tree you can do it with you a github pull request.</p>

---

## Post #3 by @muratmaga (2017-05-25 18:30 UTC)

<p>Thank Steve.</p>
<p>But now I am stuck with this error, which I think is real.<br>
[ 40%] Performing download step (git clone) for 'DCMTK’<br>
Cloning into ‘DCMTK’…<br>
fatal: repository ‘<a href="http://git.dcmtk.org/dcmtk/" rel="nofollow noopener">http://git.dcmtk.org/dcmtk/</a>’ not found<br>
Cloning into ‘DCMTK’…<br>
fatal: repository ‘<a href="http://git.dcmtk.org/dcmtk/" rel="nofollow noopener">http://git.dcmtk.org/dcmtk/</a>’ not found<br>
Cloning into ‘DCMTK’…<br>
fatal: repository ‘<a href="http://git.dcmtk.org/dcmtk/" rel="nofollow noopener">http://git.dcmtk.org/dcmtk/</a>’ not found<br>
– Had to git clone more than once:<br>
3 times.<br>
CMake Error at DCMTK-prefix/tmp/DCMTK-gitclone.cmake:56 (message):<br>
Failed to clone repository: ‘<a href="http://git.dcmtk.org/dcmtk" rel="nofollow noopener">http://git.dcmtk.org/dcmtk</a>’</p>
<p>when I type git clone <a href="http://git.dcmtk.org/dcmtk" rel="nofollow noopener">http://git.dcmtk.org/dcmtk</a> on command line I get the same repository not found error.</p>

---

## Post #4 by @muratmaga (2017-05-25 18:56 UTC)

<p>So, it has something with using http instead of git. At home, where there is no proxy, it worked with git protocol.<br>
At work, where I used the Slicer_USE_GIT_PROTOCOL=OFF, it fails.</p>

---

## Post #5 by @pieper (2017-05-25 18:57 UTC)

<p>Yes, I was just about to suggest that.  Looks like <a href="http://git.dcmtk.org">git.dcmtk.org</a> only support git protocol and not http.</p>
<p>I don’t use a proxy so I don’t really have a suggestion on that.</p>

---

## Post #6 by @lassoan (2017-05-25 22:32 UTC)

<p>There was some error with the DCMTK repository (I had a build failure on my computer because of that, too). It got fixed later. If you still have problems then you may use an unofficial mirror on github, for example: <a href="https://github.com/commontk/DCMTK">https://github.com/commontk/DCMTK</a></p>

---

## Post #7 by @jcfr (2017-05-25 23:45 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="385">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you still have problems then you may use an unofficial mirror on github, for example: <a href="https://github.com/commontk/DCMTK" class="inline-onebox">GitHub - commontk/DCMTK: WARNING: This is NOT the official upstream DCMTK git repository.</a></p>
</blockquote>
</aside>
<p>Let us know so that we can update the fork. Currently the authoritative source for DCMTK is <a href="http://git.dcmtk.org/dcmtk">git.dcmtk.org/dcmtk</a></p>

---

## Post #8 by @muratmaga (2017-05-25 23:46 UTC)

<p>Thanks Andras, I will try that. I also asked our network folks to open up the git port on the firewall. You never know, they may agree.</p>
<p>I am toggling the USE_ANTS to on via the ccmake, but after configuring it goes to back to off. How can I enable ANTs support for Slicer?</p>

---

## Post #9 by @lassoan (2017-05-26 02:29 UTC)

<p>Update Slicer\SuperBuild.cmake: change USE_ANTS:BOOL=OFF to USE_ANTS:BOOL=ON.</p>

---

## Post #10 by @muratmaga (2017-05-26 06:36 UTC)

<p>That change indeed made ccmake to configure and generate with ANTs on, but when I type make, I get the error<br>
ANTS_SOURCE_DIR=’’ does not exist, and build fails.</p>
<p>From the message it is not clear to me whether it is asking the git repo to clone, or asking for existing local installation of ANTs.</p>
<p>As far as I can tell, SuperBuild.cmake does not contain any entry for ANTs repository.</p>

---

## Post #11 by @lassoan (2017-05-26 11:28 UTC)

<p>Probably you have to download Ants and add a CMake variable ANTS_SOURCE_DIR:PATH=…</p>

---

## Post #12 by @muratmaga (2017-05-26 15:15 UTC)

<p>Thanks Andras.<br>
I was thinking ANTs would become the part of the superbuild and will be downloaded. But it doesn’t matter as I already have the source.<br>
I am not familiar with CMake variable syntax.<br>
Would ANTS_SOURCE_DIR:PATH=/some/path<br>
suffice and do I add this to SuperBuild.cmake?</p>

---

## Post #13 by @lassoan (2017-05-26 15:29 UTC)

<p>For initial testing, you can add ANTS_SOURCE_DIR:PATH=/some/path directly into your SuperBuild.cmake (below USE_ANTS:BOOL=ON).</p>
<p>An alternative to using Ants through BrainsFit is to use it directly, similarly how I’ve added Elastix (similar ITK-based registration framework). See <a href="https://github.com/lassoan/SlicerElastix">https://github.com/lassoan/SlicerElastix</a> for details. The advantage of this approach is that you don’t need to modify anything in the Slicer core to make it work.</p>

---

## Post #14 by @muratmaga (2017-05-26 15:51 UTC)

<p>Hi Andras,</p>
<p>I have an ANTs specific workflow that I wanted to test within Slicer. I did exactly what you suggested, and this time I got a different error giving the same message ANTs_LIBRARY_DIR. While I can try to enter this to superbuid cmake the same way,  am not sure what this should point to, because that’s not a variable I needed to set when I I built ANTs.</p>
<p>Also, on a different note, I tested the scissors tool with limits and works wonderfully. Thank you again!</p>

---

## Post #15 by @lassoan (2017-05-26 15:59 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="385">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I have an ANTs specific workflow that I wanted to test within Slicer.</p>
</blockquote>
</aside>
<p>In that case the easiest is to just write a Python wrapper around your executable - very similar to the <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py">Elastix Python wrapper</a>. You don’t need to make Slicer build ANTs for you.</p>

---
