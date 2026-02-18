# Document modules on readthedocs

**Topic ID**: 330
**Date**: 2017-05-16
**URL**: https://discourse.slicer.org/t/document-modules-on-readthedocs/330

---

## Post #1 by @lassoan (2017-05-16 19:46 UTC)

<p>I quite like the <a href="http://slicer.readthedocs.io/en/latest/index.html">Slicer documentation on readthedocs</a>. I would like to try to write documentation for the Segment editor module there.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> How can I contribute? Should I push changes into the <a href="https://github.com/Slicer/Slicer/tree/rst-user-and-dev-guide/Docs">rst-user-and-dev-guide branch on GitHub</a>? Or should I wait for getting this branch merged to master?</p>

---

## Post #2 by @jcfr (2017-05-16 20:21 UTC)

<p>Great. Thanks for the feedback</p>
<p>For now, since readthedocs is configured to build the associated documentation, I suggest you push to this branch.</p>
<p>Note that I just rebased it on top of master. And since only both of us are working on this branch … do not hesitate to rebase it at your convenience.</p>

---

## Post #3 by @Lorensen (2017-05-16 20:43 UTC)

<p>Looks nice. But how does this differ from using github pages?</p>
<p>I’m experimenting with it here:<br>
<a href="https://lorensen.github.io/VTKExamples" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples</a></p>

---

## Post #4 by @jcfr (2017-05-16 20:52 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="3" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>Looks nice. But how does this differ from using github pages?</p>
</blockquote>
</aside>
<p>Few advantages, in addition of providing free hosting, Readthedocs provides:</p>
<ul>
<li>
<p>a free worker node that will rebuild the documentation each time it is needed</p>
</li>
<li>
<p>management of documentation version</p>
</li>
<li>
<p>support for downloading pdf and/or ebook</p>
</li>
<li>
<p>central location … looking on the readthedocs for documentation become the norm (at least for project adopting sphinx and/or python based)</p>
</li>
</ul>
<p>Using Github is totally possible but you would have explicitly setup yet an other machine to rebuild and push documentation every night or continuously</p>

---

## Post #5 by @jcfr (2017-05-16 20:52 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="3" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I’m experimenting with it here:<br>
<a href="https://lorensen.github.io/VTKExamples">https://lorensen.github.io/VTKExamples</a></p>
</blockquote>
</aside>
<p>Well done. These look quite nice <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @Lorensen (2017-05-16 21:04 UTC)

<p>On github, the pages are automatically updated when changes are pushed.</p>

---

## Post #7 by @Lorensen (2017-05-16 21:05 UTC)

<p>I still have some minor issues but it looks a lot better than the gitlab<br>
wiki.</p>

---

## Post #8 by @jcfr (2017-05-16 21:10 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="6" data-topic="330" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>On github, the pages are automatically updated when changes are pushed</p>
</blockquote>
</aside>
<p>Exactly, and that is great. That said, this happens in two cases:</p>
<ul>
<li>regular HTML is published</li>
<li><a href="https://jekyllrb.com/">jekyll</a> based templates are used</li>
</ul>
<p>In our case, documentation is written using RestructedText (with some markdown) and it first needs to be processed by <a href="http://www.sphinx-doc.org">sphinx</a> toolchain before we obtain HTML. And it turns our ReadTheDocs will take care of running the sphinx toolchain for us.</p>
<aside class="quote no-group" data-username="Lorensen" data-post="7" data-topic="330" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I still have some minor issues but it looks a lot better than the gitlab<br>
wiki.</p>
</blockquote>
</aside>
<p>Agreed <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @Lorensen (2017-05-16 21:28 UTC)

<p>I generate markdown code from the source tree, no html. I use mkdocs with<br>
the material theme. Medics generates the html.</p>

---

## Post #10 by @Lorensen (2017-05-16 21:29 UTC)

<p>Sorry, mkdocs generates the html.</p>

---

## Post #11 by @jcfr (2017-05-16 21:31 UTC)

<p>I see. In your case, the documentation toolchain is <code>mkdocs</code> and it outputs the html that is then pushed on GitHub.</p>
<p>Instead of maintaining a build machine yourself, you could have readthedocs taking care of running mkdocs for you. See <a href="http://docs.readthedocs.io/en/latest/builds.html#mkdocs">http://docs.readthedocs.io/en/latest/builds.html#mkdocs</a></p>

---

## Post #12 by @Lorensen (2017-05-16 21:45 UTC)

<p>I’ll take a look at readthedocs and see if it adds value for my app.</p>
<p>How long has readthe docs been around and is it’s future as stable as<br>
github?</p>

---

