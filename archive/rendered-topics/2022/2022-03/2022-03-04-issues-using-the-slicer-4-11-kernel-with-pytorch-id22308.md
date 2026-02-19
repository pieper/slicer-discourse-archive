---
topic_id: 22308
title: "Issues Using The Slicer 4 11 Kernel With Pytorch"
date: 2022-03-04
url: https://discourse.slicer.org/t/22308
---

# Issues using the Slicer 4.11 kernel with Pytorch

**Topic ID**: 22308
**Date**: 2022-03-04
**URL**: https://discourse.slicer.org/t/issues-using-the-slicer-4-11-kernel-with-pytorch/22308

---

## Post #1 by @dariodo.fal (2022-03-04 12:42 UTC)

<p>Hello, I am trying to do the Transfer Learning tutorial that the Pytorch website offers using the Slicer 4.11 kernel with the TorchIO extension but I am finding a problem I don’t understand. The code looks like this so far</p>
<pre><code class="lang-auto">from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.backends.cudnn as cudnn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy

cudnn.benchmark = True
plt.ion()   # interactive mode

import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(299),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(299),
        transforms.CenterCrop(299),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

data_dir = r"c:\Users\dario\Letters"
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
                  for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                             shuffle=True, num_workers=4)
              for x in ['train', 'val']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
class_names = image_datasets['train'].classes

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print(class_names)

def imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.numpy().transpose((1, 2, 0))
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated

# Get a batch of training data
inputs, classes = next(iter(dataloaders['train']))
# Make a grid from batch
out = torchvision.utils.make_grid(inputs)
imshow(out, title=[class_names[x] for x in classes]) 
</code></pre>
<p>As you can see, I am using the InceptionV3 model with 5 possible classes because that’s what I am required to work with. The problem comes when it gets to the following line:</p>
<pre><code class="lang-auto">inputs, classes = next(iter(dataloaders['train'])) 
</code></pre>
<p>When it gets here, this window shows up on my screen<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e8f79ccefb3caa9b64ac7aba2a1d0401c18e222.png" data-download-href="/uploads/short-url/24O4XEqSEN8OkFWK5STGbZa8sOm.png?dl=1" title="slicerproblem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8f79ccefb3caa9b64ac7aba2a1d0401c18e222_2_690x399.png" alt="slicerproblem" data-base62-sha1="24O4XEqSEN8OkFWK5STGbZa8sOm" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8f79ccefb3caa9b64ac7aba2a1d0401c18e222_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e8f79ccefb3caa9b64ac7aba2a1d0401c18e222_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e8f79ccefb3caa9b64ac7aba2a1d0401c18e222.png 2x" data-dominant-color="1D1D1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerproblem</span><span class="informations">1118×647 6.81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I don’t know what I am supposed to put in here or if this is supposed to be happening as I haven’t worked with Slicer ever before. Does anyone know how I can solve it?</p>

---

## Post #2 by @pieper (2022-03-04 14:24 UTC)

<p>Can you add a link to the tutorial you are trying to follow?  Is it supposed to work in Slicer?</p>

---

## Post #3 by @dariodo.fal (2022-03-06 17:12 UTC)

<p>Hello, this is the tutorial: <a href="https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html" rel="noopener nofollow ugc">https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html</a><br>
I it is not made for the Slicer kernel afaik, but I was trying to see if it would work for it since other models worked in it.</p>

---

## Post #4 by @pieper (2022-03-06 17:52 UTC)

<p>You should try with the slicer preview build.  It has a newer python and works with pytorch.</p>

---
