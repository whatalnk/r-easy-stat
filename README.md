# r-easy-stat
## About
『[Rによるやさしい統計学](http://shop.ohmsha.co.jp/shopdetail/000000001781/)』（オーム社）のnotebooks

## Rを[Jupyter notebook](http://jupyter.org/) で使う

* Rのインストール
* Pythonのインストール
  * [Miniconda](http://conda.pydata.org/miniconda.html) をインストールする
* Jupyter インストール
  * コマンドプロンプト（Macの人はTerminal等）から
```
conda install jupyter
```
* [IRkernel](http://irkernel.github.io/)インストール
  * R を起動して，
```
install.packages(c('repr', 'pbdZMQ', 'devtools')) 
devtools::install_github('irkernel/IRdisplay')
devtools::install_github('irkernel/IRkernel')
IRkernel::installspec()
```
* 起動
  * コマンドプロンプト（or Terminal）から，
```
jupyter notebook
```