## Post #13 by @jcfr (2017-05-16 21:53 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="12" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>How long has readthe docs been around and is it’s future as stable as<br>
github?</p>
</blockquote>
</aside>
<p>Code base has been around for 7 years so far. See <a href="https://github.com/rtfd/readthedocs.org/graphs" class="inline-onebox">Pulse · readthedocs/readthedocs.org · GitHub</a></p>
<p>Hosting has been around for 4 years.</p>
<p>From  <a href="https://readthedocs.org/sustainability/" class="inline-onebox">Pricing - Read the Docs</a> :</p>
<pre><code class="lang-auto">Read the Docs has grown substantially since its beginning as a weekend project.
Today, we:

    Serve over 20 million pages of documentation a month
    Have 10 servers and serve over 2 TB of documentation a month
    Host over 18,000 projects and support 25,000 users
    Are supported by two dedicated engineers

</code></pre>

---

## Post #14 by @Lorensen (2017-05-16 22:07 UTC)

<p>2 guys… I think I’ll stick with github.</p>

---

## Post #15 by @jcfr (2017-05-16 22:31 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="14" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>2 guys…</p>
</blockquote>
</aside>
<p>Sounds good.</p>
<p>One more comment and I will let you make your final call …</p>
<ul>
<li>
<p>Having two dedicated engineers along with the described resources is (I think) outstanding and a positive and encouraging point <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  Also worth noting that Rackspace (who is also <a href="https://github.com/blog/493-github-is-moving-to-rackspace">providing the backend storage for GitHub</a>) is graciously providing the storage for readthedocs.</p>
</li>
<li>
<p>In addition of two dedicated engineers, their are three teams: Support team, operation team and development team. See <a href="https://docs.readthedocs.io/en/latest/team.html" class="inline-onebox">Read the Docs team — Read the Docs user documentation</a></p>
</li>
<li>
<p>To put things in perspective, there are three (most likely not dedicated and/or volunteer) maintainers for mkdocs. See <a href="http://www.mkdocs.org/about/release-notes/#maintenance-team" class="inline-onebox">Release Notes - MkDocs</a></p>
</li>
</ul>

---

## Post #16 by @jcfr (2017-05-16 22:32 UTC)

<p>Finally, note that in both case … if you want to serve documentation over https using a custom domain, you will have to setup your own server:</p>
<ul>
<li><a href="http://docs.readthedocs.io/en/latest/alternate_domains.html#cname-ssl">http://docs.readthedocs.io/en/latest/alternate_domains.html#cname-ssl</a></li>
<li><a href="https://help.github.com/articles/securing-your-github-pages-site-with-https/">https://help.github.com/articles/securing-your-github-pages-site-with-https/</a></li>
</ul>

---

## Post #17 by @lassoan (2017-05-16 22:36 UTC)

<p>Custom domain is very important, as it allows you to change anything (hosting, documentation generator, etc.) without disrupting users or search indexing bots. It is impossible to know what services will still exist in 2-3 years or if there will be much better options you will want to switch to.</p>

---

## Post #18 by @lassoan (2018-09-10 19:25 UTC)

<p>it would be nice to start using readthedocs more seriously for Slicer core module documentation. People could just use their GitHub account to contribute (no more wiki signup troubles), we could keep the code and documentation tightly linked, etc.</p>
<p><a href="https://blender-manual.readthedocs.io/en/latest/#">Blender manual on ReadTheDocs</a> is a good example of how it could look. It is a huge manual, so most probably we can use the same techniques, we would not need to invent anything new. Its source code is available here: <a href="https://developer.blender.org/diffusion/BM/">https://developer.blender.org/diffusion/BM/</a></p>
<p>The main complication right now is that the documentation is generated from a <a href="https://github.com/Slicer/Slicer/tree/rst-user-and-dev-guide">separate branch</a>. Keeping the documentation branch in sync with master is difficult because for example I want to merge changes of <code>util.py</code> from master, but some files are only present in the documentation branch.</p>
<p><strong>Should we maintain code and documentation in same repository and branch?</strong></p>
<p>Advantages of keeping code and documentation together:</p>
<ul>
<li>Documentation and code would be tightly synchronized. We could ensure that even small details, programming examples, etc. are always accurate.</li>
<li>We could do code and documentation updates in the same pull request (we can better enforce consistency and quality, include documentation testing in continuous integration, etc).</li>
<li>Documentation and code is kept together in smaller projects anyway, such as in Slicer extensions. We would use the same operating mechanism for Slicer core and extension documentation.</li>
<li>We can generate user and API documentation from the same repository. User and developer documentation are often interlinked, so it is useful if we can generate them together.</li>
</ul>
<p>Advantages of keeping documentation in separate repositories:</p>
<ul>
<li>Smaller code repository size. Slicer source code size is currently about 110MB. Over time, documentation would probably make it about 50% larger (estimated based on Blender manual, which is 70MB: contains 1900 png files, 1200 rst files).</li>
<li>Access control and development process could be defined separately for source code and documentation.</li>
</ul>
<p>I lean towards keeping code and documentation in one repository and branch. What do you think?<br>
<a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #19 by @cpinter (2018-09-10 19:42 UTC)

