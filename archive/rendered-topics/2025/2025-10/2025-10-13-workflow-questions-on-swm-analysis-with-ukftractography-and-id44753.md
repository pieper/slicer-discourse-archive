# Workflow Questions on SWM Analysis with UKFtractography and whitematteranalysis

**Topic ID**: 44753
**Date**: 2025-10-13
**URL**: https://discourse.slicer.org/t/workflow-questions-on-swm-analysis-with-ukftractography-and-whitematteranalysis/44753

---

## Post #1 by @younghoo (2025-10-13 20:58 UTC)

<p>Dear Experts,</p>
<p>I am attempting to replicate the methodology described in the following paper and have a few questions that I hope you can help clarify:</p>
<p>Wang, S., Zhang, F., Zeng, Q., Hong, H., Zhang, Y., Xie, L., Lin, M., Jiaerken, Y., Yu, X., Zhang, R., Luo, X., Li, K., Xu, X., Hassanzadeh-Behbahani, S., Lin, B., Rushmore, J., Wang, C., Rathi, Y., Makris, N., Huang, P., … Alzheimer’s Disease Neuroimaging Initiative (2025). Association of Superficial White Matter Microstructure With Cortical Pathology Deposition Across Early Stages of the AD Continuum. <em>Neurology</em> , <em>105</em>(2), e213666. <a href="https://doi.org/10.1212/WNL.0000000000213666" rel="noopener nofollow ugc">https://doi.org/10.1212/WNL.0000000000213666</a></p>
<p><strong>Q1:</strong> I first ran <code>ukftractography</code> on my preprocessed DWI data and then applied <code>whitematteranalysis</code> to cluster fiber tracts and obtain microstructure measures for each anatomical tract. Below is the code I used. Could you confirm whether this workflow is correct?</p>
<pre data-code-wrap="bash"><code class="lang-bash">## Run 2-Tensor tractography with free water
ukf.py --bvals dwi.bval --bvecs dwi.bvec -i dwi.nii.gz -m dwi_brainmask.nii.gz -o dwi.vtk \
        --params '--seedingThreshold',0.1,'--stoppingFA',0.08,'--stoppingThreshold',0.06,--freeWater,--recordFA,--recordTrace,--recordFreeWater
## Run fiber clustering and measurement
wm_apply_ORG_atlas_to_subject.sh \
        -i ${input_dir}/dwi.vtk \
        -o ${output_dir} \
        -a ${atlas_dir}/ORG-Atlases-1.1.1 \
        -s ${soft_dir}/Slicer-5.8.1-linux-amd64/Slicer \
        -d 1 \
        -m ${soft_dir}/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/SlicerDMRI/lib/Slicer-5.8/cli-modules/FiberTractMeasurements
</code></pre>
<p><strong>Q2:</strong> In Wang et al. (2025), three microstructure measures were evaluated: free water fraction (FW), free-water-corrected fractional anisotropy (FAt), and free-water-corrected mean diffusivity (MDt). After running <code>wm_apply_ORG_atlas_to_subject.sh</code> , I obtained FA and MD values for each tensor. How can I derive the FAt and MDt measures used in the paper?</p>
<p><strong>Q3:</strong> The paper mentions that 396 superficial white matter (SWM) fiber clusters were considered. In my output, I only obtained 800 clusters grouped into 74 anatomical tracts. How could I obtain the mappings between the 800 clusters and the 74 anatomical tracts so that I can identify the 396 SWM clusters?</p>
<p>Thank you in advance for your assistance!</p>

---

## Post #2 by @younghoo (2025-10-14 00:05 UTC)

<p>Regarding my third question, I have found the solution. The mapping between fiber clusters and anatomical tracts is provided in the FiberClusterAnnotation file within the ORG Atlas repository:  <a href="https://github.com/SlicerDMRI/ORG-Atlases/blob/master/ORG-800FC-100HCP/FiberClusterAnnotation_k0800_v1.0.csv" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/ORG-Atlases/blob/master/ORG-800FC-100HCP/FiberClusterAnnotation_k0800_v1.0.csv</a></p>

