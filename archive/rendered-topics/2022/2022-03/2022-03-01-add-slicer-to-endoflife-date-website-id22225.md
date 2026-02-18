# Add slicer to endoflife.date website?

**Topic ID**: 22225
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/add-slicer-to-endoflife-date-website/22225

---

## Post #1 by @jcfr (2022-03-01 05:19 UTC)

<h3><a name="p-74727-overview-1" class="anchor" href="#p-74727-overview-1" aria-label="Heading link"></a>Overview</h3>
<p>The website is a useful resource to find out which version is current, actively maintained, receiving  security patches, …</p>
<p>Here are few examples:</p>
<ul>
<li><a href="https://endoflife.date/blender">https://endoflife.date/blender</a>  (contributed through <a href="https://github.com/endoflife-date/endoflife.date/pull/374">PR endoflife.date#374</a>)</li>
<li><a href="https://endoflife.date/python">https://endoflife.date/python</a></li>
<li><a href="https://endoflife.date/qt">https://endoflife.date/qt</a></li>
<li><a href="https://endoflife.date/nvidia-gpu">https://endoflife.date/nvidia-gpu</a></li>
</ul>
<h3><a name="p-74727-slicer-release-cycles-list-2" class="anchor" href="#p-74727-slicer-release-cycles-list-2" aria-label="Heading link"></a>Slicer release cycles, list, …</h3>
<p>We could basically transition the information of these pages into something more formal:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Release_Details" class="inline-onebox">Release Details - Slicer Wiki</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation" class="inline-onebox">Documentation - Slicer Wiki</a></li>
</ul>
<p>The idea could be to :</p>
<ul>
<li>have an authoritative document [1] listing all releases hosted on our GitHub repository</li>
<li>render it on our website similarly to what is done one the <code>endoflife</code> website by levering the relevant template [2]</li>
</ul>
<p>or we could simply redirect to the endoflife and just have a PR automatically created against <a href="https://github.com/endoflife-date/endoflife.date">https://github.com/endoflife-date/endoflife.date</a> when we modify our version.</p>
<p>Reading this is also informative: <a href="https://endoflife.date/recommendations" class="inline-onebox">Recommendations for maintainers | endoflife.date</a></p>
<h3><a name="p-74727-questions-3" class="anchor" href="#p-74727-questions-3" aria-label="Heading link"></a>Question(s)</h3>
<p>Would that be helpful ?</p>
<p>Any other suggestions ?</p>
<hr>
<p>[1]: For example, it could be stored like as a markdown like <a href="https://raw.githubusercontent.com/endoflife-date/endoflife.date/master/products/blender.md">blender.md</a><br>
[2]: <a href="https://github.com/endoflife-date/endoflife.date/blob/master/_layouts/post.html">https://github.com/endoflife-date/endoflife.date/blob/master/_layouts/post.html</a></p>

---

## Post #2 by @jamesobutler (2022-03-01 13:23 UTC)

<p>The endoflife sites are nice easy to read websites if there are going to be multiple minor versions of Slicer supported at any given time. Does Slicer plan to start supporting multiple minor released versions? As far as I have observed there has typically only been 1 stable version and then the preview release. If there is a bug or minor improvement it has gone into the preview release and there really hasn’t been backporting of items to continue support for a released version. I believe version 4.10.2 was still fairly similar to the main <code>master</code> branch at the time of its release.</p>
<p>It would seem the multiple supported versions would increase maintenance duties if there is someone who has the time to cut more frequent patch releases to truly continue support for multiple versions. Using endoflife you would specify at time of a new release when it go endoflife, so you would need to keep official support for that version during that entire time and also have its replacement released by then. The dates could be changed, but that should probably be avoided if possible.</p>
<p>As it relates to documentation of release date, release notes, announcements, etc that would all be good to have in the GitHub Releases area. I typically check dates of tags/releases and look for changes in that area for other projects.</p>

---

## Post #3 by @pieper (2022-03-01 14:12 UTC)

<p>+1 for a clearer support policy for slicer releases to make things transparent for users but also for extension developers/users.  I agree we should try to keep things simple, and to be realistic somewhat flexible given that we don’t have a lot of dedicated resources.</p>

---

## Post #4 by @lassoan (2022-03-01 17:36 UTC)

<p>I agree that we should document more clearly what Slicer releases are supported. The <a href="https://github.com/Slicer/Slicer/wiki">GitHub wiki</a> could be a good place for it.</p>
<p>Contents of <a href="https://www.slicer.org/wiki/Release_Details#Slicer_4.11" class="inline-onebox">Release Details - Slicer Wiki</a> and <a href="https://www.slicer.org/wiki/Documentation" class="inline-onebox">Documentation - Slicer Wiki</a> pages could be moved to <a href="https://github.com/Slicer/Slicer/releases">GitHub releases</a>.</p>
<p>The <a href="https://endoflife.date/">https://endoflife.date/</a> website contains a tiny collection of about 90 projects (just in comparison, there are 28 million public projects on GitHub). The selection seems completely random - operating systems, applications, frameworks, libraries and not comprehensive or organized in any way. I don’t think we are missing out on anything by not listing Slicer there.</p>

---
