# Its all about transitions! Lets talk about Slicer's landing page

**Topic ID**: 113
**Date**: 2017-04-13
**URL**: https://discourse.slicer.org/t/its-all-about-transitions-lets-talk-about-slicers-landing-page/113

---

## Post #1 by @bpaniagua (2017-04-13 20:03 UTC)

<p>Hi all,</p>
<p>I would like to bring up again the topic of transitioning the <a href="http://Slicer.org">Slicer.org</a> landing page to a place that facilitates collaboration.</p>
<p>As you know, <a class="mention" href="/u/rkikinis">@rkikinis</a> appointed me to start looking into showcasing the different slicer-communities in the Slicer landing page. We created a mockup in January during project week that planned to show different slicer user communities directly in the landing page.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1c4ed49edcbf722dd83b69752f6fab177f3cc60.png" data-download-href="/uploads/short-url/rEa44L1CVK1veeftdRHJbmMhtks.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c4ed49edcbf722dd83b69752f6fab177f3cc60_2_663x500.png" alt="image" data-base62-sha1="rEa44L1CVK1veeftdRHJbmMhtks" width="663" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c4ed49edcbf722dd83b69752f6fab177f3cc60_2_663x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1c4ed49edcbf722dd83b69752f6fab177f3cc60.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1c4ed49edcbf722dd83b69752f6fab177f3cc60.png 2x" data-dominant-color="DFDEDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×599 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> and I have discussed before about moving <a href="http://slicer.org">slicer.org</a> to github pages within the<a href="https://github.com/Slicer"> Slicer github group</a>. I know this has been <a href="https://www.na-mic.org/Wiki/index.php/2016_Winter_Project_Week/Projects/UpgradeNAMICSlicerWiki">a topic of discussion for a while</a>.</p>
<p>Are there any supporters for conserving the current structure, or to move towards github pages? Are there any general ideas on how to move forward with this?</p>
<p>Thank you!<br>
Bea</p>

---

## Post #2 by @Lorensen (2017-04-13 20:51 UTC)

<p>What is wrong with the current technology.</p>

---

## Post #3 by @jcfr (2017-04-13 21:33 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="2" data-topic="113" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>What is wrong with the current technology.</p>
</blockquote>
</aside>
<p>Hi Bill,</p>
<p>Thanks for commenting on the new Slicer Discourse forum <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<h4><a name="p-248-overview-1" class="anchor" href="#p-248-overview-1" aria-label="Heading link"></a>Overview</h4>
<p>The current website already successfully presents Slicer and its outstanding community. It served us well and is still serving us and our users.</p>
<p>That said, considering what is possible today, the current infrastructure doesn’t allow to easily experiment and improve the website. I think it is important to enable everyone to do so. In the long run, it will make the Slicer platform and associated projects more useful.</p>
<h4><a name="p-248-current-infrastructure-2" class="anchor" href="#p-248-current-infrastructure-2" aria-label="Heading link"></a>Current infrastructure</h4>
<p>It consists of html pages (and few wiki2web pages) stored on a server that have to be updated by a single person (without relying on version control).</p>
<p>While the individual(s) helping in the process are awesome and responsive, the process is quite daunting and involves often a lot of emails.</p>
<h4><a name="p-248-next-3" class="anchor" href="#p-248-next-3" aria-label="Heading link"></a>Next</h4>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> will help us move forward and improve the user experience related to the main Slicer website.</p>

---

## Post #4 by @Lorensen (2017-04-13 22:00 UTC)

<p>I see. I thought the discussion was about the wiki. I  agree that html is<br>
old technology.</p>

---

