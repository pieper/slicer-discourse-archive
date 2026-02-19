---
topic_id: 34805
title: "Installing Extension In Users Folder In Linux"
date: 2024-03-10
url: https://discourse.slicer.org/t/34805
---

# Installing extension in user's folder in Linux

**Topic ID**: 34805
**Date**: 2024-03-10
**URL**: https://discourse.slicer.org/t/installing-extension-in-users-folder-in-linux/34805

---

## Post #1 by @muratmaga (2024-03-10 06:51 UTC)

<p>In a project we might need to mount the Slicer installation tree in a read only network share, with the assumption that all user configs and extensions can be installed under user’s own folder, perhaps something like <strong>/home/murat/.slicer/</strong>, including the ini files. We only need this to work on Linux.</p>
<p>Is this possible?</p>

---

## Post #2 by @muratmaga (2024-03-10 07:23 UTC)

<p>While the extension path is configurable and indeed I can set it up to a place like /home/murat/.config/slicer.org/Extensions from preferences, Extension manager seems to want the <a href="http://slicer.org/Slicer-XXXXX.ini">slicer.org/Slicer-XXXXX.ini</a> under the installation tree to be writable.</p>
<p>Is there an alternative?</p>
<p>Also what about the user/extension install python libraries? I didn’t see a configuration for that. Do all go to the site-packages folder under the installation tree?</p>

---

## Post #3 by @pieper (2024-03-10 16:44 UTC)

<p>It’s not set up for that.  Better to either pre-install all extensions in the read-only directory or give each user their own copy of Slicer to install extensions in.</p>

---

## Post #4 by @muratmaga (2024-03-10 19:22 UTC)

<p>Understood. Is this somewhere on the roadmap?</p>
<p>It would facilitate easier deployment of Slicer on centrally managed institutional servers and HPC type systems (all Linux based).</p>

---

## Post #5 by @pieper (2024-03-10 19:56 UTC)

<p>I remember we had looked into it at one point and the sticking issue as I recall is the python package folders, where different extensions can install different packages.  Probably it’s possible to do something like symlink all the other files and directories to the readonly location and leave some as real directories in the user’s space, but that sounds kind of fragile.  If people are using HPC resources then a couple gig of space for their software doesn’t seem to much to ask, especially for just this one use case where they need user-specific extensions.</p>

---

## Post #6 by @muratmaga (2024-03-10 20:38 UTC)

<p>Thanks. We will keep in mind.</p>
<p>The issue is not about the space. It is about management and update. Centrally managed, closed resource like HPC systems may not even give you as a user external internet access…</p>

---

## Post #7 by @pieper (2024-03-11 00:24 UTC)

<p>Well, in that case you wouldn’t be able to install extensions anyway so installing a read-only shared version of Slicer shouldn’t be a problem.</p>
<p>You can always send <code>--additional-module-paths</code> on the command line to add modules, you just wouldn’t install python packages the normal way.  You could just put them in a place where your custom module knows where import them from (e.g. by adding a path <code>sys.path</code>)</p>
<p>The user-specific config is already in <code>~/.config/slicer.org/Slicer.ini</code>. What else were you concerned about?</p>

---

## Post #8 by @muratmaga (2024-03-11 01:24 UTC)

<p>We are trying to figure out what work, what creates other issues. There is a potential to deploy Slicer  in the our central HPC system.</p>
<p>If we overcome the internet access issue, and let people install Slicer into their home directories, the issue is not the space. There will be a bunch of stale slicer installation. We are not talking about people who would be using Slicer day and out and necessarily be aware they are using a version from two years ago.</p>
<p>I personally preferred a solution, where people do something like</p>
<p><code>module load Slicer</code>,</p>
<p>which brings the latest stable (HPC admins responsibility)<br>
and then the first time they use it they  bookmark their extensions (which are saved in a place <code>~.config/slicer.org/Extensions-XXXXX</code>, or <code>~./config/slicer.org/python-packages</code>, etc). So they will always be using whatever the latest stable version system provides, and if this upgrades than all extensions and packages are automatically repopulated (or that’s roughly the idea).</p>
<p>Anyways, we will do some experiments and report…</p>

---

## Post #9 by @jamesobutler (2024-03-11 02:55 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>which brings the latest stable (HPC admins responsibility)</p>
</blockquote>
</aside>
<p>Is the use of an HOC admin a solution to a more general issue of people not knowing there is a new stable release available and their decision to not update to it? Should there be a focus to improve the Slicer update process to encourage more people to use the latest stable? Would this avoid the need for such a central read-only Slicer solution?</p>

