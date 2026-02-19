---
topic_id: 7332
title: "Sequences Extension With Custom Build"
date: 2019-06-27
url: https://discourse.slicer.org/t/7332
---

# Sequences extension with custom build

**Topic ID**: 7332
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/sequences-extension-with-custom-build/7332

---

## Post #1 by @MattTroke (2019-06-27 03:30 UTC)

<p>I am developing a custom build of slicer based on the master-410 branch (I override the revision number to 28257 to match the 4.10.2 release and enable the extension manager). I would like to use the Sequences extension, but in my custom build, it doesn’t seem to work. I can load a sample data set, and the volume/slices appear, but the sequence will not play. I have confirmed that the downloaded 4.10.2 version of slicer works correctly (with the same downloaded extension). Is there something else I’m missing that makes my build differ from the officially released 4.10.2 version? I also am using a modified VTK (my VTK repo is based off of the “slicer-v8.2.0-2018-10-02-74d9488523” branch) and CTK. Differing cmake configuration?</p>
<p>Thanks,<br>
Matt</p>

---

## Post #2 by @jcfr (2019-06-27 03:35 UTC)

<blockquote>
<p>developing a custom build of slicer based on the master-410 […] use the Sequences extension […] doesn’t seem to work</p>
</blockquote>
<p>Instead of installing the Sequence extension using the extension manager, I suggest you build the extension, this will ensure the ABI is consistent.</p>
<p>After building the extension locally against your custom build of Slicer, you could  start Slicer from the Sequence build tree executing the <code>SlicerWithSequence</code> launcher.</p>

---