## Post #5 by @jcfr (2017-04-13 23:09 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="4" data-topic="113">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>I  agree that html is old technology.</p>
</blockquote>
</aside>
<p>It is not that HTML in itself is <em>old technology</em>, I think there are more modern ways for collaboratively managing the associated code and assets.</p>
<p>Otherwise, you will find below the list of pages I compiled back in 2015 when we moved pages from wiki2web technology to the wiki.</p>
<p>It illustrates that all the pages except the top level one are now hosted on the the wiki (with redirect in place when needed)</p>
<p>To get started, I just:</p>
<ul>
<li>added the current top level page and associated assets to <a href="https://github.com/Slicer/slicer.org/tree/gh-pages">https://github.com/Slicer/slicer.org/tree/gh-pages</a></li>
<li>updated the readme file: <a href="https://github.com/Slicer/slicer.org" class="inline-onebox">GitHub - Slicer/slicer.org: This site is published at slicer.org.</a></li>
</ul>
<p>The website have been published bu GitHub is now served from <a href="http://slicer.github.io/slicer.org/">http://slicer.github.io/slicer.org/</a></p>
<p>If we all agree to move forward with this experiment and adopt GitHub to host and serve our website, I wonder if Mike and/or Greg could setup the redirection ? (cc: <a class="mention" href="/u/pieper">@pieper</a> ?)</p>
<h4><a name="p-258-about-slicer-1" class="anchor" href="#p-258-about-slicer-1" aria-label="Heading link"></a>About Slicer</h4>
<ul>
<li>Introduction: <a href="https://www.slicer.org/wiki/Documentation/Release/Announcements">wiki/Documentation/Release/Announcements</a></li>
<li>Acknowledgments: <a href="https://www.slicer.org/wiki/Documentation/Release/Acknowledgments">wiki/Documentation/Release/Acknowledgments</a></li>
<li>News: <a href="https://www.slicer.org/wiki/News">wiki/News</a></li>
<li>Contact: <a href="https://www.slicer.org/wiki/Contact">wiki/Contact</a>
<ul>
<li>Redirected from: <a href="http://www.slicer.org/pages/Contact" class="inline-onebox">Contact - Slicer Wiki</a></li>
</ul>
</li>
<li>Licensing: <a href="https://www.slicer.org/wiki/Licensing">wiki/Licensing</a>
<ul>
<li>Redirected from <a href="http://www.slicer.org/pages/License" class="inline-onebox">License - Slicer Wiki</a></li>
</ul>
</li>
<li>Commercial Use: <a href="https://www.slicer.org/wiki/CommercialUse">wiki/CommercialUse</a>
<ul>
<li>Redirected from <a href="http://www.slicer.org/pages/Slicer4Industry">http://www.slicer.org/pages/Slicer4Industry</a></li>
</ul>
</li>
</ul>
<h4><a name="p-258-publications-2" class="anchor" href="#p-258-publications-2" aria-label="Heading link"></a>Publications</h4>
<ul>
<li>Publication DB: External website <a href="http://www.spl.harvard.edu/publications/pages/display/?collection=11">www.spl.harvard.edu/publications</a></li>
<li>Image Gallery: External website <a href="http://www.spl.harvard.edu/publications/gallery?selectedCollection=11">www.spl.harvard.edu/publications/gallery</a></li>
<li>Slicer Community: <a href="https://www.slicer.org/wiki/Main_Page/SlicerCommunity">wiki/Main_Page/SlicerCommunity</a></li>
<li>Citing Slicer: <a href="https://www.slicer.org/wiki/CitingSlicer">wiki/CitingSlicer</a></li>
</ul>
<h4><a name="p-258-documentation-3" class="anchor" href="#p-258-documentation-3" aria-label="Heading link"></a>Documentation</h4>
<ul>
<li>Slicer Training: <a href="https://www.slicer.org/wiki/Documentation/4.6/Training">wiki/Documentation/4.6/Training</a></li>
<li>User manual: <a href="https://www.slicer.org/wiki/Documentation/4.6">wiki/Documentation/4.6</a></li>
<li>Developer manual: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers">wiki/Documentation/Nightly/Developers</a></li>
</ul>
<h4><a name="p-258-help-4" class="anchor" href="#p-258-help-4" aria-label="Heading link"></a>Help</h4>
<ul>
<li>Help: <a href="https://www.slicer.org/wiki/Help">wiki/Help</a></li>
<li>User FAQ: <a href="https://www.slicer.org/wiki/FAQ">wiki/FAQ</a></li>
<li>Developer FAQ: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ">wiki/Documentation/Nightly/Developers/FAQ</a></li>
</ul>
<h4><a name="p-258-links-5" class="anchor" href="#p-258-links-5" aria-label="Heading link"></a>Links</h4>
<ul>
<li><a href="http://download.slicer.org">download.slicer.org</a>: <a href="http://download.slicer.org">http://download.slicer.org</a></li>
<li>Slicer Wiki: <a href="https://www.slicer.org/wiki/Main_Page">wiki/Main_Page</a></li>
<li><a href="http://slicer.org">slicer.org</a>: <a href="https://www.slicer.org/">https://www.slicer.org/</a></li>
</ul>

---

