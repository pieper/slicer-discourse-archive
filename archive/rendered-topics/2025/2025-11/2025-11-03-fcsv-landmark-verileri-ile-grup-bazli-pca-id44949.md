---
topic_id: 44949
title: "Fcsv Landmark Verileri Ile Grup Bazli Pca"
date: 2025-11-03
url: https://discourse.slicer.org/t/44949
---

# Fcsv Landmark Verileri ile Grup Bazlı PCA

**Topic ID**: 44949
**Date**: 2025-11-03
**URL**: https://discourse.slicer.org/t/fcsv-landmark-verileri-ile-grup-bazli-pca/44949

---

## Post #1 by @Esra_Karacan (2025-11-03 16:25 UTC)

<p>Hello,</p>
<p>I am comparing my archaeological and modern mandible data. I saved my landmark sets in fcsv format. I would like to include male and female individuals as separate groups for PCA analysis. Could you guide me on how to create sex-based PCA results by separating my fcsv files into groups? Furthermore, do you have any suggestions on the steps I should follow to obtain PCA comparisons between groups?</p>
<p>Thank you very much in advance…</p>

---

## Post #2 by @muratmaga (2025-11-03 16:35 UTC)

<p>If you follow the [<strong>Step</strong> <span class="hashtag-raw">#7</span> of this tutorial](<a href="https://github.com/SlicerMorph/Tutorials/blob/main/GPA_1/README.md#setup-analysis" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/GPA_1/README.md at main · SlicerMorph/Tutorials · GitHub</a>), you can create a covariate file for your specimens. Then in GPA module, you can choose the Sex factor (you created) as an coloring option for the PCA plot.</p>
<p>However, there is no option to subset your data via factors (like Sex) and analyze them separately in GPA module. You can organize your data that way (i.e., males in folder, females in another).</p>

---
