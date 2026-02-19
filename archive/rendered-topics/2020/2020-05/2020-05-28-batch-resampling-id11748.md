---
topic_id: 11748
title: "Batch Resampling"
date: 2020-05-28
url: https://discourse.slicer.org/t/11748
---

# Batch resampling

**Topic ID**: 11748
**Date**: 2020-05-28
**URL**: https://discourse.slicer.org/t/batch-resampling/11748

---

## Post #1 by @HugoTrentesaux (2020-05-28 14:09 UTC)

<p>Is there a way to use the transform.h5 file from a script to apply the same transform on a batch of volumes? The easiest way would be directly from bash script like:</p>
<pre><code class="lang-bash">$ for i in $list;
do Slicer resample \
--transform transform${i}.h5 \
--fixed source${i}.nrrd \
--moving target${i}.nrrd;
done;
</code></pre>
<p>A python call would also make it, but I can not find documentation about that…</p>

---

## Post #2 by @pieper (2020-05-28 19:06 UTC)

<p>You can do pretty much exactly that in bash using slicer CLI modules as executables using the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Launcher">launcher</a>.</p>
<p>You can also do <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">something similar</a> in python if you would rather.</p>

---

## Post #3 by @HugoTrentesaux (2020-05-29 09:19 UTC)

<p>Thanks for pointing me to the relevant documentation.</p>
<p>The thing I needed was</p>
<pre><code class="lang-bash">Slicer --launch BRAINSResample --help
</code></pre>
<p>And the command to run</p>
<pre><code class="lang-bash">Slicer --launch BRAINSResample \
--inputVolume source_1.nrrd \
--outputVolume reformated_1.nrrd \
--referenceVolume target_1.nrrd \
--warpTransform transform_1.h5
</code></pre>

---

## Post #4 by @pieper (2020-05-29 11:45 UTC)

<p>cool - let us know what you find.  The log file will show the parameters used when you invoke the cli module via the gui.</p>

---
