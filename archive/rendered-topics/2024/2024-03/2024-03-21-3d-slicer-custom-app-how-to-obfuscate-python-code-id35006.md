# 3d slicer custom app: how to obfuscate python code

**Topic ID**: 35006
**Date**: 2024-03-21
**URL**: https://discourse.slicer.org/t/3d-slicer-custom-app-how-to-obfuscate-python-code/35006

---

## Post #1 by @aymeric.chataigner (2024-03-21 13:23 UTC)

<p>Hi,</p>
<p>We would like to obfuscate the python code in the install archive of our 3D Slicer custom app.<br>
We tried to use cython without success for now.<br>
Do you have any solution, any advice ?</p>
<p>Regards</p>

---

## Post #2 by @cpinter (2024-03-21 13:56 UTC)

<p>I suggest looking at this thread</p><aside class="quote" data-post="26" data-topic="26135">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-hide-the-code-of-the-script-module/26135/26">How to hide the code of the script module?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Corresponding approach was revisited by instead introduce the option CTK_COMPILE_PYTHON_SCRIPT_KEEP_ONLY_PYC to support removing *.py script once the corresponding *.pyc file has been generated in the destination directory. 
See <a href="https://github.com/commontk/CTK/pull/1192">https://github.com/commontk/CTK/pull/1192</a> 
<a class="mention" href="/u/mjamal">@MJamal</a> At your convenience, consider reviewing and testing the proposed changes <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title="pray" alt="pray" class="emoji">
  </blockquote>
</aside>


---
