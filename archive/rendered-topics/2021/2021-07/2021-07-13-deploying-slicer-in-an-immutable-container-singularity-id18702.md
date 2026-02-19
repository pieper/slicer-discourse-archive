---
topic_id: 18702
title: "Deploying Slicer In An Immutable Container Singularity"
date: 2021-07-13
url: https://discourse.slicer.org/t/18702
---

# Deploying slicer in an immutable container (Singularity)

**Topic ID**: 18702
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/deploying-slicer-in-an-immutable-container-singularity/18702

---

## Post #1 by @Blake_Fitch (2021-07-13 10:10 UTC)

<p>Hello Sir,</p>
<p>I am deploying slicer in an immutable container (Singularity) and the install directory is not writable.</p>
<p>From reading the above posts, it seems like there is a way to tell Slicer to keep all extensions, etc, in the users $HOME without recompiling the application. But I’m not quite clear on how to setup the .ini file.</p>
<p>Could you provide an example of a .ini that perhaps used $HOME or $USER to place the slicer state?</p>
<p>Any help is most appreciated!</p>
<p>Best,<br>
Blake</p>

---

## Post #2 by @lassoan (2021-07-13 18:32 UTC)

<p>If you want to let your users install any extensions (including those that them relying on Python packages) then the application installation folder must be writable. Since the Slicer application folder is fully relocatable, you can achieve this by simply copying the entire Slicer application folder content to the user’s home folder in some startup script.</p>
<p>If you don’t want to let your users install extensions then you can install Slicer in a read-only location.</p>
<p>I think these are the same options that are offered for any other Python environments.</p>
<p>If you want to allow your users to install extensions that do not require any additional Python packages then in the <code>NA-MIC\Slicer-NNNNN.ini</code> config file you can set the <code>Extensions/InstallPath</code> value to an absolute path in a writable location, but I would not recommend this “mixed” mode because users would not understand why some extensions<br>
(those that rely on extra Python packages) don’t work.</p>

---

## Post #3 by @Blake_Fitch (2021-07-13 22:49 UTC)

<p>Thanks for the quick response. Sorry about spamming with a second post.</p>
<p>So, I’m not eager to be in-the-loop with users installing extensions. Hopefully they are not too dangerous! It seems like nothing would stop a user from installing Slicer to their home directory on the cluster and installing extensions anyway. Or am I missing something here?</p>
<p>What I see the container doing that copying the Slicer install directory alone doesn’t is ensuring the proper libraries are available.</p>
<p>One idea might be to have the container startup script immediately copy the Slicer install directory to the users home directory, which is writable. Slicer would still run in the container, providing the libs but would be run from the users home dir, and so, writable for all extensions.</p>
<p>This seems to be what you are suggesting. Do I have that right?</p>
<p>Best,<br>
Blake</p>

---

## Post #4 by @pieper (2021-07-14 00:14 UTC)

<p>Hi -</p>
<p>I’m not sure what your target environment is, but it sounds like a cluster where each user has a home directory with some disk space that is accessible from the nodes.  In this case it’s probably good for each user to have their own installation of Slicer that they can customize with the extensions they need.  Slicer can work from a container, but doesn’t really need one since it comes bundled with all the dependencies it needs (our launcher configures the paths to resolve to our copies of all the libs).  Since these may change from version to version, users might end up with a couple different Slicer installs with different extensions installed and you can let them manage that on their own.</p>

---

## Post #5 by @muratmaga (2021-07-14 00:24 UTC)

<p><a class="mention" href="/u/blake_fitch">@Blake_Fitch</a> alternatively, if your users need the same set of extensions (and will not require anymore extensions or python libraries after you build your container), you can install Slicer on any Linux platform host (along with the extensions), and and tar.gz the installation folder and copy it to your container during the build time.</p>

---

## Post #6 by @Blake_Fitch (2021-07-14 08:26 UTC)

<p>Hi All,</p>
<p>This environment is an OpenHPC cluster where we try to keep native installed software to a minimum and deploy applications in singularity. Each user has access to a $HOME which is accessible from the compute nodes.</p>
<p>I should try Slicer outside a container as user installed data and see how that goes. My guess is that system libraries (e.g. X11 related) may not be available. If this is the case, I will create a singularity container that, as mentioned, installs the base Slicer if it’s not there, and stays running to provide the library environment.</p>
<p>Best,<br>
Blake</p>

---

## Post #7 by @pieper (2021-07-14 12:41 UTC)

<p>There are several examples of Slicer running in containers (search for SlicerDocker, SlicerDockers, SlicerMorphCloud) with a virtual X session.  You could set up the virtual desktop part but then let users run Slicer from a mounted writable volume so they could customize it as needed.</p>

---
