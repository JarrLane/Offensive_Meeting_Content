My notes from reading javascript tutorials from W3 schools.

JavaScript is primarily used to program the behavior of web pages. We can use it to change the HTML that is displayed to us. (If you dont know what HTML is, it is hypertext markup language, it is what we actually see when using a website)
Typically we can see the javascript inserted within the HTML when we inspect a pages source using f12, this is contained within ```<script> </script>```. We can also find JavaScript contained in external files that are referred to, these files
end in .js, and we can refer to them in the html using src like so: ```<script src="myScript.js"></script>``` Along with that, we can also reference external js code (im going to start saying js instead of JavaScript because its faster) 
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

In js there are two types of values, fixed (wont change) and variable (can change). Fixed values are hard coded, or directly writen in the code, variables are declared, and hold whatever they are assigned. Use var and let to create variables. Any variable declered with const doesnt chabge its asssigned value. 


