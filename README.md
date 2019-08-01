## Installation

```
$ pip install git+https://github.com/ushitora/bwt
```

or clone this repository and run `pip install`

```
$ git clone git@github.com:ushitora/bwt.git
$ pip install -e bwt
```


## Usage

```python
import bwt

# Bullows-Wheeler transform of the string 'abracadabra'
# --> ('rdarcaaaabb', 2)
bwt.bwt('abracadabra')

# Bullows-Wheeler transform of the string 'abracadabra'
# --> 'ardrcaaaabb'
bwt.bijective_bwt('abracadabra')
```