## Post #6 by @jcfr (2017-04-13 23:24 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>could setup the redirection</p>
</blockquote>
</aside>
<p>The only downside (if an issue at all) is that we can not redirect <a href="https://slicer.org">https://slicer.org</a> to <a href="https://github.com/Slicer/slicer.org" class="inline-onebox">GitHub - Slicer/slicer.org: This site is published at slicer.org.</a></p>
<blockquote>
<p>HTTPS is not supported for GitHub Pages using custom domains.</p>
</blockquote>
<p>Source: <a href="https://help.github.com/articles/securing-your-github-pages-site-with-https/" class="inline-onebox">Securing your GitHub Pages site with HTTPS - GitHub Docs</a></p>
<p>That said, there are ways to enable this:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/">
  <header class="source">
      <img src="https://blog.cloudflare.com/images/favicon-32x32.png" class="site-icon" width="" height="">

      <a href="https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/" target="_blank" rel="noopener" title="02:04PM - 14 June 2016">The Cloudflare Blog – 14 Jun 16</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/" target="_blank" rel="noopener">Secure and fast GitHub Pages with CloudFlare</a></h3>

  <p>Get the latest news on how products at Cloudflare are built, technologies used, and join the teams helping to build a better Internet.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But these come with trade-off too.</p>

---

## Post #7 by @mhalle (2017-04-25 18:41 UTC)

<p>Actually, this is going to be tricky, possibly too tricky to have <a href="http://github.io" rel="nofollow noopener">github.io</a> hosting be viable.</p>
<p><a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> (which forwards to <a href="http://www.slicer.org" rel="nofollow noopener">www.slicer.org</a> as per best practices) is now hosted on Digital Ocean.  <a href="http://www.slicer.org/wiki" rel="nofollow noopener">www.slicer.org/wiki</a> points to the wiki, also hosted on digital ocean. There are a bunch of rules on the <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> web server that keep old links working while allowing current, consistent, cleaned up wiki URIs.  Backward compatibility was one of our goals in the re-architecture of the wiki.</p>
<p>If we moved <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> to github, we don’t have a place to put those Apache configurations, since <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> is top-level.  Right now I don’t see how it can be done.</p>
<p>An alternative would be to author the site on github, and pull it over to the main site where our existing <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> HTTP server would serve it.  That would also take care of the SSL configuration, which is working and continuously maintained using letsencrypt.</p>
<p>Let me know your thoughts.<br>
–Mike</p>

---

## Post #8 by @fedorov (2017-04-25 20:20 UTC)

<p>Yet another alternative is to declare everything-wiki “legacy”, and move on with hosting documentation using ReadTheDocs or GitBook, as some of the folks discussed earlier.</p>
<p>Do we have any idea of who is using Slicer wiki, how it is used (editors/readers ratio), what pages are being accessed, etc? My guess is that it could be the case that most of the wiki content is not used either because it is obsolete, not searchable, or for various other reasons.</p>
<p>Just wanted to float this idea around.</p>

---

## Post #9 by @pieper (2017-04-25 21:19 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> in fact, we do now have some good data on that via google analytics, at least on page views and it’s in the thousands per day (see below).  I would not want to move to either gitbooks or readthedocs because either one would be a disruptive change that doesn’t offer enough advantages at the moment.</p>
<p>I like the idea of hosting the repository for <a href="http://slicer.org">slicer.org</a> static pages on github and then using the existing digital ocean infrastructure that already handles the wiki to host that content under https.</p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> it sounds like we could set up something like:</p>
<p><a href="http://github.com/SlicerExample/example.slicer.org">github.com/SlicerExample/example.slicer.org</a> =&gt; <a href="https://example.slicer.org">https://example.slicer.org</a></p>
<p>where “=&gt;” means a githook publishes every commit over to the digital ocean host and “example” can be any community that wants to participate, is that right?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f44548017f00899bb7f01f154023252a97eec0b.png" data-download-href="/uploads/short-url/2b3yDaxsJJRkjRmB3Wk0Gnbnb9p.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f44548017f00899bb7f01f154023252a97eec0b_2_565x500.png" alt="image" data-base62-sha1="2b3yDaxsJJRkjRmB3Wk0Gnbnb9p" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f44548017f00899bb7f01f154023252a97eec0b_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f44548017f00899bb7f01f154023252a97eec0b_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f44548017f00899bb7f01f154023252a97eec0b.png 2x" data-dominant-color="F3F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1069×945 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @fedorov (2017-04-25 21:43 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> it is great that we have analytics set up! It should be very helpful to prioritize migration, if there is ever agreement to do it.</p>
<p>I disagree though about “a disruptive change that doesn’t offer enough advantages”. I think it is an opportunity to bring some order to the various resources that piled up over the last decade, and improve the appeal of these resources. By making documentation more accessible for both users and developers, we have a chance to attract more people and grow the community, and there are few things that are more valuable than that. I think there is also relatively low risk if wiki is maintained in read-only legacy mode, as the content is migrated/populated.</p>
<p>But I also think that, as we have experienced already, reaching consensus on what will be the new platform is challenging.</p>

