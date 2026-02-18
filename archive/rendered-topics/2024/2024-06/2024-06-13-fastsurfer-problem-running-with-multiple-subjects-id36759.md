# FastSurfer: Problem running with multiple subjects

**Topic ID**: 36759
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/fastsurfer-problem-running-with-multiple-subjects/36759

---

## Post #1 by @Farah_N (2024-06-13 14:47 UTC)

<h3><a name="p-112629-i-am-running-fastsufer-for-multiple-subjects-but-i-dont-get-it-whether-the-problem-is-with-the-entrypoint-flag-or-docker-1" class="anchor" href="#p-112629-i-am-running-fastsufer-for-multiple-subjects-but-i-dont-get-it-whether-the-problem-is-with-the-entrypoint-flag-or-docker-1" aria-label="Heading link"></a>I am running FastSufer for multiple subjects, but I don’t get it whether the problem is with the ‘–entrypoint’ flag or docker.</h3>
<pre><code class="lang-auto">(base) user1nrx@srv-imgrm-04:~/software_research/my_fastsurfer_analysis/DATA$ sudo docker run --gpus all -v /home/user1nrx/software_research/my_fastsurfer_analysis/DATA:/data -v /home/user1nrx/software_research/my_fastsurfer_analysis/OUTPUT:/output -v /home/user1nrx/software_research/my_fastsurfer_analysis/freesurfer_license:/fs_license --entrypoint "/fastsurfer/brun_fastsurfer.sh" --rm --user $(id -u):$(id -g) deepmi/fastsurfer:latest --fs_license /fs_license/license.txt --sd /output --subject_list /data/subjects_list.txt --parallel --3T

</code></pre>
<pre><code class="lang-auto">INFO: run_fastsurfer not explicitly specified, using $FASTSURFER_HOME/run_fastsurfer.sh.
ERROR: Flag unrecognized.
</code></pre>

---

## Post #2 by @pieper (2024-06-13 20:47 UTC)

<p>You should probably check with the freesurfer/fastsurfer team for help with this.</p>

---
