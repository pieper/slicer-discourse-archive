# Docker is sunsetting Free Team organizations

**Topic ID**: 28497
**Date**: 2023-03-21
**URL**: https://discourse.slicer.org/t/docker-is-sunsetting-free-team-organizations/28497

---

## Post #1 by @jcfr (2023-03-21 14:14 UTC)

<h3><a name="p-92373-summary-1" class="anchor" href="#p-92373-summary-1" aria-label="Heading link"></a>Summary</h3>
<p>Docker is ending the Free Team organizations support that we are leveraging to publish, manage and store the <code>slicer</code> docker images available on dockerhub.</p>
<p>See <a href="https://hub.docker.com/u/slicer">https://hub.docker.com/u/slicer</a></p>
<p>Additional impacted dockerhub organizations - that we are involved with - are the following:</p>
<ul>
<li>dockcross
<ul>
<li><a href="https://github.com/dockcross/dockcross#readme">https://github.com/dockcross/dockcross#readme</a></li>
<li><a href="https://hub.docker.com/u/dockcross">https://hub.docker.com/u/dockcross</a></li>
</ul>
</li>
<li>ITK
<ul>
<li><a href="https://github.com/InsightSoftwareConsortium/ITK">https://github.com/InsightSoftwareConsortium/ITK</a></li>
<li><a href="https://hub.docker.com/u/insighttoolkit">https://hub.docker.com/u/insighttoolkit</a></li>
</ul>
</li>
<li>ctk
<ul>
<li><a href="https://commontk.org">https://commontk.org</a></li>
<li><a href="https://hub.docker.com/u/commontk">https://hub.docker.com/u/commontk</a></li>
</ul>
</li>
<li>dockbuild
<ul>
<li><a href="https://github.com/dockbuild/dockbuild#readme">https://github.com/dockbuild/dockbuild#readme</a></li>
<li><a href="https://hub.docker.com/u/dockbuild">https://hub.docker.com/u/dockbuild</a></li>
</ul>
</li>
</ul>
<h3><a name="p-92373-emails-posts-comments-2" class="anchor" href="#p-92373-emails-posts-comments-2" aria-label="Heading link"></a>Emails, posts &amp; comments</h3>
<p>On March 14th, we received the following message sent by docker:</p>
<blockquote>
<p>Free Team organizations are a legacy subscription tier that no longer exists. This tier included many of the same features, rates, and functionality as a paid Docker Team subscription.</p>
<p>After reviewing the list of accounts that are members of legacy Free Team organizations, we’ve identified yours as potentially being one of them.</p>
<p>If you own a legacy Free Team organization, access to paid features — including private repositories — will be suspended on <strong>April 14, 2023 (11:59 pm UTC)</strong>. Upgrade your subscription before <strong>April 14, 2023</strong> to continue accessing your organization.</p>
<p>If you don’t upgrade to a paid subscription, Docker will retain your organization data for 30 days, after which it will be subject to deletion. During that time, you will maintain access to any images in your public repositories, though rate limitations will apply. At any point during the 30-day period, you can restore access to your organization account if you upgrade to a paid subscription. Visit our <a href="https://em.docker.com/NzkwLVNTQi0zNzUAAAGKf9O0IC8BwS-GUyEnxbhy4Uf7tH7ZVtDfkFlOEsKbXFuO-JvEgPyl-T4CA8cvqUsQgE9pz_5brKqaGrg=">FAQ</a> for more information.</p>
</blockquote>

---

## Post #2 by @jcfr (2023-03-21 14:18 UTC)