---

## Post #10 by @muratmaga (2024-03-11 05:00 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is the use of an HOC admin a solution to a more general issue of people not knowing there is a new stable release available and their decision to not update to it?</p>
</blockquote>
</aside>
<p>Not just that, admin is required to make Slicer work with their self-signed certificates and network settings. it makes much more sense this is done once for everyone (and checked for every update).</p>
<p>I think we are currently doing a OK job of notifying the stable updates in the software (it might be a bit more prominent then just a text in welcome page). And extension update mechanism works great.</p>

---

## Post #11 by @pieper (2024-03-11 12:18 UTC)

<p>For a similar situation where most users want to use a read-only version of slicer maintained by the admins, we added a slicer directory to everyone’s path that had scripts to launch specific versions with any customizations needed for that system.</p>
<p>E.g. there was a script called <code>slicer522</code> that did this:</p>
<pre><code class="lang-auto">#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &amp;&gt; /dev/null &amp;&amp; pwd )

LD_LIBRARY_PATH=${SCRIPT_DIR}/openssl:${SCRIPT_DIR}/krb5/src/lib:${LD_LIBRARY_PATH} ${SCRIPT_DIR}/Slicer $*
</code></pre>
<p>You could do something similar to point to read-only versions with SlicerMorph installed.</p>
<p>For users like you describe it’s important that they use specific versions so they have consistent behavior - changing the program that appears when they type <code>slicer</code> would add confusion and possibly change their experimental results.</p>
<p>For users who need to install specific extensions they should just be able to copy your customized version into a writable space.</p>
<p>I think you want to minimize the amount of custom development work to support a particular HPC system.  You want users to develop skills that will transfer to other situations.</p>

---

## Post #12 by @RafaelPalomar (2024-03-12 12:23 UTC)

<p>I’ve been facing a similar issue with the Slicer-Flatpak project. I ended up having a couple of patches to enable the extensions and pip-installed python packages land in local folders (i.e., /home/rafael/.local…); as far as I remember the patches were working fine.  <a class="mention" href="/u/muratmaga">@muratmaga</a> If your use-case could be based on a custom-built Slicer, this could be an option and I can help you set it up.</p>
<p>During last project week I was discussing with <a class="mention" href="/u/jcfr">@jcfr</a> on the idea of enabling this behavior in runtime (launcher flag?), but we didn’t concluded on any solution. Something like this could be useful in these scenarios and to wrap the Slicer binaries in a Flatpak, instead of building a custom Slicer. <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a> could something like this make sense?</p>

---

## Post #13 by @lassoan (2024-03-12 12:44 UTC)

<p>What happens when an extension installs a Python package that is already bundled with Slicer (but a different version)? Does the Python package installed in the user folder override the Python package bundled with Slicer core?</p>
<p>If yes then we can add this patch to Slicer core and make it easier to activate this option (right now I think it can only be enabled with a CMake flag at build time). The launcher needs to know about this, so adding a flag to the SlicerLauncherSettings.ini file is a good place to store the flag.</p>

---

## Post #14 by @RafaelPalomar (2024-03-12 12:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What happens when an extension installs a Python package that is already bundled with Slicer (but a different version)? Does the Python package installed in the user folder override the Python package bundled with Slicer core?</p>
</blockquote>
</aside>
<p>I would have to check for a definitive answer on this, but if I remember correctly, the one installed on the user’s folder will take precedence. We might be able to change this behavior, though.</p>
<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If yes then we can add this patch to Slicer core and make it easier to activate this option (right now I think it can only be enabled with a CMake flag at build time). The launcher needs to know about this, so adding a flag to the SlicerLauncherSettings.ini file is a good place to store the flag.</p>
</blockquote>
</aside>
<p>Enabling something like this would enable us to wrap the official Slicer binaries on flatpak and have one more distribution channel. My current implementation of the Slicer-Flatpak is a custom build and still have some ABI compatibility issues with extensions.</p>

---

## Post #15 by @muratmaga (2024-03-12 15:36 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="12" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>If your use-case could be based on a custom-built Slicer, this could be an option and I can help you set it up.</p>
</blockquote>
</aside>
<p>I did not consider the custom build. The issue with custom build we will need to build all the extensions as well. We will discuss these options see which one is going to require the least administrative oversight.</p>
<p>But I think it will be nice to have a solution that allow centrally managed Slicer installation, with options for users to customize.</p>
<p>M</p>

