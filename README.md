# launchchess-python

Play chess on a Launchpad with python!

## install
Installation is optional, and can be skipped if you just want to run the file directly.
### pip
`pip3 install launchchess-python`

### local
`git clone https://github.com/quaternionmedia/launchchess-python.git`

`cd launchchess-python`

`pip3 install -r requirements.txt`

`pip3 install launchchess-python/`

## config
Download a [UCI](https://en.wikipedia.org/wiki/Universal_Chess_Interface) compatible chess engine, such as the [free stockfish engine](https://stockfishchess.org/download/).

Edit `config.py` to include the path to this file:

`STOCKFISH='./stockfish_20090216_x64_avx'`

### pieces
Visit [scad-chess](https://github.com/quaternionmedia/scad-chess) for a free 3D printable chess set, which can be printed at any scale, in any color!

## run
Plug in your Launchpad and run:
`python3 launchchess/launchchess.py`

Select your midi device, and begin playing!
