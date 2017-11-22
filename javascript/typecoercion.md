## javascript types
1. null
2. undefined
4. boolen
5. number
3. string
6. object
7. symbol

## ToString
String(.)
* null --> "null"
* undefined --> "undefined"
* false --> "false"
* 123 --> "123", 1.07*1000*1000*1000*1000*1000*1000*1000 --> "1.07e21"
* object : use toString
  * {a:1} --> "[object Object]"
  * [1,2,3] --> "1,2,3"
  * var x={a:1}; x.toString=function(){return "HaHa"}; x--> "HaHa"

## ToNumber
Number(.)
* null --> 0
* undefined --> NaN
* false --> 0, true --> 1
* "345" --> 345, "34A" --> NaN, "1e43" --> 1e+43, "" --> 0
* use valueOf() if value is primitive, otherwise toString()
  * [] --> "" -->0
  * ["abc"] --> "abc" --> NaN

## ToBoolean
Boolean(.)
### Falsy Valies
* null
* undefined
* false
* +0, -0, NaN
* ""

## Parsing Numeric Strings
parseInt is used to parse string.
* parseInt("42A") //42
* Number("42A")  // NaN
* parseInt(1/0,19)  // 1/0 --> infinity --> "infinity" --> "i" -->18
* parseInt(1/0)   // 1/0 --> infinity --> "infinity" --> NaN

## + algorithm
[1,2]+[3,4] --> "1,23,4"

```According to ES5 spec section 11.6.1, the + algorithm (when an object value is an operand) will concatenate if either operand is either already a string, or if the following steps produce a string representation. So, when + receives an object (including array) for either operand, it first calls the ToPrimitive abstract operation (section 9.1) on the value, which then calls the [[DefaultValue]] algorithm (section 8.12.8) with a context hint of number.```

[]+{} --> ""+"[object Object]" --> "[object Object]"

{}+[] --> 0 (Why ? See Blocks)

## Loose Equals
ES5 spec 11.9.3

11.9.3.1 If the two values being compared are of the same type, they are simply and naturally compared via Identity as you'd expect`. For example, 42 is only equal to 42, and "abc" is only equal to "abc".
  * NaN is never equal to itself
  * +0 and  -0 are equal to each other
  * [1]==[1]  // false
  * {} == {}  //false

11.9.3.4:
If Type(x) is Number and Type(y) is String, return the result of the comparison x == ToNumber(y).

11.9.3.5: If Type(x) is String and Type(y) is Number, return the result of the comparison ToNumber(x) == y`.
  * 3 =="3" // --> 3 == 3 --> true 

11.9.3.6: If Type(x) is Boolean, return the result of the comparison ToNumber(x) == y. 

11.9.3.7: If Type(y) is Boolean, return the result of the comparison x == ToNumber(y).
  * 3 == true // --> 3 == 1 --> false

11.9.3.2: If x is null and y is undefined, return true. 

11.9.3.3: If x is undefined and y is null, return true.`
  * null == undefined // true

11.9.3.8: If Type(x) is either String or Number and Type(y) is Object, return the result of the comparison x == ToPrimitive(y). 

11.9.3.9: If Type(x) is Object and Type(y) is either String or Number, return the result of the comparison ToPrimitive(x) == y.`
  * 42 == [42] // --> 42 == "42" --> 42 == 42 --> true
  * "42" == [42] // --> "42" == "42" --> true

## False compariosn
* "0" == null  // false
* "0" == undefined // false
* "0" == false // (r67)--> "0" == 0 --> 0 ==0  --> true
* "0" == NaN // false
* "0" == 0 // (r45)--> 0 == 0 --> true
* "0" == "" // r1 --> false
* false == null // r67-> 0==null --> false
* false== undefined // r67 --> 0 == undefined --> false
* false == NaN // r67-> 0==Nan -->false
* false ==0 // r67 --> 0==0 -> true
* false == "" // r67 --> 0=="" r45--> 0==0 -> true
* false==[] // r67-->0==[] r89-->0=="" r45-->0==0-->true
* false=={} // r67-->0=={} r89-->0=="[object Object]" r45-->0==NaN-->false
* ""==null  //false
* ""==undefined //false
* ""==Nan //false
* ""==0 //r45-->0==0-->true
* ""==[] //r89-->""==""-->true
* ""=={} //r89-->""=="[object Object]"-->false
* 0==null // false
* 0==undefined //false
* 0==false //r67-->0==0-->true
* 0==Nan //false
* 0==[] //r89-->0==""-->0==0-->true
* 0=={} //r89-->0=="[object Object]"-->0==NaN-->false
* []==![] // -->[]==false r67-->[]==0 r89-->""==0 r45-->0==0-->true

## Safely using implicit coercion
1. If either side of the comparison can have true or false values, don't ever, EVER use ==.
2. If either side of the comparison can have [], "", or 0 values, seriously consider not using ==.

## Abstract Relational Comparison
`<` and `>`

Es5 11.8.5 The algorithm first calls ToPrimitive coercion on both values, and if the return result of either call is not a string, then both values are coerced to number values using the ToNumber operation rules, and compared numerically.

* `a <= b` is equivalent ot `!(a>b)`

* `a >= b` is equivalent ot `!(a<b)`
```
var a = { b: 42 };
var b = { b: 43 };

a < b;	// false
a == b;	// false
a > b;	// false

a <= b;	// true
a >= b;	// true
```