---

## Post #3 by @ljod (2025-10-15 08:07 UTC)

<p>Hello and thanks for your questions. The FAt and MDt are the values from tensor 1, which is the tract or fiber specific estimate.</p>

---

## Post #4 by @ljod (2025-10-15 08:11 UTC)

<p>Also yes the pipeline looks generally correct. It is always important to visually inspect the results of each step to ensure it’s working well in your data, especially that coordinate systems are correct for gradient vectors etc. One thing to make sure is that any conversion from nii to the nerd format used by UKF is correctly working.</p>

---

## Post #5 by @younghoo (2025-10-15 09:18 UTC)

<p>Thank you for the reminder. I have followed the quality control (QC) procedure outlined in the step-by-step WMA tutorial: <a href="https://whitematteranalysis.readthedocs.io/en/latest/subject-specific-tractography-parcellation.html" rel="noopener nofollow ugc">https://whitematteranalysis.readthedocs.io/en/latest/subject-specific-tractography-parcellation.html</a></p>
<p>Briefly, the steps I performed are as follows:</p>
<ul>
<li>First, I used <code>wm_quality_control_tractography.py</code> to obtain an overall view of the whole-brain tractography data and confirm that it appears anatomically plausible. A normal-looking tractography result suggests that the DWI data and gradient vectors were correctly interpreted by the UKF algorithm.</li>
<li>Next, I applied <code>wm_quality_control_tract_overlap.py</code> to assess the alignment between the input tractography and the ORG Atlas tractography <strong>before registration</strong> . A rough misalignment at this stage helps verify that the input data is in the same coordinate system as the ORG Atlas.</li>
<li>I then used <code>wm_quality_control_tract_overlap.py</code> again to evaluate the alignment <strong>after registration</strong> , ensuring that the registration works as expected.</li>
<li>Finally, I ran <code>wm_quality_control_tractography.py</code> to visualize the identified anatomical tracts, confirming that characteristic deep white matter tracts were successfully reconstructed and resemble those in the ORG Atlas.</li>
</ul>
<p>Could you please confirm whether this QC procedure is sufficient to ensure the validity of the results?</p>

---

## Post #6 by @ljod (2025-10-15 09:45 UTC)

<p>Yes this QC procedure looks good. If the anatomical tracts look correct, then your data and processing are working well. It’s important to view multiple tracts that run in different orientation such as CC, AF, IOFF/IFOF, CST, etc. to be confident. For your project it is also a good idea to view the superficial tract categories and some individual fiber clusters.</p>
<p>It looks like you used our QC scripts, so you should also have an HTML page with some views of all subjects tractography (whole brain tractograms) to do a visual inspection overview to make sure all brains look reasonable.</p>
<p>Also it’s important to preprocess your DWI prior to the tractography pipeline to handle eddy current/movement correction, and any other preprocessing you choose. I assume you did that previously.</p>
<p>How did you run the UKF.py with nii inputs? Is that a script you wrote or is it from our code?</p>

---

## Post #7 by @younghoo (2025-10-15 09:57 UTC)

<p>As for the quality control (QC) procedure, I utilized the scripts provided within the <a href="https://github.com/SlicerDMRI/whitematteranalysis" rel="noopener nofollow ugc">WMA</a> package. Regarding the <a href="https://github.com/pnlbwh/ukftractography" rel="noopener nofollow ugc">UKF</a> tractography, it directly accepts NIFTI format, as the tool automatically performs an on-the-fly conversion to NRRD.</p>

---

## Post #8 by @younghoo (2025-10-15 10:32 UTC)

<p>I have a follow-up question on the FA measurement. Since I have little knowledge of the underlying algorithms, could you provide an intuitive explanation for why the FA of a whole fiber is taken exclusively from tensor 1, as the tractography may follow tensor 2’s direction? This will help me ensure I’m interpreting the results correctly. Thank you!</p>

---

