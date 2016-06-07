# r-easy-stat
## About
『[Rによるやさしい統計学](http://shop.ohmsha.co.jp/shopdetail/000000001781/)』（オーム社）のnotebooks

## 目次
第I部

* [1章](http://whatalnk.github.io/r-easy-stat/Chap01.html)  
    * [hawks.csv](https://github.com/whatalnk/r-easy-stat/raw/master/hawks.csv)
    * [varp.r](https://github.com/whatalnk/r-easy-stat/raw/master/varp.r)
* [2章](http://whatalnk.github.io/r-easy-stat/Chap02.html)  
* [3章](http://whatalnk.github.io/r-easy-stat/Chap03.html)  
    * [Chap03_food.xlsx](https://github.com/whatalnk/r-easy-stat/raw/master/Chap03_food.xlsx)
* [4章](http://whatalnk.github.io/r-easy-stat/Chap04.html)  
* [5章](http://whatalnk.github.io/r-easy-stat/Chap05.html) 
    * [teaching_methods.csv](https://github.com/whatalnk/r-easy-stat/raw/master/teaching_methods.csv)
* [6章](http://whatalnk.github.io/r-easy-stat/Chap06.html)  
* [7章](http://whatalnk.github.io/r-easy-stat/Chap07.html)    
    * [chap07_2.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_2.csv)
    * [chap07_3.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_3.csv)
    * [chap07_ex1.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_ex1.csv)
    * [chap07_ex2.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_ex2.csv)  
...

## Macで日本語を含んだcsvファイルを読み込んだ時にfileEncodingを正しく指定しても文字化けする場合
* [osx - Installing R on Mac - Warning messages: Setting LC_CTYPE failed, using "C" - Stack Overflow](http://stackoverflow.com/questions/9689104/installing-r-on-mac-warning-messages-setting-lc-ctype-failed-using-c)

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