---

## Post #16 by @muratmaga (2024-03-12 15:40 UTC)

<aside class="quote no-group" data-username="pieper" data-post="11" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For users like you describe it’s important that they use specific versions so they have consistent behavior - changing the program that appears when they type <code>slicer</code> would add confusion and possibly change their experimental results.</p>
</blockquote>
</aside>
<p>That’s usually handled by <code>modules</code> module. You can maintain independent versions of the sofware. Whichever one you activate provides the executable you wish.</p>
<p>So, <code>module load slicer</code> may bring the latest stable but you can conitnue to have the previous one through <code>module load slicer-5.4.1</code> (or whatever you want to call). That’s usually how multiple versions of the same software package is maintained in hpc systems.</p>

---

## Post #17 by @jose-d (2024-03-12 15:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="15" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think it will be nice to have a solution that allow centrally managed Slicer installation</p>
</blockquote>
</aside>
<p>I second this. I came to this tread as I automated installation of Slicer using Easybuild (to have <code>module load Slicer</code> ), but quickly realized, that there is no good mechanism how to deal with user-managed extensions with centralized Slicer install.</p>

---

## Post #18 by @jose-d (2024-03-13 11:59 UTC)

<p>I was able to create proof-of-concept based on <code>fuse-overlays</code>.</p>
<p>TL/DR: we create per-user overlay fs on top of read-only baseline install of Slicer.</p>
<p><strong>Proof of concept Setup:</strong></p>
<p>(as <strong>sw repository admin:</strong>  - steps with <code>a.</code> prefix)</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> a.1) Install slicer into shared, read-only directory (in our case Cern VM fs)<br>
<img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> a.2) apply all baseline workarounds (eg. delete <code>libcrypto.so.*</code> )</p>
<p>result: We have working Slicer in <code>/cvmfs/sys.sw.nudz/software/Slicer/5.6.1_bin</code>, but we’re not able install extensions.</p>
<p>(<strong>as system admin</strong>  - steps with <code>b.</code> prefix)</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> b.1)  make sure that <code>fuse-overlayfs</code> is available at compute nodes</p>
<p>proof of concept:</p>
<p>(as <strong>user at compute node</strong> steps with <code>c.</code> prefix)</p>
<p>prepare directories and export them as environment variables:</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> c.1.1): create directory for temporary working data of overlayfs and export it as <code>WORKDIR</code><br>
(assuming we’re inside of Slurm job, so using <code>SLURM_JOB_ID</code> env. variable )</p>
<pre data-code-wrap="bash"><code class="lang-bash">export WORKDIR="${HOME}/.cache/slicerfs/${SLURM_JOB_ID}"
mkdir -p $WORKDIR
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> c.1.2): create directory for per-user persistent data and export it as <code>UPPERDIR</code><br>
<em>TODO: we should make this directory unique for every Slicer installation</em></p>
<pre data-code-wrap="bash"><code class="lang-bash">export UPPERDIR="${HOME}/.local/slicerFS"
mkdir -p $UPPERDIR
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> c.1.3): create mountpoint for overlayfs in user home.</p>
<pre data-code-wrap="bash"><code class="lang-bash">mkdir ${HOME}/SlicerMount
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> c.2.1): Mount overlayfs</p>
<pre data-code-wrap="bash"><code class="lang-bash">fuse-overlayfs -o lowerdir=/cvmfs/sys.sw.nudz/software/Slicer/5.6.1_bin,upperdir=${UPPERDIR},workdir=${WORKDIR},squash_to_uid=${UID} ${HOME}/SlicerMount
</code></pre>
<p>now we see the mount in <code>df</code>:</p>
<pre data-code-wrap="bash"><code class="lang-bash">user@sup204:~$ df | grep Slicer
fuse-overlayfs                       15300820992 13382676352 1918144640  88% /home/user/SlicerMount
user@sup204:~$
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> c.2.2): we can run Slicer by typing</p>
<pre data-code-wrap="bash"><code class="lang-bash">SlicerMount/Slicer
</code></pre>
<p>possibly install some extensions, restart app, and see extensions files here:</p>
<pre data-code-wrap="bash"><code class="lang-bash">user@sup204:~$ ls -1 ${HOME}/.local/slicerFS/slicer.org/Extensions-32438/
ABLTemporalBoneSegmentation
ABLTemporalBoneSegmentation-icon.png
ABLTemporalBoneSegmentation.s4ext
SlicerElastix
SlicerElastix-icon.png
SlicerElastix.s4ext
user@sup204:~$
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/arrow_right.png?v=12" title=":arrow_right:" class="emoji" alt=":arrow_right:" loading="lazy" width="20" height="20"> c.3.1): Umounting overlayfs</p>
<pre><code class="lang-auto">fusermount --unmount ./SlicerMount/
</code></pre>
<p><strong>Conclusion</strong></p>
<p>we were able to workaround issues coming from concepts used in Slicer. Follow-up tasks are to investigate feasibility of implementation steps indicated in this P-O-C using current state-of-the-art module system, Lmod.</p>