---

## Post #11 by @jcfr (2017-04-26 04:21 UTC)

<p><a class="mention" href="/u/mhalle">@mhalle</a> Thanks for the investigating. It all makes sense.</p>
<aside class="quote no-group" data-username="mhalle" data-post="7" data-topic="113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>An alternative would be to author the site on github, and pull it over to the main site where our existing <a href="http://slicer.org">slicer.org</a> HTTP server would serve it.  That would also take care of the SSL configuration, which is working and continuously maintained using letsencrypt.</p>
</blockquote>
</aside>
<p>Agreed.</p>
<p>Look like this tools should be helpful: <a href="https://github.com/adnanh/webhook" class="inline-onebox">GitHub - adnanh/webhook: webhook is a lightweight incoming webhook server to run shell commands</a></p>
<p>It should allow to easily create endpoint and execute command based on the payload.</p>
<p>For example, here is a <a href="https://github.com/adnanh/webhook/wiki/Hook-Examples#incoming-github-webhook">hook definition</a> for GitHub payload.</p>
<p>In other word, it is a generalization of the <a href="https://github.com/Slicer/github-circleci-trigger">flask app</a> I put together to trigger generation of apidocs.</p>
<p>We should make sure the end points we setup:</p>
<ul>
<li>checks that the payload come from the range of ips matching Github (see <a href="https://developer.github.com/v3/meta/" class="inline-onebox">Meta - GitHub Docs</a>   and <a href="https://github.com/Slicer/github-circleci-trigger/blob/cf77f2866a06f8db385fc3e326d574a0eccd94c6/github-circleci-trigger.py#L32-L61">ip_check</a></li>
<li>checks a secret agreed one when setting the webhook</li>
</ul>

---

## Post #12 by @jcfr (2017-05-16 14:17 UTC)

<p>During the weekly developer hangout, <a class="mention" href="/u/bpaniagua">@bpaniagua</a> and I talk about this, and we suggest to setup a cron job on the server that is currently serving “<a href="http://slicer.org">slicer.org</a>” ?</p>
<p>A cron job like this one (running every minutes) should do the work:</p>
<pre><code class="lang-auto">SITE_DIR=/path/to/slicer.org
if [[ ! -d $SITE_DIR ]]; then
  git clone https://github.com/Slicer/slicer.org $SITE_DIR
fi
cd $SITE_DIR
git fetch origin
git reset --hard origin/gh-pages
</code></pre>

---

## Post #13 by @pieper (2017-06-06 13:55 UTC)

<p>I just talked with <a class="mention" href="/u/mhalle">@mhalle</a> about this and it sounds like the digital ocean instance is now set up and would be ready to start autopulling from <a href="http://github.com/Slicer/Slicer.org">github.com/Slicer/Slicer.org</a>.  As I understand it <a class="mention" href="/u/freephile">@freephile</a> has a git repository of what is currently hosted on <a href="https://slicer.org">https://slicer.org</a> which I think is similar (identical?) to what is currently on github.</p>
<p>So I think we are ready for the plan to make the <a href="http://github.com/Slicer/Slicer.org">github.com/Slicer/Slicer.org</a> repository become the official one and use github issues and pull requests to maintain it.</p>

---

## Post #14 by @freephile (2017-06-06 14:51 UTC)

<p>I haven’t compared them bit by bit, but the index.html content does look similar between <a href="https://slicer.github.io/slicer.org/" rel="nofollow noopener">https://slicer.github.io/slicer.org/</a> and <a href="https://slicer.org/index.html" rel="nofollow noopener">https://slicer.org/index.html</a></p>
<p>There is a bunch more file content in the live <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> site.  Some of which just needs to be purged (e.g. DownloadSlicer.php).  Some may be desired, but ignored in the repo (e.g. doc), in which case we’ll just use the .gitignore file to avoid collision. And some would be candidates for addition to the repo (e.g. robots.txt).</p>
<p>Also, <a class="mention" href="/u/mhalle">@mhalle</a> I noticed that <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a> is different from <a href="http://download.slicer.org/" rel="nofollow noopener">http://download.slicer.org/</a></p>
<p>git ls-files|grep -v doc/<br>
.gitignore<br>
DownloadSlicer.php<br>
css/basic.css<br>
css/basic.css~<br>
css/ie.css<br>
css/ie5mac.css<br>
css/styles.css<br>
css/styles.css.bak<br>
css/styles.css~<br>
favicon.ico<br>
img/3DSlicer-DesktopIcon.png<br>
img/3DSlicer4Logo-H-218X144.png<br>
img/3DSlicerLogo-H-Color-218x144.png<br>
img/Logo-Slicer.png<br>
img/Logo-Slicertext.png<br>
img/Search.png<br>
img/Slicer4Announcement-HiRes.png<br>
img/animated_favicon1.gif<br>
img/bullet_more2.gif<br>
img/bullet_style1.gif<br>
img/bullet_style1.png<br>
img/bullet_style4.jpg<br>
img/bullet_style5.jpg<br>
img/bullet_style6.jpg<br>
img/dl-l.png<br>
img/doc-l.png<br>
img/favicon.ico<br>
img/fb-l.png<br>
img/focal/js/config.php<br>
img/focal/js/download.php<br>
img/icons612.png<br>
img/logo2_slicer.png<br>
img/logo_slicer.png<br>
img/misc/Bugtracking-hover-old.png<br>
img/misc/Bugtracking-hover.png<br>
img/misc/Bugtracking-l.png<br>
img/misc/Bugtracking-old.png<br>
img/misc/Bugtracking.png<br>
img/misc/Documentations-hover-old.png<br>
img/misc/Documentations-hover.png<br>
img/misc/Documentations-l.png<br>
img/misc/Documentations-old.png<br>
img/misc/Documentations.png<br>
img/misc/Download-hover-old.png<br>
img/misc/Download-hover.png<br>
img/misc/Download-l.png<br>
img/misc/Download-old.png<br>
img/misc/Download.png<br>
img/misc/DownloadNav-hover.png<br>
img/misc/DownloadNav-hover.png.bak<br>
img/misc/DownloadNav.png<br>
img/misc/DownloadNav.png.bak<br>
img/misc/Slicer3.6Release.png<br>
img/misc/Slicer4Announcement-612x362.jpg<br>
img/misc/SlicerExtensions-612.png<br>
img/misc/Tutorial-hover-old.png<br>
img/misc/Tutorial-hover.png<br>
img/misc/Tutorial-l.png<br>
img/misc/Tutorial-old.png<br>
img/misc/Tutorial.png<br>
img/misc/bugtracker.png<br>
img/misc/bugtracker1.png<br>
img/misc/documentation.png<br>
img/misc/documentation1.png<br>
img/misc/download.png<br>
img/misc/download1.png<br>
img/misc/slicer4Announcement612px-i-mj.png<br>
img/misc/tutorial1.png<br>
img/misc/tutorials.png<br>
img/re/chunk1.png<br>
img/re/chunk10.png<br>
img/re/chunk11.png<br>
img/re/chunk12.png<br>
img/re/chunk2.png<br>
img/re/chunk3-blank.png<br>
img/re/chunk3-orange.png<br>
img/re/chunk3.png<br>
img/re/chunk4-blank.png<br>
img/re/chunk4-orange.png<br>
img/re/chunk4.png<br>
img/re/chunk5-blank.png<br>
img/re/chunk5-orange.png<br>
img/re/chunk5.png<br>
img/re/chunk6-blank.png<br>
img/re/chunk6-orange.png<br>
img/re/chunk6.png<br>
img/re/chunk7.png<br>
img/re/chunk7r.png<br>
img/re/chunk8-blank.png<br>
img/re/chunk8-orange.png<br>
img/re/chunk8.png<br>
img/re/chunk8r-orange.png<br>
img/re/chunk8r.png<br>
img/re/chunk8r2.png<br>
img/re/chunk9.png<br>
img/re4.1/Bugtracking-hover.png<br>
img/re4.1/Bugtracking.png<br>
img/re4.1/Documentations-hover.png<br>
img/re4.1/Documentations.png<br>
img/re4.1/Download-hover.png<br>
img/re4.1/Download.png<br>
img/re4.1/Tutorial-hover.png<br>
img/re4.1/Tutorial.png<br>
index.html<br>
robots.txt</p>

---

## Post #15 by @pieper (2017-06-06 15:13 UTC)

<p>Thanks Greg.  I’m not sure what all is in the existing <a href="http://slicer.org">slicer.org</a> folder,<br>
but based on the toplevel page it looks like most links to go the wiki or<br>
to the download site, so perhaps we just start fresh with just index.html<br>
and its assets.  On the other hand it doesn’t look huge, so we could commit<br>
it all and then clean up.</p>
<p>Either way I understand that <a href="http://github.com/Slicer/Slicer.org">github.com/Slicer/Slicer.org</a> is a placeholder<br>
that can be overwritten by the content of the currently non-public<br>
<a href="http://slicer.org">slicer.org</a> git.</p>

---

## Post #16 by @freephile (2017-06-06 15:43 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I made a <a href="https://github.com/Slicer/slicer.org/pull/1" rel="nofollow noopener">pull request</a> to update index.html  Do you want to make me an editor on the repo, so I can push, or if you want I can continue to issue pull requests.</p>
<p>With that merged, I can pull the github repo and setup cron on <a href="https://slicer.org" rel="nofollow noopener">https://slicer.org</a></p>
<p>I’ll simply archive the existing content listed above (it’s all legacy by the looks of it), and add in the .gitignore, favicon and robots.txt files to the github repo.</p>

---

## Post #17 by @jcfr (2017-06-06 15:52 UTC)

<p>Thanks Greg. PR merged <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #18 by @jcfr (2017-06-06 15:54 UTC)

<p><a class="mention" href="/u/freephile">@freephile</a> I also just sent you an invite to join <a href="https://github.com/orgs/Slicer/teams/slicer-website-maintainers">https://github.com/orgs/Slicer/teams/slicer-website-maintainers</a></p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> Similarly you also have a pending invitation …</p>

---

## Post #19 by @freephile (2017-06-06 18:55 UTC)

<p>OK, this is done.  The website is pulling every 5 minutes from the repo.  <strong>Any merged changes into the repo will go live automatically.</strong></p>
<p>The <a href="https://github.com/Slicer/slicer.org/tree/gh-pages" rel="nofollow noopener">repo has been updated</a> with a README etc. And unused content has been moved aside on the server for eventual deletion.</p>

---

## Post #20 by @jcfr (2017-06-06 19:03 UTC)

<p>Very nice <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=5" title=":thumbsup:" class="emoji" alt=":thumbsup:"></p>
<p>Now that we have the sync setup, what do you think of:</p>
<ul>
<li>we rename <code>gh-page</code> branch to <code>slicer-org</code>
</li>
<li>create a branch <code>preview-slicer-org</code>  that would allow to try changes on “<a href="http://preview.slicer.org">preview.slicer.org</a>” (or we could have the preview rendered by Github configured at as github page)</li>
</ul>

---

## Post #21 by @freephile (2017-06-06 22:28 UTC)

<p>I’d have to change the sync if we change the branch name, so it’s important to coordinate.</p>
<p>Since gh-pages is configured in GitHub to automatically be hosted at <a href="http://slicer.github.io" rel="nofollow noopener">slicer.github.io</a>. I’d use that branch name as a ‘preview’, but the caveat is how do we avoid accidental visits that would fake out a user?</p>
<p>For hosting the true site, we don’t really need a new branch. we could just merge the current gh-pages into master and then pull from master.</p>

---

## Post #22 by @jcfr (2017-06-06 23:00 UTC)

<aside class="quote no-group" data-username="freephile" data-post="21" data-topic="113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/freephile/48/248_2.png" class="avatar"> freephile:</div>
<blockquote>
<p>I’d use that branch name as a ‘preview’</p>
</blockquote>
</aside>
<p>The branch used for github pages can now be configured</p>
<blockquote>
<p>merge the current gh-pages into master and then pull from master</p>
</blockquote>
<p>Since I anticipate we will add some scripts and tooling to potentially help build the static content, I still think it makes sense to server the site from a dedicated branch (e.g <code>slicer-org</code>)</p>
<p>In the mean time, I created a new branch named <code>slicer-org</code> based of the existing <code>gh-pages</code> …</p>
<blockquote>
<p>how do we avoid accidental visits that would fake out a user</p>
</blockquote>
<p>We could add some javascript checking the hostname and making a banner visible</p>

---

## Post #23 by @freephile (2017-06-07 02:02 UTC)

<p>Sounds good.</p>
<p>I updated the git version on the host which works better with credential configuration and cron seems happy with <code>git fetch</code></p>

---

## Post #24 by @bpaniagua (2017-06-21 16:57 UTC)

<p>What is the font that is used in the 3DSlicer logo? Such in this image <a href="https://www.slicer.org/img/3DSlicerLogo-H-Color-218x144.png">https://www.slicer.org/img/3DSlicerLogo-H-Color-218x144.png</a></p>

---

## Post #25 by @ihnorton (2017-07-17 15:33 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> I was just wondering the same thing for another logo and found your question <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"> Copy-pasting the text from Mac Preview of a <a href="https://www.slicer.org/wiki/Slicer3:Slicer3Brand#PDF">pdf version of the logo</a> into TextEdit, the font appears to be Verdana (changing it back and forth gives the same look so I think that’s correct).</p>

---

## Post #26 by @bpaniagua (2017-09-13 15:01 UTC)

<p>Hi all,</p>
<p>Now that are using the <a href="http://github.com/Slicer/Slicer.org">github.com/Slicer/Slicer.org</a> repo as the main Slicer landing page, I wanted to bring back to the conversation the fact we wanted to give some presence to the SlicerDistributions to the landing page.</p>
<p>I did a version of what that would look like here: <a href="https://bpaniagua.github.io/slicer.org/">https://bpaniagua.github.io/slicer.org/</a></p>
<p>Ideas?</p>
<p>Bea</p>

---

## Post #27 by @lassoan (2017-09-16 13:46 UTC)

<p>It’s a good start.</p>
<p>What I miss the most is that these distributions are most importantly custom downloads, but they are not mentioned on the download page.</p>
<p>SlicerRT and SlicerIGT will remain just extensions - we don’t plan to create custom install packages. So, I don’t know if we should list them among distributions.</p>

---

## Post #28 by @bpaniagua (2017-09-18 20:29 UTC)

<p>I believe we discussed this over <a href="https://na-mic.org/wiki/2017_Winter_Project_Week/Organizations">Project Week</a> thinking it is not really about the dissemination mechanism (custom packages vs extensions), but about having a start-to-end software solution that serves a very specific research community. These communities can be either methodological (i.e. salt, dmri) or clinical (i.e. IGT, CIP).</p>
<p>The problem here is that we might be getting a bit tangled on the syntax/branding of what we are trying to provide more presence to. Maybe “SlicerDistributions” refers too much to the dissemination vehicle. I believe it will benefit everybody to present these specialized solutions within Slicer to our user-base 1) because it might attract specialized researchers to the Slicer community 2) because it showcases the real power of Slicer to be customized to a number of different applications.</p>
<p><a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/rkikinis">@rkikinis</a> <a class="mention" href="/u/jcfr">@jcfr</a> anything to add to this opinion?</p>

