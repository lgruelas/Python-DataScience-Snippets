# remove old versions of the library
pip uninstall -y pystatslearn
rm -rf pystatslearn/Pystatslearn.egg-info
rm pystatslearn/pystatslearn/__init__.pyc

#install the library
cd pystatslearn
pip2 install -e .