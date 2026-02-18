# Renaming all objects in a node

**Topic ID**: 35298
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/renaming-all-objects-in-a-node/35298

---

## Post #1 by @S_Motch_Perrine (2024-04-04 22:00 UTC)

<p>When using ALPACA, the folder names are automatically something like “ALPACA_output_01”, with all files within it having a corresponding name. I need my folders to have the specimen names in. How do I make the names of all of the associated files within have a similar naming scheme?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5165539bed704b6b8947a378d835566842b0242.png" alt="image" data-base62-sha1="yY8Pm03QyzfxldQYtmciHBNeQMi" width="538" height="203"><br>
I am especially concerned with making sure that the markups file Final ALPACA landmark estimate_1 reads instead, “Final ALPACA landmark estimate_Prdm16_E17.5_002” for example. I don’t want to manually change them all the time as there are so many files, etc. Thank you!</p>

---

## Post #2 by @muratmaga (2024-04-05 08:33 UTC)

<p><a class="mention" href="/u/s_motch_perrine">@S_Motch_Perrine</a> interactive mode is only for exploring, and all of those things that are nested in the output is to help you visualize different stages of the ALPACA for better alignment and landmark transfer. Once you are done with the exploration, find the set of parameters that work well for your samples and ready to analyze, you should use the batch mode.</p>
<p>In batch mode, the outputs will be saved directly to the disk using the file prefix from the target model.</p>
<p>Please see the alpaca tutorial at <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></p>

---

## Post #3 by @S_Motch_Perrine (2024-04-05 14:34 UTC)

<p>Thanks, yes I do normally use batch mode… I have just been testing a ton and was thinking it would be easier for me to go back and compare if I could make everything named after all the specific mice and tissues.</p>

---

## Post #4 by @lassoan (2024-04-05 14:36 UTC)

<aside class="quote no-group" data-username="S_Motch_Perrine" data-post="1" data-topic="35298">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/s_motch_perrine/48/81028_2.png" class="avatar"> S_Motch_Perrine:</div>
<blockquote>
<p>How do I make the names of all of the associated files within have a similar naming scheme?</p>
</blockquote>
</aside>
<p>You can right-click on the folder, choose <code>Export to file...</code> and enable <code>Export folder structure</code> option. Then all the models within a subject hierarchy branch will be saved into a separate folder on disk.</p>

---
