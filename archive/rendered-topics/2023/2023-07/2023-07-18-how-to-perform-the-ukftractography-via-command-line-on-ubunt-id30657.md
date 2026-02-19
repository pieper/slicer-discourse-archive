---
topic_id: 30657
title: "How To Perform The Ukftractography Via Command Line On Ubunt"
date: 2023-07-18
url: https://discourse.slicer.org/t/30657
---

# How to perform the UKFTractography via command line on ubuntu 20.04?

**Topic ID**: 30657
**Date**: 2023-07-18
**URL**: https://discourse.slicer.org/t/how-to-perform-the-ukftractography-via-command-line-on-ubuntu-20-04/30657

---

## Post #1 by @dazhangge-666 (2023-07-18 15:03 UTC)

<p>I want to use .sh to batch process my data via UKFTractography ,so maybe I must use the command line of it.How could I do?</p>

---

## Post #2 by @dazhangge-666 (2023-07-18 15:03 UTC)

<p>I want to use the UKFTractography singlely in order to use batch process on my data for tractography.<br>
when I make the code UKFTractography from github,I met the problem.<br>
I use the correct command from author.<br>
fatal: not a git repository (or any of the parent directories): .git<br>
make[5]: *** [ukf/CMakeFiles/_GEN_GITVER.dir/build.make:60: ukf/CMakeFiles/<em>GEN</em><br>
make[4]: *** [CMakeFiles/Makefile2:1043: ukf/CMakeFiles/_GEN_GITVER.dir/all] Err<br>
make[3]: *** [Makefile:141: all] Error 2<br>
make[2]: *** [CMakeFiles/UKFTractography.dir/build.make:119: UKFTractography-prey-build] Error 2<br>
make[1]: *** [CMakeFiles/Makefile2:123: CMakeFiles/UKFTractography.dir/all] Erro<br>
make: *** [Makefile:95: all] Error 2</p>

---

## Post #3 by @pieper (2023-07-18 20:52 UTC)

<p>You should be able to just install SlicerDMRI and then you can run something like <code>Slicer --launch UKFTractography</code>.  If you run through the GUI first you can see the command line arguments in the log and adjust them as needed for your script.</p>
<p>This is just a one-off script I did to process a bunch of dicom diffusion studies but it may give you some ideas: <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py#L292-L384">https://github.com/SlicerDMRI/SlicerDMRI/blob/batchtract/Modules/Scripted/BatchTract/BatchTract.py#L292-L384</a></p>

---

## Post #4 by @dazhangge-666 (2023-07-19 01:25 UTC)

<p>OK,thank u very much.I’m trying.Are there some methods that I could use the command line to use the UKFtractography via Slicer5.22?</p>

---

## Post #5 by @dazhangge-666 (2023-07-19 01:30 UTC)

<p>And I have tried the command line to use the Slicer,but there is no difference.I couldn’t find some thing named UKFTractography in SlicerDMRI.</p>

---

## Post #6 by @dazhangge-666 (2023-07-19 01:34 UTC)

<p>Couldn’t I use ./UKFTractography in Slicer’s directory?like:<br>
(base) ubuntu@dmri:~/tools/Slicer/NA-MIC/Extensions-31382/UKFTractography/lib/Slicer-5               .2/cli-modules$ ./UKFTractography --help<br>
./UKFTractography: error while loading shared libraries: libITKFactoryRegistration.so:                cannot open shared object file: No such file or directory<br>
(base) ubuntu@dmri:~/tools/Slicer/NA-MIC/Extensions-31382/UKFTractography/lib/Slicer-5               .2/cli-modules$</p>

---

## Post #7 by @pieper (2023-07-19 14:59 UTC)

<p>Since the CLI module is in an extension you need to use a command like this:</p>
<pre><code class="lang-auto">~/Downloads/Slicer-5.2.2-linux-amd64/Slicer --launch bash -c UKFTractography
</code></pre>

---

## Post #8 by @dazhangge-666 (2023-10-14 07:11 UTC)

<p>Thank you very much! Hi pieper,when I use the command how could I indicate the input files and output files?<br>
Because I want to use the Slicer to generate the mask and .nrrd file of bvec bval nii.<br>
the Error occured like the following :</p>
<p>“Error! Must indicate DWI data, mask and tracts output files!”</p>

---

## Post #9 by @pieper (2023-10-14 17:26 UTC)

<p>I think you mean that you have bval/bvec filts and you need .nrrd files for UKF?</p>
<p>You can find converter code here: <a href="https://github.com/pnlbwh/conversion" class="inline-onebox">GitHub - pnlbwh/conversion: Various mri conversion/modification scripts</a></p>

---

## Post #10 by @dazhangge-666 (2023-10-15 08:44 UTC)

<p>I mean this command “~/Downloads/Slicer-5.2.2-linux-amd64/Slicer --launch bash -c UKFTractography” how could I input the DWI data, mask and seeds files？</p>

---

## Post #11 by @pieper (2023-10-15 21:54 UTC)

<p>The easiest way to do that is to run the process via the user interface and look at the log file.  You’ll see the command line arguments and you need to map those to the files you use.</p>

---

## Post #13 by @dazhangge-666 (2023-10-16 03:36 UTC)

<p>Thank you very much!I got this!</p>

---
