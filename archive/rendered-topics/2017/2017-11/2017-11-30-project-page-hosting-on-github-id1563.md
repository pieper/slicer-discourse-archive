---
topic_id: 1563
title: "Project Page Hosting On Github"
date: 2017-11-30
url: https://discourse.slicer.org/t/1563
---

# Project page hosting on GitHub?

**Topic ID**: 1563
**Date**: 2017-11-30
**URL**: https://discourse.slicer.org/t/project-page-hosting-on-github/1563

---

## Post #1 by @lassoan (2017-11-30 14:46 UTC)

<p>I’ve ported a couple of intro pages and the current project week page from Slicer wiki to GitHub to show how we could use GitHub for project week page hosting:</p>
<p>Published website (using default blank theme): <a href="https://na-mic.github.io/ProjectWeek/">https://na-mic.github.io/ProjectWeek/</a></p>
<p>Example project page: <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/SlicerVR/">https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/SlicerVR/</a></p>
<p>Link for editing/uploading pages: <a href="https://github.com/NA-MIC/ProjectWeek">https://github.com/NA-MIC/ProjectWeek</a></p>
<p>Editable project template: <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW27_2018_Boston/Projects/Template/README.md">https://github.com/NA-MIC/ProjectWeek/blob/master/PW27_2018_Boston/Projects/Template/README.md</a></p>
<p>Main advantages of GitHub:</p>
<ul>
<li>Full offline access. Entire wiki can be downloaded and viewed/edited on a laptop, without network access.</li>
<li>Developer familiarity. All developers have GitHub account and familiar with how to upload and edit files.</li>
<li>Uses Markdown, a very commonly used markup style (used for in the Slicer forum, GitHub, Slack, etc). MediaWiki markup is only used on MediaWiki sites.</li>
</ul>
<p>Should we start using GitHub for hosting projects pages for this project week?</p>
<p><a class="mention" href="/u/tina_kapur">@Tina_Kapur</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/ungi">@ungi</a></p>
<p><s><strong>EDITED:</strong> Changed project name from <code>ProjectWeek</code> into <code>SlicerProjectWeeks</code></s><br>
<strong>EDITED <span class="hashtag">#2:</span></strong> Changed back to <code>ProjectWeek</code> to be inclusive and not focused on a specific platform.<br>
<strong>EDITED <span class="hashtag">#3:</span></strong> Changed <code>27</code> to <code>PW27_2018_Boston</code></p>

---

## Post #2 by @fedorov (2017-11-30 18:11 UTC)

<p>I agree there are many advantages moving away from the wiki. Another one to add to the list is that the process becomes much easier for new users to get an account and contribute content. It happened several times in my memory when users requested wiki accounts, but their request was misplaced, or took too long to approve.</p>
<p>I am struggling to think of disadvantages moving away from the wiki. Perhaps it is the ranking of the existing pages, but I would think that should be resolved with cross-linking.</p>
<p>However, I do not think web page is the right format. I would recommend GitBook. In addition to all of the advantages listed above:</p>
<ul>
<li>it supports hierarchical organization of the content</li>
<li>content can be edited in a WYSIWYG editor, or directly in Markdown</li>
<li>content can be contributed using either GitHub pull request, or direct edit of the content</li>
</ul>
<p>See example here: <a href="https://qiicr.gitbooks.io/dcmqi-guide/content/">https://qiicr.gitbooks.io/dcmqi-guide/content/</a>. GitBook is also working on a new release, which has (in my view) further streamlined presentation (I have not spent a lot of time investigating the new one, just learned about it this week), see example of the same content on the new platform here: <a href="https://qiicr.gitbook.io/dcmqi-guide/">https://qiicr.gitbook.io/dcmqi-guide/</a>.</p>

---

## Post #3 by @fedorov (2017-11-30 18:14 UTC)

<p>I could put together an example of how this would look like on GitBook a bit later, if interested, so we can compare side by side…</p>

---

## Post #4 by @lassoan (2017-11-30 19:58 UTC)

