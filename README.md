SYSNet: an end-to-end imaging systematics cleaning pipeline
===========================================================

[![arXiv](https://img.shields.io/badge/arXiv-1907.11355-b31b1b.svg)](https://arxiv.org/pdf/1907.11355)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SYSNet** is an open source software based on Python for modeling the imaging systematics in large-scale structure data. The observed galaxy density maps are a combination of true signal and systematic noise. The latter is inevitably unknown, however, we do have a set of templates for observational realities that may be the potential sources of systematic error. SYSNet uses a fully connected neural network to model the response to the templates. The methodology is decribed in [Rezaie, Seo, Ross, Bunescu (2020)](https://doi.org/10.1093/mnras/staa1231). The code incorporates:

1. Cyclic Learning Rate (Loshchilov & Hutter 2016 / ICLR 2017)
2. Batch Normalization (Ioffe, Sergey; Szegedy, Christian 2015)
3. Different Cost functions: Mean Squared Error and Poisson Negative log-likelihood.
4. Different Optimizers (e.g., SGD, AdamW, Adam)

Core developers: Mehdi Rezaie, Reza Katebi

Demo
=====
For installation and running the pipeline, check out [this demo](https://github.com/mehdirezaie/sysnetdev/blob/master/docs/demo/decals_dr7.md).

Build Status
============
We plan to perform integrated tests of the code, including all models in a miniconda environment for Python 3.8.

[![Build Status](https://travis-ci.org/mehdirezaie/sysnetdev.svg?branch=master)](https://travis-ci.org/mehdirezaie/sysnetdev)


Please email me at mr095415@ohio.edu if you encounter any issues.

