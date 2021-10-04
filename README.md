# pro_hw2_simulator
To run the simulator you will need to install the pyphysx library.

Instructions for Ubuntu users:
```
conda create --name pro2021 python=3.8
conda activate pro2021
pip install numpy==1.20
pip install git+https://github.com/petrikvladimir/pyphysx.git@master
pip install jupyter notebook
```

Instructions for Windows users:
```
conda create --name pro2021 python=3.8
conda activate pro2021
pip install conan
pip install numpy==1.20
pip install cmake
pip install git+https://github.com/petrikvladimir/pyphysx.git@master
pip install jupyter notebook
```

## Visualize DH paramters of simulation
To visualize run
```python visualize_dh.py ```
The script assumes that you have `hw02.json` as described on homework page.

## To change thetas
Open jupyter notebook. Run all the cells. New window with simulator will open. Now you can change `id_theta` and move the slider.
The script assumes that you have `hw02.json` as described on homework page.
