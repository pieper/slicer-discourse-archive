# Build Slicer on Win11, use git bash to configure Slicer repo failed due to ownership discripancy

**Topic ID**: 38050
**Date**: 2024-08-27
**URL**: https://discourse.slicer.org/t/build-slicer-on-win11-use-git-bash-to-configure-slicer-repo-failed-due-to-ownership-discripancy/38050

---

## Post #1 by @chz31 (2024-08-27 05:29 UTC)

<p>Hi all,</p>
<p>I’m trying to build Slicer on Win 11. However, when I tried to configure the Slicer repository by selecting “open bash here” for the Utility folder, following instruction <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#:~:text=Configure%20the%20repository,on%20this%20page" rel="noopener nofollow ugc">here</a>, I got an repo owner discrepancy error below:</p>
<pre><code class="lang-auto">$ ./SetupForDevelopment.sh
fatal: not in a git directory
fatal: not in a git directory
Checking basic user information...
Please enter your full name, such as 'John Doe': Chi Zhang
Setting name to 'Chi Zhang'
fatal: not in a git directory
Please enter your email address, such as 'john@email.com': chi.zhang@tamu.edu
Setting email address to 'chi.zhang@tamu.edu'
fatal: not in a git directory
Your commits will have the following author:

   &lt;&gt;

Is the author name and email address above correct? [Y/n] Y

Setting up git hooks...
Pulling the hooks...
fatal: detected dubious ownership in repository at 'C:/slicer_build/slicer_source/.git/hooks'
'C:/slicer_build/slicer_source/.git/hooks' is owned by:
        BUILTIN/Administrators (S-1-5-32-544)
but the current user is:
        AUTH/chi.zhang (S-1-5-21-1167378736-2199707310-2242153877-1186313)
To add an exception for this directory, call:

        git config --global --add safe.directory C:/slicer_build/slicer_source/.git/hooks
Failure during hook setup
-------------------------

Downloading the hooks failed.
</code></pre>
<p>I wonder if it is related to the ownership of the computer in my institution. The IT did install an AdaminByRequest software to allow me temporarily run my computer under admin mode. Is there anyway to fix this problem? Thanks!</p>
<p>Chi</p>

---

## Post #2 by @muratmaga (2024-08-27 15:48 UTC)

<p>You need to get the IT to change ownership of all your slicer_build tree folder from Admin to chi.zhang or add your personal account to the permissions of the folder.</p>
<p>In general assume that if IT installs a software for you, you won’t be able to write to those folders since they would be created under a different account/permission than yours.</p>

---

## Post #3 by @chz31 (2024-08-27 16:55 UTC)

<p>Thanks! I did <code>takeown /f "C:\slicer_build\slicer_source" /r /d y</code>, and then <code>git config --global --add safe.directory C:/slicer_build/slicer_source</code> under admin mode, the ownership issue appears to be solved.</p>

---
