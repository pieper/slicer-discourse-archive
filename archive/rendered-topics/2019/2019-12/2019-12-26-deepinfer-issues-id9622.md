# DeepInfer issues

**Topic ID**: 9622
**Date**: 2019-12-26
**URL**: https://discourse.slicer.org/t/deepinfer-issues/9622

---

## Post #1 by @hherhold (2019-12-26 16:10 UTC)

<p>I’m trying out DeepInfer and having a few issues. This with a Dec 20 nightly version with a recently downloaded Deepinfer module and I’ve had to make some changes to get it to work at all - First issue was ‘import Queue’ should be ‘import queue’, next issue was with sorting the list of files returned from glob() in populateLocalModels(), next is with running the test button, startswith() is looking for bytes, not a string…</p>
<p>It almost seems like DeepInfer is looking for a different version of Python?</p>
<p>This is on MacOS 10.15.1.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @jamesobutler (2019-12-26 17:56 UTC)

<p>It appears that the DeepInfer extension hasn’t been updated to be compatible with Python 3 which is used in Slicer 4.11 preview while Python 2 is used in Slicer stable 4.10.2.</p>
<p>It appears someone else reported the compatibility issue in a git issue in that extension’s repo. See <a href="https://github.com/DeepInfer/Slicer-DeepInfer/issues/13" rel="nofollow noopener">https://github.com/DeepInfer/Slicer-DeepInfer/issues/13</a></p>
<p>Follow these instructions for updating the extension <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Slicer_5.0:_Python2_to_Python3" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Slicer_5.0:_Python2_to_Python3</a></p>

---

## Post #3 by @lassoan (2019-12-26 18:32 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> it would be great if you could submit a pull request with your fixes. Ideally, the changes should be backward compatible with Python2, but if you test in only with Python3 that is useful, too.</p>
<p>Note that we are trying to move towards more generic interfaces for AI-assisted segmentation. We already have NVidia Clara interface in Segment Editor. It would be an option to add Clara interface to DeepInfer models. The advantage of this approach would be that the segmentation tool would be made available very easily to all Slicer users (without requiring docker installation).</p>

---

## Post #4 by @hherhold (2019-12-28 20:26 UTC)

<p>Right now I can only test in python 3.</p>
<p>I have it running to the point where the Docker DeepInfer process completes and writes the output nrrd file, but somewhere along the line, the plumbing between docker and slicer isn’t working right. The issue appears to be in thread_doit() - the outputs from self.executeDocker() is just {‘OutputLabel’: None}.</p>
<p>I can submit a pull request for what I’ve fixed thus far, which is just some python 2 to 3 conversions. Any insights on what might be going on in thread_doit()?</p>
<p>This is perhaps a check mark in the “Pro” column for approaches that don’t require Docker, as you’ve noted…</p>

---

## Post #5 by @lassoan (2019-12-29 02:17 UTC)

<p>Please send a pull request with your changes and submit an issue in their bugtracker.</p>

---