## Post #9 by @ljod (2025-10-15 12:23 UTC)

<p>Hi. The tractography exclusively follows tensor 1 while tensor 2 models crossing fibers in the voxel. The tensor fit is done during tracking so the Kalman filter uses tensor 1 to model the pathway it is tracing. The prior of having the model fit from the previous step helps stabilize tracking.</p>

---

## Post #10 by @younghoo (2026-01-11 03:40 UTC)

<p>Dear Expert,</p>
<p>I have a follow-up question regarding the identification of the 800 white matter clusters. In my own data, I found that not all 396 superficial white matter (SWM) clusters are identified in every participant. Specifically, 227 out of the 396 clusters are missing in at least one participant. Deep white matter clusters are also not fully identified, though this is not the primary focus of my current work. On average, about 95% (standard deviation: 4%) of SWM clusters were successfully identified per participant. My DWI data were acquired using a similar protocol to that in Wang et al. (2025). My questions are:</p>
<p><strong>Q1:</strong> Is it normal to observe missing clusters, or could this indicate a problem in processing? I believe this incomplete identification may be expected, since the method is fully data-driven and these clusters may not be as reproducible as major tracts.</p>
<p><strong>Q2:</strong> Given that some SWM clusters are missing, would it be acceptable to analyze SWM tracts instead? I have noticed that although certain clusters are not consistently identified, the SWM tracts appear comparable across participants. Therefore, comparing tracts might be more reliable and anatomically interpretable.</p>
<p><strong>Q3:</strong> I suspect the incomplete identification may be related to the UKF tractography results. In my data, the average total number of fibers generated is about 100k, while Wang et al. (2025) reported generating approximately 500k fibers per participant. Although my current UKF parameters were chosen to follow this study, I am not certain whether adjusting these parameters to increase the streamline count to 500k could improve identification reliability. I would appreciate your advice on whether such tuning is feasible or recommended.</p>
<p>Thank you in advance for your insights.</p>

---

## Post #11 by @ljod (2026-01-11 15:50 UTC)

<p>Hi! I’m glad things are progressing. I strongly recommend seeding more times per voxel to achieve better white matter coverage. Also depending on your data you might need to adjust tractography parameters. Following our 2028 atlas paper parameters provides generally sensitive coverage of fiber clusters across different scan protocols and ages. I also recommend viewing the whole brain tractography and fiber cluster outputs to ensure the pipeline results look correct. A small number of missing clusters is expected, like a few percent per subject, due to anatomical variability and scan quality. But a large number is generally due to issues with input tractography.</p>

---

## Post #12 by @ljod (2026-01-11 17:03 UTC)

<p>Also, yes analyzing the larger “tracts” is reasonable, but I recommend improving tractography first.</p>

---

## Post #13 by @younghoo (2026-01-18 03:50 UTC)

<p>Dear expert,</p>
<p>Thank you once again for your insightful guidance. Following your suggestions, I re-ran the tractography with <code>--seedsPerVoxel</code> set to 10 (default was 1), which increased the average number of streamlines per participant to approximately 1 million. The results showed significant improvement: 98.7% (SD: 1.8%) of SWM clusters were successfully identified. This outcome closely aligns with the findings reported in the atlas paper by Zhang et al. (2018) (see Tables 4 &amp; 7).</p>
<p>Since my study includes older adults and patient groups, white matter atrophy or degeneration may naturally reduce cluster identifiability. Furthermore, my DWI data, acquired with a b-value of 1000 and 30 diffusion-weighting directions, is of lower angular resolution and contrast compared to the HCP dataset used to construct the ORG atlas.</p>
<p>In addition, do you have plans to release the ORG atlas as NIFTI mask files in MNI152 space? Such a resource would allow researchers to bypass tractography in certain applications and directly use predefined tract or cluster masks for microstructure analysis (e.g., extracting FA). This could improve reproducibility and accessibility, especially for studies with varying data quality, processing pipelines and population characteristics.</p>
<p>I’m grateful for your continued help.</p>

---
