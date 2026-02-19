---
topic_id: 4883
title: "Rpy2 Pip Installation Fails"
date: 2018-11-27
url: https://discourse.slicer.org/t/4883
---

# Rpy2 pip installation fails

**Topic ID**: 4883
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/rpy2-pip-installation-fails/4883

---

## Post #1 by @muratmaga (2018-11-27 06:03 UTC)

<p>Following the thread, <a href="https://discourse.slicer.org/t/pip-in-nightly-build-not-working/3325">Pip in nightly build not working</a>, I got pip working as demonstrated.</p>
<p>But this fails:<br>
&gt;&gt;&gt; pipmain([‘install’, ‘Rpy2’])</p>
<p>Collecting Rpy2</p>
<p>Using cached <a href="https://files.pythonhosted.org/packages/f1/98/c7652cc9d7fc0afce74d2c30a52b9c9ac391713a63d037e4ab8feb56c530/rpy2-2.9.4.tar.gz" rel="nofollow noopener">https://files.pythonhosted.org/packages/f1/98/c7652cc9d7fc0afce74d2c30a52b9c9ac391713a63d037e4ab8feb56c530/rpy2-2.9.4.tar.gz</a></p>
<p>Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘c:\users\murat\appdata\local\temp\pip-req-tracker-vuah0s\a3317999c50976d8efecf0ed8dfd36602d75111dfb34525631802c24’</p>
<p>Any suggestions on how to fix this?</p>

---

## Post #2 by @muratmaga (2018-11-27 06:11 UTC)

<p>I think this is the same issue as this:</p><aside class="quote" data-post="22" data-topic="984">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/22">Slicer-Python Packages Use and Install</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Why I cant install this package 
pipmain([‘install’,‘scikit-fuzzy’]) 
Collecting scikit-fuzzy 
Using cached <a href="https://files.pythonhosted.org/packages/fb/79/71a79d2663ed662d30461aca261baff4fc87ddfd23f3e9baeaee86917f6b/scikit-fuzzy-0.3.1.tar.gz" rel="nofollow noopener">https://files.pythonhosted.org/packages/fb/79/71a79d2663ed662d30461aca261baff4fc87ddfd23f3e9baeaee86917f6b/scikit-fuzzy-0.3.1.tar.gz</a> 
Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘c:\users\22374464\appdata\local\temp\pip-req-tracker-v9vnky\6fa5e984c9f7c4180f5cbc9dc5bc4378cf0a090dcb740963746419f9’
  </blockquote>
</aside>


---

## Post #3 by @jamesobutler (2018-11-27 06:58 UTC)

<p>Yes, from briefly looking at the Rpy2 documentation there are some precompiled binaries. If you’re using Windows, you’re not going to be able to use this package in Slicer’s environment at this time. I recommend using pure python packages when using Slicer on Windows.</p>
<p>From the other thread that you linked above, the important information is in JC’s <a href="https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984/2">comment</a>.</p>
<blockquote>
<p>Second, on linux (and most likely macOS), it is indeed  <strong>possible to pip install official packages</strong>  (even the including binaries like  <code>scipy</code> ,  <code>tensorflow</code> , …).</p>
<p>On windows, it will currently work only for  <em>pure</em>  python wheels because the official package for python 2.7 are built with a compiler than the one used for the official wheels. Note that this will change as soon as we standardize on Visual Studio 2015 and switch to python &gt;= 3.5.</p>
</blockquote>
<p>The work towards python3 I believe is scheduled following a 4.10.1 release. So likely early next year.</p>

---

## Post #4 by @lassoan (2018-11-27 07:26 UTC)

<p>Note that you only need to use Slicer’s built-in Python interpreter to directly access GUI and scene data. You can run Python scripts in any external environment with any Python packages installed as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" rel="nofollow noopener">here</a>.</p>

---

## Post #5 by @muratmaga (2018-11-27 18:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>I am trying to get Rpy2 working within Slicer so that we can do some computations in R and visualize the results in Slicer using the extension we are building. So, if this is the use case, should I try to get it working with the internal python or use the external environment?</p>
<p>Thanks.</p>

---

## Post #6 by @jamesobutler (2018-11-27 19:56 UTC)

<p>If you’re needing Rpy2, use the external environment method as suggested by <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Can you describe the computation that you are doing in R? There could be another way of doing this without using R.</p>

---

## Post #7 by @muratmaga (2018-11-27 20:08 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>.</p>
<p>There are many different types of analyses that one can use landmark based shape analyses to investigate different biological questions (phylogenetics, ecology, evolutionary trajectories etc). Most of these are already implemented in R as different packages (and surprisingly almost none in python, AFAIK). We just don’t want to reimplement them in Slicer (and also take the responsibility of maintaining them). Instead our goal is to have a standard way of visualizing results by pulling and pushing data between these R packages (or at least that’s the idea).</p>
<p>I also noticed that is another package called pyRserve, which makes a remote connection to its sister package Rserve. That model may work us better than Rpy2.</p>

---

## Post #8 by @lassoan (2018-11-28 06:25 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="4883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Most of these are already implemented in R as different packages</p>
</blockquote>
</aside>
<p>We do landmark-based shape analysis using VTK and also experimenting with SlicerSALT and they work quite well.</p>
<p>What analysis do you plan to do? What R packages would you like to use? I’ve done a quick search and found <em>morpho</em> and <em>Rvcg</em> packages, but their features seem to be very limited compared to what VTK can do.</p>

---