<p>I’d strongly prefer having them in the same repository. If we have the documentation in the code then it also will be much harder to forget updating the documentation (you need to realize that it needs to be changed, find the wiki page, upload new screenshot to mediawiki, etc.).</p>
<p>About the disadvantages of the same repository approach, the only one I consider a problem is access. I guess then we’d need a place where anybody can suggest edits, and a person who’s responsible for migrating the suggestions. Neither seem to be an easy problem to solve, but the second one could happen the same way we handle PRs: anyone who has a minute reviewing/integrating does it. Any ideas about how to offer the documentation for editing for the wide public?</p>

---

## Post #20 by @lassoan (2018-09-10 20:44 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="19" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Any ideas about how to offer the documentation for editing for the wide public?</p>
</blockquote>
</aside>
<p>You can edit documentation on the web interface and when you submit your change then a pull request is automatically created. So, documentation changes can be managed the same way as source code change requests. This would require promoting GitHub to be the primary repository (which we plan to do anyway).</p>

---

## Post #21 by @pieper (2018-09-10 21:10 UTC)

<p>I like the idea of putting everything in the same repository.  I think it’s just way simpler (and things are already complicated enough).</p>
<p>Repository size would be an issue if we host all images and movies in the repo.  Look at the <a href="https://github.com/NA-MIC/ProjectWeek">ProjectWeek</a> repo which is already almost half a gig.  At the same time I’d like a seamless process for adding media to the documentation.</p>
<p>Access control, actually sounds easier if we make all documentation changes pull requests.</p>

---

## Post #22 by @lassoan (2018-09-11 04:22 UTC)

<aside class="quote no-group" data-username="pieper" data-post="21" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Repository size would be an issue if we host all images and movies in the repo</p>
</blockquote>
</aside>
<p>Videos would probably not be updated that frequently, could be very big, and mostly accessed online (you could not print, would not want to bundle them with the manual anyway), so I think we should just add youtube links for videos (as it is done in Blender manual). We can enforce reduced-size screenshots and images through code reviews.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> It seems that we all lean towards trying to host documentation in the same repository and branch as the source code. If you agree, too, then it would be great if you could merge rst… branch to master and change readthedocs settings to generate documentation from master branch.</p>

---

## Post #23 by @cpinter (2018-09-11 12:48 UTC)

<p>If we make the merge and finally have a “live” rst documentation (the current one I consider kindof dormant), then I volunteer to migrate some of the most important pages to rst.</p>

---

## Post #24 by @lassoan (2018-09-11 14:14 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="23" data-topic="330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>the current one I consider kindof dormant</p>
</blockquote>
</aside>
<p>It is live (updated automatically within minutes) but generated from <a href="https://github.com/Slicer/Slicer/tree/rst-user-and-dev-guide">rst-user-and-dev-guide</a> branch. You can start adding content in that branch.</p>

---

## Post #25 by @cpinter (2018-09-11 14:27 UTC)

<p>Yes, thanks! I meant that it is a bit obscure and this is why nobody edits it. Once the doc is with the actual source code then editing it will be more coupled with the development process itself. I think this is the biggest issue right now.</p>

---

## Post #26 by @ihnorton (2018-09-11 20:51 UTC)

<p>One option for images is to store them in git-lfs. That way they are versioned, but don’t impact cloning or take up space in the “real” repository (when they are not used). See <a href="https://github.com/rtfd/readthedocs.org/issues/1846#issuecomment-278286430">this comment</a>.</p>

---

## Post #27 by @lassoan (2018-09-11 21:39 UTC)

<p>This is a great idea.</p>
<p>I think git-lfs is still a niche and can cause problems at many places, but if it is only used for documentation files then probably the impact can be minimized. If somebody does not bother with setting up git-lfs then only documentation files would be missed.</p>
<p>We would need to do some experiments if it works with web uploads and if automatic rules can be created that prevent accidental uploads of large documentation files as non-lfs objects.</p>

---

## Post #28 by @Lorensen (2018-09-11 22:18 UTC)

<p>I use git-lfs for large datasets in the VTKExamples. No probkems<br>
It does require a client side intsall to see the files.</p>

---
