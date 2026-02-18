# Slicer cli starts before the last cli ends

**Topic ID**: 23056
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/slicer-cli-starts-before-the-last-cli-ends/23056

---

## Post #1 by @hotsen (2022-04-20 17:00 UTC)

<p>Hi all,<br>
I got the following issue with slicer.cli.run. The first loop generates 3 registration output volumes, then the second loop extracts features from those 3 output volumes. But the last extraction always went wrong (the other two extractions worked fine), it starts before the last registration finished and get no result. It seems like once the slicer.cli in the first loop gets the last input params and starts to run, the second loop will start, and the second loop will finish before the last run of first loop. Something I did wrong here? <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<pre><code class="lang-auto">for i in range(3):
  setting = settings[i]
  slicer.cli.run(antsRegistration(setting), wait_for_completion=True)


for i in range(3):
  slicer.cli.run(SlicerRadiomics(), wait_for_completion=True)
</code></pre>

---

## Post #2 by @pieper (2022-04-20 17:22 UTC)

<p>Not sure - it looks like that should work.  It could help for you to create a full self-contained example that replicates the problem in isolation.  I.e. downloads sample data, creates a simple threshold segmentation, and runs registration/radiomics.  Ideally this would be in the form of a test that could be included in nightly testing so that once any underlying issues are fixed we will be able to see that no regressions are introduced in the future.</p>

---
