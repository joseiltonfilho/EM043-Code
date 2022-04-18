# EM043-Code
To run this code, please run the `run-EM043.sh` script with :

```bash
cd ~ && \
apt update && \
cd ~/EM043-Code/
chmod u+x run-EM043.sh
./run-EM043.sh
```

Please note that the python version of this project is `3.6`, not `3.7` as originaly from [Ubuntu 18 image](http://download.terasic.com/downloads/cd-rom/de10-nano/AzureImage/DE10-Nano-Cloud-Native_18.04.zip). Check your version by command:
```bash
python3 --version
```
For image processing at the EDGE with Azure connection, please downgrade and follow the [step-by-step](https://github.com/joseiltonfilho/EM043-Code/blob/main/step-by-step.md) proceedures. A Jupyter Notebook for the image and video processing (offline) is presented [here](https://github.com/joseiltonfilho/EM043-Code/blob/main/HPS_INTEL_De10nano.ipynb). To run in DE10nano, use virtual env or install jupyter using 'pip3 from python3.6'.