---

## Post #19 by @RafaelPalomar (2024-03-13 12:24 UTC)

<p>Would this work for python packages installed through <code>pip_install</code> inside Slicer?</p>

---

## Post #20 by @lassoan (2024-03-13 12:46 UTC)

<p>Thanks for sharing all these details <a class="mention" href="/u/jose-d">@jose-d</a>.</p>
<p>I am wondering if it is OK to install large Python packages in user-writable folders (e.g., Pytorch size is 5-10 GB when unpacked) then could the Slicer package (less than a GB when unpacked) be installed in the same user-writable folder? The Slicer executable would then be just a script that installs Slicer (downloads the package, unpacks it, applies any patches), and run the application. If Slicer is already installed then it would just run it.</p>
<p>That said, if overriding preinstalled Python packages by ones installed in user folders work then that is worth exploring, because then commonly used large packages could be preinstalled, saving some storage space.</p>

---

## Post #21 by @jose-d (2024-03-13 14:32 UTC)

<p>hello <a class="mention" href="/u/lassoan">@lassoan</a>;</p>
<p>first, thank you for reviewing my POC!</p>
<p>I saw <a class="mention" href="/u/muratmaga">@muratmaga</a> above being in apparently similar situation, I felt I should not keep my thoughts for myself so submitted it here for comments, brainstorming but also to collect critic. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>if it is OK to install large Python packages in user-writable folders</p>
</blockquote>
<p>So far my goal is to create centralized installation which will cover <em>typical scenario</em> of <em>typical user</em>, but keeping the possibility to install user extensions.</p>
<p>Hypothetical situation with having each user having very own Pytorch is indeed suboptimal, ideal solution could be based on concepts known in standard Python distributions - anything what is in <code>PYTHONPATH</code> is considered as python library… So introducing eg. <code>SLICERPATH</code> would make this for us much easier…</p>
<p>To me it loooks that Slicer has Windows-desktop-centric concepts, and I understand that HPC/cloud computing approaches, with features such as immutable app directories and software module systems, might seem exotic at first glance…</p>
<p>…but there are some reasons why the evolution of scientific computing / HPC went in this direction…:</p>
<ol>
<li>
<p><strong>science reproducibility</strong> - often various team-members onboards at various time, if they’d install the tools themselves, they’ll end with various versions possibly producing various results. With software modules it is easy to eg. require everybody use particular version of tool for given project, and eg. the latest one for casual work.</p>
</li>
<li>
<p><strong>aim to save human labor</strong> Why ask every single user to download tool, tweak it in certain way, if this could be done centrally? Some users are not IT-savvy, simple  <code>module load Software</code> and <code>Software</code> is then universal for all tools. There are projects with multiple team-members having identical setups. Their time is valuable, and they should not spend the time by repeating install procedure.</p>
</li>
<li>
<p><strong>governance of software updates</strong> Not every researcher reads announcements of majors tools. Scientific support engineers do.</p>
</li>
<li>
<p><strong>efficiency of software repository</strong> Today we have modern ways how to distribute scientific software - eg. CVMFS - this enables institutions to share our software repositories and letting users just “bring your own data”, or e.g  use cvmfs-distributed software at various collaborating institutions.</p>
</li>
<li>
<p><strong>platform optimization</strong> - with platform knowledge you can provide users with optimized numeric libraries, depending on eg. CPU microarchitecture or CUDA compute capabilities.</p>
</li>
</ol>
<p>EDIT: and possibly one last, reason:</p>
<ol start="6">
<li><strong>Slicer is one of many software we support</strong> - various users of our infrastructure use various apps in various ways, Conda, HCP Pipelines and ConnectomeWorkbench, Matlab, MRtrix, DCMTK, FSL, FreeSurfer… and perhaps tomorow Slicer too <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">   When new researcher comes, (s)he can quickly start with any tool with support. The low barrier is key.</li>
</ol>
<p>thanks for reading</p>

