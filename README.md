# gen_list_pub_from_bibtex
Generate a list of publications in Markdown (e.g., publishing to a personal website) from a Bibtex file. 

## To run 

```
python listpubfromBib.py 
```

## Input format 
This code requires a Bibtex file name `proceedings.bib`. In this file, there are your papers' bibtex (e.g., that can be obtained 
from Google Scholar). However, in addition to standard fileds in Bibtex (i.e., title, author, booktile), you can add some additional 
files (i.e, `code`,`paper`,`poster`,`presentation` that link to your github repository, paper, poster or slide, respectively). Example as below or in the `proceedings.bib` file. 

```
@inproceedings{bui2021improving,
  title={Improving ensemble robustness by collaboratively promoting and demoting adversarial robustness},
  author={Bui, Anh Tuan and Le, Trung and Zhao, He and Montague, Paul and deVel, Olivier and Abraham, Tamas and Phung, Dinh},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={35},
  number={8},
  pages={6831--6839},
  year={2021}, 
  paper={https://arxiv.org/abs/2009.09612},
  code={https://github.com/tuananhbui89/Crossing-Collaborative-Ensemble},
  poster={https://www.dropbox.com/s/88gfbrm84io12jv/6932_BuiA_Poster.pdf?dl=0}, 
  presentation={https://www.dropbox.com/s/cytsud07rjido1v/6932_long_presentation.pdf?dl=0},
}
```

## Output format 
Will generate a Markdown list of publication like below 

[1]  [**Anh Bui**](https://tuananhbui89.github.io/),  [Trung Le](https://scholar.google.com/citations?user=gysdMxwAAAAJ&hl=en),  [He Zhao](https://ethanhezhao.github.io/),  Paul Montague,  Seyit Camtepe,  [Dinh Phung](http://dinhphung.ml/), 'Understanding and achieving efficient robustness with adversarial supervised contrastive learning', arXiv preprint arXiv:2101.10027, 2021. [paper](https://arxiv.org/abs/2101.10027) [code](https://github.com/tuananhbui89/ASCL)<br>
[2]  [**Anh Bui**](https://tuananhbui89.github.io/),  [Trung Le](https://scholar.google.com/citations?user=gysdMxwAAAAJ&hl=en),  Quan Tran,  [He Zhao](https://ethanhezhao.github.io/),  [Dinh Phung](http://dinhphung.ml/), 'A Unified Wasserstein Distributional Robustness Framework for Adversarial Training', International Conference on Learning Representations, 2021. [paper](https://openreview.net/forum?id=Dzpe9C1mpiv) [code](https://github.com/tuananhbui89/Unified-Distributional-Robustness)<br>