<p>The open-source community at large has been confused about the exact impact of this communication, reviewing <a href="https://github.com/docker/hub-feedback/issues/2314">docker/hub-feedback#2314</a> gives a good idea of this.</p>
<p>Below are selected replies from Docker staff attempting to clarify:</p>
<hr>
<blockquote>
<p>Hi folks, than you for your feedback!</p>
<p>Docker has a <a href="https://www.docker.com/community/open-source/application">specific DSOS program for open-source projects</a>, and it is not affected by the sunsetting of Free Team plans. We are listening to feedback and may offer additional programs in the future.</p>
<p>We will defer any organization suspension or deletion while DSOS application is under review, and give organizations at least 30 days before we suspend the organization if the application is ultimately rejected.</p>
<p>Any organizations suspended or deleted will not release the namespace, so squatting previous namespaces will not be possible.</p>
<p>Thank you and please keep the open feedback coming!</p>
</blockquote>
<p>Source: <a href="https://github.com/docker/hub-feedback/issues/2314#issuecomment-1468574145">https://github.com/docker/hub-feedback/issues/2314#issuecomment-1468574145</a></p>
<hr>
<blockquote>
<p>We relaunched the Docker-Sponsored Open Source program in September 2022 (<a href="https://www.docker.com/blog/docker-sponsored-open-source-program-has-a-new-look/">blog post here</a>). Since we made significant changes to the qualification criteria (we removed the limitation of not being able to have commercial funding for your project), we emailed all projects who applied the to Docker-Sponsored Open Source program prior to September to invite them to reapply with our new review process. If you did not receive that communication, there may have been gaps in email deliverability. I encourage everyone to apply to the Docker-Sponsored Open Source program using the <a href="https://www.docker.com/community/open-source/application/">updated application form</a> and criteria.</p>
<p>Additionally, thank you for the feedback on the submission form. We are using your suggestions to inform how we can bring more clarity to the Docker-Sponsored Open Source program and ultimately serve the open-source community as best we can.</p>
</blockquote>
<p>Source: <a href="https://github.com/docker/hub-feedback/issues/2314#issuecomment-1470011070">https://github.com/docker/hub-feedback/issues/2314#issuecomment-1470011070</a></p>

---

## Post #3 by @jcfr (2023-03-21 14:22 UTC)

<p>We considered applying to <em>Docker-Sponsored Open Source Program</em> offered by Docker, but the current offering does not seems compliant with our commercialization pathways.</p>
<blockquote>
<p>To qualify for the program, your project namespace must:</p>
<ul>
<li>Be shared in public repos.</li>
<li>Meet the <a href="https://opensource.org/docs/osd">Open Source Initiative definition</a></li>
<li>Be in active development (this means image updates are pushed regularly within the past 6 months or dependencies are updated regularly, even if the project source code is stable)</li>
<li>Not have a pathway to commercialization. Your organization must not seek to make a profit through services or by charging for higher tiers. Accepting donations to sustain your efforts is permissible.</li>
</ul>
</blockquote>
<p>Source: <a href="https://www.docker.com/community/open-source/application/">https://www.docker.com/community/open-source/application/</a></p>

---

## Post #4 by @jcfr (2023-03-21 14:27 UTC)

<p>In an attempt to clarify, Docker staff followed with additional official communication</p>
<blockquote>
<p><strong>We apologize for how we communicated and executed sunsetting Docker “Free Team” subscriptions, which alarmed the open source community.</strong></p>
<p>For those of you catching up, we recently emailed accounts that are members of Free Team organizations, to let them know that they will lose features unless they move to one of our supported free or paid offerings. This impacted less than 2% of our users. <strong>Note that this change does not affect</strong> <a href="https://www.docker.com/pricing"><strong>Docker Personal, Docker Pro, Docker Team, or Docker Business accounts</strong></a><strong>,</strong> <a href="https://www.docker.com/community/open-source/application/"><strong>Docker-Sponsored Open Source</strong></a> <strong>members,</strong> <a href="https://docs.docker.com/docker-hub/publish/"><strong>Docker Verified Publishers</strong></a><strong>, or</strong> <a href="https://docs.docker.com/docker-hub/official_images/"><strong>Docker Official Images</strong></a><strong>.</strong></p>
<p>The Docker Free Team subscription was deprecated in part because it was poorly targeted. In particular, it didn’t serve the open source audience as well as <a href="https://www.docker.com/blog/docker-sponsored-open-source-program-has-a-new-look/">our recently updated Docker-Sponsored Open Source program</a>, the latter offering benefits that exceed those of the deprecated Free Team plan.</p>
<p><strong>We’d also like to clarify that public images will only be removed from Docker Hub if their maintainer decides to delete them.</strong> We’re sorry that our initial communications failed to make this clear.</p>
<p>We apologize again for the poor communication and execution surrounding this deprecation and promise to continue to <a href="https://github.com/docker/hub-feedback/issues/">listen to community feedback</a>.</p>
<p>[…]</p>
<p><strong>FAQ</strong></p>
<p>Will open source images I rely on get deleted?</p>
<p><strong>Not by Docker. Public images will only disappear if the maintainer of the image decides to proactively delete it from Docker Hub. If the maintainer takes no action, we will continue to distribute their public images.</strong> (Of course, if the maintainer migrates to the Docker-Sponsored Open Source program or to a paid Docker subscription, we will also continue to distribute their public images.)</p>
<p>[…]</p>
</blockquote>
<p>Source: <a href="https://www.docker.com/blog/we-apologize-we-did-a-terrible-job-announcing-the-end-of-docker-free-teams/">https://www.docker.com/blog/we-apologize-we-did-a-terrible-job-announcing-the-end-of-docker-free-teams/</a></p>