<p>GitBook is just another html generator/hosting with some nice additional tools and it’s own Markdown flavor. We don’t need to decide on which generator(s) we will use, as we’ll host and edit Markdown files on GitHub anyway.</p>
<p>Last time we checked GitBook was not open to provide their service freely to a large number of users. Has anything changed?</p>
<p>In addition to GitBook, we may consider GitHub pages with various templates, Sphinx/ReadTheDocs, Reveal.js, etc. If we keep things simple then we can probably remain compatible with multiple generators.</p>

---

## Post #5 by @lassoan (2017-11-30 20:02 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="1563" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I could put together an example of how this would look like on GitBook a bit later, if interested, so we can compare side by side…</p>
</blockquote>
</aside>
<p>You can probably generate a gitbook from the current repository (maybe fork it so that you can experiment with what additional template and other files you have to add).</p>

---

## Post #6 by @jcfr (2017-11-30 21:57 UTC)

<p>Well done <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I like it.</p>
<p>Any objection in renaming the project to “slicer-project-week” or “SlicerProjectWeek” ?</p>
<blockquote>
<p>becomes much easier for new users to get an account and contribute content. It happened several times in my<br>
memory when users requested wiki accounts, but their request was misplaced, or took too long to approve.</p>
</blockquote>
<p>For the wiki, I think the idea was to avoid systematically granting access to everyone and explicitly authorize individual. We could change that and it will greatly streamline contribution. I start an other topic to discuss this.</p>
<p>The advantage of Github is that anyone can submit a PR without having anyone explicitly granting access before hand. This will indeed streamline the process.</p>

---

## Post #7 by @lassoan (2017-12-01 02:22 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Any objection in renaming the project to “slicer-project-week” or “SlicerProjectWeek” ?</p>
</blockquote>
</aside>
<p>I actually wanted to rename it to SlicerProjectWeeks but did not have the required access level. I think SlicerProjectWeeks is better than SlicerProjectWeek, as most likely we would host multiple project weeks in the same repository.</p>

---

## Post #8 by @lassoan (2017-12-01 02:25 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>The advantage of Github is that anyone can submit a PR without having anyone explicitly granting access</p>
</blockquote>
</aside>
<p>We’ll have to see what works well in practice but we could grant write access to each person who submits a pull request with a meaningful project page. With protected branches it is quite safe to grant people write access, as it prevents accidentally overwriting the history. But I would expect that most people would directly edit the pages on the web GUI.</p>

---

## Post #9 by @cpinter (2017-12-01 03:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>With protected branches it is quite safe to grant people write access</p>
</blockquote>
</aside>
<p>In this page <a href="https://help.github.com/articles/about-protected-branches" class="inline-onebox">About protected branches - GitHub Docs</a> I read “Can’t be edited or have files uploaded to it from the web”. If it is still like this, then making it a protected branch would make it much harder to edit pages as every change would require a PR or git commit.</p>

---

## Post #10 by @lassoan (2017-12-01 03:50 UTC)

<p>I’ve just tried and you can commit directly into a protected branch. I think protected branches got more sophisticated during the past years - you can set it up to only disable force push and delete of the branch.</p>

---

## Post #11 by @fedorov (2017-12-01 04:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="1563" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>GitBook is just another html generator/hosting with some nice additional tools and it’s own Markdown flavor. We don’t need to decide on which generator(s) we will use, as we’ll host and edit Markdown files on GitHub anyway.</p>
</blockquote>
</aside>
<p>Pure Markdown will not be sufficient, as we will need to adjust image sizes, insert videos etc. So some flavor of Markdown will be necessary. I don’t think flavors will migrate seamlessly across the various content management services you mentioned.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="1563" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Last time we checked GitBook was not open to provide their service freely to a large number of users. Has anything changed?</p>
</blockquote>
</aside>
<p>What do you mean? If you mean large number of collaborators on a single book, then yes - that is constrained. We can apply for free next tier subscription, and that will increase the number of collaborators on a single book to 10. We did this for QIICR.</p>
<p>However, it that is not really critical, since GitBook content can be synchronized with a GitHub repo, which can follow conventional GitHub contribution workflow, and the GitBook automatically updated to track master or another selected branch. I think it should also be possible for other contributors to fork the GitHub repo, make a GitBook from that fork, edit content using visual editor on a specific branch, and then make a pull request back upstream.</p>

