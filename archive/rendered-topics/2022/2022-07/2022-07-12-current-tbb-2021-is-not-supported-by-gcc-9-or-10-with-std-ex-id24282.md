# Current TBB 2021 is not supported by GCC 9 or 10 with `std::execution`

**Topic ID**: 24282
**Date**: 2022-07-12
**URL**: https://discourse.slicer.org/t/current-tbb-2021-is-not-supported-by-gcc-9-or-10-with-std-execution/24282

---

## Post #1 by @keri (2022-07-12 09:27 UTC)

<p>Hi,</p>
<p>Slicer recently moved to TBB 2021 version.<br>
I just figured out that this version is not compatible with neither GCC 9 or 10 (<a href="https://stackoverflow.com/questions/65521032/cant-run-c17-parallel-algorithms-with-gcc-on-linux" rel="noopener nofollow ugc">issue link1</a> and <a href="https://community.intel.com/t5/Intel-oneAPI-Threading-Building/tbb-task-has-not-been-declared/td-p/1254418" rel="noopener nofollow ugc">issue link2</a>) when using <a href="https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag" rel="noopener nofollow ugc">std::execution</a> to paralelize <code>stl</code> algorithms.</p>
<p>As I know GCC 9.3 fully supports C++17 but if you decide to use <code>std::execution</code> within Slicer then you will likely get an error mentioned in the links above.<br>
As I understood GCC 11 and 12 support TBB 2021.</p>
<p>Maybe we should allow the developper to choose the desired TBB version? Like we had with VTK 8 and VTK 9.</p>

---

## Post #2 by @lassoan (2022-07-12 20:13 UTC)

<p>Do you see any explanation in the commit that made the TBB library version hardcoded about why it was made? If no specific reason is given then most likely it was made to just make things simpler. If there is a confirmed need to make it more configurable then that can justify the additional complication.</p>

---

## Post #3 by @jcfr (2022-07-12 20:19 UTC)

<blockquote>
<p>any explanation in the commit that made the TBB library version hardcoded about why it was made</p>
</blockquote>
<p>For reference, see <a href="https://github.com/Slicer/Slicer/commit/3ea8ba4b4e0981ea05677df65bc3e7c9819c1d5b" class="inline-onebox">COMP: Update TBB from 2019_U9 to 2021.5.0 · Slicer/Slicer@3ea8ba4 · GitHub</a></p>

---

## Post #4 by @keri (2022-07-12 20:23 UTC)

<p>I see now.<br>
Probably it is worth to leave it as is.</p>

---
