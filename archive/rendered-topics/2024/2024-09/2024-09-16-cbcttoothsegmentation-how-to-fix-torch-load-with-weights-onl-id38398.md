# CBCTToothSegmentation: How to fix "torch.load with weights_only=False"

**Topic ID**: 38398
**Date**: 2024-09-16
**URL**: https://discourse.slicer.org/t/cbcttoothsegmentation-how-to-fix-torch-load-with-weights-only-false/38398

---

## Post #1 by @Bay_6 (2024-09-16 11:42 UTC)

<p>When I work with the extension <a class="hashtag-cooked" href="/tag/extensions-manager" data-type="tag" data-slug="extensions-manager" data-id="9"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>extensions-manager</span></a> CBCTToothSegmentation, the below error occur. Which file do I need to fix and how to do with it. It seems to be a python problem and I searched some solution but it did not work.</p>
<p>Slicer version：Slicer 5.7.0-2024-09-05</p>
<blockquote>
<p>You are using torch.load with weights_only=False (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See <a href="https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models" class="inline-onebox" rel="noopener nofollow ugc">pytorch/SECURITY.md at main · pytorch/pytorch · GitHub</a> for more details). In a future release, the default value for weights_only will be flipped to True. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via torch.serialization.add_safe_globals. We recommend you start setting weights_only=True for any use case where you don’t have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.</p>
</blockquote>

---

## Post #2 by @lassoan (2024-09-16 11:45 UTC)

<p>This does not sound like an error (just a warning that some unsecure feature will be disabled in the future).</p>
<p>You can reach developers in the <a href="https://github.com/KitwareMedical/SlicerCBCTToothSegmentation/issues">repository’s issue tracker</a>. You will need to provide information about what did you do exactly, on what operating system, using what hardware (CPU, GPU, RAM, …), on what data, how did you get this error message, and post not just a selected message but the full log.</p>

---
