My notes from reading javascript tutorials from W3 schools. https://www.w3schools.com/js/default.asp

These notes are scattered so proceed with caution

JavaScript is primarily used to program the behavior of web pages. We can use it to change the HTML that is displayed to us.
Typically we can see the javascript inserted within the HTML when we inspect a pages source using f12, this is contained within ```<script> </script>```. We can also find JavaScript contained in external files that are referred to, these files
end in .js, and we can refer to them in the html using src like so: ```<script src="myScript.js"></script>``` Along with that, we can also reference external js code.
by refering to a link that goes to js code or a file path to js code. 

To see the output/result of js code, we can use an html element, html output, alert boxes, or the browser console. (What is an HTML element? it is a part or section of the html that makes up a certain part of what we see, like a paragraph 
or maybe a header, it is made up of two tags, with the contwnt in the middle, so ```<p>This is paragraph content.</p>``` is an element and we use the tags p to know this is a paragraph, and the content inside is what makes up the paragraph,
we use multiple html elements to make up an html document, elements can also be "nested" or put inside each other) There is a method called innerHTMl that js will use to change the contents of an html element, and to access this element we
want to change we use document.getElementById(id), so here: 
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "<h2>js changed me from a blank element to this</h2>";
</script>
```
We reference the id of the paragraph element and change its contents, and we will see this change displayed to us. If we want to change just the text of an element we can use innerTEXT too. There is also document write, this will write to
html but it should be used with caution because if it is used after a page is loaded it gets rid of all the other html. Using window.alert or alert will show a popup of some output. console.log() can also display output in the console in the
browser, usually for debugging. 

Separate statements with ;

A variable defined with const cant be assigned a new value.

In js there are two types of values, fixed (wont change) and variable (can change). Fixed values are hard coded, or directly writen in the code, variables are declared, and hold whatever they are assigned. Use var and let to create variables. Any variable declered with const doesnt chabge its asssigned value. 

Js has 8 data types: string, number, Bigint, Boolean, Undefined, Null, Symbol, Object. An object can be built-in (objects, arrays, dates, maps, sets, intarrays, floatarrays, promises, etc.) or user defined. Js types are dynamic so one variable can hold different types, if it was static, the type of variable needs to be known at runtime but js is dynamic. Bigint stores higher numbers than the normal integer value. Objects are written in curly braces {}. An undefined variable has no value. You can empty a variable by setting it to undefined. 

To define an object, you can use an object literal, the new keyword, or a constructor. A literal is a list of key:values in curly braces. If you use the new keyword you create a new object, and then the object has data added to it after its creation. To access an objects property use object.property or object["property"]. Using "this" in an object references the object itself so if you see this.name in person its refering to person.name. Objects are containers for properties and methods, in js almost everything is an object. All values but primitives are objects. A primitive value has no properties or methods, this can be string number bool null undefined symbol or bigint. Objects are mutable so they can be changed. They are also passed by reference not value. This means an object assigned to two variables is not stored twice in memory as a copy for each variable, instead the two variables hold the address to the object in memory. Delete keyword deletes a property from an object. Nested objects means object inside an object. To access this nested object do family.pets.dog. Use constructors to create objects of the same type, this is a function. 

A constructor function looks like: 
```
function Person(name, age) {
this.name = name;
this.age = age;
}
```
"this" has no value, the value of "this" will become the new object when a new object is created.

Then use the new keyword to make a new object:
```
const personWritingThis = new Person("Jarrett", "21");
```
If you want to add a property to a constructor you add it to the constructor function prototype.

In HTML events are things that happen to elements, js can react to these events. Common events: onchange if an element was changed, onclick if an element was clicked, onmouseover if the user has their mouse over an element, onmouseout if the users mouse moves away from an element, onkeydown if a keyboard key is pressed, and onload when a browser finishes loading a page. 

Template strings are special strings defined with ` quotes that can contain quotes, and take variables and interpolate them. Interpolation is the insertion of something of a different nature into something else. They can also take in expressions and evaluate them in the string. 

JavaScript numbers are always stored as double precision floating point numbers, following the international IEEE 754 standard. Some integers round incorrectly if they are too big. Safe integers are all integers from -(2^53 - 1) to +(2^53 - 1). 

For comparisons,== is equal to, === is equal value and type, != is not equal, !== is not equal value or type. The ?? operator returns the first argument if it is not nullish (null or undefined). Otherwise it returns the second argument.

Use for in to loop through the properties of an object, use for of to loop through the properties of an iterable object.

A JavaScript Set is a collection of unique values. Each value can only occur once in a Set. The values can be of any type, primitive values or objects. If you try adding duplicate values only the first instance will be added. A js map is a data structure for storing key-value pairs with flexible key types and insertion order preservation. It is like an object but it maintains order of insertion and can have the key be any type. Typed Arrays handle binary data, they hold fixed length of data, they are very fast. 

Iterating means looping over a sequence of elements. An Iterator is an object that provides a standard way to access elements sequentially. An Iterator must adheres to the Iterator Protocol: It must have a next() method. The next() method returns an object with two properties:

  The value property holds the next value in the iteration sequence.
  The done property returns false if there are more elements to iterate over, otherwise it returns true.

