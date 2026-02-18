# Github for issue tracking

**Topic ID**: 10678
**Date**: 2020-03-13
**URL**: https://discourse.slicer.org/t/github-for-issue-tracking/10678

---

## Post #1 by @lassoan (2020-03-13 17:08 UTC)

<p>Now that we have moved to github, we need to update our process to capabilities of github’s issue tracker.</p>
<p>I’ve collected all the fields that were stored in Mantis and a proposal for how we could manage them from now on. I’ve tried to keep things simple (we can always make things more complex if needed) and be similar to Github’s defaults/recommendations, and other projects that our community uses (such as ITK).</p>
<p>Nothing to do (equivalent feature is available in github):</p>
<ul>
<li>Reporter: (automatic username)</li>
<li>Assigned to: (username)</li>
<li>Target version: backlog, Slicer-4.11.0, Slicer-5.1.0 =&gt; in github milestone</li>
<li>Fixed in version: Slicer-4.11.0, Slicer-5.1.0, Slicer-4.10.2, … =&gt; in github milestone (if issue is fixed but then it turns out to be not fixed after all then a new issue should be created in the new milestone)</li>
</ul>
<p>Move to issue reporting template:</p>
<ul>
<li>Platform: (free text)</li>
<li>Product version: backlog, Slicer-4.11.0, Slicer-5.1.0, Slicer-4.10.2, …</li>
<li>OS version: (free text)</li>
<li>OS: (free text)</li>
<li>Reproducibility: always, sometimes, random, have not tried, unable to reproduce, N/A</li>
<li>Description</li>
<li>Steps to reproduce</li>
<li>Additional information</li>
</ul>
<p>Move to labels (see github default labels: <a href="https://help.github.com/en/github/managing-your-work-on-github/about-labels#using-default-labels">https://help.github.com/en/github/managing-your-work-on-github/about-labels#using-default-labels</a>)</p>
<ul>
<li>Priority: none, low, normal, high, urgent, immediate =&gt; priority:low, priority:normal, priority:high, priority:urgent</li>
<li>Severity: feature, trivial, text, tweak, minor, major, crash, block =&gt; this is a mix between type, priority, and severity; since we will have priority labels, probably it would be enough to use default labels: type:bug, type:enhancement</li>
<li>Status: new, feedback, acknowledged, confirmed, assigned, resolved, closed =&gt; use issue status (open/close) and github default labels:  status:duplicate, status:invalid, status:question, status:wontfix + I would add status:in-progress (to indicate that the issue is not just assigned to someone but that person is actually working on that)</li>
</ul>
<p>Discontinue:</p>
<ul>
<li>Category: Core: Base Code, Core: Building (Cmake, Superbuild), Core: GUI, …. =&gt; this was used for automatic assignment of the issue. This was not very well defined, did not work very well (partially because email notifications were broken in Mantis), it would not be trivial to implement in github, and not that important anymore (since extensions are managed independently).</li>
<li>Resolution: open, fixed, reopened, unable to reproduce, not fixable, duplicate, no change required, suspended, won’t fix =&gt; these can be described in notes or associated commit comments</li>
</ul>
<p>Any comments and suggestions are welcome. If we reach a general agreement then we can create labels and bug report and feature request templates accordingly.</p>

---

## Post #2 by @pieper (2020-03-13 18:04 UTC)

<p>Makes sense to me - thanks for working through this.</p>
<p>We want to use the issue reporting templates carefully.  I find that unfortunately many of the templates are too long and full of instructions, but then users don’t fill them out.  If you are watching the issues you end up with a long email that needs to be visually scanned in order to see if there is any non-template text it at all.</p>
<p>So let’s just use the fields you have laid out as the template.</p>
<p>We can also have multiple issue templates for different kinds of issue.  I’m not sure yet how we can best make use of that feature.</p>

---

## Post #3 by @lassoan (2020-03-13 18:53 UTC)

<p>Agreed. Long templates and many issue labels are quite annoying.</p>
<p>It makes sense to have different template for bugs and features (reproducibility, Slicer versions, etc. are not relevant for features). The issue template could be as simple as this:</p>
<pre><code class="lang-nohighlight">Slicer version: Slicer-4.??.?-YYYY-MM-DD
Operating system: Windows / Mac / Linux + version
Description:

What you did, what you expected to happen, and what happened instead?
More information: https://github.com/Slicer/Slicer/blob/master/CONTRIBUTING.md#report-issues
</code></pre>

---

## Post #4 by @Sam_Horvath (2020-03-16 19:35 UTC)

<p>One thing that needs to happen is to go through the backlog and triage / close issues on the git repo.  A large number are currently already fixed / invalid (extension issue, etc)</p>

---

## Post #5 by @lassoan (2020-03-16 21:44 UTC)

<p>I’ve added bug report and feature request templates - see <a href="https://github.com/Slicer/Slicer/issues/new/choose">https://github.com/Slicer/Slicer/issues/new/choose</a></p>
<p>Feel free to submit pull requests or discuss here if you have any suggestions how to improve them.</p>

---
