```
function *foo(x) {
	var y = x * (yield "Hello");	// <-- yield a value!
	return y;
}

var it = foo( 6 );

var res = it.next();	// first `next()`, don't pass anything
console.log(res.value);				// "Hello"

res = it.next( 7 );		// pass `7` to waiting `yield`
res.value;
```

```
function *foo2(x) {
	var y = x * (yield "Hello");	// <-- yield a value!
	return y;
}

var it = foo2( 6 );   // 6 will be discarded

var res = it.next(7);	
console.log(res.value);			
res=it.next(8)
res.value
```
```
var a = 1;
var b = 2;

function *foo() {
	a++;
  console.log(a)
	yield;
	b = b * a;
  console.log(b)
	a = (yield b) + 3;
  console.log(a,b)
}
function *bar() {
	b--;
	yield;
	a = (yield 8) + b;
	b = a * (yield 2);
}
function step(gen) {
	var it = gen();
	var last;

	return function() {
		// whatever is `yield`ed out, just
		// send it right back in the next time!
		last = it.next( last ).value;
	};
}

var s1=step(foo)
var s2=step(bar)
s2();		// b--;
s2();		// yield 8
s1();		// a++;
s2();		// a = 8 + b;
			// yield 2
s1();		// b = b * a;
			// yield b
s1();		// a = b + 3;
s2()
console.log(a,b)

var it=foo()
console.log(it.next().done)
console.log(it.next().done)
console.log(it.next().done)
console.log(it.next().done)
console.log(it.next().done)

```
```
var something = (function(){
	var nextVal;

	return {
		// needed for `for..of` loops
		[Symbol.iterator]: function(){ return this; }, // for (var v of something)...

		// standard iterator interface method
		next: function(){
			if (nextVal === undefined) {
				nextVal = 1;
			}
			else {
				nextVal = (3 * nextVal) + 6;
			}

			return { done:false, value:nextVal };
		}
	};
})();

something.next().value;		// 1
something.next().value;		// 9
something.next().value;		// 33
something.next().value;		// 105
for (v of something){
  console.log(v)
  if (v>500) break
}

```

function *foo(){
  console.log("seg 1")
  var y=yield " inner message one"
  console.log("seg 2")
  yield y+' inner message two'
  console.log("seg 3")
  return 8
}

var it=foo()
console.log(it.next("ext message 1").value)
console.log(it.next("ext message 2").value)
console.log(it.next("ext message 3").value)
