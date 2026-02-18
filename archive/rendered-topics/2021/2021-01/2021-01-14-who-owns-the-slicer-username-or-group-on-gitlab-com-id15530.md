# Who owns the Slicer username or group on gitlab.com?

**Topic ID**: 15530
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/who-owns-the-slicer-username-or-group-on-gitlab-com/15530

---

## Post #1 by @jcfr (2021-01-14 20:47 UTC)

<p>I tried to create the group Slicer on <a href="http://gitbab.com">gitbab.com</a> and realized it was not available.</p>
<h4>Background</h4>
<p>While working on addressing issues related to use of Plastimatch in the SlicerRt extension, I realized a fork of plastimatch  was currently used (see <a href="https://github.com/SlicerRt/SlicerRT/blob/6a635866c34311b54fad56bb71eff9d0f203652b/SuperBuild/External_Plastimatch.cmake#L21-L24">here</a>)</p>
<p>I plan on consolidating the change and submit a merge request to the upstream repository.</p>
<p>That said, waiting these are integrated, I would like to have a staging area on Gitlab for the changes. Similarly to what we already do with VTK, ITK, … in the <a href="https://github.com/slicer" class="inline-onebox">Slicer · GitHub</a> organization.</p>
<h4>Follow up questions</h4>
<ol>
<li>
<p>Generally speaking, should we create fork of Gitlab project on GitHub ? I think we should as it streamline integration of changes in the upstream project.</p>
</li>
<li>
<p>In this particular case, since Plastimatch is made available in Slicer through SlicerRt, should we create the <code>SlicerRt</code> group on Gitlab ?</p>
</li>
</ol>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2021-01-14 21:05 UTC)

<p>I understand github forks, because it is very convenient to find all the projects in the world in one place. It is not clear to me how gitlab fork can be useful. Developers do not expect to find projects on gitlab, we do not want to get pull requests or bug reports from gitlab, we would not want any discussions to take place there, etc. Having a placeholder Slicer organization could make sense (to avoid any confusion by someone else taking that organization name and maintaining an official-looking fork, then not taking care of it properly), but other than that I would not bother much with gitlab.</p>

---

## Post #3 by @jcfr (2021-01-14 21:13 UTC)

<blockquote>
<p>Having a placeholder Slicer organization could make sense</p>
</blockquote>
<p>I created one for SlicerRt and added you as owner. I also updated the description to indicate development is happen on GitHub and added a link to it. See <a href="https://gitlab.com/slicerrt" class="inline-onebox">SlicerRT · GitLab</a></p>
<p>Since the Slicer one is not available, I couldn’t create one.</p>
<blockquote>
<p>plastimatch</p>
</blockquote>
<p>I will create a placeholder for plastimatch organization on GitHub along with a  plastimatch project, and will fork it into the SlicerRt organization.</p>

---

## Post #4 by @jcfr (2021-01-14 21:34 UTC)

<p>There is now the following placeholders:</p>
<ul>
<li><a href="https://github.com/plastimatch">https://github.com/plastimatch</a></li>
<li><a href="https://github.com/plastimatch/plastimatch">https://github.com/plastimatch/plastimatch</a></li>
</ul>
<p>These have explicit descriptions indicating that GitLab is where all development is happening.</p>
<p>In <a href="https://github.com/plastimatch/plastimatch">https://github.com/plastimatch/plastimatch</a> I also provided guidance on how to name branches in forks (aka “staging area” waiting changes are integrated in upstream project)</p>
<p>cc: <a class="mention" href="/u/gcsharp">@gcsharp</a></p>

---
