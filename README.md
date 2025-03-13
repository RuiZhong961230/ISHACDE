# ISHACDE
Space Mission Trajectory Optimization via Competitive Differential Evolution with Independent Success History Adaptation

## Highlights
• We propose an independent success history adaptation competitive differential evolution (ISHACDE).  
• We hypothesize the independent evolution of parameters can accelerate the optimization.  
• We conduct numerical experiments on CEC benchmarks and space mission trajectory problems to evaluate ISHACDE.  
• The ablation experiments are conducted to investigate the independent success history adaptation scheme.  
• Comprehensive numerical experiments and statistical analysis confirm the efficiency and effectiveness of ISHACDE.  


## Abstract
This paper proposes a novel Independent Success History Adaptation Competitive Differential Evolution (ISHACDE) algorithm to address the functional optimization problems and the Space Mission Trajectory Optimization (SMTO). ISHACDE is developed based on the efficient optimizer Competitive Differential Evolution (CDE) and integrates an independent success history adaptation scheme. This scheme inherits the hypothesis from Success History Adaptive Differential Evolution (SHADE) that the scaling factor $F$ and crossover rate $Cr$ from success evolution may contribute to accelerating the evolution of the whole population, and we further hypothesize that the independent evolution of $F$ in CDE may perform better. We conduct comprehensive numerical experiments on median-scale CEC2017, large-scale CEC2020, small-scale CEC2022, and the single-objective GTOPX benchmark to evaluate the performance of ISHACDE. Ten state-of-the-art optimizers and ten recently proposed optimizers are employed as competitor algorithms. The experimental results and statistical analysis confirm the competitiveness of the proposed ISHACDE against twenty optimizers, and the ablation experiments practically prove the effectiveness of the independent success history adaptation scheme. The source code of this research can be found in https://github.com/RuiZhong961230/ISHACDE.

## Citation
@article{Zhong:25,  
title = {Space mission trajectory optimization via competitive differential evolution with independent success history adaptation},  
journal = {Applied Soft Computing},  
volume = {171},  
pages = {112777},  
year = {2025},  
issn = {1568-4946},  
doi = {https://doi.org/10.1016/j.asoc.2025.112777 },  
author = {Rui Zhong and Abdelazim G. Hussien and Shilong Zhang and Yuefeng Xu and Jun Yu},  
}

## Datasets and Libraries
CEC benchmarks and Engineering problems are provided by opfunu==1.0.0 and enoppy==0.1.1 libraries, respectively. GTOPX can be found at M. Schlueter, M. Neshat, M. Wahib, M. Munetomo, M. Wagner, Gtopx space mission benchmarks, SoftwareX 14 (2021) 100666 and https://github.com/ElsevierSoftwareX/SOFTX-D-20-00072.

## Contact
If you have any questions, please don't hesitate to contact zhongrui[at]iic.hokudai.ac.jp
