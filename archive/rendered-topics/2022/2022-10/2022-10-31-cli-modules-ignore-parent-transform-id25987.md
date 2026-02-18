# CLI modules ignore parent transform

**Topic ID**: 25987
**Date**: 2022-10-31
**URL**: https://discourse.slicer.org/t/cli-modules-ignore-parent-transform/25987

---

## Post #1 by @lassoan (2022-10-31 19:09 UTC)

<p>It seems confusing that CLI modules ignore the parent transform and users need to harden the transform to get the results that they expect. See this discussion for a recent example:</p>
<aside class="quote quote-modified" data-post="17" data-topic="25786">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/multiple-partial-volumes-reconstruction/25786/17">Multiple partial volumes reconstruction</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Is there a way to automatically add a warning of some kind to CLI modules if a user tries to select a transformed node as an input?  It is not always obvious to end users that a module they select is a CLI module behind the scenes, and even if they did know, it is not obvious that soft transforms are ignored for these modules.  I’ve unexpectedly run into that multiple times over the years before I learned to check for it (so much so that, as you can see above, I assumed that it might be a Slice…
  </blockquote>
</aside>

<ul>
<li>Does anyone know the reason why CLI modules are implemented like this?</li>
<li>Should we transform to/from RAS space before sending a node to a CLI module and convert outputs from RAS to the node’s parent transform’s space?</li>
<li>Or should we at least display a warning when a node under a transform is used as CLI module input or output?</li>
</ul>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #2 by @pieper (2022-10-31 19:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="25987">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does anyone know the reason why CLI modules are implemented like this?</p>
</blockquote>
</aside>
<p>As I recall transforms were being added and improved around the same time CLIs were being developed and I think this feature just never got implemented.  It would definitely be nice to handle this automatically at the CLI GUI/logic layer by assuming that CLIs expect all their inputs to be in the same space (RAS).</p>
<p>We could do this by extending the node combo box to have a method like currrentNodeInWorldSpace that would do the clone/harden step if needed.  If a transformable node has a nonlinear transform parent, then the combo box could have a submenu that selects a reference volume to define the desired resampling (and maybe the option not to delete the clone volume in case you want to reuse it).</p>

---
