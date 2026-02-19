---
topic_id: 44540
title: "New Extension Massvision"
date: 2025-09-21
url: https://discourse.slicer.org/t/44540
---

# New Extension: MassVision

**Topic ID**: 44540
**Date**: 2025-09-21
**URL**: https://discourse.slicer.org/t/new-extension-massvision/44540

---

## Post #1 by @Amoon (2025-09-21 02:28 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=15" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"> Happy to announce the official release of <strong>MassVision</strong> extension v 1.0, now available through the 3D Slicer Extension Manager (compatible with the latest stable release, v5.8.1).</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/light_bulb.png?v=15" title=":light_bulb:" class="emoji" alt=":light_bulb:" loading="lazy" width="20" height="20"> <strong>MassVision</strong> is an end-to-end platform for AI-driven exploration and analysis of mass spectrometry imaging (MSI) data.</p>
<p>          <a href="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/MassVision/Resources/Icons/UI_logoM.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/MassVision/Resources/Icons/UI_logoM.png" width="250" height="288">
          </a>
</p>
<h2><a name="p-128618-key-features-1" class="anchor" href="#p-128618-key-features-1" aria-label="Heading link"></a>Key Features:</h2>
<ul>
<li>Data compatibility: imzML, structured CSV, hierarchical HDF5, DESI TXT images</li>
<li>Visualization: targeted (single-ion heatmap, multi-ion colormap), untargeted (global/local contrast PCA, UMAP, t-SNE), multi-pixel spectrum plotting</li>
<li>Exploration: clustering, segmentation, correlation analysis</li>
<li>Dataset generation: spatial co-localization with pathology annotations, pathology-guided spatial annotation, spectrum labeling and extraction</li>
<li>Multi-slide merge: feature alignment, peak matching</li>
<li>Preprocessing: normalization (TIC, TSC, single-ion, mean, median, RMS), spectral filtering, spatial pixel aggregation</li>
<li>Statistical analysis: ANOVA, volcano plots, boxplots</li>
<li>AI model training/validation:
<ul>
<li>Feature ranking (PLS-DA, Linear SVC, LDA)</li>
<li>Feature selection (automated, manual)</li>
<li>Data stratification (random, patient-based, cross-validation)</li>
<li>Data balancing (oversampling, undersampling)</li>
<li>Model training (PCA-LDA, Linear SVM, Random Forest, PLS-DA)</li>
</ul>
</li>
<li>Whole-slide AI deployment: feature matching, global or masked deployment</li>
</ul>
<h2><a name="p-128618-useful-links-2" class="anchor" href="#p-128618-useful-links-2" aria-label="Heading link"></a>Useful Links:</h2>
<ul>
<li><img src="https://emoji.discourse-cdn.com/twitter/laptop.png?v=15" title=":laptop:" class="emoji only-emoji" alt=":laptop:" loading="lazy" width="20" height="20"><a href="https://github.com/jamzad/SlicerMassVision" rel="noopener nofollow ugc">Codebase</a></li>
<li><img src="https://emoji.discourse-cdn.com/twitter/page_facing_up.png?v=15" title=":page_facing_up:" class="emoji only-emoji" alt=":page_facing_up:" loading="lazy" width="20" height="20"><a href="https://slicermassvision.readthedocs.io/en/latest/" rel="noopener nofollow ugc">User Manual</a></li>
<li><img src="https://emoji.discourse-cdn.com/twitter/closed_book.png?v=15" title=":closed_book:" class="emoji only-emoji" alt=":closed_book:" loading="lazy" width="20" height="20"><a href="https://doi.org/10.1021/acs.analchem.5c04018" rel="noopener nofollow ugc">Publication</a></li>
</ul>
<h2><a name="p-128618-demonstrations-3" class="anchor" href="#p-128618-demonstrations-3" aria-label="Heading link"></a>Demonstrations:</h2>
<p>Visualization and exploration</p>
<p>          <a href="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/visualization.gif" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/visualization.gif" width="690" height="370">
          </a>
</p>
<p>Spatial colocalization</p>
<p><a href="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/colocalization.gif" class="onebox" target="_blank" rel="noopener nofollow ugc">https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/colocalization.gif</a></p>
<p>Pathology guided ROI dataset curation</p>
<p><a href="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/roi.gif" class="onebox" target="_blank" rel="noopener nofollow ugc">https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/roi.gif</a></p>
<p>Statustucal analysis</p>
<p>          <a href="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/statistical.gif" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://raw.githubusercontent.com/jamzad/SlicerMassVision/refs/heads/main/docs/source/Images/statistical.gif" width="690" height="370">
          </a>
</p>
<h2><a name="p-128618-citation-4" class="anchor" href="#p-128618-citation-4" aria-label="Heading link"></a>Citation</h2>
<p>Please use the following citations if you use <strong>MassVision</strong> in your research</p>
<p>A Jamzad, J Warren, A Syeda, M Kaufmann, N Iaboni, C JB Nicol, J F Rudan, K YM Ren, D Hurlbut, S Varma, G Fichtinger, and P Mousavi; "MassVision: An Open-Source End-to-End Platform for AI-Driven Mass Spectrometry Imaging Analysis, <em>Analytical Chemistry</em> 2025, <a href="https://doi.org/10.1021/acs.analchem.5c04018" rel="noopener nofollow ugc">DOI: 10.1021/acs.analchem.5c04018</a>.</p>

---