## Post #9 by @muratmaga (2018-11-28 07:42 UTC)

<p>Try geomorph as well. It provides the basic procrustes superimposition and its typical outputs (consensus shape, procrustes residuals, riemann distances, centroid sizes, etc). From there  you can do eigen decomposition on your resultant coordinates and take your data to do phylogenetic analysis (phylocurve), or developmental trajectory studies, or do a partial least squares to assess overlaps in VCV matrices between different  components of your data (aka morphological integration).</p>
<p>These types of analyses are somewhat different (and harder to generalize) than the typical two group analyses (control vs patient) that are so common in biomedical contexts.</p>
<p>But more perhaps more importantly (for the users), the statistical foundation of most of those methods are well-understood and validated, and published in statistical (or field specific) journals, which is important for the target audience of our project.</p>

---

## Post #10 by @ihnorton (2018-11-28 14:11 UTC)

<p>If pyRserve works and is fast enough for your needs, then that sounds like a good option; network-based, de-coupled solutions are generally easier to maintain. If it turns out not to be fast enough, you may be able to build Rpy2 from source as part of your extension. This would assume it only links at runtime (e.g. ctypes) against a separate, configurable R library. However, if it requires R headers and libraries to build, then that is probably prohibitively complicated.</p>

---

## Post #11 by @lassoan (2018-11-28 14:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="4883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Try geomorph as well.</p>
</blockquote>
</aside>
<p>Thanks, yes, indeed <em>geomorph</em> seems to have a few features that are not available in VTK. Also, if your community uses geomorph as reference implementation then you may have little choice.</p>
<p>I’m surprised that geomorph uses GPL license. It is too bad, because I cannot afford to spend time on learning (and testing, reporting errors, contributing to) libraries that I may not be allowed to use in the future for any projects. Is this a trend in R community?</p>

---

## Post #12 by @muratmaga (2018-11-28 15:28 UTC)

<p>I can’t generalize, but I think there a lot of packages that are out there with GPL. You need to understand that people behind these packages are not team, but academicians that are spending a lot of time on very specific topic.</p>
<p>Though, I am not sure I understand your reluctance. GPL has only implications only on if you are going to redistribute the software. If your only using/testing reporting errors than why does it matter? I am assuming you are using Linux in your lab in one way or another, so your use case for geomorph is not much different than that.</p>

---

## Post #13 by @ihnorton (2018-11-28 16:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="4883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is this a trend in R community?</p>
</blockquote>
</aside>
<p>I’ve had the impression that GPL is preferred in the R community, and apparently it dominates by a wide margin:</p>
<p><a href="http://adolfoalvarez.cl/the-free-open-and-proprietary-flavors-of-r/" class="onebox" target="_blank" rel="noopener">http://adolfoalvarez.cl/the-free-open-and-proprietary-flavors-of-r/</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37b28d5ad5ca95b48b6be25da04a0f5bbe19caa.png" alt="image" data-base62-sha1="yJVTo36SBjjc4d4XueGEfzdj4Fk" width="418" height="333"></p>

---

## Post #14 by @lassoan (2018-11-28 23:42 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="4883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>GPL has only implications only on if you are going to redistribute the software. If your only using/testing reporting errors than why does it matter?</p>
</blockquote>
</aside>
<p>If I invest my into learning and contributing to GPL-licensed software then my time may be wasted because for some projects I or my collaborators cannot use software with restrictive license.</p>

---

## Post #15 by @pieper (2018-11-29 14:14 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> to echo what Andras is saying, the problem with GPL code is that it we <em>do</em> redistribute software in the form of Slicer and Slicer Extensions.  The terms of the GPL are such that if we include even one line of GPL licensed code in our distribution, then the copyright holder of that one line could insist that all other code in the same distribution needs to be GPL.  This would prevent people from using Slicer as the basis for non-public extensions (e.g. if making a medical device based on Slicer or even release binaries of pre-publication work in progress).</p>
<p>That’s why Andras and I and others (including the ITK community) are careful not to rely on GPL code.  In actual practice it would becomes very restrictive and counter-productive.  There’s a large literature on this so I won’t repeat it here, but the Linux kernel has specific clarifications about how it can be used in and redistributed and that’s one reason it’s so popular in products.</p>
<p>Anyone writing software that incorporates GPL code you should carefully read up on the terms and understand what obligations come with it.  The code may be so good that accepting those obligations is the best solution, but other times its best to find workarounds that are compatible with the licensing.</p>
<p>For us, the workaround of using R and other GPL’d code as an executable or network server sounds the cleanest way to address this for now.  It will allow us to make progress without raising license issues that may be hard to resolve.</p>
<p>Once we have the python 3 issues sorted out then <em>users will be able to install</em> R and R packages independently, and that will sidestep the distribution issues since it won’t be <em>us</em> distributing the software but the <em>user</em> installing it.  If Slicer only provides interfaces that are compatible with R then we don’t have the license issues.</p>
<p>I wish this weren’t so complicated but it’s the situation we have.  Fortunately the processes we have in place have worked well.  As long as we are careful there are no technical or legal hurdles that will get in our way.</p>

---

## Post #16 by @muratmaga (2018-11-29 18:16 UTC)

<p>thanks <a class="mention" href="/u/pieper">@pieper</a>. Yes, I think pyRserve/Rserve combination is the best solution, because indeed user will use packages that they specifically installed in their own R environment (wherever that might be). Glad to hear that this will not cause a license issue.</p>

---