---

## Post #29 by @ljod (2017-09-18 22:10 UTC)

<p>Yes I agree that we settled on the goal was to provide visibility to “packages” and showcase Slicer’s usefulness as a platform rather than to focus on the dissemination mechanism. Our original idea was that an extension or distribution with sufficient user base, documentation, website, etc. can be featured, and this will benefit all of us.</p>
<p>As I remember we thought Slicer Solutions was a good name, to remove the focus from the dissemination method. What do you think?</p>

---

## Post #30 by @lassoan (2017-09-18 22:48 UTC)

<p>I like “Slicer solutions” to refer to group of features and related documentation etc. It make sense to use this term even if there is no specialized installer.</p>
<p>“Distribution” word is good for referring to the specialized installation packages.</p>
<p>It would be important to feature distributions on the Slicer download page and preferably include them in the download stats. Have you talked to <a class="mention" href="/u/mhalle">@mhalle</a> about this to see if this is feasible?</p>

---

## Post #31 by @lassoan (2017-09-18 22:54 UTC)

<p>As I think about this more, I like the “solutions” concept a lot. If user clicks a solution then we could show a page with some nice pictures about typical use cases, instructions about how to set up (either download a special distribution or download Slicer and install extensions), tutorials, sample data sets, etc.</p>

---

