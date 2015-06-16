git clone https://github.com/CIFASIS/VDiscover.git
cd VDiscover
./setup.py install --user
cd ..

git clone https://github.com/CIFASIS/ManFuzzer.git
cd ManFuzzer
./setup.py install --user
cd ..

echo "VDiscover and ManFuzzer should be installed now"
echo "Do not forget to add ~/.local/bin to your PATH"
