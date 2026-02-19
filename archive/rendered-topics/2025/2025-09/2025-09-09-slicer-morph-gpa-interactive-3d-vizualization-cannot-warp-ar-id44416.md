---
topic_id: 44416
title: "Slicer Morph Gpa Interactive 3D Vizualization Cannot Warp Ar"
date: 2025-09-09
url: https://discourse.slicer.org/t/44416
---

# Slicer Morph GPA | Interactive 3D vizualization | Cannot warp around PCs

**Topic ID**: 44416
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/slicer-morph-gpa-interactive-3d-vizualization-cannot-warp-around-pcs/44416

---

## Post #1 by @macorreia42 (2025-09-09 15:49 UTC)

<p>Operating system: Windows 11 Home<br>
Slicer version: 5.8.1 r33241 / 11eaf62<br>
Expected behavior: reference model warps around PCs<br>
Actual behavior: Critical error TypeError: unsupported operand type(s) for -: ‘str’ and ‘int’</p>
<p>Hello,<br>
My 3DSlicer and SlicerMorph are up to date. The full error log is</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Users/corre/AppData/Local/slicer.org/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/GPA.py”, line 1777, in onSelect<br>
indexToRemove.append(self.LMExclusionList[i]-1)<br>
TypeError: unsupported operand type(s) for -: ‘str’ and ‘int’</p>
</blockquote>
<p>For context, my workflow is: place landmarks on 3Dslicer, export as .mrk.json, import into R using <code>SlicerMorphR::read.markups.json()</code>, convert into into an array 3D (code below in case that’s the source), estimate missing landmarks using <code>geomorph::estimate.missing()</code>, conduct GPA using <code>geomorph::gpagen()</code> and PCA using <code>geomorph::gm.prcomp()</code> on aligned coordinates, and export using <code>SlicerMorphR::geomorph2slicermorph2()</code>, and import into 3D slicer using the Load previous analysis. The subjects load and I can ExploreData/Results normally, and the output from <code>geomorph2slicermorph2()</code> looks “normal” to me.</p>
<p>I’m following this <a href="https://github.com/SlicerMorph/SlicerMorphR" rel="noopener nofollow ugc">tutorial</a>, except for the transformation to array (because mine is differently sized and I made it in a more intuitive way for me). ChatGPT suggested I mess with the Python file (<code>GPA.py</code>), by “casting the string to int before subtracting”, but I don’t know Python and I thought I’d try here first.</p>
<p>Very recent user of 3DSlicer and my first time posting. Thankful for any help.</p>
<p>My code for creating the array3d:</p>
<p><code>json_paths ← list.files(raw_dir, pattern = “\.json$”, full.names = TRUE)</code><br>
<code>specimen_ids ← tools::file_path_sans_ext(basename(json_paths))</code></p>
<pre><code class="lang-auto">4) Read JSON into numeric matrices
read_lmk_matrix ← function(path) {
m ← SlicerMorphR::read.markups.json(path)
m ← as.matrix(m)
m ← apply(m, 2, as.numeric)
if (is.null(colnames(m))) colnames(m) ← c(“X”, “Y”, “Z”)
m
}
landmark_list ← purrr::map(json_paths, read_lmk_matrix) |&gt; purrr::set_names(specimen_ids)

5) Build array3d
p ← nrow(landmark_list[[1]])
k ← 3
n ← length(landmark_list)

array3d ← array(
NA_real_,dim = c(p, k, n),
dimnames = list(
landmark = seq_len(p),
coord    = c(“X”, “Y”, “Z”),
specimen = names(landmark_list)
)
)
for (i in seq_along(landmark_list)) array3d[, , i] ← landmark_list[[i]]
storage.mode(array3d) ← “double”
</code></pre>
<p>This produces an object like this</p>
<pre><code class="lang-auto">str(array3d)
 num [1:21, 1:3, 1:11] 25.4 23.3 22.6 23.1 25.5 ...
 - attr(*, "dimnames")=List of 3
  ..$ landmark: chr [1:21] "1" "2" "3" "4" ...
  ..$ coord   : chr [1:3] "X" "Y" "Z"
  ..$ specimen: chr [1:11] "ILH_Zvejnieki_34.107.217.mrk" "ILH_Zvejnieki_34.115.228.mrk" "ILH_Zvejnieki_34.116.229.mrk" "ILH_Zvejnieki_34.118.328.mrk" ...
</code></pre>

---

## Post #2 by @muratmaga (2025-09-09 16:43 UTC)

<p>I can’t replicate this error with SlicerMorph SampleData. Can you:</p>
<ol>
<li>Go to extension manager, click <strong>check for updates</strong> and see if there is a more recent SlicerMorph version and tr</li>
<li>Share your data.</li>
</ol>

---

## Post #3 by @macorreia42 (2025-09-09 16:52 UTC)

<p>UPDATE: If I go to the <code>analysis.json</code> file and change<code>“ExcludedLM”: "[]"</code> to <code>“ExcludedLM”: []</code>and<code>“SemiLandmarks”: "[]"</code> to <code>“SemiLandmarks”: []</code>, it works.</p>
<p>yes, it’s up to date, following Extensions &gt; Check for Updates.<br>
Here is a <a href="https://drive.google.com/drive/folders/1ePJXx6_8vSkhaXldT9fU47sHxkxZgl1M?usp=drive_link" rel="noopener nofollow ugc">link</a> for my R directory backup, in the data folder, there’s some .mrk.json in raw and the geomorph2slicermorph2() output is in derived data. I’d share the GitHub, but it doesn’t have the raw data.</p>
<p>Thank you</p>

---

## Post #4 by @muratmaga (2025-09-10 02:36 UTC)

<p>I am sorry, I am a bit confused. Is this error coming during the GPA  of original data in SlicerMorph or when you are trying to move results from geomorph to SlicerMorph using SlicerMorphR?</p>

---

## Post #5 by @macorreia42 (2025-09-10 06:11 UTC)

<p>The error log is from SlicerMorph when setting up the interactive 3D visualization. So, I’ve already exported the GPA+PCA results from geomorph using SlicerMorphR, uploaded them into SlicerMorph, and I’m trying to visualise it, producing that error log.<br>
However, the workaround above involves editing the analysis.json file produced via SlicerMorphR, by removing the ““ around the square brackets, <strong>before</strong> uploading the GPA+PCA into 3DSlicer/SlicerMorph.<br>
It’s not ideal so you have any input, it’d be appreciated.</p>

---

## Post #6 by @macorreia42 (2025-09-10 08:01 UTC)

<p>Here is a <a href="https://drive.google.com/drive/folders/1N_XMV7bAv9eFuZqyj9muf_UkeAKMhqlH?usp=sharing" rel="noopener nofollow ugc">link</a> for some .mrk.json data, and for the GitHub <a href="https://github.com/macorreia42/zvej_mandibles.git" rel="noopener nofollow ugc">repo</a><br>
(I had to break the previous link)</p>

---

## Post #7 by @muratmaga (2025-09-10 15:20 UTC)

<p>landmark configuration includes missing landmarks, so I can’t run them with GPA. I presume you used geomorph to estimate those. I am not sure why you are getting an extra set of ““ from the geomorph2slicermorph2 to function, as it doesn’t happen for me.</p>
<p>I am glad you figured out your work around.</p>

---

## Post #8 by @macorreia42 (2025-09-12 10:54 UTC)

<p>I deleted the files with missing landmarks, if you have time/patience to try again, but yes, it seems that the issue is on the geomorph2slicermorph2 output.</p>

---