## Post #32 by @bpaniagua (2017-09-19 00:35 UTC)

<p>Great! I am glad we all agree on SlicerSolutions as possible branding, since this was the initial plan. I will incorporate this change tomorrow and send the link again for review.</p>

---

## Post #33 by @bpaniagua (2017-09-19 18:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/rkikinis">@rkikinis</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>New version  <a href="https://bpaniagua.github.io/slicer.org/">https://bpaniagua.github.io/slicer.org/</a></p>
<ol>
<li>change of branding from SlicerDistributions to SlicerSolutions</li>
<li>improving Tooltips on the landing page so it is explicitly mentioned what the slicer solution is about early on (clinical vs methodological, extension or customized package)</li>
</ol>

---

## Post #34 by @fedorov (2017-09-19 21:42 UTC)

<p>What is the process of deciding whether “X” can be called “a SlicerSolution” or not?</p>

---

## Post #35 by @bpaniagua (2017-09-20 12:53 UTC)

<p>People involved in the SlicerVerse project during the Winter Project Week 2017 decided there will be some sort of voting process that will score/evaluate the candidate solution in base to certain criteria. I am just trying to recall discussion points and thinking out loud, but probably we can formulate all this.</p>
<p>Ideas about criteria:</p>
<ul>
<li>Provides service to an specific community (clinical/methodological)</li>
<li>Provides a processing pipeline from beginning to end</li>
<li>Has a support system: a dedicated PI/coordinator, a website, documentation/tutorials etc</li>
</ul>
<p>We have not yet decided who will be the people making this decision, but it would make sense to collect any SlicerSolution candidates during the year (maybe they have to send a form that can be provided in the website) and decide if they are provided with visibility in the landing page after a meeting at either of the project weeks (that happen twice a year).</p>
<p>What do you think?</p>