---

## Post #22 by @muratmaga (2024-03-13 14:59 UTC)

<aside class="quote no-group" data-username="jose-d" data-post="21" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jose-d/48/69652_2.png" class="avatar"> jose-d:</div>
<blockquote>
<p>To me it loooks that Slicer has Windows-desktop-centric concepts, and I understand that HPC/cloud computing approaches, with features such as immutable app directories and software module systems, might seem exotic at first glance…</p>
</blockquote>
</aside>
<p>About 95% of the Slicer users are using Slicer in Windows or Mac, and the remaining portion are probably using Linux boxes that they have full control over (like desktop computer). Current design has a long history, and it was aimed to make Slicer portable (i.e., if you put in the entire directory Slicer in a USB drive it should work, and it does). So it is normal a lot of things are designed for a proper desktop like enviornment with interactivity in mind.</p>
<p>Up until recently it was not easy (or sometime impossible) to deploy interactive UI applications in queue-based HPC systems, but it is becoming more and more common and doable. With powerful nodes and GPUS, if one has access to a local HPC, it makes sense to use it instead of cloud since probably costs are lower, plus your data is easier to get to (or out) than a remote cloud. So the discussion is more about how we can make it work without breaking what other 95% of users are used to.</p>
<p>I think for reproducibility point of view, what slicer does makes sense. Every package and extension you used to process the data is under the installation tree. if you want to preserve all you have to do is achive tar/zip it. For simpler than creating a docker or like container. Your zip file is the container.</p>
<p>My institutional environment has additional administrative challenges which uses proxies, firewalls, self-signed certificates making a user installed package like Slicer not to work very well (like extension manager would fail with https calls, etc). Otherwise I would probably let them install the software, but then everyone would have to figure out how to make the certificates work, which is a big ask.  So in this particular case maintaining it centrally makes sense…</p>
<p>We are also starting a new project to deploy Slicer on the cloud, and some of these discussion points are relevant. So I think we should keep talking, and I will definitely experiment with your install script and see if it helps for us.</p>

---

## Post #23 by @muratmaga (2024-03-13 15:06 UTC)

<aside class="quote no-group" data-username="jose-d" data-post="21" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jose-d/48/69652_2.png" class="avatar"> jose-d:</div>
<blockquote>
<p>Hypothetical situation with having each user having very own Pytorch is indeed suboptimal, ideal solution could be based on concepts known in standard Python distributions - anything what is in <code>PYTHONPATH</code> is considered as python library… So introducing eg. <code>SLICERPATH</code> would make this for us much easier…</p>
</blockquote>
</aside>
<p>So what is going to happen if people need different (or specific) versions of these packages (e.g., due to API differences or extension ask for a specific version of the python package), if the python packages are maintained centrally?</p>

---

## Post #24 by @jose-d (2024-03-14 08:32 UTC)

<p>this is very inspirative question. I have to say that I came here exactly for this. Thank you! The more I learn about slicer, the more I somehow understand the current state of things…</p>
<p>I see the need of somehow hybrid approach.</p>
<p>I am converging to concept of providing our users with</p>
<p>(1)  “<strong>slicer + goodies</strong>” - slicer + common modules + the possibility to install custom add-ons somewhere in <code>$HOME</code>…</p>
<p>(2) “<strong>bare</strong>” slicer - no site-installed add-ons - to be used in cases, when slicer+goodies distribution is not satisfactory, dependencies are blocking custom add-ons, etc. Extensions to be installed on top of that in <code>$HOME</code>.</p>
<p>We need to investigate use-cases of our researchers. Is it that they tend to use the same set of extensions? Or is it that they go <em>shopping</em> for addons, quite often? Do we have some idea how <em>typical user</em> acts?</p>
<p>Based on my experience with Python - we’re often able to cover need for basic modules, but at the end, every researcher ends with some custom per-project packages done by pip/conda/venv.</p>

---

## Post #25 by @jose-d (2024-03-14 08:46 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="22" data-topic="34805">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Up until recently it was not easy (or sometime impossible) to deploy interactive UI applications in queue-based HPC systems, but it is becoming more and more common and doable.</p>
</blockquote>
</aside>
<p>Yes. And the amount of data we’re collecting about our research subjects and increased awareness about data security is also significant motivation to keep data in well defined and secured server environments…</p>

---
