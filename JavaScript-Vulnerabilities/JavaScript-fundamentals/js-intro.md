My notes from reading javascript tutorials from W3 schools.

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

Continue at js template strings