---

## Post #12 by @jcfr (2017-12-01 07:03 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I actually wanted to rename it to SlicerProjectWeeks.</p>
</blockquote>
</aside>
<p>~~Repository renamed to <code>SlicerProjectWeeks</code> . See <a href="https://na-mic.github.io/SlicerProjectWeeks/~~">https://na-mic.github.io/SlicerProjectWeeks/~~</a></p>
<p><strong>EDITED:</strong> Changed project name changed back to <code>ProjectWeek</code> so pages are available at <a href="https://na-mic.github.io/ProjectWeek/" class="inline-onebox">Welcome to the main page for the Project Week events! | NA-MIC Project Weeks</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but did not have the required access level.</p>
</blockquote>
</aside>
<p>Strange. You have “Owner” role within the NA-MIC GitHub organization.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We’ll have to see what works well in practice but we could grant write access to each person who submits a pull request with a meaningful project page. With protected branches it is quite safe to grant people write access, as it prevents accidentally overwriting the history. But I would expect that most people would directly edit the pages on the web GUI.</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>we will need to adjust image sizes, insert videos etc</p>
</blockquote>
</aside>
<p>For youtube video, the preview picture  could be added. See <a href="https://stackoverflow.com/questions/4279611/how-to-embed-a-video-into-github-readme-md">here</a></p>
<p>For adjusting image size, using <code>&lt;img width="250px" src="https://url/to/image.png"&gt;</code> should work</p>

---

## Post #13 by @pieper (2017-12-01 13:35 UTC)

<p>I suspect there will be a learning curve for the community no matter which method we pick.  Hosting directly from github markdown pages seems the most “standard” and for that reason I think that people will derive the most educational benefit from getting familiar with the github process and github markdown, even if we have to live with some limitations (which so far seem fairly minor for our purposes).</p>

---

## Post #14 by @lassoan (2017-12-01 14:39 UTC)

<p>I agree. We can start with plain markdown syntax, it’s simple and compatible with everything. Once we gathered some initial experience, we can make much better informed decisions about how to improve things.</p>
<p>Has anybody talked to <a class="mention" href="/u/tina_kapur">@Tina_Kapur</a>? If she is OK with this, too, then we should announce that project pages should be created in this GitHub repository (and update the wiki page so that it points to the GitHub page).</p>

---

## Post #15 by @jcfr (2017-12-01 15:38 UTC)

<p>Nitpick:</p>
<p>Instead of <code>27</code> as the name of the directory, should we follow a convention like <code>&lt;Number&gt;_&lt;YYYY-MM&gt;_&lt;COUNTRY&gt;_&lt;CITY&gt;</code></p>
<p>For example:</p>
<pre><code class="lang-auto">25_2017-06_Italy_Calabria
27_2018-01_USA_Boston
</code></pre>

---

## Post #16 by @ihnorton (2017-12-01 16:27 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="15" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Instead of 27 as the name of the directory, should we follow a convention like &lt;Number&gt;<em>&lt;YYYY-MM&gt;</em>&lt;COUNTRY&gt;_&lt;CITY&gt;</p>
</blockquote>
</aside>
<p>I think these are too long and annoying to type during the week – especially on mobile. So could we please at least set up <a href="http://projectweek.slicer.org">projectweek.slicer.org</a> or even <a href="http://pw.slicer.org">pw.slicer.org</a> as a redirect?</p>
<p>(I’m not sure why would these semantic URLs be useful? no one is going to remember how to type that, and google doesn’t care anyway <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )</p>

---

## Post #17 by @pieper (2017-12-01 16:50 UTC)

<p>The value of the semantic URL to me would be when you send or embed a link it would be easier to know in advance what you are linking to.</p>
<p>+1 to the idea of <a href="http://pw.slicer.org">pw.slicer.org</a> as a redirect.</p>

