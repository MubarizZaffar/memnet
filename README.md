# Memnet

This is a quick implementation and archiving of "Understanding and Predicting Image Memorability at a Large Scale, Khosla et al., ICCV 2015." It is a model useful for predicting the memorability score of an image, which could be used for selecting which images to store in a localization database for example.

See example usage for this application in "Memorable Maps: A Framework for re-defining Places in Visual Place Recognition, Zaffar et al., T-ITS, 2022."

While the inference code (feel free to use ofc) is written by the author; all credits and rights for the development of Memnet are with Khosla et al. Please cite accordingly. Since their original webpage [http://memorability.csail.mit.edu/] is not accessible anymore, I am archiving the model here for any potential future user.

       
    python3 -m venv memnet_env
    
    source memnet_env/bin/activate
    
    pip install -r requirements.txt
    
    python3 memnet.py 

Citatations:
      @inproceedings{khosla2015understanding,
      title={Understanding and predicting image memorability at a large scale},
      author={Khosla, Aditya and Raju, Akhil S and Torralba, Antonio and Oliva, Aude},
      booktitle={Proceedings of the IEEE international conference on computer vision},
      pages={2390--2398},
      year={2015}
    }

    @article{zaffar2020memorable,
      title={Memorable maps: A framework for re-defining places in visual place recognition},
      author={Zaffar, Mubariz and Ehsan, Shoaib and Milford, Michael and McDonald-Maier, Klaus D},
      journal={IEEE Transactions on Intelligent Transportation Systems},
      volume={22},
      number={12},
      pages={7355--7369},
      year={2020},
      publisher={IEEE}
    }

