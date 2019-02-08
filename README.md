# LR-1-parser-in-Python-Closure-and-Parse-table-
A implementation of LR(1) Parser or CLR Parser in Python3.

**input(edit in line number 268)**


```^::=S$',
    'S::=CC',
    'C::=cC',
    'C::=d'
 ```

**Output**>>
```
	{'0+S': 'shift 2', '0+C': 'shift 3', '0+c': 'shift 10', '0+d': 'shift 8',
	 '1+d': 'reduce C::=d', '1+c': 'reduce C::=d', '2+$': 'reduce ^::=S', '3+C': 'shift 6', 
	 '3+c': 'shift 7', '3+d': 'shift 5', '4+C': 'shift 12', '4+c': 'shift 10', '4+d': 'shift 8', 
	'5+$': 'reduce C::=d', '6+$': 'reduce S::=CC', '7+C': 'shift 11', '7+c': 'shift 7', 
	'7+d': 'shift 5', '8+d': 'reduce C::=d', '9+d': 'reduce C::=cC', '9+c': 'reduce C::=cC', 
	'10+C': 'shift 12', '10+c': 'shift 10', '10+d': 'shift 8', '11+$': 'reduce C::=cC', '12+d': 'reduce C::=cC'}
  ```
  '
	(Contents Of Parsing Table)
	where an entry,
	5+$: 'reduce C::=d' represents reduction in state 5 , under $ symbol from d to C.

```
	State  0
	[['^::=.S$'], ['S::=.CC$'], ['C::=.cCd'], ['C::=.cCc'], ['C::=.dd'], ['C::=.dc']]
	*********************
	State  1
	[['C::=d.d'], ['C::=d.c']]
	*********************
	State  2
	[['^::=S.$']]
	*********************
	State  3
	[['S::=C.C$'], ['C::=.cC$'], ['C::=.d$']]
	*********************
	State  4
	[['C::=c.Cd'], ['C::=c.Cc'], ['C::=.cCd'], ['C::=.dd']]
	*********************
	State  5
	[['C::=d.$']]
	*********************
	State  6
	[['S::=CC.$']]
	*********************
	State  7
	[['C::=c.C$'], ['C::=.cC$'], ['C::=.d$']]
	*********************
	State  8
	[['C::=d.d']]
	*********************
	State  9
	[['C::=cC.d'], ['C::=cC.c']]
	*********************
	State  10
	[['C::=c.Cd'], ['C::=.cCd'], ['C::=.dd']]
	*********************
	State  11
	[['C::=cC.$']]
	*********************
	State  12
	[['C::=cC.d']]
	*********************
  ```