---

## Post #36 by @jcfr (2017-09-25 17:55 UTC)

<p>Here is a PR with the changes of <a class="mention" href="/u/bpaniagua">@bpaniagua</a>: <a href="https://github.com/Slicer/slicer.org/pull/7">https://github.com/Slicer/slicer.org/pull/7</a></p>
<p>If there are no objection, we would like to move forward with the integration later this afternoon.</p>

---

## Post #37 by @lassoan (2017-09-25 19:14 UTC)

<p>LGTM for now. We should work on creating “solution” pages, based on the same template, such as a short intro describing the scope, list a couple of use cases with nice pictures, etc. and link to the external website. That would allow users quickly browse through what solutions are available.</p>

---

## Post #38 by @bpaniagua (2017-09-25 19:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, wouldnt that be redundant? SlicerSolutions need to have a page to be included within the landing page.<br>
That external website should have all the information necessary.</p>
<p>I believe this is something we should enforce before a solution is provided presence in the landing page.</p>

---

## Post #39 by @lassoan (2017-09-25 19:51 UTC)

<p>No, it would not be redundant. It would not be feasible to maintain a uniform design among solution overview pages if they were hosted on different websites (each using different technologies - jekyll, WordPress, Drupal,…). As a prospective user, I would like to browse through these solutions easily, so overview pages should follow the same template and have “go to previous/next solution” link on them.</p>
<p>Update of overview pages should be a very lightweight process: if you save send a PR with some changes of your own solution’s overview page, then it would be merged very quickly, almost automatically.</p>

