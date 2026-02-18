# one tensor missed after two-tensor tractography

**Topic ID**: 6370
**Date**: 2019-04-02
**URL**: https://discourse.slicer.org/t/one-tensor-missed-after-two-tensor-tractography/6370

---

## Post #1 by @mali (2019-04-02 14:38 UTC)

<p>Dear all,</p>
<p>I used two-tensor tractography for my whole brain analysis and extracted several fiber tracts by drawing ROIs manually. Strangely, one fiber tract  is now missing the first tensor in two scans although all of the scans were processed identically and there were no issues with the other tracts in the exact same scans. When I load the respective tracts in Slicer only one active tensor can be seen. Do you have a hint to solve this problem?</p>
<p>Best, Marlene</p>

---

## Post #2 by @ljod (2019-04-02 17:47 UTC)

<p>Hi Marlene. Have you checked the whole brain tractography to make sure it has two tensors? It is possible to run UKF tractography with one or two tensors, so the first thing is to make sure definitely you have two tensors in the original tractography.</p>
<p>By “exact same scans” do you mean you processed the same whole brain tractography more than once to extract different tracts, and sometimes you did not get both tensors?</p>
<p>We also need exact information about what modules you used to do the processing.</p>

---

## Post #3 by @mali (2019-04-02 18:44 UTC)

<p>Hi Lauren,</p>
<p>thanks for your quick answer! I checked the whole brain tractography and somehow there is only one active tensor left in the two cases that are affected. Is it possible that one of the two tensors got enabled? I used the same brain tractography to extract different fiber bundles via different ROIs earlier but strangely the other fiber bundles of the same cases show two active tensors, although I always used the same whole brain tractography.</p>
<p>I used UKFTractography.py for the whole brain tractography and then drew my ROIs in slicer to extract different fiber bundles. For measurements, I also used the tool in Slicer.</p>
<p>Thanks for your help!</p>

---

## Post #4 by @ljod (2019-04-02 19:04 UTC)

<p>Hi! Please let us know specifically how you are checking if there is one tensor or two. What module, what button, etc.</p>

---

## Post #5 by @mali (2019-04-02 19:39 UTC)

<p>I found out when I had a look at the output-file with the measurements where two cases had only values for one tensor and “NAN” for the values of the second tensor. Also, when I go to “Tractography Display” in Slicer and look at the “advanced display”, there is only tensor1 in the drop-down menu of “active tensor”. The other cases all show tensor1 and tensor2.</p>

---

## Post #6 by @ljod (2019-04-02 19:54 UTC)

<p>This is unusual. Could you please explain exactly how you ran tractography with ukf? Inside slicer? On the command line? Were there any error messages? You may need to re-run this to check.</p>

---

## Post #7 by @mali (2019-04-03 05:38 UTC)

<p>I used UKFTractography on the command line in the terminal. Can you run 2 tensor tractography inside Slicer? I will re-run this step and get back to you as soon as it’s finished.</p>

---

## Post #8 by @mali (2019-04-03 14:55 UTC)

<p>Hello Lauren,</p>
<p>I tried to re-run UKFTractography on my personal computer again but the process was killed when I used more than 2 seeds per voxel. For 2 seeds per voxel the output shows again only one tensor. Is there a special command to make sure that two tensors are being calculated? I thought UKFTractography on the command line would always use two tensors. Is there a chance that the two tensors have been compressed and the values I get represent the mean of the two tensors?</p>

---

## Post #9 by @ljod (2019-04-03 15:46 UTC)

<p>You have to specify to use two tensors on the command line. You can test quickly by seeding in a smaller ROI than the whole brain. --numTensors 2 on the command line should do this. Also, the default should be two tensors.</p>
<p>This sounds more like a problem saving the tractography output file. If there are disk access issues with the computer, because the second tensor is saved last, it may not get correctly saved. Please check your disk. Is it full?</p>

---

## Post #10 by @mali (2019-04-05 03:51 UTC)

<p>I re-run the process but unfortunately, I still only get one tensor even if I use --numTensor 2. Storage does not seem to be a problem as I still have plently of space on my disk. Do you have another idea?<br>
Thanks, I really appreciate your help!</p>

---

## Post #11 by @ljod (2019-04-08 16:36 UTC)

<p>Hi this is quite strange since it worked on your other datasets. Does this one have smaller voxels or more image slices? I am wondering if you are effectively seeding more times and running out of computer memory?</p>

---

## Post #12 by @mali (2019-04-09 03:24 UTC)

<p>Hello Lauren,<br>
computer memory might be the point! The process was killed earlier when I used more than two seeding points which would support this theory. Is there a way to find out for sure?<br>
Actually, I processed all scans on a computer at the PNL last year and wanted to re-run the process on my computer now but it is still strange that two of the “PNL scans” have been saved with only one tensor.</p>

---

## Post #13 by @ljod (2019-04-09 12:51 UTC)

<p>Hi. On the other computer this may have been a disk or memory issue. It sounds like your current computer is not able to run this. I recommend using a bigger computer to re-run those last two.</p>

---

## Post #14 by @mali (2019-04-10 03:17 UTC)

<p>Hi Lauren,<br>
that’s sad news but thanks a lot for your expertise which I appreciate a lot!<br>
Best, Marlene</p>

---