Empty an object by setting it to Null. Undefined and null are the smae value but undefined is of type undefined and Null is of type object. Destructuring is unpacking object properties into variables. Regular expressions are characters that form a search pattern. The syntax for using them is ```/pattern/modifier flags; ```. Im not getting into the specifics because i can always come back to the module. 

With operator precedence, operations with the same precedence (like * and /) are computed from left to right. Python and js handle errors similarly, try = try except = catch finally = finally raise = throw. Python is generally stricter and has more built in errors, and Java script is more dynamic and can have more surprises. Js returns an error object with name and message. 

With JavaScript, the global scope is the JavaScript environment.

In HTML, the global scope is the window object.

Hoisting in JavaScript is a behavior where variable and function declarations are moved to the top of their scope (either the global scope or function scope) before code execution, this is done by default. JavaScript only hoists declarations, not initializations, so you can use a variable before its declaration but if you use a variable before initialization you get an error, if the variable is made with let and const they are hoisted but unlike with var they aren’t able to be used before declaration. When coding in js its good practice to declare all variables at the top to avoid unexpected behavior and stick with the default. 

Js can be executed in struct mode with ```"use strict";```. It wont let you use undeclared variables. When doing use strict, it applies to the scope its declared in. Strict mode transforms acceptible bad syntax to real errors. In strict mode, ```this``` refers to the object that called the function. If the object is not specified strict mode returns undefined and normal mode returns the global object. 

In js use ```class``` to create a class and always add a method named ```constructor```. A js class is not an object, its a template for js objects. A class uses a prototype under the hood, its just cleaner syntax. Js modules let code be broken into different files.

Js modules let you break up your code into different files. There are two ways (there are more than two but for simplicity 2) to share code between files. One way is modules and another is using ```src =```. The difference between the two is that modules can have certain parts explicitly exportable to be used elsewhere or otherwise have parts in a private scope. Using ```src =``` puts everything in that code in the global scope. When you import from a module you can only import things that are explicitly able to be exported. With src = you get everything. Use modules for encapsulation, selective imports, and scalability. Use src equals for smaller projects. Codebase maintenance refers to the ongoing process of keeping a software project's source code in a functional, efficient, and adaptable state. Separate files can simplify maintaining a code base. In the script tag modules must have ```type = module```. Modules only work with the http(s) protocol because using file:// could compromise security and reach system files.  

Scope determines the accessibility of variables, objects, and functions from different parts of the code. Java script scopes originally covered just functions and global. Now there is also block scope which is when a variable is declared in an object/block. Block scope can be used with ```let``` and ```const``` but not ```var```. In JavaScript, objects and functions are also variables. If you assign a value to a variable that has not been declared, it will automatically become a GLOBAL variable (Unless you are in strict mode). With JavaScript, the global scope is the JavaScript environment. In HTML, the global scope is the window object. Global variables defined with the var keyword belong to the window object. Global variables defined with the let keyword do not belong to the window object. The lifetime of a JavaScript variable starts when it is declared. Function (local) variables are deleted when the function is completed. In a web browser, global variables are deleted when you close the browser window (or tab). Parameters in functions are local to the function. Pay attention to where the variable is declared to know the scope. 

Searching for (and fixing) errors in programming code is called code debugging. This can report errors and set breakpoints to examine variables at certain points in execution. The debugger keyword stops the execution of JavaScript, and calls (if available) the debugging function. This has the same function as setting a breakpoint in the debugger.

Always use 2 spaces for indentation of code blocks. Do not use tabs (tabulators) for indentation. Different editors interpret tabs differently. Hyphens can be mistaken as subtraction attempts. Hyphens are not allowed in JavaScript names. Use simple syntax for loading external scripts (the type attribute is not necessary): ```<script src="myscript.js"></script>```. If possible, use the same naming convention (as JavaScript) in HTML. Avoid global variables, avoid new, avoid ==, avoid eval(). Global varbiables should be minimized because global variables and functions can be overwritten by other scripts.All variables used in a function should be declared as local variables. Local variables must be declared with the var, the let, or the const keyword, otherwise they will become global variables. Declaring objects with const will prevent any accidental change of type. 

Plus sign does both adding and concatenation. For whatever reason if you put a semi colon at the end of an if statement like ```if (x==5);``` will evaluate as true even if x = 9. Each statement in a loop, including the for statement, is executed for each iteration of the loop. Statements or assignments that can be placed outside the loop will make the loop run faster. So ```for (let i = 0; i < arr.length; i++) {``` is slow compared to ```let l = arr.length; for (let i = 0; i < l; i++) {```. Accessing the HTML DOM is very slow, compared to other JavaScript statements. If you expect to access a DOM element several times, access it once, and use it as a local variable like this ```const obj = document.getElementById("demo"); obj.innerHTML = "Hello";```. Keep the number of elements in the HTML DOM small. Putting your scripts at the bottom of the page body lets the browser load the page first. The defer attribute specifies that the script should be executed after the page has finished parsing, but it only works for external scripts. The with keyword is slow.

JavaScript statements start with a statement identifier to identify the JavaScript action to be performed. Statement identifiers are reserved words and cannot be used as variable names (or any other things). (Ex: break, class). 


Continue at js statements reserved