---

## Post #5 by @jcfr (2023-03-21 14:37 UTC)

<h3><a name="p-92378-path-forward-1" class="anchor" href="#p-92378-path-forward-1" aria-label="Heading link"></a>Path forward</h3>
<p>We are currently looking into the following:</p>
<ul>
<li><a href="https://www.docker.com/pricing/">Team</a> subscription offered by dockerhub</li>
<li>Transition to <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry">GitHub packages registry</a></li>
<li>Transition to <a href="https://quay.io/plans/">quay</a> registry</li>
<li>Self-hosting</li>
</ul>

---

## Post #6 by @RafaelPalomar (2023-03-21 15:20 UTC)

<p>Thanks a lot <a class="mention" href="/u/jcfr">@jcfr</a> for the post. It is very informative!</p>

---

## Post #7 by @Vad1mo (2023-03-23 15:03 UTC)

<p>Hey all, we are running an alternative service to Docker Hub based on CNCF Harbor Open-Source Registry. I am one of the maintainers.</p>
<p>As an org that builds OSS and exists because of OSS we are offering a dedicated container registry for OSS projects.<br>
Some advantages you won’t see anywhere else.</p>
<ol>
<li>Maintain your brand and control access with a custom domain, e.g. <a href="http://registry.slicer.org" rel="noopener nofollow ugc">registry.slicer.org</a><br>
(btw. it is also super easy to move, no lock-in)</li>
<li>Replicate to other registries from a central hub.</li>
</ol>
<p>Hit me up if you want to elaborate the option, happy to help.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://container-registry.com/posts/how-does-dockers-decision-of-sunsetting-free-team-organizations-impacts-you/">
  <header class="source">
      <img src="https://container-registry.com/favicon.png" class="site-icon" width="" height="">

      <a href="https://container-registry.com/posts/how-does-dockers-decision-of-sunsetting-free-team-organizations-impacts-you/" target="_blank" rel="noopener nofollow ugc">container-registry.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://container-registry.com/posts/How-Does-Dockers-Decision-of-Sunsetting-Free-Team-Organizations-Impacts-You/card.jpg" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://container-registry.com/posts/how-does-dockers-decision-of-sunsetting-free-team-organizations-impacts-you/" target="_blank" rel="noopener nofollow ugc">How Does Dockers Decision of Sunsetting Free Team Organizations Impacts You</a></h3>

  <p>Even if you don’t have a team organization and what you can do about it. Docker Inc. continues on its course of eliminating free offerings: Now the "Docker Free Team" model has to take its turn. With the «Free Team Organizations» offering, it was...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @jcfr (2023-03-23 16:44 UTC)