---

## Post #18 by @lassoan (2017-12-01 17:16 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="15" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>27_2018-01_USA_Boston</p>
</blockquote>
</aside>
<p>In same cases more verbose, in other situations simpler, more predictable names are better.</p>
<p>Probably 27 is not trivial to interpret, while 27_2018-01_USA_Boston is a bit too long to type. What about these?</p>
<ul>
<li>PW27</li>
<li>PW27_2018_Boston</li>
<li>PW27_2018_Jan_Boston</li>
</ul>

---

## Post #19 by @cpinter (2017-12-01 17:18 UTC)

<p>I support finding some middle ground. My vote goes to PW27_2018_Boston, I think it’s not hard to remember even if you need to type it, and you’ll know when and where that project week was.</p>

---

## Post #20 by @fedorov (2017-12-01 22:19 UTC)

<p>I would definitely suggest <a href="http://pw.na-mic.org">pw.na-mic.org</a>. Branding project week with a specific platform can create various issues now and especially in the future. We should be inclusive, and think about possible issues down the road. I also think that this kind of decision should involve Ron. Monitoring updates from discourse can be cumbersome, and I suggest we should email Ron directly to seek his input.</p>

---

## Post #21 by @jcfr (2017-12-01 22:36 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="19" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>My vote goes to PW27_2018_Boston,</p>
</blockquote>
</aside>
<p>Here is a PR renaming the directory. If there is no objection,  will plan on merging tomorrow.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/NA-MIC/ProjectWeek/pull/1">
  <header class="source">

      <a href="https://github.com/NA-MIC/ProjectWeek/pull/1" target="_blank" rel="noopener">github.com/NA-MIC/ProjectWeek</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/NA-MIC/ProjectWeek/pull/1" target="_blank" rel="noopener">Rename "27" to "PW27_2018_Boston"</a>
      </h4>

    <div class="branches">
      <code>NA-MIC:master</code> ← <code>jcfr:rename-27-to-pw27-2018-boston</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2017-12-01" data-time="22:35:15" data-timezone="UTC">10:35PM - 01 Dec 17 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 9 files with 1 additions and 1 deletions">
          <a href="https://github.com/NA-MIC/ProjectWeek/pull/1/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/project-page-hosting-on-github/1563/19?u=jcfr</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Cc: <a class="mention" href="/u/ihnorton">@ihnorton</a></p>

---

## Post #22 by @jcfr (2017-12-02 00:53 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="21" data-topic="1563">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>will plan on merging tomorrow.</p>
</blockquote>
</aside>
<p>Following the review of <a class="mention" href="/u/ihnorton">@ihnorton</a>, the change has been merged.</p>

---

## Post #23 by @mschwier (2017-12-07 16:11 UTC)

<p>Just wanted to quickly check about the decision status. Has it been decided if GitHub will be the new home for the Project Week pages (i.e. should I add my projects there)?</p>

---

## Post #24 by @cpinter (2017-12-07 16:25 UTC)

<p>Yes, numerous projects have been added already, please add yours there too.</p>

---

## Post #25 by @gcsharp (2017-12-13 17:26 UTC)

<p>Is there some description of how to add the project page?  Apparently I don’t have write access, so I should fork and issue a pull request?  Or something else?</p>

---

## Post #26 by @gcsharp (2017-12-13 17:27 UTC)

<p>Also, I tried <a href="http://pw.na-mic.org" rel="nofollow noopener">pw.na-mic.org</a>, and it redirects to mantis.</p>

---

## Post #27 by @ihnorton (2017-12-13 17:51 UTC)

<p>See</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/" target="_blank" rel="nofollow noopener">ProjectWeek</a>
  </header>
  <article class="onebox-body">
    

<h3><a href="https://na-mic.github.io/ProjectWeek/PW27_2018_Boston/Projects/" target="_blank" rel="nofollow noopener">How to create a new project</a></h3>

<p>Website for NA-MIC Project Weeks</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
