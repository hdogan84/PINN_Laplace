Physics-informed neural networks
==============================
In this repository, a PyTorch implementation for the solution of Laplace equation is presented.
THis will be extended to Helmholtz equation in near future. 
Project Organization on Github
------------

    ├── LICENSE
    ├── README.md          --> This readme file
    ├── data               -->   
    │   │                      
    │   └── Laplace_datasets --> 
    │
    ├── models             --> The models produced by the notebook code.
    │   └── DL_Models      --> Deep Learning Models
    │
    ├── notebooks          --> Jupyter notebooks.
    │   └── result_files   --> helper files to build the figures.
    │
    ├── references         --> The references we used for the project.
    │
    ├── reports            --> Our created reports (.pdf) or summary 
    │   │                      
    │   └── figures        --> Figures and classification  
    │                          reports.
    │
    ├── requirements.txt   --> The requirements to run the Notebooks
    │
    └── src                --> This folder is practically not used right now.  


## How to use the Github repo / the notebooks

1. Notebook1: Data generation, Data Vizualization and Preprocessing:
A square domain with length=1, i.e. [0, 1] x [0, 1], is considered in the solutions. 
Other geometry configurations can be handled via coordinate transformation 

2. Notebook2: This is a playground script to implement custom gradient calculations and to visualize tensor gradients etc.  

3. Notebooks 3a / 3b: Deep learning models. Notebook 3a will deal with the Helmholtz problem where as notebook 3b implements the Laplace equation, including model building, hyperparameter choices train-test loops and a final visualization of the analytical solution vs. PINN solution. 
Currently, implemented architecture is ANN. Other model options will be tried. 