---

## Post #41 by @lassoan (2019-01-13 14:31 UTC)

<p>Yes, the plan is about what you described. Anything that is specific to a software version (such as user and developer manuals) will be hosted on readthedocs. Documentation that is common to all versions (main page, intro, events, use cases, etc) will probably remain hosted on a wiki-like website (most likely stored on github).</p>

---

## Post #43 by @jcfr (2020-04-24 19:24 UTC)

<p>To follow up this, the re-design of the page has been official added to Kitware team design queue. Stay tuned for some updates.</p>
<p>For now, the goal will be to re-design both the main landing page <a href="https://slicer.org">https://slicer.org</a> and <a href="https://download.slicer.org">https://download.slicer.org</a></p>

---

## Post #44 by @jcfr (2021-03-26 18:12 UTC)

<p>Et voila, thanks to the time, feedback and contributions of many, the new landing page is now live !</p>
<p>See <a href="https://slicer.org">https://slicer.org</a></p>
<p>Do not hesitate to reply here with questions or suggestions to improve it.</p>
<p>To learn more about the infrastructure, see <a href="https://github.com/Slicer/slicer.org#readme">https://github.com/Slicer/slicer.org#readme</a></p>
<p>Related discussions:</p>
<ul>
<li><a href="https://github.com/Slicer/slicer.org/pull/16">https://github.com/Slicer/slicer.org/pull/16</a>: This is the pull request where we have been iterating over the design since July 2020.</li>
<li><a href="https://discourse.slicer.org/t/proposed-new-slicer-logo/11295:">https://discourse.slicer.org/t/proposed-new-slicer-logo/11295:</a> Discourse post where we discussed updating the new Slicer logo</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55c1a8548d90a6b2338be543334574c071c84c11.png" alt="image" data-base62-sha1="ceDuEivxoxIsek9j6s88kwGrUe5" width="672" height="414"></p>

---
