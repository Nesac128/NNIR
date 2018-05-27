import os
from nnir.meta.config import external_working_directory_path

if not os.path.exists(external_working_directory_path+'/datasets'):
    os.mkdir(external_working_directory_path+'/datasets')
if not os.path.exists(external_working_directory_path+'/trained_models'):
    os.mkdir(external_working_directory_path+'/trained_models')
if not os.path.exists(external_working_directory_path+'/data'):
    os.mkdir(external_working_directory_path+'/data')
if not os.path.exists(external_working_directory_path+'/training_images'):
    os.mkdir(external_working_directory_path+'/training_images')
if not os.path.exists(external_working_directory_path+'testing_images'):
    os.mkdir(external_working_directory_path+'/testing_images')