<h3><a name="p-92482-path-forward-1" class="anchor" href="#p-92482-path-forward-1" aria-label="Heading link"></a>Path forward</h3>
<p>On March 28th during our <a href="https://discourse.slicer.org/c/community/hangout/20">weekly meeting</a>, we will select a registry.</p>
<h3><a name="p-92482-our-images-2" class="anchor" href="#p-92482-our-images-2" aria-label="Heading link"></a>Our images</h3>
<ul>
<li>
<p><code>slicer-base</code> image</p>
<ul>
<li>Built daily &amp; automatically on the <code>metroplex</code> Linux factory.</li>
<li>Currently hosted at <a href="https://hub.docker.com/r/slicer/slicer-base">https://hub.docker.com/r/slicer/slicer-base</a></li>
<li>The image is then used to build Slicer pull requests. See <a href="https://github.com/Slicer/Slicer/blob/main/.github/actions/slicer-build/Dockerfile">.github/actions/slicer-build/Dockerfile</a></li>
<li>Sources at <a href="https://github.com/Slicer/SlicerDocker">https://github.com/Slicer/SlicerDocker</a></li>
</ul>
</li>
<li>
<p><code>slicer/slicer-notebook</code> image</p>
<ul>
<li>Manually built</li>
<li>Sources at <a href="https://github.com/Slicer/SlicerDocker">https://github.com/Slicer/SlicerDocker</a></li>
<li>See <a href="https://github.com/Slicer/SlicerDocker/issues/34" class="inline-onebox">Push slicer-notebook image to dockerhub · Issue #34 · Slicer/SlicerDocker · GitHub</a></li>
</ul>
</li>
<li>
<p><code>buildenv-qt&lt;version&gt;-&lt;operatingsystem&gt;</code> (e.g <code>buildenv-qt5-centos7</code>)</p>
<ul>
<li>Hosted at <a href="https://hub.docker.com/r/slicer/buildenv-qt5-centos7">https://hub.docker.com/r/slicer/buildenv-qt5-centos7</a></li>
<li>Built manually on a Linux workstation  (usually <code>metroplex</code>)</li>
<li>Sources at <a href="https://github.com/Slicer/SlicerBuildEnvironment">https://github.com/Slicer/SlicerBuildEnvironment</a></li>
<li>Depends on <code>dockbuild-*</code> images (e.g <code>dockbuild/centos7-devtoolset7-gcc7</code>)</li>
</ul>
</li>
<li>
<p><code>dockbuild</code> images</p>
<ul>
<li>Hosted at <a href="https://hub.docker.com/u/dockbuild">https://hub.docker.com/u/dockbuild</a></li>
<li>Automatically published leveraging <a href="https://github.com/dockbuild/dockbuild/blob/master/.circleci/config.yml">CircleCI</a> workflow</li>
<li>Can be published manually</li>
<li>Sources at <a href="https://github.com/dockbuild/dockbuild">https://github.com/dockbuild/dockbuild</a></li>
</ul>
</li>
<li>
<p><code>commontk/qt-static:4.8.6-centos-5.5</code></p>
<ul>
<li>Hosted at <a href="https://hub.docker.com/r/commontk/qt-static/tags">https://hub.docker.com/r/commontk/qt-static/tags</a></li>
<li>Manually built and published</li>
<li>Used to build the <code>CTKAppLauncher</code> Linux binary package. See associated CircleCI workflow at <a href="https://github.com/commontk/AppLauncher/blob/v0.1.31/.circleci/config.yml">.circleci/config.yml</a></li>
</ul>
</li>
<li>
<p><code>slicer/slicerexecutionmodel</code></p>
<ul>
<li>Hosted at <a href="https://hub.docker.com/r/slicer/slicerexecutionmodel">https://hub.docker.com/r/slicer/slicerexecutionmodel</a></li>
<li>Used for the testing of <code>SlicerExecutionModel</code>. See associated CircleCI workflow at <a href="https://github.com/Slicer/SlicerExecutionModel/blob/master/.circleci/config.yml">.circleci/config.yml</a></li>
<li>Sources at <a href="https://github.com/Slicer/SlicerExecutionModel/tree/master/test">https://github.com/Slicer/SlicerExecutionModel/tree/master/test</a></li>
</ul>
</li>
</ul>
<h3><a name="p-92482-alternatives-3" class="anchor" href="#p-92482-alternatives-3" aria-label="Heading link"></a>Alternatives</h3>
<p>Reviewing the comments associated with <a href="https://github.com/docker/hub-feedback/issues/2314">docker/hub-feedback#2314</a>, I identified few projects that transitioned.</p>
<h4><a name="p-92482-github-packages-registry-4" class="anchor" href="#p-92482-github-packages-registry-4" aria-label="Heading link"></a>GitHub packages registry</h4>
<blockquote>
<p>GitHub Packages is free for public repositories</p>
</blockquote>
<p>See <a href="https://github.com/features/packages#pricing">https://github.com/features/packages#pricing</a></p>
<p>Links:</p>
<ul>
<li>Documentation: <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry">https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry</a></li>
<li>Portal: Built-in each GitHub organization</li>
<li>Examples:
<ul>
<li><a href="https://github.com/orgs/clamsproject/packages" class="inline-onebox">Packages · CLAMS Project · GitHub</a>
<ul>
<li><a href="https://github.com/clamsproject/.github/issues/1">https://github.com/clamsproject/.github/issues/1</a></li>
</ul>
</li>
<li><a href="https://github.com/orgs/qmk/packages" class="inline-onebox">Packages · QMK · GitHub</a>
<ul>
<li><a href="https://github.com/qmk/qmk_base_container/pull/39">https://github.com/qmk/qmk_base_container/pull/39</a></li>
</ul>
</li>
<li><a href="https://github.com/orgs/livebook-dev/packages" class="inline-onebox">Packages · Livebook · GitHub</a>
<ul>
<li><a href="https://github.com/livebook-dev/livebook/pull/1792">https://github.com/livebook-dev/livebook/pull/1792</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<h4><a name="p-92482-quay-5" class="anchor" href="#p-92482-quay-5" aria-label="Heading link"></a>quay</h4>
<blockquote>
<p>[…] offer unlimited storage and serving of public repositories.</p>
</blockquote>
<p>See “Additional FAQs” at <a href="https://quay.io/plans/">https://quay.io/plans/</a></p>
<p>Links:</p>
<ul>
<li>Documentation: <a href="https://docs.quay.io/">https://docs.quay.io/</a></li>
<li>Portal: <a href="https://quay.io/search">https://quay.io/search</a></li>
<li>Example(s):
<ul>
<li><a href="https://quay.io/organization/pypa">https://quay.io/organization/pypa</a></li>
</ul>
</li>
</ul>
<h4><a name="p-92482-container-registry-6" class="anchor" href="#p-92482-container-registry-6" aria-label="Heading link"></a>container-registry</h4>
<blockquote>
<p>offering a […] discounted dedicated container to Open-Source projects […]</p>
</blockquote>
<p>See <a href="https://container-registry.com/posts/how-does-dockers-decision-of-sunsetting-free-team-organizations-impacts-you/">this post</a></p>
<p>Links:</p>
<ul>
<li>Documentation: <a href="https://container-registry.com/docs/">https://container-registry.com/docs/</a></li>
<li>Portal: <a href="https://c8n.io/">https://c8n.io/</a></li>
</ul>

---

## Post #9 by @jcfr (2023-03-24 22:18 UTC)

<p>Docker is reversing its original plan <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=12" title=":tada:" class="emoji" alt=":tada:" loading="lazy" width="20" height="20">  This means we do not need to migrate our images.</p>
<blockquote>
<p>from: Docker<br>
date: Mar 24, 2023, 5:25 PM<br>
subject: We’re no longer sunsetting Free Team organizations</p>
<p>On March 14, 2023, we emailed you about your Free Team subscription, outlining our intention to sunset that plan. After listening to the concerns of the community, we’ve decided to reverse course, and are no longer sunsetting the Free Team plan.</p>
<p>If you’re currently on the Free Team plan, you no longer have to migrate to another plan by April 14. All customers who upgraded to a paid subscription will automatically receive a full refund for the transaction in the next 30 days, allowing them to use their new paid subscription for free for the duration of the term they purchased.</p>
</blockquote>
<p>See <a href="https://www.docker.com/developers/free-team-faq/">https://www.docker.com/developers/free-team-faq/</a>:</p>

---

## Post #10 by @rbumm (2023-03-25 06:13 UTC)

<p>Thank you JC for all the work you have put into this.</p>

---
