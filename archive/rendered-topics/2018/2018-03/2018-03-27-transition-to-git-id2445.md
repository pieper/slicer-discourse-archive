---
topic_id: 2445
title: "Transition To Git"
date: 2018-03-27
url: https://discourse.slicer.org/t/2445
---

# Transition to Git

**Topic ID**: 2445
**Date**: 2018-03-27
**URL**: https://discourse.slicer.org/t/transition-to-git/2445

---

## Post #1 by @jcfr (2018-03-27 20:52 UTC)

<p>Hi,</p>
<p>Current status associated with the transition is documented <a href="https://www.slicer.org/wiki/Documentation/Labs/TransitionToGit">here</a> on the Slicer wiki.</p>
<p>On of the task is to take that opportunity to filter the history and remove the large object (aka files) so that checking out the Slicer source tree is very fast.</p>
<p>To identify the large blobs, a <a href="https://gist.github.com/jcfr/4348af13d2c8931daeab4ff9ab73e14b#gistcomment-2393756">script</a> was created.</p>
<p>Output looks like this:</p>
<pre><code class="lang-nohighlight">$ cd Slicer
$ git_list_largest_file_from_history.sh 350
        size    pack_size sha                                      location
       55MiB        55MiB 2cadcca7dd65c008c03ca0786ed3b02ad86cc900 Modules/Meshing/Testing/Data/CA05042124RFinal.img.gz
       22MiB       4.9MiB 56760af8680e9ff7e857a97b384fb9c0b974ea11 Modules/Meshing/Testing/Data/lumbar_smoothed_04075.stl
       15MiB       4.6MiB 0b64a9fbd9a0b02f65c726da71b7128013b94e3a Modules/CLI/RigidRegistration/Data/Baseline/RigidRegistrationTest02.nrrd
       13MiB        13MiB d8ffda6d56ebd27758e54d3550dd64ff362a9589 Applications/CLI/BRAINSTools/BRAINSCommonLib/TestData/OutDefField_orientedImage.nii.gz
       [....]
</code></pre>
<p>The complete list is <a href="https://gist.github.com/jcfr/93fe51974d9db8ef55a6d3172c1de68d">here</a>.</p>
<p>After identifying the files to remove, there are few possible approaches that will present in a later post.</p>

---

## Post #2 by @jcfr (2018-03-28 03:33 UTC)

<p>5 posts were split to a new topic: <a href="/t/should-we-use-git-lfs-to-manage-data/2448">Should we use Git LFS to manage data?</a></p>

---
