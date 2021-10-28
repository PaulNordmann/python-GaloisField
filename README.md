# Galois Field

Generate with a modular polynomial a list of elements representing a Galois Field.

## possible modular polynomals
     111
	 1011
	 10011
	 100101
	 1000011
	 10001001
	 100011101
	 1000010001
	 10000001001
## use case

```git clone git@github.com:PaulNordmann/python-GaloisField.git gf```


```python
from gf import AlphaList;

for a in AlphaList('1011'):
	print a.getAlpha();
```

## operations

```
>>> alphalist = AlphaList('1011');
```
* vector-representation
```
>>> alphalist[0];
001
```
* alpha-representation
```
>>> alphalist[0].getAlpha();
α⁰
```
* addition
```
>>> alphalist[0] + alphalist[1];
011  
```
* multiplication
```
>>> alphalist[0] * alphalist[1];
010
```
* inverse
```
>>> -alphalist[1];
101
```
